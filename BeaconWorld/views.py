from django.shortcuts import render
from django.http import HttpResponse
from BeaconWorld.models import User
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def dashboard(request):
    '''
     give overview of user's collection
    '''
    all_users = User.objects.all()
    t = get_template('BeaconWorld/dashboard.html')
    html = t.render(Context({
        'users':all_users,
        'name_count': len(all_users),
        'half_count': len(all_users)/2 + 1
    }))
    return HttpResponse(html)


