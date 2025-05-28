from rest_framework.views import APIView
from rest_framework.response import Response

#dev_4
class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World"})

