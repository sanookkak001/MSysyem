from django.shortcuts import render , redirect , get_object_or_404
from Stock.models import Stock_info as Stocks_informations
from Stock.models import Stock_History
from Stock.models import BuySell
from Stock.models import Symbol
from Stock.models import Dividend_History
from django.contrib import messages
import yfinance as yf
import os
import math


def stock_history_view(request, data_id):
    List_Manange = []
    List_Manange_Dividend = []
    
    
    try:
        Symbol_instance = Symbol.objects.get(Symbolname=data_id)
        history_entries = Stock_History.objects.filter(Symbol_Ticker=Symbol_instance)
        Dividend = Dividend_History.objects.filter(Ticker=Symbol_instance)
        Stock_Ticker = yf.Ticker(Symbol_instance.Symbolname)
        Stock_Fullname = Stock_Ticker.info.get('longName', 'Unknown')
        for item in Dividend:
            List_Manange_Dividend.append({
                'Channel' : item.Channel_item,
                'Type' : item.Type_item,
                'Ticker' : item.Ticker,
                'Currency' :item.Currency_item,
                'Dividend_Per_Share' : item.Dividend_Per_Share,
                'Before_TAX' : item.Before_TAX,
                'Withholding_TAX' : item.Withholding_TAX,
                'After_TAX' : item.After_TAX,
                'Amount_holding' : item.Amount_holding,
                'Rate' : item.Rate,
                'Date' : item.Date,
                'Quarter_item' : QuarterDate(item.Date,item.Quarter_item)
            })

        
        for item in history_entries:
                List_Manange.append({
                    'Date' : item.Day,
                    'Symbol_Ticker' : item.Symbol_Ticker,
                    'Result' : str(item.BuyandSell),
                    'Type' : item.Type,
                    'Amount' : item.Amount,
                    'AvgPrice' : item.AvgPrice,
                    'Values' : round(item.Values ,2)
                    
                }) 
    except Stocks_informations.DoesNotExist:
        return render(request, '404.html')
    
    except Stock_History.DoesNotExist:
        history_entries = []  
        
    except Exception as e:
        print(e)
        return render(request, '500.html') 
    
    return render(request, 'Stock_History.html', {'Ticker': Symbol_instance,
                                                 'Stock_Fullname' : Stock_Fullname, 
                                                 'List_Manange': List_Manange,
                                                 'List_Manange_Dividend' : List_Manange_Dividend,
                                                 'total_After_TAX' : Summary(List_Manange_Dividend,'After_TAX'),
                                                 'total_Amount' : Summary(List_Manange,'Amount'),
                                                 'AVG_price' : Average(List_Manange),
                                                 'Buy' : Count(List_Manange,'Result','Buy'),
                                                 'Sell' : Count(List_Manange,'Result','Sell'),
                                                 'Event' : Count(List_Manange,'Result' , 'Event'),
                                                 "Images" : get_stock_image(Symbol_instance , '.ico')})

def QuarterDate(Date,Quarter_item):
    QuarterDate = f'{Quarter_item}/{Date.year}'
    return QuarterDate

def Summary(Lists,Data):
    total_after_tax = 0
    for item in Lists:
        total_after_tax += item[Data]
    return total_after_tax

def Average(Lists):
    Amount_total = 0
    Total_cost = 0
    for item in Lists:
        price = item['Amount'] * item['AvgPrice']
        Amount_total += item['Amount']
        Total_cost += price
    
    if Amount_total == 0:
        return 0  # Return 0 if no items are present
        
    average_price = Total_cost / Amount_total
    return math.ceil(average_price * 100) / 100

def Count(List_Manange, Data ,Values):
    Count = 0
    for item in List_Manange:
        if Data in item and str(item[Data]) == Values:
            Count += 1
    return Count
            
def Stock_History_All(request):
    List_Manange_Dividend = []
    Dividend = Dividend_History.objects.all()
    for item in Dividend:
        List_Manange_Dividend.append({
            'Channel' : item.Channel_item,
            'Type' : item.Type_item,
            'Ticker' : item.Ticker,
            'Currency' :item.Currency_item,
            'Dividend_Per_Share' : item.Dividend_Per_Share,
            'Before_TAX' : item.Before_TAX,
            'Withholding_TAX' : item.Withholding_TAX,
            'After_TAX' : item.After_TAX,
            'Amount_holding' : item.Amount_holding,
            'Rate' : item.Rate,
            'Date' : item.Date,
            'Quarter_item' : QuarterDate(item.Date,item.Quarter_item)
        })
    return render(request,'Stock_HistoryAll.html' , {'List_Manange_Dividend' : List_Manange_Dividend,
                                                     'total_After_TAX' : Summary(List_Manange_Dividend,'After_TAX')})
    
            

def Stock_info(request):
    stock_info_list = fetch_stock_info()
    return render(request, 'Stock_info.html', {'stock_info_list': stock_info_list})

def fetch_stock_info():
    stock_info_objects = Stocks_informations.objects.all()
    stock_info_list = []

    for stock_info in stock_info_objects:
        try:
            symbol_str = str(stock_info.Symbol_Ticker)
            Stock_Ticker = yf.Ticker(symbol_str)
            Stock_Fullname = Stock_Ticker.info.get('longName', 'Unknown')
            current_price = round(Stock_Ticker.history(period='1d')['Close'].iloc[-1], 2)
            Estimate = round(stock_info.Amount * current_price, 2)
            Result = 'กำไร' if current_price > stock_info.AvgPrice else ('ขาดทุน' if current_price < stock_info.AvgPrice else 'เท่าทุน')
            stock_info_list.append({
                'ID': stock_info.id,
                'Ticker': symbol_str,
                'Fullname': Stock_Fullname,
                'Sector': get_sector(Stock_Ticker),
                'Amount': round(stock_info.Amount,7),
                'AvgPrice': stock_info.AvgPrice,
                'Price': current_price,
                'Estimate': Estimate,
                'Result': Result,
                'Images': get_stock_image(symbol_str),
                'Precent' : Precent(stock_info.Amount,Estimate,stock_info.AvgPrice)
            })
        except Exception as e:
            print(f"Error processing stock {symbol_str}: {e}")
            

    return stock_info_list

def get_stock_image(Ticker , Type=".png"):
    
    image_dir = 'static/Images'
    Type = '.png' if Type != "png" else '.ico'
    if os.path.exists(os.path.join(image_dir, f'{Ticker}{Type}')):
        return f'{Ticker}{Type}'
    else:
        return f'NoImages{Type}'

def get_sector(Stock_Ticker):
    sector_info = Stock_Ticker.info.get('sector')
    if sector_info:
        return sector_info
    else:
        return Stock_Ticker.info.get('quoteType', 'Unknown')

def get_result_color(Result):
    if Result == 'กำไร':
        return 'green'
    elif Result == 'เท่าทุน':
        return 'yellow'
    else:
        return 'red'

def Precent(Amount , Estimate , AvgPrices):
    Amount_values = round((Amount * AvgPrices), 2)
    Minusprice = round((Estimate - Amount_values) , 2)
    Precent = round((Minusprice / Amount_values) * (100) , 2)
    return Precent
    
    
def Add_History(request):
    
    date = request.POST.get('date', 0)
    Ticker = request.POST.get('Ticker',0)
    AveragePrice = float(request.POST.get('AvgPrice' , 0))
    Amounts =  float(request.POST.get('Amounts' , 0))
    Values = round(AveragePrice * Amounts , 2)
    usdthb = yf.Ticker('USDTHB=X')
    usdthb_date = usdthb.history(period='1d')['Close'].iloc[-1]
    usdthb_formmate = f'{usdthb_date:.2f}' if usdthb_date % 1 != 0 else f'{usdthb_date:.2f}'
    Bath = float(usdthb_date * Values)
    BuyandSell = 1
    
    if date == '0' or Ticker == '0' or AveragePrice == '0' or Amounts == 0  :
        messages.success(request,'Please choose option')
        return redirect(request,'Stock_information')
    
    Symbol_instance = Symbol.objects.get(Symbolname=Ticker)
    symbol_id = Symbol_instance.id
    Symbol_type = Symbol_instance.TypeSector


    BuyandSell_id = BuySell.objects.get(pk=BuyandSell)
    Ticker_id = Symbol.objects.get(pk=symbol_id)
    
    
            
    Data = Stock_History.objects.create(
        Day = date,
        Symbol_Ticker = Ticker_id,
        BuyandSell = BuyandSell_id,
        Type = Symbol_type,
        Amount = Amounts,
        AvgPrice = AveragePrice,
        Values = Values,
        Rate = usdthb_formmate,
        Bath = Bath
    )
    
    Data.save()
    messages.success(request, "Clothes added successfully.")
    return redirect('Stock_information')
