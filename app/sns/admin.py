from django.contrib import admin

# Register your models here.

from .models import ExecList, Reports

admin.site.register(ExecList)
admin.site.register(Reports)