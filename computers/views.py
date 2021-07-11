from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Computer, Portable, Desktop, Review, CPU, Memory, Storage, Graphics, OS
from .forms import ReviewForm, ImageForm
from cart.forms import CartAddProductForm


def home(request):
    computers = Computer.objects.all()[0:3]
    return render(request, 'index.html', {'computers' : computers})

def computers(request):
    computers = Computer.objects.all()[0:6]
    return render(request,'computers/computers.html', {'computers':computers})

def products(request):
    computers = Computer.objects.all()
    return render(request, 'computers/products.html', {'computers':computers} )

def product_details(request, pk):
    computer = get_object_or_404(Computer, id=pk)
    cart_product_form = CartAddProductForm()

    reviews = Review.objects.all()
    cpu = CPU.objects.get(id=1)
    memory = Memory.objects.get(id=1)
    storage = Storage.objects.get(id=1)
    graphics = Graphics.objects.get(id=1)
    os = OS.objects.get(id=1)

    new_review = None

    if request.method == 'POST':
        # A comment was posted
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            # Create comment object but don't save to the database yet
            new_review = review_form.save(commit=False)
            # Assign the current post to the comment
            new_review.computer = computer
            # Save the comment to the database
            new_review.save()
    else:
        review_form = ReviewForm()

    return render(request, "computers/product_details.html", {'computer':computer, 
                                                              'cart_product_form': cart_product_form, 
                                                              'review_form' : review_form,
                                                              'reviews' : reviews,
                                                              'new_review' : new_review,
                                                              "cpu": cpu,
                                                              "memory":memory,
                                                              "storage":storage,
                                                              "graphics":graphics,
                                                              "os":os})




def payment(request):
    return render(request, "computers/payment.html")


def computer_upload_view(request):

    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES) 
        if image_form.is_valid():
            image_form.save()
            return HttpResponse("It worked")
    else:
        image_form = ImageForm()
    return render(request, 'computers/sell.html', {"form" : image_form} )