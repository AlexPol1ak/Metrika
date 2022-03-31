from django.contrib import admin
from .models import User
from .models import UserAnthropometry
from .models import SizeStandard

admin.site.register(User)
admin.site.register(UserAnthropometry)
admin.site.register(SizeStandard)
