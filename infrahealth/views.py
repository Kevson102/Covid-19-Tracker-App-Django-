from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from .serializers import *
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
# Create your views here.

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
        
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
# Healthchecklist questions API
@csrf_exempt
def HealthCheck(request, id = 0):
    if request.method == 'POST':
        question_data = JSONParser().parse(request)
        question_serializer = HealthCheckSerializer(data = question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            print("working")
            return JsonResponse("The question was added successfully", safe=False)
        return JsonResponse("There was a problem adding the question", safe=False)
    elif request.method == 'GET':
        questions = HealthCheckQuestions.objects.all()
        questions_serializer = HealthCheckSerializer(questions, many = True)
        return JsonResponse(questions_serializer.data, safe = False)
    elif request.method == 'PUT':
        question_data = JSONParser().parse(request)
        question = HealthCheckQuestions.objects.get (id = question_data['id'])
        question_serializer = HealthCheckSerializer(question, data = question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            return JsonResponse("The question was updated successfully", safe = False)
        return JsonResponse("Question update was not successful", safe=False)
    elif request.method == 'DELETE':
        question = HealthCheckQuestions.objects.get(id=id)
        question.delete()
        return JsonResponse("Question deleted successfully", safe=False)
    

