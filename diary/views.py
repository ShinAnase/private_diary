from django.shortcuts import render
from django.views import generic
from .forms import  inquiryForm

class IndexView(generic.TemplateView):
    template_name = "index.html"

class inquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = inquiryForm