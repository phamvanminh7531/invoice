from django.urls import path
from .views import *

urlpatterns = [
    path('check-invoice/<str:code>', check_invoice),
    path('', tool_list_view),
]