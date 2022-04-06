from django.urls import path
from . import views
#url Redirection for api Page on project level
urlpatterns = [
    path('callback/', views.callback),
    path('red/', views.red),
    path('test/', views.apitest),
]