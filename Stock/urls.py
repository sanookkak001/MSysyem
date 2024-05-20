from django.urls import path
from . import views

urlpatterns = [
    path('', views.Stock_info, name='Stock_information'),
    path('Stock_History/<data_id>', views.stock_history_view , name='Stock_History'),
    path('Stock_History_All' , views.Stock_History_All , name='Stock_History_All'),
    path('Add_History' , views.Add_History , name='Add_History')
]
