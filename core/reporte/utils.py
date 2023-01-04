from io import BytesIO
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def link_callback(uri, rel):
    sUrl = settings.STATIC_URL
    sRoot = settings.STATIC_ROOT
    mUrl = settings.MEDIA_URL
    mRoot = settings.MEDIA_ROOT

    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri

    if not os.path.isfile(path):    
        raise Exception( 'media URI must start with %s or %s' % (sUrl, mUrl))

    return path

def render_to_pdf(template_src,context_dict={}):
    template_name = get_template(template_src)
    html = template_name.render(context_dict)
    resultado=BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')),resultado,link_callback=link_callback)
    if not pdf.err:
        return HttpResponse(resultado.getvalue(),content_type='application/pdf')
    
    return None