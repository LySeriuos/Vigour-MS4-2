from django.contrib import admin
from .models import Blogs

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    # The tuple that will tell the admin which fields to display.
    list_display = (
        'author',
        'title',
        'content',
        'date',
    )
# sorting products by:

    ordering = (
        'date',
        )