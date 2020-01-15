from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.
from .models import post

# Registration of models in admin site
admin.site.register(post, SimpleHistoryAdmin)