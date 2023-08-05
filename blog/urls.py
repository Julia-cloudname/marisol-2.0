from django.urls import path
from .views import PostList, PostDetail, BookingView, SuccessView, UserProfileView, ChangeBookingView, EditBookingView, DeleteBookingView

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('success_page/', SuccessView.as_view(), name='success_page'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('edit_booking/', EditBookingView.as_view(), name='edit_booking'),
    path('delete_booking/', DeleteBookingView.as_view(), name='delete_booking'),
]
