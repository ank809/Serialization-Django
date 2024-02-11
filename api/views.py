from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def student_info(request, id):
    # Complex datatype
    stu_obj= Student.objects.get(id=id)
    print(stu_obj)

    # Serializing student object
    serializer=StudentSerializer(stu_obj)
    print(type(serializer))
    print(serializer)

    # Converting serializer data to JSON
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)

    return HttpResponse(json_data, content_type='application/json')


def student_list(request):
    stuObj=Student.objects.all()
    print(stuObj)
    serializer=StudentSerializer(stuObj, many=True)
    print(serializer)
    json_Data=JSONRenderer().render(serializer.data)
    print(json_Data)
    return HttpResponse(json_Data, content_type='application/json')


