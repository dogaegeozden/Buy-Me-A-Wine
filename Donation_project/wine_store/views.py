# LIBRARIES
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from django.conf import settings
import stripe

# MODELS
from wine_store.models import (
    HomePageMetaDescription,
    HomePageHookLine, 
    Message,
)

# FORMS
from .forms import MessageForm

# Configuring debugging feature code
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Hint: Comment out this line to enable debugging.
# disable(CRITICAL)



##############################

# WINE STORE PAGE

##############################

def home(request):
    """A view function rendering the wine store page."""

    all_meta_description_objs = HomePageMetaDescription.objects.all()
    all_hook_line_ojbs = HomePageHookLine.objects.all()

    message_form = MessageForm()

    if request.method == "POST" and "submitMsgBtn" in request.POST:
    
        message_form = MessageForm(request.POST)
    
        if message_form.is_valid():

            # Store values in session
            request.session['full_name'] = message_form.cleaned_data['full_name']
            request.session['email'] = message_form.cleaned_data['email']
            request.session['message'] = message_form.cleaned_data['message']
            request.session['message_created'] = False

            return HttpResponseRedirect("/checkout/")
    
        else:
    
            debug(message_form.errors)

    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_hook_line_ojbs': all_hook_line_ojbs,
    }

    return render(request, "wine_store/home.html", context=context)



##############################

# SUCCESS PAGE

##############################

def success(request):
    """A view function rendering the success page."""
    
    if not request.session.get('message_created', False):
        debug(f"Full Name: {request.session.get('full_name')}")
        debug(f"Email: {request.session.get('email')}")
        debug(f"Message: {request.session.get('message')}")

        Message.objects.create(
            full_name=request.session.get('full_name'),
            email=request.session.get('email'),
            message=request.session.get('message')
        )

        request.session['message_created'] = True

    context = {}

    return render(request, "wine_store/success.html", context=context)



##############################

# CANCEL PAGE

##############################

def cancel(request):
    """A view function rendering the cancel page."""

    context = {}

    return render(request, "wine_store/cancel.html", context=context)



##############################

# CHECKOUT PAGE

##############################

def checkout(request):
    """A view function to display the checkout page."""

    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    try:

        # Create a Stripe checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': settings.STRIPE_DONATION_PRODUCT_PRICE_ID,
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )

        return HttpResponseRedirect(session.url)

    except Exception as e:

        return HttpResponse('Error: ' + str(e))