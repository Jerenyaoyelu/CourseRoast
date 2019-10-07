"""myproject URL Configuration

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
from django.urls import path
from django.conf.urls import url

from boards import views
from accounts import views as accounts_views

#the order in urlpatterns matters
#because Django matches url following this order,
#and if a url is very permissive, it may never go to the urls below it
urlpatterns = [
    path('admin/', admin.site.urls),#for simpler lookups
    #r'' specifies that the string is a raw string. 
    #'^' signifies the start, and $ marks the end.
    url(r'^$',views.home,name = 'home'),#supports more complex regular expression
    #\d matches [0-9] and other digit characters.
    #'+' signifies that there must be at least 1 or more digits in the number
    url(r'^signup/$',accounts_views.signup,name='signup'),
    url(r'^boards/(?P<pk>\d+)/$',views.board_topics,name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$',views.new_topic,name='new_topic'),

    #1. adding page
    # url(r'^about/$',view.about,name='about'),
    # url(r'^about/company/$',views.about_company,name=about_company),
    # url(r'^about/author/$',views.about_author,name='about_author'),
    # url(r'^about/author/jeren/$',views.about_jeren,name='about_jeren'),
    # url(r'^privacy/$',views.privacy_policy,name='privacy_policy'),
    #2. then create coresponding functions in views.py following the structure below
    # def about(request):
    #     # do something...
    #     return render(request, 'about.html')

    # def about_company(request):
    #     # do something else...
    #     # return some data along with the view...
    #     return render(request, 'about_company.html', {'company_name': 'Simple Complex'})
]
