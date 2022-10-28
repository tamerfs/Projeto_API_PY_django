from rest_framework.views import APIView
from rest_framework.response import Response


class homeApiView(APIView):
    def get(self, request, format=None):
        return Response({"ACESSE OS END-POINTS LISTADOS A SEGUIR": "-->","Status do Server": "/**/status", "Servidor": "/**/provedores"}, status=200)