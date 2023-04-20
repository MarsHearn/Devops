from django.contrib import admin
from .models import test_model
#from rest_framework.authtoken.admin import TokenAdmin # use for Token
# Register your models here.
admin.site.register(test_model)

#TokenAdmin.raw_id_fields = ['zhxt'] # use for Token