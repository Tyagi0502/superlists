from django.conf.urls import url
from lists import views as list_views

app_name = 'lists'
urlpatterns = [
	url(r'^(\d+)/$', list_views.view_list, name = 'view_list'),
	url(r'^(\d+)/add_item$', list_views.add_item, name = 'add_item'),
	url(r'^new$', list_views.new_list, name = 'new_list'),
]