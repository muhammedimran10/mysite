from django import template
register = template.Library()
from ..models import Weekly_entry,Loan_interest,Loan
from django.db.models import Sum

def ch(i):
        if i == None:
            i=0
        return i

@register.filter
def total_pm_invest(id,date):
    totalinvest=Weekly_entry.objects.filter(memmber_id=id).filter(entry_date__lt=date).aggregate(Sum('invest_amt')) 
    a=totalinvest['invest_amt__sum']
    return ch(a)

@register.filter
def total_invest(id,date):
    pt=total_pm_invest(id,date)
    i_rp=Weekly_entry.objects.filter(memmber_id=id).filter(entry_date__month=date.month).filter(entry_date__year=date.year).aggregate(invest_amt=Sum('invest_amt'))
    inv=i_rp['invest_amt']
    a=ch(inv)+pt
    return a

@register.filter
def interest_enterd(id,date):
    ob=Loan_interest.objects.filter(memmber_id=id)
    fill_date=ob.filter(date__month=date.month).filter(date__year=date.year)
    for l in fill_date:
        return l.interest_amt

@register.filter
def p_loan_amt(id, date):
    loans=Loan.objects.all().filter(memmber_id=id).filter(loan_date__month__lte = date.month).filter(loan_date__year__lte = date.year).aggregate(loan_amt=Sum('loan_amt'))
    l=loans['loan_amt']
    l=ch(l)
    interest_t=Loan_interest.objects.filter(memmber_id=id).filter(date__lt=date).aggregate(interest_amt=Sum('interest_amt'))
    i=interest_t['interest_amt']
    i=ch(i)
    l_rp=Weekly_entry.objects.filter(memmber_id=id).filter(entry_date__lt=date).aggregate(loan_amt=Sum('loan_amt'))
    lr=l_rp['loan_amt']
    lr=ch(lr)
    r=(l+i)-lr
    return r

@register.filter
def monthlyloan(id ,date):
    loan_reseved = Weekly_entry.objects.filter(memmber_id=id).filter(entry_date__month=date.month).filter(entry_date__year=date.year).aggregate(ml=Sum('loan_amt'))
    print(loan_reseved)
    lr=loan_reseved['ml']
    lr=ch(lr)
    return lr

@register.filter
def totalloan(id ,date):

    r=p_loan_amt(id,date)
    interest_c=Loan_interest.objects.filter(memmber_id=id).filter(date__month=date.month).filter(date__year=date.year).aggregate(interest_amt=Sum('interest_amt'))
    b=interest_c['interest_amt']
    b=ch(b)
    return r+b

    




@register.filter
def balance(id ,date):
    
    tl_amts = Loan.objects.filter(memmber_id=id).filter(loan_date__month__lte = date.month).filter(loan_date__year__lte = date.year).aggregate(tl_amt=Sum('loan_amt'))
    tl = tl_amts['tl_amt']
    tl=ch(tl)

    ti_amts = Loan_interest.objects.filter(memmber_id=id).filter(date__month__lte = date.month).filter(date__year__lte = date.year).aggregate(ti_amt=Sum('interest_amt'))
    ti = ti_amts['ti_amt']
    ti = ch(ti)

    tlp_amts = Weekly_entry.objects.filter(memmber_id=id).filter(entry_date__month__lte = date.month).filter(entry_date__year__lte = date.year).aggregate(tlp_amt=Sum('loan_amt'))
    tlp = tlp_amts['tlp_amt']
    tlp=ch(tlp)
    return (tl+ti)-tlp