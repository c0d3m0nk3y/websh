import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from rockety.models import Rocket

logger = logging.getLogger(__name__)


class Index(TemplateView):
    template_name = 'strappy/index.html'

    def get(self, request):
        logger.warning('hmm')
        return render(
            request,
            self.template_name,
            {
                'rockets': Rocket.objects.all(),
            },
        )


class Hijack(TemplateView):
    template_name = 'strappy/hijack.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {},
        )
