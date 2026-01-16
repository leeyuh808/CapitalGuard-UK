from django.db import models

# Create your models here.
class Trade(models.Model):
    ticker = models.CharField(max_length=10)        # e.g., 'BTC', 'TSLA'
    buy_price = models.DecimalField(max_digits=12, decimal_places=2)
    sell_price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.DecimalField(max_digits=12, decimal_places=4) # Fractions for crypto
    sell_date = models.DateField()
    
    def get_profit(self):
        """Calculates the raw profit of this specific trade."""
        return (self.sell_price - self.buy_price) * self.quantity
    
    def __str__(self):
        return f"{self.ticker} sold on {self.sell_date}"