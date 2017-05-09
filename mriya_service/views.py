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

def index(request):
    return HttpResponseRedirect('/edit')

@login_required(login_url='/login/')
def execute(request):
    current_user = request.user
    if request.method == 'POST':
        try:
            query_obj = MyQuery.objects.get(user=current_user)
        except MyQuery.DoesNotExist:
            query_obj = None
        form = QueryForm(request.POST, instance=query_obj)
        sys.stderr.write(str(form.errors))
        if form.is_valid():
            form.cleaned_data['user'] = str(request.user)
            form.save()
            #return HttpResponse('Query executed')
            return HttpResponseRedirect('/edit')
        else:
            return HttpResponse('Bad request')
    else:
        return HttpResponseRedirect('/edit')

@login_required(login_url='/login/')
def edit_query(request):
    current_user = request.user
    # get saved query belonging to user
    try:
        saved_query = MyQuery.objects.get(user=current_user).query
        sys.stderr.write(saved_query)        
    except MyQuery.DoesNotExist:
        saved_query = None
    form = QueryForm(initial={'query':saved_query, 'user':current_user})
    return render(request, 'edit.html', {'form': form})
