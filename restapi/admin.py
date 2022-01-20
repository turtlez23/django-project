from django.contrib import admin

# Register your models here.

from restapi import models as m

admin.site.register(m.Person)
admin.site.register(m.Department)
admin.site.register(m.Project)
admin.site.register(m.Responsibility)
admin.site.register(m.Stage)