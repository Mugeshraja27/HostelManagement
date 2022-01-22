from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializers import *
from . models import *

# Create your views here.
@api_view(('GET',))
def students(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data)

@api_view(('GET',))
def rooms(request):
    rooms=Room.objects.all()
    serializer=RoomSerializer(rooms,many=True)
    return Response(serializer.data)

@api_view(('GET',))
def studentDetails(request,id):
    student=Student.objects.get(id=id)
    serializer=StudentSerializer(student,many=False)
    return Response(serializer.data)

@api_view(('GET',))
def roomDetails(request,id):
    room=Room.objects.get(number=id)
    serializer=RoomSerializer(room,many=False)
    return Response(serializer.data)

@api_view(('GET',))
def deleteRoom(request,id):
    room=Room.objects.get(number=id)
    room.delete()
    return HttpResponse()

@api_view(('GET',))
def deleteStudent(request,id):
    student=Student.objects.get(id=id)
    if student.room:
        room_no=student.room.number
        room=Room.objects.get(number=room_no)
        room.status="Empty"
        room.save()
        student.delete()
        data=[{
                'deletion':'pass'
            }]
        return Response(data)
    else:
        student.delete()
        data=[{
                'deletion':'pass'
            }]
        return Response(data)

@api_view(('GET',))
def mess(request):
    mess=Mess.objects.all()
    serializer=MessSerializer(mess,many=True)
    return Response(serializer.data)

@api_view(('GET','POST'))
def login(request):
    if request.method=="POST":
        data=list(request.data[0].values())
        email=data[0]
        password=data[1]
        student=Student.objects.get(email=email)
        if student and student.password==password:
            validate=[{
                    'validation':'pass'
                }]
        else:
            validate=[{
                    'validation':'fail'
                }]
        return Response(validate)
    else:
        return Response()

@api_view(('GET','POST'))
def register(request):
    if request.method=="POST":
        data=list(request.data[0].values())
        name=data[0]
        email=data[1]
        address=data[2]
        phone=data[3]
        password=data[4]
        Student.objects.create(
            name=name,
            email=email,
            address=address,
            phone=phone,
            password=password
        )
        data=[{
            'registered':'pass'
        }]
        return Response(data)
    else:
        return Response()

@api_view(('GET','POST'))
def studentUpdate(request):
    if request.method=="POST":
        data=list(request.data[0].values())
        id=data[0]
        name=data[1]
        email=data[2]
        address=data[3]
        phone=data[4]
        room=data[5]
        hostel_fees=data[6]
        mess_fees=data[7]
        attendance=data[8]
        student=Student.objects.get(id=id)
        if student:
            student.name=name
            student.email=email
            student.address=address
            student.phone=phone
            if hostel_fees=="Paid":
                student.hostel_fees=True
            else:
                student.hostel_fees=False
            if mess_fees=="Paid":
                student.mess_fees=True
            else:
                student.mess_fees=False
            student.attendnace=attendance
            student.save()
            data=[{
            'update':'pass'
            }]
        else:
            data=[{
            'update':'fail'
            }]
        return Response(data)
    else:
        return Response()