from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from .serializers import *
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


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
@api_view(['GET','POST','PUT','DELETE'])
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
        return Response(questions_serializer.data, status.HTTP_200_OK)
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

@csrf_exempt
def Answers(request, id = 0):
    if request.method == 'POST':
        response_data = JSONParser().parse(request)
        response_serializer = AnswerSerializer(data = response_data)
        if response_serializer.is_valid():
            response_serializer.save()
            print("working")
            return JsonResponse("The response was added successfully", safe=False)
        return JsonResponse("There was a problem adding the response", safe=False)
    elif request.method == 'GET':
        responses = Answer.objects.all()
        response_serializer = AnswerSerializer(responses, many = True)
        return JsonResponse(response_serializer.data, safe = False)
    elif request.method == 'PUT':
        response_data = JSONParser().parse(request)
        response = Answer.objects.get (id = response_data['id'])
        response_serializer = AnswerSerializer(response, data = response_data)
        if response_serializer.is_valid():
            response_serializer.save()
            return JsonResponse("The response was updated successfully", safe = False)
        return JsonResponse("response update was not successful", safe=False)
    elif request.method == 'DELETE':
        response = Answer.objects.get(id=id)
        response.delete()
        return JsonResponse("response deleted successfully", safe=False)

