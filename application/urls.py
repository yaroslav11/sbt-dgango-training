from django.conf.urls import url
from . import views

app_name = 'app_urls'

urlpatterns = [
    # ex: /application/
    url(r'^$', views.index, name='index'),
    # ex: /application/5/
    # the 'name' value as called by the {% url %} template tag
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /application/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /application/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^mng/$', views.mng, name='mng'),
    url(r'^delete_question/$', views.delete_question, name='delete_question'),
    # url(r'^delete_question/[\S]+$', views.delete_question, name='delete_question'),
]