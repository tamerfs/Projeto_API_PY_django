from django.forms import ValidationError
from rest_framework import serializers
from provedor.models import Provedor, Servico

class ProvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provedor
        fields = '__all__'

class CadastrarProvedoresSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length = 100)
    preco = serializers.DecimalField(max_digits= 1000, decimal_places=2)
    descricao = serializers.CharField(max_length = 10000)
    foto = serializers.CharField(max_length = 1000)
    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError("Deve conter pelo menos três caracteres")
        return value

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

class CadastrarServicoSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length = 100)
    email = serializers.EmailField(max_length = 255)
    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError("Deve conter pelo menos três caracteres")
        return value