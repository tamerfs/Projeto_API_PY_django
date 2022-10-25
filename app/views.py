from django.shortcuts import render
from django.http import JsonResponse


def status(request):
    return render(request, 'app/status.html')

# def home(request):
#     return JsonResponse({"nome": "Abude Abadia", "idade": 27})

# Feito com REST framework


from rest_framework.views import APIView
from rest_framework.response import Response


class homeApiView(APIView):
    def get(self, request, format=None):
        return Response({"ACESSE OS END-POINTS LISTADOS A SEGUIR": "-->","Status do Server": "/**/status", "Servidor": "/**/provedores"}, status=200)