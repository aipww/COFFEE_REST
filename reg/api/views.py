from rest_framework import generics
from reg.models import UserReg
from .serializers import UserRegSerializer


class RegView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    serializer_class = UserRegSerializer

    def get_queryset(self):
        return UserReg.objects.all()
