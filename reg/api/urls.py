
from django.conf.urls import url
from .views import RegView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', RegView.as_view(), name='post-userReg'),
]
