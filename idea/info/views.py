# -*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from .models import ContactInfo, Subscriber
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response,redirect
from feincms.module.page.models import Page
from blog.models import Blog
from cases.models import Case
from amocrm import amo_settings
from .crm_utils import Contact, Lead
from django.core.mail import send_mail

amo_settings.set('ideadigitalukraine@gmail.com', '00e79897bdda78ca52e7fdbcf2b710a9', 'ideadigital')
#amo_settings.set('alexrians@gmail.com', 'c8bad8aedb1d614006877dfbf693a5ef', 'ideatest1')

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
                                         company=company, message=message,
                                         )
        save_object.save()

        new_contact = Contact(name=first_name + ' ' + second_name, company=company, position='QA', phone=phone, email=email,)
        new_contact.email = email
        new_contact.save()

        new_lead = Lead(name=company, budget=budget.replace("$", ""),  contact=new_contact.id, email=email,)
        new_lead.save()
        new_contact.leads = new_lead
        new_contact.save()

        return redirect('/')

def add_subscriber(request):
    if request.GET:
        name = request.GET['name']
        email = request.GET['email']
        save_object = Subscriber(name=name, email=email)
        save_object.save()

        return redirect('/')


def callback_form(request):
    if request.GET:
        name = request.GET['name']
        phone = request.GET['phone']
        comment = request.GET['comment']

        try:
            service = request.GET['select']
        except:
            service = None

        try:
            form_name = request.GET['form_name']
        except:
            form_name = None

        new_contact = Contact(name=name, company='FastCall{0}'.format(datetime.now().strftime("%Y-%m-%d %H:%M")), position='QA', phone=phone, email=form_name,)
        new_contact.save()

        new_lead = Lead(name='FastCall - ({0})'.format(datetime.now().strftime("%Y-%m-%d %H:%M")), budget="1000",  contact=new_contact.id, email=form_name,)
        new_lead.save()
        new_contact.leads = new_lead
        new_contact.save()


        # new_contact = Contact(name=name, company='FastCall', position='QA', phone=phone, email="nodata@data.com",)
        # new_contact.save()

        send_mail('Idea Callback Form', name + " " + phone + " " + comment + " " + service, 'bot.idea@yandex.ru', ['ideadigitalclients@gmail.com',])



def site_map(request):
    pages = Page.objects.all()
    blogs = Blog.objects.all()
    cases = Case.objects.all()

    response = render_to_response('sitemap.xml', {'pages': pages,'blogs': blogs, 'cases': cases})
    response['Content-Type'] = 'application/xml;'
    return response
