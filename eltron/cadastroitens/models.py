from django.db import models
from django.db import models
from django.utils import timezone
# Create your models here.


class item(models.Model):
	name = models.CharField('Nome', max_length=200)
	code = models.SlugField('Código', max_length=15)
	description = models.TextField('Descrição', max_length=300, blank=True, null=True)
	part_number = models.SlugField('part_number', max_length=50, blank=True, null=True)
	datasheet = models.URLField(null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'item'
		verbose_name_plural = 'Itens'
		ordering = ['name']

