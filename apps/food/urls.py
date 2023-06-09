from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('detail/<int:item_id>', views.detail, name='detail'),
    path('add-item', views.add_item, name='add_item'),
    path('update-item/<int:item_id>', views.update_item, name='update_item'),
    path('delete-item/<int:item_id>', views.delete_item, name='delete_item'),
]
