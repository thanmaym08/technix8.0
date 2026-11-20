# 🚩 ROUND 4: CITADEL CORE BREACH // CAPTURE THE FLAG (CTF)
## Master Operations & Tournament Execution Guide (Final Round)
### Setting: Operation Aegis // Postgraduate (MCA) Edition

Welcome to the command package for **Round 4: Capture The Flag (Citadel Core Breach)**. This is the grand finale of the Cyber Tournament, specifically calibrated for **MCA (Master of Computer Applications) students** with deep, multi-stage cybersecurity, cryptographic, network forensics, database exploitation, and reverse-engineering challenges.

---

## 📂 Deliverables in this Package

| File / Folder | Purpose | Intended Audience |
| :--- | :--- | :--- |
| **[`index.html`](file:///f:/CYBER%20EVENT%2023,34/Round4_Capture_The_Flag/index.html)** | Standalone, zero-dependency interactive Cyber CTF application. Features live HUD timer, progressive level gating, in-browser packet dissector, SQLi sandbox with blunt hints, Web Audio sound effects, and secret Judge HUD. | All Student Workstations |
| **[`FACILITATOR_MASTER_SOLUTIONS.md`](file:///f:/CYBER%20EVENT%2023,34/Round4_Capture_The_Flag/FACILITATOR_MASTER_SOLUTIONS.md)** | **Confidential answer key, walkthroughs, and judge manual.** Includes exact flags, SHA-256 hashes, AI prompting solutions, judge PIN (`1337`), and tie-breaker protocols. | Scoring Judges & Staff Only |
| **[`PARTICIPANT_CHALLENGE_MANUAL.md`](file:///f:/CYBER%20EVENT%2023,34/Round4_Capture_The_Flag/PARTICIPANT_CHALLENGE_MANUAL.md)** | Briefing document detailing tournament rules, tool permissions (Internet allowed, AI restricted until Level 4), and tactical objectives. | Student Teams / Printing |
| **[`TEAM_SCORE_SUBMISSION_SHEET.md`](file:///f:/CYBER%20EVENT%2023,34/Round4_Capture_The_Flag/TEAM_SCORE_SUBMISSION_SHEET.md)** | Official print-ready scoring sheet for physical verification and judge sign-offs at each station. | All Student Teams |
| **[`challenges/`](file:///f:/CYBER%20EVENT%2023,34/Round4_Capture_The_Flag/challenges/)** | Standalone challenge files for Level 2 (`citadel_traffic.pcap`) and Level 4 (`citadel_core_engine.py` and `solver.py`). | Files / Verification |

---

## 📈 Progressive Level Architecture (1000 Total Points)

| Level | Codename | Domain | Points | Tool Rules | Challenge Description |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | **The Signal Intercept** | Cryptanalysis | **100 PTS** | Web / CyberChef *(❌ No AI)* | Multi-hop conversion: RFC 1924 Ascii85 ➔ Header key extraction ➔ Vigenère decrypt. |
| **2** | **Packet Sniffer** | Network Forensics | **200 PTS** | Wireshark / Strings *(❌ No AI)* | Network PCAP analysis: Filter HTTP POST traffic / Follow TCP stream to extract JSON token. |
| **3** | **Gateway Override** | Web Security (SQLi) | **300 PTS** | Web / DevTools *(❌ No AI)* | SQL Injection authentication bypass via `' OR 1=1 --` on vulnerable login query with blunt hint. |
| **4** | **Micro-VM Core** | Reverse Eng. | **400 PTS** | 🤖 **AI PROTOCOLS AUTHORIZED** | Obfuscated 8-bit Micro-Virtual Machine bytecode; prompt AI to write reverse solver script. |

---

## 🎮 How to Run the Competition on Student Workstations

1. **Zero Setup Required:**
   - Copy the `Round4_Capture_The_Flag` folder onto each lab computer or share via USB / local network drive.
   - Double-click [`index.html`](file:///f:/CYBER%20EVENT%2023,34/Round4_Capture_The_Flag/index.html) in any modern web browser (Google Chrome, Microsoft Edge, Firefox, Brave).
   - **No web server, node, python, or internet hosting is required** to run the platform!
2. **Team Registration:**
   - Students enter their **Team Designation** and **Station #**, then click **INITIALIZE INFILTRATION**.
   - The mission clock immediately begins ticking down, and Level 1 unfolds.
3. **State Persistence:**
   - All team progress, elapsed seconds, scores, and checkpoint split times are automatically stored in browser `localStorage`. If a student accidentally refreshes or closes the browser tab, their progress resumes automatically!

---

## 🛡️ Secret Judge Telemetry HUD (How to Evaluate & Break Ties)

1. **Accessing the Judge HUD:**
   - Press **`[Ctrl] + [Shift] + [J]`** on the team's keyboard (or click the glowing shield emblem in the top header).
   - Enter Security PIN: **`1337`**.
2. **Evaluating Progress:**
   - The panel displays the exact **Checkpoint Split Times** for every level cleared by the team.
   - **Tie-Breaker Rule:** If two teams finish on the same level (e.g. both on Level 3), look at who cleared that level earliest (lower Checkpoint Timestamp). The earlier timestamp wins!
3. **Tamper-Proof Verification:**
   - The panel displays a 64-character SHA-256 cryptographic verification token computed from the team's performance metrics and a secret salt. Students cannot forge their score or completion time by editing HTML text.
4. **Exporting Scores:**
   - Click **`📋 COPY JUDGE REPORT`** to copy a clean text summary of the team's results for your master grading sheet.
