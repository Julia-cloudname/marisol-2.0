from django.urls import path
from .views import PostList, PostDetail, BookingView, SuccessView, UserProfileView

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('success/', SuccessView.as_view(), name='success_page'),
    path('profile/', UserProfileView.as_view(), name='profile'), 
]
