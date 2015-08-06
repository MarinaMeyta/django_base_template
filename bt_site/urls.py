from django.conf.urls import include, url
from django.contrib import admin

from bt_app.views import add_person

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bt_app.views.home_page', name='home'),
    url(r'^people/', 'bt_app.views.people_page', name='people'),
    url(r'^about/', 'bt_app.views.about_page', name='about'),
    url(r'^contacts/', 'bt_app.views.contacts_page', name='contacts'),

    #url(r'^add_person/$', 'bt_app.views.add_person', name='add_person'),
    url(r'^add_person/$', add_person, name='add_person'),
]
