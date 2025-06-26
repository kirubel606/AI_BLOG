from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from accounts.serializers import UserSerializer


User = get_user_model()


class SignupView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        user = request.user

        if not (user.is_admin and user.has_perm("accounts.add_user")):
            return Response(
                {"detail": "You do not have permission to create users."},
                status=status.HTTP_403_FORBIDDEN,
            )

        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response(
                data={
                    "message": "User created successfully",
                    "user": user_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            data={"message": user_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def put(self, request, *args, **kwargs):
        if not hasattr(request, "_data"):
            request._load_data_and_files()

        user = request.user
        if not (user.is_staff and user.has_perm("accounts.change_user")):
            return Response(
                {"detail": "You do not have permission to update users."},
                status=status.HTTP_403_FORBIDDEN,
            )

        pk = kwargs.get("pk")
        if not pk:
            return Response(
                {"message": "User ID required for update"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user_instance = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "User updated successfully",
                "user": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class UsersListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        user = request.user

        if not user.has_perm("accounts.view_user"):
            return Response(
                {"detail": "You do not have permission to view users."},
                status=status.HTTP_403_FORBIDDEN
            )

        all_users = User.objects.all()
        total_count = User.objects.count()
        user_serializer = UserSerializer(instance=all_users, many=True)
        return Response(data={'total_count': total_count, 'users': user_serializer.data}, status=status.HTTP_200_OK)

class UserDetailView(APIView):
    parser_classes = [JSONParser,MultiPartParser, FormParser]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        try:
            user = User.objects.get(pk=request.user.id)
            user_serializer = UserSerializer(instance=user)
            return Response(data=user_serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(data={'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request) -> Response:
        try:
            user = User.objects.get(pk=request.user.id)
            user_serializer = UserSerializer(
                instance=user, data=request.data, partial=True)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
                return Response(
                    data={
                        'message': 'User credentials updated successfully',
                        'user': user_serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            return Response(data={'message': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(data={'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, pk=None) -> Response:
        user = request.user

        # Check for admin + permission
        if not user.is_staff or not user.has_perm('accounts.delete_user'):
            return Response(
                {"detail": "You do not have permission to delete users."},
                status=status.HTTP_403_FORBIDDEN
            )

        if not pk:
            return Response(
                {"detail": "User ID required for deletion."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            target_user = User.objects.get(pk=pk)
            target_user.delete()

            return Response(
                data={'message': f'User {target_user.username} deleted successfully'},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                data={'message': 'User does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )



from django.contrib.auth.models import Permission

class PermissionsListView(APIView):
    permission_classes = [IsAuthenticated]  # adjust as needed

    def get(self, request):
        permissions = Permission.objects.all().values('id', 'codename', 'name')
        return Response({"permissions": list(permissions)})
