from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
# Import Models and Forms
from orders.models import Order
from orders.forms import orderForm,deliverForm
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class index(TemplateView):
    template_name = 'orders/index.html'

class order_query(TemplateView):
    template_name = 'orders/query.html'

class form_query(TemplateView):
    template_name = 'orders/form_query.html'

class order_create(SuccessMessageMixin,CreateView):
    model = Order
    form_class = orderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('index')
    success_message = 'Su formulario se envio con exito!'

@login_required
def order_edit(request,id):
    order = Order.objects.get(id=id)
    if request.method == 'GET':
        form = orderForm(instance=order)
    else:
        form = orderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('order_list')
    return render(request, 'orders/order_form_edit.html', {'form':form})

@login_required
def deliver_edit(request,id):
    order = Order.objects.get(id=id)
    if request.method == 'GET':
        form = deliverForm(instance=order)
    else:
        form = deliverForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('order_list')
    return render(request, 'orders/deliver_form.html', {'form':form})

@login_required
def order_list(request):
    order = Order.objects.all().order_by("-date_order")
    paginator = Paginator(order, 7)
    page = request.GET.get('page')
    order = paginator.get_page(page)
    contexto = {'object_list': order}
    return render (request, 'orders/order_list.html', contexto)

@login_required
def order_search_users(request):
    search = request.POST.get('search')
    if search:
        order = Order.objects.filter(document__contains=search)
    else:
        order = Order.objects.all()
        paginator = Paginator(order, 7)
        page = request.GET.get('page')
        order = paginator.get_page(page)
    context = {'object_list':order}
    return render(request, 'orders/search_users.html',context)

def order_search(request):
    try:
        search = request.POST.get('search')
        if search == "" or len(search) < 8 or len(search) > 8:
            messages.error(request, "Ingresá tu número de DNI sin puntos, si consideras que es un error ponte en ")
            return redirect("order_query")
        elif not search.isdigit():
            messages.error(request, "Ingresá tu número de DNI sin puntos, si consideras que es un error ponte en ")
            return redirect("order_query")
        elif search:
            order = Order.objects.get(document__exact=search)
    except Order.DoesNotExist:
        messages.error(request, "No tenemos registrada una solicitud con este DNI, si consideras que es un error ponte en ")
        return redirect('order_query')
    context = {'order':order}
    return render(request, 'orders/search.html',context)

def query_search(request):
    try:
        search = request.POST.get('search')
        if search == "" or len(search) < 8 or len(search) > 8:
            messages.error(request, "Ingresá tu número de DNI sin puntos")
            return redirect("form_query")
        elif not search.isdigit():
            messages.error(request, "Ingresá un DNI valido sin puntos")
            return redirect("form_query")
        elif search:
            order = Order.objects.get(document__exact=search)
            messages.error(request, "Ya tenemos registrada una solicitud con este DNI.")
        return render(request, 'orders/form_query.html')
    except Order.DoesNotExist:
        return redirect("order_new")

@login_required
def dates(request,id_order):
    order = Order.objects.get(id=id_order)
    contexto = {'order':order}
    return render(request,'orders/dates.html',contexto)

def contact(request):
    if request.method == 'POST':
        subject = request.POST['asunto']
        msg = request.POST['msg']+' '+request.POST['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['tapiaw38@gmail.com']
        send_mail(subject,msg,email_from,recipient_list)
        messages.success(request, "Mensaje enviado correctamente")
        return render(request,'orders/contact.html')

    return render(request,'orders/contact.html')
