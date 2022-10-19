from django.contrib import admin
from .models import Osoba
from .models import Druzyna

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie','nazwisko','miesiac_urodzenia','druzyna']
    list_filter = ['druzyna']
    pass

admin.site.register(Osoba, OsobaAdmin)

class DruzynaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Druzyna, DruzynaAdmin)