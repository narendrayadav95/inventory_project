# Super username = narendra
# pwd = admin

# username = Ken
# pwd = adminken

from django.contrib import admin
from .models import Product, Order

from django.contrib.auth.models import Group

admin.site.site_header = 'Inventory DashBoard'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['id','name','category','quantity']
	list_filter = ['category']

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
# 	list_display = ['id', 'product', 'staff', 'order_qualtity', 'date']


# admin.site.unregister(Group)

admin.site.register(Order) 