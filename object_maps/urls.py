from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
	url(r'^insert/(?P<id>.+);(?P<objectX>.+);(?P<objectY>.+);(?P<width>.+);(?P<height>.*)', views.Insertobject),
]