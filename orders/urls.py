from django.urls import path
from orders import views


urlpatterns = [
    path('new/', views.order_create.as_view(), name='order_new'),
    path('edit/<id>/', views.order_edit, name='order_edit'),
    path('deliver/<id>/', views.deliver_edit, name='deliver_edit'),
    path('list/', views.order_list, name='order_list'),
    path('search/', views.order_search, name='order_search'),
    path('search_users/', views.order_search_users, name='order_search_users'),
    path('order_query/', views.order_query.as_view(),name='order_query'),
    path('form_query/', views.form_query.as_view(),name='form_query'),
    path('query_search/', views.query_search,name='query_search'),
    path('dates/<str:id_order>/', views.dates, name='dates'),
    path('contact/', views.contact, name='contact'),
]