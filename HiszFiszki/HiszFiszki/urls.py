from django.conf.urls import url, include
from django.contrib import admin
from fiszki import views

urlpatterns = [
    url(r'^fiszki/', include('fiszki.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.welcome, name='welcome')
]