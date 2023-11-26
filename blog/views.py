from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, CallBooking
from django.http import HttpResponseRedirect
from .forms import CallBookingForm, CommentForm
import datetime
from django.urls import reverse
import logging


# Initialize a logger to track events
logger = logging.getLogger(__name__)


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


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Handles booking form rendering and submission
class BookingView(View):
    booking_form = CallBookingForm()

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "booking/booking.html",
            {
                "booking_form": self.booking_form,
            },
        )

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            booking_form = CallBookingForm(request.POST)
        if booking_form.is_valid():
            call_time = request.POST['call_time']
            booking = booking_form.save(commit=False)
            booking.call_time = call_time
            booking.user = request.user
            booking.save()
            return redirect(reverse('success_page'))

        return render(
            request,
            "booking/booking.html",
            {
                "booking_form": booking_form,
            },
        )


# Renders the success page after a successful action
class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'booking/success_page.html')


# Retrieves and displays user's profile data
class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        try:
            last_booking = CallBooking.objects.filter(user=request.user).latest('created_on')
        except CallBooking.DoesNotExist:
            last_booking = None
        return render(request, 'profile.html', {"last_booking": last_booking})


# Handles editing of a booking (requires user login)
class EditBookingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            last_booking = CallBooking.objects.filter(user=request.user).latest('created_on')
            booking_form = CallBookingForm(instance=last_booking)
        except CallBooking.DoesNotExist:
            last_booking = None
            booking_form = CallBookingForm()

        return render(
            request,
            'booking/booking.html',
            {
                "last_booking": last_booking,
                "booking_form": booking_form,
            }
        )

    def post(self, request, *args, **kwargs):
        try:
            last_booking = CallBooking.objects.filter(user=request.user).latest('created_on')
        except CallBooking.DoesNotExist:
            last_booking = None

        if last_booking:
            booking_form = CallBookingForm(request.POST, instance=last_booking)
        else:
            booking_form = CallBookingForm(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('success_page')

        return render(
            request,
            'booking/booking.html',
            {
                "last_booking": last_booking,
                "booking_form": booking_form,
            }
        )


# Handles deletion of a booking (requires user login)
class DeleteBookingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # logger.error("Get")
        try:
            last_booking = CallBooking.objects.filter(user=request.user).latest('created_on')
        except CallBooking.DoesNotExist:
            last_booking = None

        return render(request, 'booking/delete_booking.html')

    def post(self, request, *args, **kwargs):
        # logger.error("Post")
        try:
            last_booking = CallBooking.objects.filter(user=request.user).latest('created_on')
            last_booking.delete()
        except CallBooking.DoesNotExist:
            pass

        return redirect('success_delete_page')


# Renders the success page after a booking is deleted
class SuccessDeleteView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'booking/success_delete_page.html')

# Renders the contact page
class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts.html')

 