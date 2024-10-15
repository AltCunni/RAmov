from django.urls import path
from .views import submit_review
from .views import index, success

urlpatterns = [
    path('', submit_review, name='index'),
    path('', index, name='index'),
    path('success/', success, name='success')
]



