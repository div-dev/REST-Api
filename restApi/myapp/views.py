from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import User_Serializer


@api_view(['GET'])
def Search_User(request):
    name1 = request.GET.get('q')
    if name1:
        users = User.search(name1)
        serializer = User_Serializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response({'message':'No search query found'})
    

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
