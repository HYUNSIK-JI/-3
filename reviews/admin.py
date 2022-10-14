from django.contrib import admin
from .models import Review,Comment
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['username']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['user__username']

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)