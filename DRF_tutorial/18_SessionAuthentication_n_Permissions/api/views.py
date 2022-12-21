from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly ,AllowAny , DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated] # perrmission only when user is authenticated
    # permission_classes = [AllowAny] # All permission to all user
    # permission_class =[IsAuthenticatedOrReadOnly] # if user is authenticated all permission or  only read get() permisision
    # permission_classes = [DjangoModelPermissions] # user must authenticated and user which have specific permission that can only specific activity
                                                  # deafult get permission
    
    permission_classes =[DjangoModelPermissionsOrAnonReadOnly] # unauthenticated user can read here

    

    
    