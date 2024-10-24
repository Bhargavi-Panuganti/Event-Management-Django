from django.urls import path,re_path

from myapp import views
urlpatterns=[
    path('show_venue/<index>',views.show_venue,name='show-v'),
    path('update_venue/<index>',views.update_venue,name='update-v'),
    path('delete_event/<index>',views.delete_event,name='delete-e'),
    path('delete_venue/<index>',views.delete_venue,name='delete-v'),
    path('update_event/<index>',views.update_event,name='update-e'),
    path('venue_list',views.venue_list,name='venue_list'),
    path('<int:year>/<str:month>',views.cal,name='cal'),
    path('',views.cal,name='cal'),
    path('events',views.event_list,name='check'),
    path('venue',views.addVenue,name='add-ven'),
    path('addevent',views.addEvent,name='add-event'),
    path('sayhi/',views.sayhi,name='sayhi'),
    path('bharu/',views.bharu),
    path('temp/',views.temp),
    path('drinks/<str:dish>',views.men),
    path('index',views.index),
    path('venuesList',views.list_venues,name='venues_list'),
    # path('cal/',views.cal),
]