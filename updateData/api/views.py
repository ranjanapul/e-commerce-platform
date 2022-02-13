from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import 
# Create your views here.
def student_api(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.ByteIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)# If we are not provided with an id, give None
        if id is not None:
            stu=Student.objects.get(id=id)
            


