from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login(request):
    return Response ({'admin':'Bienvenido'})
        
@api_view(['POST'])
def register(request):
    return 

@api_view(['POST'])
def profile(request):
    return 

@api_view(['POST'])
def delete_user(request):
    return 
        
                
# Create your views here.
