from rest_framework import serializers
from .models import Pais, Departamento, Municipio

# Serializer para Pais
class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['nombre', 'codigo']


# Serializer para Departamento
class DepartamentoSerializer(serializers.ModelSerializer):
    # Incluir el nombre del país en lugar del ID
    pais = serializers.StringRelatedField()

    class Meta:
        model = Departamento
        fields = ['nombre', 'pais', 'codigo', 'active']


# Serializer para Municipio
class MunicipioSerializer(serializers.ModelSerializer):
    # Incluir el nombre del país en lugar del ID
    pais = serializers.StringRelatedField()

    class Meta:
        model = Municipio
        fields = ['nombre', 'pais', 'codigo', 'active']
