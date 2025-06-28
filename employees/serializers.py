from rest_framework import serializers
from .models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'full_name', 'email', 'department', 'get_role']  # I excluded sensitive fields here

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['id', 'full_name', 'email', 'mentor', 'internship_end', 'get_role']  # I excluded sensitive fields here
