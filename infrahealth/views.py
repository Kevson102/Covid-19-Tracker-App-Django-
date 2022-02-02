from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
# from django.contrib.auth.models import User

from .models import *
from .serializers import *

# Create your views here.

def home(request):
  return render(request, 'index.html')

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        messages.success(request, f'User was registered successfully')
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    
    
    def post(self, request, format=None):
        
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        get_user(request)
        return super(LoginAPI, self).post(request, format=None)
    
def get_user(request):
    current_user = request.user
    if request.user.is_authenticated:
        return Response({current_user.id, current_user.username, current_user.email})



# Healthchecklist questions API
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
@login_required(login_url='/api/login/')
def HealthCheck(request, id=0):
    if request.method == 'POST':
        question_data = JSONParser().parse(request)
        question_serializer = HealthCheckSerializer(data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            print("working")
            return JsonResponse("The question was added successfully", safe=False)
        return JsonResponse("There was a problem adding the question", safe=False)
    
    elif request.method == 'GET':
        questions = HealthCheckQuestions.objects.all()
        questions_serializer = HealthCheckSerializer(questions, many=True)
        return JsonResponse(questions_serializer.data, safe=False)
    
    elif request.method == 'PUT':
        question_data = JSONParser().parse(request)
        question = HealthCheckQuestions.objects.get(id=question_data['id'])
        question_serializer = HealthCheckSerializer(
            question, data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            return JsonResponse("The question was updated successfully", safe=False)
        return JsonResponse("Question update was not successful", safe=False)
    
    elif request.method == 'DELETE':
        question = HealthCheckQuestions.objects.get(id=id)
        question.delete()
        return JsonResponse("Question deleted successfully", safe=False)


@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
@login_required(login_url='/api/login/')
def Answers(request, id=0):
    if request.method == 'POST':
        response_data = JSONParser().parse(request)
        response_serializer = AnswerSerializer(data=response_data)
        if response_serializer.is_valid():
            response_serializer.save()
            print("working")
            return JsonResponse("The response was added successfully", safe=False)
        return JsonResponse("There was a problem adding the response", safe=False)
    elif request.method == 'GET':
        current_user = request.user
        patient = Patient.objects.get(user_id = current_user.id)
        print(patient.id)
        if request.user.is_authenticated:
            # print({patient.username, patient.id})
            responses = Answer.objects.filter(patient_id=patient.id)
            response_serializer = AnswerSerializer(responses, many=True)
            return JsonResponse(response_serializer.data, safe=False)
        return JsonResponse("That patient do not exist", safe = False)
    elif request.method == 'PUT':
        response_data = JSONParser().parse(request)
        response = Answer.objects.get(id=response_data['id'])
        response_serializer = AnswerSerializer(response, data=response_data)
        if response_serializer.is_valid():
            response_serializer.save()
            return JsonResponse("The response was updated successfully", safe=False)
        return JsonResponse("response update was not successful", safe=False)
    elif request.method == 'DELETE':
        response = Answer.objects.get(id=id)
        response.delete()
        return JsonResponse("response deleted successfully", safe=False)


@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
@login_required(login_url='/api/login/')
def MedicalTestView(request, id=0):
    if request.method == 'POST':
        response_data = JSONParser().parse(request)
        response_serializer = MedicalTestSerializer(data=response_data)
        if response_serializer.is_valid():
            response_serializer.save()
            return JsonResponse('Medical Test Results were saved successfully', safe=False)
        return JsonResponse('Save Failed', safe=False)
    elif request.method == 'GET':
        response = MedicalTest.objects.all()
        response_serializer = MedicalTestSerializer(response, many=True)
        return JsonResponse(response_serializer.data, safe=False)
    elif request.method == 'PUT':
        response_data = JSONParser().parse(request)
        response = MedicalTest.objects.get(id=response_data['id'])
        response_serializer = MedicalTestSerializer(
            response, data=response_data)
        if response_serializer.is_valid():
            response_serializer.save()
            return JsonResponse('Record Updated Successfully', safe=False)
        return JsonResponse('Update Failed', safe=False)
    elif request.method == 'DELETE':
        response = MedicalTest.objects.get(id=id)
        response.delete()
        return JsonResponse('Deleted Successfully', safe=False)

@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
@login_required(login_url='/api/login/')
def PatientsView(request, id=0):
    if request.method == 'POST':
        response_data = JSONParser().parse(request)
        response_serializer = PatientSerializer(data=response_data)
        if response_serializer.is_valid():
            response_serializer.save()
            return JsonResponse('Patient was saved successfully', safe=False)
        return JsonResponse('Save Failed', safe=False)
    elif request.method == 'GET':
        response = Patient.objects.all()
        response_serializer = PatientSerializer(response, many=True)
        return JsonResponse(response_serializer.data, safe=False)
    elif request.method == 'PUT':
        response_data = JSONParser().parse(request)
        response = Patient.objects.get(id=response_data['id'])
        response_serializer = PatientSerializer(
            response, data=response_data)
        if response_serializer.is_valid():
            response_serializer.save()
            return JsonResponse('Patient Record Updated Successfully', safe=False)
        return JsonResponse('Patient Update Failed', safe=False)
    elif request.method == 'DELETE':
        response = Patient.objects.get(id=id)
        response.delete()
        return JsonResponse('Patient Deleted Successfully', safe=False)