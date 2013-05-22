from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('', 
    # ex: /polls/
    #url(r'^$', views.indexx, name='indexx'), 	
    url(r'^$', views.IndexView.as_view(), name='index'),
	
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'), 	
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),	
	
    # ex:  /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	
    # ex: /polls/5/votes
    url(r'^(?P<poll_id>\d+)/votes/$', views.votes, name='votes')    
)