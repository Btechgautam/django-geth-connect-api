# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

base_rpc_url = 'http://localhost:8545'
rpc_headers = {'Content-Type': 'application/json'}


@csrf_exempt
def new_account(request):
    passphrase = request.POST.get('passphrase')
    response = requests.post(base_rpc_url,
                             data='{"jsonrpc": "2.0", "method": "personal_newAccount", "params": ["' +
                                  passphrase + '"], "id": 1}',
                             headers=rpc_headers)
    return HttpResponse(response.content, content_type='application/json')


@csrf_exempt
def lock_account(request):
    address = request.POST.get('address')
    response = requests.post(base_rpc_url,
                             data='{"jsonrpc": "2.0", "method": "personal_lockAccount", "params": ["' +
                                  address + '"], "id": 1}',
                             headers=rpc_headers)
    return HttpResponse(response.content, content_type='application/json')


@csrf_exempt
def unlock_account(request):
    address = request.POST.get('address')
    passphrase = request.POST.get('passphrase')
    duration = request.POST.get('duration') or '300'
    response = requests.post(base_rpc_url,
                             data='{"jsonrpc": "2.0", "method": "personal_unlockAccount", "params": ["' +
                                  address + '", "' + passphrase + '",' + duration + ' ], "id": 1}',
                             headers=rpc_headers)
    return HttpResponse(response.content, content_type='application/json')
