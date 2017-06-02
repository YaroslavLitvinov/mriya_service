from django.conf.urls import patterns, url
#from django.conf.urls.defaults import patterns, url
from views import ElfinderConnectorView

urlpatterns = [
    url(r'^yawd-connector/(?P<optionset>.+)/(?P<start_path>.+)/$', ElfinderConnectorView.as_view(), name='yawdElfinderConnectorView'),
]
