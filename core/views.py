from django.shortcuts import render
from .models import Tipo, Cancion, Book, Verse
# Create your views here.

def home(request):
    tipos = Tipo.objects.all()
    variables = {
        'tipos':tipos,
    }

    return render(request, 'core/home.html', variables)

def tupla_versiculos(desde, hasta=0):
    rango = []

    if hasta<=desde:
        rango.append(desde)
    else:
        for x in range(desde,hasta+1):
            rango.append(x)
    return rango

def biblia(request):
    libros = Book.objects.all()
    variables = {
        'libros':libros,
    }
    #preguntar Versiculo

    if request.POST:

            
        libro = request.POST.get('cboLibro')

        capitulo = request.POST.get('cap')
        desde = int(request.POST.get('des'))
        hasta =request.POST.get('hasta')
        
        direccion_versiculo = Book.objects.get(id=libro).name+' '+str(capitulo)+' : '+str(desde)
        
        
        if len(hasta)==0 or int(hasta)<=int(desde):
            hasta = 0
        else:
            hasta = int(hasta)
            direccion_versiculo = direccion_versiculo +' - '+str(hasta)
            variables['hasta'] = hasta

        versiculos = Verse.objects.filter(book=libro, chapter=capitulo, verse__in=tupla_versiculos(desde,hasta) )
        
        try:
            if versiculos.exists():
                variables['versiculos'] = versiculos
            else:
                variables['no_encontrado'] = 'Ups!!, el versiculo no se encuentra'      
        except:
            pass
        variables['direccion_versiculo'] = direccion_versiculo

        #le mandamos los valores que recojemos del POST para que se mantengan en el formulario
        variables['capitulo'] = capitulo
        variables['desde'] = desde
        variables['libro'] = Book.objects.get(id=libro).name
        
    #-------------
    return render(request, 'core/biblia.html',variables)

def listado(request, id=-1):
    if id==-1:
        canciones = Cancion.objects.all()
    else:
        canciones = Cancion.objects.filter(tipo_id=id)

    tipos = Tipo.objects.all()
    variables = {
        'tipos':tipos,
        'canciones':canciones,
    }

    return render(request, 'core/listado.html', variables)

def cancion(request, id):

    cancion = Cancion.objects.filter(id=id)

    tipos = Tipo.objects.all()
    variables = {
        'tipos':tipos,
        'cancion':cancion,
    }

    return render(request, 'core/cancion.html', variables)
