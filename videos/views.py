from django.shortcuts import render
from django.http import JsonResponse
from .models import Video

def index(request):
  video = Video()
  response = video.search({"query": {"match_all": {}}})
  return JsonResponse(response)