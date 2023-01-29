import io, time
from django.conf import settings
from django.core.exceptions import BadRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from functools import partial
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import BaseDocTemplate, Frame, Image, PageTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from register_events.models import Event, Participant

pagesize = landscape(A4)
bottomMargin = 18
leftMargin = 144
rightMargin = 144
topMargin = 72
width_total, height_total = pagesize
width_util = width_total - (leftMargin + rightMargin)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER, fontSize=15, leading=25))
styles.add(ParagraphStyle(name='FontXL', alignment=TA_CENTER, fontSize=40))
styles.add(ParagraphStyle(name='FontL', alignment=TA_CENTER, fontSize=30))


def minutes_to_HMM(total_minutes: int):
    '''Converte minutos para formato 1h30min'''
    return "{}h{}min".format(*divmod(total_minutes, 60))


def base_template(ID, canvas, doc):
    '''Cria página base'''
    canvas.saveState()
    canvas.setTitle(f'Certificado { ID }')
    # page_num = canvas.getPageNumber()
    # text =  f'Página { page_num }'

    header_img = Image(
        settings.BASE_DIR  / 'apps/register_events/assets/gold-frame-border-texture.png',
        width=width_total,
        height=height_total
    )
    header_img.drawOn(canvas=canvas, x=0, y=0)
    text =  time.ctime()
    canvas.setFillColorRGB(0.75, 0.75, 0.75)
    canvas.setFont('Helvetica', 10)
    canvas.drawRightString(width_total - 36, 10, text)
    canvas.restoreState()


def see_pdf(request, event_id, participant_id):
    participant = Participant.objects.get(pk=participant_id)
    event = get_object_or_404(Event, pk=event_id)
    if event not in participant.events.all():
        raise BadRequest('Bad request!')

    buffer = io.BytesIO()
    doc = BaseDocTemplate(
        buffer,
        pagesize=pagesize,
        bottomMargin=bottomMargin,
        leftMargin=leftMargin,
        rightMargin=rightMargin,
        topMargin=topMargin*2.5,
    )

    frame = Frame(leftMargin, bottomMargin, doc.width, doc.height, id='normal')
    template_header = PageTemplate(
        id='base_template',
        frames=frame,
        onPage=partial(base_template, f'{ event_id } - { participant_id }'),
    )
    doc.addPageTemplates([template_header])
    Story = []

    Story.append(Paragraph('<i><strong>Certificado</strong></i>', styles['FontXL']))
    Story.append(Spacer(1, 60))

    Story.append(Paragraph('Certificamos que, para os devidos fins, o participante', styles['Center']))
    Story.append(Spacer(1, 10))

    Story.append(Paragraph(participant.name, styles['FontL']))
    Story.append(Spacer(1, 40))

    ptext = f'''
        concluiu o curso livre de "<strong>{ event.name }</strong>"
        ministrado pelo profissional <strong>{ event.taught_by }</strong>
        em <strong>{ event.date.strftime("%d/%m/%Y") }</strong>
        com duração de <strong>{ minutes_to_HMM(event.how_long) }</strong>.
    '''
    Story.append(Paragraph(ptext, styles['Center']))
    Story.append(Spacer(1, 40))

    img = Image(settings.BASE_DIR  / 'apps/register_events/assets/signature.png', 49*3, 22*3)
    Story.append(img)
    Story.append(Paragraph(event.taught_by, styles['Center']))

    doc.build(Story)
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
