from django.contrib import admin
from  .models import Posts,Author, Tag
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Posts, postAdmin)
admin.site.register(Author)
admin.site.register(Tag)