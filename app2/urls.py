from django.urls import path
from app2.views import *

app_name='app2'

urlpatterns=[
    path('charminar/',charminar,name='charminar'),
    path('tajmahal/',tajmahal,name='tajmahal'),
]