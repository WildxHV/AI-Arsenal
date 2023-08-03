from django.contrib import admin
from .models import Category, AiTool, Contact
import admin_thumbnails
from .actions import export_selected_as_csv
 


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'updated_at')
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = Contact.SearchableFields
    list_filter = ('updated_at',)
    actions = [export_selected_as_csv]
    
    
@admin_thumbnails.thumbnail('image')
class AiToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = Contact.SearchableFields
    list_filter = ('updated_at',)
    actions = [export_selected_as_csv]
    

class ContactAdmin(admin.ModelAdmin):
    list_display = ('customer_name','email', 'phone_number', 'is_reviewed', 'is_entertained')
    search_fields = Contact.SearchableFields
    list_filter = ('is_reviewed', 'is_entertained')
    actions = [export_selected_as_csv]
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(AiTool,AiToolAdmin)
admin.site.register(Contact, ContactAdmin)



