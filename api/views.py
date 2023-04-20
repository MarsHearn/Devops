from .models import test_model
from rest_framework import viewsets
from rest_framework import permissions
#from rest_framework import authentication
from .serializer import test_serializer

class test_viewset(viewsets.ModelViewSet):
    queryset = test_model.objects.all()
    serializer_class = test_serializer
    #authentication_classes = [authentication.SessionAuthentication] #test
    permission_classes = [permissions.IsAuthenticated]