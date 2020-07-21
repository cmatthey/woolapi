from rest_framework import serializers
from api.models import Volunteer

class VolunteerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer
        fields = ("id", "name", "group", "created")