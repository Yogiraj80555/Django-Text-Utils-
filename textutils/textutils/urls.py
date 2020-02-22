"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
import django.conf.urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('remove',views.delete,name="remove"),
	path('excel',views.excel,name="Excel Operations"),
	path('anagram',views.anagram,name="Anagram of Word"),
	path('infix',views.infix,name="Infix to Post and Prefix"),
	
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	
	
handler404 = 'textutils.views.errorFun'

handler400 = 'textutils.views.errorFun'

handler403 = 'textutils.views.errorFun'