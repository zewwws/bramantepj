from django.contrib import admin

from .models import ContactRequest, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'material', 'order', 'is_published']
    list_editable = ['order', 'is_published']
    list_filter = ['category', 'material', 'is_published']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name', 'short_description']


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'product', 'created_at', 'is_handled']
    list_editable = ['is_handled']
    list_filter = ['is_handled', 'product']
    search_fields = ['name', 'phone', 'email', 'message']
    readonly_fields = ['created_at']


admin.site.site_header = 'Bramante — administrare'
admin.site.site_title = 'Bramante'
admin.site.index_title = 'Conținutul site-ului'
