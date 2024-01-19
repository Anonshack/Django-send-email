from django.urls import path
from main_app.views import send_email

urlpatterns = [
    path('email/', send_email, name='index')
]
