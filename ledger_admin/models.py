from django.db import models

class BankDetail(models.Model):
    bank_name = models.CharField(max_length=50, primary_key=True)

    def bank_names(self):
        return f"{self.bank_name}"
    
    def __str__(self):
        return f"{self.bank_name}"

class Bank(models.Model):
    account_number = models.CharField(max_length=50, primary_key=True)
    ifsc_code = models.CharField(max_length=50)
    bank_name = models.ForeignKey(BankDetail, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=20,decimal_places=2)

    def account_numbers(self):
        return f"{self.account_number}"
    
    def __str__(self):
        return f"{self.account_number}"


class Expenditure(models.Model):
    amount_spent = models.DecimalField(max_digits=20,decimal_places=2)
    description = models.CharField(max_length=500)
    account_number = models.ForeignKey(Bank, on_delete=models.PROTECT)
    
    def descriptions(self):
        return f"{self.description}"
    def __str__(self):
        return f"{self.description}"

class Income(models.Model):
    amount_earned = models.DecimalField(max_digits=20,decimal_places=2)
    description = models.CharField(max_length=500)
    account_number = models.ForeignKey(Bank, on_delete=models.PROTECT)
    
    def descriptions(self):
        return f"{self.description}"
    def __str__(self):
        return f"{self.description}"

class InvestmentType(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def names(self):
        return f"{self.name}"
    def __str__(self):
        return f"{self.name}"

class Investment(models.Model):
    amount_invested = models.DecimalField(max_digits=20,decimal_places=2)
    investment_type = models.ForeignKey(InvestmentType, on_delete=models.PROTECT)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    bank_name = models.ForeignKey(BankDetail, on_delete=models.PROTECT)

    def names(self):
        return f"{self.investment_type}"
    def __str__(self):
        return f"{self.investment_type}"

class TradingInvestment(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def names(self):
        return f"{self.name}"
    def __str__(self):
        return f"{self.name}"

class Trading(models.Model):
    amount_invested = models.DecimalField(max_digits=20,decimal_places=2)
    trading_type = models.ForeignKey(TradingInvestment, on_delete=models.PROTECT)
    type_details = models.CharField(max_length=500)
    bank_name = models.ForeignKey(BankDetail, on_delete=models.PROTECT)

    def names(self):
        return f"{self.type_details}"
    def __str__(self):
        return f"{self.type_details}"