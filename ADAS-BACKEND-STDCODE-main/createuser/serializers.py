from .models import ProjectFiles, SceneLevel, assignTaskFiles, loginprofile, objectLevel,  Objectcategories
from rest_framework import serializers
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = loginprofile
        fields = '__all__'

class ObjectcategoriesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Objectcategories
        fields = ('id',
                  'object_category')
class assignTaskFilesserializer(serializers.ModelSerializer):
     class Meta:
        model = assignTaskFiles
        fields = (
                  'File_Name','project_name','Task_level','Priority','Created_Date','status','Action','annotation_image')

class ObjectLevelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = objectLevel
        fields = ('id',
                  'trackId','objectClass','occlusion','pose','lane_change','breakLight')

class SceneLevelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = SceneLevel
        fields = ('id',
                  'Light_Condition','Road_Type','Road_works','Tunnel','Weather','Street_Condition')

class ProjectFilesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ProjectFiles
        fields = ('id',
                  'project_name','project_Feature','Tool_version')

class TaskFilesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = assignTaskFiles
        fields = ('id',
                  'File_Name','project_name','Task_level','Priority','Created_Date','status','Action','annotation_image')