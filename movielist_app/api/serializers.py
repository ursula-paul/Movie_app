from wsgiref import validate
from rest_framework import serializers
from movielist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields= '__all__'
        
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and Description should not be same ')
        else:
            return data
        
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name too short')
        else:
            return value
        
        

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name too short')
#     else:
#         return value
        
        
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     # def update(self, instance, validated_data):
#     #     return Movie.objects.filter(pk=instance.id).update(**validated_data)
    
#     def update(self, instance, validated_data):
#         print(instance)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should not be same ')
#         return data
        
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name too short')
    #     else:
    #         return value
        
        
    
        
    # class MoviedetailsSerializer(serializers.Serializer):
    #     movie = serializers.IntegerField
    #     description = serializers.CharField
    #     active = serializers.CharField
    