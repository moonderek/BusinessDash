from rest_framework import generics, permissions
from rest_framework.response import Response 
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


#Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.validate_email(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context).data,
            "token": AuthToken.objects.create(user)[1]

        })
        '''
        {
            "user": {
                "id": 2,
                "username": "peter",
                "email": "peter@email.com"
            },
            "token": "e1fe0b0d6d3db5726e88f06725b5715261f13b92600804e6ca63f3ba81f6bb18"
        }
        '''

#Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context).data,
            "token": AuthToken.objects.create(user)[1]

        })

#Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

        '''
        In Auth header => Token 4w545940358
        '''