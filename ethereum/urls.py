from django.urls import path
from ethereum.views import Get_top_100

urlpatterns = [
    path('', Get_top_100.as_view()),
]
