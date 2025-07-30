from django.contrib import admin
from .models import Annonce, Category

class AnnoncesAdmin(admin.ModelAdmin):
    list_display = ('id','titre','prix', 'statut', 'description')
    list_filter = ('titre',)
    search_fields = ('titre',)

admin.site.register(Annonce, AnnoncesAdmin)
admin.site.register(Category)
