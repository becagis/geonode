## Config
Add Below lines to geonode/urls.py

# becagis module
urlpatterns += [
    url(r'^api/becagis/', include('geonode.becagis.urls')),
]