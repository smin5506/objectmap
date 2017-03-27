from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
	url(r'^setobstacle/', views.setobstacle),
	#url(r'^insert/(?P<nobjectX>.+);(?P<nobjectY>.+);(?P<nwidth>.+);(?P<nheight>.+);(?P<ndis>.+);(?P<nreliability>.*);', views.Insertobject),
	url(r'^viewobstacle/', views.viewobstacle),
]
