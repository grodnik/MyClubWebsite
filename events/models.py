from django.db import models


class Club(models.Model):
	name = models.CharField('Supper Club', max_length=120)
	address = models.CharField('Address', max_length=300)
	phone = models.CharField('Phone', max_length=20)
	email = models.EmailField('Email', blank=True)
	web = models.URLField('Web Site', blank=True)
	info = models.TextField('Info', blank=True)

	def __str__(self):
		return self.name



class Motel(models.Model):
	name = models.CharField('Motel', max_length=120)
	address = models.CharField('Address', max_length=300)
	phone = models.CharField('Phone', max_length=20, blank=True)

	def __str__(self):
		return self.name



class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	#club = models.CharField(max_length=120, blank=True)
	club = models.ForeignKey('Club', blank=True, null=True, on_delete=models.SET_NULL)
	#motel = models.CharField(max_length=120, blank=True)
	motel = models.ForeignKey('Motel', blank=True, null=True, on_delete=models.SET_NULL)
	comments = models.TextField('Comments', blank=True)

	def __str__(self):
		return self.name

