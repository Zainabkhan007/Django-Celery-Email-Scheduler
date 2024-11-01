from django.contrib import admin
from .models import ProfileInfo,MessageBoard,Messages
# Register your models here.
admin.site.register(ProfileInfo)
admin.site.register(MessageBoard)
admin.site.register(Messages)