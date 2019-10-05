from django.contrib import admin

from .models import SearchQuery

class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('query', 'user')
admin.site.register(SearchQuery,SearchQueryAdmin)