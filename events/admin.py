from django.contrib import admin

from .models import Club
from .models import Motel
from .models import Event

admin.site.register(Club)
admin.site.register(Motel)
admin.site.register(Event)