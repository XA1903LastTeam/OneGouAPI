from django.urls import path

from .views import CategoryView, CatechildView

app_name = 'fun'

urlpatterns = [
    path('category/',CategoryView.as_view(),name='category'),
    path('catchild/',CatechildView.as_view(),name='catchild')
]