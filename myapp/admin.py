from django.contrib import admin
from myapp.models import Menu,MenuCat,Event,Venue,MyUser
# Register your models here.
admin.site.register(MenuCat)
admin.site.register(Menu)
admin.site.register(Event)
# admin.site.register(Venue)
admin.site.register(MyUser)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    fields=(('name','zip'),'phone','email_address')
    list_display=('name','phone','email_address')
    ordering=('name',)
    search_fields=('name',)
