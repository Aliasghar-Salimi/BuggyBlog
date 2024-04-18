from django.contrib import admin
from .models import articles, Category

# Register your models here.
class articleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug' : ('title',)}

    def category_to_str(self, obj):
        return "، ".join([cat.title for cat in obj.category_published()])

    category_to_str.short_description = 'دسته‌بندی'

admin.site.register(articles, articleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'slug','parent', 'position', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')

admin.site.register(Category, CategoryAdmin)