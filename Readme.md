## App 
usado como principal para configurações do aplicativo
com o prmeiro endereço d server status em HTML  e o Home view cru com um json retornado direto
__originalmente colocado como models nele mas removido__
template do HTML colocado aqui

## myteacher
onde se encontram as configurações, setting om os parametros como TIMEZONE, apps instalados e outras config como URLS ASGI ou WSGI

## Provedor
é onde se encontra os modelos, o serializer, a classe para o objeto tirado do db SQL 
o view com  o http que recebe o request, pega os dados do SQL, converte ele com o modelo e volta como JSON e devolve a resposta ao request url

## comandos

VM python =>
.\.venv\Scripts\activate

run server =>
python manage.py runserver