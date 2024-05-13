from rest_framework import serializers
from drf.models import Book, User


class BookSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=32, required=False)
    owned_date = serializers.DateField(required=False)
    current_position = serializers.CharField(max_length=255, required=False)
    reading_process = serializers.CharField(max_length=255, required=False)
    readings = serializers.IntegerField(required=False)
    remove_status = serializers.BooleanField(required=False)

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        book_count = Book.objects.filter(id=instance.id).update(**validated_data)
        if book_count > 0:
            updated_book = Book.objects.get(id=instance.id)
            return updated_book
        return None


class GetOneBookModelSerializers(serializers.ModelSerializer):
    date = serializers.DateField(source='owned_date')

    class Meta:
        model = Book
        fields = ['id', 'title', 'date']


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['address']
