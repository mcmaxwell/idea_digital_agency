from django.shortcuts import render
from .models import ContactInfo, Subscriber
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response,redirect
from feincms.module.page.models import Page
from blog.models import Blog
from cases.models import Case

# Create your views here.
def add_contact_form(request):
    if request.GET:
        first_name = request.GET['first']
        second_name = request.GET['second']
        email = request.GET['email']
        phone = request.GET['phone']
        budget = request.GET['budget']
        company = request.GET['company']
        message = request.GET['message']
        save_object = ContactInfo(first_name=first_name, second_name=second_name,
                                         email=email, phone=phone, budget=budget,
                                         company=company, message=message
                                         )
        save_object.save()

        return redirect('/')

def add_subscriber(request):
    if request.GET:
        name = request.GET['name']
        email = request.GET['email']
        save_object = Subscriber(name=name, email=email)
        save_object.save()

        return redirect('/')



def site_map(request):
    pages = Page.objects.all()
    blogs = Blog.objects.all()
    cases = Case.objects.all()

    response = render_to_response('sitemap.xml', {'pages': pages,'blogs': blogs, 'cases': cases})
    response['Content-Type'] = 'application/xml;'
    return response
