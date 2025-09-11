from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Employee


from django.http import HttpResponse
from .models import Employee
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Employee


def api_response(success, message, data=None, status_code=200):
    return Response({
        "success": success,
        "message": message,
        "data": data
    }, status=status_code)


@api_view(['GET'])
def employee_list(request):
    try:
        employees = list(Employee.objects.all().values())
        return api_response(True, "Employee list fetched successfully", employees, 200)
    except Exception as e:
        return api_response(False, f"Error fetching employee list: {str(e)}", None, 500)


@api_view(['POST'])
@csrf_exempt
def add_employee(request):
    try:
        data = json.loads(request.body)

        # Check if email already exists
        if Employee.objects.filter(email_id=data.get('email_id')).exists():
            return api_response(False, "Email ID already exists", None, 400)

        emp = Employee.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email_id=data.get('email_id'),
            department=data.get('department'),
            salary=data.get('salary'),
            hire_date=data.get('hire_date'),
            age=data.get('age'),
            selectedGender = data.get('selectedGender'),
            dob = data.get('dob'),
            skills = data.get('skills')
        )

        return api_response(True, "Employee added successfully", {"employee_id": emp.employee_id}, 201)

    except (KeyError, json.JSONDecodeError) as e:
        return api_response(False, f"Invalid data: {str(e)}", None, 400)
    except Exception as e:
        return api_response(False, f"Server error: {str(e)}", None, 500)


@api_view(['PUT'])
@csrf_exempt
def update_employee(request, pk):
    try:
        data = json.loads(request.body)
        try:
            emp = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return api_response(False, "Employee not found", None, 404)

        # Update fields
        emp.first_name = data.get('first_name', emp.first_name)
        emp.last_name = data.get('last_name', emp.last_name)
        emp.department = data.get('department', emp.department)
        emp.salary = data.get('salary', emp.salary)
        emp.hire_date = data.get('hire_date', emp.hire_date)
        emp.email_id = data.get('email_id', emp.email_id)
        emp.age = data.get('age', emp.age)
        emp.selectedGender = data.get('selectedGender', emp.selectedGender)
        emp.dob = data.get('dob', emp.dob)
        emp.skills = data.get('skills', emp.skills)

        emp.save()
        return api_response(True, "Employee updated successfully", {"employee_id": emp.employee_id}, 200)

    except (KeyError, json.JSONDecodeError) as e:
        return api_response(False, f"Invalid data: {str(e)}", None, 400)
    except Exception as e:
        return api_response(False, f"Server error: {str(e)}", None, 500)


@api_view(['DELETE'])
@csrf_exempt
def delete_employee(request, pk):
    try:
        try:
            emp = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return api_response(False, "Employee not found", None, 404)

        emp.delete()
        return api_response(True, "Employee deleted successfully", None, 200)

    except Exception as e:
        return api_response(False, f"Server error: {str(e)}", None, 500)