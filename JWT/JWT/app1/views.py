from django.shortcuts import render
from rest_framework import viewsets
from .serializer import EmployeeSerializer
from .models import Employee
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class EmployeeDetail(viewsets.ViewSet):
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes  =[IsAuthenticated,]


    def list(self,request):
        obj = Employee.objects.all()
        serializer = EmployeeSerializer(obj,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeInfo(viewsets.ViewSet):
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def retrieve(self,request,id):
        try:
            obj = Employee.objects.get(eid=id)

        except Employee.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self,request,id):
        try:
            obj = Employee.objects.get(eid=id)

        except Employee.DoesNotExist:
            msg = {"msg":"not found"}

            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, id):
        try:
            obj = Employee.objects.get(eid=id)

        except Employee.DoesNotExist:
            msg = {"msg": "not found"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destory(self,request,id):
        try:
            obj = Employee.objects.get(eid=id)

        except Employee.DoesNotExist:
            msg = {"msg":"not found"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg":"deleted"}, status=status.HTTP_204_NO_CONTENT)
