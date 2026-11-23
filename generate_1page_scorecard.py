import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

def build_1page_pdf(filename="ULTRON_ROUNDS_1_AND_2_1PAGE_SCORECARD.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=8 * mm,
        rightMargin=8 * mm,
        topMargin=8 * mm,
        bottomMargin=8 * mm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=14,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    sub_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#CBD5E1'),
        alignment=0
    )

    badge_style = ParagraphStyle(
        'Badge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#FFFFFF')
    )

    meta_style = ParagraphStyle(
        'Meta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#0F172A')
    )

    team_badge = ParagraphStyle(
        'TBadge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=9.5,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1
    )

    team_name = ParagraphStyle(
        'TName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9,
        textColor=colors.HexColor('#0F172A')
    )

    score_box = ParagraphStyle(
        'SBox',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=8,
        leading=9.5,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    score_lbl = ParagraphStyle(
        'SLbl',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6,
        leading=7.5,
        textColor=colors.HexColor('#64748B'),
        alignment=1
    )

    total_box = ParagraphStyle(
        'TBox',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=9,
        leading=10.5,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    dec_qual = ParagraphStyle(
        'DQual',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#15803D')
    )

    dec_elim = ParagraphStyle(
        'DElim',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#B91C1C')
    )

    story = []

    # Compact Header Banner
    header_data = [
        [
            Paragraph("OPERATION ULTRON // 10-TEAM RAPID EVALUATION SCORECARD", title_style),
            Paragraph("CONFIDENTIAL // JUDGES ROSTER", badge_style)
        ],
        [
            Paragraph("Rounds 1 & 2 Marks Verification (30 Marks Each &bull; 60 Marks Total) & Round 3 Elimination Selection", sub_style),
            ""
        ]
    ]
    header_tbl = Table(header_data, colWidths=[140 * mm, 54 * mm])
    header_tbl.setStyle(TableStyle([
        ('SPAN', (0, 1), (1, 1)),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#090D16')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('LINEBEFORE', (0,0), (0,-1), 3, colors.HexColor('#E11D48')),
    ]))
    story.append(header_tbl)
    story.append(Spacer(1, 1.5 * mm))

    # Meta bar
    meta_data = [
        [
            Paragraph("<b>Date:</b> ____________", meta_style),
            Paragraph("<b>Venue:</b> ____________", meta_style),
            Paragraph("<b>Round 1:</b> 30 Qs = <b>30 M</b>", meta_style),
            Paragraph("<b>Round 2:</b> 30 Emails = <b>30 M</b>", meta_style),
            Paragraph("<b>Total:</b> <b>60 M</b>", meta_style),
            Paragraph("<b>Cutoff:</b> Top ___ Advance", meta_style)
        ]
    ]
    meta_tbl = Table(meta_data, colWidths=[30 * mm, 32 * mm, 32 * mm, 34 * mm, 28 * mm, 38 * mm])
    meta_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(meta_tbl)
    story.append(Spacer(1, 2 * mm))

    # 10 Team Cards in a 2-Column Grid (5 rows of 2 cards each)
    def make_mini_card(t_num):
        card_content = [
            # Row 0: Team ID and Name
            [
                Paragraph(f"<b>T-{t_num:02d}</b>", team_badge),
                Paragraph(f"<b>Name:</b> ___________________________", team_name),
                Paragraph("<b>Desk:</b> ____", team_name)
            ],
            # Row 1: Scores
            [
                Paragraph("<b>Round 1 (Recon Quiz)</b><br/><font size='7.5'><b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 30 ]</b></font>", score_box),
                Paragraph("<b>Round 2 (Phishing Webmail)</b><br/><font size='7.5'><b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 30 ]</b></font><br/>"
                          "<font size='5.5' color='#64748B'>E: ___ /10 &bull; M: ___ /10 &bull; H: ___ /10</font>", score_box),
                Paragraph("<b>COMBINED</b><br/><font size='8.5'><b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 60 ]</b></font><br/>"
                          "<b>Rank: [ # ___ ]</b>", total_box)
            ],
            # Row 2: Decision
            [
                Paragraph("[ &nbsp; ] <b>ADVANCE (QUALIFIED)</b>", dec_qual),
                Paragraph("[ &nbsp; ] <b>ELIMINATED</b>", dec_elim),
                Paragraph("Sign: ________", score_lbl)
            ]
        ]
        c_tbl = Table(card_content, colWidths=[24 * mm, 46 * mm, 25 * mm])
        c_tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,0), colors.HexColor('#0F172A')),
            ('BACKGROUND', (1,0), (2,0), colors.HexColor('#F1F5F9')),
            ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#FFFFFF')),
            ('BACKGROUND', (0,2), (0,2), colors.HexColor('#DCFCE7')),
            ('BACKGROUND', (1,2), (1,2), colors.HexColor('#FEE2E2')),
            ('BACKGROUND', (2,2), (2,2), colors.HexColor('#F8FAFC')),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0,0), (-1,-1), 1.6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.6),
            ('LEFTPADDING', (0,0), (-1,-1), 2.5),
            ('RIGHTPADDING', (0,0), (-1,-1), 2.5),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        return c_tbl

    grid_rows = []
    for r in range(5):
        t1 = r * 2 + 1
        t2 = r * 2 + 2
        card1 = make_mini_card(t1)
        card2 = make_mini_card(t2)
        grid_rows.append([card1, card2])

    grid_tbl = Table(grid_rows, colWidths=[96 * mm, 96 * mm])
    grid_tbl.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
        ('LEFTPADDING', (0,0), (-1,-1), 1),
        ('RIGHTPADDING', (0,0), (-1,-1), 1),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(grid_tbl)
    story.append(Spacer(1, 1.5 * mm))

    # Bottom certification
    foot_data = [
        [
            Paragraph("<b>EVALUATION CERTIFICATION:</b> We certify that scores for all 10 teams across Round 1 (30 M) and Round 2 (30 M) are accurate.<br/>"
                      "Advancing Cutoff Line: Top ______ Teams &bull; Total Teams Promoted: ______ &bull; Total Teams Eliminated: ______", meta_style),
            Paragraph("Lead Judge Signature: _______________________<br/>"
                      "Scoring Master Signature: _____________________", meta_style)
        ]
    ]
    foot_tbl = Table(foot_data, colWidths=[125 * mm, 69 * mm])
    foot_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('LINEBEFORE', (0,0), (0,-1), 2.5, colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(foot_tbl)

    doc.build(story)
    print(f"Successfully generated 1-Page Scorecard {filename} (Size: {os.path.getsize(filename)} bytes)")

if __name__ == "__main__":
    out_name = sys.argv[1] if len(sys.argv) > 1 else "ULTRON_ROUNDS_1_AND_2_1PAGE_SCORECARD.pdf"
    build_1page_pdf(out_name)
