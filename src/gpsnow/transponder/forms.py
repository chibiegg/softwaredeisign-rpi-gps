# encoding=utf-8

from django import forms
from gpsnow.models import Transponder, Waypoint

class WaypointForm(forms.ModelForm):

    class Meta:
        model = Waypoint
        fields = ("transponder", "created", "latitude", "longitude")

    transponder = forms.ModelChoiceField(queryset=Transponder.objects.all(), to_field_name='name')


