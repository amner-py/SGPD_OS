from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.http.response import JsonResponse
import json
from .models import Notificacion

class NotificacionesListView(ListView):
    template_name='notificaciones_view.html'
    model=Notificacion
    paginate_by=15


    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)


class NotificacionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        notificaciones=list(Notificacion.objects.values())
        if len(notificaciones)>0:
            datos={'message':'success','hay_notificacion':True,'notificaciones':notificaciones}
        else:
            datos={'message':'wrong','hay_notificacion':False}
        return JsonResponse(datos)

    
    def put(self,request,id):
        jd=json.loads(request.body)
        notificaciones=list(Notificacion.objects.values())
        if len(notificaciones)>0:
            notificacion=Notificacion.objects.get(id=id)
            notificacion.leido=jd['leido']
            notificacion.save()
            datos={'message':'success'}
        else:
            datos={'message':'wrong'}
        return JsonResponse(datos)