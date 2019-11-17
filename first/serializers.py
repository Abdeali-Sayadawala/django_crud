# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Note

class NoteSerializers(serializers.ModelSerializer):
    many = True
    class Meta:
        model = Note
        fields = ('title', 'description')

