from django.urls import path
from . import views
# from sili.views import home, get_response
app_name = 'sili'


urlpatterns = [
    path('', views.home),
    path('get-response/', views.get_response),
]
