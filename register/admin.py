from django.contrib import admin
from register.models import Registrations
# Register your models here.
class registrationAdmin(admin.ModelAdmin):
    list_display = ('Name','Branch','Year','Section','Email','Contact_No','Contest','Roll')

admin.site.register(Registrations,registrationAdmin)
