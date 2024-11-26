from rest_framework.response import Response
from rest_framework.views import APIView
from firstapp.models import userModel
from firstapp.serializers import userSerializer, createUserSerializer
from rest_framework import status
from django.http import *

class userProfileView(APIView):

    def get_object(self, id):
        try:
            return userModel.objects.get(id=id)
        except userModel.DoesNotExist:
            raise Http404

    def get(self, request, id=None):
        if not id:
            req_data = userModel.objects.all()
            serializer = userSerializer(req_data, many=True)
            return Response(serializer.data)
        else:
            req_data = self.get_object(id)
            serializer = userSerializer(req_data)
            return Response(serializer.data)

    
    def post(self, request):
        serializer = createUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    def put(self, request, id):
        obj_data = self.get_object(id=id)
        serializer = createUserSerializer(obj_data, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        req_data = self.get_object(id=id)
        req_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










# @api_view(['GET','POST'])
# def users(request):
#     if request.method == 'GET':
#         data = userModel.objects.all()
#         serialData = userSerializer(data, many=True)
#         return Response(serialData.data)
#     elif request.method == 'POST':
#         req_data = request.data
#         serializer = createUserSerializer(data=req_data)

#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)