from account import views
from django.conf.urls import url

urlpatterns = [
    url(r'^new', views.new_account, name='new_account'),
    url(r'^lock', views.lock_account, name='lock_account'),
    url(r'^unlock', views.unlock_account, name='unlock_account')
]
