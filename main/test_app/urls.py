from django.conf.urls import url,patterns
from . import views           # This line is new!
admin.autodiscover()

urlpatterns = ['',
    url(r'^$', views.index)     # This line has changed!
    ]
