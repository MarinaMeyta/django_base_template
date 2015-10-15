from django.conf.urls import include, url
from django.contrib import admin

from bt_app.views import add_object

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bt_app.views.home_page', name='home'),
    url(r'^objects/', 'bt_app.views.objects_page', name='objects'),
    url(r'^about/', 'bt_app.views.about_page', name='about'),

    #url(r'^add_person/$', 'bt_app.views.add_person', name='add_person'),
    url(r'^add_object/$', add_object, name='add_object'),
]
