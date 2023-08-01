from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User 
from .models import Post, Comment, CallBooking
from django_summernote.admin import SummernoteModelAdmin

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('date_joined',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

@admin.register(CallBooking)
class CallBookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'phone_number', 'call_data', 'user')  # Include 'user' in list_display
    list_filter = ('call_date', 'call_time')
    search_fields = ('client_name', 'client_email', 'phone_number')
    date_hierarchy = 'call_date'

