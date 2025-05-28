from rest_framework.views import APIView
from rest_framework.response import Response

#dev_4
#dev_5_수정
class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World"})


