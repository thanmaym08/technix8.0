# 🛡️ ROUND 4: CITADEL CORE BREACH // PARTICIPANT MISSION MANUAL
## Operation Aegis — The Final Showdown (Capture The Flag)
### Target Track: MCA / Postgraduate Cybersecurity Symposium

---

## 🎯 1. Mission Briefing
Welcome to the grand finale of the Cyber Tournament: **Operation Aegis — Citadel Core Breach**. 

You are stationed at an infiltration terminal connected to the central Citadel network. Your mission is to breach **4 progressive security levels**, decrypt intercepted transmissions, analyze network packet captures, exploit database authentication portals, and reverse-engineer a custom virtual machine before the countdown timer hits `00:00`.

---

## ⚖️ 2. Rules of Engagement & Tool Permissions

### 🌐 The Internet Rule (Levels 1 to 4):
* You are **PERMITTED** to use web search engines (Google), technical documentation, CyberChef, Wireshark, online format converters, command-line tools, and Python across **ALL levels**.

### 🤖 The AI Assistant Rule (STRICTLY ENFORCED):
* **Levels 1, 2, and 3:**
  - The use of **Generative AI, Large Language Models (LLMs), or AI chatbots** (including ChatGPT, Claude, Microsoft Copilot, Gemini, Perplexity, or AI code assistants) is **STRICTLY PROHIBITED**.
  - Any team observed using AI tools during Levels 1–3 will receive an **immediate penalty or disqualification**.
* **Level 4 (The Boss Level):**
  - **AI SANCTION UNLOCKED!** 🤖
  - Upon clearing Level 3, the interface will flash an alert granting full AI authorization.
  - On Level 4, you are **officially permitted and encouraged to use Generative AI tools** to assist in reverse-engineering complex virtual machine logic and writing solver scripts!

---

## ⏱️ 3. Tournament Structure & Progression

1. **Linear Progression:** All teams begin at **Level 1**. You cannot access Level 2 until Level 1's flag has been validated.
2. **Scoring Architecture (60 Total Points):**
   * **Level 1 (The Signal Intercept):** **5 Points**
   * **Level 2 (The Packet Sniffer):** **10 Points**
   * **Level 3 (Gateway Override):** **15 Points**
   * **Level 4 (Micro-VM Core):** **30 Points**
   * **Total Maximum Score:** **60 Points**
3. **Flag Format:** All authentic flags adhere to the standard format:
   ```text
   AEGIS{flag_text_here}
   ```
   *(Flags are case-insensitive: both capital and small letters, such as `AEGIS{...}` or `aegis{...}`, as well as the inner key from online decoders, are accepted).*
4. **Live Checkpoint Split Timers:**
   * Every time your team submits a valid flag, the mission clock records your **Checkpoint Elapsed Time** and **Split Duration**.
   * If two teams tie on score at the end of the round, the team that reached that milestone with the **earliest Checkpoint Split Time wins the tie**!

---

## 🗺️ 4. Level Overviews & Tactical Objectives

### 🟢 LEVEL 1: THE SIGNAL INTERCEPT (5 PTS)
* **Objective:** Decode an intercepted drone telemetry transmission burst.
* **Permitted:** Web search, CyberChef, online decoders. *(❌ No AI)*
* **Briefing:**
  - The raw burst is encoded using RFC 1924 **Ascii85 (Base85)**.
  - Decoding the representation layer reveals an encrypted polyalphabetic ciphertext.
  - Inspect the transmission header for the synchronization key (`TITANIUM`) and perform **Vigenère decryption** to reveal the flag!

---

### 🟡 LEVEL 2: THE PACKET SNIFFER (10 PTS)
* **Objective:** Analyze an intercepted network packet capture (`citadel_traffic.pcap`).
* **Permitted:** Web search, Wireshark, Strings, Packet Analyzers. *(❌ No AI)*
* **Briefing:**
  - Download `citadel_traffic.pcap` or use the in-browser packet dissector table.
  - Web traffic over standard HTTP (port 80) is unencrypted.
  - Inspect outgoing client request streams to locate the JSON authorization token containing the cleartext flag!

---

### 🟠 LEVEL 3: GATEWAY OVERRIDE (15 PTS)
* **Objective:** Bypass the Citadel login terminal using SQL Injection.
* **Permitted:** Web search, Browser, SQL Reference. *(❌ No AI)*
* **Briefing:**
  - The login portal queries an SQL database:
    `SELECT * FROM admin_users WHERE username = '$user' AND password = '$password'`
  - Construct an SQL injection string in the Administrator Username field to evaluate the condition to true and reveal the admin access flag!

---

### 🔴 LEVEL 4: THE MICRO-VM CORE — BOSS LEVEL (30 PTS)
* **Objective:** Reverse-engineer a custom 8-bit Micro-Virtual Machine bytecode routine.
* **Permitted:** 🤖 **ALL GENERATIVE AI / LLMs (ChatGPT, Claude, Gemini) AUTHORIZED!**
* **Briefing:**
  - Download or copy `citadel_core_engine.py`.
  - The script executes a 4-stage pipeline per byte against `TARGET_STATE_REGISTER`.
  - Prompt your AI assistant to analyze the MicroVM operations, invert each stage, and generate a Python solver script that extracts the master key!

---

## 🏆 5. Mission Completion & Grand Champion Surprise
When you crack Level 4, the **Victory Screen** unlocks the **Citadel Grand Champion Honors**, featuring:
* Total Score (`60 / 60 PTS`)
* Final Infiltration Time
* Official Tamper-Proof Cryptographic Token
* **Exclusive Grand Champion Prize Claim Token** (`AEGIS-0804-CHAMPION-OVERRIDE`) to claim your symposium award!
* An interactive **Matrix God-Mode** celebration button!
