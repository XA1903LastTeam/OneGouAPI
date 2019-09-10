"""LastTeamOneGouAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings

urlpatterns = [
                  path('admin/', admin.site.urls),
<<<<<<< HEAD
                  path('goods/', include('Goods.urls', namespace='goods')),
                  path('user/', include('UserApp.urls', namespace='user')),
=======
                  path('goods/', include('Goods.urls', namespace='goods_app')),
                  path('user/', include('UserApp.urls', namespace='user_app')),
>>>>>>> 57b859ac59c4c116f344f6f190f4ebd3e9b0b437
                  path('city/', include('Citys.urls', namespace='city')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
