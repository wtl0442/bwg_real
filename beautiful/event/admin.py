from django.contrib import admin
from .models import Event, Tag, Googlemap
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
# Register your models here.
admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(Googlemap)
# admin.site.register(Month)

class GooglemapAdmin(admin.ModelAdmin):
    formfield_overrides = {
    map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
}