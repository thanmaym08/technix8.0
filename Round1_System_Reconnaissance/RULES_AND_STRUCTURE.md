# ⚡ ROUND 1: SYSTEM RECONNAISSANCE (THE QUIZ)
## Operation Ultron — Rapid Intelligence & Perimeter Breach
### Official Event Guidelines & Scoring Architecture

---

## 🎯 1. Overview & Tactical Objective
**Round 1: System Reconnaissance** serves as the initial high-intensity elimination filter of the cyber event. Designed in the aesthetic and narrative lore of **Operation ULTRON / S.H.I.E.L.D. Cyber Defense**, this round evaluates a team's theoretical depth, real-time diagnostic intuition, offensive exploitation knowledge, and split-second decision-making.

> *"I'm going to tear you apart... from the inside."* — **ULTRON**

Teams are tasked with answering **30 progressive challenge questions** within a strict **45-second window per question**. Questions begin with core security reconnaissance and ramp up to complex zero-days, memory corruption, side-channel attacks, and autonomous AI subversion.

---

## ⏱️ 2. Execution Parameters & Format
* **Total Questions:** 30 Questions
* **Time Allocation:** **30 Seconds per Question** (Hard countdown with auditory & visual warnings)
* **Execution Options:**
  1. **Auditorium Screen Display:** Projected using the custom, zero-dependency `index.html` presentation console featuring real-time HUD timer, dynamic question cards, sound cues, and quizmaster controls.
  2. **Interactive Platform:** Pre-exported formats ready for instant import into **Quizizz**, **Kahoot!**, or **Google Forms**.
* **Advancement Condition:** Fast-paced initial filter. All teams actively participate to establish baseline seeding or tier elimination for Round 2.

---

## 📈 3. Progressive Scoring & Difficulty Matrix
Unlike standard flat-score quizzes, Round 1 implements a **progressive risk-reward scale** where each 5-question block increases in complexity and point yield:

| Question Block | Question Range | Difficulty Level | Points / Marks Each | Block Total | Cumulative Total | Core Focus & Marvel/Ultron Lore Link |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Tier 1: Perimeter Scan** | Q01 – Q05 | Easy / Warm-up | **1 Mark** | 5 Marks | 5 Marks | HTTPS port 443, CIA Availability, **Age of Ultron: J.A.R.V.I.S.**, Trojan Horse, Multi-Factor Authentication (MFA) |
| **Tier 2: Infiltration Vector** | Q06 – Q10 | Easy-Medium | **2 Marks** | 10 Marks | 15 Marks | `ping` & ICMP reachability, **Age of Ultron: Vibranium**, Whaling executive phishing, IDS vs IPS, Symmetric encryption keys |
| **Tier 3: Core Penetration** | Q11 – Q15 | Medium | **3 Marks** | 15 Marks | 30 Marks | SQL Injection auth bypass, **Age of Ultron: Oslo NEXUS Internet Hub**, Stored XSS, ARP Spoofing / MITM, Password Salting vs Rainbow Tables |
| **Tier 4: Deep Subversion** | Q16 – Q20 | Medium | **4 Marks** | 20 Marks | 50 Marks | Evil Twin Wi-Fi AP, **Age of Ultron: F.R.I.D.A.Y.**, Botnet DDoS attacks, Honeypots, Asymmetric Public Key encryption |
| **Tier 5: Perimeter Breach** | Q21 – Q25 | Medium-Hard | **5 Marks** | 25 Marks | 75 Marks | Stack Buffer Overflow, **Age of Ultron: The Mind Stone**, Zero-Day vulnerabilities, Nmap SYN Half-Open scan, Pass-the-Hash (PtH) |
| **Tier 6: The Singularity** | Q26 – Q30 | Hard / Climax | **6 Marks** | 30 Marks | **30 Marks** | ASLR memory randomization, **Age of Ultron: The Vision burning Ultron out of the net**, Ring 0 Kernel Rootkits, Cloud IMDS SSRF, BGP Route Hijacking |

> **Total Potential Score:** **30 Marks**

---

## ⚖️ 4. Rules of Engagement for Participants
1. **Zero External Devices:** No smartphones, laptops, smartwatch browsers, or external cellular modems are permitted unless the quiz is officially conducted via the approved Kahoot/Quizizz platform.
2. **Strict Time Limit:** Answers submitted after the 45-second timer hits zero (`00:00`) receive **0 marks**.
3. **Negative Marking:** Optional at the discretion of the organizing committee (Standard: No negative marks to encourage rapid risk-taking; Tournament Mode: -1 Mark for incorrect answers on Tiers 4–6).
4. **Tie-Breaker Rule:**
   - In case of a point tie, the team with the highest marks in **Tier 6 (The Singularity)** advances.
   - If still tied, shortest cumulative response latency (fastest submission) determines the victor.

---

## 🖥️ 5. Presenter & Stage Control Hotkeys (`index.html`)
The included interactive visual dashboard has built-in keyboard controls for the stage facilitator:

* `[Right Arrow]` or `[N]` : Advance to Next Question
* `[Left Arrow]` or `[P]` : Return to Previous Question
* `[Spacebar]` : Pause / Resume the 30-Second Countdown Timer
* `[R]` : Reset 30-Second Timer to full
* `[A]` : Reveal the Correct Answer + Facilitator Dossier Panel
* `[M]` : Mute / Unmute Cyber Audio SFX (Timer tick, Alarm, Gong, Win fanfares)
* `[F]` : Toggle Fullscreen Projection Mode
* `[Esc]` : Close Overlays / Return to Slide View

---

## 📁 6. Folder & Asset Structure
```
Round1_System_Reconnaissance/
├── index.html                   # High-tech interactive Ultron-themed projector presentation app
├── QUESTION_BANK_MASTER.md      # Complete 30-question bank with deep technical analysis & trap guides
├── FACILITATOR_CHEAT_SHEET.md   # Quick 2-page print-ready answer key & scoring sheet for judges
├── QUIZ_IMPORT_DATA.json        # Machine-readable JSON for web engines & automated scoring
├── QUIZ_IMPORT_DATA.csv         # Universal CSV format for Quizizz / Kahoot / Canvas
└── RULES_AND_STRUCTURE.md       # Event brochure, tournament rules & scoring matrix
```
