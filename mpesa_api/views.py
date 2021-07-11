import requests
import json
import base64
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from django.shortcuts import render, redirect, get_object_or_404


business_shortCode = "174379" #paybill number
#phone_number = "254713369784"
lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
consumer_keyy = "7y5JAcKCeOAjODAhR7gBBOppnBG8wwlm"
consumer_secrett = "VbY93kVWVEecsLPQ"


def getAccessToken():
    consumer_key = consumer_keyy
    consumer_secret = consumer_secrett
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return validated_mpesa_access_token
 

def lipa_na_mpesa(request):
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    data_to_encode = business_shortCode + lipa_na_mpesa_passkey + formatted_time
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode('utf-8')
    access_token = getAccessToken()
    
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization" : "Bearer %s" % access_token}

    request = {
        "BusinessShortCode" : business_shortCode,
        "Password" : decoded_password,
        "Timestamp" : formatted_time,
        "TransactionType" : "CustomerPayBillOnline",
        "Amount" : "1",
        "PartyA" : request.session.get("phone_number"),
        "PartyB" : business_shortCode,
        "PhoneNumber" :request.session.get("phone_number"),
        "CallBackURL" : "https://djangofullstack.com/lipanampesa/",
        "AccountReference" : "Test Aware",
        "TransactionDesc" : "Pay Hassan"
    }

    response = requests.post(api_url, json=request, headers=headers)

    #return HttpResponse("success")
    return redirect("payment:done")
