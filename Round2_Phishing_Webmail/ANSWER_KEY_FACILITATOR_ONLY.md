# 🔑 ROUND 2 — BALANCED ANSWER KEY & TECHNICAL EVALUATION GUIDE

## ⚠️ FACILITATOR ONLY — DO NOT DISTRIBUTE TO PARTICIPANTS
### Target Track: MCA / Cybersecurity & Ethical Hacking

---

## 🎯 Quick Classification Table

| # | Tier | Verdict | Primary Technical Indicator | Authentication Summary |
|---|---|---|---|---|
| **1** | Easy | 🚩 MALICIOUS | IP not authorized by Stark Industries SPF; DMARC fails | `spf=fail`, `dkim=none`, `dmarc=fail` |
| **2** | Easy | ✅ LEGITIMATE | Official Workday HCM portal; aligned SPF & DKIM | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **3** | Easy | 🚩 MALICIOUS | PayPal spoofed from untrusted bulkmail server | `spf=softfail`, `dkim=fail`, `dmarc=fail` |
| **4** | Easy | ✅ LEGITIMATE | Internal Stark network relay (10.0.10.5); trusted domain | `auth=pass` (internal relay) |
| **5** | Easy | 🚩 MALICIOUS | DocuSign spoofed from untrusted marketing host | `spf=fail`, `dkim=none`, `dmarc=fail` |
| **6** | Easy | ✅ LEGITIMATE | Amazon Web Services SES billing alert; aligned DKIM | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **7** | Easy | 🚩 MALICIOUS | Return-Path is `cheaphoster.xyz`; DMARC alignment fails | `spf=pass` (for spammer), `dmarc=fail` |
| **8** | Easy | ✅ LEGITIMATE | Authentic GitHub Dependabot advisory; GitHub DKIM valid | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **9** | Easy | 🚩 MALICIOUS | FedEx spoofed from unpermitted IP; DMARC fails | `spf=fail`, `dkim=none`, `dmarc=fail` |
| **10**| Easy | ✅ LEGITIMATE | Authentic Slack workspace notification; Slack DKIM valid | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **11**| Medium | 🚩 MALICIOUS | Overdue invoice wire fraud; Reply-To mismatch; DMARC `p=none` | `spf=pass` (relay), `dmarc=fail` (`p=none`) |
| **12**| Medium | ✅ LEGITIMATE | PagerDuty critical incident trigger; official CIDR | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **13**| Medium | 🚩 MALICIOUS | Open Redirect on Zendesk logout (`return_to=`) trampolining to C2 | SPF/DKIM pass (Zendesk abused) |
| **14**| Medium | ✅ LEGITIMATE | Authorized internal phishing drill (`X-PHISHTEST: KnowBe4`) | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **15**| Medium | 🚩 MALICIOUS | Quishing (QR code hiding credential harvester URI) | `dmarc=fail`, `dkim=none` |
| **16**| Medium | ✅ LEGITIMATE | External law firm deposition transcripts via Citrix ShareFile | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **17**| Medium | 🚩 MALICIOUS | Malicious `.ics` calendar invite embedding WebRTC harvester | `dmarc=fail`, `dkim=none` |
| **18**| Medium | ✅ LEGITIMATE | Google Workspace Admin security notice for App Password creation | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **19**| Medium | 🚩 MALICIOUS | Subdomain Takeover: CNAME points to deleted/claimed AWS S3 bucket | `spf=pass` (AWS IP), `dmarc=pass` (`p=none`) |
| **20**| Medium | ✅ LEGITIMATE | S.H.I.E.L.D. inter-agency briefing from official `shield.gov` gateway | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **21**| Hard | 🚩 MALICIOUS | IDN Punycode homoglyph: Cyrillic 'і' in `starkіndustries.com` | `dmarc=pass` (for punycode domain!) |
| **22**| Hard | ✅ LEGITIMATE | Linux Jenkins CI build crash on internal subnet (`10.0.50.45`) | `dmarc=none` (Internal network routing) |
| **23**| Hard | 🚩 MALICIOUS | Illicit OAuth 2.0 Consent Grant targeting `login.microsoftonline.com` | Legitimate Microsoft domain abused |
| **24**| Hard | ✅ LEGITIMATE | IETF mailing list alert: DKIM body hash broken by footer, ARC passes | `dkim=fail`, `arc=pass` |
| **25**| Hard | 🚩 MALICIOUS | Adversary-in-the-Middle (AiTM) reverse proxy on `workers.dev` | `dmarc=fail`, `spf=pass` (Cloudflare) |
| **26**| Hard | 🚩 MALICIOUS | BEC / Session Hijack: Internal mailbox hijacked to divert stipend | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **27**| Hard | 🚩 MALICIOUS | Thread Hijacking: Compromised supplier mailbox drops weaponized `.iso` | `spf=pass`, `dkim=pass`, `dmarc=pass` |
| **28**| Hard | 🚩 MALICIOUS | Zero-Font HTML CSS insertion to evade spam keyword heuristics | `dmarc=fail`, `dkim=none` |
| **29**| Hard | 🚩 MALICIOUS | Microsoft Device Code Phishing (`microsoft.com/devicelogin`) | Official Microsoft domain abused |
| **30**| Hard | ✅ LEGITIMATE | Official CISA Cybersecurity Advisory AA26-321A | `spf=pass`, `dkim=pass`, `dmarc=pass` |

---

# ═══════════════════════════════════════
# DETAILED SECTION-BY-SECTION ANALYSIS
# ═══════════════════════════════════════

---

## 🟢 SECTION A — EASY (Textbook Header Analysis)

In this section, any student who looks at the **`Authentication-Results`** and **`Return-Path`** can easily tell the legitimate from the malicious:

* **Email #1 (🚩 Malicious):** 
  * Header shows: `spf=fail (sender IP 185.220.101.34 is not authorized by starkindustries.com)`.
  * Return-Path is from `unknown-relay.serverhost.ru`.
  * Obvious credential phishing link to a bare IP address (`185.220.101.34`).
* **Email #2 (✅ Legitimate):** 
  * Header shows: `spf=pass`, `dkim=pass`, `dmarc=pass`.
  * Valid Workday IP (`216.58.214.195`) and genuine tenant link (`wd5.myworkday.com`).
* **Email #3 (🚩 Malicious):** 
  * Header shows: `spf=softfail`, `dkim=fail`, `dmarc=fail`.
  * From says `paypal.com` but sent from `194.147.140.29` (`bulkmail.com`).
* **Email #4 (✅ Legitimate):** 
  * Internal relay `10.0.10.5` sending internal maintenance notice.
  * No links, standard internal extension (`4400`).
* **Email #5 (🚩 Malicious):** 
  * Header shows: `spf=fail`, `dkim=none`, `dmarc=fail`.
  * From says `docusign.com`, but Return-Path is `marketinghost.net`.
* **Email #6 (✅ Legitimate):** 
  * Header shows: `spf=pass`, `dkim=pass`, `dmarc=pass`.
  * Legitimate Amazon SES relay (`54.240.27.88`) with valid AWS console link.
* **Email #7 (🚩 Malicious):** 
  * Classic DMARC alignment failure: SPF passes for `cheaphoster.xyz`, but From is `microsoft.com` (`dmarc=fail`).
* **Email #8 (✅ Legitimate):** 
  * Header shows: `spf=pass`, `dkim=pass`, `dmarc=pass` from GitHub's mailer (`192.30.252.195`).
* **Email #9 (🚩 Malicious):** 
  * Header shows: `spf=fail`, `dmarc=fail`. Return-Path is `delivery-service-pro.com` while From is `fedex.com`.
* **Email #10 (✅ Legitimate):** 
  * Header shows: `spf=pass`, `dkim=pass`, `dmarc=pass` from Slack's official mailer.

---

## 🟡 SECTION B — MEDIUM (SOC L1/L2 & OSINT Lookups)

Here, students must inspect headers deeper, detect manipulation techniques, and use OSINT tools (WHOIS, AbuseIPDB, Shodan) on external IPs:

* **Email #11 (🚩 Malicious — Vendor Invoice Fraud):**
  * **Technique:** Compromised billing lure. From is `accounting@hammermfg.com`, but `Reply-To:` is `justin.hammer@vendor-accounting-portal.com`.
  * **OSINT on IP `185.191.34.12`:** WHOIS reveals hosting in Lithuania/Cyprus (ASN 47583 / Hostinger rogue VPS).
* **Email #12 (✅ Legitimate — PagerDuty Incident):**
  * All authentication passes (`199.193.115.12` is PagerDuty's official IP block).
* **Email #13 (🚩 Malicious — Open Redirect):**
  * **The Trap:** SPF and DKIM **PASS** because Zendesk's legitimate server sent the message!
  * **The Exploit:** Open Redirect vulnerability in Zendesk logout URL:
    `https://support.zendesk.com/access/logout?return_to=https%3A%2F%2Fultron-c2-harvest.cc%2Fauth%2Fstark-potts`
  * The parameter `return_to=` redirects the victim to Ultron's harvest domain `ultron-c2-harvest.cc`.
* **Email #14 (✅ Legitimate — Authorized Phishing Drill):**
  * Sent by KnowBe4 (`147.160.167.21`).
  * Identified by SOC bypass header: `X-PHISHTEST: Stark-Security-Authorized-Simulation-Q4`.
* **Email #15 (🚩 Malicious — Quishing / QR Phishing):**
  * **Technique:** Quishing. Body has no plain hyperlink; the phishing link is embedded in an image QR code.
  * Decoded QR parameter: `https://mfa-starksecurity-sso.com/enroll?id=clint.barton`.
  * **OSINT on IP `185.143.223.89`:** Traces to FlokiNET (Romania), a known privacy/bulletproof hoster.
* **Email #16 (✅ Legitimate — Legal Vault):**
  * Aligned SPF/DKIM/DMARC from Hogan Lovells (`165.225.198.44`) to legitimate Citrix ShareFile vault.
* **Email #17 (🚩 Malicious — Calendar `.ics` Injection):**
  * Weaponized iCalendar invite. The link is hidden in the `DESCRIPTION:` field (`stark-webrtc-bridge.ru`).
  * **OSINT on IP `179.43.187.22`:** Traces to Private Layer / Njalla in Switzerland (bulletproof host).
* **Email #18 (✅ Legitimate — Google Workspace Security Alert):**
  * Authentic Google alert (`209.85.220.69`). Informs admin of App Password generation.
* **Email #19 (🚩 Malicious — Subdomain Takeover):**
  * **Technique:** Subdomain Takeover / Dangling CNAME.
  * Stark Industries created a CNAME: `analytics.starkindustries.com -> stark-telemetry-dump-legacy.s3.amazonaws.com`.
  * When the old S3 bucket was deleted, the CNAME remained. Ultron registered the bucket in AWS and now hosts a malicious page on Stark Industries' legitimate subdomain!
* **Email #20 (✅ Legitimate — S.H.I.E.L.D. Briefing):**
  * Originates from official federal gateway `204.141.42.10` with valid government DKIM.

---

## 🔴 SECTION C — HARD (SOC L3 / Ethical Hacker Tier)

Advanced evasion, identity protocols, and deep forensics:

* **Email #21 (🚩 Malicious — IDN / Punycode Homoglyph):**
  * Display address: `pepper.potts@starkіndustries.com`.
  * The letter **'і'** is **Cyrillic Small Letter Byelorussian-Ukrainian I (`U+0456`)**.
  * Encoded Punycode: `xn--starkndustries-ilc.com`.
  * Because Ultron bought this punycode domain, **SPF, DKIM, and DMARC all PASS**! Students must spot the punycode string in the headers.
  * **OSINT on IP `89.187.163.42`:** Datacamp Limited (Czech Republic).
* **Email #22 (✅ Legitimate — Internal CI Build Crash):**
  * Host-to-host Linux system message (`10.0.50.45`). Lacks external SPF/DKIM (`dmarc=none`), but has authentic kernel OOM error logs on local NFS mount.
* **Email #23 (🚩 Malicious — Illicit OAuth 2.0 Consent Grant):**
  * The link points to official Microsoft identity infrastructure: `https://login.microsoftonline.com/common/oauth2/v2.0/authorize`.
  * Does NOT steal passwords. It tricks the user into granting permissions (`Mail.ReadWrite`, `Files.ReadWrite.All`, `offline_access`) to a malicious Azure App registered by Ultron (`client_id=7c94b291-...`).
* **Email #24 (✅ Legitimate — Mailing List with Broken DKIM + ARC):**
  * `dkim=fail` because the IETF mailing list added an unsubscription footer to the email body (breaking the original body hash).
  * `arc=pass` (Authenticated Received Chain) proves the email was authentic when it entered the mailing list server.
* **Email #25 (🚩 Malicious — Adversary-in-the-Middle / AiTM):**
  * Attacker hosts an Evilginx reverse proxy on Cloudflare Workers (`stark-sso.auth-gateway-proxy.workers.dev`).
  * Proxies legitimate SAML login, captures real-time 2FA session cookies.
* **Email #26 (🚩 Malicious — Business Email Compromise / Session Hijacking):**
  * SPF, DKIM, and DMARC all pass because it was sent from Tony Stark's internal Exchange mailbox!
  * **The Tell:** `X-Originating-IP: [104.28.192.44]` is an external Cloudflare WARP/VPN IP, and the text diverts payroll to an offshore Swiss IBAN without voice confirmation.
* **Email #27 (🚩 Malicious — Thread Hijacking / Reply-Chain Phishing):**
  * Attacker compromised supplier Carl Creel's email and replied to a real historic thread.
  * Delivers a `.iso` file (`ArcLens_Refraction_Telemetry_M4.iso`). Threat actors use ISO files because Windows automatically mounts them, bypassing Mark-of-the-Web (MOTW) security warnings.
* **Email #28 (🚩 Malicious — Zero-Font HTML CSS Obfuscation):**
  * Inserts zero-pixel, invisible text between letters (`P<span style="font-size:0px...">lorem ipsum</span>lease`).
  * Bypasses NLP and spam word filters while appearing normal to human eyes.
  * **OSINT on IP `45.133.1.72`:** Known bulletproof host (FranTech / Netherlands).
* **Email #29 (🚩 Malicious — Microsoft Device Code Flow Phishing):**
  * URL is legitimate: `https://microsoft.com/devicelogin`.
  * Ultron ran `az login --use-device-code` on his terminal and received code `WD7G-9K4P`.
  * If the victim enters this code on the Microsoft portal, their active session and MFA token are bound to Ultron's terminal.
* **Email #30 (✅ Legitimate — CISA KEV Advisory):**
  * Valid CISA notification from `204.141.42.50` with genuine links to the KEV catalog.

---

# ═══════════════════════════════════════
# ULTRON OSINT & SHODAN THREAT MAP
# ═══════════════════════════════════════

For teams performing OSINT lookups on external IPs:

| IP Address | Geolocation | ASN / Provider | Shodan / Threat Intel Profile |
|---|---|---|---|
| `185.220.101.34` | Germany | ASN 208294 (Zwiebelfreunde) | Tor Exit Relay, Port 9001 open |
| `194.147.140.29` | Ukraine | ASN 200019 (Alexhost) | Known phishing drop, Port 80/443 |
| `185.143.223.89` | Romania | ASN 200651 (FlokiNET) | Bulletproof hosting, Cobalt Strike team server |
| `193.238.46.73` | Poland | ASN 44050 (Hostinger) | Generic spam relay |
| `176.111.174.26` | Ukraine | ASN 49392 (Ukrnames) | FedEx scam landing page |
| `185.191.34.12` | Lithuania | ASN 47583 (Hostinger) | Phishing remittance portal |
| `179.43.187.22` | Switzerland | ASN 51852 (Private Layer / Njalla) | Bulletproof proxy, WebRTC phishing |
| `89.187.163.42` | Czechia | ASN 60068 (Datacamp Ltd) | Punycode DNS server (`xn--...`) |
| `45.133.1.72` | Netherlands | ASN 204655 (FranTech Solutions) | Bulletproof hoster, legal summons lure |
| `185.56.83.41` | Germany | ASN 44486 (Root SA) | Device Code C2 listener |

---

# ═══════════════════════════════════════
# SCORING RUBRIC (Max: 520 pts)
# ═══════════════════════════════════════

1. **Classification:** 10 pts per correct email (300 pts)
2. **Technical Explanation & Header Analysis:**
   - Section A (Easy): +3 pts each (30 pts)
   - Section B (Medium): +5 pts each (50 pts)
   - Section C (Hard): +7 pts each (70 pts)
3. **OSINT Lookups & Decoded Payloads:**
   - Identifying Open Redirect parameter (#13): +10 pts
   - Decoding QR code payload (#15): +10 pts
   - Identifying Subdomain Takeover (#19): +10 pts
   - Identifying Cyrillic Punycode (#21): +10 pts
   - Explaining Device Code hijacking (#29): +15 pts
   - Reconstructing Ultron's C2 network: +15 pts

*Facilitator Tip: Use time of submission as the tiebreaker!*
