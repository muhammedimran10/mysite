from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .form import RegistrForm,WeekEntryForm,LoanForm,CreateUserForm,InterestForm
from .models import Memmber,Weekly_entry,Loan,Loan_interest
from .filters import weekfilter,loanfilter
from django.db import connection
from .decorators import unautenticated_user,allowed_users,admin_only
from django.db.models import Sum
from django.core.paginator import Paginator

# Create your views here.


@login_required(login_url='login')
@admin_only
def home(request):
    context={}
    return render(request,'app/home.html',context)


@login_required(login_url='login')
@admin_only
def memmberlist(request):
    memmbers=Memmber.objects.all()
    context={
        'liobject':memmbers
    }
    return render(request,'app/memmber_view.html',context)
    

@login_required(login_url='login')
@allowed_users(allowed_roles =['admin'])
def register(request):
    form = RegistrForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('memmberlist')
    context={
        'form':form
    }
    return render(request,'app/memmber_registration.html',context)


@login_required(login_url='login')

def editmemmber(request,pk):
    memmberob=Memmber.objects.get(id=pk)
    form=RegistrForm(instance=memmberob)
    if request.method=='POST':
        form=RegistrForm(request.POST,instance=memmberob)
        if form.is_valid():
            form.save()
            return redirect('memmberlist')
    context={
        'form':form
    }
    return render(request,'app/memmber_registration.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def weeklyentry(request):
    form = WeekEntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('weeklyview')
    context={
        'form':form
    }
    return render(request,'app/weeklyentry.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def weeklyview(request):
    w_list=Weekly_entry.objects.all().order_by('-entry_date')
    myFilter = weekfilter(request.GET,queryset=w_list)
    w_list=Weekly_entry.objects.all().order_by('-entry_date')
    w_list=myFilter.qs
    # p= Paginator(w_list,2)
    # w_list=p.object_list
    # print(p.num_pages)
    # for page in p.page_range:
    #     print(page)
    # p1=p.page(1)
    # p1.number
    # p1.object_list
    # p1.has_previous()
    # p1.has_next
    # p1.next_page_number()
    # print(p1.)
    context={
        'w_list':w_list,
        'myFilter':myFilter
    }
    return render(request,'app/weeklylistview.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateweek(request,pk):
    id=1
    weekob=Weekly_entry.objects.get(id=pk)
    form=WeekEntryForm(instance=weekob)
    if request.method=='POST':
        form=WeekEntryForm(request.POST,instance=weekob)
        if form.is_valid():
            form.save()
            return redirect('weeklyview')
    context={
        'form':form,
        'id':id
    }
    
    return render(request,'app/weeklyentry.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def loanview(request):
    loanob=Loan.objects.all()
    myFilter = loanfilter(request.GET,queryset=loanob)
    loanob=myFilter.qs
    context={
        'loanob':loanob,
        'myFilter':myFilter
    }
    return render(request,'app/loanlist.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def giveloan(request):
    form = LoanForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('loanview')
    context={
        'form':form
    }
    return render(request,'app/giveloan.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateloan(request,pk):
    d=1
    loanob=Loan.objects.get(id=pk)
    form=LoanForm(instance=loanob)
    if request.method=='POST':
        form=LoanForm(request.POST,instance=loanob)
        if form.is_valid():
            form.save()
            return redirect('loanview')
    context={
        'form':form,
        'd':d
    }
    return render(request,'app/giveloan.html',context)

@login_required(login_url='login')
def memmberdetail(request,pk):
    memmberob=Memmber.objects.get(id=pk)
    last_tra=Weekly_entry.objects.all().filter(memmber_id=pk).order_by('-entry_date')[:5]
    totalloan=Loan.objects.filter(memmber_id=pk).aggregate(Sum('loan_amt'))
    totalinvest=Weekly_entry.objects.filter(memmber_id=pk).aggregate(Sum('invest_amt'))
    loanamt=Weekly_entry.objects.filter(memmber_id=pk).aggregate(Sum('loan_amt'))
    interestamt=Loan_interest.objects.filter(memmber_id=pk).aggregate(iat=Sum('interest_amt'))
    context={
        'memmberob':memmberob,
        'totalloan':totalloan,
        'totalinvest':totalinvest,
        'loanamt':loanamt,
        'interestamt':interestamt['iat'],
        'last_tra':last_tra
    }
    return render(request,'app/memmberdetail.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def groupdetail(request):
    weekob=Weekly_entry.objects.all()
    total_invest=weekob.aggregate(Sum('invest_amt'))
    total_loan= Loan.objects.all().aggregate(Sum('loan_amt'))
    loan_amt_get=weekob.aggregate(Sum('loan_amt'))
    interest=Loan_interest.objects.aggregate(iat=Sum('interest_amt'))
    context={
        'total_invest':total_invest,
        'total_loan':total_loan,
        'loan_amt_get':loan_amt_get,
        'interest':interest['iat']
    }
    return render(request,'app/groupdetail.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def monthlyview(request):
    ml= connection.ops.date_trunc_sql('month','entry_date')
    monthlydate=Weekly_entry.objects.extra({'month': ml}).values('month').distinct()
    context = {
        'monthlydate':monthlydate
    }
    return render(request,'app/monthly_view.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def monthlysummary(request,date):
    import datetime
    format_str = '%Y-%m-%d' # The format
    datetime_obj = datetime.datetime.strptime(date, format_str)
    listofmonthlyob=Weekly_entry.objects.filter(entry_date__month=datetime_obj.month).filter(entry_date__year=datetime_obj.year)

    monthlyresult=listofmonthlyob.values('memmber_id__fullname','memmber_id').annotate(invest=Sum('invest_amt'),
    loan_amt=Sum('loan_amt'))
    context={
        'monthlyresult':monthlyresult,
        'date':datetime_obj
    }
    return render(request,'app/monthlysummary.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def registeruser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Memmber.objects.create(
                user=user,
                fullname=user.username,
            )
            messages.success(request,f'Account created for {user.username}!')

            return redirect('memmberlist')
    context={'form':form}
    return render(request,'app/registeruser.html',context)

@unautenticated_user
def loginpage(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username OR password is incorrect')
    context={}
    return render(request,'app/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def memmberprofile(request):
    memmberob=request.user.memmber
    pk=memmberob.id
    last_tra=Weekly_entry.objects.all().filter(memmber_id=pk).order_by('-entry_date')[:5]
    totalloan=Loan.objects.filter(memmber_id=pk).aggregate(Sum('loan_amt'))
    totalinvest=Weekly_entry.objects.filter(memmber_id=pk).aggregate(Sum('invest_amt'))
    loanamt=Weekly_entry.objects.filter(memmber_id=pk).aggregate(Sum('loan_amt'))
    interestamt=Loan_interest.objects.filter(memmber_id=pk).aggregate(iat=Sum('interest_amt'))
    context={
        'memmberob':memmberob,
        'totalloan':totalloan,
        'totalinvest':totalinvest,
        'loanamt':loanamt,
        'interestamt':interestamt['iat'],
        'last_tra':last_tra,
    }
    return render(request,'app/memmberdetail.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createinterest(request):
    form =InterestForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('monthlyview')
    context={
        'form':form
    }
    return render(request,'app/interest.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateinterest(request,pk,date):
    import datetime
    format_str = '%Y-%m-%d' # The format
    datetime_obj = datetime.datetime.strptime(date, format_str)
    loan_in=Loan_interest.objects.filter(memmber_id=pk).filter(date__month=datetime_obj.month).filter(date__year=datetime_obj.year)
    for l in loan_in:
        loan_i=l
    form=InterestForm(instance=loan_i)
    if request.method=='POST':
        form=InterestForm(request.POST,instance=loan_i)
        if form.is_valid():
            form.save()
            return redirect('monthlysummary',date)
    context={
        'form':form
    }
    
    return render(request,'app/interest.html',context)