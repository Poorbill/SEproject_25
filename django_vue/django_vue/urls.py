"""django_vue URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import myapp.urls
import myapp.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(myapp.urls)),
    url(r'^captcha/', include('captcha.urls')),  # 这是生成验证码的图片
    url(r'^$',myapp.views.login),
    # url(r'^$',TemplateView.as_view(template_name="index.html")),
    url(r'^login-action$', myapp.views.login_action ),
    url(r'^minsheng_submit$', myapp.views.minsheng_submit),
    url(r'^minsheng_query$', myapp.views.minsheng_query),
    url(r'^index_minsheng.html$', TemplateView.as_view(template_name="index_minsheng.html")),
    url(r'^aboutus.html$', TemplateView.as_view(template_name="aboutus.html")),
    url(r'^contact.html$', TemplateView.as_view(template_name="contact.html")),
    url(r'^quiry_result.html$', TemplateView.as_view(template_name="quiry_result.html") ),
    url(r'^services.html$', TemplateView.as_view(template_name="services.html") ),
    url(r'^Submit_succes.html$', TemplateView.as_view(template_name="Submit_success.html") ),
    url(r'^quiry_byphone.html$', TemplateView.as_view(template_name="quiry_byphone.html") ),
    url(r'^minsheng_query_phone_num$', myapp.views.minsheng_query_phone_num),
]
