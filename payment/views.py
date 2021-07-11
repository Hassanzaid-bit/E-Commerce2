from django.shortcuts import render, redirect, get_object_or_404
import braintree
from django.conf import settings
from orders.models import Order
from .forms import MpesaForm
from django.http import HttpResponse
from .tasks import payment_completed

# INstantiate Braintree payment gateway
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def mpesa_payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        Mpesaform = MpesaForm(request.POST)
        if Mpesaform.is_valid():
            number = Mpesaform.cleaned_data["phone_number"] 
            request.session["phone_number"] = number
            return redirect("mpesa:lipa_na_mpesa")
   
    else:
        Mpesaform = MpesaForm()
        return render(request, 'payment/process.html', {'order':order, "Mpesaform":MpesaForm })



def braintree_payment_process(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == "POST":
        #retrieve nonce
        nonce = request.POST.get("payment_method_nonce", None)
        # create and submit transaction
        result = gateway.transaction.sale({
            "amount":f"{total_cost:.2f}",
            "payment_method_nonce" : nonce,
            "options" : {
                "submit_for_settlement" : True
            }
        })
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            #launch asynchronous tasks
            payment_completed.delay(order.id)
            return redirect("payment:done")
        else:
           return redirect("payment:canceled")
    else:
        #generate token
        client_token = gateway.client_token.generate()
        return render(request,
                      "payment/process.html",
                      {"order" : order,
                      "client_token" : client_token})










def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')