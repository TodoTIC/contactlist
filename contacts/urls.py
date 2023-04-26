from django.urls import path

from contacts import views

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('new/', views.ContactCreateView.as_view(), name='contact_new'),
    path('<int:pk>/edit/', views.ContactUpdateView.as_view(), name='contact_edit'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
]
