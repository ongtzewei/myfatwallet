from api.models import Inventory, Transaction
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django_hosts.resolvers import reverse


@require_http_methods(['GET'])
def get_signout(request, *args, **kwargs):
    logout(request)
    return redirect(reverse('website-main', host='default'))


@require_http_methods(['GET',])
@login_required
def get_main(request, *args, **kwargs):
    return render_to_response('app/main.html', None,
                              context_instance=RequestContext(request))


@require_http_methods(['GET',])
@login_required
def get_inventory(request, *args, **kwargs):
    inventory = bool('pk' in kwargs) and Inventory.objects.get(pk=kwargs['pk']) or None
    return render_to_response('app/inventory.html', {'inventory':inventory},
                              context_instance=RequestContext(request))


@require_http_methods(['GET',])
@login_required
def manage_inventory(request, *args, **kwargs):
    inventory = Inventory.objects.all()
    return render_to_response('app/inventory-management.html', {'inventory':inventory},
                              context_instance=RequestContext(request))


@require_http_methods(['GET',])
@login_required
def get_confirm(request, *args, **kwargs):
    inventory = bool('pk' in kwargs) and Inventory.objects.get(pk=kwargs['pk']) or None
    return render_to_response('app/confirm.html', {'inventory':inventory},
                              context_instance=RequestContext(request))


@require_http_methods(['GET',])
@login_required
def get_transaction(request, *args, **kwargs):
    #transaction = Transaction.objects.get(pk=kwargs['pk'])
    transaction = None
    return render_to_response('app/transaction.html', {'transaction':transaction},
                              context_instance=RequestContext(request))

