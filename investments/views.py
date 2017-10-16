from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from investments.utils import get_links

@login_required
def lgd_in(request):
    #username = request.POST.get('id_username')
    #password = request.POST.get('id_password')
    #user = authenticate(username=username, password=password)
    return render(request, 'investments/logged_in.html')

def lgd_out(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next','/'))

def account(request):
    return HttpResponse("Account")

def register(request):
    if request.user.is_authenticated():
       return HttpResponseRedirect('/')
    else:
       if request.POST.get('name') is not None and request.POST.get('password') == request.POST.get('password2'):
         requesty = 'Passwords matchhh wooooo'
       else:
         requesty = 'Boooo'
       context = {'links': get_links(request.path), 'requesty': requesty}
       if request.POST.get('name'):
         return render(request, 'investments/register.html', context)
       else:
         return render(request, 'investments/register.html', context)

def haqqalla(request):
    return HttpResponse("6rbNJVhD2srz_V6q9y2tvD75s-ImDIRvZWyvCs5D3_M.5zuhqYTufukHSc-gAZ6bdu2U1GfCC9r8LHiGruDTlco")
