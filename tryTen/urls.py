"""tryTen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from profiles import views as profiles_views
from contact import views as contact_views
from checkout import views as checkout_views
from blog import views as blog_views
from rest_framework.urlpatterns import format_suffix_patterns
from iteminformation import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^profile/$', profiles_views.userProfile, name='profile'),
     url(r'^checkout/$', checkout_views.checkout, name='checkout'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^postlist/', include('blog.urls')),
    url(r'^stocks/', views.StockList.as_view()),
    

    #url(r'^postlist/$', blog_views.post_list, name='post_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL, document_Root = settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL, document_Root = settings.MEDIA_ROOT)