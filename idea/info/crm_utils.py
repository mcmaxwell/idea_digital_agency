# -*- coding: utf-8 -*-

from amocrm import BaseContact, BaseLead, fields, LeadsManager

class Contact(BaseContact):
    position = fields.CustomField(u'Должность')
    site = fields.CustomField(u'Сайт')
    email = fields.EnumCustomField(u'Email', enum='WORK')
    phone = fields.EnumCustomField(u'Телефон', enum='WORK')

class Lead(BaseLead):
    position = fields.CustomField(u'Должность')
    site = fields.CustomField(u'Сайт')
    #email = fields.CustomField(u'Email')
    phone = fields.EnumCustomField(u'Телефон', enum='WORK')
    status = fields._StatusTypeField()
