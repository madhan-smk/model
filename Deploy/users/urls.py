from django.urls import path
from .views import chatbot, home,index, profile, logout_view
from . import views

urlpatterns = [
    path('', home, name='users-home'),
    # path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('logout_view/',logout_view,name='logout_view'),
    path('index/', index, name='users-index'),
    path('Report/',views.Report,name='Report'),
    # path('chatbot/', views.chatbot_response_view,name='chatbot'),
    path('chatbot/', chatbot),
    
    
    
    
    ]


 