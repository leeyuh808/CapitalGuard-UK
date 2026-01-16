from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Trade  
from .logic import calculate_uk_cgt  
from decimal import Decimal

# Create your views here.

# from django.shortcuts import render

# def home_view(request):
#     # 1. Fetch all trades
#     trades = Trade.objects.all().order_by('-sell_date')
    
#     # 2. Calculate Totals
#     total_gains = sum(t.get_profit() for t in trades) if trades.exists() else Decimal('0.00')
#     tax_owed = calculate_uk_cgt(total_gains)
    
#     # 3. Handle Form Submission (Adding a trade)
#     if request.method == "POST":
#         Trade.objects.create(
#             ticker=request.POST.get('ticker').upper(),
#             buy_price=request.POST.get('buy_price'),
#             sell_price=request.POST.get('sell_price'),
#             quantity=request.POST.get('quantity'),
#             sell_date=request.POST.get('sell_date')
#         )
#         return redirect('home') # Refresh page to show new trade

#     context = {
#         'trades': trades,
#         'total_gains': total_gains,
#         'tax_owed': tax_owed,
#         'allowance_left': max(0, 3000 - total_gains)
#     }
#     return render(request, 'home.html', context)






# 1. THE DASHBOARD VIEW 
def home_view(request):
    trades = Trade.objects.all()
    total_gains = sum(t.get_profit() for t in trades) if trades.exists() else Decimal('0.00')
    tax_owed = calculate_uk_cgt(total_gains)
    
    context = {
        'total_gains': total_gains,
        'tax_owed': tax_owed,
        'allowance_left': max(0, 3000 - total_gains)
    }
    return render(request, 'home.html', context)

# 2. THE HISTORY VIEW 
def history_view(request):
    # Grabs every trade sorted by the newest date first
    trades = Trade.objects.all().order_by('-sell_date')
    return render(request, 'history.html', {'trades': trades})

# 3. THE ADD TRADE VIEW 
def add_trade_view(request):
    if request.method == "POST":
        # Save what the user typed in the form
        Trade.objects.create(
            ticker=request.POST.get('ticker').upper(),
            buy_price=request.POST.get('buy_price'),
            sell_price=request.POST.get('sell_price'),
            quantity=request.POST.get('quantity'),
            sell_date=request.POST.get('sell_date')
        )
        return redirect('home') 
    
    return render(request, 'add_trade.html')

# 4. THE ACCOUNTS VIEW
def accounts_view(request):
    return render(request, 'accounts.html', {
        'username': request.user.username,
        'trade_count': Trade.objects.count()
    })


