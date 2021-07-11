from django.contrib import admin
from  .models import Computer, Portable, Desktop, OS, CPU, Memory, Storage, Graphics


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    pass

@admin.register(Portable)
class PortableAdmin(admin.ModelAdmin):
    list_display = ["Brand", "type", "memory", "cpu","price", "available", "created",
    "updated"]
    list_filter = ['Brand', "type", "memory", "cpu", "price","available", "created",
    "updated"]
    list_editable = ['price', "available"]
    prepopulated_fields = {'slug': ("Brand", "series", "model")}

@admin.register(Desktop)
class DesktopAdmin(admin.ModelAdmin):
    list_display = ["Brand", "type", "memory", "cpu","price", "available", "created",
    "updated"]
    list_filter = ['Brand', "type", "memory", "cpu", "price","available", "created",
    "updated"]
    list_editable = ['price', "available"]
    prepopulated_fields = {'slug': ("Brand", "series", "model")}
  
@admin.register(OS)
class OSAdmin(admin.ModelAdmin):
    pass
@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    pass
@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    pass
@admin.register(Graphics)
class GraphicsAdmin(admin.ModelAdmin):
    pass