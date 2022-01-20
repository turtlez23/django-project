from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Tworzenie dokumentacji
# Obsługa klientów
# Sprzątanie
# Wysyłka towaru
# odbiór towaru
class Responsibility(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	
	def __str__(self):
		return f'{self.id}: {self.name} | {self.description}'

class Department(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	responsibilities = models.ManyToManyField(Responsibility)

	def __str__(self):
		return f'{self.id}: {self.name} | {self.description} | [{" ,".join(self.responsibilities)}]'

class Person(models.Model):
	personalId = models.CharField(max_length=11)
	age = models.IntegerField(default=0)
	department = models.ForeignKey(Department, on_delete=models.PROTECT)
	django_user = models.OneToOneField(User, related_name='django_user', default=None, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.id}: {self.personalId} | {self.age} | {self.department} | {self.django_user}'

class Project(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f'{self.id}: {self.name} | {self.description}'

class Stage(models.Model):
	type = models.CharField(max_length=10, choices=(("none","None"), ("task","Task"), ("meeting","Meeting")))
	state = models.BooleanField(default=False)
	description = models.TextField(null=True, blank=True)
	project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name="Project")

	def __str__(self):
		return f'{self.id}: {self.type} | {self.state} | {self.description} | {self.project}'
		
	class Meta:
		managed = True  # No database table creation or deletion  \
						 # operations will be performed for this model.	   
		#default_permissions = () # disable "add", "change", "delete"
								 # and "view" default permissions
		# permissions = (
		#	 ('access_system_files_webservices', 'System File WebServices'),
		# )