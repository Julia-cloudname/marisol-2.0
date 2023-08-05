from django.contrib import admin
from django.urls import path, include
from blog.views import PostList, PostDetail, BookingView, SuccessView, UserProfileView, EditBookingView, DeleteBookingView, SuccessDeleteView
from allauth.account.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostList.as_view(), name='home'),
    path('blog/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('success_page/', SuccessView.as_view(), name='success_page'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path("accounts/", include("allauth.urls")),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    path('edit_booking/', EditBookingView.as_view(), name='edit_booking'),
    path('delete_booking/', DeleteBookingView.as_view(), name='delete_booking'),
    path('success_delete_page/', SuccessDeleteView.as_view(), name='success_delete_page'),
]
