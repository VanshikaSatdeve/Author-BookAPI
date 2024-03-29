from django.shortcuts import render
from .serializers import AuthorSerializer, AuthorDetailSerializer,AuthorImageSerilizer
from . models import Author
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, parsers
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
# Create your views here.


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    parser_classes = (parsers.FormParser,parsers.MultiPartParser, parsers.FileUploadParser)
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.

    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorDetailSerializer
        if self.action == 'create':
            return AuthorSerializer
        elif self.action == 'upload_image':
            return AuthorImageSerilizer
        return self.serializer_class

    @action(methods=['POST'],detail=True,url_path='upload-image')
    def upload_image(self,request,pk=None):

        author_objs = self.get_object()
        serializer = self.get_serializer(author_objs,data=request.data)

        if not serializer.is_valid():
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'errors': serializer.errors,
                'message':'Invalid data'
            })

        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            'data': serializer.data,
            'message':'Author image added successfully'
        })



    #get all authors
    def list(self,request):
        try:
            author_objs = Author.objects.all()
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



