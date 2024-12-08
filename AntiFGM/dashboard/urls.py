from django.urls import path
from .import views
from .views import edit_profile, profile_view

urlpatterns = [
    path('', views.home, name='home'),
    path('community', views.community_forum, name='community_forum'),
    path('forum/post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create-post', views.create_post, name='create_post'),
    path('forum/post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('reply/<int:post_id>/', views.reply_to_post, name='reply_to_post'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('report/', views.submit_report, name='submit_report'),
    path('report/thankYou/', views.thank_you, name='thank_you'),
    path('report/view/', views.view_reports, name='view_reports'),
    path('events/', views.events_view, name='events'),
    path('groups/', views.support_view, name='groups'),
    path('resources/', views.resources_view, name='resources'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('blogs/', views.blog_view, name='blogs'),
    path('contact/', views.contact_view, name='contact'),
    path('resources/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('search/', views.search, name='search'),
]