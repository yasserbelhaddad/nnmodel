from django.urls import path
from api.views import predict, hello

urlpatterns = [
    path('predict/', predict, name='predict'),
    path('', hello, name='hello'),
]
