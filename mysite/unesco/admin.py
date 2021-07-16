from django.contrib import admin

from unesco.models import Site, Category, Iso, Region, State
# Register your models here.

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Iso)
admin.site.register(Region)
admin.site.register(State)
