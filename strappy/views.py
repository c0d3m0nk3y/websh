import logging

from django.shortcuts import render
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)

class Index(TemplateView):
    template_name = 'strappy/index.html'

    def get(self, request):
        logger.warning('hmm')
        return render(
            request,
            self.template_name,
            {},
        )
