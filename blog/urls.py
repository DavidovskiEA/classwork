from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
    path('product/delete/<str:pk>', ProductDeleteView.as_view()),
    path('product/update/<str:pk>', ProductUpdateView.as_view()),
    path('product/list/<str:pk>', ProductListView.as_view()),
]