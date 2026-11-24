import os
import sys
from reportlab.lib.pagesizes import A4, landscape
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
            self.drawString(10 * mm, 287 * mm, "TECHNIX 8.0 // GRAND FINALE ALL-ROUNDS EVALUATION & RANKING DOSSIER")
            self.drawRightString(200 * mm, 287 * mm, "OFFICIAL JUDGING MATRIX (ROUNDS 1, 2, 3 & 4 • 165 MARKS TOTAL)")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(10 * mm, 285 * mm, 200 * mm, 285 * mm)

        # Footer
        self.setFont("Helvetica", 7.5)
        self.drawString(10 * mm, 7 * mm, "TECHNIX 8.0 Cyber Defense Symposium • R1 (30M) + R2 (30M) + R3 (45M) + R4 (60M) = 165M Total")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(200 * mm, 7 * mm, page_str)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(10 * mm, 10 * mm, 200 * mm, 10 * mm)
        self.restoreState()


def build_multipage_pdf(filename="TECHNIX8_FINAL_GRAND_TOURNAMENT_SCORECARD_4ROUNDS.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=8 * mm,
        rightMargin=8 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm
    )

    styles = getSampleStyleSheet()

    # Typography styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
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
        fontSize=9,
        leading=11.5,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=4,
        spaceAfter=2
    )

    tbl_hdr = ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1
    )

    tbl_hdr_left = ParagraphStyle(
        'TblHdrL',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    tbl_cell = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    tbl_cell_left = ParagraphStyle(
        'TblCellL',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#0F172A'),
        alignment=0
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#0F172A')
    )

    team_num_badge = ParagraphStyle(
        'TeamNumBadge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=9.5,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1
    )

    card_header_name = ParagraphStyle(
        'CardHdrName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#0F172A')
    )

    card_stat_lbl = ParagraphStyle(
        'CardStatLbl',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6,
        leading=7.5,
        textColor=colors.HexColor('#475569'),
        alignment=1
    )

    card_stat_box = ParagraphStyle(
        'CardStatBox',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=8,
        leading=9.5,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    card_total_box = ParagraphStyle(
        'CardTotalBox',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    award_style = ParagraphStyle(
        'AwardStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#047857')
    )

    story = []

    # Banner Table (Page 1)
    banner_data = [
        [
            Paragraph("OFFICIAL MASTER TOURNAMENT SCORING & FINAL RANKINGS", badge_style),
            Paragraph("FORM: TECHNIX8-GRAND-ALL-ROUNDS-165M", ref_style)
        ],
        [
            Paragraph("TECHNIX 8.0 // ALL-ROUND CONSOLIDATED MASTER SCORECARD", title_style),
            ""
        ],
        [
            Paragraph("Comprehensive 4-Round Evaluation (R1: 30M &bull; R2: 30M &bull; R3: 45M &bull; R4: 60M &bull; Total: 165 Marks) & Podium Ranks", subtitle_style),
            ""
        ]
    ]
    banner_tbl = Table(banner_data, colWidths=[134 * mm, 60 * mm])
    banner_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#090D16')),
        ('SPAN', (0, 1), (1, 1)),
        ('SPAN', (0, 2), (1, 2)),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('LINEBEFORE', (0,0), (0,-1), 3.5, colors.HexColor('#2563EB')),
    ]))
    story.append(banner_tbl)
    story.append(Spacer(1, 1.5 * mm))

    # Event Meta Block
    meta_data = [
        [
            Paragraph("<b>Evaluation Date:</b> _______________", meta_val),
            Paragraph("<b>Venue / Lab:</b> ____________________", meta_val),
            Paragraph("<b>Lead Evaluator:</b> ____________________", meta_val)
        ],
        [
            Paragraph("<b>Round 1 (Recon Quiz):</b> 30 Qs = <b>30 M</b>", meta_val),
            Paragraph("<b>Round 2 (Phishing Triage):</b> 30 Emails = <b>30 M</b>", meta_val),
            Paragraph("<b>Round 3 (Crypto Decryption):</b> 15M + 30M = <b>45 M</b>", meta_val)
        ],
        [
            Paragraph("<b>Round 4 (Citadel CTF):</b> 4 Levels = <b>60 M</b>", meta_val),
            Paragraph("<b>GRAND TOTAL SCORE:</b> <b>165 MARKS</b>", meta_val),
            Paragraph("<b>Tiebreaker:</b> R4 Score &bull; R4 Time &bull; R3 Hard", meta_val)
        ]
    ]
    meta_tbl = Table(meta_data, colWidths=[64 * mm, 66 * mm, 64 * mm])
    meta_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(meta_tbl)
    story.append(Spacer(1, 2 * mm))

    # Page 1: Grand Master Consolidated Leaderboard Table
    story.append(Paragraph("1. MASTER 10-TEAM ALL-ROUND LEADERBOARD & FINAL RANKINGS AUDIT", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CBD5E1'), spaceAfter=1.5 * mm))

    master_headers = [
        Paragraph("Rank", tbl_hdr),
        Paragraph("Team ID", tbl_hdr),
        Paragraph("Team Name & Members", tbl_hdr_left),
        Paragraph("R-1<br/>Recon<br/>(/30)", tbl_hdr),
        Paragraph("R-2<br/>Phish<br/>(/30)", tbl_hdr),
        Paragraph("R-3<br/>Crypto<br/>(/45)", tbl_hdr),
        Paragraph("R-4<br/>CTF<br/>(/60)", tbl_hdr),
        Paragraph("GRAND<br/>TOTAL<br/>(/165)", tbl_hdr),
        Paragraph("CTF<br/>Time", tbl_hdr),
        Paragraph("Final Standing & Official Award", tbl_hdr),
        Paragraph("Sign", tbl_hdr)
    ]

    master_rows = [master_headers]
    for i in range(1, 11):
        num_str = f"T-{i:02d}"
        master_rows.append([
            Paragraph(f"<b>#{i}</b>", tbl_cell),
            Paragraph(f"<b>{num_str}</b>", tbl_cell),
            Paragraph(f"Team {i}: _________________________________", tbl_cell_left),
            Paragraph("[ &nbsp;&nbsp;&nbsp;&nbsp; / 30 ]", tbl_cell),
            Paragraph("[ &nbsp;&nbsp;&nbsp;&nbsp; / 30 ]", tbl_cell),
            Paragraph("[ &nbsp;&nbsp;&nbsp;&nbsp; / 45 ]", tbl_cell),
            Paragraph("[ &nbsp;&nbsp;&nbsp;&nbsp; / 60 ]", tbl_cell),
            Paragraph("<b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 165 ]</b>", tbl_cell),
            Paragraph("___:___", tbl_cell),
            Paragraph("[ &nbsp; ] 1st &nbsp; [ &nbsp; ] 2nd &nbsp; [ &nbsp; ] 3rd &nbsp; [ &nbsp; ] Finalist", tbl_cell_left),
            Paragraph("_____", tbl_cell)
        ])

    # Col Widths total: 8+12+43+14+14+16+16+24+14+24+9 = 194 mm
    master_tbl = Table(master_rows, colWidths=[8 * mm, 12 * mm, 43 * mm, 14 * mm, 14 * mm, 16 * mm, 16 * mm, 24 * mm, 14 * mm, 24 * mm, 9 * mm])
    m_style = [
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]
    for r in range(1, len(master_rows)):
        if r % 2 == 0:
            m_style.append(('BACKGROUND', (0, r), (-1, r), colors.HexColor('#F8FAFC')))
    master_tbl.setStyle(TableStyle(m_style))
    story.append(master_tbl)
    story.append(Spacer(1, 2 * mm))

    # Tiebreaker & Ranking Protocol Callout
    protocol_box_data = [
        [
            Paragraph("<b>OFFICIAL TIE-BREAKER PROTOCOL (165 MARKS TOTAL):</b><br/>"
                      "1. <b>Primary Score:</b> Highest cumulative Grand Total across all 4 rounds (/165 Marks).<br/>"
                      "2. <b>Tiebreaker 1:</b> Highest score obtained in <b>Round 4: Citadel CTF</b> (max 60 Marks).<br/>"
                      "3. <b>Tiebreaker 2:</b> Shortest verified completion split time for highest cleared level in Round 4 (from Judge HUD PIN 0804).<br/>"
                      "4. <b>Tiebreaker 3:</b> Highest score in <b>Round 3: Phase 2 Hard Decryption Chit</b> (max 20 Marks).<br/>"
                      "5. <b>Tiebreaker 4:</b> Highest score in <b>Round 2: Hard Phishing Triage</b> (Emails 21–30, max 10 Marks).", meta_val),
            Paragraph("<b>TOURNAMENT PODIUM ALLOCATION:</b><br/>"
                      "&bull; <b>Rank #1 (Champion):</b> ____________________<br/>"
                      "&bull; <b>Rank #2 (1st Runner-Up):</b> ______________<br/>"
                      "&bull; <b>Rank #3 (2nd Runner-Up):</b> ______________<br/>"
                      "&bull; <b>Best Cryptographer (R3):</b> ______________<br/>"
                      "&bull; <b>Fastest CTF Infiltrator (R4):</b> ___________", meta_val)
        ]
    ]
    protocol_tbl = Table(protocol_box_data, colWidths=[114 * mm, 80 * mm])
    protocol_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#BFDBFE')),
        ('LINEBEFORE', (0,0), (0,-1), 3, colors.HexColor('#2563EB')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(protocol_tbl)

    story.append(PageBreak())

    # Page 2: Detailed Team Scoring Cards (Teams 1 to 5)
    story.append(Paragraph("2. INDIVIDUAL TEAM PERFORMANCE CARDS // TEAMS 01 – 05 (165 MARKS TOTAL)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CBD5E1'), spaceAfter=2 * mm))

    def create_team_card(team_id_num):
        card_data = [
            # Row 0: Header
            [
                Paragraph(f"<b>TEAM {team_id_num:02d}</b>", team_num_badge),
                Paragraph(f"<b>Team Name:</b> ____________________________________________________", card_header_name),
                Paragraph("<b>Station / PC:</b> ______", card_header_name)
            ],
            # Row 1: Sub-scores Across All 4 Rounds
            [
                Paragraph("<b>Round 1: Recon</b><br/><font size='7.5'><b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 30 ]</b></font><br/>"
                          "<font size='5.5' color='#64748B'>30 Questions &bull; 1M/Q</font>", card_stat_box),
                Paragraph("<b>Round 2: Phish</b><br/><font size='7.5'><b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 30 ]</b></font><br/>"
                          "<font size='5.5' color='#64748B'>E: ___ M: ___ H: ___</font>", card_stat_box),
                Paragraph("<b>Round 3: Crypto</b><br/><font size='7.5'><b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 45 ]</b></font><br/>"
                          "<font size='5.5' color='#64748B'>Q: ___/15 &bull; E: ___/10 &bull; H: ___/20</font>", card_stat_box),
                Paragraph("<b>Round 4: CTF</b><br/><font size='7.5'><b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 60 ]</b></font><br/>"
                          "<font size='5.5' color='#64748B'>L1:5 &bull; L2:10 &bull; L3:15 &bull; L4:30</font>", card_stat_box)
            ],
            # Row 2: Totals & Ranking
            [
                Paragraph("<b>GRAND TOTAL:</b><br/><font size='10'><b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 165 ]</b></font>", card_total_box),
                Paragraph("<b>CTF TELEMETRY:</b><br/>Split Time: <b>___m ___s</b><br/>Attempts: <b>____</b>", card_stat_box),
                Paragraph("<b>FINAL RANKING:</b><br/><font size='9.5'><b>[ # ______ ]</b></font><br/>Sign: ________", card_total_box),
                Paragraph("<b>AWARD VERDICT:</b><br/>"
                          "[ &nbsp; ] <b>1st (Champion)</b><br/>"
                          "[ &nbsp; ] <b>2nd</b> &nbsp;&nbsp; [ &nbsp; ] <b>3rd</b> &nbsp;&nbsp; [ &nbsp; ] <b>Finalist</b>", award_style)
            ],
            # Row 3: Remarks
            [
                Paragraph("<b>Evaluator Verification Notes:</b> ____________________________________________________________________________________________", meta_val),
                "",
                "",
                ""
            ]
        ]

        team_tbl = Table(card_data, colWidths=[40 * mm, 50 * mm, 54 * mm, 50 * mm])
        c_style = [
            ('SPAN', (0, 0), (0, 0)),
            ('SPAN', (1, 0), (1, 0)),
            ('SPAN', (2, 0), (3, 0)),
            ('SPAN', (0, 3), (3, 3)),
            ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#0F172A')),
            ('BACKGROUND', (1, 0), (3, 0), colors.HexColor('#F1F5F9')),
            ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#FFFFFF')),
            ('BACKGROUND', (0, 2), (0, 2), colors.HexColor('#EFF6FF')),
            ('BACKGROUND', (1, 2), (1, 2), colors.HexColor('#F8FAFC')),
            ('BACKGROUND', (2, 2), (2, 2), colors.HexColor('#EFF6FF')),
            ('BACKGROUND', (3, 2), (3, 2), colors.HexColor('#F0FDF4')),
            ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#FFFFFF')),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
            ('INNERGRID', (0, 0), (-1, 2), 0.5, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0, 0), (-1, -1), 1.8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1.8),
            ('LEFTPADDING', (0, 0), (-1, -1), 3),
            ('RIGHTPADDING', (0, 0), (-1, -1), 3),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]
        team_tbl.setStyle(TableStyle(c_style))
        return team_tbl

    for t in range(1, 6):
        story.append(create_team_card(t))
        story.append(Spacer(1, 2 * mm))

    story.append(PageBreak())

    # Page 3: Detailed Team Scoring Cards (Teams 6 to 10) + Final Certification
    story.append(Paragraph("3. INDIVIDUAL TEAM PERFORMANCE CARDS // TEAMS 06 – 10 (165 MARKS TOTAL)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CBD5E1'), spaceAfter=2 * mm))

    for t in range(6, 11):
        story.append(create_team_card(t))
        story.append(Spacer(1, 2 * mm))

    story.append(Spacer(1, 1.5 * mm))

    # Official Certification Block
    cert_data = [
        [
            Paragraph("<b>FINAL TOURNAMENT ADJUDICATION & PODIUM CERTIFICATION</b><br/>"
                      "We, the undersigned Lead Judges and Event Directors, hereby certify that scores across all 4 operational rounds "
                      "(Round 1: 30M, Round 2: 30M, Round 3: 45M, Round 4: 60M — Cumulative Total 165 Marks) have been strictly audited, "
                      "calculated, and verified. Official ranks and podium awards recorded herein are final, binding, and conclusive.", meta_val),
            Paragraph("<b>EVALUATOR SIGNATURES & STAMP:</b><br/><br/>"
                      "Lead Judge: ________________________<br/>"
                      "Technical Chair: ____________________<br/>"
                      "Symposium Convenor: ______________<br/>"
                      "Date & Time: _______________________", meta_val)
        ]
    ]
    cert_tbl = Table(cert_data, colWidths=[126 * mm, 68 * mm])
    cert_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('LINEBEFORE', (0,0), (0,-1), 3, colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(cert_tbl)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated Multi-Page Scorecard {filename} (Size: {os.path.getsize(filename)} bytes)")


def build_1page_landscape_pdf(filename="TECHNIX8_FINAL_1PAGE_GRAND_SCORECARD.pdf"):
    # A4 Landscape: 297mm x 210mm
    doc = SimpleDocTemplate(
        filename,
        pagesize=landscape(A4),
        leftMargin=8 * mm,
        rightMargin=8 * mm,
        topMargin=8 * mm,
        bottomMargin=8 * mm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitleL',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=14,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    sub_style = ParagraphStyle(
        'DocSubL',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#CBD5E1'),
        alignment=0
    )

    badge_style = ParagraphStyle(
        'BadgeL',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=2
    )

    meta_style = ParagraphStyle(
        'MetaL',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#0F172A')
    )

    tbl_hdr = ParagraphStyle(
        'TblHdrLnd',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=1
    )

    tbl_hdr_left = ParagraphStyle(
        'TblHdrLeftLnd',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    tbl_cell = ParagraphStyle(
        'TblCellLnd',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    tbl_cell_bold = ParagraphStyle(
        'TblCellBoldLnd',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=7.5,
        leading=9,
        textColor=colors.HexColor('#0F172A'),
        alignment=1
    )

    tbl_cell_left = ParagraphStyle(
        'TblCellLeftLnd',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor('#0F172A'),
        alignment=0
    )

    story = []

    # Compact Header Banner (Landscape 281mm wide)
    header_data = [
        [
            Paragraph("TECHNIX 8.0 // 1-PAGE GRAND MASTER SCORECARD & FINAL RANKINGS", title_style),
            Paragraph("CONFIDENTIAL // JUDGES CONSOLE", badge_style)
        ],
        [
            Paragraph("All 4 Rounds Unified Evaluation: Round 1 (30M) + Round 2 (30M) + Round 3 (45M) + Round 4 (60M) = <b>165 Marks Total</b>", sub_style),
            ""
        ]
    ]
    header_tbl = Table(header_data, colWidths=[210 * mm, 71 * mm])
    header_tbl.setStyle(TableStyle([
        ('SPAN', (0, 1), (1, 1)),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#090D16')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('LINEBEFORE', (0,0), (0,-1), 3, colors.HexColor('#2563EB')),
    ]))
    story.append(header_tbl)
    story.append(Spacer(1, 1.2 * mm))

    # Meta bar
    meta_data = [
        [
            Paragraph("<b>Date:</b> ____________", meta_style),
            Paragraph("<b>Venue:</b> ____________", meta_style),
            Paragraph("<b>Round 1:</b> <b>30 M</b> (Recon)", meta_style),
            Paragraph("<b>Round 2:</b> <b>30 M</b> (Phish)", meta_style),
            Paragraph("<b>Round 3:</b> <b>45 M</b> (Crypto)", meta_style),
            Paragraph("<b>Round 4:</b> <b>60 M</b> (CTF)", meta_style),
            Paragraph("<b>GRAND TOTAL:</b> <b>165 M</b>", meta_style),
            Paragraph("<b>Tiebreak:</b> R4 Score &bull; R4 Split Time", meta_style)
        ]
    ]
    meta_tbl = Table(meta_data, colWidths=[26 * mm, 28 * mm, 32 * mm, 32 * mm, 35 * mm, 32 * mm, 40 * mm, 56 * mm])
    meta_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ('LEFTPADDING', (0,0), (-1,-1), 2.5),
        ('RIGHTPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(meta_tbl)
    story.append(Spacer(1, 1.5 * mm))

    # Master Table (281 mm wide)
    # Col widths: 11+14+46+17+18+18+24+20+24+27+16+16+30 = 281 mm
    master_headers = [
        Paragraph("Rank", tbl_hdr),
        Paragraph("Team", tbl_hdr),
        Paragraph("Team Name & Members", tbl_hdr_left),
        Paragraph("R-1<br/>Recon<br/>(/30)", tbl_hdr),
        Paragraph("R-2<br/>Phish<br/>(/30)", tbl_hdr),
        Paragraph("Sub<br/>R1+R2<br/>(/60)", tbl_hdr),
        Paragraph("R-3<br/>Crypto<br/>(/45)", tbl_hdr),
        Paragraph("Sub<br/>R1-R3<br/>(/105)", tbl_hdr),
        Paragraph("R-4<br/>CTF<br/>(/60)", tbl_hdr),
        Paragraph("GRAND<br/>TOTAL<br/>(/165)", tbl_hdr),
        Paragraph("CTF<br/>Time", tbl_hdr),
        Paragraph("Final<br/>Rank", tbl_hdr),
        Paragraph("Podium & Award Standing", tbl_hdr_left)
    ]

    master_rows = [master_headers]
    for i in range(1, 11):
        num_str = f"T-{i:02d}"
        master_rows.append([
            Paragraph(f"<b>#{i}</b>", tbl_cell),
            Paragraph(f"<b>{num_str}</b>", tbl_cell),
            Paragraph(f"Team {i}: ___________________________________________", tbl_cell_left),
            Paragraph("[ &nbsp;&nbsp;&nbsp; / 30 ]", tbl_cell),
            Paragraph("[ &nbsp;&nbsp;&nbsp; / 30 ]", tbl_cell),
            Paragraph("[ &nbsp;&nbsp;&nbsp; / 60 ]", tbl_cell),
            Paragraph("[ &nbsp;&nbsp;&nbsp; / 45 ]", tbl_cell),
            Paragraph("[ &nbsp;&nbsp;&nbsp;&nbsp; / 105 ]", tbl_cell),
            Paragraph("[ &nbsp;&nbsp;&nbsp; / 60 ]", tbl_cell),
            Paragraph("<b>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 165 ]</b>", tbl_cell_bold),
            Paragraph("___:___", tbl_cell),
            Paragraph("<b># ___</b>", tbl_cell_bold),
            Paragraph("[ &nbsp; ] 1st &nbsp; [ &nbsp; ] 2nd &nbsp; [ &nbsp; ] 3rd &nbsp; [ &nbsp; ] Fin", tbl_cell_left)
        ])

    master_tbl = Table(master_rows, colWidths=[11 * mm, 14 * mm, 46 * mm, 17 * mm, 18 * mm, 18 * mm, 24 * mm, 20 * mm, 24 * mm, 27 * mm, 16 * mm, 16 * mm, 30 * mm])
    m_style = [
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]
    for r in range(1, len(master_rows)):
        if r % 2 == 0:
            m_style.append(('BACKGROUND', (0, r), (-1, r), colors.HexColor('#F8FAFC')))
    master_tbl.setStyle(TableStyle(m_style))
    story.append(master_tbl)
    story.append(Spacer(1, 1.5 * mm))

    # Bottom certification bar
    foot_data = [
        [
            Paragraph("<b>EVALUATION CERTIFICATION:</b> We verify that scores across all 4 rounds (Total 165 Marks) are accurate.<br/>"
                      "<b>Podium Winners:</b> &nbsp; <b>1st Place (Champion):</b> ______________________ &nbsp;&bull;&nbsp; "
                      "<b>2nd Place:</b> ______________________ &nbsp;&bull;&nbsp; <b>3rd Place:</b> ______________________", meta_style),
            Paragraph("Lead Judge Signature: _______________________<br/>"
                      "Convenor Signature: ________________________", meta_style)
        ]
    ]
    foot_tbl = Table(foot_data, colWidths=[205 * mm, 76 * mm])
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
    print(f"Successfully generated 1-Page Landscape Scorecard {filename} (Size: {os.path.getsize(filename)} bytes)")


if __name__ == "__main__":
    out_multi = sys.argv[1] if len(sys.argv) > 1 else "TECHNIX8_FINAL_GRAND_TOURNAMENT_SCORECARD_4ROUNDS.pdf"
    out_1page = sys.argv[2] if len(sys.argv) > 2 else "TECHNIX8_FINAL_1PAGE_GRAND_SCORECARD.pdf"
    build_multipage_pdf(out_multi)
    build_1page_landscape_pdf(out_1page)
