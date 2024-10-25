from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Currency_detail
# Register your models here.
@admin.register(Currency_detail)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id','amount','from_currency','to_currency','converted_amount','converstion_rate','date']