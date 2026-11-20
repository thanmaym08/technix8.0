# 📧 ROUND 2: AUTHENTIC GMAIL REPLICA // PHISHING INVESTIGATION
## Operational Facilitator & Participant Guide

Welcome to the **Authentic Gmail Replica** for **Round 2: The Social Engineering Breach**. This environment reproduces a modern Google Workspace / Gmail client where students act as SOC analysts and security investigators. Every email represents a real-world phishing campaign or authentic corporate communication, requiring participants to perform rigorous header forensics (`SPF`, `DKIM`, `DMARC`, `Return-Path`, `Reply-To`, link destinations, and IDN punycode analysis).

---

## 📁 Package Contents

| File | Purpose |
| :--- | :--- |
| **[`index.html`](file:///f:/CYBER%20EVENT%2023,34/Round2_Phishing_Webmail/index.html)** | Standalone, zero-dependency interactive Gmail interface with 30 realistic emails, authentic "Show Original" modal (RFC 5322 headers), Google Workspace "External" tags, "to me" header dropdown, and browser link status bar. |
| **[`emails_data.json`](file:///f:/CYBER%20EVENT%2023,34/Round2_Phishing_Webmail/emails_data.json)** | Complete RFC 5322 MIME dataset with headers, senders, authentication results, and rendered HTML bodies. |
| **[`TEAM_ANSWER_SHEET.md`](file:///f:/CYBER%20EVENT%2023,34/Round2_Phishing_Webmail/TEAM_ANSWER_SHEET.md)** | Ready-to-print official response sheet for student teams to record verdicts and evidence. |
| **[`ANSWER_KEY_FACILITATOR_ONLY.md`](file:///f:/CYBER%20EVENT%2023,34/Round2_Phishing_Webmail/ANSWER_KEY_FACILITATOR_ONLY.md)** | Confidential scoring sheet and deep technical explanations for judges. |

---

## 🎯 Authentic Gmail Features & Investigation Tools

1. **Google Workspace "External" Tags (For Easy Phishing Emails)**:
   - In corporate Google Workspace, emails received from external mail servers carry an authentic gray **`External`** chip.
   - For easy phishing questions (Emails 1, 3, 5, 7, 9), students see the `External` badge next to the sender in both the **inbox list** and the **email reading pane**.
   - Example: Email 1 displays `Stark IT Helpdesk <support@starkindustries.com> [External]`, providing an authentic visual clue that this claimed "internal helpdesk" email was actually sent from outside the company!

2. **Authentic RFC 5322 "📄 Show Original" Modal**:
   - The "Show original" modal displays the authentic Google Workspace delivery header: `Message ID`, `Created at`, `From`, `To`, and `Subject`.
   - **No Spoon-Fed PASS/FAIL Summary:** It does **not** pre-digest or display a pass/fail summary table.
   - Students must inspect the **Full RFC 5322 Headers** directly in the monospace viewer to locate `Authentication-Results:` (`spf=`, `dkim=`, `dmarc=`) and `Return-Path:`, exactly as real security analysts do and as instructed in the team answer sheet.

3. **Header Inspection ("to me ▼" Dropdown)**:
   - Click the small arrow beside **to me** to reveal `From`, `Reply-To`, `To`, `Date`, `Subject`, `mailed-by`, `signed-by`, and TLS encryption status.

4. **Simulated Browser Hover Status Bar**:
   - Hovering over buttons and hyperlinks in emails reveals the real destination URL in the bottom-left corner of the window (e.g., exposing bare IP addresses, fake portals, or open redirects without clicking).

5. **Clean Competition Environment**:
   - The web interface contains **zero answers, zero verdicts, and zero facilitator modes**.
   - All evaluation is verified against the printed [`ANSWER_KEY_FACILITATOR_ONLY.md`](file:///f:/CYBER%20EVENT%2023,34/Round2_Phishing_Webmail/ANSWER_KEY_FACILITATOR_ONLY.md).

---

## 📝 Participant Workflow

1. Students open [`index.html`](file:///f:/CYBER%20EVENT%2023,34/Round2_Phishing_Webmail/index.html) in their browser.
2. For each email (`#1` to `#30`), students analyze the email content, sender info, and click **"Show original"** to inspect the RFC 5322 headers.
3. Students record their verdicts (✅ Legitimate vs 🚩 Malicious) and technical justifications on their printed [`TEAM_ANSWER_SHEET.md`](file:///f:/CYBER%20EVENT%2023,34/Round2_Phishing_Webmail/TEAM_ANSWER_SHEET.md).
4. Organizers collect and grade the sheets using [`ANSWER_KEY_FACILITATOR_ONLY.md`](file:///f:/CYBER%20EVENT%2023,34/Round2_Phishing_Webmail/ANSWER_KEY_FACILITATOR_ONLY.md).
