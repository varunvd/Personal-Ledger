from django.contrib import admin
from .models import Bank, Expenditure, Income, InvestmentType, Investment, TradingInvestment, Trading, BankDetail

admin.site.register(BankDetail)
admin.site.register(Bank)
admin.site.register(Expenditure)
admin.site.register(Income)
admin.site.register(InvestmentType)
admin.site.register(Investment)
admin.site.register(TradingInvestment)
admin.site.register(Trading)


admin.site.site_header = 'Personal Ledger'
admin.site.site_title = "Personal Ledger"
admin.site.index_title = "Welcome to your personal ledger"