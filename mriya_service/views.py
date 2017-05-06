from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import render
from django.template.loader import get_template
from mriya_service.forms import LoginForm
from mriya_service.models import Login

def index(request):
    return HttpResponseRedirect('/login')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
    try:
        user = Login.objects.get()
    except:
        user = None
    form = LoginForm(initial={'user':user})

    # from django.db import connection
    # import sys
    # tables = connection.introspection.table_names()
    # sys.stderr.write(str(tables))
    # seen_models = connection.introspection.installed_models(tables)
    # sys.stderr.write(str(seen_models))
    # sys.stderr.write(str(connection.settings_dict))
    
    return render(request, 'login.html', {'form': form})

def edit_query(request):
    return HttpResponse("Edit query.")
