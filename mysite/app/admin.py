from django.contrib import admin

# Register your models here.
from .models import Memmber,Weekly_entry,Loan,Loan_interest

admin.site.register(Memmber)
admin.site.register(Weekly_entry)
admin.site.register(Loan)
admin.site.register(Loan_interest)
