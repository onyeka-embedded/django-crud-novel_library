from django.contrib import admin
from .models import Novel

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'created')

admin.site.register(Novel, MemberAdmin)
