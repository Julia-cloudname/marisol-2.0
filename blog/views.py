from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, CallBooking
from .forms import CallBookingForm, CommentForm
import datetime
from django.urls import reverse


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class BookingView(View):
    def get(self, request, *args, **kwargs):
        booking_form = CallBookingForm()
        available_time_slots = [
            ('09:00', '10:00 AM'),
            ('10:00', '11:00 AM'),
            ('11:00', '12:00 AM'),
            ('12:00', '1:00 PM'),
            ('01:00', '02:00 PM'),
            ('02:00', '03:00 PM'),
            ('03:00', '04:00 PM'),
            ('04:00', '05:00 PM'),
            ('05:00', '06:00 PM'),
            ('06:00', '07:00 PM'),
            ('07:00', '08:00 PM'),
        ]

        return render(
            request,
            "booking.html",
            {
                "booking_form": booking_form,
                "available_time_slots": available_time_slots,
            },
        )

    def post(self, request, *args, **kwargs):
        booking_form = CallBookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return redirect(reverse('success_page'))

        available_time_slots = [
             ('09:00', '10:00 AM'),
            ('10:00', '11:00 AM'),
            ('11:00', '12:00 AM'),
            ('12:00', '1:00 PM'),
            ('01:00', '02:00 PM'),
            ('02:00', '03:00 PM'),
            ('03:00', '04:00 PM'),
            ('04:00', '05:00 PM'),
            ('05:00', '06:00 PM'),
            ('06:00', '07:00 PM'),
            ('07:00', '08:00 PM'),
        ]

        return render(
            request,
            "booking.html",
            {
                "booking_form": booking_form,
                "available_time_slots": available_time_slots,
            },
        )



