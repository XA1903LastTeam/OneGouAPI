import io

from django.core.cache import cache
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from  django.core.files.images import ImageFile
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from UserApp.models import UserModel

from .api import UserSeraLizer

# Create your views here.
# 用户登陆接口,接收用户手机号和模拟短信验证码,登陆成功后将成功登陆的用户ID写入session中，时间设置位关闭连接时清除session

class UserAPIView(View):
    def get(self, request):
        datas = UserModel.objects.all()
        serializer = UserSeraLizer(datas, many=True)
        return JsonResponse({'data': serializer.data })


    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        menu = request.POST.get('menu', None)
        # 用户登陆接口,接收用户手机号和模拟短信验证码,登陆成功后将成功登陆的用户ID写入session中，时间设置位关闭连接时清除session
        if menu == '0':
            phone = request.POST.get('phone', None)
            yan = request.POST.get('yan', None)
            print(yan)
            print(cache.get('yanzhengma'))
            if phone:
                if UserModel.objects.filter(phone=phone).first():
                    if yan == cache.get('yanzhengma'):
                        user = UserModel.objects.filter(phone=phone).first()
                        request.session['user'] = user.id
                        request.session.set_expiry(0)
                        return JsonResponse({'msg': '登陆成功'})
                    else:
                        return JsonResponse({'msg': '验证码错误'})
                else:
                    return JsonResponse({'msg': '该用户未注册'})
            else:
                return JsonResponse({'msg': '手机号错误!'})
        # 用户创建处理函数,使用图片验证码模拟手机验证码注册账号
        elif menu == '1':
            u = UserModel()
            yan = request.POST.get('yan')
            if yan == cache.get('yanzhengma'):
                u.name = request.POST.get('name')
                u.phone = request.POST.get('phone')
                u.sex = int(request.POST.get('sex'))
                u.bool = request.POST.get('bool')
                try:
                    u.save()
                except:
                    return JsonResponse({ 'msg': '数据异常创建失败'})
                else:
                    if request.FILES.get('image'):
                        file_content = ImageFile(request.FILES['image'])
                        default_storage.delete('photo/%s.jpg' % u.id)
                        default_storage.save('photo/%s.jpg' % u.id, file_content)
                        u.image = 'photo/%s.jpg' % u.id
                        try:
                            u.save()
                        except:
                            return JsonResponse({'msg': '图片数据异使用默认头像, 用户创建成功!'})
                    return JsonResponse({ 'msg': '用户创建成功' })

            else:
                JsonResponse({'msg': '验证码错误'})
        else:
            return JsonResponse({'msg': '无效的操作'})

    # 数据更新接口接收用户上传到的数据,获取数据并传入首先需要用户登陆成功,若数据超出限制返回数据异常更新失败
    def put(self, request):
        user = request.session.get('user', None)
        if not user:
            return JsonResponse({'msg': '登陆已经失效'})
        u = UserModel.objects.filter(id=user).first()
        if u:
            u.name = request.POST.get('name') if request.POST.get('name') else u.name
            u.phone = request.POST.get('phone') if request.POST.get('phone') else u.phone
            u.sex = int(request.POST.get('sex')) if request.POST.get('sex') else u.sex
            u.sex = request.POST.get('bool') if request.POST.get('bool') else u.bool
            if request.FILES.get('image'):
                file_content = ImageFile(request.FILES['image'])
                default_storage.delete('photo/%s.jpg' % user)
                default_storage.save('photo/%s.jpg' % user, file_content)
                u.image = 'photo/%s.jpg' % user
            try:
                u.save()
            except:
                return JsonResponse({'msg': '数据异常更新失败'})
            else:
                return JsonResponse({'msg': '数据更新成功'})
        else:
            return JsonResponse({'msg': '用户不存在或'})

    def delete(self, request):
        print('执行删除')
        user = request.session.get('user')
        if user:
           u = UserModel.objects.filter(id=user).first()
           if u:
               u.bool = False
               try:
                   u.save()
               except:
                   return JsonResponse({ 'msg': '数据异常用户注销失败'})
               else:
                   request.session.delete('user')
                   print(request.session.get('user'))
                   return JsonResponse({ 'msg': '用户注销成功'})
           else:
               return JsonResponse({ 'msg': '该用户不存在'})
        else:
            return JsonResponse({ 'msg': '用户未登陆'})
