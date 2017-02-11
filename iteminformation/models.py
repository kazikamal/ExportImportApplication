from __future__ import unicode_literals

from django.db import models

class Stock(models.Model):
	itemName = models.CharField(max_length=20)
	openPrice = models.FloatField()
	closePrice = models.FloatField()
	volume = models.IntegerField()

	def __str__(self):
		return self.itemName