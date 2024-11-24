from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from app_optimus.models.banner import Banner
from app_optimus.serializers.banner import BannerSerializer

class BannerDetailView(APIView):
    def get(self, request, pk):
        banner = get_object_or_404(Banner, pk=pk)
        banner_serialized = BannerSerializer(banner).data
        return Response(banner_serialized, status=status.HTTP_200_OK)