from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView,TemplateView
from django.http.response import JsonResponse
from django.core.paginator import Paginator
import json
from .models import Notificacion

class NotificacionesTemplateView(TemplateView):
    template_name='notificaciones_view.html'

    @method_decorator(login_required)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        page=request.GET.get('page',1)
        noti= Notificacion.objects.filter(receptor=self.request.user)
        notificaciones=[]
        for noti in reversed(noti):
            noti.leido=True
            noti.save()
            notificaciones.append(noti)
        hay_notificacion=len(notificaciones)>0
        try:
            paginator=Paginator(notificaciones,5)
            notificaciones= paginator.page(page)
        except Exception as e:
            print(e)
        return render(request,self.template_name,{
            'hay_notificacion':hay_notificacion,
            'entity':notificaciones,
            'paginator':paginator
        })


class NotificacionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        notis=Notificacion.objects.values()
        no_leidos=0
        for noti in notis:
            if noti['receptor_id'] == self.request.user.pk:
                if noti['leido'] == False:
                    no_leidos+=1
            datos={'message':'wrong','hay_notificacion':False,'no_leidos':no_leidos}
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