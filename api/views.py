#from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Volunteer
from api.serializers import VolunteerSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def volunteer_list(request):
    if request.method == 'GET':
        volunteers = Volunteer.objects.all()
        group = request.GET.get('group', None)
        if group is not None:
            volunteers = volunteers.filter(group__icontains=group)
        volunteer_serializer = VolunteerSerializer(volunteers, many=True)
        return JsonResponse(volunteer_serializer.data, safe=False)
    elif request.method == 'POST':
        volunteer_data = JSONParser().parse(request)
        volunteer_serializer = VolunteerSerializer(data=volunteer_data)
        if volunteer_serializer.is_valid():
            volunteer_serializer.save()
            return JsonResponse(volunteer_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(volunteer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            count = Volunteer.objects.all().delete()
            return JsonResponse({'message': '{} Volunteers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)