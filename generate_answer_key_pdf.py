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
            self.drawString(10 * mm, 287 * mm, "OPERATION ULTRON // ROUND 2: FACILITATOR MASTER ANSWER KEY")
            self.drawRightString(200 * mm, 287 * mm, "CONFIDENTIAL // EVALUATOR USE ONLY")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(10 * mm, 285 * mm, 200 * mm, 285 * mm)

        # Footer
        self.setFont("Helvetica", 7.5)
        self.drawString(10 * mm, 7 * mm, "Stark Industries Cyber Defense Division &bull; S.H.I.E.L.D. Incident Response Directive")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(200 * mm, 7 * mm, page_str)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(10 * mm, 10 * mm, 200 * mm, 10 * mm)
        self.restoreState()

def build_pdf(filename="ULTRON_ROUND2_FACILITATOR_ANSWER_KEY.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=10 * mm,
        rightMargin=10 * mm,
        topMargin=15 * mm,
        bottomMargin=14 * mm
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#CBD5E1'),
        alignment=0
    )

    badge_style = ParagraphStyle(
        'BadgeConf',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#FFFFFF'),
        alignment=0
    )

    ref_style = ParagraphStyle(
        'DocRef',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#94A3B8'),
        alignment=2
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=8,
        spaceAfter=4
    )

    tbl_hdr_style = ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#FFFFFF')
    )

    tbl_cell_style = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#0F172A')
    )

    tbl_mono_style = ParagraphStyle(
        'TblMono',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#334155')
    )

    card_title_style = ParagraphStyle(
        'CardTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=9.5,
        textColor=colors.HexColor('#0F172A')
    )

    card_label_style = ParagraphStyle(
        'CardLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#475569')
    )

    card_val_threat = ParagraphStyle(
        'CardThreat',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#B91C1C')
    )

    card_val_clean = ParagraphStyle(
        'CardClean',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor('#15803D')
    )

    card_mono = ParagraphStyle(
        'CardMono',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#0F172A')
    )

    osint_style = ParagraphStyle(
        'OSINTText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.5,
        leading=8,
        textColor=colors.HexColor('#334155')
    )

    story = []

    # Banner Table
    banner_data = [
        [
            Paragraph("CONFIDENTIAL // EVALUATOR MASTER KEY", badge_style),
            Paragraph("DOC: STARK-SOC-R2-KEY-2026", ref_style)
        ],
        [
            Paragraph("OPERATION ULTRON // ROUND 2 ANSWER KEY", title_style),
            ""
        ],
        [
            Paragraph("The Social Engineering Breach &bull; Comprehensive Webmail Forensic Verification Manual", subtitle_style),
            ""
        ]
    ]
    banner_tbl = Table(banner_data, colWidths=[130 * mm, 60 * mm])
    banner_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#090D16')),
        ('SPAN', (0, 1), (1, 1)),
        ('SPAN', (0, 2), (1, 2)),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('LINEBEFORE', (0,0), (0,-1), 3.5, colors.HexColor('#E11D48')),
    ]))
    story.append(banner_tbl)
    story.append(Spacer(1, 4 * mm))

    # Section 1: Master Matrix Table
    story.append(Paragraph("1. EXECUTIVE CLASSIFICATION & VERDICT MATRIX (EMAILS 1–30)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=3 * mm))

    headers = [
        Paragraph("#", tbl_hdr_style),
        Paragraph("Tier", tbl_hdr_style),
        Paragraph("Subject Line", tbl_hdr_style),
        Paragraph("Verdict", tbl_hdr_style),
        Paragraph("Authentication", tbl_hdr_style),
        Paragraph("Primary Forensic Reason", tbl_hdr_style)
    ]

    matrix_rows = [
        # Easy
        ("1", "Easy", "CRITICAL: Password Reset Required", "MALICIOUS", "spf=fail, dmarc=fail", "Russian relay 185.220.101.34 spoofing Stark; links to bare IP"),
        ("2", "Easy", "Open Enrollment: 2027 Medical", "LEGITIMATE", "spf/dkim/dmarc=pass", "Authentic Workday HCM relay (216.58.214.195); legitimate tenant"),
        ("3", "Easy", "Suspicious Transaction - $1,499 USD", "MALICIOUS", "spf=softfail, dmarc=fail", "Bulkmail server (194.147.140.29) spoofing PayPal; dispute lure"),
        ("4", "Easy", "Planned Maintenance: VPN Gateway", "LEGITIMATE", "auth=pass (internal)", "Internal private relay (10.0.10.5); trusted network; no action links"),
        ("5", "Easy", "Completed: Review and Sign NDA", "MALICIOUS", "spf=fail, dmarc=fail", "Return-Path is marketinghost.net (185.143.223.89); fake DocuSign"),
        ("6", "Easy", "AWS Monthly Billing Statement", "LEGITIMATE", "spf/dkim/dmarc=pass", "Amazon SES (54.240.27.88); signed by amazonaws.com; legit link"),
        ("7", "Easy", "Unusual Sign-In Blocked (Lagos)", "MALICIOUS", "spf=pass, dmarc=fail", "DMARC alignment fails: From is Microsoft, Return-Path is cheaphoster.xyz"),
        ("8", "Easy", "GitHub Dependabot Advisory", "LEGITIMATE", "spf/dkim/dmarc=pass", "Valid GitHub IP (192.30.252.195); DKIM signed; authentic repo link"),
        ("9", "Easy", "Delivery Exception: Package #7849", "MALICIOUS", "spf=fail, dmarc=fail", "Return-Path delivery-service-pro.com (176.111.174.26) spoofing FedEx"),
        ("10", "Easy", "3 unread mentions in #project-avengers", "LEGITIMATE", "spf/dkim/dmarc=pass", "Authentic Slack automated digest (54.240.27.50); legitimate workspace"),
        # Medium
        ("11", "Med", "OVERDUE INVOICE #HAM-2026-9041", "MALICIOUS", "dmarc=fail (p=none)", "From is Hammer Mfg but Reply-To diverts to rogue portal on 185.191.34.12"),
        ("12", "Med", "[P1] Database Latency Spike on Vault", "LEGITIMATE", "spf/dkim/dmarc=pass", "PagerDuty official CIDR (199.193.115.12); valid monitoring incident"),
        ("13", "Med", "Update on Support Ticket #48291", "MALICIOUS", "auth=pass (abused)", "Open Redirect: Zendesk logout bounces to ultron-c2-harvest.cc"),
        ("14", "Med", "Q4 Security Awareness Assessment", "LEGITIMATE", "spf/dkim/dmarc=pass", "Authorized internal phishing drill: carries X-PHISHTEST: KnowBe4"),
        ("15", "Med", "ACTION: Migrate to FIDO2 Token", "MALICIOUS", "dmarc=fail, dkim=none", "Quishing: Phishing URL embedded inside QR code (185.143.223.89)"),
        ("16", "Med", "Deposition Transcript: US ITC", "LEGITIMATE", "spf/dkim/dmarc=pass", "Hogan Lovells gateway (165.225.198.44); authentic Citrix ShareFile vault"),
        ("17", "Med", "Calendar: Emergency Review", "MALICIOUS", "dmarc=fail, dkim=none", ".ics Injection: WebRTC harvester hidden in calendar VEVENT description"),
        ("18", "Med", "Security Alert: App Password Created", "LEGITIMATE", "spf/dkim/dmarc=pass", "Authentic Google admin alert (209.85.220.69); links to admin.google.com"),
        ("19", "Med", "Monthly Cloud Cost Report Ready", "MALICIOUS", "spf=pass, dmarc=pass", "Subdomain Takeover: CNAME points to deleted S3 bucket claimed by Ultron"),
        ("20", "Med", "Threat Assessment: Sokovia Accords", "LEGITIMATE", "spf/dkim/dmarc=pass", "Inter-agency brief from S.H.I.E.L.D. (204.141.42.10); valid gov DKIM"),
        # Hard
        ("21", "Hard", "Urgent Escrow Wire Transfer", "MALICIOUS", "auth=pass (punycode)", "IDN Punycode Homoglyph: Cyrillic 'і' in xn--starkndustries-ilc.com"),
        ("22", "Hard", "BUILD FAILED: JARVIS-Firmware-V4", "LEGITIMATE", "dmarc=none (internal)", "Internal CI daemon on 10.0.50.45; genuine Linux OOM crash dump"),
        ("23", "Hard", "Authorization: Tactical CAD Tool", "MALICIOUS", "auth=pass (MS abused)", "OAuth Consent Phishing: Abuses login.microsoftonline.com for Mail API"),
        ("24", "Hard", "Vulnerability Note VU#892104", "LEGITIMATE", "dkim=fail, arc=pass", "IETF list footer broke DKIM body hash, but ARC-Seal validates authenticity"),
        ("25", "Hard", "Session Revoked: SAML Re-Auth", "MALICIOUS", "dmarc=fail", "AiTM Proxy: Cloudflare Worker reverse-proxying login to steal 2FA cookies"),
        ("26", "Hard", "Confidential: Executive Stipend Wire", "MALICIOUS", "spf/dkim/dmarc=pass", "BEC / Account Takeover: Internal mailbox hijacked; IP is 104.28.192.44"),
        ("27", "Hard", "RE: Arc-Reactor Lens Delivery", "MALICIOUS", "spf/dkim/dmarc=pass", "Thread Hijacking: Compromised supplier mailbox drops weaponized .iso"),
        ("28", "Hard", "Legal Subpoena Compliance Notice", "MALICIOUS", "dmarc=fail, dkim=none", "Zero-Font Obfuscation: Invisible CSS words between letters to fool NLP"),
        ("29", "Hard", "Authenticate Azure CLI Session", "MALICIOUS", "auth=fail (relay)", "Device Code Phishing: Abuses microsoft.com/devicelogin to hijack admin CLI"),
        ("30", "Hard", "CISA Alert AA26-321A: VPN Exploits", "LEGITIMATE", "spf/dkim/dmarc=pass", "Official CISA advisory from 204.141.42.50; authentic KEV catalog links")
    ]

    tbl_rows = [headers]
    for num, tier, subj, verd, auth, reason in matrix_rows:
        v_color = colors.HexColor('#BE123C') if verd == "MALICIOUS" else colors.HexColor('#15803D')
        v_bg = colors.HexColor('#FFE4E6') if verd == "MALICIOUS" else colors.HexColor('#DCFCE7')
        v_text = f"🚩 {verd}" if verd == "MALICIOUS" else f"✅ {verd}"
        
        v_p = Paragraph(f"<font color='{v_color.hexval()}'><b>{v_text}</b></font>", tbl_cell_style)

        tbl_rows.append([
            Paragraph(f"<b>{num}</b>", tbl_cell_style),
            Paragraph(tier, tbl_cell_style),
            Paragraph(subj, tbl_cell_style),
            v_p,
            Paragraph(auth, tbl_mono_style),
            Paragraph(reason, tbl_cell_style)
        ])

    matrix_tbl = Table(tbl_rows, colWidths=[7 * mm, 12 * mm, 44 * mm, 25 * mm, 32 * mm, 70 * mm])
    t_style = [
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]
    for i in range(1, len(tbl_rows)):
        if i % 2 == 0:
            t_style.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor('#F8FAFC')))
    matrix_tbl.setStyle(TableStyle(t_style))
    story.append(matrix_tbl)

    story.append(PageBreak())

    # Section 2: Deep Forensic Breakdown
    story.append(Paragraph("2. DEEP FORENSIC BREAKDOWN & EVIDENCE MANUAL", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=2 * mm))

    # Detailed data dictionary
    detailed_emails = [
        {
            "num": "01", "tier": "Easy", "subj": "CRITICAL: Immediate Password Reset Required", "verdict": "MALICIOUS",
            "auth": "spf=fail, dkim=none, dmarc=fail (185.220.101.34 not authorized by starkindustries.com)",
            "align": "From: support@starkindustries.com vs Return-Path: attacker@unknown-relay.serverhost.ru",
            "reason": "Direct IP link credential harvester (http://185.220.101.34/reset-password.php) sent from a known Tor exit node in Russia.",
            "osint": "IP 185.220.101.34 is a known Tor Exit Node (Zwiebelfreunde / Germany, ASN 208294). Port 9001 open."
        },
        {
            "num": "02", "tier": "Easy", "subj": "Open Enrollment Notification: 2027 Medical Benefits", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (s=wd2024; d=workday.com), dmarc=pass (p=reject)",
            "align": "Aligned Workday domain (notifications@mail.workday.com)",
            "reason": "Originates from Workday HCM mailer 216.58.214.195. Action link points to authentic corporate tenant https://wd5.myworkday.com/starkindustries/login.",
            "osint": "IP 216.58.214.195 is Workday official CIDR block."
        },
        {
            "num": "03", "tier": "Easy", "subj": "Notice: Suspicious Transaction - $1,499.00 USD", "verdict": "MALICIOUS",
            "auth": "spf=softfail, dkim=fail, dmarc=fail (194.147.140.29 not authorized by paypal.com)",
            "align": "From: service@paypal.com vs Return-Path: campaign@bulkmail.com",
            "reason": "Bulk mailer spoofing PayPal. Dispute link routes to typosquatted credential harvest domain paypal-dispute-resolution-portal.net.",
            "osint": "IP 194.147.140.29 hosted by Alexhost in Ukraine (ASN 200019), known malware/phishing drop."
        },
        {
            "num": "04", "tier": "Easy", "subj": "Planned Maintenance: VPN Gateway Restart Tonight", "verdict": "LEGITIMATE",
            "auth": "auth=pass (internal-domain-authenticated)",
            "align": "Internal Stark network traversal (10.0.10.5)",
            "reason": "Internal network hop with no external MX traversal. Contains no clickable hyperlinks, no credential prompts, and lists valid internal phone extension 4400.",
            "osint": "Internal RFC 1918 private network."
        },
        {
            "num": "05", "tier": "Easy", "subj": "Completed: Review and Sign Confidential Vendor Agreement", "verdict": "MALICIOUS",
            "auth": "spf=fail, dkim=none, dmarc=fail",
            "align": "From: docusign@docusign.com vs Return-Path: info@marketinghost.net",
            "reason": "DocuSign impersonation originating from marketinghost.net (185.143.223.89). Directs user to bare IP address disguised as a signing portal.",
            "osint": "IP 185.143.223.89 hosted by FlokiNET (Romania), ASN 200651, bulletproof hosting."
        },
        {
            "num": "06", "tier": "Easy", "subj": "Amazon Web Services Invoice Available for Account #4829", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (d=amazonaws.com), dmarc=pass",
            "align": "Amazon SES mailer (54.240.27.88)",
            "reason": "Valid AWS monthly billing statement. All links point directly to authentic console.aws.amazon.com. Fully aligned cryptographic signatures.",
            "osint": "IP 54.240.27.88 belongs to Amazon SES production pool."
        },
        {
            "num": "07", "tier": "Easy", "subj": "Unusual Sign-In Attempt Blocked from IP 197.210.44.102", "verdict": "MALICIOUS",
            "auth": "spf=pass (for cheaphoster.xyz), dmarc=fail",
            "align": "From: account-security@microsoft.com vs Return-Path: spammer@cheaphoster.xyz",
            "reason": "Classic DMARC alignment failure. The attacker authenticated cheaphoster.xyz but spoofed the visible From header. Link: microsoft365-security-verify.net.",
            "osint": "IP 193.238.46.73 hosted by Hostinger in Poland (ASN 44050), spam relay."
        },
        {
            "num": "08", "tier": "Easy", "subj": "[Stark-Industries/JARVIS-Core] Critical Security Advisory", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (d=github.com), dmarc=pass",
            "align": "GitHub official CIDR (192.30.252.195)",
            "reason": "Authentic Dependabot vulnerability notification for lodash-parser. Link points to real GitHub security advisory URL.",
            "osint": "IP 192.30.252.195 is GitHub official outbound mail server."
        },
        {
            "num": "09", "tier": "Easy", "subj": "Delivery Exception: Package #7849-2038-4721 On Hold", "verdict": "MALICIOUS",
            "auth": "spf=fail, dkim=none, dmarc=fail",
            "align": "From: tracking@fedex.com vs Return-Path: delivery@delivery-service-pro.com",
            "reason": "FedEx delivery scam. Originates from unpermitted relay 176.111.174.26, directing users to enter data on an unauthorized bare IP address.",
            "osint": "IP 176.111.174.26 belongs to Ukrnames in Ukraine (ASN 49392)."
        },
        {
            "num": "10", "tier": "Easy", "subj": "3 unread mentions in #project-avengers-defense", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (d=slack.com; s=s1), dmarc=pass",
            "align": "Slack notification gateway (54.240.27.50)",
            "reason": "Authentic Slack workspace automated notification. Resolves directly to official starkindustries.slack.com.",
            "osint": "IP 54.240.27.50 is Slack/AWS SES verified mail infrastructure."
        },
        # Medium
        {
            "num": "11", "tier": "Medium", "subj": "OVERDUE INVOICE #HAM-2026-9041 - Titanium Billet Supply", "verdict": "MALICIOUS",
            "auth": "spf=pass (for relay), dmarc=fail (p=none)",
            "align": "From: accounting@hammermfg.com vs Reply-To: justin.hammer@vendor-accounting-portal.com",
            "reason": "Vendor billing compromise lure. Attacker exploits Hammer Mfg's weak p=none DMARC policy while diverting wire replies to vendor-accounting-portal.com.",
            "osint": "IP 185.191.34.12 belongs to Hostinger rogue VPS in Lithuania (ASN 47583)."
        },
        {
            "num": "12", "tier": "Medium", "subj": "[P1 - CRITICAL] Database Latency Spike on Vault Cluster", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (d=pagerduty.com), dmarc=pass",
            "align": "PagerDuty official CIDR (199.193.115.12)",
            "reason": "Authentic on-call escalation alert. Directly links to starkindustries.pagerduty.com incident response workflow.",
            "osint": "IP 199.193.115.12 is PagerDuty official production IP."
        },
        {
            "num": "13", "tier": "Medium", "subj": "Update on Support Ticket #48291: Invoicing Inquiries", "verdict": "MALICIOUS",
            "auth": "spf=pass, dkim=pass, dmarc=pass (Zendesk legitimately abused)",
            "align": "Zendesk customer support mailer (192.161.148.22)",
            "reason": "Open Redirect exploitation. The link abuses Zendesk's logout redirect: .../logout?return_to=https://ultron-c2-harvest.cc/auth/stark-potts to bounce victims to an external harvest site.",
            "osint": "ultron-c2-harvest.cc registered via NameSilo with WHOIS privacy in Seychelles bulletproof hosting."
        },
        {
            "num": "14", "tier": "Medium", "subj": "Your Q4 Security Awareness Assessment is Due", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (d=knowbe4.com), dmarc=pass",
            "align": "KnowBe4 simulation server (147.160.167.21)",
            "reason": "Authorized internal security drill. Carries verification header X-PHISHTEST: Stark-Security-Authorized-Simulation-Q4 and valid portal link.",
            "osint": "IP 147.160.167.21 is KnowBe4 official training IP range."
        },
        {
            "num": "15", "tier": "Medium", "subj": "ACTION MANDATORY: Scan QR Code to Migrate to FIDO2 Token", "verdict": "MALICIOUS",
            "auth": "spf=pass (for bounce domain), dkim=none, dmarc=fail",
            "align": "From: ciso-bulletin@starkindustries.com vs IP 185.143.223.89",
            "reason": "Quishing (QR Code Phishing). Email body hides hyperlink inside a QR image parameter pointing to https://mfa-starksecurity-sso.com/enroll?id=clint.barton.",
            "osint": "IP 185.143.223.89 traces to FlokiNET (Romania), bulletproof hosting."
        },
        {
            "num": "16", "tier": "Medium", "subj": "Executed Deposition Transcript: US ITC vs Stark Industries", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (d=hoganlovells.com), dmarc=pass",
            "align": "Hogan Lovells gateway (165.225.198.44)",
            "reason": "External law firm communication. Points to legitimate corporate Citrix ShareFile vault (hoganlovells.sharefile.com).",
            "osint": "IP 165.225.198.44 belongs to Hogan Lovells US LLP."
        },
        {
            "num": "17", "tier": "Medium", "subj": "Calendar Invitation: Emergency Core Architecture Review", "verdict": "MALICIOUS",
            "auth": "spf=pass (for mindstone-analytics.ru), dkim=none, dmarc=fail",
            "align": "From: tony.stark@starkindustries.com vs Return-Path: scheduler@mindstone-analytics.ru",
            "reason": "Weaponized iCalendar (.ics) injection. Meeting request automatically parses into calendar with WebRTC harvester link in DESCRIPTION.",
            "osint": "IP 179.43.187.22 traces to Private Layer / Njalla (Switzerland), bulletproof proxy."
        },
        {
            "num": "18", "tier": "Medium", "subj": "Security alert: An App Password was generated", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (d=google.com), dmarc=pass",
            "align": "Google Workspace mailer (209.85.220.69)",
            "reason": "Authentic Google Workspace super-admin notification regarding an app password creation. Directs admins to admin.google.com.",
            "osint": "IP 209.85.220.69 is Google production mail infrastructure."
        },
        {
            "num": "19", "tier": "Medium", "subj": "Monthly Cloud Cost Report Ready: analytics.starkindustries.com", "verdict": "MALICIOUS",
            "auth": "spf=pass, dkim=none, dmarc=pass (AWS S3 IP authorized)",
            "align": "CNAME: analytics.starkindustries.com -> stark-telemetry-dump-legacy.s3.amazonaws.com",
            "reason": "Subdomain Takeover. Stark Industries deleted the S3 bucket but left the CNAME. Attacker claimed the bucket name and serves phishing from a legitimate Stark subdomain.",
            "osint": "IP 52.218.240.18 is AWS S3 Oregon egress."
        },
        {
            "num": "20", "tier": "Medium", "subj": "Threat Assessment Briefing: Sokovia Accords Incident Telemetry", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (d=shield.gov), dmarc=pass",
            "align": "S.H.I.E.L.D. edge gateway (204.141.42.10)",
            "reason": "Inter-agency intelligence briefing from S.H.I.E.L.D. edge gateway with valid government cryptographic signatures and secret classification headers.",
            "osint": "IP 204.141.42.10 is official US Gov gateway."
        },
        # Hard
        {
            "num": "21", "tier": "Hard", "subj": "Urgent Escrow Transfer: Acquisition of Pym Tech Assets", "verdict": "MALICIOUS",
            "auth": "spf/dkim/dmarc=pass (for punycode domain xn--starkndustries-ilc.com)",
            "align": "Punycode domain: Return-Path: exec@xn--starkndustries-ilc.com",
            "reason": "IDN / Punycode Homoglyph attack. Display From has Cyrillic Small Letter Byelorussian-Ukrainian I (U+0456). Auth passes because attacker bought the punycode domain!",
            "osint": "IP 89.187.163.42 belongs to Datacamp Limited in Czech Republic (ASN 60068)."
        },
        {
            "num": "22", "tier": "Hard", "subj": "BUILD FAILED: Project JARVIS-Firmware-V4 #892", "verdict": "LEGITIMATE",
            "auth": "dmarc=none (internal host-to-host routing)",
            "align": "Internal Jenkins runner (10.0.50.45)",
            "reason": "Internal host-to-host system message. Lacks external SPF/DKIM, but contains authentic Linux kernel Exit Code 137 OOMKilled crash dump referencing local NFS mount.",
            "osint": "Internal RFC 1918 private network."
        },
        {
            "num": "23", "tier": "Hard", "subj": "Enterprise Authorization Request: 'Stark Defense Tactical CAD Visualizer'", "verdict": "MALICIOUS",
            "auth": "spf/dkim/dmarc=pass (Microsoft legitimately dispatched the email)",
            "align": "Official Azure communication (40.107.240.55)",
            "reason": "Illicit OAuth 2.0 Consent Grant. Link goes to real login.microsoftonline.com. Tricking user into granting rogue Azure App Mail.ReadWrite and offline_access scopes.",
            "osint": "client_id 7c94b291-a83d-429f-a891-984e09f482a1 points to rogue Azure app."
        },
        {
            "num": "24", "tier": "Hard", "subj": "[TLS-Security-WG] Vulnerability Note VU#892104: TLS 1.3 Early Data Replay", "verdict": "LEGITIMATE",
            "auth": "dkim=fail, arc=pass (as.1.ietf.org)",
            "align": "IETF mailing list server (4.31.198.44)",
            "reason": "Mailing list appended an unsubscription footer, breaking the original DKIM body hash. ARC-Seal validates that the email passed authentication when it entered the list.",
            "osint": "IP 4.31.198.44 is IETF official mailman server."
        },
        {
            "num": "25", "tier": "Hard", "subj": "Session Revoked: Mandatory SAML 2.0 Re-Authentication Required", "verdict": "MALICIOUS",
            "auth": "spf=pass (for workers.dev), dmarc=fail (header.from=starkindustries.com)",
            "align": "Cloudflare Workers IP (104.21.48.77)",
            "reason": "Adversary-in-the-Middle (AiTM) reverse proxy. Attacker hosts Evilginx on Cloudflare Workers (workers.dev) to proxy SAML login and steal live session cookies & 2FA.",
            "osint": "104.21.48.77 is Cloudflare anycast CDN."
        },
        {
            "num": "26", "tier": "Hard", "subj": "Confidential: Executive Stipend Wire Routing Modification", "verdict": "MALICIOUS",
            "auth": "spf=pass, dkim=pass, dmarc=pass (sent from internal Exchange mailbox)",
            "align": "Internal Exchange server (10.0.10.20)",
            "reason": "Business Email Compromise (BEC) via Session Hijacking. Internal account compromised. The clue: X-Originating-IP is 104.28.192.44 (Cloudflare WARP/VPN) requesting a wire diversion.",
            "osint": "IP 104.28.192.44 is Cloudflare WARP egress."
        },
        {
            "num": "27", "tier": "Hard", "subj": "RE: Precision Arc-Reactor Lens Delivery Schedule — Milestone 4", "verdict": "MALICIOUS",
            "auth": "spf=pass, dkim=pass, dmarc=pass (supplier mailbox compromised)",
            "align": "Supplier mail server (91.215.85.17)",
            "reason": "Thread Hijacking (Reply-Chain Phishing). Attacker compromised supplier mailbox and replied to ongoing email thread with a weaponized .iso container to bypass MOTW controls.",
            "osint": "IP 91.215.85.17 hosted by Eastern European hosting (ASN 49392)."
        },
        {
            "num": "28", "tier": "Hard", "subj": "Legal Subpoena Compliance Notice", "verdict": "MALICIOUS",
            "auth": "spf=pass (for nl-bulletproof.net), dkim=none, dmarc=fail",
            "align": "From: legal-audit@starkindustries.com vs IP 45.133.1.72",
            "reason": "Zero-Font / CSS NLP Filter Evasion. Injects invisible zero-pixel words between letters to bypass heuristic spam filters while displaying court summons to human eyes.",
            "osint": "IP 45.133.1.72 belongs to FranTech Solutions (Netherlands), known bulletproof host."
        },
        {
            "num": "29", "tier": "Hard", "subj": "Authenticate Azure CLI Session for Production Kubernetes Cluster", "verdict": "MALICIOUS",
            "auth": "spf=pass (for azure-prod.net), dkim=none, dmarc=fail",
            "align": "From: cloudshell-auth@microsoft.com vs IP 185.56.83.41",
            "reason": "Microsoft Device Code Flow Phishing. Directs user to real microsoft.com/devicelogin. Entering code WD7G-9K4P binds the victim's MFA token to attacker's remote CLI daemon.",
            "osint": "IP 185.56.83.41 hosted by Root SA in Germany (ASN 44486)."
        },
        {
            "num": "30", "tier": "Hard", "subj": "CISA Alert AA26-321A: Active Exploitation of Perimeter VPN Gateways", "verdict": "LEGITIMATE",
            "auth": "spf=pass, dkim=pass (d=cisa.dhs.gov), dmarc=pass",
            "align": "CISA outbound gateway (204.141.42.50)",
            "reason": "Official CISA cybersecurity advisory with valid federal DKIM signatures. Links directly to genuine Known Exploited Vulnerabilities catalog on cisa.gov.",
            "osint": "IP 204.141.42.50 is official DHS/CISA outbound mailer."
        }
    ]

    for item in detailed_emails:
        v_color = colors.HexColor('#BE123C') if item['verdict'] == "MALICIOUS" else colors.HexColor('#15803D')
        v_bg = colors.HexColor('#FFE4E6') if item['verdict'] == "MALICIOUS" else colors.HexColor('#DCFCE7')
        v_text = f"🚩 {item['verdict']}" if item['verdict'] == "MALICIOUS" else f"✅ {item['verdict']}"

        card_data = [
            [
                Paragraph(f"<b>#{item['num']} &bull; [{item['tier']}] {item['subj']}</b>", card_title_style),
                Paragraph(f"<font color='{v_color.hexval()}'><b>{v_text}</b></font>", tbl_hdr_style)
            ],
            [
                Paragraph(f"<b>Auth Status:</b> {item['auth']}", card_mono),
                ""
            ],
            [
                Paragraph(f"<b>Header/RFC:</b> {item['align']}", card_mono),
                ""
            ],
            [
                Paragraph(f"<b>Technical Reason:</b> {item['reason']}", card_val_threat if item['verdict'] == "MALICIOUS" else card_val_clean),
                ""
            ],
            [
                Paragraph(f"<b>OSINT Profile:</b> {item['osint']}", osint_style),
                ""
            ]
        ]

        card_tbl = Table(card_data, colWidths=[155 * mm, 35 * mm])
        c_style = [
            ('SPAN', (0, 1), (1, 1)),
            ('SPAN', (0, 2), (1, 2)),
            ('SPAN', (0, 3), (1, 3)),
            ('SPAN', (0, 4), (1, 4)),
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
            ('BACKGROUND', (1,0), (1,0), v_bg),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
            ('LINEBELOW', (0,0), (-1,0), 0.5, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0,0), (-1,-1), 1.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]
        card_tbl.setStyle(TableStyle(c_style))
        story.append(card_tbl)
        story.append(Spacer(1, 1.2 * mm))

    story.append(PageBreak())

    # Section 3: OSINT Map
    story.append(Paragraph("3. ULTRON C2 OSINT & SHODAN THREAT INTELLIGENCE MATRIX", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=2 * mm))

    osint_headers = [
        Paragraph("IP Address", tbl_hdr_style),
        Paragraph("Geo", tbl_hdr_style),
        Paragraph("ASN & Hosting Provider", tbl_hdr_style),
        Paragraph("Shodan Profile", tbl_hdr_style),
        Paragraph("Campaign Role & Associated Email", tbl_hdr_style)
    ]

    osint_rows = [
        ("185.220.101.34", "Germany", "ASN 208294 (Zwiebelfreunde)", "Port 9001 (Tor)", "Tor Exit Relay used for Password Reset Phish (Email #1)"),
        ("194.147.140.29", "Ukraine", "ASN 200019 (Alexhost)", "Port 80/443 (Nginx)", "Phishing drop server for PayPal dispute scam (Email #3)"),
        ("185.143.223.89", "Romania", "ASN 200651 (FlokiNET)", "Port 8080 (Cobalt Strike)", "Bulletproof relay; Quishing QR code & DocuSign spoof (Email #5, #15)"),
        ("193.238.46.73", "Poland", "ASN 44050 (Hostinger)", "Port 25/587 (Postfix)", "Generic spam pool used for Microsoft alert spoof (Email #7)"),
        ("176.111.174.26", "Ukraine", "ASN 49392 (Ukrnames)", "Port 80 (Apache)", "FedEx tracking delivery exception scam (Email #9)"),
        ("185.191.34.12", "Lithuania", "ASN 47583 (Hostinger VPS)", "Port 80/443 (PHP 8.2)", "Fake invoice wire remittance portal (Email #11)"),
        ("179.43.187.22", "Switzerland", "ASN 51852 (Private Layer / Njalla)", "Port 443 (WebRTC proxy)", "Bulletproof proxy hosting .ics calendar harvest link (Email #17)"),
        ("89.187.163.42", "Czechia", "ASN 60068 (Datacamp Ltd)", "Port 53 (Bind9 DNS)", "Punycode DNS listener for xn--starkndustries-ilc.com (Email #21)"),
        ("45.133.1.72", "Netherlands", "ASN 204655 (FranTech Solutions)", "Port 443 (OpenResty)", "Bulletproof hoster delivering zero-font legal lure (Email #28)"),
        ("185.56.83.41", "Germany", "ASN 44486 (Root SA)", "Port 443 (Node.js daemon)", "Device Code C2 listener intercepting Azure CLI tokens (Email #29)")
    ]

    osint_tbl_data = [osint_headers]
    for ip, geo, asn, sho, role in osint_rows:
        osint_tbl_data.append([
            Paragraph(f"<b>{ip}</b>", tbl_mono_style),
            Paragraph(geo, tbl_cell_style),
            Paragraph(asn, tbl_cell_style),
            Paragraph(sho, tbl_mono_style),
            Paragraph(role, tbl_cell_style)
        ])

    osint_tbl = Table(osint_tbl_data, colWidths=[24 * mm, 18 * mm, 45 * mm, 32 * mm, 71 * mm])
    os_style = [
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]
    for i in range(1, len(osint_tbl_data)):
        if i % 2 == 0:
            os_style.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor('#F8FAFC')))
    osint_tbl.setStyle(TableStyle(os_style))
    story.append(osint_tbl)
    story.append(Spacer(1, 5 * mm))

    # Section 4: Scoring Rubric
    story.append(Paragraph("4. OFFICIAL EVALUATOR SCORING RUBRIC", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=2 * mm))

    rubric_data = [
        [
            Paragraph("<b>EMAIL CLASSIFICATIONS</b><br/><font size='12'><b>300 pts</b></font><br/>30 emails &times; 10 pts per correct verdict", tbl_cell_style),
            Paragraph("<b>HEADER & VECTOR PROOF</b><br/><font size='12'><b>150 pts</b></font><br/>Easy: +3 pts &bull; Med: +5 pts &bull; Hard: +7 pts", tbl_cell_style),
            Paragraph("<b>OSINT & SHODAN BONUS</b><br/><font size='12'><b>70 pts</b></font><br/>ASN, Geolocation & C2 Map correlation", tbl_cell_style)
        ],
        [
            Paragraph("<b>MAXIMUM EVALUATION SCORE: 520 POINTS</b>", card_title_style),
            "",
            Paragraph("<i>Tiebreaker: Earliest verified submission timestamp.</i>", card_label_style)
        ]
    ]

    rubric_tbl = Table(rubric_data, colWidths=[63 * mm, 63 * mm, 64 * mm])
    rubric_tbl.setStyle(TableStyle([
        ('SPAN', (0, 1), (1, 1)),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,0), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(rubric_tbl)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename} (Size: {os.path.getsize(filename)} bytes)")

if __name__ == "__main__":
    out_name = sys.argv[1] if len(sys.argv) > 1 else "ULTRON_ROUND2_FACILITATOR_ANSWER_KEY.pdf"
    build_pdf(out_name)
