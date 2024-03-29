from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    #specify model name and field inside meta class
    class Meta:
        model = Author
        fields = ['id','name','city']
        read_only_fields = ['id']
        
        
class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields=AuthorSerializer.Meta.fields+['image']
        read_only_fields = ['id']
        
class AuthorImageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields=['id','image']
        read_only_fields = ['id']