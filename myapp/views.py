from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from myapp.models import Employee
from myapp.serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.decorators import api_view , APIView
from rest_framework.response import Response 


# ----------------Generic Base Api -------------------
# -----------start-------
class genericlistcreate(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
class genericretriveupdatedestroy(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
# ------------end-------    


    
# ----------------Function Base Api -------------------
# ---------start---------
@api_view(['GET'])
def f_get(request):
    data = Employee.objects.all()
    ser = EmployeeSerializer(data, many=True)
    return Response({"data": ser.data},status=status.HTTP_200_OK)
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
        data = Employee.objects.all()
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



