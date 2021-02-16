from django.shortcuts import render
from django.views import generic
from .forms import  inquiryForm
import logging
from django.urls import reverse_lazy

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"

class inquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = inquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_mail()
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

