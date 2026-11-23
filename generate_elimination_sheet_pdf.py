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

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 7)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(10 * mm, 287 * mm, "OPERATION ULTRON // ROUNDS 1 & 2 EVALUATION & ELIMINATION DOSSIER")
            self.drawRightString(200 * mm, 287 * mm, "OFFICIAL JUDGING & SELECTION SHEET (30 MARKS PER ROUND)")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(10 * mm, 285 * mm, 200 * mm, 285 * mm)

        # Footer
        self.setFont("Helvetica", 7.5)
        self.drawString(10 * mm, 7 * mm, "S.H.I.E.L.D. Cyber Defense Division &bull; Round 1 (30 M) + Round 2 (30 M) = 60 M Total")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(200 * mm, 7 * mm, page_str)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(10 * mm, 10 * mm, 200 * mm, 10 * mm)
        self.restoreState()

def build_pdf(filename="ULTRON_ROUNDS_1_AND_2_ELIMINATION_SCORE_SHEET.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=10 * mm,
        rightMargin=10 * mm,
        topMargin=14 * mm,
        bottomMargin=13 * mm
    )

    styles = getSampleStyleSheet()

    # Typography styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13.5,
        leading=16.5,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#CBD5E1'),
        alignment=0
    )

    badge_style = ParagraphStyle(
        'BadgeConf',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    ref_style = ParagraphStyle(
        'DocRef',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#94A3B8'),
        alignment=2
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=6,
        spaceAfter=3
    )

    tbl_hdr = ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1
    )

    tbl_hdr_left = ParagraphStyle(
        'TblHdrL',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    tbl_cell = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    tbl_cell_left = ParagraphStyle(
        'TblCellL',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#0F172A'),
        alignment=0
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#0F172A')
    )

    team_num_badge = ParagraphStyle(
        'TeamNumBadge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1
    )

    card_header_name = ParagraphStyle(
        'CardHdrName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#0F172A')
    )

    card_stat_lbl = ParagraphStyle(
        'CardStatLbl',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#64748B'),
        alignment=1
    )

    card_stat_box = ParagraphStyle(
        'CardStatBox',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=8.5,
        leading=10,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    card_total_box = ParagraphStyle(
        'CardTotalBox',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=9.5,
        leading=11.5,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    decision_pass = ParagraphStyle(
        'DecPass',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#15803D')
    )

    story = []

    # Banner Table
    banner_data = [
        [
            Paragraph("OFFICIAL JUDGING & ELIMINATION DOSSIER", badge_style),
            Paragraph("FORM: STARK-EVAL-R1-R2-30M", ref_style)
        ],
        [
            Paragraph("OPERATION ULTRON // ROUNDS 1 & 2 SCORING MATRIX", title_style),
            ""
        ],
        [
            Paragraph("Consolidated Team Performance & Selection for Round 3 Elimination Cutoff (30 Marks per Round)", subtitle_style),
            ""
        ]
    ]
    banner_tbl = Table(banner_data, colWidths=[130 * mm, 60 * mm])
    banner_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#090D16')),
        ('SPAN', (0, 1), (1, 1)),
        ('SPAN', (0, 2), (1, 2)),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('LINEBEFORE', (0,0), (0,-1), 3.5, colors.HexColor('#E11D48')),
    ]))
    story.append(banner_tbl)
    story.append(Spacer(1, 2 * mm))

    # Event Meta Block
    meta_data = [
        [
            Paragraph("<b>Evaluation Date:</b> _______________", meta_val),
            Paragraph("<b>Venue / Lab:</b> ____________________", meta_val),
            Paragraph("<b>Lead Evaluator:</b> ____________________", meta_val)
        ],
        [
            Paragraph("<b>Round 1:</b> 30 Questions = <b>30 Marks</b> (1 Mark/Q)", meta_val),
            Paragraph("<b>Round 2:</b> 30 Emails = <b>30 Marks</b> (10E + 10M + 10H)", meta_val),
            Paragraph("<b>Combined Total:</b> <b>60 Marks</b> &nbsp;|&nbsp; <b>Cutoff:</b> Top ____ Teams", meta_val)
        ]
    ]
    meta_tbl = Table(meta_data, colWidths=[63 * mm, 64 * mm, 63 * mm])
    meta_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(meta_tbl)
    story.append(Spacer(1, 2.5 * mm))

    # Page 1: Master Elimination Leaderboard Table
    story.append(Paragraph("1. MASTER 10-TEAM CONSOLIDATED LEADERBOARD & ELIMINATION AUDIT", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=2 * mm))

    master_headers = [
        Paragraph("Rank", tbl_hdr),
        Paragraph("Team ID", tbl_hdr),
        Paragraph("Team Name & Leader", tbl_hdr_left),
        Paragraph("Round 1<br/>(Recon /30)", tbl_hdr),
        Paragraph("Round 2<br/>(Phish /30)", tbl_hdr),
        Paragraph("Combined<br/>Total (/60)", tbl_hdr),
        Paragraph("Tiebreaker<br/>Time", tbl_hdr),
        Paragraph("Elimination Verdict", tbl_hdr),
        Paragraph("Judge Init", tbl_hdr)
    ]

    master_rows = [master_headers]
    for i in range(1, 11):
        num_str = f"T-{i:02d}"
        master_rows.append([
            Paragraph(f"<b>#{i}</b>", tbl_cell),
            Paragraph(f"<b>{num_str}</b>", tbl_cell),
            Paragraph(f"Team {i}: _________________________________", tbl_cell_left),
            Paragraph("[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 30 ]", tbl_cell),
            Paragraph("[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 30 ]", tbl_cell),
            Paragraph("<b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 60 ]</b>", tbl_cell),
            Paragraph("____ : ____", tbl_cell),
            Paragraph("[ &nbsp; ] ADVANCE &nbsp;&nbsp; [ &nbsp; ] ELIMINATE", tbl_cell_left),
            Paragraph("_______", tbl_cell)
        ])

    master_tbl = Table(master_rows, colWidths=[9 * mm, 12 * mm, 52 * mm, 20 * mm, 20 * mm, 20 * mm, 14 * mm, 32 * mm, 11 * mm])
    m_style = [
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 2.5),
        ('RIGHTPADDING', (0,0), (-1,-1), 2.5),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]
    for r in range(1, len(master_rows)):
        if r % 2 == 0:
            m_style.append(('BACKGROUND', (0, r), (-1, r), colors.HexColor('#F8FAFC')))
    master_tbl.setStyle(TableStyle(m_style))
    story.append(master_tbl)
    story.append(Spacer(1, 2.5 * mm))

    # Cutoff Rule Callout
    cutoff_box_data = [
        [
            Paragraph("<b>ELIMINATION PROTOCOL & TIEBREAKERS (60 MARKS TOTAL):</b><br/>"
                      "1. Top ranked teams advance to <b>Round 3: Cryptographic Decryption</b>.<br/>"
                      "2. <b>Primary Tiebreaker:</b> Highest marks in Round 2 Hard Tier (Emails 21–30, max 10 marks).<br/>"
                      "3. <b>Secondary Tiebreaker:</b> Highest marks in Round 1 Tier 6 (Questions 26–30, max 5 marks).<br/>"
                      "4. <b>Final Tiebreaker:</b> Shortest verified submission timestamp for Round 2.", meta_val),
            Paragraph("<b>OFFICIAL CUT-OFF SELECTION:</b><br/><br/>"
                      "Advancement Cutoff: Rank # ______<br/>"
                      "Total Advancing: ______ Teams<br/>"
                      "Total Eliminated: ______ Teams", meta_val)
        ]
    ]
    cutoff_tbl = Table(cutoff_box_data, colWidths=[135 * mm, 55 * mm])
    cutoff_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF1F2')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#FECDD3')),
        ('LINEBEFORE', (0,0), (0,-1), 3, colors.HexColor('#E11D48')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(cutoff_tbl)

    story.append(PageBreak())

    # Page 2: Detailed Team Scoring Cards (Teams 1 to 5)
    story.append(Paragraph("2. INDIVIDUAL TEAM EVALUATION CARDS // TEAMS 01 – 05 (30 MARKS EACH ROUND)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=2.5 * mm))

    def create_team_card(team_id_num):
        card_data = [
            # Row 0: Header
            [
                Paragraph(f"<b>TEAM {team_id_num:02d}</b>", team_num_badge),
                Paragraph(f"<b>Team Name:</b> ____________________________________________________", card_header_name),
                Paragraph("<b>Table / Lab Seat:</b> ________", card_header_name)
            ],
            # Row 1: Metrics Header
            [
                Paragraph("<b>Round 1 (Recon Quiz)</b>", card_stat_lbl),
                Paragraph("<b>Round 2 Breakdown (30 Emails: Easy / Med / Hard)</b>", card_stat_lbl),
                Paragraph("<b>Round 2 Subtotal</b>", card_stat_lbl)
            ],
            # Row 2: Score Inputs
            [
                Paragraph("Score: <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 30 ]</b><br/><font size='6' color='#64748B'>30 Questions &bull; 1 Mark/Q</font>", card_stat_box),
                Paragraph("Easy (Q1-10): <b>[ &nbsp;&nbsp;&nbsp; / 10 ]</b> &nbsp;&bull;&nbsp; Med (Q11-20): <b>[ &nbsp;&nbsp;&nbsp; / 10 ]</b> &nbsp;&bull;&nbsp; Hard (Q21-30): <b>[ &nbsp;&nbsp; / 10 ]</b>", card_stat_box),
                Paragraph("Score: <b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 30 ]</b><br/><font size='6' color='#64748B'>30 Emails &bull; 1 Mark/Email</font>", card_stat_box)
            ],
            # Row 3: Totals & Elimination Decision
            [
                Paragraph("<b>COMBINED SCORE:</b><br/><font size='11'><b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 60 ]</b></font>", card_total_box),
                Paragraph("<b>ELIMINATION STATUS / SELECTION:</b><br/>"
                          "[ &nbsp; ] <b>QUALIFIED &bull; ADVANCE TO ROUND 3</b> &nbsp;&nbsp;&nbsp;&nbsp;"
                          "[ &nbsp; ] <b>ELIMINATED &bull; BELOW CUTOFF</b><br/>"
                          "[ &nbsp; ] <b>TIED / ON BUBBLE</b> (Apply Tiebreaker Criteria)", decision_pass),
                Paragraph("<b>FINAL RANK:</b><br/><font size='10'><b>[ # ______ ]</b></font><br/>Sign: _________", card_stat_box)
            ],
            # Row 4: Remarks
            [
                Paragraph("<b>Judge Remarks / Disciplinary / Time Latency:</b> ____________________________________________________________________________________________", meta_val),
                "",
                ""
            ]
        ]

        team_tbl = Table(card_data, colWidths=[38 * mm, 117 * mm, 35 * mm])
        c_style = [
            ('SPAN', (0, 4), (2, 4)),
            ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#0F172A')),
            ('BACKGROUND', (1, 0), (2, 0), colors.HexColor('#F1F5F9')),
            ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#F8FAFC')),
            ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#FFFFFF')),
            ('BACKGROUND', (0, 3), (0, 3), colors.HexColor('#EEF2F6')),
            ('BACKGROUND', (1, 3), (1, 3), colors.HexColor('#F8FAFC')),
            ('BACKGROUND', (2, 3), (2, 3), colors.HexColor('#EEF2F6')),
            ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#FFFFFF')),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
            ('INNERGRID', (0, 0), (-1, 3), 0.5, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0, 0), (-1, -1), 2.2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2),
            ('LEFTPADDING', (0, 0), (-1, -1), 3.5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 3.5),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]
        team_tbl.setStyle(TableStyle(c_style))
        return team_tbl

    for t in range(1, 6):
        story.append(create_team_card(t))
        story.append(Spacer(1, 2.5 * mm))

    story.append(PageBreak())

    # Page 3: Detailed Team Scoring Cards (Teams 6 to 10) + Final Certification
    story.append(Paragraph("3. INDIVIDUAL TEAM EVALUATION CARDS // TEAMS 06 – 10 (30 MARKS EACH ROUND)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=2.5 * mm))

    for t in range(6, 11):
        story.append(create_team_card(t))
        story.append(Spacer(1, 2.5 * mm))

    story.append(Spacer(1, 2 * mm))

    # Official Certification Block
    cert_data = [
        [
            Paragraph("<b>OFFICIAL EVALUATION & ELIMINATION CERTIFICATION</b><br/>"
                      "We hereby certify that all marks from Round 1 (30 Questions = 30 Marks) and Round 2 (30 Emails = 30 Marks, Combined 60 Marks) "
                      "have been strictly computed, cross-verified, and validated against official answer keys without bias. "
                      "Teams checked 'QUALIFIED' are officially promoted to Round 3: Cryptographic Decryption.", meta_val),
            Paragraph("<b>EVALUATOR SIGNATURES:</b><br/><br/>"
                      "Lead Judge: ____________________<br/>"
                      "Scoring Master: __________________<br/>"
                      "Date & Time: ____________________", meta_val)
        ]
    ]
    cert_tbl = Table(cert_data, colWidths=[130 * mm, 60 * mm])
    cert_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('LINEBEFORE', (0,0), (0,-1), 3, colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(cert_tbl)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename} (Size: {os.path.getsize(filename)} bytes)")

if __name__ == "__main__":
    out_name = sys.argv[1] if len(sys.argv) > 1 else "ULTRON_ROUNDS_1_AND_2_ELIMINATION_SCORE_SHEET.pdf"
    build_pdf(out_name)
