import sys
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.loader import get_template
from django import forms # for runtime altering
from .models import MyQuery, Config
from .forms import QueryForm, ConfigForm
from .mriya_interface import config_items_f, save_uploaded_config_f, config_items
from .mriya_interface import config_name, config_choices

def index(request):
    return HttpResponseRedirect('/edit')

@login_required(login_url='/login/')
def execute(request):
    if request.method == 'POST':
        current_user = request.user
        try:
            query_obj = MyQuery.objects.get(user=current_user)
            form = QueryForm(request.POST, instance=query_obj)
        except MyQuery.DoesNotExist:
            form = QueryForm(request.POST)
        if form.is_valid():
            form.cleaned_data['user'] = str(request.user)
            form.save()
            return HttpResponseRedirect('/edit')
        else:
            return render(request, 'error.html', {'error': str(form.errors)})
    else:
        return HttpResponseRedirect('/edit')

@login_required(login_url='/login/')
def edit_query(request):
    current_user = request.user
    choices = config_choices(current_user)
    # get saved query belonging to user
    try:
        query_obj = MyQuery.objects.get(user=current_user)
        saved_query = query_obj.query
        src = query_obj.src
        dst = query_obj.dst
        sys.stderr.write(saved_query)        
    except MyQuery.DoesNotExist:
        saved_query = None
        src = None
        dst = None
    form = QueryForm(initial={'query':saved_query,
                              'user':current_user,
                              'src':src,
                              'dst': dst},
                     src_choices=choices, dst_choices=choices)
    return render(request, 'edit.html', {'form': form})

@login_required(login_url='/login/')
def config(request):
    status = ''
    current_user = request.user
    if request.method == 'POST':
        try:
            config_obj = Config.objects.get(user=current_user)
        except Config.DoesNotExist:
            config_obj = None
        form = ConfigForm(request.POST, instance=config_obj)
        # make config required to raise an error
        if 'config' not in request.FILES:
            form.fields['config'] = forms.FileField(required=True)
        #
        if form.is_valid():
            conf_items = config_items_f(request.FILES['config'])
            if not conf_items:
                return render(request, 'error.html',
                              {'error':"Config doesn't contains endpoint data sections"})
            form.cleaned_data['user'] = str(request.user)
            save_uploaded_config_f(request.FILES['config'], current_user)
            form.save()
            status = 'new'
        else:
            return render(request, 'error.html', {'error': str(form.errors)})

    items = config_items(current_user)
    form = ConfigForm(initial={'user':current_user})
    return render(request, 'config.html', {'form': form,
                                           'status': status,
                                           'items': items})
