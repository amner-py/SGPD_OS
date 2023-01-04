from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Subproducto

class SubproductoView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if id>0:
            subproductos=list(Subproducto.objects.filter(producto=id).values())
            if len(subproductos)>0:
                datos={'message':'success','hay_subproductos':True,'subproductos':subproductos}
            else:
                datos={'message':'wrong','hay_subproductos':False}
        else:
            subproductos=list(Subproducto.objects.values())
            if len(subproductos)>0:
                datos={'message':'success','hay_subproductos':True,'subproductos':subproductos}
            else:
                datos={'message':'wrong','hay_subproductos':False}
        return JsonResponse(datos)