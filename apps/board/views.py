import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

from ..common.exceptions import EntityDoesNotExist
from .serializers import TicketSerializer


class ViewWrapper(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        body, status = self.view_factory.create().get(**kwargs)

        return HttpResponse(
            json.dumps(body),
            status=status,
            content_type='application/json'
        )

    def post(self, request, *args, **kwargs):
        body, status = self.view_factory.create().post(**kwargs)

        return HttpResponse(
            json.dumps(body),
            status=status,
            content_type='application/json'
        )

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ViewWrapper, self).dispatch(*args, **kwargs)



class TicketView:

    def __init__(self, ticket_interactor):
        self.ticket_interactor = ticket_interactor

    # def get(self, identify: int):
    def get(self, **kwargs):
        try:
            if "identify" in kwargs:
                identify = kwargs['identify']
                ticket = self.ticket_interactor.set_params(
                    identify
                ).execute()
            else:
                ticket = self.ticket_interactor.set_params().execute()
        except EntityDoesNotExist:
            body = {
                'error': 'Ticket does not exist!'
            }
            status = 404
        else:
            body = TicketSerializer.serialize(ticket)
            status = 200
        
        return body, status

    def post(self, **kwargs):
        
        return {'post': "POST"}, 200
