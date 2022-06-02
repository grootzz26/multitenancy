from django.shortcuts import render
from django.http import HttpResponse
from .models import Tenant, members
# Create your views here.

from .utilities import get_tenant


def our_team(request):
    if request.method == 'GET':
        tenant=get_tenant(request)
        member = members.objects.filter(tenant=tenant).first()
        print(request)
        return render(request, 'home.html',{'tenant':tenant, 'member':member})
    if request.method == 'POST':
        pass