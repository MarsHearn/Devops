#序列化是指把数据库模型转换为JSON
from .models import test_model
from rest_framework import serializers

class test_serializer(serializers.ModelSerializer):  #派生类 derived class
    class Meta:
        model = test_model
        fields = ['t1', 't2']
