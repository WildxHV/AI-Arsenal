from django.contrib import admin
from .models import Category, AiTool


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'updated_at')
    prepopulated_fields = {'slug': ('category_name',)}
    
class AiToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(AiTool,AiToolAdmin)


