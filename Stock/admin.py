from django.contrib import admin
from Stock import models

class Stock(admin.ModelAdmin):
    
    list_display = ('id','Day','BuyandSell','Type','Symbol_Ticker','Amount','AvgPrice','Values','Rate','Bath')
    
class Typeclass(admin.ModelAdmin):
    
    list_display = ('id','TypeSector')

class Symbol(admin.ModelAdmin):
    
    list_display = ('id','TypeSector','Symbolname')
    
class BuySell(admin.ModelAdmin):
    
    list_display = ('id','BuyandSell')
    
class Stock_info(admin.ModelAdmin):
    list_display = ('id','Symbol_Ticker','Amount','AvgPrice')
    
class Channel(admin.ModelAdmin):
    list_display = ('id','Channel_name')

class Currency(admin.ModelAdmin):
    list_display = ('id', 'Currency_name')

class Quarter(admin.ModelAdmin):
    list_display = ('id','Quarter_name')

class Dividend_History(admin.ModelAdmin):
    list_display = ('id','Channel_item','Type_item','Ticker','Currency_item','Dividend_Per_Share','Before_TAX','Withholding_TAX','After_TAX','Amount_holding','Rate','Date','Quarter_item')
    
admin.site.register(models.Stock_History , Stock)
admin.site.register(models.BuySell , BuySell)
admin.site.register(models.Type , Typeclass)
admin.site.register(models.Symbol , Symbol)
admin.site.register(models.Stock_info , Stock_info)
admin.site.register(models.Channel, Channel)
admin.site.register(models.Currency, Currency)
admin.site.register(models.Quarter, Quarter)
admin.site.register(models.Dividend_History, Dividend_History)
