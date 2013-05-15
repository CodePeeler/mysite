from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('', 
	# ex: /polls/
	url(r'^$', views.indexx, name='indexx'), 
	# ex: /polls/5/
	url(r'^(?P<p_id>\d+)/$', views.detail, name='detail'), 
	# ex:  /polls/5/results/
	url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
	# ex: /polls/5/vote
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote')
	)