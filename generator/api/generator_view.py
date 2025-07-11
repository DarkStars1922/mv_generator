import os
import uuid
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from ..utils import mock_agent1, mock_agent2, mock_agent3, mock_agent4

class generate_prompt(APIView):
    def post(self,request):
        try:
            image = request.FILES.get('image')
            prompt = request.POST.get('prompt', '')
            new_prompt = mock_agent1(image, prompt)
            return Response({'prompt':new_prompt},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
    

class generate_music(APIView):
    def post(self,request):
        try:
            prompt = request.POST.get('prompt', '')
            music_data = mock_agent2(prompt) 
            filename = f"music_{uuid.uuid4()}.mp3"
            filepath = default_storage.save(filename, music_data)
            music_url = request.build_absolute_uri(default_storage.url(filepath))
            return Response({'music_url':music_url},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

class generate_images(APIView):
    def post(self,request):
        try:
            prompt = request.POST.get('prompt', '')
            image_urls = mock_agent3(prompt)  
            return Response({'image_urls':image_urls},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

class generate_video(APIView): 
    def get(self,request):
        return render(request)
    
    def post(self,request):
        try:
            images = request.FILES.getlist('images')  
            music = request.FILES.get('music')      
            video_data = mock_agent4(images, music)
            filename = f"video_{uuid.uuid4()}.mp4"
            filepath = default_storage.save(filename, video_data)
            video_url = request.build_absolute_uri(default_storage.url(filepath))
            return Response({'video_url':video_url},status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)