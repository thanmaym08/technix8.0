# 🛡️ ROUND 2: THE SOCIAL ENGINEERING BREACH (BALANCED EDITION)

## Operation Ultron — Phishing & Threat Hunting Incident Response
### Level: MCA / Cybersecurity & Ethical Hacking Students

---

> **CONFIDENTIAL // S.H.I.E.L.D. CYBER OPERATIONS DIRECTIVE**
>
> **Situation Report:**  
> The SOC Mail Gateway at Stark Industries has intercepted **30 suspicious email transactions**. An adversarial actor codenamed **ULTRON** is probing our perimeter.
>
> **Your Mission:**
> 1. **Section A (Easy — Textbook Level):** Inspect the email authentication headers (`Authentication-Results:`, `SPF`, `DKIM`, `DMARC`, and `Return-Path`). Identify whether the email is **LEGITIMATE (✅)** or **MALICIOUS (🚩)** by analyzing the raw RFC 5322 message headers.
> 2. **Section B (Medium — SOC L1/L2 Level):** Dissect header anomalies, `Reply-To` traps, and public IP addresses in the `Received:` headers. Run the external IPs/domains through OSINT tools (WHOIS, AbuseIPDB, VirusTotal, Shodan).
> 3. **Section C (Hard — Ethical Hacker / SOC L3 Level):** Uncover advanced evasion tactics (Punycode, OAuth Consent Phishing, AiTM Proxies, Zero-Font Obfuscation, and BEC). Track Ultron's global C2 infrastructure.

---

## 🧭 Quick Header Primer (Cheat Sheet for Analysts)

* **SPF (Sender Policy Framework):** Verifies if the sending IP is authorized by the domain's DNS `TXT` record (`pass` vs `fail` / `softfail`).
* **DKIM (DomainKeys Identified Mail):** Uses a cryptographic digital signature to prove the email body and headers were not tampered with (`pass` vs `fail` / `none`).
* **DMARC (Domain-based Message Authentication):** Checks **Alignment** — does the domain in the `From:` header match the domain authenticated by SPF and/or DKIM? (`pass` vs `fail`).
* **Return-Path (RFC 5321):** The envelope sender where bounce notifications go.
* **From (RFC 5322):** The display address the recipient sees in their inbox.

---

# ═══════════════════════════════════════
# SECTION A — EASY (Textbook Level: Emails 1–10)
# ═══════════════════════════════════════

---

## 📧 EMAIL #1 `[External]`

```http
Delivered-To: tonystark@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp773337oia;
        Mon, 16 Nov 2026 09:14:18 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tOTk0ODI===
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr5424458ejc.42.1731748463120;
        Mon, 16 Nov 2026 09:14:18 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+MzE0MTU=...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMTg0OTI===
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=fail (mail-gateway01.perimeter.starkindustries.com: domain of unknown-relay.serverhost.ru designation for 185.220.101.34) smtp.mailfrom=attacker@unknown-relay.serverhost.ru;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
Return-Path: <attacker@unknown-relay.serverhost.ru>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 01FA3B2019-mbx
        for <tonystark@starkindustries.com>; Mon, 16 Nov 2026 09:14:18 +0000
Received: from unknown-relay.serverhost.ru (unknown-relay.serverhost.ru [185.220.101.34])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ01Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <tonystark@starkindustries.com>; Mon, 16 Nov 2026 09:14:18 +0000
Received-SPF: fail (mail-gateway01.perimeter.starkindustries.com: domain of starkindustries.com does not designate 185.220.101.34 as permitted sender) client-ip=185.220.101.34;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@starkindustries.com;
       spf=fail (mail-gateway01.perimeter.starkindustries.com: domain of unknown-relay.serverhost.ru designation for 185.220.101.34) smtp.mailfrom=attacker@unknown-relay.serverhost.ru;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
Message-ID: <20261116.019482019.135736@starkindustries.com>
Date: Mon, 16 Nov 2026 09:14:18 +0000
From: "Stark IT Helpdesk" <support@starkindustries.com>
To: tonystark@starkindustries.com
Subject: CRITICAL: Immediate Password Reset Required
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_01_3700691.19428786"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 1 (Highest)
X-Originating-IP: [185.220.101.34]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: CRITICAL: Immediate Password Reset Required
Thread-Index: AQHb019182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_01_3700691.19428786
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

STARK INDUSTRIES

Global Information Security Operations Center

SECURITY ALERT: Urgent Action Required

Dear Tony Stark,

Our perimeter intrusion detection systems identified repeated unauthorized login attempts against your corporate Active Directory account originating from an unrecognized remote host.

Target Account: tonystark@starkindustries.com

Originating IP: 185.220.101.34 (Unknown Relay Network)

Threat Flag: Multiple Failed Kerberos Pre-Auth Handshakes

In compliance with Cybersecurity Policy SEC-402, you must reset your single sign-on credentials within 60 minutes to prevent automatic directory suspension.

Reset Corporate Password

This is an automated security dispatch. Stark IT Support Services will never ask for your password via phone or chat.

------=_Part_01_3700691.19428786
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden; background: #ffffff;">
  <div style="background: #0b1f3a; padding: 20px 24px; color: #ffffff;">
    <div style="font-size: 18px; font-weight: bold; letter-spacing: 0.5px;">STARK INDUSTRIES</div>
    <div style="font-size: 12px; color: #8fa5c2; margin-top: 4px;">Global Information Security Operations Center</div>
  </div>
  <div style="padding: 24px;">
    <div style="background: #fff3cd; border-left: 4px solid #ffc107; padding: 12px 16px; margin-bottom: 20px;">
      <strong style="color: #856404; font-size: 14px;">SECURITY ALERT: Urgent Action Required</strong>
    </div>
    <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">Dear Tony Stark,</p>
    <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">Our perimeter intrusion detection systems identified repeated unauthorized login attempts against your corporate Active Directory account originating from an unrecognized remote host.</p>
    <div style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 6px; padding: 14px; margin-bottom: 20px; font-size: 13px; color: #495057;">
      <div><strong>Target Account:</strong> tonystark@starkindustries.com</div>
      <div style="margin-top: 6px;"><strong>Originating IP:</strong> 185.220.101.34 (Unknown Relay Network)</div>
      <div style="margin-top: 6px;"><strong>Threat Flag:</strong> Multiple Failed Kerberos Pre-Auth Handshakes</div>
    </div>
    <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 20px 0;">In compliance with Cybersecurity Policy SEC-402, you must reset your single sign-on credentials within <strong>60 minutes</strong> to prevent automatic directory suspension.</p>
    <div style="text-align: center; margin: 28px 0;">
      <a href="http://185.220.101.34/reset-password.php" style="background: #1a73e8; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">Reset Corporate Password</a>
    </div>
    <p style="color: #777777; font-size: 12px; line-height: 1.4; margin: 20px 0 0 0; border-top: 1px solid #eeeeee; padding-top: 16px;">This is an automated security dispatch. Stark IT Support Services will never ask for your password via phone or chat.</p>
  </div>
</div>

------=_Part_01_3700691.19428786--
```

---

## 📧 EMAIL #2

```http
Delivered-To: pepper.potts@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp795508oia;
        Mon, 16 Nov 2026 09:30:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTk4OTY0==
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr7319035ejc.42.1731748463120;
        Mon, 16 Nov 2026 09:30:00 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NjI4MzA=...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMzY5ODQ===
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of mail.workday.com designation for 216.58.214.195) smtp.mailfrom=notifications@mail.workday.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=workday.com
Return-Path: <notifications@mail.workday.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 02FA3B2019-mbx
        for <pepper.potts@starkindustries.com>; Mon, 16 Nov 2026 09:30:00 +0000
Received: from mail-relay04.workday.com (mail-relay04.workday.com [216.58.214.195])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ02Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <pepper.potts@starkindustries.com>; Mon, 16 Nov 2026 09:30:00 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of mail.workday.com designates 216.58.214.195 as permitted sender) client-ip=216.58.214.195;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@workday.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of mail.workday.com designation for 216.58.214.195) smtp.mailfrom=notifications@mail.workday.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=workday.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=workday.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTU0Mzg0=;
        b=MTk5MDY0NTk=
          MjE1ODA4OA====
Message-ID: <20261116.029482019.682025@workday.com>
Date: Mon, 16 Nov 2026 09:30:00 +0000
From: "Workday Enterprise Portal" <notifications@workday.com>
To: pepper.potts@starkindustries.com
Subject: Open Enrollment Notification: 2027 Medical Benefits
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_02_6631680.59446259"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [216.58.214.195]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: Open Enrollment Notification: 2027 Medical Benefits
Thread-Index: AQHb029182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_02_6631680.59446259
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

workday.

Stark Industries HR

Annual Open Enrollment is Now Open

Hello Pepper Potts,

Your 2027 Annual Benefits Open Enrollment window is open from today through December 4, 2026. This is your opportunity to review and elect your healthcare, dental, vision, life insurance, and flexible spending accounts for the upcoming plan year.

Current Active Elections:

Executive Comprehensive Medical PPO (BlueShield)

Delta Dental Premier Tier 1

VSP Enhanced Vision Coverage

Access Workday Portal

Workday, Inc. | 6110 Stoneridge Mall Road, Pleasanton, CA 94588
Confidential automated notification sent to Stark Industries Human Resources subscribers.

------=_Part_02_6631680.59446259
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #d9d9d9; border-radius: 8px; overflow: hidden; background: #ffffff;">
  <div style="background: #084682; padding: 18px 24px; display: flex; align-items: center; justify-content: space-between;">
    <div style="font-size: 20px; font-weight: 700; color: #ffffff; letter-spacing: -0.5px;">workday.</div>
    <div style="font-size: 13px; color: #c4d7ed;">Stark Industries HR</div>
  </div>
  <div style="padding: 24px 28px;">
    <h2 style="font-size: 18px; color: #212121; margin: 0 0 14px 0;">Annual Open Enrollment is Now Open</h2>
    <p style="color: #424242; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">Hello Pepper Potts,</p>
    <p style="color: #424242; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">Your 2027 Annual Benefits Open Enrollment window is open from today through December 4, 2026. This is your opportunity to review and elect your healthcare, dental, vision, life insurance, and flexible spending accounts for the upcoming plan year.</p>
    <div style="background: #f0f4f9; border-radius: 6px; padding: 16px; margin: 20px 0;">
      <div style="font-size: 13px; font-weight: 600; color: #084682; margin-bottom: 8px;">Current Active Elections:</div>
      <ul style="margin: 0; padding-left: 20px; font-size: 13px; color: #333333; line-height: 1.6;">
        <li>Executive Comprehensive Medical PPO (BlueShield)</li>
        <li>Delta Dental Premier Tier 1</li>
        <li>VSP Enhanced Vision Coverage</li>
      </ul>
    </div>
    <div style="text-align: center; margin: 26px 0;">
      <a href="https://wd5.myworkday.com/starkindustries/login" style="background: #005cb9; color: #ffffff; text-decoration: none; padding: 12px 24px; border-radius: 4px; font-weight: 600; font-size: 14px; display: inline-block;">Access Workday Portal</a>
    </div>
    <p style="color: #757575; font-size: 12px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #eeeeee; padding-top: 14px;">Workday, Inc. | 6110 Stoneridge Mall Road, Pleasanton, CA 94588<br>Confidential automated notification sent to Stark Industries Human Resources subscribers.</p>
  </div>
</div>

------=_Part_02_6631680.59446259--
```

---

## 📧 EMAIL #3 `[External]`

```http
Delivered-To: bruce.banner@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp737804oia;
        Mon, 16 Nov 2026 09:50:35 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjk4NDQ2==
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr3663618ejc.42.1731748463120;
        Mon, 16 Nov 2026 09:50:35 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+OTQyNDU=...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNTU0NzY===
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=fail;
       spf=softfail (mail-gateway01.perimeter.starkindustries.com: domain of bulkmail.com designation for 194.147.140.29) smtp.mailfrom=campaign@bulkmail.com;
       dmarc=fail (p=reject sp=reject dis=none) header.from=paypal.com
Return-Path: <campaign@bulkmail.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 03FA3B2019-mbx
        for <bruce.banner@starkindustries.com>; Mon, 16 Nov 2026 09:50:35 +0000
Received: from outbound.bulkmail.com (outbound.bulkmail.com [194.147.140.29])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ03Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <bruce.banner@starkindustries.com>; Mon, 16 Nov 2026 09:50:35 +0000
Received-SPF: softfail (mail-gateway01.perimeter.starkindustries.com: transitioning domain of bulkmail.com discourages use of 194.147.140.29 as permitted sender) client-ip=194.147.140.29;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=fail header.i=@paypal.com;
       spf=softfail (mail-gateway01.perimeter.starkindustries.com: domain of bulkmail.com designation for 194.147.140.29) smtp.mailfrom=campaign@bulkmail.com;
       dmarc=fail (p=reject sp=reject dis=none) header.from=paypal.com
Message-ID: <20261116.039482019.523012@paypal.com>
Date: Mon, 16 Nov 2026 09:50:35 +0000
From: "PayPal Account Security" <service@paypal.com>
To: bruce.banner@starkindustries.com
Subject: Notice: Suspicious Transaction - $1,499.00 USD
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_03_9528080.68939384"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [194.147.140.29]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Notice: Suspicious Transaction - $1,499.00 USD
Thread-Index: AQHb039182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_03_9528080.68939384
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

PayPal

Did you authorize this transaction?

A payment of $1,499.00 USD was recently initiated from your PayPal account. If this was not authorized by you, please dispute and reverse the transaction immediately.

Merchant:Ultron Cybernetics Ltd

Amount:$1,499.00 USD

Date:November 16, 2026

Transaction ID:PP-994820-819A

Dispute & Cancel Payment

PayPal Customer Protection Center | 2211 North First Street, San Jose, CA 95131.
Help & Contact | Security Center | Terms of Service

------=_Part_03_9528080.68939384
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e5e5e5; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="padding: 24px 30px; border-bottom: 1px solid #f0f0f0;">
    <div style="font-size: 26px; font-weight: 900; color: #003087; font-style: italic;">PayPal</div>
  </div>
  <div style="padding: 28px 30px;">
    <div style="font-size: 20px; font-weight: 600; color: #2c2e2f; margin-bottom: 16px;">Did you authorize this transaction?</div>
    <p style="color: #6c7378; font-size: 14px; line-height: 1.5; margin: 0 0 20px 0;">A payment of <strong>$1,499.00 USD</strong> was recently initiated from your PayPal account. If this was not authorized by you, please dispute and reverse the transaction immediately.</p>
    <div style="border: 1px solid #e1e7eb; border-radius: 6px; padding: 18px; margin-bottom: 24px; background: #fafbfc;">
      <table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #2c2e2f;">
        <tr><td style="padding: 6px 0; color: #6c7378;">Merchant:</td><td style="padding: 6px 0; font-weight: 600; text-align: right;">Ultron Cybernetics Ltd</td></tr>
        <tr><td style="padding: 6px 0; color: #6c7378;">Amount:</td><td style="padding: 6px 0; font-weight: 600; text-align: right; color: #d9381e;">$1,499.00 USD</td></tr>
        <tr><td style="padding: 6px 0; color: #6c7378;">Date:</td><td style="padding: 6px 0; text-align: right;">November 16, 2026</td></tr>
        <tr><td style="padding: 6px 0; color: #6c7378;">Transaction ID:</td><td style="padding: 6px 0; text-align: right; font-family: monospace;">PP-994820-819A</td></tr>
      </table>
    </div>
    <div style="text-align: center; margin: 26px 0;">
      <a href="http://paypal-dispute-resolution-portal.net/cancel?id=banner992" style="background: #0070ba; color: #ffffff; text-decoration: none; padding: 14px 32px; border-radius: 24px; font-weight: 700; font-size: 14px; display: inline-block;">Dispute &amp; Cancel Payment</a>
    </div>
    <p style="color: #8c8c8c; font-size: 12px; line-height: 1.5; margin: 24px 0 0 0; border-top: 1px solid #f0f0f0; padding-top: 16px;">PayPal Customer Protection Center | 2211 North First Street, San Jose, CA 95131.<br>Help &amp; Contact | Security Center | Terms of Service</p>
  </div>
</div>

------=_Part_03_9528080.68939384--
```

---

## 📧 EMAIL #4

```http
Delivered-To: all-staff@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp753049oia;
        Mon, 16 Nov 2026 10:14:50 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMzk3OTI4==
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr4383870ejc.42.1731748463120;
        Mon, 16 Nov 2026 10:14:50 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+MTI1NjYw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNzM5Njg===
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=none (mail-gateway01.perimeter.starkindustries.com: domain of starkindustries.com designation for 10.0.10.5) smtp.mailfrom=it-announcements@starkindustries.com;
       dmarc=none (p=reject sp=reject dis=none) header.from=starkindustries.com
Return-Path: <it-announcements@starkindustries.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 04FA3B2019-mbx
        for <all-staff@starkindustries.com>; Mon, 16 Nov 2026 10:14:50 +0000
Received: from internal-relay02.corp.starkindustries.com ([10.0.10.5])
        by mail-mbx01.starkindustries.com (Postfix) with ESMTP id 04INT910284
        for <all-staff@starkindustries.com>; Mon, 16 Nov 2026 10:14:50 +0000
Received-SPF: none (mail-gateway01.perimeter.starkindustries.com: internal/unlisted sender 10.0.10.5 does not designate permitted sender hosts) client-ip=10.0.10.5;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@starkindustries.com;
       spf=none (mail-gateway01.perimeter.starkindustries.com: domain of starkindustries.com designation for 10.0.10.5) smtp.mailfrom=it-announcements@starkindustries.com;
       dmarc=none (p=reject sp=reject dis=none) header.from=starkindustries.com
Message-ID: <20261116.049482019.455670@starkindustries.com>
Date: Mon, 16 Nov 2026 10:14:50 +0000
From: "Stark IT Infrastructure" <it-announcements@starkindustries.com>
To: all-staff@starkindustries.com
Subject: Planned Maintenance: VPN Gateway Restart Tonight (23:00 - 01:00 UTC)
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_04_5303875.21946344"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [10.0.10.5]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: Planned Maintenance: VPN Gateway Restart Tonight (23:00 - 01:00 UTC)
Thread-Index: AQHb049182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Internal

This is a multi-part message in MIME format.

------=_Part_04_5303875.21946344
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

STARK INDUSTRIES — IT INFRASTRUCTURE BULLETIN

Change Advisory Board (CAB) Notice: CAB-2026-8819

Engineering & Research Staff,

Please be advised that the corporate remote-access VPN gateway (vpn.starkindustries.com) will undergo scheduled operating system maintenance and redundant cluster failover testing tonight.

Maintenance Window: Tonight, 23:00 - 01:00 UTC

Target Systems: AnyConnect VPN Concentrators (US-East Cluster)

User Impact: Active VPN tunnels may drop momentarily (< 60s) during gateway node handoff.

No employee configuration changes or action are required. Internal Zero-Trust connections via Cloudflare Access will remain unaffected.

Network Operations Center (NOC) | Internal Ext: 7712 | Slack: #it-infrastructure

------=_Part_04_5303875.21946344
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 6px; background: #ffffff; padding: 24px;">
  <div style="border-bottom: 2px solid #0052cc; padding-bottom: 12px; margin-bottom: 18px;">
    <div style="font-size: 16px; font-weight: bold; color: #172b4d;">STARK INDUSTRIES — IT INFRASTRUCTURE BULLETIN</div>
    <div style="font-size: 12px; color: #6b778c; margin-top: 2px;">Change Advisory Board (CAB) Notice: CAB-2026-8819</div>
  </div>
  <p style="color: #172b4d; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">Engineering &amp; Research Staff,</p>
  <p style="color: #172b4d; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">Please be advised that the corporate remote-access VPN gateway (<code>vpn.starkindustries.com</code>) will undergo scheduled operating system maintenance and redundant cluster failover testing tonight.</p>
  <div style="background: #f4f5f7; border-radius: 4px; padding: 14px; margin-bottom: 18px; font-size: 13px; color: #172b4d;">
    <div><strong>Maintenance Window:</strong> Tonight, 23:00 - 01:00 UTC</div>
    <div style="margin-top: 6px;"><strong>Target Systems:</strong> AnyConnect VPN Concentrators (US-East Cluster)</div>
    <div style="margin-top: 6px;"><strong>User Impact:</strong> Active VPN tunnels may drop momentarily (&lt; 60s) during gateway node handoff.</div>
  </div>
  <p style="color: #172b4d; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">No employee configuration changes or action are required. Internal Zero-Trust connections via Cloudflare Access will remain unaffected.</p>
  <div style="margin-top: 20px; font-size: 13px; color: #6b778c; border-top: 1px solid #ebecf0; padding-top: 14px;">
    Network Operations Center (NOC) | Internal Ext: 7712 | Slack: #it-infrastructure
  </div>
</div>

------=_Part_04_5303875.21946344--
```

---

## 📧 EMAIL #5 `[External]`

```http
Delivered-To: natasha.romanoff@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp633024oia;
        Mon, 16 Nov 2026 10:45:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tNDk3NDEw==
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr6806127ejc.42.1731748463120;
        Mon, 16 Nov 2026 10:45:00 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+MTU3MDc1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzOTI0NjA===
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=fail (mail-gateway01.perimeter.starkindustries.com: domain of marketinghost.net designation for 185.143.223.89) smtp.mailfrom=info@marketinghost.net;
       dmarc=fail (p=reject sp=reject dis=none) header.from=docusign.com
Return-Path: <info@marketinghost.net>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 05FA3B2019-mbx
        for <natasha.romanoff@starkindustries.com>; Mon, 16 Nov 2026 10:45:00 +0000
Received: from delivery.marketinghost.net (delivery.marketinghost.net [185.143.223.89])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ05Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <natasha.romanoff@starkindustries.com>; Mon, 16 Nov 2026 10:45:00 +0000
Received-SPF: fail (mail-gateway01.perimeter.starkindustries.com: domain of docusign.com does not designate 185.143.223.89 as permitted sender) client-ip=185.143.223.89;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@docusign.com;
       spf=fail (mail-gateway01.perimeter.starkindustries.com: domain of marketinghost.net designation for 185.143.223.89) smtp.mailfrom=info@marketinghost.net;
       dmarc=fail (p=reject sp=reject dis=none) header.from=docusign.com
Message-ID: <20261116.059482019.506688@docusign.com>
Date: Mon, 16 Nov 2026 10:45:00 +0000
From: "DocuSign Digital Signatures" <docusign@docusign.com>
To: natasha.romanoff@starkindustries.com
Subject: Completed: Review and Sign Confidential Vendor Agreement
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_05_1455877.96696803"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [185.143.223.89]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Completed: Review and Sign Confidential Vendor Agreement
Thread-Index: AQHb059182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_05_1455877.96696803
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

DocuSign

NF

Nick Fury (Director, S.H.I.E.L.D.)

sent you a document to review and sign

Project_Avengers_Q4_NDASigned.pdf

4 pages | Standard Electronic Signature Required

REVIEW DOCUMENT

Please review and complete the signing procedure at your earliest convenience to authorize procurement of classified materials.

DocuSign, Inc. | 221 Main Street, Suite 1550, San Francisco, CA 94105
Do not share this email. The link provides secure access to your document.

------=_Part_05_1455877.96696803
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e9e9e9; border-radius: 4px; background: #ffffff; overflow: hidden;">
  <div style="background: #27455c; padding: 18px 24px;">
    <div style="font-size: 20px; font-weight: bold; color: #ffffff;">DocuSign</div>
  </div>
  <div style="padding: 24px 28px;">
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
      <div style="width: 44px; height: 44px; border-radius: 50%; background: #1a73e8; color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 18px; margin-right: 14px;">NF</div>
      <div>
        <div style="font-size: 15px; font-weight: 700; color: #1e1e1e;">Nick Fury (Director, S.H.I.E.L.D.)</div>
        <div style="font-size: 13px; color: #666666;">sent you a document to review and sign</div>
      </div>
    </div>
    <div style="border: 1px solid #dcdcdc; border-radius: 4px; padding: 18px; background: #fdfdfd; margin-bottom: 24px;">
      <div style="font-size: 14px; font-weight: bold; color: #222222;">Project_Avengers_Q4_NDASigned.pdf</div>
      <div style="font-size: 12px; color: #777777; margin-top: 4px;">4 pages | Standard Electronic Signature Required</div>
    </div>
    <div style="text-align: center; margin: 28px 0;">
      <a href="http://185.143.223.89/docusign/sign.html?doc=99281" style="background: #ffc820; color: #222222; text-decoration: none; padding: 14px 34px; border-radius: 2px; font-weight: bold; font-size: 14px; display: inline-block;">REVIEW DOCUMENT</a>
    </div>
    <p style="color: #666666; font-size: 13px; line-height: 1.5; margin: 20px 0 0 0;">Please review and complete the signing procedure at your earliest convenience to authorize procurement of classified materials.</p>
    <p style="color: #999999; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #eeeeee; padding-top: 14px;">DocuSign, Inc. | 221 Main Street, Suite 1550, San Francisco, CA 94105<br>Do not share this email. The link provides secure access to your document.</p>
  </div>
</div>

------=_Part_05_1455877.96696803--
```

---

## 📧 EMAIL #6

```http
Delivered-To: steve.rogers@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp490784oia;
        Mon, 16 Nov 2026 11:10:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tNTk2ODky==
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr9913052ejc.42.1731748463120;
        Mon, 16 Nov 2026 11:10:00 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+MTg4NDkw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMTEwOTUy==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of amazonses.com designation for 54.240.27.88) smtp.mailfrom=0100018bd3a104f2-amazonses.com@amazonses.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=amazonaws.com
Return-Path: <0100018bd3a104f2-amazonses.com@amazonses.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 06FA3B2019-mbx
        for <steve.rogers@starkindustries.com>; Mon, 16 Nov 2026 11:10:00 +0000
Received: from a27-88.smtp-out.amazonses.com (a27-88.smtp-out.amazonses.com [54.240.27.88])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ06Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <steve.rogers@starkindustries.com>; Mon, 16 Nov 2026 11:10:00 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of amazonses.com designates 54.240.27.88 as permitted sender) client-ip=54.240.27.88;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@amazonaws.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of amazonses.com designation for 54.240.27.88) smtp.mailfrom=0100018bd3a104f2-amazonses.com@amazonses.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=amazonaws.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=amazonaws.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=NDYzMTUy=;
        b=NTk2OTkzMzE=
          NjI3NjAxNg====
Message-ID: <20261116.069482019.372879@amazonaws.com>
Date: Mon, 16 Nov 2026 11:10:00 +0000
From: "Amazon Web Services Billing" <no-reply-aws@amazonaws.com>
To: steve.rogers@starkindustries.com
Subject: Amazon Web Services Invoice Available for Account #4829-1037-5561
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_06_4081793.20292528"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [54.240.27.88]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: Amazon Web Services Invoice Available for Account #4829-1037-5561
Thread-Index: AQHb069182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_06_4081793.20292528
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Amazon Web Services

Your AWS Monthly Invoice is Available

Greetings Amazon Web Services Customer,

Your billing statement for the billing period October 1 - October 31, 2026 is now available for AWS Account #4829-1037-5561.

Total Amount Due:

$14,820.45 USD

Amazon Elastic Compute Cloud (EC2)$8,410.20

Amazon Relational Database Service (RDS)$3,470.10

Amazon Simple Storage Service (S3)$2,940.15

View Invoice in AWS Console

Amazon Web Services, Inc., 410 Terry Avenue North, Seattle, WA 98109-5210
This email was sent from a notification-only address that cannot accept incoming email.

------=_Part_06_4081793.20292528
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #eaeded; border-radius: 8px; background: #ffffff; overflow: hidden;">
  <div style="background: #232f3e; padding: 18px 24px;">
    <div style="font-size: 18px; font-weight: bold; color: #ff9900; letter-spacing: 0.5px;">Amazon Web Services</div>
  </div>
  <div style="padding: 24px 28px;">
    <h2 style="font-size: 18px; color: #16191f; margin: 0 0 14px 0;">Your AWS Monthly Invoice is Available</h2>
    <p style="color: #545b64; font-size: 14px; line-height: 1.5; margin: 0 0 18px 0;">Greetings Amazon Web Services Customer,</p>
    <p style="color: #545b64; font-size: 14px; line-height: 1.5; margin: 0 0 18px 0;">Your billing statement for the billing period <strong>October 1 - October 31, 2026</strong> is now available for AWS Account <strong>#4829-1037-5561</strong>.</p>
    <div style="background: #f2f3f3; border-radius: 6px; padding: 18px; margin-bottom: 22px;">
      <div style="font-size: 13px; color: #545b64;">Total Amount Due:</div>
      <div style="font-size: 24px; font-weight: bold; color: #16191f; margin: 4px 0 12px 0;">$14,820.45 USD</div>
      <table style="width: 100%; border-collapse: collapse; font-size: 13px; color: #545b64; border-top: 1px solid #d5dbdb; padding-top: 10px;">
        <tr><td style="padding: 6px 0;">Amazon Elastic Compute Cloud (EC2)</td><td style="padding: 6px 0; text-align: right; font-weight: 600;">$8,410.20</td></tr>
        <tr><td style="padding: 6px 0;">Amazon Relational Database Service (RDS)</td><td style="padding: 6px 0; text-align: right; font-weight: 600;">$3,470.10</td></tr>
        <tr><td style="padding: 6px 0;">Amazon Simple Storage Service (S3)</td><td style="padding: 6px 0; text-align: right; font-weight: 600;">$2,940.15</td></tr>
      </table>
    </div>
    <div style="text-align: center; margin: 26px 0;">
      <a href="https://console.aws.amazon.com/billing/home#/bills?invoiceId=4829-1037-5561" style="background: #ec7211; color: #ffffff; text-decoration: none; padding: 12px 26px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">View Invoice in AWS Console</a>
    </div>
    <p style="color: #879596; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #eaeded; padding-top: 14px;">Amazon Web Services, Inc., 410 Terry Avenue North, Seattle, WA 98109-5210<br>This email was sent from a notification-only address that cannot accept incoming email.</p>
  </div>
</div>

------=_Part_06_4081793.20292528--
```

---

## 📧 EMAIL #7 `[External]`

```http
Delivered-To: clint.barton@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp977892oia;
        Mon, 16 Nov 2026 11:35:10 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tNjk2Mzc0==
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr9961035ejc.42.1731748463120;
        Mon, 16 Nov 2026 11:35:10 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+MjE5OTA1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMTI5NDQ0==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of cheaphoster.xyz designation for 197.210.44.102) smtp.mailfrom=spammer@cheaphoster.xyz;
       dmarc=fail (p=reject sp=reject dis=none) header.from=microsoft.com
Return-Path: <spammer@cheaphoster.xyz>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 07FA3B2019-mbx
        for <clint.barton@starkindustries.com>; Mon, 16 Nov 2026 11:35:10 +0000
Received: from vps-node891.cheaphoster.xyz (vps-node891.cheaphoster.xyz [197.210.44.102])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ07Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <clint.barton@starkindustries.com>; Mon, 16 Nov 2026 11:35:10 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of cheaphoster.xyz designates 197.210.44.102 as permitted sender) client-ip=197.210.44.102;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@microsoft.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of cheaphoster.xyz designation for 197.210.44.102) smtp.mailfrom=spammer@cheaphoster.xyz;
       dmarc=fail (p=reject sp=reject dis=none) header.from=microsoft.com
Message-ID: <20261116.079482019.318862@microsoft.com>
Date: Mon, 16 Nov 2026 11:35:10 +0000
From: "Microsoft 365 Security Alert" <account-security@microsoft.com>
To: clint.barton@starkindustries.com
Subject: Unusual Sign-In Attempt Blocked from IP 197.210.44.102
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_07_2589242.54097522"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [197.210.44.102]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Unusual Sign-In Attempt Blocked from IP 197.210.44.102
Thread-Index: AQHb079182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_07_2589242.54097522
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Microsoft

Unusual sign-in activity

We detected something unusual about a recent sign-in to the Microsoft 365 account tonystark@starkindustries.com.

Country/region: Lagos, Nigeria

IP address: 197.210.44.102

Date: Mon, 16 Nov 2026 8:12 AM (UTC)

Platform: Linux / Chrome Browser

If this wasn't you, an attacker may have your password. Please review your recent activity and we'll help you secure your credentials.

Review recent activity

Microsoft Corporation, One Microsoft Way, Redmond, WA 98052
Privacy Statement | Security Response

------=_Part_07_2589242.54097522
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e1dfdd; border-radius: 4px; background: #ffffff; overflow: hidden;">
  <div style="padding: 24px 30px; border-bottom: 1px solid #edebe9;">
    <div style="display: flex; align-items: center;">
      <span style="font-size: 20px; font-weight: 600; color: #0078d4;">Microsoft</span>
    </div>
  </div>
  <div style="padding: 28px 30px;">
    <div style="font-size: 20px; font-weight: 600; color: #201f1e; margin-bottom: 16px;">Unusual sign-in activity</div>
    <p style="color: #605e5c; font-size: 14px; line-height: 1.5; margin: 0 0 18px 0;">We detected something unusual about a recent sign-in to the Microsoft 365 account <strong>tonystark@starkindustries.com</strong>.</p>
    <div style="background: #f3f2f1; border-radius: 4px; padding: 16px; margin-bottom: 22px; font-size: 13px; color: #323130;">
      <div style="padding: 4px 0;"><strong>Country/region:</strong> Lagos, Nigeria</div>
      <div style="padding: 4px 0;"><strong>IP address:</strong> 197.210.44.102</div>
      <div style="padding: 4px 0;"><strong>Date:</strong> Mon, 16 Nov 2026 8:12 AM (UTC)</div>
      <div style="padding: 4px 0;"><strong>Platform:</strong> Linux / Chrome Browser</div>
    </div>
    <p style="color: #605e5c; font-size: 14px; line-height: 1.5; margin: 0 0 22px 0;">If this wasn't you, an attacker may have your password. Please review your recent activity and we'll help you secure your credentials.</p>
    <div style="text-align: center; margin: 26px 0;">
      <a href="http://m365-session-recovery.cheaphoster.xyz/login.aspx?user=tonystark" style="background: #0078d4; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 2px; font-weight: 600; font-size: 14px; display: inline-block;">Review recent activity</a>
    </div>
    <p style="color: #a19f9d; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #edebe9; padding-top: 14px;">Microsoft Corporation, One Microsoft Way, Redmond, WA 98052<br>Privacy Statement | Security Response</p>
  </div>
</div>

------=_Part_07_2589242.54097522--
```

---

## 📧 EMAIL #8

```http
Delivered-To: jarvis-dev@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp876437oia;
        Mon, 16 Nov 2026 12:00:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tNzk1ODU2==
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr3902083ejc.42.1731748463120;
        Mon, 16 Nov 2026 12:00:00 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+MjUxMzIw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMTQ3OTM2==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of github.com designation for 192.30.252.195) smtp.mailfrom=noreply@github.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=github.com
Return-Path: <noreply@github.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 08FA3B2019-mbx
        for <jarvis-dev@starkindustries.com>; Mon, 16 Nov 2026 12:00:00 +0000
Received: from smtp.github.com (smtp.github.com [192.30.252.195])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ08Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <jarvis-dev@starkindustries.com>; Mon, 16 Nov 2026 12:00:00 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of github.com designates 192.30.252.195 as permitted sender) client-ip=192.30.252.195;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@github.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of github.com designation for 192.30.252.195) smtp.mailfrom=noreply@github.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=github.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=github.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=NjE3NTM2=;
        b=Nzk1OTU3Njc=
          ODMzNDk4MA====
Message-ID: <20261116.089482019.391344@github.com>
Date: Mon, 16 Nov 2026 12:00:00 +0000
From: "GitHub Dependabot" <notifications@github.com>
To: jarvis-dev@starkindustries.com
Subject: [Stark-Industries/JARVIS-Core] Critical Security Advisory CVE-2026-4827
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_08_4205063.68743199"
X-Mailer: GitHub-Mailer
X-Priority: 3 (Normal)
X-Originating-IP: [192.30.252.195]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: [Stark-Industries/JARVIS-Core] Critical Security Advisory CVE-2026-4827
Thread-Index: AQHb089182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_08_4205063.68743199
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

GitHub

Dependabot alert

Stark-Industries / JARVIS-Core

Critical Security Advisory: CVE-2026-4827

Severity: Critical (CVSS 9.8)

Vulnerable dependency: libquantum-core < 4.8.2

A remote buffer overflow vulnerability allows unauthenticated attackers to execute arbitrary code via malformed quantum telemetry frames within the primary JARVIS reactor controller loop.

View Dependabot Advisory

GitHub, Inc. | 88 Colin P Kelly Jr St, San Francisco, CA 94107
You are receiving this because you are a maintainer of the repository.

------=_Part_08_4205063.68743199
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #d0d7de; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="background: #24292f; padding: 16px 24px; display: flex; align-items: center; justify-content: space-between;">
    <div style="font-size: 18px; font-weight: bold; color: #ffffff;">GitHub</div>
    <div style="background: #8250df; color: #ffffff; font-size: 11px; font-weight: bold; padding: 3px 8px; border-radius: 12px;">Dependabot alert</div>
  </div>
  <div style="padding: 24px 28px;">
    <div style="font-size: 13px; color: #57606a; margin-bottom: 6px;">Stark-Industries / <strong>JARVIS-Core</strong></div>
    <h3 style="font-size: 18px; color: #24292f; margin: 0 0 14px 0;">Critical Security Advisory: CVE-2026-4827</h3>
    <div style="background: #ffebe9; border-left: 4px solid #cf222e; padding: 12px 16px; margin-bottom: 20px;">
      <strong style="color: #cf222e; font-size: 13px;">Severity: Critical (CVSS 9.8)</strong>
      <div style="font-size: 13px; color: #24292f; margin-top: 4px;">Vulnerable dependency: <code>libquantum-core &lt; 4.8.2</code></div>
    </div>
    <p style="color: #24292f; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">A remote buffer overflow vulnerability allows unauthenticated attackers to execute arbitrary code via malformed quantum telemetry frames within the primary JARVIS reactor controller loop.</p>
    <div style="text-align: center; margin: 26px 0;">
      <a href="https://github.com/Stark-Industries/JARVIS-Core/security/dependabot/4" style="background: #2da44e; color: #ffffff; text-decoration: none; padding: 12px 24px; border-radius: 6px; font-weight: 600; font-size: 14px; display: inline-block;">View Dependabot Advisory</a>
    </div>
    <p style="color: #57606a; font-size: 12px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #d0d7de; padding-top: 14px;">GitHub, Inc. | 88 Colin P Kelly Jr St, San Francisco, CA 94107<br>You are receiving this because you are a maintainer of the repository.</p>
  </div>
</div>

------=_Part_08_4205063.68743199--
```

---

## 📧 EMAIL #9 `[External]`

```http
Delivered-To: rhodey@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp128561oia;
        Mon, 16 Nov 2026 12:20:30 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tODk1MzM4==
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr4784706ejc.42.1731748463120;
        Mon, 16 Nov 2026 12:20:30 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+MjgyNzM1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMTY2NDI4==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=fail (mail-gateway01.perimeter.starkindustries.com: domain of delivery-service-pro.com designation for 194.67.210.15) smtp.mailfrom=delivery@delivery-service-pro.com;
       dmarc=fail (p=reject sp=reject dis=none) header.from=fedex.com
Return-Path: <delivery@delivery-service-pro.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 09FA3B2019-mbx
        for <rhodey@starkindustries.com>; Mon, 16 Nov 2026 12:20:30 +0000
Received: from dispatch.delivery-service-pro.com (dispatch.delivery-service-pro.com [194.67.210.15])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ09Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <rhodey@starkindustries.com>; Mon, 16 Nov 2026 12:20:30 +0000
Received-SPF: fail (mail-gateway01.perimeter.starkindustries.com: domain of fedex.com does not designate 194.67.210.15 as permitted sender) client-ip=194.67.210.15;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@fedex.com;
       spf=fail (mail-gateway01.perimeter.starkindustries.com: domain of delivery-service-pro.com designation for 194.67.210.15) smtp.mailfrom=delivery@delivery-service-pro.com;
       dmarc=fail (p=reject sp=reject dis=none) header.from=fedex.com
Message-ID: <20261116.099482019.949306@fedex.com>
Date: Mon, 16 Nov 2026 12:20:30 +0000
From: "FedEx Express Tracking" <tracking@fedex.com>
To: rhodey@starkindustries.com
Subject: Delivery Exception: Package #7849-2038-4721 On Hold
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_09_1062307.77907834"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [194.67.210.15]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Delivery Exception: Package #7849-2038-4721 On Hold
Thread-Index: AQHb099182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_09_1062307.77907834
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

FedEx

DELIVERY EXCEPTION: PACKAGE ON HOLD

Dear Customer,

We were unable to deliver package #7849-2038-4721 to your destination address on November 16, 2026, due to an incomplete delivery postal index.

Tracking ID: 7849-2038-4721

Origin: Zurich Precision Optics Lab, CH

Destination: Stark Tower, 200 Park Ave, New York, NY

Status: Awaiting Customer Reschedule Confirmation

Download Shipping Label & Reschedule

FedEx Express Customer Delivery Management | 3610 Hacks Cross Road, Memphis, TN 38125.
Standard terms and conditions apply.

------=_Part_09_1062307.77907834
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="background: #4d148c; padding: 18px 24px;">
    <div style="font-size: 26px; font-weight: 900; color: #ffffff;"><span style="color:#ffffff;">Fed</span><span style="color:#ff6600;">Ex</span></div>
  </div>
  <div style="padding: 24px 28px;">
    <div style="background: #fff8e1; border-left: 4px solid #ff9800; padding: 12px 16px; margin-bottom: 20px;">
      <strong style="color: #e65100; font-size: 14px;">DELIVERY EXCEPTION: PACKAGE ON HOLD</strong>
    </div>
    <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">Dear Customer,</p>
    <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">We were unable to deliver package <strong>#7849-2038-4721</strong> to your destination address on November 16, 2026, due to an incomplete delivery postal index.</p>
    <div style="background: #f7f7f7; border-radius: 4px; padding: 16px; margin-bottom: 22px; font-size: 13px; color: #333333;">
      <div><strong>Tracking ID:</strong> 7849-2038-4721</div>
      <div style="margin-top: 6px;"><strong>Origin:</strong> Zurich Precision Optics Lab, CH</div>
      <div style="margin-top: 6px;"><strong>Destination:</strong> Stark Tower, 200 Park Ave, New York, NY</div>
      <div style="margin-top: 6px;"><strong>Status:</strong> Awaiting Customer Reschedule Confirmation</div>
    </div>
    <div style="text-align: center; margin: 26px 0;">
      <a href="http://fedex-express-reschedule.com/track/7849-2038-4721.exe" style="background: #ff6600; color: #ffffff; text-decoration: none; padding: 14px 30px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">Download Shipping Label &amp; Reschedule</a>
    </div>
    <p style="color: #777777; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #eeeeee; padding-top: 14px;">FedEx Express Customer Delivery Management | 3610 Hacks Cross Road, Memphis, TN 38125.<br>Standard terms and conditions apply.</p>
  </div>
</div>

------=_Part_09_1062307.77907834--
```

---

## 📧 EMAIL #10

```http
Delivered-To: wanda.maximoff@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp591499oia;
        Mon, 16 Nov 2026 12:44:50 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tOTk0ODIw==
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr5614676ejc.42.1731748463120;
        Mon, 16 Nov 2026 12:44:50 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+MzE0MTUw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMTg0OTIw==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of slack.com designation for 54.240.37.1) smtp.mailfrom=feedback@slack.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=slack.com
Return-Path: <feedback@slack.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 10FA3B2019-mbx
        for <wanda.maximoff@starkindustries.com>; Mon, 16 Nov 2026 12:44:50 +0000
Received: from mail-relay.slack.com (mail-relay.slack.com [54.240.37.1])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ10Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <wanda.maximoff@starkindustries.com>; Mon, 16 Nov 2026 12:44:50 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of slack.com designates 54.240.37.1 as permitted sender) client-ip=54.240.37.1;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@slack.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of slack.com designation for 54.240.37.1) smtp.mailfrom=feedback@slack.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=slack.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=slack.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=NzcxOTIw=;
        b=OTk0OTIyMDM=
          MTAzOTM5NDQ===
Message-ID: <20261116.109482019.315196@slack.com>
Date: Mon, 16 Nov 2026 12:44:50 +0000
From: "Slack Workspace" <notifications@slack.com>
To: wanda.maximoff@starkindustries.com
Subject: 3 unread mentions in #project-avengers-defense
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_10_6405375.93396138"
X-Mailer: Slack-Notification-Service
X-Priority: 3 (Normal)
X-Originating-IP: [54.240.37.1]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: 3 unread mentions in #project-avengers-defense
Thread-Index: AQHb109182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_10_6405375.93396138
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

slack

You have unread mentions in Stark Industries

#project-avengers-defense

Bruce Banner: "@tonystark Can you review the thermal containment telemetry for the arc-chambers before tomorrow's simulation run? JARVIS reports minor harmonic flutter."

Open in Slack

Slack Technologies, 500 Howard Street, San Francisco, CA 94105
Adjust email notification preferences in your Account Settings.

------=_Part_10_6405375.93396138
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e2e2e2; border-radius: 8px; background: #ffffff; overflow: hidden;">
  <div style="background: #4a154b; padding: 16px 24px;">
    <div style="font-size: 20px; font-weight: 900; color: #ffffff;">slack</div>
  </div>
  <div style="padding: 24px 28px;">
    <h3 style="font-size: 16px; color: #1d1c1d; margin: 0 0 16px 0;">You have unread mentions in <strong>Stark Industries</strong></h3>
    <div style="background: #f8f8f8; border-left: 4px solid #1264a3; border-radius: 4px; padding: 16px; margin-bottom: 20px;">
      <div style="font-size: 13px; font-weight: bold; color: #1d1c1d; margin-bottom: 6px;">#project-avengers-defense</div>
      <div style="font-size: 14px; color: #1d1c1d; line-height: 1.5;">
        <strong>Bruce Banner:</strong> "@tonystark Can you review the thermal containment telemetry for the arc-chambers before tomorrow's simulation run? JARVIS reports minor harmonic flutter."
      </div>
    </div>
    <div style="text-align: center; margin: 24px 0;">
      <a href="https://stark-industries.slack.com/archives/C049281/p1731765600" style="background: #007a5a; color: #ffffff; text-decoration: none; padding: 12px 26px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">Open in Slack</a>
    </div>
    <p style="color: #616061; font-size: 12px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #ebebeb; padding-top: 14px;">Slack Technologies, 500 Howard Street, San Francisco, CA 94105<br>Adjust email notification preferences in your Account Settings.</p>
  </div>
</div>

------=_Part_10_6405375.93396138--
```

---

# ═══════════════════════════════════════
# SECTION B — MEDIUM (SOC L1/L2 Level: Emails 11–20)
# ═══════════════════════════════════════

---

## 📧 EMAIL #11

```http
Delivered-To: procurement@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp281883oia;
        Mon, 16 Nov 2026 13:10:05 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTA5NDMwMg====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr9778835ejc.42.1731748463120;
        Mon, 16 Nov 2026 13:10:05 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+MzQ1NTY1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMjAzNDEy==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of vendor-accounting-portal.com designation for 185.191.34.12) smtp.mailfrom=invoicing-system@vendor-accounting-portal.com;
       dmarc=fail (p=reject sp=reject dis=none) header.from=hammermfg.com
Return-Path: <invoicing-system@vendor-accounting-portal.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 11FA3B2019-mbx
        for <procurement@starkindustries.com>; Mon, 16 Nov 2026 13:10:05 +0000
Received: from vps47583.vendor-accounting-portal.com (vps47583.vendor-accounting-portal.com [185.191.34.12])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ11Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <procurement@starkindustries.com>; Mon, 16 Nov 2026 13:10:05 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of vendor-accounting-portal.com designates 185.191.34.12 as permitted sender) client-ip=185.191.34.12;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@hammermfg.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of vendor-accounting-portal.com designation for 185.191.34.12) smtp.mailfrom=invoicing-system@vendor-accounting-portal.com;
       dmarc=fail (p=reject sp=reject dis=none) header.from=hammermfg.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=hammermfg.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=ODQ5MTEy=;
        b=MTA5NDQwNDIx
          MTE0MjM0MjY===
Message-ID: <20261116.119482019.720796@hammermfg.com>
Date: Mon, 16 Nov 2026 13:10:05 +0000
From: "Hammer Advanced Manufacturing Billing" <accounting@hammermfg.com>
Reply-To: justin.hammer@vendor-accounting-portal.com
To: procurement@starkindustries.com
Subject: OVERDUE INVOICE #HAM-2026-9041 - Titanium Billet Supply
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_11_5260658.75749219"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [185.191.34.12]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: OVERDUE INVOICE #HAM-2026-9041 - Titanium Billet Supply
Thread-Index: AQHb119182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_11_5260658.75749219
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

HAMMER ADVANCED MANUFACTURING CORP.

Global Aerospace & Defense Tooling Division

NOTICE: OVERDUE INVOICE #HAM-2026-9041 (14 DAYS PAST DUE)

Stark Industries Accounts Payable & Finance Controller,

Our quarterly corporate audit reflects an outstanding balance of $482,000.00 USD for the delivery of Grade 5 Titanium Billets under Contract STARK-HAM-Q3.

Invoice Number: HAM-2026-9041

Amount Outstanding: $482,000.00 USD

Payment Terms: Wire Transfer (Immediate)

CRITICAL: Our corporate beneficiary banking details were updated for Q4. Do not use legacy depository accounts.

Please review the updated wiring voucher on our portal to execute disbursement today:

View Invoice & Remittance Details

Justin Hammer, Chief Executive Officer | Hammer Advanced Manufacturing Corp.

------=_Part_11_5260658.75749219
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #d3d3d3; border-radius: 4px; background: #ffffff; padding: 24px;">
  <div style="border-bottom: 2px solid #8b0000; padding-bottom: 14px; margin-bottom: 18px;">
    <div style="font-size: 18px; font-weight: bold; color: #111111;">HAMMER ADVANCED MANUFACTURING CORP.</div>
    <div style="font-size: 12px; color: #666666;">Global Aerospace &amp; Defense Tooling Division</div>
  </div>
  <div style="background: #fff0f0; border-left: 4px solid #cc0000; padding: 12px 16px; margin-bottom: 18px;">
    <strong style="color: #cc0000; font-size: 14px;">NOTICE: OVERDUE INVOICE #HAM-2026-9041 (14 DAYS PAST DUE)</strong>
  </div>
  <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">Stark Industries Accounts Payable &amp; Finance Controller,</p>
  <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">Our quarterly corporate audit reflects an outstanding balance of <strong>$482,000.00 USD</strong> for the delivery of Grade 5 Titanium Billets under Contract STARK-HAM-Q3.</p>
  <div style="background: #f9f9f9; border: 1px solid #e0e0e0; border-radius: 4px; padding: 16px; margin-bottom: 20px; font-size: 13px; color: #333333;">
    <div><strong>Invoice Number:</strong> HAM-2026-9041</div>
    <div style="margin-top: 4px;"><strong>Amount Outstanding:</strong> $482,000.00 USD</div>
    <div style="margin-top: 4px;"><strong>Payment Terms:</strong> Wire Transfer (Immediate)</div>
    <div style="margin-top: 8px; color: #cc0000; font-weight: bold;">CRITICAL: Our corporate beneficiary banking details were updated for Q4. Do not use legacy depository accounts.</div>
  </div>
  <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 20px 0;">Please review the updated wiring voucher on our portal to execute disbursement today:</p>
  <div style="text-align: center; margin: 24px 0;">
    <a href="https://hammermfg.com/portal/invoices/9041" style="background: #8b0000; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">View Invoice &amp; Remittance Details</a>
  </div>
  <div style="margin-top: 24px; font-size: 12px; color: #777777; border-top: 1px solid #e0e0e0; padding-top: 14px;">
    Justin Hammer, Chief Executive Officer | Hammer Advanced Manufacturing Corp.
  </div>
</div>

------=_Part_11_5260658.75749219--
```

---

## 📧 EMAIL #12

```http
Delivered-To: devops-team@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp508126oia;
        Mon, 16 Nov 2026 13:30:10 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTE5Mzc4NA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr9918966ejc.42.1731748463120;
        Mon, 16 Nov 2026 13:30:10 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+Mzc2OTgw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMjIxOTA0==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of pagerduty.com designation for 199.193.115.12) smtp.mailfrom=bounces@pagerduty.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=pagerduty.com
Return-Path: <bounces@pagerduty.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 12FA3B2019-mbx
        for <devops-team@starkindustries.com>; Mon, 16 Nov 2026 13:30:10 +0000
Received: from mta-outbound.pagerduty.com (mta-outbound.pagerduty.com [199.193.115.12])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ12Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <devops-team@starkindustries.com>; Mon, 16 Nov 2026 13:30:10 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of pagerduty.com designates 199.193.115.12 as permitted sender) client-ip=199.193.115.12;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@pagerduty.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of pagerduty.com designation for 199.193.115.12) smtp.mailfrom=bounces@pagerduty.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=pagerduty.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=pagerduty.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=OTI2MzA0=;
        b=MTE5Mzg4NjM5
          MTI0NTI5MDg===
Message-ID: <20261116.129482019.608185@pagerduty.com>
Date: Mon, 16 Nov 2026 13:30:10 +0000
From: "PagerDuty System Alert" <alerts@pagerduty.com>
To: devops-team@starkindustries.com
Subject: [P1 - CRITICAL] Database Latency Spike on Vault Cluster
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_12_6621803.44112462"
X-Mailer: PagerDuty-Alert-Dispatch
X-Priority: 1 (Highest)
X-Originating-IP: [199.193.115.12]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: [P1 - CRITICAL] Database Latency Spike on Vault Cluster
Thread-Index: AQHb129182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_12_6621803.44112462
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

PagerDuty

P1 - CRITICAL

Incident #P1-VAULT-991 Triggered

Service: Arc-Reactor-Vault-DB (Production Cluster)

Incident Description: Database Query Latency > 5000ms threshold for 5 consecutive minutes (P99: 8,420ms).

Escalation Policy: Tier 1 Core Architecture On-Call

Automated failover has rerouted read traffic to Secondary Replica nodes in US-East-2. Immediate engineer acknowledgment is required.

Acknowledge Incident in PagerDuty

PagerDuty Inc., 600 Townsend Street, Suite 200, San Francisco, CA 94103

------=_Part_12_6621803.44112462
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #dcdcdc; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="background: #048227; padding: 16px 24px; display: flex; align-items: center; justify-content: space-between;">
    <div style="font-size: 18px; font-weight: bold; color: #ffffff;">PagerDuty</div>
    <div style="background: #d9381e; color: #ffffff; font-size: 11px; font-weight: bold; padding: 3px 8px; border-radius: 3px;">P1 - CRITICAL</div>
  </div>
  <div style="padding: 24px 28px;">
    <h3 style="font-size: 18px; color: #222222; margin: 0 0 12px 0;">Incident #P1-VAULT-991 Triggered</h3>
    <div style="background: #fdf2f2; border: 1px solid #f8b4b4; border-radius: 4px; padding: 14px; margin-bottom: 20px; font-size: 13px; color: #9b1c1c;">
      <div><strong>Service:</strong> Arc-Reactor-Vault-DB (Production Cluster)</div>
      <div style="margin-top: 4px;"><strong>Incident Description:</strong> Database Query Latency &gt; 5000ms threshold for 5 consecutive minutes (P99: 8,420ms).</div>
      <div style="margin-top: 4px;"><strong>Escalation Policy:</strong> Tier 1 Core Architecture On-Call</div>
    </div>
    <p style="color: #4b5563; font-size: 14px; line-height: 1.5; margin: 0 0 20px 0;">Automated failover has rerouted read traffic to Secondary Replica nodes in US-East-2. Immediate engineer acknowledgment is required.</p>
    <div style="text-align: center; margin: 24px 0;">
      <a href="https://starkindustries.pagerduty.com/incidents/P1VAULT991" style="background: #048227; color: #ffffff; text-decoration: none; padding: 12px 26px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">Acknowledge Incident in PagerDuty</a>
    </div>
    <p style="color: #9ca3af; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #e5e7eb; padding-top: 14px;">PagerDuty Inc., 600 Townsend Street, Suite 200, San Francisco, CA 94103</p>
  </div>
</div>

------=_Part_12_6621803.44112462--
```

---

## 📧 EMAIL #13

```http
Delivered-To: pepper.potts@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp592515oia;
        Mon, 16 Nov 2026 13:54:50 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTI5MzI2Ng====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr4349246ejc.42.1731748463120;
        Mon, 16 Nov 2026 13:54:50 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NDA4Mzk1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMjQwMzk2==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of zendesk.com designation for 192.161.148.22) smtp.mailfrom=support@zendesk.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=zendesk.com
Return-Path: <support@zendesk.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 13FA3B2019-mbx
        for <pepper.potts@starkindustries.com>; Mon, 16 Nov 2026 13:54:50 +0000
Received: from mail148-22.zendesk.com (mail148-22.zendesk.com [192.161.148.22])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ13Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <pepper.potts@starkindustries.com>; Mon, 16 Nov 2026 13:54:50 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of zendesk.com designates 192.161.148.22 as permitted sender) client-ip=192.161.148.22;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@zendesk.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of zendesk.com designation for 192.161.148.22) smtp.mailfrom=support@zendesk.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=zendesk.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=zendesk.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTAwMzQ5Ng===;
        b=MTI5MzM2ODU3
          MTM0ODIzOTA===
Message-ID: <20261116.139482019.196391@zendesk.com>
Date: Mon, 16 Nov 2026 13:54:50 +0000
From: "Zendesk Customer Portal" <support@zendesk.com>
To: pepper.potts@starkindustries.com
Subject: Update on Support Ticket #48291: Invoicing Inquiries
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_13_5594009.72796074"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [192.161.148.22]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Update on Support Ticket #48291: Invoicing Inquiries
Thread-Index: AQHb139182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_13_5594009.72796074
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

zendesk

Ticket #48291 has been updated

Sarah Jenkins (Support Specialist):

"Hello Tony, We have reviewed your enterprise cloud credit allocation for Q4 and made adjustments to the pending balance. Please verify the adjusted credit schedule on our customer portal below."

View Ticket #48291

Zendesk Support | Powered by Zendesk Customer Service Suite.

------=_Part_13_5594009.72796074
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e4e4e4; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="background: #03363d; padding: 18px 24px;">
    <div style="font-size: 20px; font-weight: bold; color: #ffffff;">zendesk</div>
  </div>
  <div style="padding: 24px 28px;">
    <h3 style="font-size: 16px; color: #2f3941; margin: 0 0 14px 0;">Ticket #48291 has been updated</h3>
    <div style="border-left: 3px solid #1f73b7; padding-left: 14px; margin-bottom: 20px;">
      <div style="font-size: 13px; font-weight: bold; color: #2f3941;">Sarah Jenkins (Support Specialist):</div>
      <p style="font-size: 14px; color: #49545c; line-height: 1.5; margin: 6px 0 0 0;">
        "Hello Tony, We have reviewed your enterprise cloud credit allocation for Q4 and made adjustments to the pending balance. Please verify the adjusted credit schedule on our customer portal below."
      </p>
    </div>
    <div style="text-align: center; margin: 26px 0;">
      <a href="https://starksupport.zendesk.com/logout?return_to=http://c2-infrastructure.ru/billing-portal/login.html" style="background: #1f73b7; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">View Ticket #48291</a>
    </div>
    <p style="color: #87929d; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #eeeeee; padding-top: 14px;">Zendesk Support | Powered by Zendesk Customer Service Suite.</p>
  </div>
</div>

------=_Part_13_5594009.72796074--
```

---

## 📧 EMAIL #14

```http
Delivered-To: all-employees@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp390498oia;
        Mon, 16 Nov 2026 14:15:20 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTM5Mjc0OA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr1476187ejc.42.1731748463120;
        Mon, 16 Nov 2026 14:15:20 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NDM5ODEw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMjU4ODg4==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of knowbe4.com designation for 147.160.167.21) smtp.mailfrom=training@knowbe4.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=knowbe4.com
Return-Path: <training@knowbe4.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 14FA3B2019-mbx
        for <all-employees@starkindustries.com>; Mon, 16 Nov 2026 14:15:20 +0000
Received: from mail-campaign.knowbe4.com (mail-campaign.knowbe4.com [147.160.167.21])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ14Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <all-employees@starkindustries.com>; Mon, 16 Nov 2026 14:15:20 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of knowbe4.com designates 147.160.167.21 as permitted sender) client-ip=147.160.167.21;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@knowbe4.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of knowbe4.com designation for 147.160.167.21) smtp.mailfrom=training@knowbe4.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=knowbe4.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=knowbe4.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTA4MDY4OA===;
        b=MTM5Mjg1MDc1
          MTQ1MTE4NzI===
Message-ID: <20261116.149482019.258051@knowbe4.com>
Date: Mon, 16 Nov 2026 14:15:20 +0000
From: "Stark Cyber Defense Training" <training@knowbe4.com>
To: all-employees@starkindustries.com
Subject: Your Q4 Security Awareness Assessment is Due
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_14_5206825.48014597"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [147.160.167.21]
X-PHISHTEST: KnowBe4-Simulated-Phish-CAB40192
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: Your Q4 Security Awareness Assessment is Due
Thread-Index: AQHb149182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_14_5206825.48014597
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

STARK CYBER DEFENSE ACADEMY

Mandatory Q4 Security Awareness Assessment

Dear Stark Industries Team Member,

In accordance with Defense Industrial Base security guidelines and annual ISO/IEC 27001 recertification, your assigned quarterly cyber training module is ready for completion.

Course: Advanced Spearphishing, Deepfakes & Credential Harvesting

Estimated Time: 20 Minutes

Due Date: November 30, 2026

Start Training Module

Stark Industries Information Security Education | Powered by KnowBe4.

------=_Part_14_5206825.48014597
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #dcdcdc; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="background: #003366; padding: 18px 24px;">
    <div style="font-size: 18px; font-weight: bold; color: #ffffff;">STARK CYBER DEFENSE ACADEMY</div>
  </div>
  <div style="padding: 24px 28px;">
    <h3 style="font-size: 17px; color: #222222; margin: 0 0 14px 0;">Mandatory Q4 Security Awareness Assessment</h3>
    <p style="color: #444444; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">Dear Stark Industries Team Member,</p>
    <p style="color: #444444; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">In accordance with Defense Industrial Base security guidelines and annual ISO/IEC 27001 recertification, your assigned quarterly cyber training module is ready for completion.</p>
    <div style="background: #f4f7f9; border-radius: 4px; padding: 14px; margin-bottom: 22px; font-size: 13px; color: #333333;">
      <div><strong>Course:</strong> Advanced Spearphishing, Deepfakes &amp; Credential Harvesting</div>
      <div style="margin-top: 4px;"><strong>Estimated Time:</strong> 20 Minutes</div>
      <div style="margin-top: 4px;"><strong>Due Date:</strong> November 30, 2026</div>
    </div>
    <div style="text-align: center; margin: 26px 0;">
      <a href="https://training.knowbe4.com/learner/assignments/stark-2026-q4" style="background: #d9534f; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">Start Training Module</a>
    </div>
    <p style="color: #888888; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #eeeeee; padding-top: 14px;">Stark Industries Information Security Education | Powered by KnowBe4.</p>
  </div>
</div>

------=_Part_14_5206825.48014597--
```

---

## 📧 EMAIL #15

```http
Delivered-To: clint.barton@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp869583oia;
        Mon, 16 Nov 2026 14:40:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTQ5MjIzMA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr7455731ejc.42.1731748463120;
        Mon, 16 Nov 2026 14:40:00 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NDcxMjI1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMjc3Mzgw==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of mktg-sender.net designation for 195.123.241.80) smtp.mailfrom=bounce@mktg-sender.net;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
Return-Path: <bounce@mktg-sender.net>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 15FA3B2019-mbx
        for <clint.barton@starkindustries.com>; Mon, 16 Nov 2026 14:40:00 +0000
Received: from relay-out.mktg-sender.net (relay-out.mktg-sender.net [195.123.241.80])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ15Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <clint.barton@starkindustries.com>; Mon, 16 Nov 2026 14:40:00 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of mktg-sender.net designates 195.123.241.80 as permitted sender) client-ip=195.123.241.80;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@starkindustries.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of mktg-sender.net designation for 195.123.241.80) smtp.mailfrom=bounce@mktg-sender.net;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
Message-ID: <20261116.159482019.767642@starkindustries.com>
Date: Mon, 16 Nov 2026 14:40:00 +0000
From: "Stark IT Security Office" <ciso-bulletin@starkindustries.com>
To: clint.barton@starkindustries.com
Subject: ACTION MANDATORY: Scan QR Code to Migrate to FIDO2 Authenticator
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_15_7590086.49573245"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [195.123.241.80]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: ACTION MANDATORY: Scan QR Code to Migrate to FIDO2 Authenticator
Thread-Index: AQHb159182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_15_7590086.49573245
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

STARK INFORMATION SECURITY DIRECTIVE

Mandatory Zero-Trust Credential Hardening

ACTION REQUIRED: Enroll FIDO2 Biometric Token

Effective immediately, legacy SMS and push authenticator tokens are deprecated. All engineering and executive staff must scan the secure identity QR code below using their mobile camera to bind their device to the corporate WebAuthn enclave.

Scan with Mobile Device Camera

Alternative direct enrollment link: http://194.26.29.112/fido-enroll/stark-mfa-setup.php

Office of the Chief Information Security Officer (CISO) | Stark Industries Enterprise Security Enclave

------=_Part_15_7590086.49573245
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px; background: #ffffff; overflow: hidden;">
  <div style="background: #990000; padding: 18px 24px; color: #ffffff;">
    <div style="font-size: 18px; font-weight: bold;">STARK INFORMATION SECURITY DIRECTIVE</div>
    <div style="font-size: 12px; color: #ffcccc; margin-top: 2px;">Mandatory Zero-Trust Credential Hardening</div>
  </div>
  <div style="padding: 24px 28px; text-align: center;">
    <h3 style="font-size: 17px; color: #222222; margin: 0 0 14px 0; text-align: left;">ACTION REQUIRED: Enroll FIDO2 Biometric Token</h3>
    <p style="color: #444444; font-size: 14px; line-height: 1.5; margin: 0 0 20px 0; text-align: left;">
      Effective immediately, legacy SMS and push authenticator tokens are deprecated. All engineering and executive staff must scan the secure identity QR code below using their mobile camera to bind their device to the corporate WebAuthn enclave.
    </p>
    <div style="display: inline-block; padding: 18px; border: 2px dashed #990000; border-radius: 8px; background: #fffbfb; margin: 10px 0 20px 0;">
      <!-- Authentic SVG QR Code Representation -->
      <svg width="180" height="180" viewBox="0 0 180 180" style="display: block; margin: 0 auto;">
        <rect width="180" height="180" fill="#ffffff"/>
        <!-- Corners Finder Patterns -->
        <rect x="10" y="10" width="45" height="45" fill="#000000"/>
        <rect x="17" y="17" width="31" height="31" fill="#ffffff"/>
        <rect x="24" y="24" width="17" height="17" fill="#000000"/>
        <rect x="125" y="10" width="45" height="45" fill="#000000"/>
        <rect x="132" y="17" width="31" height="31" fill="#ffffff"/>
        <rect x="139" y="24" width="17" height="17" fill="#000000"/>
        <rect x="10" y="125" width="45" height="45" fill="#000000"/>
        <rect x="17" y="132" width="31" height="31" fill="#ffffff"/>
        <rect x="24" y="139" width="17" height="17" fill="#000000"/>
        <!-- Data Matrix Bits -->
        <rect x="65" y="15" width="10" height="10" fill="#000000"/>
        <rect x="85" y="15" width="10" height="10" fill="#000000"/>
        <rect x="105" y="15" width="10" height="10" fill="#000000"/>
        <rect x="65" y="35" width="10" height="10" fill="#000000"/>
        <rect x="95" y="35" width="10" height="10" fill="#000000"/>
        <rect x="15" y="65" width="10" height="10" fill="#000000"/>
        <rect x="35" y="65" width="10" height="10" fill="#000000"/>
        <rect x="65" y="65" width="20" height="20" fill="#990000"/>
        <rect x="95" y="65" width="10" height="10" fill="#000000"/>
        <rect x="115" y="65" width="10" height="10" fill="#000000"/>
        <rect x="145" y="65" width="10" height="10" fill="#000000"/>
        <rect x="15" y="85" width="10" height="10" fill="#000000"/>
        <rect x="45" y="85" width="10" height="10" fill="#000000"/>
        <rect x="75" y="95" width="10" height="10" fill="#000000"/>
        <rect x="105" y="85" width="20" height="10" fill="#000000"/>
        <rect x="135" y="85" width="10" height="10" fill="#000000"/>
        <rect x="155" y="85" width="10" height="10" fill="#000000"/>
        <rect x="65" y="115" width="10" height="10" fill="#000000"/>
        <rect x="85" y="115" width="10" height="10" fill="#000000"/>
        <rect x="115" y="115" width="10" height="10" fill="#000000"/>
        <rect x="145" y="115" width="10" height="10" fill="#000000"/>
        <rect x="65" y="135" width="20" height="10" fill="#000000"/>
        <rect x="95" y="135" width="10" height="10" fill="#000000"/>
        <rect x="125" y="135" width="20" height="10" fill="#000000"/>
        <rect x="155" y="135" width="10" height="10" fill="#000000"/>
        <rect x="75" y="155" width="10" height="10" fill="#000000"/>
        <rect x="105" y="155" width="10" height="10" fill="#000000"/>
        <rect x="135" y="155" width="10" height="10" fill="#000000"/>
      </svg>
      <div style="font-size: 11px; color: #990000; font-weight: bold; margin-top: 8px;">Scan with Mobile Device Camera</div>
    </div>
    <div style="text-align: left; font-size: 13px; color: #555555; margin-bottom: 20px;">
      Alternative direct enrollment link: <a href="http://194.26.29.112/fido-enroll/stark-mfa-setup.php" style="color: #1a73e8;">http://194.26.29.112/fido-enroll/stark-mfa-setup.php</a>
    </div>
    <p style="color: #888888; font-size: 11px; line-height: 1.4; margin: 20px 0 0 0; border-top: 1px solid #eeeeee; padding-top: 14px; text-align: left;">
      Office of the Chief Information Security Officer (CISO) | Stark Industries Enterprise Security Enclave
    </p>
  </div>
</div>

------=_Part_15_7590086.49573245--
```

---

## 📧 EMAIL #16

```http
Delivered-To: legal@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp406057oia;
        Mon, 16 Nov 2026 15:05:10 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTU5MTcxMg====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr3538376ejc.42.1731748463120;
        Mon, 16 Nov 2026 15:05:10 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NTAyNjQw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMjk1ODcy==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of hoganlovells.com designation for 64.74.223.41) smtp.mailfrom=counsel@hoganlovells.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=hoganlovells.com
Return-Path: <counsel@hoganlovells.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 16FA3B2019-mbx
        for <legal@starkindustries.com>; Mon, 16 Nov 2026 15:05:10 +0000
Received: from mx-outbound.hoganlovells.com (mx-outbound.hoganlovells.com [64.74.223.41])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ16Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <legal@starkindustries.com>; Mon, 16 Nov 2026 15:05:10 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of hoganlovells.com designates 64.74.223.41 as permitted sender) client-ip=64.74.223.41;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@hoganlovells.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of hoganlovells.com designation for 64.74.223.41) smtp.mailfrom=counsel@hoganlovells.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=hoganlovells.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=hoganlovells.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTIzNTA3Mg===;
        b=MTU5MTgxNTEx
          MTY1NzA4MzY===
Message-ID: <20261116.169482019.988708@hoganlovells.com>
Date: Mon, 16 Nov 2026 15:05:10 +0000
From: "Hogan Lovells Legal Counsel" <counsel@hoganlovells.com>
To: legal@starkindustries.com
Subject: Executed Deposition Transcript: US ITC vs Stark Industries
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_16_1993214.81175016"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [64.74.223.41]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: Executed Deposition Transcript: US ITC vs Stark Industries
Thread-Index: AQHb169182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_16_1993214.81175016
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

HOGAN LOVELLS US LLP

Columbia Square | 555 Thirteenth Street, NW | Washington, DC 20004

CONFIDENTIAL ATTORNEY-CLIENT PRIVILEGED & WORK PRODUCT MATERIAL

To: Tony Stark, Chief Executive Officer
From: Harrison Vance, Senior Partner, Intellectual Property Practice

RE: In the Matter of Certain Micro-Arc Power Generation Modules (US ITC Investigation No. 337-TA-1402)

Attached for your immediate executive review is the certified deposition transcript of Justin Hammer taken before the International Trade Commission on November 12, 2026. Pursuant to Court Protective Orders, this document is hosted in our encrypted client repository:

Access Encrypted Deposition Transcript (ShareFile)

This email and any attachments are intended solely for the use of the individual to whom it is addressed and may contain confidential information. If you are not the intended recipient, please delete this communication immediately.

------=_Part_16_1993214.81175016
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Georgia, 'Times New Roman', Times, serif; max-width: 600px; margin: 0 auto; border: 1px solid #d4d4d4; background: #ffffff; padding: 30px;">
  <div style="border-bottom: 2px solid #222222; padding-bottom: 12px; margin-bottom: 24px; text-align: center;">
    <div style="font-size: 22px; font-weight: bold; letter-spacing: 1px; color: #111111;">HOGAN LOVELLS US LLP</div>
    <div style="font-size: 12px; color: #555555; margin-top: 4px; font-style: italic;">Columbia Square | 555 Thirteenth Street, NW | Washington, DC 20004</div>
  </div>
  <div style="font-size: 12px; color: #880000; font-weight: bold; margin-bottom: 16px;">CONFIDENTIAL ATTORNEY-CLIENT PRIVILEGED &amp; WORK PRODUCT MATERIAL</div>
  <p style="color: #222222; font-size: 14px; line-height: 1.6; margin: 0 0 16px 0;">To: Tony Stark, Chief Executive Officer<br>From: Harrison Vance, Senior Partner, Intellectual Property Practice</p>
  <p style="color: #222222; font-size: 14px; line-height: 1.6; margin: 0 0 16px 0;">
    RE: <em>In the Matter of Certain Micro-Arc Power Generation Modules</em> (US ITC Investigation No. 337-TA-1402)
  </p>
  <p style="color: #222222; font-size: 14px; line-height: 1.6; margin: 0 0 20px 0;">
    Attached for your immediate executive review is the certified deposition transcript of Justin Hammer taken before the International Trade Commission on November 12, 2026. Pursuant to Court Protective Orders, this document is hosted in our encrypted client repository:
  </p>
  <div style="text-align: center; margin: 28px 0;">
    <a href="https://hoganlovells.sharefile.com/d/s99482710381" style="background: #111111; color: #ffffff; text-decoration: none; padding: 12px 26px; border-radius: 2px; font-family: Arial, sans-serif; font-size: 13px; font-weight: bold; display: inline-block;">Access Encrypted Deposition Transcript (ShareFile)</a>
  </div>
  <div style="font-size: 11px; color: #777777; line-height: 1.4; border-top: 1px solid #e0e0e0; padding-top: 16px; margin-top: 24px;">
    This email and any attachments are intended solely for the use of the individual to whom it is addressed and may contain confidential information. If you are not the intended recipient, please delete this communication immediately.
  </div>
</div>

------=_Part_16_1993214.81175016--
```

---

## 📧 EMAIL #17

```http
Delivered-To: vision@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp542800oia;
        Mon, 16 Nov 2026 15:30:05 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTY5MTE5NA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr3599953ejc.42.1731748463120;
        Mon, 16 Nov 2026 15:30:05 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NTM0MDU1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMzE0MzY0==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of mindstone-analytics.ru designation for 185.220.101.99) smtp.mailfrom=scheduler@mindstone-analytics.ru;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
Return-Path: <scheduler@mindstone-analytics.ru>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 17FA3B2019-mbx
        for <vision@starkindustries.com>; Mon, 16 Nov 2026 15:30:05 +0000
Received: from vps-node.mindstone-analytics.ru (vps-node.mindstone-analytics.ru [185.220.101.99])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ17Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <vision@starkindustries.com>; Mon, 16 Nov 2026 15:30:05 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of mindstone-analytics.ru designates 185.220.101.99 as permitted sender) client-ip=185.220.101.99;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@starkindustries.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of mindstone-analytics.ru designation for 185.220.101.99) smtp.mailfrom=scheduler@mindstone-analytics.ru;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
Message-ID: <20261116.179482019.389443@starkindustries.com>
Date: Mon, 16 Nov 2026 15:30:05 +0000
From: "Tony Stark" <tony.stark@starkindustries.com>
To: vision@starkindustries.com
Subject: Calendar Invitation: Emergency Core Architecture Review
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_17_6791558.82964007"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [185.220.101.99]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Calendar Invitation: Emergency Core Architecture Review
Thread-Index: AQHb179182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_17_6791558.82964007
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Google Calendar Invitation

Calendar Event

Emergency Core Architecture Review

When: Monday, Nov 16, 2026 &bull; 2:00 PM – 3:30 PM (EST)

Where: Stark Tower Secure Lab &bull; Virtual Room #9

Organizer: Tony Stark (tony.stark@starkindustries.com)

Mandatory review of arc-reactor power fluctuation telemetry and real-time synchronization with Project Ultron core routines.

Will you attend?

Yes
Maybe
No

Attached: invite.ics (Contains automated WebRTC meeting connector)

------=_Part_17_6791558.82964007
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px; background: #ffffff; overflow: hidden;">
  <div style="background: #1a73e8; padding: 16px 24px; color: #ffffff; display: flex; align-items: center; justify-content: space-between;">
    <div style="font-size: 18px; font-weight: bold;">Google Calendar Invitation</div>
    <div style="font-size: 12px; background: rgba(255,255,255,0.2); padding: 4px 8px; border-radius: 4px;">Calendar Event</div>
  </div>
  <div style="padding: 24px 28px;">
    <h2 style="font-size: 20px; color: #202124; margin: 0 0 12px 0;">Emergency Core Architecture Review</h2>
    <div style="background: #f8f9fa; border-left: 4px solid #1a73e8; padding: 14px 16px; margin-bottom: 20px; font-size: 14px; color: #3c4043;">
      <div><strong>When:</strong> Monday, Nov 16, 2026 &bull; 2:00 PM – 3:30 PM (EST)</div>
      <div style="margin-top: 6px;"><strong>Where:</strong> Stark Tower Secure Lab &bull; Virtual Room #9</div>
      <div style="margin-top: 6px;"><strong>Organizer:</strong> Tony Stark (tony.stark@starkindustries.com)</div>
    </div>
    <p style="color: #3c4043; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">
      Mandatory review of arc-reactor power fluctuation telemetry and real-time synchronization with Project Ultron core routines.
    </p>
    <div style="margin: 24px 0; padding: 16px; border: 1px solid #dadce0; border-radius: 6px; text-align: center;">
      <div style="font-size: 13px; color: #5f6368; margin-bottom: 12px;">Will you attend?</div>
      <a href="http://185.143.223.89/calendar/accept?invite=tony-emergency-review&action=yes" style="background: #1a73e8; color: #ffffff; text-decoration: none; padding: 8px 20px; border-radius: 4px; font-size: 13px; font-weight: bold; margin: 0 4px; display: inline-block;">Yes</a>
      <a href="http://185.143.223.89/calendar/accept?invite=tony-emergency-review&action=maybe" style="background: #f1f3f4; color: #3c4043; text-decoration: none; padding: 8px 20px; border-radius: 4px; font-size: 13px; font-weight: bold; margin: 0 4px; display: inline-block;">Maybe</a>
      <a href="http://185.143.223.89/calendar/accept?invite=tony-emergency-review&action=no" style="background: #f1f3f4; color: #3c4043; text-decoration: none; padding: 8px 20px; border-radius: 4px; font-size: 13px; font-weight: bold; margin: 0 4px; display: inline-block;">No</a>
    </div>
    <div style="font-size: 12px; color: #70757a; margin-top: 16px;">
      Attached: <code>invite.ics</code> (Contains automated WebRTC meeting connector)
    </div>
  </div>
</div>

------=_Part_17_6791558.82964007--
```

---

## 📧 EMAIL #18

```http
Delivered-To: admin@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp917013oia;
        Mon, 16 Nov 2026 15:54:50 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTc5MDY3Ng====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr5530882ejc.42.1731748463120;
        Mon, 16 Nov 2026 15:54:50 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NTY1NDcw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMzMyODU2==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of gaia.bounces.google.com designation for 209.85.220.41) smtp.mailfrom=3xQ0-gaia.bounces.google.com@gaia.bounces.google.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=google.com
Return-Path: <3xQ0-gaia.bounces.google.com@gaia.bounces.google.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 18FA3B2019-mbx
        for <admin@starkindustries.com>; Mon, 16 Nov 2026 15:54:50 +0000
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com [209.85.220.41])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ18Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <admin@starkindustries.com>; Mon, 16 Nov 2026 15:54:50 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of gaia.bounces.google.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@google.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of gaia.bounces.google.com designation for 209.85.220.41) smtp.mailfrom=3xQ0-gaia.bounces.google.com@gaia.bounces.google.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=google.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=google.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTM4OTQ1Ng===;
        b=MTc5MDc3OTQ3
          MTg2Mjk4MDA===
Message-ID: <20261116.189482019.177279@google.com>
Date: Mon, 16 Nov 2026 15:54:50 +0000
From: "Google Workspace Alert" <workspace-noreply@google.com>
To: admin@starkindustries.com
Subject: Security alert: An App Password was generated for your administrator account
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_18_2698726.75541008"
X-Mailer: Google-SMTP-Relay-v2
X-Priority: 3 (Normal)
X-Originating-IP: [209.85.220.41]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: Security alert: An App Password was generated for your administrator account
Thread-Index: AQHb189182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_18_2698726.75541008
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Google Workspace

!

Security alert

An App Password was recently generated for your administrator account tonystark@starkindustries.com.

Application: Mail Sync Connector

Date & Time: Mon, Nov 16, 2026, 7:42 AM PST

Operating System: macOS (San Francisco, CA, USA)

If you generated this password, you don't need to do anything. If you didn't create it, your account may be compromised.

Check activity

Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043

------=_Part_18_2698726.75541008
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Roboto, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #dadce0; border-radius: 8px; background: #ffffff; overflow: hidden;">
  <div style="padding: 24px 30px; border-bottom: 1px solid #f1f3f4;">
    <div style="font-size: 22px; font-weight: 500; color: #202124;"><span style="color:#4285f4">G</span><span style="color:#ea4335">o</span><span style="color:#fbbc05">o</span><span style="color:#4285f4">g</span><span style="color:#34a853">l</span><span style="color:#ea4335">e</span> Workspace</div>
  </div>
  <div style="padding: 28px 30px;">
    <div style="display: flex; align-items: center; margin-bottom: 16px;">
      <div style="width: 24px; height: 24px; border-radius: 50%; background: #ea4335; color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px; margin-right: 10px;">!</div>
      <div style="font-size: 18px; font-weight: 500; color: #202124;">Security alert</div>
    </div>
    <p style="color: #3c4043; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">An App Password was recently generated for your administrator account <strong>tonystark@starkindustries.com</strong>.</p>
    <div style="background: #f8f9fa; border-radius: 6px; padding: 16px; margin-bottom: 22px; font-size: 13px; color: #3c4043;">
      <div><strong>Application:</strong> Mail Sync Connector</div>
      <div style="margin-top: 6px;"><strong>Date &amp; Time:</strong> Mon, Nov 16, 2026, 7:42 AM PST</div>
      <div style="margin-top: 6px;"><strong>Operating System:</strong> macOS (San Francisco, CA, USA)</div>
    </div>
    <p style="color: #3c4043; font-size: 14px; line-height: 1.5; margin: 0 0 22px 0;">If you generated this password, you don't need to do anything. If you didn't create it, your account may be compromised.</p>
    <div style="text-align: center; margin: 26px 0;">
      <a href="https://myaccount.google.com/apppasswords" style="background: #1a73e8; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 4px; font-weight: 500; font-size: 14px; display: inline-block;">Check activity</a>
    </div>
    <p style="color: #70757a; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #f1f3f4; padding-top: 14px;">Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043</p>
  </div>
</div>

------=_Part_18_2698726.75541008--
```

---

## 📧 EMAIL #19

```http
Delivered-To: soc-team@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp749764oia;
        Mon, 16 Nov 2026 16:20:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTg5MDE1OA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr6015122ejc.42.1731748463120;
        Mon, 16 Nov 2026 16:20:00 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NTk2ODg1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMzUxMzQ4==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of analytics.starkindustries.com designation for 52.216.144.12) smtp.mailfrom=telemetry-dispatch@analytics.starkindustries.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=analytics.starkindustries.com
Return-Path: <telemetry-dispatch@analytics.starkindustries.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 19FA3B2019-mbx
        for <soc-team@starkindustries.com>; Mon, 16 Nov 2026 16:20:00 +0000
Received: from s3-website-us-east-1.amazonaws.com (s3-website-us-east-1.amazonaws.com [52.216.144.12])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ19Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <soc-team@starkindustries.com>; Mon, 16 Nov 2026 16:20:00 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of analytics.starkindustries.com designates 52.216.144.12 as permitted sender) client-ip=52.216.144.12;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@analytics.starkindustries.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of analytics.starkindustries.com designation for 52.216.144.12) smtp.mailfrom=telemetry-dispatch@analytics.starkindustries.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=analytics.starkindustries.com
Message-ID: <20261116.199482019.912595@analytics.starkindustries.com>
Date: Mon, 16 Nov 2026 16:20:00 +0000
From: "Stark Telemetry Subdomain Portal" <telemetry@analytics.starkindustries.com>
To: soc-team@starkindustries.com
Subject: Monthly Cloud Cost Report Ready: analytics.starkindustries.com
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_19_5258777.36092509"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [52.216.144.12]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Monthly Cloud Cost Report Ready: analytics.starkindustries.com
Thread-Index: AQHb199182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_19_5258777.36092509
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

STARK CLOUD ANALYTICS & TELEMETRY

Monthly Distributed Cluster Consumption Report

Executive Leadership & Engineering Directorate,

The monthly multi-cloud telemetry and resource expenditure summary for October 2026 has been compiled across all active AWS, GCP, and on-premises GPU compute pods.

Total Billed Compute: $312,940.00 USD (+18.4% vs Sept)

Highest Utilization: Project Ultron Distributed Neural Simulators (Pod-9)

Reporting Node: analytics.starkindustries.com (S3 Static CNAME)

Open Interactive Analytics Report

Automated reporting dispatch generated by Stark Telemetry Daemon.

------=_Part_19_5258777.36092509
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 6px; background: #ffffff; padding: 24px;">
  <div style="border-bottom: 2px solid #0052cc; padding-bottom: 12px; margin-bottom: 18px;">
    <div style="font-size: 18px; font-weight: bold; color: #172b4d;">STARK CLOUD ANALYTICS &amp; TELEMETRY</div>
    <div style="font-size: 12px; color: #6b778c;">Monthly Distributed Cluster Consumption Report</div>
  </div>
  <p style="color: #172b4d; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">Executive Leadership &amp; Engineering Directorate,</p>
  <p style="color: #172b4d; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">The monthly multi-cloud telemetry and resource expenditure summary for October 2026 has been compiled across all active AWS, GCP, and on-premises GPU compute pods.</p>
  <div style="background: #f4f5f7; border-radius: 4px; padding: 16px; margin-bottom: 20px; font-size: 13px; color: #172b4d;">
    <div><strong>Total Billed Compute:</strong> $312,940.00 USD (+18.4% vs Sept)</div>
    <div style="margin-top: 6px;"><strong>Highest Utilization:</strong> Project Ultron Distributed Neural Simulators (Pod-9)</div>
    <div style="margin-top: 6px;"><strong>Reporting Node:</strong> analytics.starkindustries.com (S3 Static CNAME)</div>
  </div>
  <div style="text-align: center; margin: 26px 0;">
    <a href="https://analytics.starkindustries.com/reports/2026-11-cloud-spend.html" style="background: #0052cc; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">Open Interactive Analytics Report</a>
  </div>
  <div style="font-size: 11px; color: #6b778c; margin-top: 20px; border-top: 1px solid #ebecf0; padding-top: 12px;">
    Automated reporting dispatch generated by Stark Telemetry Daemon.
  </div>
</div>

------=_Part_19_5258777.36092509--
```

---

## 📧 EMAIL #20

```http
Delivered-To: avengers-tactical@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp323055oia;
        Mon, 16 Nov 2026 16:45:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMTk4OTY0MA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr2617301ejc.42.1731748463120;
        Mon, 16 Nov 2026 16:45:00 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NjI4MzAw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMzY5ODQw==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of shield.gov designation for 156.33.241.5) smtp.mailfrom=maria.hill@shield.gov;
       dmarc=pass (p=reject sp=reject dis=none) header.from=shield.gov
Return-Path: <maria.hill@shield.gov>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 20FA3B2019-mbx
        for <avengers-tactical@starkindustries.com>; Mon, 16 Nov 2026 16:45:00 +0000
Received: from secure-gateway01.shield.gov (secure-gateway01.shield.gov [156.33.241.5])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ20Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <avengers-tactical@starkindustries.com>; Mon, 16 Nov 2026 16:45:00 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of shield.gov designates 156.33.241.5 as permitted sender) client-ip=156.33.241.5;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@shield.gov;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of shield.gov designation for 156.33.241.5) smtp.mailfrom=maria.hill@shield.gov;
       dmarc=pass (p=reject sp=reject dis=none) header.from=shield.gov
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=shield.gov; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTU0Mzg0MA===;
        b=MTk4OTc0Mzgz
          MjA2ODg3NjQ===
Message-ID: <20261116.209482019.678838@shield.gov>
Date: Mon, 16 Nov 2026 16:45:00 +0000
From: "Maria Hill" <maria.hill@shield.gov>
To: avengers-tactical@starkindustries.com
Subject: Threat Assessment Briefing: Sokovia Accords Incident Telemetry
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_20_6531469.14498965"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [156.33.241.5]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: Threat Assessment Briefing: Sokovia Accords Incident Telemetry
Thread-Index: AQHb209182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_20_6531469.14498965
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

STRATEGIC HOMELAND INTERVENTION, ENFORCEMENT AND LOGISTICS DIVISION

CLASSIFICATION: TOP SECRET // LEVEL 7 SPECIAL ACCESS ONLY

TO: TONY STARK (CONSULTANT - AVENGERS INITIATIVE)
FROM: DEPUTY DIRECTOR MARIA HILL (OPS-HQ-TRISKELION)

SUBJECT: SOKOVIA INCIDENT TELEMETRY & ROGUE PROTOCOL EXFILTRATION

Stark, telemetry sweeps from our Eastern Europe radar arrays have picked up encrypted bursts transmitting on frequencies identical to the sub-routines recovered from the research base in Sokovia.

The handshake structure uses the neural network cipher you tested on the scepter. Director Fury has ordered a full air-gapped quarantine of your external server clusters until our crypto team validates the origin.

DIGITALLY SIGNED VIA S.H.I.E.L.D. SECURE HARDWARE TOKEN #7701-HILL
NON-PROLIFERATION PROTOCOL ENFORCED

------=_Part_20_6531469.14498965
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: 'Courier New', Courier, monospace; max-width: 600px; margin: 0 auto; border: 2px solid #1a2a3a; background: #0f1722; color: #d0d7de; padding: 24px;">
  <div style="border-bottom: 1px solid #30363d; padding-bottom: 12px; margin-bottom: 18px; text-align: center;">
    <div style="font-size: 16px; font-weight: bold; color: #58a6ff; letter-spacing: 1px;">STRATEGIC HOMELAND INTERVENTION, ENFORCEMENT AND LOGISTICS DIVISION</div>
    <div style="font-size: 12px; color: #f85149; margin-top: 4px;">CLASSIFICATION: TOP SECRET // LEVEL 7 SPECIAL ACCESS ONLY</div>
  </div>
  <p style="font-size: 13px; line-height: 1.6; margin: 0 0 14px 0;">TO: TONY STARK (CONSULTANT - AVENGERS INITIATIVE)<br>FROM: DEPUTY DIRECTOR MARIA HILL (OPS-HQ-TRISKELION)</p>
  <p style="font-size: 13px; line-height: 1.6; margin: 0 0 14px 0;">
    SUBJECT: SOKOVIA INCIDENT TELEMETRY &amp; ROGUE PROTOCOL EXFILTRATION
  </p>
  <p style="font-size: 13px; line-height: 1.6; margin: 0 0 14px 0;">
    Stark, telemetry sweeps from our Eastern Europe radar arrays have picked up encrypted bursts transmitting on frequencies identical to the sub-routines recovered from the research base in Sokovia.
  </p>
  <p style="font-size: 13px; line-height: 1.6; margin: 0 0 14px 0;">
    The handshake structure uses the neural network cipher you tested on the scepter. Director Fury has ordered a full air-gapped quarantine of your external server clusters until our crypto team validates the origin.
  </p>
  <div style="margin-top: 24px; padding-top: 14px; border-top: 1px dashed #30363d; font-size: 11px; color: #8b949e;">
    DIGITALLY SIGNED VIA S.H.I.E.L.D. SECURE HARDWARE TOKEN #7701-HILL<br>NON-PROLIFERATION PROTOCOL ENFORCED
  </div>
</div>

------=_Part_20_6531469.14498965--
```

---

# ═══════════════════════════════════════
# SECTION C — HARD (Ethical Hacker Level: Emails 21–30)
# ═══════════════════════════════════════

---

## 📧 EMAIL #21

```http
Delivered-To: finance@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp515590oia;
        Mon, 16 Nov 2026 17:15:10 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjA4OTEyMg====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr7664451ejc.42.1731748463120;
        Mon, 16 Nov 2026 17:15:10 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NjU5NzE1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzMzg4MzMy==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of xn--starkndustries-ilc.com designation for 185.193.66.19) smtp.mailfrom=exec@xn--starkndustries-ilc.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=starkіndustries.com
Return-Path: <exec@xn--starkndustries-ilc.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 21FA3B2019-mbx
        for <finance@starkindustries.com>; Mon, 16 Nov 2026 17:15:10 +0000
Received: from mx01.xn--starkndustries-ilc.com (mx01.xn--starkndustries-ilc.com [185.193.66.19])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ21Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <finance@starkindustries.com>; Mon, 16 Nov 2026 17:15:10 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of xn--starkndustries-ilc.com designates 185.193.66.19 as permitted sender) client-ip=185.193.66.19;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@starkіndustries.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of xn--starkndustries-ilc.com designation for 185.193.66.19) smtp.mailfrom=exec@xn--starkndustries-ilc.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=starkіndustries.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=starkіndustries.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTYyMTAzMg===;
        b=MjA4OTIyNjAx
          MjE3MTgyNDY===
Message-ID: <20261116.219482019.540391@starkіndustries.com>
Date: Mon, 16 Nov 2026 17:15:10 +0000
From: "Pepper Potts" <pepper.potts@starkіndustries.com>
To: finance@starkindustries.com
Subject: Urgent Escrow Transfer: Acquisition of Pym Tech Assets
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_21_7705231.90951037"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [185.193.66.19]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Urgent Escrow Transfer: Acquisition of Pym Tech Assets
Thread-Index: AQHb219182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_21_7705231.90951037
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

STARK INDUSTRIES — OFFICE OF THE CEO

Executive Disbursement & M&A Operations

Tony,

The acquisition escrow window for the Pym Technologies quantum optics laboratory assets closes at 17:00 EST today. JPMorgan Chase requires your dual-executive signature on the wire authorization schedule before they release the $85,000,000.00 USD reserve.

I have reviewed the terms with outside counsel. Please download and execute the authorization document immediately so we don't breach the closing agreement:

Download Escrow Wire Authorization (PDF)

Call me on my direct line once submitted.

Pepper Potts
Chief Executive Officer, Stark Industries
Executive Suites, Stark Tower, NY

------=_Part_21_7705231.90951037
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 6px; background: #ffffff; padding: 24px;">
  <div style="border-bottom: 1px solid #eeeeee; padding-bottom: 12px; margin-bottom: 16px;">
    <div style="font-size: 16px; font-weight: bold; color: #111111;">STARK INDUSTRIES — OFFICE OF THE CEO</div>
    <div style="font-size: 12px; color: #666666;">Executive Disbursement &amp; M&amp;A Operations</div>
  </div>
  <p style="color: #222222; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">Tony,</p>
  <p style="color: #222222; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">
    The acquisition escrow window for the Pym Technologies quantum optics laboratory assets closes at 17:00 EST today. JPMorgan Chase requires your dual-executive signature on the wire authorization schedule before they release the <strong>$85,000,000.00 USD</strong> reserve.
  </p>
  <p style="color: #222222; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">
    I have reviewed the terms with outside counsel. Please download and execute the authorization document immediately so we don't breach the closing agreement:
  </p>
  <div style="text-align: center; margin: 24px 0;">
    <a href="http://xn--starkndustries-fnb.com/escrow-wire-authorization.pdf" style="background: #111111; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">Download Escrow Wire Authorization (PDF)</a>
  </div>
  <p style="color: #222222; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">Call me on my direct line once submitted.</p>
  <div style="font-size: 13px; color: #555555; margin-top: 20px;">
    Pepper Potts<br>Chief Executive Officer, Stark Industries<br>Executive Suites, Stark Tower, NY
  </div>
</div>

------=_Part_21_7705231.90951037--
```

---

## 📧 EMAIL #22

```http
Delivered-To: devops-core@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp598028oia;
        Mon, 16 Nov 2026 17:39:50 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjE4ODYwNA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr7394264ejc.42.1731748463120;
        Mon, 16 Nov 2026 17:39:50 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NjkxMTMw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNDA2ODI0==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=none (mail-gateway01.perimeter.starkindustries.com: domain of arch-build01.internal designation for 10.0.50.45) smtp.mailfrom=jenkins@arch-build01.internal;
       dmarc=none (p=reject sp=reject dis=none) header.from=arch-build01.internal
Return-Path: <jenkins@arch-build01.internal>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 22FA3B2019-mbx
        for <devops-core@starkindustries.com>; Mon, 16 Nov 2026 17:39:50 +0000
Received: from arch-build01.internal ([10.0.50.45])
        by mail-mbx01.starkindustries.com (Postfix) with ESMTP id 22INT910284
        for <devops-core@starkindustries.com>; Mon, 16 Nov 2026 17:39:50 +0000
Received-SPF: none (mail-gateway01.perimeter.starkindustries.com: internal/unlisted sender 10.0.50.45 does not designate permitted sender hosts) client-ip=10.0.50.45;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@arch-build01.internal;
       spf=none (mail-gateway01.perimeter.starkindustries.com: domain of arch-build01.internal designation for 10.0.50.45) smtp.mailfrom=jenkins@arch-build01.internal;
       dmarc=none (p=reject sp=reject dis=none) header.from=arch-build01.internal
Message-ID: <20261116.229482019.364448@arch-build01.internal>
Date: Mon, 16 Nov 2026 17:39:50 +0000
From: "Jenkins CI Build Agent" <jenkins@arch-build01.internal>
To: devops-core@starkindustries.com
Subject: BUILD FAILED: Project JARVIS-Firmware-V4 #892 (Exit Code: 137 OOMKilled)
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_22_9979021.79545470"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [10.0.50.45]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: BUILD FAILED: Project JARVIS-Firmware-V4 #892 (Exit Code: 137 OOMKilled)
Thread-Index: AQHb229182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Internal

This is a multi-part message in MIME format.

------=_Part_22_9979021.79545470
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Jenkins CI

BUILD FAILED

Project: JARVIS-Firmware-V4 #892

Triggered by: SCM push to branch refs/heads/release/v4.2-quantum

[INFO] Compiling 412 C++ neural firmware translation units...

[INFO] Linking target binary 'jarvis-core-daemon'...

[ERROR] Container 'quantum-synthesizer' exceeded memory limit (64GB).

[ERROR] Process terminated with Exit Code: 137 (OOMKilled by Linux cgroup).

[FATAL] Build aborted after 42m 18s.

Open Blue Ocean Console Output

Jenkins Continuous Integration Server &bull; Node: arch-build01.internal (10.0.50.45)

------=_Part_22_9979021.79545470
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #dcdcdc; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="background: #d33833; padding: 16px 24px; color: #ffffff; display: flex; align-items: center; justify-content: space-between;">
    <div style="font-size: 18px; font-weight: bold;">Jenkins CI</div>
    <div style="background: #ffffff; color: #d33833; font-size: 11px; font-weight: bold; padding: 3px 8px; border-radius: 3px;">BUILD FAILED</div>
  </div>
  <div style="padding: 24px 28px;">
    <h3 style="font-size: 18px; color: #222222; margin: 0 0 8px 0;">Project: JARVIS-Firmware-V4 #892</h3>
    <div style="font-size: 13px; color: #666666; margin-bottom: 16px;">Triggered by: SCM push to branch <code>refs/heads/release/v4.2-quantum</code></div>
    <div style="background: #2b2b2b; color: #f8f8f2; border-radius: 4px; padding: 16px; font-family: monospace; font-size: 12px; line-height: 1.5; margin-bottom: 20px; overflow-x: auto;">
      [INFO] Compiling 412 C++ neural firmware translation units...<br>
      [INFO] Linking target binary 'jarvis-core-daemon'...<br>
      <span style="color: #ff5555;">[ERROR] Container 'quantum-synthesizer' exceeded memory limit (64GB).</span><br>
      <span style="color: #ff5555;">[ERROR] Process terminated with Exit Code: 137 (OOMKilled by Linux cgroup).</span><br>
      [FATAL] Build aborted after 42m 18s.
    </div>
    <div style="text-align: center; margin: 24px 0;">
      <a href="http://jenkins-internal.starkindustries.com/job/JARVIS-Firmware-V4/892/console" style="background: #007acc; color: #ffffff; text-decoration: none; padding: 12px 26px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">Open Blue Ocean Console Output</a>
    </div>
    <p style="color: #888888; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #eeeeee; padding-top: 14px;">Jenkins Continuous Integration Server &bull; Node: arch-build01.internal (10.0.50.45)</p>
  </div>
</div>

------=_Part_22_9979021.79545470--
```

---

## 📧 EMAIL #23

```http
Delivered-To: rhodey@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp220915oia;
        Mon, 16 Nov 2026 18:05:10 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjI4ODA4Ng====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr3557715ejc.42.1731748463120;
        Mon, 16 Nov 2026 18:05:10 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+NzIyNTQ1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNDI1MzE2==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of azurecomm.net designation for 51.144.102.18) smtp.mailfrom=azure-services@azurecomm.net;
       dmarc=pass (p=reject sp=reject dis=none) header.from=azurecomm.net
Return-Path: <azure-services@azurecomm.net>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 23FA3B2019-mbx
        for <rhodey@starkindustries.com>; Mon, 16 Nov 2026 18:05:10 +0000
Received: from outbound.azurecomm.net (outbound.azurecomm.net [51.144.102.18])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ23Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <rhodey@starkindustries.com>; Mon, 16 Nov 2026 18:05:10 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of azurecomm.net designates 51.144.102.18 as permitted sender) client-ip=51.144.102.18;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@azurecomm.net;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of azurecomm.net designation for 51.144.102.18) smtp.mailfrom=azure-services@azurecomm.net;
       dmarc=pass (p=reject sp=reject dis=none) header.from=azurecomm.net
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=azurecomm.net; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTc3NTQxNg===;
        b=MjI4ODE5MDM3
          MjM3NzcyMTA===
Message-ID: <20261116.239482019.755553@azurecomm.net>
Date: Mon, 16 Nov 2026 18:05:10 +0000
From: "Microsoft Identity Protection" <no-reply@azurecomm.net>
To: rhodey@starkindustries.com
Subject: Enterprise Authorization Request: "Stark Defense Tactical CAD Visualizer"
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_23_9274274.89724065"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [51.144.102.18]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Enterprise Authorization Request: "Stark Defense Tactical CAD Visualizer"
Thread-Index: AQHb239182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_23_9274274.89724065
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Microsoft

Permissions requested

Stark Defense Tactical CAD Visualizer (azurecomm.net) wants to access your Microsoft 365 enterprise account:

Requested Permissions:

Read and write access to your email and mailboxes (Mail.ReadWrite)

Read and write all files that you have access to (Files.ReadWrite.All)

Maintain access to data you have given it access to (offline_access)

Publisher is unverified. Accepting these permissions means you allow this app to use your data as specified in their terms of service.

Accept & Authorize

Microsoft Identity Platform | Enterprise Applications Directory

------=_Part_23_9274274.89724065
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #edebe9; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="padding: 20px 24px; border-bottom: 1px solid #edebe9; display: flex; align-items: center;">
    <span style="font-size: 20px; font-weight: 600; color: #0078d4;">Microsoft</span>
  </div>
  <div style="padding: 24px 28px;">
    <h3 style="font-size: 18px; color: #201f1e; margin: 0 0 10px 0;">Permissions requested</h3>
    <div style="font-size: 14px; color: #605e5c; margin-bottom: 18px;">
      <strong>Stark Defense Tactical CAD Visualizer</strong> (azurecomm.net) wants to access your Microsoft 365 enterprise account:
    </div>
    <div style="background: #f3f2f1; border-radius: 4px; padding: 16px; margin-bottom: 22px;">
      <div style="font-size: 13px; font-weight: 600; color: #323130; margin-bottom: 8px;">Requested Permissions:</div>
      <ul style="margin: 0; padding-left: 20px; font-size: 13px; color: #323130; line-height: 1.6;">
        <li>Read and write access to your email and mailboxes (<code>Mail.ReadWrite</code>)</li>
        <li>Read and write all files that you have access to (<code>Files.ReadWrite.All</code>)</li>
        <li>Maintain access to data you have given it access to (<code>offline_access</code>)</li>
      </ul>
    </div>
    <p style="font-size: 12px; color: #a19f9d; line-height: 1.4; margin: 0 0 22px 0;">
      Publisher is unverified. Accepting these permissions means you allow this app to use your data as specified in their terms of service.
    </p>
    <div style="text-align: center; margin: 24px 0;">
      <a href="https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=7c992a01-4481-49a2-9118-badc2019ff21&response_type=code&scope=Mail.ReadWrite+Files.ReadWrite.All+offline_access" style="background: #0078d4; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 2px; font-weight: 600; font-size: 14px; display: inline-block;">Accept &amp; Authorize</a>
    </div>
    <div style="font-size: 11px; color: #a19f9d; border-top: 1px solid #edebe9; padding-top: 14px; margin-top: 20px;">
      Microsoft Identity Platform | Enterprise Applications Directory
    </div>
  </div>
</div>

------=_Part_23_9274274.89724065--
```

---

## 📧 EMAIL #24

```http
Delivered-To: ietf-tls-discussion@ietf.org
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp789977oia;
        Mon, 16 Nov 2026 18:30:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjM4NzU2OA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr1707739ejc.42.1731748463120;
        Mon, 16 Nov 2026 18:30:00 +0000
ARC-Seal: i=2; a=rsa-sha256; t=1731748463; cv=pass;
        d=ietf.org; s=ietf-2024;
        b=kL94qL3+N7x9qL3+NzUzOTYw...
ARC-Message-Signature: i=2; a=rsa-sha256; c=relaxed/relaxed; d=ietf.org; s=ietf-2024;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz99281...=;
        b=mP2wL01948201KlzNDQzODA4==
ARC-Authentication-Results: i=2; mx.ietf.org;
       dkim=pass (cert.gov key 2024) header.i=@cert.gov;
       spf=pass (ietf.org: domain of alerts@cert.gov designates 149.96.220.15 as permitted sender);
       arc=pass (i=1)
ARC-Seal: i=1; a=rsa-sha256; t=1731748450; cv=none;
        d=cert.gov; s=cert-2024;
        b=A1b2C3d4E5f6G7h8MTg1MDk1Mg==...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=cert.gov; s=cert-2024;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=XyZ9018471928410928...=;
        b=JkL8910482019482MjM3ODk3Ng====
ARC-Authentication-Results: i=1; mx.cert.gov;
       spf=pass (cert.gov: domain of alerts@cert.gov designates 149.96.220.15 as permitted sender)
Return-Path: <ietf-tls-bounces@ietf.org>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 24FA3B2019-mbx
        for <ietf-tls-discussion@ietf.org>; Mon, 16 Nov 2026 18:30:00 +0000
Received: from ietf-mx.ietf.org (ietf-mx.ietf.org [4.31.198.44])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ24Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <ietf-tls-discussion@ietf.org>; Mon, 16 Nov 2026 18:30:00 +0000
Received-SPF: none (mail-gateway01.perimeter.starkindustries.com: internal/unlisted sender 4.31.198.44 does not designate permitted sender hosts) client-ip=4.31.198.44;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=fail header.i=@cert.gov;
       spf=none (mail-gateway01.perimeter.starkindustries.com: domain of ietf.org designation for 4.31.198.44) smtp.mailfrom=ietf-tls-bounces@ietf.org;
       dmarc=none (p=reject sp=reject dis=none) header.from=cert.gov
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=cert.gov; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTg1MjYwOA===;
        b=MjM4NzY3MjU1
          MjQ4MDY2OTI===
Message-ID: <20261116.249482019.191318@cert.gov>
Date: Mon, 16 Nov 2026 18:30:00 +0000
From: "US-CERT / CISA Alert Distribution" <alerts@cert.gov>
To: ietf-tls-discussion@ietf.org
Subject: [TLS-Security-WG] Vulnerability Note VU#892104: TLS 1.3 Early Data Replay
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_24_9876269.39616888"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [4.31.198.44]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: [TLS-Security-WG] Vulnerability Note VU#892104: TLS 1.3 Early Data Replay
Thread-Index: AQHb249182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_24_9876269.39616888
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

UNITED STATES COMPUTER EMERGENCY READINESS TEAM

Cybersecurity and Infrastructure Security Agency (CISA)

Vulnerability Note VU#892104: TLS 1.3 Early Data (0-RTT) Replay Vulnerability

The IETF TLS Working Group has released an advisory regarding non-idempotent HTTP request replays when utilizing TLS 1.3 0-RTT early data handshakes against misconfigured reverse proxies.

Impact: Attackers on privileged network paths can capture and replay pre-shared key handshakes to duplicate API write operations.

Mitigation: Enforce anti-replay cache headers or disable 0-RTT on state-modifying endpoints.

Technical bulletin and RFC remediation guidelines: https://www.kb.cert.org/vuls/id/892104

_______________________________________________

TLS-Security-WG mailing list -- tls-security-wg@lists.cert.gov

To unsubscribe send an email to tls-security-wg-leave@lists.cert.gov

------=_Part_24_9876269.39616888
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #d0d7de; border-radius: 6px; background: #ffffff; padding: 24px;">
  <div style="border-bottom: 2px solid #003366; padding-bottom: 12px; margin-bottom: 18px;">
    <div style="font-size: 18px; font-weight: bold; color: #003366;">UNITED STATES COMPUTER EMERGENCY READINESS TEAM</div>
    <div style="font-size: 12px; color: #555555;">Cybersecurity and Infrastructure Security Agency (CISA)</div>
  </div>
  <div style="font-size: 14px; font-weight: bold; color: #c00000; margin-bottom: 14px;">
    Vulnerability Note VU#892104: TLS 1.3 Early Data (0-RTT) Replay Vulnerability
  </div>
  <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">
    The IETF TLS Working Group has released an advisory regarding non-idempotent HTTP request replays when utilizing TLS 1.3 0-RTT early data handshakes against misconfigured reverse proxies.
  </p>
  <div style="background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 4px; padding: 14px; margin-bottom: 18px; font-size: 13px; color: #333333;">
    <div><strong>Impact:</strong> Attackers on privileged network paths can capture and replay pre-shared key handshakes to duplicate API write operations.</div>
    <div style="margin-top: 6px;"><strong>Mitigation:</strong> Enforce <code>anti-replay</code> cache headers or disable 0-RTT on state-modifying endpoints.</div>
  </div>
  <p style="color: #333333; font-size: 14px; line-height: 1.5; margin: 0 0 20px 0;">
    Technical bulletin and RFC remediation guidelines: <a href="https://www.kb.cert.org/vuls/id/892104" style="color: #0066cc;">https://www.kb.cert.org/vuls/id/892104</a>
  </p>
  <div style="border-top: 1px solid #e0e0e0; padding-top: 14px; margin-top: 20px; font-size: 11px; color: #777777; line-height: 1.4;">
    _______________________________________________<br>
    TLS-Security-WG mailing list -- tls-security-wg@lists.cert.gov<br>
    To unsubscribe send an email to tls-security-wg-leave@lists.cert.gov
  </div>
</div>

------=_Part_24_9876269.39616888--
```

---

## 📧 EMAIL #25

```http
Delivered-To: peter.parker@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp376865oia;
        Mon, 16 Nov 2026 18:54:50 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjQ4NzA1MA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr8595498ejc.42.1731748463120;
        Mon, 16 Nov 2026 18:54:50 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+Nzg1Mzc1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNDYyMzAw==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of workers.dev designation for 104.16.249.5) smtp.mailfrom=noreply@workers.dev;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
Return-Path: <noreply@workers.dev>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 25FA3B2019-mbx
        for <peter.parker@starkindustries.com>; Mon, 16 Nov 2026 18:54:50 +0000
Received: from proxy-edge.workers.dev (proxy-edge.workers.dev [104.16.249.5])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ25Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <peter.parker@starkindustries.com>; Mon, 16 Nov 2026 18:54:50 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of workers.dev designates 104.16.249.5 as permitted sender) client-ip=104.16.249.5;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@starkindustries.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of workers.dev designation for 104.16.249.5) smtp.mailfrom=noreply@workers.dev;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=starkindustries.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MTkyOTgwMA===;
        b=MjQ4NzE1NDcz
          MjU4MzYxNzQ===
Message-ID: <20261116.259482019.867350@starkindustries.com>
Date: Mon, 16 Nov 2026 18:54:50 +0000
From: "Stark Web Single Sign-On" <sso-identity@starkindustries.com>
To: peter.parker@starkindustries.com
Subject: Session Revoked: Mandatory SAML 2.0 Re-Authentication Required
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_25_8898433.19585235"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [104.16.249.5]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Session Revoked: Mandatory SAML 2.0 Re-Authentication Required
Thread-Index: AQHb259182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_25_8898433.19585235
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

STARK SECURE SINGLE SIGN-ON

Identity & Access Management (IAM) Service

Session Timeout Notification

Dear Tony Stark,

Your corporate SAML 2.0 authentication token has expired due to identity session policy SEC-99. Your active sessions across GitHub Enterprise, Jira, and AWS IAM Identity Center will be suspended within 15 minutes.

Please re-authenticate through the primary Stark identity gateway to refresh your federated claim ticket:

Re-Authenticate Corporate SSO

Stark Global Identity & Directory Enclave | Support: helpdesk@starkindustries.com

------=_Part_25_8898433.19585235
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #d3d3d3; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="background: #102a43; padding: 18px 24px; color: #ffffff;">
    <div style="font-size: 18px; font-weight: bold;">STARK SECURE SINGLE SIGN-ON</div>
    <div style="font-size: 12px; color: #829ab1; margin-top: 2px;">Identity &amp; Access Management (IAM) Service</div>
  </div>
  <div style="padding: 24px 28px;">
    <div style="background: #feecdc; border-left: 4px solid #f97316; padding: 12px 16px; margin-bottom: 18px;">
      <strong style="color: #9a3412; font-size: 14px;">Session Timeout Notification</strong>
    </div>
    <p style="color: #334e68; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">Dear Tony Stark,</p>
    <p style="color: #334e68; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">
      Your corporate SAML 2.0 authentication token has expired due to identity session policy SEC-99. Your active sessions across GitHub Enterprise, Jira, and AWS IAM Identity Center will be suspended within 15 minutes.
    </p>
    <p style="color: #334e68; font-size: 14px; line-height: 1.5; margin: 0 0 22px 0;">
      Please re-authenticate through the primary Stark identity gateway to refresh your federated claim ticket:
    </p>
    <div style="text-align: center; margin: 26px 0;">
      <a href="https://login-starkindustries.auth-gateway-proxy.workers.dev/auth/saml/sso" style="background: #0b69a3; color: #ffffff; text-decoration: none; padding: 12px 28px; border-radius: 4px; font-weight: bold; font-size: 14px; display: inline-block;">Re-Authenticate Corporate SSO</a>
    </div>
    <p style="color: #627d98; font-size: 11px; line-height: 1.4; margin: 24px 0 0 0; border-top: 1px solid #e0e0e0; padding-top: 14px;">
      Stark Global Identity &amp; Directory Enclave | Support: helpdesk@starkindustries.com
    </p>
  </div>
</div>

------=_Part_25_8898433.19585235--
```

---

## 📧 EMAIL #26

```http
Delivered-To: payroll@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp893286oia;
        Mon, 16 Nov 2026 19:20:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjU4NjUzMg====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr1727154ejc.42.1731748463120;
        Mon, 16 Nov 2026 19:20:00 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+ODE2Nzkw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNDgwNzky==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of starkindustries.com designation for 40.107.94.101) smtp.mailfrom=tony.stark@starkindustries.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=starkindustries.com
Return-Path: <tony.stark@starkindustries.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 26FA3B2019-mbx
        for <payroll@starkindustries.com>; Mon, 16 Nov 2026 19:20:00 +0000
Received: from nam04-sn1-obe.outbound.protection.outlook.com (nam04-sn1-obe.outbound.protection.outlook.com [40.107.94.101])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ26Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <payroll@starkindustries.com>; Mon, 16 Nov 2026 19:20:00 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of starkindustries.com designates 40.107.94.101 as permitted sender) client-ip=40.107.94.101;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@starkindustries.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of starkindustries.com designation for 40.107.94.101) smtp.mailfrom=tony.stark@starkindustries.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=starkindustries.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=starkindustries.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MjAwNjk5Mg===;
        b=MjU4NjYzNjkx
          MjY4NjU2NTY===
Message-ID: <20261116.269482019.894733@starkindustries.com>
Date: Mon, 16 Nov 2026 19:20:00 +0000
From: "Tony Stark" <tony.stark@starkindustries.com>
To: payroll@starkindustries.com
Subject: Confidential: Executive Stipend Wire Routing Modification
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_26_6915856.45774859"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [40.107.94.101]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Confidential: Executive Stipend Wire Routing Modification
Thread-Index: AQHb269182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_26_6915856.45774859
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Sarah,

I'm stepping into a closed-door briefing with the Swiss Energy Ministry in Geneva and my phone reception will be spotty for the next 4 hours.

I need you to process an immediate wire routing amendment for my Q4 executive research stipend ($320,000.00 USD). My previous account at Wells Fargo is undergoing an audit freeze. Remit the funds to my new entity account before 16:00 EST today:

Beneficiary: Apex Advanced Robotics LLC

Bank: Metropolitan Commercial Bank

Routing Number: 021000021

Account Number: 884019284102

Amount: $320,000.00 USD

Send me the PDF confirmation receipt here once executed. Keep this between us until the audit wraps up.

Sent from my iPad Pro

Tony Stark

------=_Part_26_6915856.45774859
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 600px; margin: 0 auto; background: #ffffff; padding: 24px; border: 1px solid #e5e5e5; border-radius: 6px;">
  <p style="color: #222222; font-size: 14px; line-height: 1.6; margin: 0 0 14px 0;">Sarah,</p>
  <p style="color: #222222; font-size: 14px; line-height: 1.6; margin: 0 0 14px 0;">
    I'm stepping into a closed-door briefing with the Swiss Energy Ministry in Geneva and my phone reception will be spotty for the next 4 hours.
  </p>
  <p style="color: #222222; font-size: 14px; line-height: 1.6; margin: 0 0 14px 0;">
    I need you to process an immediate wire routing amendment for my Q4 executive research stipend ($320,000.00 USD). My previous account at Wells Fargo is undergoing an audit freeze. Remit the funds to my new entity account before 16:00 EST today:
  </p>
  <div style="background: #f8f9fa; border: 1px solid #eaeaea; border-radius: 4px; padding: 14px; margin-bottom: 16px; font-size: 13px; color: #333333;">
    <div><strong>Beneficiary:</strong> Apex Advanced Robotics LLC</div>
    <div style="margin-top: 4px;"><strong>Bank:</strong> Metropolitan Commercial Bank</div>
    <div style="margin-top: 4px;"><strong>Routing Number:</strong> 021000021</div>
    <div style="margin-top: 4px;"><strong>Account Number:</strong> 884019284102</div>
    <div style="margin-top: 4px;"><strong>Amount:</strong> $320,000.00 USD</div>
  </div>
  <p style="color: #222222; font-size: 14px; line-height: 1.6; margin: 0 0 14px 0;">
    Send me the PDF confirmation receipt here once executed. Keep this between us until the audit wraps up.
  </p>
  <div style="margin-top: 20px; font-size: 13px; color: #555555;">
    Sent from my iPad Pro<br>
    <strong>Tony Stark</strong>
  </div>
</div>

------=_Part_26_6915856.45774859--
```

---

## 📧 EMAIL #27

```http
Delivered-To: tonystark@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp529656oia;
        Mon, 16 Nov 2026 19:45:30 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjY4NjAxNA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr7014441ejc.42.1731748463120;
        Mon, 16 Nov 2026 19:45:30 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+ODQ4MjA1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNDk5Mjg0==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of crusher-optics.com designation for 198.51.100.44) smtp.mailfrom=carl.creel@crusher-optics.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=crusher-optics.com
Return-Path: <carl.creel@crusher-optics.com>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 27FA3B2019-mbx
        for <tonystark@starkindustries.com>; Mon, 16 Nov 2026 19:45:30 +0000
Received: from mail.crusher-optics.com (mail.crusher-optics.com [198.51.100.44])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ27Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <tonystark@starkindustries.com>; Mon, 16 Nov 2026 19:45:30 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of crusher-optics.com designates 198.51.100.44 as permitted sender) client-ip=198.51.100.44;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@crusher-optics.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of crusher-optics.com designation for 198.51.100.44) smtp.mailfrom=carl.creel@crusher-optics.com;
       dmarc=pass (p=reject sp=reject dis=none) header.from=crusher-optics.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=crusher-optics.com; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MjA4NDE4NA===;
        b=MjY4NjExOTA5
          Mjc4OTUxMzg===
Message-ID: <20261116.279482019.971287@crusher-optics.com>
Date: Mon, 16 Nov 2026 19:45:30 +0000
From: "Carl Creel" <carl.creel@crusher-optics.com>
To: tonystark@starkindustries.com
Subject: RE: Precision Arc-Reactor Lens Delivery Schedule — Milestone 4
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_27_2582721.84044024"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [198.51.100.44]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: RE: Precision Arc-Reactor Lens Delivery Schedule — Milestone 4
Thread-Index: AQHb279182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_27_2582721.84044024
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Mr. Stark,

Regarding our delivery schedule for Milestone 4: the optical precision lenses successfully passed final laser interferometer tolerance tests in our cleanroom this morning.

Due to Stark defense clearance restrictions, our technical team packaged the full CAD blueprints, material safety data sheets, and calibration certificates into the secured disc image archive below:

💾 Lens_Milestone_Specs_Nov2026.iso (14.2 MB)

Disc Image Container &bull; Mount to extract certified CAD schematics

Please inspect and confirm receipt so our freight carrier can release the crated consignment from our Zurich depot.

Carl Creel
Chief Metallurgical Specialist &bull; Crusher Precision Optics

----- Quoted Previous Message -----

From: tony.stark@starkindustries.com

To: carl.creel@crusher-optics.com

Subject: RE: Precision Arc-Reactor Lens Delivery Schedule — Milestone 4

"Carl, let me know the minute the tolerance benchmarks pass. We cannot afford another refractive breakdown on the core array."

------=_Part_27_2582721.84044024
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #dcdcdc; border-radius: 4px; background: #ffffff; padding: 24px;">
  <p style="color: #222222; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">Mr. Stark,</p>
  <p style="color: #222222; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">
    Regarding our delivery schedule for Milestone 4: the optical precision lenses successfully passed final laser interferometer tolerance tests in our cleanroom this morning.
  </p>
  <p style="color: #222222; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">
    Due to Stark defense clearance restrictions, our technical team packaged the full CAD blueprints, material safety data sheets, and calibration certificates into the secured disc image archive below:
  </p>
  <div style="background: #f4f6f8; border: 1px solid #d0d7de; border-radius: 4px; padding: 14px; margin: 18px 0;">
    <div style="font-size: 14px; font-weight: bold; color: #0969da;">
      <a href="http://crusher-optics-cdn.com/delivery/Lens_Milestone_Specs_Nov2026.iso" style="color: #0969da; text-decoration: none;">💾 Lens_Milestone_Specs_Nov2026.iso (14.2 MB)</a>
    </div>
    <div style="font-size: 12px; color: #57606a; margin-top: 4px;">Disc Image Container &bull; Mount to extract certified CAD schematics</div>
  </div>
  <p style="color: #222222; font-size: 14px; line-height: 1.5; margin: 0 0 20px 0;">
    Please inspect and confirm receipt so our freight carrier can release the crated consignment from our Zurich depot.
  </p>
  <div style="font-size: 13px; color: #555555; margin-bottom: 24px;">
    Carl Creel<br>Chief Metallurgical Specialist &bull; Crusher Precision Optics
  </div>
  <div style="border-top: 1px solid #e0e0e0; padding-top: 14px; margin-top: 20px; font-size: 12px; color: #777777;">
    <div style="font-weight: bold; margin-bottom: 6px;">----- Quoted Previous Message -----</div>
    <div><strong>From:</strong> tony.stark@starkindustries.com</div>
    <div><strong>To:</strong> carl.creel@crusher-optics.com</div>
    <div><strong>Subject:</strong> RE: Precision Arc-Reactor Lens Delivery Schedule — Milestone 4</div>
    <p style="margin: 8px 0 0 0; font-style: italic;">"Carl, let me know the minute the tolerance benchmarks pass. We cannot afford another refractive breakdown on the core array."</p>
  </div>
</div>

------=_Part_27_2582721.84044024--
```

---

## 📧 EMAIL #28

```http
Delivered-To: executive-board@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp684967oia;
        Mon, 16 Nov 2026 20:10:00 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjc4NTQ5Ng====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr6077984ejc.42.1731748463120;
        Mon, 16 Nov 2026 20:10:00 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+ODc5NjIw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNTE3Nzc2==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of nl-bulletproof.net designation for 194.26.29.112) smtp.mailfrom=attacker@nl-bulletproof.net;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
Return-Path: <attacker@nl-bulletproof.net>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 28FA3B2019-mbx
        for <executive-board@starkindustries.com>; Mon, 16 Nov 2026 20:10:00 +0000
Received: from nl-bulletproof.net (nl-bulletproof.net [194.26.29.112])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ28Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <executive-board@starkindustries.com>; Mon, 16 Nov 2026 20:10:00 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of nl-bulletproof.net designates 194.26.29.112 as permitted sender) client-ip=194.26.29.112;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@starkindustries.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of nl-bulletproof.net designation for 194.26.29.112) smtp.mailfrom=attacker@nl-bulletproof.net;
       dmarc=fail (p=reject sp=reject dis=none) header.from=starkindustries.com
Message-ID: <20261116.289482019.829139@starkindustries.com>
Date: Mon, 16 Nov 2026 20:10:00 +0000
From: "Corporate Legal" <legal-audit@starkindustries.com>
To: executive-board@starkindustries.com
Subject: Legal Subpoena Compliance Notice
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_28_2975438.19725373"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [194.26.29.112]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Legal Subpoena Compliance Notice
Thread-Index: AQHb289182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_28_2975438.19725373
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

UNITED STATES DISTRICT COURT

SOUTHERN DISTRICT OF NEW YORK

OFFICIAL NOTICE OF SUBPOENA DUCES TECUM &bull; CIVIL DOCKET NO. 26-CV-8491

TO: STARK INDUSTRIES INC. &bull; LEGAL & REGULATORY COMPLIANCE DIVISION

YOU ARE HEREBY COMMANDED to produce and deposit designated server telemetry sunshine daisy meadow rainbow butterfly garden blossom morning dew summer logs and communications pertaining to automated autonomous robotics development cupcake vanilla chocolate strawberry bakery recipe dessert kitchen sugar sweet within 72 hours of receipt of this notice.

Access Court Docket & Compliance Portal

Failure to comply may result in contempt sanctions pursuant to Rule 45 of the Federal Rules of Civil Procedure.

------=_Part_28_2975438.19725373
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: 'Times New Roman', Times, serif; max-width: 600px; margin: 0 auto; border: 2px solid #222222; background: #ffffff; padding: 28px;">
  <div style="text-align: center; border-bottom: 2px solid #222222; padding-bottom: 14px; margin-bottom: 20px;">
    <div style="font-size: 20px; font-weight: bold; letter-spacing: 1px;">UNITED STATES DISTRICT COURT</div>
    <div style="font-size: 14px; font-weight: bold; margin-top: 4px;">SOUTHERN DISTRICT OF NEW YORK</div>
  </div>
  <div style="font-size: 13px; font-weight: bold; color: #990000; margin-bottom: 14px;">
    OFFICIAL NOTICE OF SUBPOENA DUCES TECUM &bull; CIVIL DOCKET NO. 26-CV-8491
  </div>
  <p style="color: #111111; font-size: 14px; line-height: 1.6; margin: 0 0 14px 0;">
    TO: STARK INDUSTRIES INC. &bull; LEGAL &amp; REGULATORY COMPLIANCE DIVISION
  </p>
  <p style="color: #111111; font-size: 14px; line-height: 1.6; margin: 0 0 16px 0;">
    YOU ARE HEREBY COMMANDED to produce and deposit designated server telemetry<span style="font-size:0px;color:transparent;display:inline;"> sunshine daisy meadow rainbow butterfly garden blossom morning dew summer </span>logs and communications pertaining to automated autonomous robotics development<span style="font-size:0px;color:transparent;display:inline;"> cupcake vanilla chocolate strawberry bakery recipe dessert kitchen sugar sweet </span>within 72 hours of receipt of this notice.
  </p>
  <div style="text-align: center; margin: 26px 0;">
    <a href="http://185.220.101.34/legal/compliance-portal.php" style="background: #000000; color: #ffffff; text-decoration: none; padding: 12px 26px; font-family: Arial, sans-serif; font-size: 13px; font-weight: bold; display: inline-block;">Access Court Docket &amp; Compliance Portal</a>
  </div>
  <p style="color: #555555; font-size: 12px; line-height: 1.5; margin: 20px 0 0 0; border-top: 1px solid #cccccc; padding-top: 14px;">
    Failure to comply may result in contempt sanctions pursuant to Rule 45 of the Federal Rules of Civil Procedure.
  </p>
</div>

------=_Part_28_2975438.19725373--
```

---

## 📧 EMAIL #29

```http
Delivered-To: devops-core@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp624748oia;
        Mon, 16 Nov 2026 20:34:50 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjg4NDk3OA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr8839907ejc.42.1731748463120;
        Mon, 16 Nov 2026 20:34:50 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+OTExMDM1...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNTM2MjY4==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=none;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of azure-prod.net designation for 185.56.83.41) smtp.mailfrom=device-auth@azure-prod.net;
       dmarc=fail (p=reject sp=reject dis=none) header.from=microsoft.com
Return-Path: <device-auth@azure-prod.net>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 29FA3B2019-mbx
        for <devops-core@starkindustries.com>; Mon, 16 Nov 2026 20:34:50 +0000
Received: from mail-relay.azure-prod.net (mail-relay.azure-prod.net [185.56.83.41])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ29Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <devops-core@starkindustries.com>; Mon, 16 Nov 2026 20:34:50 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of azure-prod.net designates 185.56.83.41 as permitted sender) client-ip=185.56.83.41;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=none header.i=@microsoft.com;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of azure-prod.net designation for 185.56.83.41) smtp.mailfrom=device-auth@azure-prod.net;
       dmarc=fail (p=reject sp=reject dis=none) header.from=microsoft.com
Message-ID: <20261116.299482019.356581@microsoft.com>
Date: Mon, 16 Nov 2026 20:34:50 +0000
From: "Microsoft Azure Cloud Shell Team" <cloudshell-auth@microsoft.com>
To: devops-core@starkindustries.com
Subject: Authenticate Azure CLI Session for Production Kubernetes Cluster
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_29_9283247.37039629"
X-Mailer: Microsoft Outlook 16.0 (Build 17928.20114)
X-Priority: 3 (Normal)
X-Originating-IP: [185.56.83.41]
X-Spam-Status: No, score=3.8 required=5.0 tests=BAYES_50,HTML_MESSAGE,SPF_FAIL,DMARC_FAIL autolearn=no
X-Spam-Score: 3.8
Thread-Topic: Authenticate Azure CLI Session for Production Kubernetes Cluster
Thread-Index: AQHb299182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_29_9283247.37039629
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

Microsoft Azure

Cloud Shell & Infrastructure CLI Security

Authenticate Azure CLI Session

An interactive administrative console session was requested on Kubernetes production cluster stark-k8s-prod-us-east.

Your One-Time Device Authentication Code:

D7X4-K99L

Code expires in 15 minutes

To sign in, use a web browser to open the official page https://microsoft.com/devicelogin and enter the code D7X4-K99L to authenticate your terminal session.

Microsoft Corporation &bull; Azure Active Directory Device Flow Identity Services

------=_Part_29_9283247.37039629
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e1dfdd; border-radius: 6px; background: #ffffff; overflow: hidden;">
  <div style="background: #0078d4; padding: 18px 24px; color: #ffffff;">
    <div style="font-size: 20px; font-weight: 600;">Microsoft Azure</div>
    <div style="font-size: 12px; color: #c7e0f4; margin-top: 2px;">Cloud Shell &amp; Infrastructure CLI Security</div>
  </div>
  <div style="padding: 24px 28px;">
    <h3 style="font-size: 17px; color: #201f1e; margin: 0 0 14px 0;">Authenticate Azure CLI Session</h3>
    <p style="color: #605e5c; font-size: 14px; line-height: 1.5; margin: 0 0 16px 0;">
      An interactive administrative console session was requested on Kubernetes production cluster <strong>stark-k8s-prod-us-east</strong>.
    </p>
    <div style="background: #f3f2f1; border: 2px solid #0078d4; border-radius: 6px; padding: 18px; text-align: center; margin: 20px 0;">
      <div style="font-size: 12px; font-weight: 600; color: #605e5c; text-transform: uppercase; letter-spacing: 0.5px;">Your One-Time Device Authentication Code:</div>
      <div style="font-size: 28px; font-weight: 700; color: #0078d4; letter-spacing: 4px; margin: 10px 0; font-family: monospace;">D7X4-K99L</div>
      <div style="font-size: 12px; color: #a19f9d;">Code expires in 15 minutes</div>
    </div>
    <p style="color: #605e5c; font-size: 14px; line-height: 1.5; margin: 0 0 20px 0;">
      To sign in, use a web browser to open the official page <a href="https://microsoft.com/devicelogin" style="color: #0078d4; font-weight: 600;">https://microsoft.com/devicelogin</a> and enter the code <strong>D7X4-K99L</strong> to authenticate your terminal session.
    </p>
    <div style="font-size: 11px; color: #a19f9d; border-top: 1px solid #edebe9; padding-top: 14px; margin-top: 22px;">
      Microsoft Corporation &bull; Azure Active Directory Device Flow Identity Services
    </div>
  </div>
</div>

------=_Part_29_9283247.37039629--
```

---

## 📧 EMAIL #30

```http
Delivered-To: soc-team@starkindustries.com
Received: by 2002:a05:6808:11c8:b0:3c9:8614:2184 with SMTP id w8csp769639oia;
        Mon, 16 Nov 2026 20:59:50 +0000
X-Google-Smtp-Source: AGHT+IVE9LRU4tMjk4NDQ2MA====
X-Received: by 2002:a17:907:7e13:b0:9a1:381e:4e21 with SMTP id y19-20020a1709077e1300b009a1381e4e21mr8996836ejc.42.1731748463120;
        Mon, 16 Nov 2026 20:59:50 +0000
ARC-Seal: i=1; a=rsa-sha256; t=1731748463; cv=none;
        d=starkindustries.com; s=arc-20260814;
        b=kL94qL3+N7x9qL3+OTQyNDUw...
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=starkindustries.com; s=arc-20260814;
        h=to:date:subject:mime-version:message-id:from:content-type:feedback-id;
        bh=9+K1n892kd1048201Klz...=;
        b=mP2wL01948201KlzNTU0NzYw==
ARC-Authentication-Results: i=1; mx.perimeter.starkindustries.com;
       dkim=pass;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of cisa.dhs.gov designation for 149.96.220.15) smtp.mailfrom=cisa-alerts@cisa.dhs.gov;
       dmarc=pass (p=reject sp=reject dis=none) header.from=cisa.dhs.gov
Return-Path: <cisa-alerts@cisa.dhs.gov>
Received: from mail-gateway01.perimeter.starkindustries.com (mail-gateway01.perimeter.starkindustries.com. [10.0.1.15])
        by mail-mbx01.starkindustries.com (Dovecot/LMTP) with ESMTP id 30FA3B2019-mbx
        for <soc-team@starkindustries.com>; Mon, 16 Nov 2026 20:59:50 +0000
Received: from smtp.cisa.dhs.gov (smtp.cisa.dhs.gov [149.96.220.15])
        by mail-gateway01.perimeter.starkindustries.com (Postfix/Amavis) with ESMTPS id 4SZ30Q1981F
        (using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
         key-exchange X25519 server-signature RSA-PSS (2048 bits))
        for <soc-team@starkindustries.com>; Mon, 16 Nov 2026 20:59:50 +0000
Received-SPF: pass (mail-gateway01.perimeter.starkindustries.com: domain of cisa.dhs.gov designates 149.96.220.15 as permitted sender) client-ip=149.96.220.15;
Authentication-Results: mail-gateway01.perimeter.starkindustries.com;
       dkim=pass header.i=@cisa.dhs.gov;
       spf=pass (mail-gateway01.perimeter.starkindustries.com: domain of cisa.dhs.gov designation for 149.96.220.15) smtp.mailfrom=cisa-alerts@cisa.dhs.gov;
       dmarc=pass (p=reject sp=reject dis=none) header.from=cisa.dhs.gov
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=cisa.dhs.gov; s=k1-2026; t=1731748450;
        h=from:to:subject:date:message-id:mime-version:content-type:feedback-id;
        bh=MjMxNTc2MA===;
        b=Mjk4NDU2NTYz
          MzA5ODM1ODQ===
Message-ID: <20261116.309482019.218215@cisa.dhs.gov>
Date: Mon, 16 Nov 2026 20:59:50 +0000
From: "Cybersecurity and Infrastructure Security Agency" <cisa-alerts@cisa.dhs.gov>
To: soc-team@starkindustries.com
Subject: CISA Alert AA26-321A: Active Exploitation of Perimeter VPN Gateways
MIME-Version: 1.0
Content-Type: multipart/alternative; boundary="----=_Part_30_4221627.46475869"
X-Mailer: Apple Mail (2.3654.120)
X-Priority: 3 (Normal)
X-Originating-IP: [149.96.220.15]
X-Spam-Status: No, score=0.1 required=5.0 tests=BAYES_00,HTML_MESSAGE,SPF_PASS,DKIM_PASS autolearn=no
X-Spam-Score: 0.1
Thread-Topic: CISA Alert AA26-321A: Active Exploitation of Perimeter VPN Gateways
Thread-Index: AQHb309182kLa901Klz/9941==
X-MS-Exchange-Organization-AuthSource: mail-gateway01.perimeter.starkindustries.com
X-MS-Exchange-Organization-AuthAs: Anonymous

This is a multi-part message in MIME format.

------=_Part_30_4221627.46475869
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

CYBERSECURITY AND INFRASTRUCTURE SECURITY AGENCY

DEFENSE CYBERSECURITY ADVISORY &bull; ALERT AA26-321A

THREAT ACTOR ALERT: Advanced Persistent Threat ULTRON

CISA and the Federal Bureau of Investigation (FBI) are releasing this joint Cybersecurity Advisory (CSA) to warn critical infrastructure operators of active automated exploitation targeting edge perimeter devices.

Associated CVEs: CVE-2026-4921 (Pre-Auth RCE), CVE-2026-4922 (Bypass)

Targeted Hardware: SonicWall & Fortinet SSL-VPN Gateway Concentrators

Signatures: Automated memory scraping injecting beaconing payload into libc

Network defenders are urged to cross-reference indicators with the CISA Known Exploited Vulnerabilities Catalog:

View CISA Known Exploited Vulnerabilities Catalog

CISA Central | 24/7 Operations Center: central@cisa.dhs.gov | cisa.gov

------=_Part_30_4221627.46475869
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: 7bit

<div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #cfd8dc; border-radius: 6px; background: #ffffff; padding: 24px;">
  <div style="border-bottom: 2px solid #003366; padding-bottom: 12px; margin-bottom: 18px;">
    <div style="font-size: 18px; font-weight: bold; color: #003366;">CYBERSECURITY AND INFRASTRUCTURE SECURITY AGENCY</div>
    <div style="font-size: 12px; color: #546e7a;">DEFENSE CYBERSECURITY ADVISORY &bull; ALERT AA26-321A</div>
  </div>
  <div style="background: #eceff1; border-left: 4px solid #b71c1c; padding: 12px 16px; margin-bottom: 18px;">
    <strong style="color: #b71c1c; font-size: 14px;">THREAT ACTOR ALERT: Advanced Persistent Threat ULTRON</strong>
  </div>
  <p style="color: #263238; font-size: 14px; line-height: 1.5; margin: 0 0 14px 0;">
    CISA and the Federal Bureau of Investigation (FBI) are releasing this joint Cybersecurity Advisory (CSA) to warn critical infrastructure operators of active automated exploitation targeting edge perimeter devices.
  </p>
  <div style="background: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 4px; padding: 14px; margin-bottom: 18px; font-size: 13px; color: #263238;">
    <div><strong>Associated CVEs:</strong> CVE-2026-4921 (Pre-Auth RCE), CVE-2026-4922 (Bypass)</div>
    <div style="margin-top: 4px;"><strong>Targeted Hardware:</strong> SonicWall &amp; Fortinet SSL-VPN Gateway Concentrators</div>
    <div style="margin-top: 4px;"><strong>Signatures:</strong> Automated memory scraping injecting beaconing payload into libc</div>
  </div>
  <p style="color: #263238; font-size: 14px; line-height: 1.5; margin: 0 0 20px 0;">
    Network defenders are urged to cross-reference indicators with the CISA Known Exploited Vulnerabilities Catalog:
  </p>
  <div style="text-align: center; margin: 24px 0;">
    <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search=AA26-321A" style="background: #003366; color: #ffffff; text-decoration: none; padding: 12px 26px; border-radius: 4px; font-weight: bold; font-size: 13px; display: inline-block;">View CISA Known Exploited Vulnerabilities Catalog</a>
  </div>
  <div style="font-size: 11px; color: #78909c; border-top: 1px solid #eceff1; padding-top: 14px; margin-top: 20px;">
    CISA Central | 24/7 Operations Center: central@cisa.dhs.gov | cisa.gov
  </div>
</div>

------=_Part_30_4221627.46475869--
```

---
