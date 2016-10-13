from django.contrib import admin

from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import uri_to_iri

from .models import Cupcake, Flavor, Icing, Topping, hasFlavor

# Register your models here.

class hasFlavorInline(admin.TabularInline):
	model = hasFlavor
	extra = 1
	verbose_name = "Flavor"
	verbose_name_plural = verbose_name + "s"

class CupcakeAdmin(admin.ModelAdmin):
	inlines = [hasFlavorInline,]

	fieldsets = [
		(None, {'fields': ['name']}),
		("Inventory", {'fields': ['stock', 'price']}),
		("Extras", {'fields': ['icing', 'topping']})
	]

	def edited(self, obj):
		return str(obj.edited_by) + "<br />" + obj.edited_on.strftime('%Y-%m-%d %H:%M:%S')

	def created(self, obj):
		return str(obj.created_by) + "<br />" + obj.created_on.strftime('%Y-%m-%d %H:%M:%S')

	def save_model(self, request, obj, form, change):
		if change:
			obj.edited_by = request.user
			obj.edited_on = timezone.now()
		else:
			obj.created_by = request.user
			obj.created_on = timezone.now()
		obj.save()

admin.site.register(Cupcake, CupcakeAdmin)
admin.site.register(Flavor)
admin.site.register(Icing)
admin.site.register(Topping)