from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('category/<int:category_id>/',
         category_page_view,
         name="category_page"),
    path('about_us/', about_us_page_view, name="about_us"),
    path('our_team/', our_team_page_view, name="our_team"),
    path('services/', services_page_view, name="services"),

    path('article/<int:article_id>/', article_detail_page_view,
         name="article_detail"),

    path('add_article/', add_article_view, name='add_article'),
    path('register/', register_user_view, name="register"),
    path('login/', login_user_view, name="login"),
    path('logout/', logout_user_view, name="logout"),

    path('search/', search_view, name="search"),

    path('update_article/<int:article_id>/',
         update_article_view, name="update_article"),
    path('delete_article/<int:article_id>/',
         delete_article_view, name="delete_article"),
    path('profile/<int:user_id>/', check_profile, name="profile"),
    path('edit_profile/<int:user_id>/', update_profile_view,
         name="edit_profile"),
]
