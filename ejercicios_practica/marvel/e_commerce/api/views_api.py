from django.http import HttpResponse
from rest_framework.decorators import api_view
from e_commerce.models import *



@api_view(['GET', 'POST'])
def saludo(request):
    nombre = 'matias toniolo'
    #opcion post para modificar variable dentro de la peticion --> ()
    opcion = request.POST.get(nombre)
    
    if nombre is None:
        nombre = opcion
    
        
    template = f'''
                <html>
                    <head>
                        <title>Saludo</title>
                    <head>
                    <body style='background: red'>
                        <div style='background: darkblue'>
                            <h1>Hello {nombre}!</h1>
                        <div>
                    <body>
                </html>
        '''
    return HttpResponse(template)



@api_view(['GET'])
def queryset(request):
    query = Comic.objects.count()
    
    if query is None:
        template = f'<h1>Aun no tienes Comics en tu lista</h1>'
    else:
        template = f'<h1>Tienes un total de {query} Comics en tu lista</h1>'
    
    return HttpResponse(template)

@api_view(['GET'])
def total(request):
    total =[sum(comic.price for comic in (Comic.objects.all()))]
    total = total[0]
   
    template = f'<h1>Llevas gastado: ${total} en Comics </h1>'
    
    return HttpResponse(template)
    





    
    