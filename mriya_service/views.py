import sys
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.loader import get_template
from .models import MyQuery
from .forms import QueryForm
from .forms import LoginForm

def index(request):
    return HttpResponseRedirect('/edit')

@login_required(login_url='/login/')
def execute(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            form.data['user'] = request.user
            query = form.cleaned_data['query']
            form.save()
            return HttpResponse('Query executed')
        else:
            return HttpResponse('Bad request')
    else:
        return HttpResponseRedirect('/edit')

#@login_required(login_url='/login/')
def edit_query(request):
    current_user = request.user
    # get saved query belonging to user
    try:
        saved_query = MyQuery.objects.get(user=current_user).query
        sys.stderr.write(saved_query)        
    except MyQuery.DoesNotExist:
        saved_query = None
    form = QueryForm(initial={'query':saved_query})
    return render(request, 'edit.html', {'form': form})
