# from django.shortcuts import render, render_to_response
import createuser
from django.db import models
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from createuser.models import ProjectFiles
from rest_framework import status
from .models import upload_path, assignTaskFiles, loginprofile, objectLevel, SceneLevel, ProjectFiles, Objectcategories
from .serializers import  ObjectcategoriesSerializer, ObjectLevelSerializer, SceneLevelSerializer, ProjectFilesSerializer,LoginSerializer, TaskFilesSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files import File
#from PIL import Image
from django.core.files.storage import FileSystemStorage
from django import forms
from django.views.decorators.csrf import csrf_exempt


#Register user, delete, update, post data
@api_view(['GET', 'POST', 'DELETE'])
def registerUsers(request):
    if request.method == 'POST':
        obj = loginprofile()  # gets new object  
        obj.firstName = request.data['firstName']
        obj.role = request.data['role']
        obj.password = request.data['password']
        obj.save()
        return Response("Saved successfully")
        
    elif request.method == 'GET':
         registeredNames = loginprofile.objects.all().values()
         return Response(registeredNames)

    else:
        request.method == 'DELETE'
        count = loginprofile.objects.all().delete()
        return JsonResponse({'message': '{} users deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def registerdUsers_id(request, pk):
    try: 
        registeredNames = loginprofile.objects.get(pk=pk) 
    except loginprofile.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        users_serializer = LoginSerializer(registeredNames) 
        return JsonResponse(users_serializer.data) 

    elif request.method == 'PUT': 
        cat_data = JSONParser().parse(request) 
        print(cat_data)
        users_serializer = LoginSerializer(registeredNames, data=cat_data) 
        if users_serializer.is_valid(): 
            users_serializer.save() 
            return JsonResponse(users_serializer.data) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        registeredNames.delete() 
        return JsonResponse({'message': 'user was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 


class Login(APIView):
    def post(self, request):
        cred=request.data
        name=request.data['firstName']
        password=request.data['password']
        print("cred",cred)
        check=loginprofile.objects.filter(firstName=name,password=password).values()
        if check:  
            result = {
                'status': '200', 
                'message': 'Login Successfull'
            }
            return JsonResponse(result)
        
        # elif (check != ("/^[0-9]") ):
        #     print("enetering elif loop")
        #     result = {'status': '401', 
        #         'message': 'invalid inputs'          
        #     }
        #     return JsonResponse(result)

        elif not check:
            return  Response('Invalid credentials', status=status.HTTP_401_UNAUTHORIZED)
        
class Getuser(APIView):
    def get(self, request):
        print (request.data)
        entry = loginprofile.objects.all().values()
        print("entry",entry)
        return Response(entry)


class GetProjectName(APIView):
    def get(self, request):
        entry = ProjectFiles.objects.values("project_name")
        return Response(entry)

# writing get, put, delete, post methods for objectlevelAtrributes
@api_view(['GET', 'POST', 'DELETE'])
def objectlevelattributes(request):
    if request.method == 'POST':
        obj = objectLevel() 
        obj.trackId = request.data['trackId']
        obj.objectClass = request.data['objectClass']
        obj.pose = request.data['pose']
        obj.occlusion = request.data['occlusion']
        obj.lane_change = request.data['lane_change']
        obj.breakLight = request.data['breakLight']
        obj.save() 
        return Response("Saved successfully")
        
    elif request.method == 'GET':
         getObjectLevelAttributes = objectLevel.objects.all().values()
         return Response(getObjectLevelAttributes)

    else:
        request.method == 'DELETE'
        count = objectLevel.objects.all().delete()
        return JsonResponse({'message': '{} objectLevelAttributes  deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def objectlevelattributes_id(request, pk):
    try: 
        objectlevelAtrributeslist = objectLevel.objects.get(pk=pk) 
    except objectLevel.DoesNotExist: 
        return JsonResponse({'message': 'The objectLevelAttributes does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        objLevelserializer = ObjectLevelSerializer(objectlevelAtrributeslist) 
        return JsonResponse(objLevelserializer.data) 

    elif request.method == 'PUT': 
        cat_data = JSONParser().parse(request) 
        print(cat_data)
        objLevelserializer = ObjectLevelSerializer(objectlevelAtrributeslist, data=cat_data) 
        if objLevelserializer.is_valid(): 
            objLevelserializer.save() 
            return JsonResponse(objLevelserializer.data) 
        return JsonResponse(objLevelserializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        objectlevelAtrributeslist.delete() 
        return JsonResponse({'message': 'objectLevelAttribute was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# writing get, put, delete, post methods for ScenelevelAtrributes
@api_view(['GET', 'POST', 'DELETE'])
def scenelevelattributes(request):
    if request.method == 'POST':
        obj = SceneLevel() 
        obj.Light_Condition = request.data['Light_Condition']
        obj.Road_Type = request.data['Road_Type']
        obj.Road_works = request.data['Road_works']
        obj.Tunnel = request.data['Tunnel']
        obj.Weather = request.data['Weather']
        obj.Street_Condition = request.data['Street_Condition']
        obj.save() 
        return Response("Saved successfully")
        
    elif request.method == 'GET':
         getsceneLevelAttributes = SceneLevel.objects.all().values()
         return Response(getsceneLevelAttributes)

    else:
        request.method == 'DELETE'
        count = SceneLevel.objects.all().delete()
        return JsonResponse({'message': '{} scenelevelAttributes  deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def scenelevelattributes_id(request, pk):
    try: 
        scenelevelAtrributeslist = SceneLevel.objects.get(pk=pk) 
    except SceneLevel.DoesNotExist: 
        return JsonResponse({'message': 'The scenelevelAttributes does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        sceneLevelserializer = SceneLevelSerializer(scenelevelAtrributeslist) 
        return JsonResponse(sceneLevelserializer.data) 

    elif request.method == 'PUT': 
        cat_data = JSONParser().parse(request) 
        print(cat_data)
        sceneLevelserializer = SceneLevelSerializer(scenelevelAtrributeslist, data=cat_data) 
        if sceneLevelserializer.is_valid(): 
            sceneLevelserializer.save() 
            return JsonResponse(sceneLevelserializer.data) 
        return JsonResponse(sceneLevelserializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        scenelevelAtrributeslist.delete() 
        return JsonResponse({'message': 'scenelevelAttribute was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# writing get, put, delete, post methods for Projectfiles(project name, tool version, feature)
@api_view(['GET', 'POST', 'DELETE'])
def projectFiles(request):
    if request.method == 'POST':
        obj = ProjectFiles() 
        project_F= request.data['project_Feature']
        tool_v= request.data['Tool_version']
        feature_without=str(project_F)[1:-1]
        tool_without=str(tool_v)[1:-1]
        obj = ProjectFiles()  # gets new object
        obj.project_name = request.data['project_name']
        obj.project_Feature =feature_without
        obj.Tool_version = tool_without 
        obj.save()
        return Response("Saved successfully")
        
    elif request.method == 'GET':
         getProjectFilesDetails = ProjectFiles.objects.all().values()
         return Response(getProjectFilesDetails)

    else:
        request.method == 'DELETE'
        count = ProjectFiles.objects.all().delete()
        return JsonResponse({'message': '{} projets deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def projectFiles_id(request, pk):
    print(pk,"pk is ")
    try: 
        projectFileslist = ProjectFiles.objects.get(pk=pk) 
    except ProjectFiles.DoesNotExist: 
        return JsonResponse({'message': 'The projectFiles does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        projectFileserializer = ProjectFilesSerializer(projectFileslist) 
        return JsonResponse(projectFileserializer.data) 

    elif request.method == 'PUT': 
        cat_data = JSONParser().parse(request) 
        print(cat_data)
        projectFileserializer = ProjectFilesSerializer(projectFileslist, data=cat_data) 
        if projectFileserializer.is_valid(): 
            projectFileserializer.save() 
            return JsonResponse(projectFileserializer.data) 
        return JsonResponse(projectFileserializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        projectFileslist.delete() 
        return JsonResponse({'message': 'project was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# writing get, put, delete, post methods for TaskFiles(project name, tool version, feature)
@api_view(['GET', 'POST', 'DELETE'])
def taskFilesList(request):
    if request.method == 'POST':
        obj = assignTaskFiles() 
        obj.File_Name = request.data['File_Name']
        obj.project_name = request.data['project_name']
        obj.Task_level = request.data['Task_level']
        obj.Priority = request.data['Priority']
        obj.Created_Date = request.data['Created_Date']
        obj.status = request.data['status']
        obj.Action = request.data['Action']
        obj.save()
        return Response("Saved successfully")
        
    elif request.method == 'GET':
         getTaskFilesDetails = assignTaskFiles.objects.all().values()
         return Response(getTaskFilesDetails)

    else:
        request.method == 'DELETE'
        count = assignTaskFiles.objects.all().delete()
        return JsonResponse({'message': '{} tasks were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def taskFilesList_id(request, pk):
    print(pk,"pk is ")
    try: 
        taskFileslist = assignTaskFiles.objects.get(pk=pk) 
    except assignTaskFiles.DoesNotExist: 
        return JsonResponse({'message': 'The task does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        taskFileserializer = TaskFilesSerializer(taskFileslist) 
        return JsonResponse(taskFileserializer.data) 

    elif request.method == 'PUT': 
        cat_data = JSONParser().parse(request) 
        print(cat_data)
        taskFileserializer = TaskFilesSerializer(taskFileslist, data=cat_data) 
        if taskFileserializer.is_valid(): 
            taskFileserializer.save() 
            return JsonResponse(taskFileserializer.data) 
        return JsonResponse(taskFileserializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        taskFileslist.delete() 
        return JsonResponse({'message': 'task was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getProjectDetails(request, project_name):
    if request.method == 'GET':
       projectdetails = ProjectFiles.objects.all()
       projectName = request.GET.get('project_name', None)
       print("projectname",projectName)
       filteredList = projectdetails.filter(project_name=projectName).values()
       #print("filtered list",filteredList)
       return Response(filteredList)

@api_view(['GET'])
def gettasksfilteredonProjects(request, project_name):
    if request.method == 'GET':
        projectdetails = assignTaskFiles.objects.all()
        projectName = request.GET.get('project_name', None)
        print("projectfilestask", projectName)
        listing = projectdetails.filter(project_name=projectName).values()
        #print(listing)
        return Response(listing)

@api_view(['GET', 'POST', 'DELETE'])
def getobjectCategories(request):
    if request.method == 'POST':
        obj = Objectcategories() 
        obj.object_category = request.data['object_category']
        obj.save() 
        return Response("Saved successfully")
        
    elif request.method == 'GET':
         categoryNames = Objectcategories.objects.all().values()
         return Response(categoryNames)

    else:
        request.method == 'DELETE'
        count = Objectcategories.objects.all().delete()
        return JsonResponse({'message': '{} obects were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def getobjectCategories_id(request, pk):
    try: 
        categoryNames = Objectcategories.objects.get(pk=pk) 
    except Objectcategories.DoesNotExist: 
        return JsonResponse({'message': 'The object does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        category_serializer = ObjectcategoriesSerializer(categoryNames) 
        return JsonResponse(category_serializer.data) 

    elif request.method == 'PUT': 
        cat_data = JSONParser().parse(request) 
        print(cat_data)
        category_serializer = ObjectcategoriesSerializer(categoryNames, data=cat_data) 
        if category_serializer.is_valid(): 
            category_serializer.save() 
            return JsonResponse(category_serializer.data) 
        return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        categoryNames.delete() 
        return JsonResponse({'message': 'object was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 
@csrf_exempt
def uploadimages(request, *args, **kwargs):
    print("request is ", request)
    title = request.POST.get('project_name')
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)  
    obj = assignTaskFiles()
    obj.File_Name = file
    obj.project_name = title
    obj.Task_level =  request.POST.get('Task_level')
    obj.Priority =  request.POST.get('Priority')
    obj.Created_Date =  request.POST.get('Created_Date')
    obj.status = request.POST.get('status')
    obj.Action =  request.POST.get('Action')
    obj.save()
    return JsonResponse(file_name,safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def getAnnotationImageFile(request, File_Name, project_name):
    if request.method == 'GET':
        projectdetails = assignTaskFiles.objects.all()
        projectName = request.GET.get('project_name')
        filename = request.GET.get('File_Name')
        print("projectname", projectName)
        print("filename", filename)
        fetchfileandProjectName = projectdetails.filter(project_name=projectName, File_Name=filename).values()
        return Response(fetchfileandProjectName)

