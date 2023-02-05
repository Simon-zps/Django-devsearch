from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from projects.models import Project, Tag
from users.models import Profile
from .serializers import ProjectSerializer

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'api/projects'},
        {'GET':'api/projects/id'},
        {'POST':'api/projects/id/vote'},

        {'POST':'api/users/token'},
        {'POST':'api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getProjects(request):
    print('USER', request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True).data
    return Response(serializer)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False).data
    return Response(serializer)