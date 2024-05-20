from django.db import models

from django.db import models

class BuySell(models.Model):
    BuyandSell = models.CharField(max_length=255)

    def __str__(self):
        return self.BuyandSell
    
class Type(models.Model):
    TypeSector = models.CharField(max_length=255)
    
    def __str__(self):
        return self.TypeSector
    
class Symbol(models.Model):
    TypeSector = models.ForeignKey(Type, on_delete=models.CASCADE)
    Symbolname = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-Symbolname']
        db_table = 'Symbol'
    
    def __str__(self):
        return f'{self.Symbolname}'

class Stock_History(models.Model):
    Day = models.DateField()
    BuyandSell = models.ForeignKey(BuySell, on_delete=models.CASCADE)
    Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    Symbol_Ticker = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    Amount = models.FloatField(default=0)
    AvgPrice = models.FloatField(default=0)
    Values = models.FloatField(default=0)
    Rate = models.FloatField(default=0)
    Bath = models.FloatField(default=0)
    DateRecord = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id} {self.Day} {self.BuyandSell}'
    
    
class Stock_info(models.Model):
    Symbol_Ticker = models.ForeignKey(Symbol,on_delete=models.CASCADE,unique=True)
    Amount = models.FloatField(default=0)
    AvgPrice = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.Symbol_Ticker)
class Channel(models.Model):
    Channel_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Channel_name
    
class Currency(models.Model):
    Currency_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Currency_name

class Quarter(models.Model):
    Quarter_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Quarter_name
    
class Dividend_History(models.Model):
    Channel_item = models.ForeignKey(Channel, on_delete=models.CASCADE)
    Type_item = models.ForeignKey(Type, on_delete=models.CASCADE)
    Ticker = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    Currency_item = models.ForeignKey(Currency , on_delete=models.CASCADE)
    Dividend_Per_Share = models.FloatField(default=0)
    Before_TAX = models.FloatField(default=0)
    Withholding_TAX = models.FloatField(default=0)
    After_TAX = models.FloatField(default=0)
    Amount_holding = models.FloatField(default=0)
    Rate = models.FloatField(default=0)
    Date = models.DateField()
    Quarter_item = models.ForeignKey(Quarter,on_delete=models.CASCADE)



