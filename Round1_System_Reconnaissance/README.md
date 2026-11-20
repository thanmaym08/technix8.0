# ⚡ ROUND 1: SYSTEM RECONNAISSANCE // OPERATION ULTRON
## Master Host & Facilitator Operations Guide (Competition Edition)

Welcome to the command package for **Round 1: System Reconnaissance**. This package is configured for **strict competitive examination integrity** (answers are suppressed on screen, options are balanced to prevent guessing, and 6 spare questions are included for tie-breakers).

---

## 📂 Deliverables in this Package

| File | Purpose | Intended Audience |
| :--- | :--- | :--- |
| **[`index.html`](file:///f:/CYBER%20EVENT%2023,34/Round1_System_Reconnaissance/index.html)** | **Zero-Reveal stage presentation console**. 45s HUD countdown ring, procedural audio warnings, 4 balanced option cards, time's up banner. (Answers suppressed!). | Stage Screen / Projector |
| **[`QUESTION_BANK_PARTICIPANT_VIEW.md`](file:///f:/CYBER%20EVENT%2023,34/Round1_System_Reconnaissance/QUESTION_BANK_PARTICIPANT_VIEW.md)** | Clean student copy containing all 36 questions and 4 options. **Strictly NO answers or hints.** | Students / Printing |
| **[`TEAM_ANSWER_SHEET.md`](file:///f:/CYBER%20EVENT%2023,34/Round1_System_Reconnaissance/TEAM_ANSWER_SHEET.md)** | Ready-to-print student response sheet for teams to fill in their answers for evaluation committee verification. | All Student Teams |
| **[`FACILITATOR_CHEAT_SHEET.md`](file:///f:/CYBER%20EVENT%2023,34/Round1_System_Reconnaissance/FACILITATOR_CHEAT_SHEET.md)** | **Confidential 2-page answer key & trap guide** for all 30 main questions + 6 spare tie-breakers. | Judges & Scoring Panel Only |
| **[`QUESTION_BANK_MASTER.md`](file:///f:/CYBER%20EVENT%2023,34/Round1_System_Reconnaissance/QUESTION_BANK_MASTER.md)** | Complete 36-question reference with deep technical rationales, lore tie-ins, and distractor trap analysis. | Technical Leads & Organizers |
| **[`QUIZ_IMPORT_DATA.csv`](file:///f:/CYBER%20EVENT%2023,34/Round1_System_Reconnaissance/QUIZ_IMPORT_DATA.csv)** | Pre-formatted spreadsheet of all 36 questions ready for 1-click import into **Quizizz**, **Kahoot!**, or **Google Forms**. | Quiz Platform Manager |
| **[`QUIZ_IMPORT_DATA.json`](file:///f:/CYBER%20EVENT%2023,34/Round1_System_Reconnaissance/QUIZ_IMPORT_DATA.json)** | Machine-readable JSON database with questions, option sets, tier tags, and points. | Web Devs / Automations |
| **[`RULES_AND_STRUCTURE.md`](file:///f:/CYBER%20EVENT%2023,34/Round1_System_Reconnaissance/RULES_AND_STRUCTURE.md)** | Official tournament guidelines, brochure specifications, pacing rules, and tie-breaker mechanics. | All Participants & Staff |

---

## 📈 Progressive Scoring Architecture (30 Total Marks (1 Mark per Question))

The main competition consists of **30 questions (45 seconds each)** scaling in difficulty and marks:

* **Tier 1 (Questions 01 – 05):** **1 Mark each** (5 Marks) — Core fundamentals: HTTPS port 443, CIA Availability, **🎬 Movie: J.A.R.V.I.S.**, Trojan Horse malware, Multi-Factor Authentication (MFA).
* **Tier 2 (Questions 06 – 10):** **2 Marks each** (10 Marks) — Networking basics: `ping` & ICMP, **🎬 Movie: Vibranium**, Whaling executive phishing, IDS vs IPS, Symmetric encryption keys.
* **Tier 3 (Questions 11 – 15):** **3 Marks each** (15 Marks) — Web & LAN: SQL Injection, **🎬 Movie: Oslo NEXUS Internet Hub**, Stored XSS, ARP Spoofing / MITM, Password Salting vs Rainbow Tables.
* **Tier 4 (Questions 16 – 20):** **4 Marks each** (20 Marks) — Wireless & Defense: Evil Twin Wi-Fi, **🎬 Movie: F.R.I.D.A.Y.**, Botnet DDoS attacks, Honeypots, Asymmetric Public Key encryption.
* **Tier 5 (Questions 21 – 25):** **5 Marks each** (25 Marks) — System & Network Exploits: Stack Buffer Overflow, **🎬 Movie: The Mind Stone**, Zero-Day vulnerabilities, Nmap SYN Half-Open scan, Windows Pass-the-Hash (PtH).
* **Tier 6 (Questions 26 – 30):** **6 Marks each** (30 Marks) — Advanced Security & Climax: ASLR memory randomization, **🎬 Movie: The Vision burning Ultron out of the net**, Ring 0 Kernel Rootkits, Cloud IMDS SSRF, BGP Route Hijacking.

> **Main Competition Maximum Score:** **30 Marks**

---

## 🛡️ Spare / Tie-Breaker Reserve Pool (Questions 31 – 36)

To resolve ties fairly without reusing questions, 6 dedicated spare questions (1 for each tier value) are included:
* **SP 31 (1 Mark):** Transport Layer Security (TLS) replacing SSL.
* **SP 32 (2 Marks):** *Age of Ultron Movie*: Sokovia drone base.
* **SP 33 (3 Marks):** Physical Security: Tailgating / Piggybacking.
* **SP 34 (4 Marks):** *Age of Ultron Movie*: Dr. Helen Cho's Regeneration Cradle.
* **SP 35 (5 Marks):** Cryptographic Attacks: Hash Collision (Birthday Paradox).
* **SP 36 (6 Marks):** Enterprise Architecture: Zero Trust Architecture (ZTA).

---

## 🎮 How to Run the Presentation (`index.html`)

1. **Launch in Browser:** Double-click `index.html` in Chrome, Edge, Firefox, or Brave.
2. **Zero Reveal Guarantee:** The app will **NEVER reveal correct answers on screen**. Clicking an option simply toggles a neutral cyan highlight for interactive focus without indicating whether it is correct or incorrect.
3. **Cinematic Middle Slide Transition Sequence:**
   * When the 45-second timer hits `00`, the alarm gong sounds and a brief alert appears: `⚠️ TIME'S UP! ADVANCING TO NEXT QUESTION SLIDE...`.
   * After 1.5 seconds, the presentation **automatically shows the Middle Transition Slide** (e.g. `QUESTION 02 // TIER 1 // +1 MARK // LORE CONTEXT`).
   * An animated countdown bar ticks down on the middle slide for **3 seconds** (`INITIALIZE IN 3s... 2s... 1s...`).
   * The app then automatically transitions into the **Question Slide**, resetting and starting the 45-second timer immediately!
   * Presenters can skip the 3s wait on the middle slide anytime by pressing `[Spacebar]` or clicking `INITIALIZE SCAN ➔`.
4. **Auto-Advance Toggle:** Presenters can pause the countdown at any time using `[Spacebar]` or toggle auto-advancement using the `⚡ AUTO-NEXT: ON/OFF` button in the top HUD.
5. **Stage Hotkeys:**
   - **`[Spacebar]`** : Pause / Resume 45s countdown.
   - **`[R]`** : Reset timer back to 45s.
   - **`[➔]` / `[N]`** : Advance to next question / transition card.
   - **`[⬅]` / `[P]`** : Return to previous question.
   - **`[F]`** : Toggle borderless Fullscreen.
   - **`[M]`** : Toggle sound effects on/off.
   - **`[JUMP]`** button : Opens the Mission Matrix to jump to any question (Q01–Q30 Main or Q31–Q36 Spares).
