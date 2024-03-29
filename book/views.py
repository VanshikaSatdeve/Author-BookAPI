from django.shortcuts import render
from .serializers import BookSerializer
from . models import Book
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, parsers
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # parser_classes = (parsers.FormParser,parsers.MultiPartParser, parsers.FileUploadParser)
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]



    def get_serializer_class(self):
        if self.action == 'list':
            return BookSerializer
        if self.action == 'create':
            return BookSerializer
        return self.serializer_class
        

    #get all authors
    def list(self,request):
        try:
            author_objs = Book.objects.all()
            serializer = self.get_serializer(author_objs, many = True)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #add author
    def create(self,request):
        try:
            serializer = self.get_serializer(data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data': serializer.data,
                'messaage':'Author added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single author
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:

                #author_objs = Author.objects.all()
                author_objs = self.get_object()
                serializer = self.get_serializer(author_objs)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update all fields of author
    def update(self,request, pk=None):
        try:
            #author_objs = Author.objects.all()
            author_objs = self.get_object()
            serializer = self.get_serializer(author_objs,data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'Author updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update specific fields
    def partial_update(self,request, pk=None):
        try:
            #author_objs = Author.objects.all()
            author_objs = self.get_object()
            serializer = self.get_serializer(author_objs,data=request.data,partial = True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'Author updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # delete specific author
    def destroy(self, request,pk):
        try:
            id=pk
            author_obj = self.get_object()
            author_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Author deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })




