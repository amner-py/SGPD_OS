from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src,context_dict={}):
    template_name = get_template(template_src)
    html = template_name.render(context_dict)
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')),resultado)
    if not pdf.err:
        return HttpsResponse(resultado.getValue(),content_type='application/pdf')
    
    return None