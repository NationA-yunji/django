from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Admin
from .serializers import AdminSerializer


@api_view(["GET"])
def get_admins(request):
    admins = Admin.objects.all()
    serializer = AdminSerializer(admins, many=True)
    return Response(serializer.data)
