from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.template.loader import render_to_string
from .models import Case
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create your views here.
class CaseView(DetailView):
    model = Case

    def get_queryset(self):
        return Case.objects.filter(slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        cases = Case.objects.all()
        case = Case.objects.get(slug=self.kwargs.get('slug'))
        context = super(CaseView, self).get_context_data(**kwargs)
        context['cases'] = cases
        return context
