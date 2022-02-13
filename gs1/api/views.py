from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Model Object - Single Student Data

def student_detail(request,pk):
    stu=Student.objects.get(id = pk)
    # print(stu)
    serializer = StudentSerializer(stu)
    # print(serializer)
    # print(serializer.data)
    # json_data= JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

# Query Set- All Student Data
def student_list(request):
    stu=Student.objects.all()
    # print(stu)
    serializer = StudentSerializer(stu,many=True)
    # print(serializer)
    # print(serializer.data)
    # json_data= JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
