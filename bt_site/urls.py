from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bt_app.views.home_page', name='home'),
    url(r'^about/', 'bt_app.views.about_page', name='about'),
    url(r'^contacts/', 'bt_app.views.contacts_page', name='contacts'),
]
