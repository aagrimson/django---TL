from django.contrib import admin

from .models import Test, Store, WaveDate, Product

admin.site.register(Test)
admin.site.register(Store)
admin.site.register(WaveDate)
admin.site.register(Product)
