from django.contrib import admin
from .models import Inventario, Vendedor, Venta

admin.site.register(Inventario)
admin.site.register(Vendedor)
admin.site.register(Venta)

