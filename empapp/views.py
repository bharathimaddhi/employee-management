from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        try:
            email = serializer.validated_data['email']
            if Employee.objects.filter(email=email).exists():
                return Response({
                    'message': 'Employee already exists',
                    'success': False,
                }, status=status.HTTP_200_OK)
            serializer.save()
            return Response({
                'message': 'Employee created successfully',
                'success': True,
                'regid': serializer.data['id'],
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Employee creation failed',
                'success': False,
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({
            'message': 'Invalid body request',
            'success': False,
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_employee(request, regid):
    try:
        employee = Employee.objects.get(id=regid)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Employee details updated successfully',
                'success': True,
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'Employee details updation failed',
                'success': False,
            }, status=status.HTTP_400_BAD_REQUEST)
    except Employee.DoesNotExist:
        return Response({
            'message': 'No employee found with this regid',
            'success': False,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'message': 'Employee updation failed',
            'success': False,
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_employee(request):
    regid = request.data.get('regid')
    try:
        employee = Employee.objects.get(id=regid)
        employee.delete()
        return Response({
            'message': 'Employee deleted successfully',
            'success': True,
        }, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response({
            'message': 'No employee found with this regid',
            'success': False,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'message': 'Employee deletion failed',
            'success': False,
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_employee(request):
    regid = request.GET.get('regid')
    if regid:
        try:
            employee = Employee.objects.get(id=regid)
            serializer = EmployeeSerializer(employee)
            return Response({
                'message': 'Employee details found',
                'success': True,
                'employees': [serializer.data],
            }, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({
                'message': 'No employee found with this regid',
                'success': False,
                'employees': [],
            }, status=status.HTTP_200_OK)
    else:
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response({
            'message': 'Employee details found',
            'success': True,
            'employees': serializer.data,
        }, status=status.HTTP_200_OK)
