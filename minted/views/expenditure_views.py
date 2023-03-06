from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from minted.forms import *
from minted.models import *
from .general_user_views.login_view_functions import *
from minted.views.expenditure_receipt_functions import handle_uploaded_file, delete_file
from django.contrib import messages

@login_required
def category_expenditures_view(request, category_name):
    category = Category.objects.get(user=request.user, name=category_name)
    expenditures = Expenditure.objects.filter(category=category).order_by('-date')
    return render(request, 'expenditures/expenditures_list.html', { 'expenditures': expenditures, 'category': category })

@login_required
def delete_expenditure(request, expenditure_id):
    if request.method == 'POST':
        expenditure = Expenditure.objects.get(pk=expenditure_id)
        category = expenditure.category
        if request.user == category.user:
            delete_file(expenditure.receipt.path)
            expenditure.delete()
        return redirect('expenditures', category_name=category.name)
    return redirect('category_list')

@login_required
def edit_expenditure(request, category_name, expenditure_id):
    expenditure = Expenditure.objects.get(id=expenditure_id)
    form = ExpenditureForm(instance=expenditure)
    if request.method == 'POST':
        form = ExpenditureForm(request.POST, instance=expenditure)
        if form.is_valid():
            expenditure = form.save(commit=False)
            new_file = request.FILES.get('receipt')
            # clear = request.POST.get('receipt-clear') # This is so broken
            current_receipt = expenditure.receipt
            update_file = new_file and current_receipt

            if update_file:
                delete_file(current_receipt.path)

            if new_file:
                receipt_path = handle_uploaded_file(request.FILES['receipt'])
                expenditure.receipt = receipt_path

            expenditure.save()

            return redirect('expenditures', category_name=category_name)
    return render(request, 'expenditures/edit_expenditures.html', { 'form': form, 'expenditure': expenditure })


@login_required
def add_expenditure(request, category_name):
    if request.method == 'POST':
        category = Category.objects.get(user=request.user, name=category_name) # Need to make sure there are no duplicate categories with same name
        form = ExpenditureForm(request.POST)
        if request.POST.get("addExpenditure"):
            if form.is_valid():
                expenditure = form.save(commit=False)
                file = request.FILES.get('receipt')
                expenditure.category = category

                if file:
                    receipt_path = handle_uploaded_file(request.FILES['receipt'])
                    expenditure.receipt = receipt_path
                
                expenditure.save()

                return redirect('expenditures', category_name=category_name)
        elif request.POST.get("cancelAddition"):
            return redirect('expenditures', category_name=category_name)
    form = ExpenditureForm()
    return render(request, 'expenditures/add_expenditure.html', { 'form': form, 'category': category_name })
