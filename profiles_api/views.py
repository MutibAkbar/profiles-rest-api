from rest_framework.views import APIView        #imports APIVies class from rest_framework model
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you control over application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})

    def post(self, request):
         """Create a hello message with our name"""
         serializer = self.serializer_class(data=request.data)

         if serializer.is_valid():
             name = serializer.validated_data.get('name')
             message = f'Hello {name}'
             return Response({'message':message})
         return Response(
             serializer.errors,
             status = status.HTTP_400_BAD_REQUEST
         )
    def put(self, request, pk=None):  #as we update a single object, so pk is used for specifying object id
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle updating an object partially"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
       """Delete an object"""
       return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
        'Uses actionns (list, create, retrieve, update, partially_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'method':'DELETE'})
