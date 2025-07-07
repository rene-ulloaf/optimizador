from django.shortcuts import render
from optimizador.modules.DataLoader import DataLoader
from optimizador.modules.OptimizationModel import OptimizationModel

def inicio(request):
    return render(request, 'cargaArchivo.html')

def carga_archivo(request):
    if request.method == 'POST':       
        if 'archivo_optimizar' in request.FILES:
            loader = DataLoader(request.FILES['archivo_optimizar'])
            if loader.validate():
                listaDatos = loader.loadData()
                return render(request, 'datosArchivo.html', {'listaDatos': listaDatos})
            else:
                return render(request, 'cargaArchivo.html', {'error': 'Archivo invalido'})
        else:
            return render(request, 'cargaArchivo.html', {'error': 'No se selecciono archivo'})
    else:
        return render(request, 'cargaArchivo.html')
    
def datos_archivo(request):
    lista = request.session.get('listaDatos', [])
    return render(request, 'datosArchivo.html', {'listaDatos': lista})

def optimizar(request):
    graphic = None
    listaData = request.POST['listaDatos'].split("], [")
    headers = str(listaData[0]).replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(",")
    values = str(listaData[1]).replace("[", "").replace("]", "").replace("'", "").split(",")
        
    optimizador = OptimizationModel(headers, values)
    res = optimizador.procesar()
    if res.success:
        #graphic = optimizador.grafico()
        graphic = None
    
    return render(request, 'optimizacion.html', {'res': res, 'PA': res.x[0], 'PB': res.x[1], 'ganancia': -res.fun, 'graphic': graphic})
    