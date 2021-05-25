
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import Memmber,Weekly_entry,Loan,Loan_interest
class DateInput(forms.DateInput):
    input_type= 'date'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class RegistrForm(forms.ModelForm):
    class Meta:
        model= Memmber
        fields=[
            'fullname',
            'address1',
            'address2',
            'address3',
            'mobile_no',
            'active',
        ]

class WeekEntryForm(forms.ModelForm):
    class Meta:
        model=Weekly_entry
        widgets={'entry_date':DateInput()}
        fields=[
            'entry_date',
            'memmber_id',
            'invest_amt',
            'loan_amt',
            'remarks',
        ]

class LoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        widgets={'loan_date':DateInput()}
        fields=[
            'loan_date',
            'memmber_id',
            'loan_amt',
            'remarks',
        ]
class InterestForm(forms.ModelForm):
    class Meta:
        model=Loan_interest
        widgets={'date':DateInput()}
        fields=[
            'date',
            'memmber_id',
            'interest_amt',
        ]