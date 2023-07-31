from django.urls import path
from blog.views import PostList, PostDetail, BookingView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('blog/<slug:slug>', PostDetail.as_view(), name='post_detail'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('success_page/', BookingView.as_view(), name='success_page'),
]
