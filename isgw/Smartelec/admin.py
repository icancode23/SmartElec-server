from django.contrib import admin
from Smartelec.models import User,UserTransaction,UserTask,DailyLog,Device

# Register your models here.
admin.site.register(User)
admin.site.register(UserTransaction)
admin.site.register(UserTask)
admin.site.register(DailyLog)
admin.site.register(Device)