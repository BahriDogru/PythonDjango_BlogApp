from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe


class BlogAdmin(admin.ModelAdmin):
    list_display=("title","slug") # burada Superadmin ile diğer adminlerin yetkilerini özelleştirebiliyoruz.
    search_fields=("title","category") # burada da admin tarafına bir search bar ekleniyor.
    # readonly_fields = ("description") Burada description alanını sadece okuma modunda açtık. yani admin tarafından da üzerinde değişiklik yapılamaz.
    readonly_fields = ("slug",)

    # def selected_categories(self, obj):
    #     html="<ul>"
    #     for category in obj.categories.all():
    #         html += "<li>" +category.name+ "</li> "
    #     html += "</ul>"

    #     return mark_safe(html) 


# Register your models here.
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
