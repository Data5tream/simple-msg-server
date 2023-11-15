from django.contrib import admin

from .models import User, MsgEntry, MsgForm

# Register your models here.
admin.site.register(User)
admin.site.register(MsgForm)
admin.site.register(MsgEntry)
