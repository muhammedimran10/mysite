import django_filters
from django_filters import CharFilter
from django import forms
from .models import Weekly_entry,Loan
class weekfilter(django_filters.FilterSet):
    class Meta:
        model=Weekly_entry
        fields='__all__'        
        exclude =[
            'invest_amt',
            'loan_amt',
            'remarks',
        ]
class loanfilter(django_filters.FilterSet):
    class Meta:
        model=Loan
        fields='__all__'
        exclude=[
            'loan_amt',
            'remarks',
        ]