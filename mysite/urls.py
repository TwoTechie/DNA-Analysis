from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('fun1',views.fun1,  name='fun1'),
    path('fun2', views.fun2, name='fun2'),
    path('fun3', views.fun3, name='fun3'),
    path('fun4', views.fun4, name='fun4'),
    path('fun5', views.fun5, name='fun5'),
    path('fun6', views.fun6, name='fun6'),
    path('fun7', views.fun7, name='fun7'),
    path('fun8', views.fun8, name='fun8'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
