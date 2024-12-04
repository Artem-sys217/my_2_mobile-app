from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('search/', views.search_action, name='search_action'),
    path('card/<str:tour_name>/', views.tour_detail, name='tour_detail'),
    path('hotels/<int:tour_id>/', views.hotel_list, name='hotel_list'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('login/', views.login_view, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register_view, name='register'),
    path('account/', views.account_info, name='account_info'),
    path('logout/', views.logout_view, name='logout'),
    path('category/<slug:category_slug>/', views.category_tours, name='category_tours'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('office/', views.office_location, name='office_location'),
    path('rating/', views.rating_view, name='rating'), 

]