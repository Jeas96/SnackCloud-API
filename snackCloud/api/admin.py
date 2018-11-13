# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import Role,Product,User,Machine,Sale,Inventory


# Register your models here.
admin.site.register(Role)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Machine)
admin.site.register(Sale)
admin.site.register(Inventory)