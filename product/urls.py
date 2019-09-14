from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ,name='home'),
    path('create/',views.create,name='create'),
    path('<int:product_id>/details/',views.detail,name='detail'),
    path('upvote/<int:product_id>/',views.upvote,name='upvote'),
]
