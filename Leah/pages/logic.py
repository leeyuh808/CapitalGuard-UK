from decimal import Decimal

def calculate_uk_cgt(total_profit, tax_band="basic"):
    """
    total_profit: The sum of all gains minus losses for the year
    tax_band: "basic" (18%) or "higher" (24%)
    """
    # constants
    ALLOWANCE = Decimal('3000.00')
    BASIC_RATE = Decimal('0.18')
    HIGHER_RATE = Decimal('0.24')
    
    # Subtract the tax-free allowance
    taxable_amount = total_profit - ALLOWANCE
    
    # If profit is less than allowance, tax is zero
    if taxable_amount <= 0:
        return Decimal('0.00')
    
    # Calculate based on the band
    if tax_band == "higher":
        return (taxable_amount * HIGHER_RATE).quantize(Decimal('0.01'))
    else:
        return (taxable_amount * BASIC_RATE).quantize(Decimal('0.01'))