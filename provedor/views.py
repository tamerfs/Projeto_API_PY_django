from provedor.serializers import ProvedorSerializer, CadastrarServicoSerializer, ServicoSerializer, CadastrarProvedoresSerializer
from rest_framework.views import APIView, Response
from django.shortcuts import get_object_or_404 # busca o objeto ou retorna um objeto nao encontrado
from provedor.models import Provedor, Servico
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class ProvedorAPIView(APIView):
    def get(self, request, format=None):
        provedores = Provedor.objects.all()
        serializer = ProvedorSerializer(provedores, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request, format=None):
            serializer = CadastrarProvedoresSerializer(data = request.data) 
            if serializer.is_valid():
                provedor = Provedor(
                    nome = serializer.validated_data.get('nome'),
                    preco = serializer.validated_data.get('preco'),
                    descricao = serializer.validated_data.get('descricao'),
                    foto = serializer.validated_data.get('foto'),
                )
                provedor.save()
                provedor_serializer = ProvedorSerializer(provedor, many=False)
                return Response(provedor_serializer.data, status=HTTP_201_CREATED)
            return Response(
                    {
                    "message":"Houveram erros de vaidação",
                    "erros" : serializer.errors
                    },
                    status=HTTP_400_BAD_REQUEST
                )        


class BuscarServicoAPIView(APIView):
    def get(self, request, format=None):
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class CadastrarServicoAPIView(APIView):
    def post(self, request, id, format=None):
        #Provedores.objects.get(id) metodo possivel mas se vier null vai lançar uma exeção
        provedor = get_object_or_404(Provedor, id=id) # vai buscar no Provedor uma coluna com o parametro id
        serializer = CadastrarServicoSerializer(data = request.data) # vai serializar os dados que recebemos na reqisção
    # o metodo consiste que na criação do objeto passamos os dados junto com a requisição para dar o retorno esperado
        if serializer.is_valid():
    # se ele estiver valido, vamos popular o servico no metodo abaixo
            servico = Servico(
                nome = serializer.validated_data.get('nome'),
                email = serializer.validated_data.get('email'),
                provedor = provedor
            )
            servico.save() # metodo que é usado para salvar aulas ou servicos  no db atrelados a um provedor ou rofessor.
            # para armazenar ou criar os novos provedores ou professores foi usado um codigo direto no shell.
            #  necssario criar um comando assim para novos provedores.
            servico_serializer = ServicoSerializer(servico, many=False)
            return Response(servico_serializer.data, status=HTTP_201_CREATED)
        return Response(
                {
                "message":"Houveram erros de vaidação",
                "erros" : serializer.errors
                },
                status=HTTP_400_BAD_REQUEST
            )

      