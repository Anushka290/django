from unicodedata import name
from django.urls import URLPattern, path
from . import views
urlpatterns =[
    path('',views.home,name='home'),
    path('table',views.table,name='table'),
    path('create',views.createe,name='create'),
    path('update_order/<int:pk>', views.updateOrder, name='updateOrder'),
]
app_name ='demo'