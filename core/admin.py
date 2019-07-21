from django.contrib import admin
from.models import *

# Register your models here.


class CancionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


admin.site.register(Tipo, TipoAdmin)
admin.site.register(Cancion, CancionAdmin)

#biblia
admin.site.register(Book)
admin.site.register(Verse)
admin.site.register(Testament)