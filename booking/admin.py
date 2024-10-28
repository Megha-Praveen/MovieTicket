from django.contrib import admin
from .models import Register, Login, Movie

# Register your models here.

admin.site.register(Register)
admin.site.register(Login)
admin.site.register(Movie)
