"""myplaka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin


from myplakaApp import views as plaka_views

urlpatterns = [

    url(r'ana/$', plaka_views.home, name='home'),

    url(r'^form/$', plaka_views.form_view),
    url(r'^search/$', plaka_views.search_view),
    # url(r'^status/$', plaka_views.bildirim_view),
    url(r'^form2/$', plaka_views.create_plaka),
    url(r'^login/$', plaka_views.login_view),
    url(r'^register/$', plaka_views.register_view),
    url(r'^logout/$', plaka_views.logout_view),

    url(r'admin/', admin.site.urls),

]