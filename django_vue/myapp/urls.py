from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = \
    [url(r'add_book$', views.add_book, ),
     url(r'show_books$', views.show_books, ),
     url(r'get_date_event$', views.get_date_event, ),
     url(r'get_date_street$', views.get_date_street, ),
     url(r'getdata_abnormal$', views.getdata_abnormal, ),
     url(r'get_problem_handled$', views.get_problem_handled, ),
     url(r'get_hotcommunity$', views.get_hotcommunity, ),
     url(r'get_abnormal_form$', views.getabnormal_plus, ),
     url(r'get_name$', views.get_name, ),
     url(r'finish_rec_id$', views.finish_rec_id, ),
     ]
