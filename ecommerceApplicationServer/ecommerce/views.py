from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .tokenExtractor import getToken


class UserDetailsView(APIView):

    def get_object(self, userId):  # Not predefined in APIView class
        try:
            return User.objects.get(userId=userId)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):  # Predefined and gets invoked if a GET request is done
        try:
            userId = getToken(request)
        except Exception:
            return Response(
                {"message": "invalid token provided."},
                status=status.HTTP_401_UNAUTHORIZED)

        user = self.get_object(userId)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
