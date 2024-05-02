from django.contrib import admin
from .models import articles, Category

# admin.site.disable_action("delete_selected") # this code is used to disabe or delete an action

# Register your models here.


def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='p')
    if updated == 1:
        message_bit = 'منتشر شد'
    elif updated > 1:
        message_bit = 'منتشر شدند'
    modeladmin.message_user(request, f"{updated} مقاله {message_bit}")


def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status='d')
    if updated == 1:
        message_bit = 'پیشنویس شد'
    elif updated > 1:
        message_bit = 'پیشنویس شدند'
    modeladmin.message_user(request, f"{updated} مقاله {message_bit}")
make_published.short_description = "انتشار مقالات انتخاب شده"
make_draft.short_description = "پیشنویس کردن مقالات انتخاب شده"

class articleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag','author', 'slug', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('title',)}
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return "، ".join([cat.title for cat in obj.category.active()])

    category_to_str.short_description = 'دسته‌بندی'

admin.site.register(articles, articleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'slug','parent', 'position', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)