from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

@api_view(('GET',))
def testAPI(request):
    return Response({'Error': 'test api'}, status=status.HTTP_204_NO_CONTENT)
