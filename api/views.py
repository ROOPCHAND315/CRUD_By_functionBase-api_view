from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == 'GET':
        id=request.data.get('id')
        print(id)
        if id is not None:
            stu=StudentModel.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=StudentModel.objects.all()
        serializer=StudentSerializer(stu ,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data=request.data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id=request.data.get('id')
        stu=StudentModel.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id=request.data.get('id')
        stu=StudentModel.objects.get(id=id)
        stu.delete()
        return Response({'msg':'object Deleted'})