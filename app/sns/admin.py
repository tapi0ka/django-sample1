from django.contrib import admin

# Register your models here.

from .models import ExecList, Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'submitter','submission_year_month')

admin.site.register(ExecList)
admin.site.register(Report, ReportAdmin)