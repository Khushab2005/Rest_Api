from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from myapp.models import Employee
from myapp.serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.decorators import api_view , APIView
from rest_framework.response import Response 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination 
from django.contrib.auth.models import User

# ----------------------Token authentication----------------
# -----------start-------
from rest_framework.authtoken.models import Token
user = User.objects.get(username='Admin')  # use your real username
token, created = Token.objects.get_or_create(user=user)
print("1")
print(token.key)



# -----------end-------
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication





@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def secure_data(request):
    return Response({'Message': 'Secure Data'})






# ------------------Custom pagination -----------------
class customPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100
    



# ----------------Generic Base Api -------------------
# -----------start-------
class genericlistcreate(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]  
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'email','gender']

    
      
    
class genericretriveupdatedestroy(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
# ------------end-------    


    
# ----------------Function Base Api -------------------
# ---------start---------
@api_view(['GET'])
def f_get(request):
    emp = Employee.objects.all()
    Pagination = customPagination()
    data = Pagination.paginate_queryset(emp, request)
    ser = EmployeeSerializer(data, many=True)
    return Pagination.get_paginated_response(ser.data)


@api_view(['POST'])
def f_post(request):
    ser = EmployeeSerializer(data = request.data)
    if ser.is_valid():
        ser.save()
        return Response({"message": "Employee created successfully"},status=status.HTTP_201_CREATED)
    
    return Response({"error": ser.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def f_put(request, id):
    data = get_object_or_404(Employee,id=id)
    ser = EmployeeSerializer(data,request.data)
    if ser.is_valid():
        ser.save()
        return Response({"message": "Employee updated successfully"},status=status.HTTP_200_OK)
    return Response({"error": ser.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def f_patch(request, id):
    data = get_object_or_404(Employee,id=id)
    ser = EmployeeSerializer(data,request.data, partial=True)
    if ser.is_valid():
        ser.save()
        return Response({"message": "Employee updated successfully"},status=status.HTTP_200_OK)
    return Response({"error": ser.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def f_delete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return Response({"message": "Employee deleted successfully"},status=status.HTTP_204_NO_CONTENT)

# -----------end-------


    
# ----------------Class Base Api -------------------
# ---------start---------
class Class_Employe(APIView):
    def get(self, request):
        emp = Employee.objects.all()
        Pagination = customPagination()
        data = Pagination.paginate_queryset(emp, request)   
        ser = EmployeeSerializer(data, many=True)
        return Response({"data": ser.data},status=status.HTTP_200_OK)
    def post(self, request):
        ser = EmployeeSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response({"message": "Employee created successfully"},status=status.HTTP_201_CREATED)
        return Response({"error": ser.errors},status=status.HTTP_400_BAD_REQUEST)

class Classs_Employe(APIView):
    def get(self, request, id):
        data = get_object_or_404(Employee,id=id)
        ser = EmployeeSerializer(data)
        return Response({"data": ser.data},status=status.HTTP_200_OK)
    
    def put(self, request, id):
        data = get_object_or_404(Employee,id=id)
        ser = EmployeeSerializer(data,request.data)
        if ser.is_valid():
            ser.save()
            return Response({"message": "Employee updated successfully"},status=status.HTTP_200_OK)
        return Response({"error": ser.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        data = get_object_or_404(Employee,id=id)
        ser = EmployeeSerializer(data,request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"message": "Employee updated successfully"},status=status.HTTP_200_OK)
        return Response({"error": ser.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        emp = Employee.objects.get(id=id)
        emp.delete()
        return Response({"message": "Employee deleted successfully"},status=status.HTTP_204_NO_CONTENT)
    

# -----------end-------



