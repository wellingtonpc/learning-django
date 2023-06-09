from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('detail/<int:item_id>', views.detail, name='detail'),
    path('add-item', views.add_item, name='add_item'),
]
