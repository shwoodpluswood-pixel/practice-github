from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Income
from .forms import IncomeForm

def home(request):
    form = IncomeForm()
    incomes = Income.objects.all().order_by('-date')
    return render(request, 'money_diary/home.html', {'form': form, 'incomes': incomes})

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            incomes = Income.objects.all().order_by('-date')
            html = render_to_string('money_diary/income_list.html', {'incomes': incomes})
            return HttpResponse(html)
    return HttpResponse(status=400)
