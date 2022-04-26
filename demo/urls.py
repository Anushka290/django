from unicodedata import name
from django.urls import URLPattern, path
from . import views
urlpatterns =[
    path('',views.home,name='home'),
    path('table',views.table,name='table'),
    path('create',views.createe,name='create'),
    path('update_order/<int:pk>', views.updateOrder, name='updateOrder'),
    path('delete_order/<int:pk>/', views.deleteOrder, name="delete_order"),
    path('leave/<int:pk>',views.leave,name='leave'),
    

]
app_name ='demo'