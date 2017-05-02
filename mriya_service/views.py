from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.template.loader import get_template
from mriya_service.models import LoginUser

def index(request):
    user_id = request.POST.get('user', None)
    try:
        user = LoginUser.objects.get(user_id)
    except:
        user = None
    template = get_template('index.html')
    context = {
        'logged_as_user': user,
    }
    return HttpResponse(template.render(context, request))

def edit_query(request):
    return HttpResponse("Edit query.")
