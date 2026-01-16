import os
import django
from decimal import Decimal

# 1. SETUP: Replace 'core' with your actual project folder name
# This tells Django where to find your settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# 2. INITIALIZE: Boot up Django context
django.setup()

# 3. IMPORTS: Import after django.setup() to avoid errors
from pages.models import Trade
from pages.logic import calculate_uk_cgt

# 4. STYLING: ANSI Escape Codes for "Fintech Terminal" look
G = '\033[32m'   # Green (Profits)
R = '\033[31m'   # Red (Losses/Tax)
Y = '\033[33m'   # Yellow (Alerts)
B = '\033[1m'    # Bold
C = '\033[36m'   # Cyan (Headers)
X = '\033[0m'    # Reset color

def run_dashboard():
    # Fetch data from Database
    trades = Trade.objects.all().order_by('-sell_date')
    
    # Calculate Totals
    total_gains = sum(t.get_profit() for t in trades) if trades.exists() else Decimal('0.00')
    tax_bill = calculate_uk_cgt(total_gains, tax_band="higher")
    net_profit = total_gains - tax_bill

    # --- RENDER HEADER ---
    print(f"\n{B}{C}  ╔════════════════════════════════════════╗{X}")
    print(f"{B}{C}  ║      CAPITALGUARD UK TERMINAL          ║{X}")
    print(f"{B}{C}  ╚════════════════════════════════════════╝{X}")
    
    print(f"{B}Financial Summary (2026/27):{X}")
    print(f"Gross Gains:      {G}£{total_gains:,.2f}{X}")
    print(f"Tax Allowance:    £3,000.00")
    print(f"Estimated Tax:    {R}£{tax_bill:,.2f}{X}")
    print(f"Net Take-home:    {B}£{net_profit:,.2f}{X}")
    print(f"{'-' * 40}")

    # --- RENDER TABLE ---
    if not trades.exists():
        print(f"{Y}No trades found. Start adding data via Admin or Web!{X}")
    else:
        print(f"{B}{'DATE':<12} | {'TICKER':<8} | {'PROFIT':>13}{X}")
        print(f"{'-' * 40}")
        for t in trades:
            p = t.get_profit()
            color = G if p >= 0 else R
            print(f"{str(t.sell_date):<12} | {t.ticker:<8} | {color}£{p:>12.2f}{X}")

    # --- ALERTS ---
    if total_gains > 3000:
        print(f"\n{B}{R}‼ TAX ALERT: £{total_gains - 3000:,.2f} is currently taxable.{X}")
    elif total_gains > 2500:
        print(f"\n{B}{Y}⚠ WARNING: You are approaching your £3,000 allowance.{X}")

    print(f"{'-' * 40}\n")

if __name__ == "__main__":
    run_dashboard()