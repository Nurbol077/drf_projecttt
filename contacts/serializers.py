from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, allow_blank=True)
    phone = serializers.CharField(max_length=50, allow_blank=True)
    class Meta:
        model = Contact
        fields = '__all__'

    def validate_name(self, value):
        if value.strip() == "":
            raise serializers.ValidationError("Аты бош болбошу керек")
        return value

    def validate_phone(self, value):
        if len(value) < 12:
            raise serializers.ValidationError('Телефон номери кыска')
        return value