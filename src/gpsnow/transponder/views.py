# encoding=utf-8

from django.views.decorators.http import require_http_methods
from gpsnow.transponder.forms import WaypointForm
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(['POST'])
def add_waypoint(request):
    
    form = WaypointForm(request.POST)
    if not form.is_valid():
        errors = "\n".join(["{0} : {1}".format(k, ",".join(v)) for k, v in form.errors.items()])
        return HttpResponse(errors, status=400)

    form.save()

    return HttpResponse("OK")
