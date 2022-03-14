from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('redirecturl/', views.redirectURL),
    path('inputurl/<str:inputText>', views.acceptInput),
    path('displayhtml/', views.templateHTML),
]
