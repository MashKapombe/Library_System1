# Register your models here.
from django.contrib import admin
from django.contrib.sessions.models import Session
admin.site.register(Session)

from .models import UserExtend
admin.site.register(UserExtend)
