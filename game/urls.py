from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
#	'game.views', 
	url(r'^user/(?P<username>[-\w]+)/$', 'game.views.bookmark_user', name='game_bookmark_user'), 
	url(r'^$', 'game.views.bookmark_list', name='game_bookmark_list'),
	url(r'^create/$', 'game.views.bookmark_create', name='game_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'game.views.bookmark_edit', name='game_bookmark_edit'),
    url(r'^search/$', 'game.views.bookmark_search', name='game_bookmark_search'),

)
