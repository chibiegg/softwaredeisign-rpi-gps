# encoding=utf-8
import json
from PIL import Image
from django.shortcuts import render, get_object_or_404
from gpsnow.models import Waypoint, Transponder
from django.http.response import HttpResponse, Http404
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse


def index(request):
    return render(request, "index.html")

def waypoint_latest(request):
    data = {}
    for transponder in Transponder.objects.all():
        try:
            waypoint = Waypoint.objects.filter(transponder=transponder).order_by("-created")[0]
            data[transponder.name] = {
                                      "created":waypoint.created.isoformat(),
                                      "latitude":waypoint.latitude_10,
                                      "longitude":waypoint.longitude_10
                                      }
        except:
            data[transponder.name] = None

    return HttpResponse(json.dumps(data), content_type="application/json")


def list_transponders(request):
    data = [];
    for transponder in Transponder.objects.all():
        item = model_to_dict(transponder, fields=["name", "description"])
        item["marker"] = reverse("transponder_marker", args=(transponder.name,)) if transponder.marker else None
        item["marker_disabled"] = reverse("transponder_marker_disabled", args=(transponder.name,)) if transponder.marker_disabled else None
        data.append(item)

    return HttpResponse(json.dumps(data), content_type="application/json")


def transponder_marker(request, name, disabled=False):
    transponder = get_object_or_404(Transponder, name=name)

    if disabled:
        marker = transponder.marker_disabled
    else:
        marker = transponder.marker

    if not marker:
        raise Http404

    response = HttpResponse(content_type="image/png")
    img = Image.open(marker)
    img.save(response, format="png")
    return response
