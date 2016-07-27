from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'dodaj_slowo/', views.dodaj_slowo, name='dodaj_slowo'),
    url(r'nauka/', views.nauka, name='nauka'),
    url(r'zapisz_odp/', views.zapisz_odp, name='zapisz_odp')
]