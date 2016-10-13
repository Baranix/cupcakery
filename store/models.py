from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Flavor(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Icing(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Topping(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Cupcake(models.Model):
	'''FLAVOR_TYPE_CHOICES = (
		(1, "Vanilla"),
		(2, "Chocolate"),
		(3, "Mocha"),
		(4, "Red Velvet"),
		(5, "Caramel"),
		(6, "Banana"),
		(7, "Blueberry"),
		)'''

	name = models.CharField(max_length=250)
	#flavor = models.ForeignKey(Flavor) #models.PositiveIntegerField(choices=FLAVOR_TYPE_CHOICES)
	icing = models.ForeignKey(Icing, default=0)
	topping = models.ForeignKey(Topping, default=0)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	stock = models.PositiveIntegerField(default=0)
	created_by = models.ForeignKey(User, related_name='created_by')
	created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
	edited_by = models.ForeignKey(User, related_name='edited_by', null=True, blank=True, verbose_name="Last edited by")
	edited_on = models.DateTimeField(auto_now=True, verbose_name="Last edited date")

	def __unicode__(self):
		return self.name

class hasFlavor(models.Model):
	cupcake = models.ForeignKey(Cupcake)
	flavor = models.ForeignKey(Flavor, default=0)

	def __unicode__(self):
		return "Flavor"