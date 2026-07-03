
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()
    

    def __str__(self):
        return self.description