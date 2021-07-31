from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.db.models import Q
from django.db.models import Count

# @login_required(login_url = 'user-login')
@login_required
def index(request):
	orders = Order.objects.all()
	order_count = orders.count()

	products = Product.objects.all()
	count = products.count()

	workers = User.objects.all()
	workers_count = workers.count()

	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.staff = request.user
			instance.save()
			return redirect('dashboard-index')
	else:
		form = OrderForm()
	context = {
		'orders': orders,
		'form': form,
		'products': products, 
		'order_count': order_count,
		'count': count,
		'workers_count': workers_count,
	}
	return render(request, 'dashboard/index.html', context)


# @login_required(login_url = 'user-login')
@login_required
def staff(request):
	workers = User.objects.all()
	# workers_count = User.objects.all().aggregate(Count(workers))
	workers_count = workers.count()

	items = Product.objects.all()
	count = items.count()

	orders = Order.objects.all()
	order_count = orders.count()

	context = {
		'workers': workers,
		'workers_count': workers_count,
		'count': count,
		'order_count': order_count,
	}
	return render(request, 'dashboard/staff.html', context)

@login_required
def staff_details(request, pk):
	workers = User.objects.get(id=pk)
	context = {
		'workers': workers,
	}
	return render(request, 'dashboard/staff_details.html', context)

# @login_required(login_url = 'user-login')
@login_required
def product(request):
	# items = Product.objects.raw("select * from dashboard_product")
	# items = Product.objects.raw('SELECT * FROM dashboard_product')
	items = Product.objects.all()
	# print(items)
	count = items.count()
	# count = Product.objects.raw('SELECT COUNT(name) FROM dashboard_product')

	workers = User.objects.all()
	workers_count = workers.count()

	orders = Order.objects.all()
	order_count = orders.count()

	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			product_name = form.cleaned_data.get('name')
			messages.success(request, f'{product_name} has been created.')
			return redirect('dashboard-product')
	else:
		form = ProductForm()
	context = {
		'items': items,
		'count': count,
		'form': form,
		'workers_count': workers_count,
		'order_count': order_count,
	}
	return render(request, 'dashboard/product.html', context)

# @login_required(login_url = 'user-login')
@login_required
def order(request):
	orders = Order.objects.all()
	order_count = orders.count()

	workers = User.objects.all()
	workers_count = workers.count()

	items = Product.objects.all()
	count = items.count()
	context = {
		'orders': orders,
		'order_count': order_count,
		'workers_count': workers_count,
		'count': count,
	}
	return render(request, 'dashboard/order.html', context)


@login_required
def product_delete(request, pk):
	item = Product.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('dashboard-product')
	return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
	item = Product.objects.get(id=pk)
	if request.method=="POST":
		form = ProductForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('dashboard-product')
	else:
		form = ProductForm(instance=item)
	context = {
		'form': form,
		# 'item': item
	}
	return render(request, 'dashboard/product_update.html', context)
