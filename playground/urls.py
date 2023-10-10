from django .urls import path
from . import views


#URL conf
urlpatterns =[ 
    path('main/', views.say_hello),
    path('handle-form/', views.handle_form, name='handle_form'),
     
]
