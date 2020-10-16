from django.contrib import admin
from .models import Readnum,ReadDetail

@admin.register(Readnum)
class ReadnumAdmin(admin.ModelAdmin):
    list_display = ("read_num","content_object",)

@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date',"read_num", "content_object",)