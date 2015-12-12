from django.contrib import admin
from orders.models import Order, Worker, Job

class JobInline(admin.TabularInline):
    model = Job

class OrderAdmin(admin.ModelAdmin):
    inlines = [JobInline, ]
    search_fields = ['name', ]


class WorkerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)

admin.site.register(Worker, WorkerAdmin)
