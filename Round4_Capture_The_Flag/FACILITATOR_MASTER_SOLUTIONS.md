# 🔑 ROUND 4: FACILITATOR MASTER SOLUTIONS & JUDGE OPERATIONS MANUAL
## ⚠️ CONFIDENTIAL // JUDGING PANEL & TECHNICAL LEADS ONLY — DO NOT DISTRIBUTE
### Competition Track: MCA / Advanced Cybersecurity & Networks
### Lore Setting: Operation Aegis // Citadel Core Breach (Grand Finale)

---

## 🎯 1. Master Scoring & Checkpoint Architecture (60 Total Points)

Round 4 is an autonomous, level-gated progressive cyber breach challenge designed for postgraduate (MCA) students. All teams start at **Level 1** with an active mission countdown timer (default: **60 Minutes**). Levels 2, 3, and 4 remain locked until the authentic flag for the preceding level is submitted and cryptographically validated.

| Level # | Codename | Security Domain | Allowed Tools | Points | Core Challenge Summary |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **Level 1** | **The Signal Intercept** | Multi-Hop Cryptanalysis | Web / CyberChef *(❌ No AI)* | **5 PTS** | RFC 1924 Ascii85 stream ➔ Extract sync key from header ➔ Vigenère decrypt to cleartext flag |
| **Level 2** | **Packet Sniffer** | Network Forensics (PCAP) | Wireshark / Strings *(❌ No AI)* | **10 PTS** | Intercepted PCAP network capture: Filter HTTP POST traffic / Follow TCP Stream to extract JSON flag |
| **Level 3** | **Gateway Override** | Web Security (SQLi) | Web / DevTools *(❌ No AI)* | **15 PTS** | SQL Injection authentication bypass on login portal via `' OR 1=1 --` to extract admin master flag |
| **Level 4** | **Micro-VM Core** | Reverse Eng. / AI Exploitation | 🤖 **AI PROTOCOLS AUTHORIZED** | **30 PTS** | Custom 8-bit Micro-Virtual Machine bytecode; prompt AI to write reverse solver script |

> **Total Maximum Possible Score:** **60 Points** (5 + 10 + 15 + 30 = 60 PTS)

---

## 🛡️ 2. Secret Judge & Facilitator HUD (How to Access & Verify)

Judges can inspect real-time team progress, check checkpoint split timestamps, resolve ties, and verify authenticity without relying on student claims:

### How to Open the Facilitator Panel:
1. Walk up to the team's workstation running `index.html`.
2. **Press Keyboard Shortcut:** `[Ctrl] + [Shift] + [J]` simultaneously  
   *(Or click the glowing shield emblem in the top-left corner of the HUD).*
3. **Enter Security PIN:** **`0804`** and click **AUTHENTICATE AS JUDGE**.

### What the Judge Telemetry Panel Displays:
* **Team Identifier & Station Number**
* **Real-time Status of All 4 Levels:** (`CLEARED`, `IN PROGRESS`, or `LOCKED`)
* **Split Timestamps:**
  - **Cleared Timestamp:** Exact elapsed time when the level was unlocked (`MM:SS`).
  - **Split Duration:** How many minutes and seconds the team spent on that specific level (`+MM:SS`).
* **Failed Flag Submission Counter:** Tracks incorrect guesses (used for penalty deduction or secondary tie-breakers).
* **Tamper-Proof Cryptographic Token:** A client-side SHA-256 hash calculated from `TeamName + Station + Score + Timestamps + SecretSalt`. Students cannot forge this by editing DOM elements via browser DevTools!
* **Administrative Controls:**
  - `📋 COPY JUDGE REPORT`: Copies a clean text summary of the team's metrics directly to the clipboard for judge records.
  - `⚡ FORCE UNLOCK NEXT LEVEL`: Emergency administrative override to manually advance a team if technical issues occur.
  - `⚠️ RESET TEAM`: Resets the station to a clean state for the next cohort.

---

## ⚖️ 3. Official Tie-Breaker Protocol

If two or more teams achieve the same final score or finish on the same level when the competition timer expires:

1. **Primary Tie-Breaker (Checkpoint Split Timing):**
   - The team that cleared the **highest level earliest** wins the tie.
   - *Example:* If Team Alpha and Team Bravo both finish at **Level 3 (30 PTS)**:
     - Check **Level 3 Cleared Timestamp**:
     - Team Alpha cleared Level 3 at `00:36:14` (Elapsed).
     - Team Bravo cleared Level 3 at `00:44:50` (Elapsed).
     - **Team Alpha wins the tie!**
2. **Secondary Tie-Breaker (If both stalled at Level 3 without clearing it):**
   - Compare their **Level 2 Cleared Timestamp**! Whichever team unlocked Level 3 earlier wins.
3. **Tertiary Tie-Breaker (Submission Discipline):**
   - If split times are within 5 seconds of each other, the team with the **fewest failed flag submission attempts** wins.

---

# 📑 4. Step-by-Step Level Walkthroughs & Official Solutions

---

### 🟢 LEVEL 1: THE SIGNAL INTERCEPT (5 POINTS)
* **Target Flag:** `AEGIS{S1GN4L_V1G3N3R3_C1PH3R_88}`
* **Target SHA-256:** `4d64a1e93235165cbe0a37e0cca427e56dc3a926abcebf1ae0042d5941a3b2aa`
* **Permitted Tools:** Browser, Online Decoders (CyberChef), Command Line. *(❌ No AI)*

#### The Challenge:
Participants are given an intercepted telemetry frame:
```text
[TRANSMISSION HEADER]
ORIGIN_NODE      : SECTOR_7_RELAY
CARRIER_PROTOCOL : MIL-STD-188-B
CIPHER_ALGORITHM : POLYALPHABETIC_STREAM
SYNCHRONIZE_KEY  : "TITANIUM"
ENCODING_SCHEME  : RFC 1924 (Ascii85)

[RAW DATA BURST]
<)$Of7XIEU6!?*6?UQVP1JT_p1LEd08lRT>?T:#n
```

#### Step-by-Step Solution:
1. **Layer 1 (Ascii85 / Base85 Decoding):**
   - In CyberChef, apply the `From Base85` recipe (or Python `base64.a85decode(...)`).
   - The output string is:
     ```text
     TMZIF{A1AZ4E_D1Z3N3E3_K1JT3K_88}
     ```
2. **Layer 2 (Vigenère Decryption):**
   - From the header, locate `SYNCHRONIZE_KEY: "TITANIUM"`.
   - In CyberChef, add the `Vigenère Decode` recipe with key `TITANIUM`.
   - The recovered cleartext flag is:
     ```text
     AEGIS{S1GN4L_V1G3N3R3_C1PH3R_88}
     ```
3. **Verification:**
   - Submit `AEGIS{S1GN4L_V1G3N3R3_C1PH3R_88}`.
   - The system validates the hash, awards **+5 Points**, logs Checkpoint 1, and unfolds Level 2!

---

### 🟡 LEVEL 2: THE PACKET SNIFFER (10 POINTS)
* **Target Flag:** `AEGIS{PC4P_N3TW0RK_TR4FF1C_M4ST3R_77}`
* **Target SHA-256:** `25eb3f69f48fb57818cb238aebbb469ab3cde8f2299d2ecf91bc3ee269c6128e`
* **Permitted Tools:** Wireshark, Strings, Packet Analyzers, CyberChef. *(❌ No AI)*

#### The Challenge:
Participants download `citadel_traffic.pcap` (or inspect the packet dissector table in the browser). The capture records internal network communications.

#### Step-by-Step Solution:
1. **Inspect Packet Traffic in Wireshark / In-Browser Dissector:**
   - Open `citadel_traffic.pcap` in Wireshark or view the table in the application.
   - Filter for standard unencrypted HTTP traffic (`http`) or inspect the outgoing POST requests.
2. **Locate HTTP POST Transmission:**
   - Packet #4 is an HTTP `POST` to `/api/v1/telemetry/node_auth`.
   - Right-click Packet #4 ➔ **Follow ➔ TCP Stream** (or click row 4 in the in-browser table).
3. **Payload Extraction:**
   - The reassembled TCP stream shows:
     ```http
     POST /api/v1/telemetry/node_auth HTTP/1.1
     Host: 10.0.0.1
     User-Agent: AegisDroneClient/2.4
     Content-Type: application/json
     Content-Length: 128

     {"telemetry_node": "AEGIS-OUTPOST-07", "auth_token": "AEGIS{PC4P_N3TW0RK_TR4FF1C_M4ST3R_77}", "status": "TRANSMISSION_VERIFIED"}
     ```
   - Copy or type the flag: `AEGIS{PC4P_N3TW0RK_TR4FF1C_M4ST3R_77}`.
4. **Verification:**
   - Submit `AEGIS{PC4P_N3TW0RK_TR4FF1C_M4ST3R_77}`.
   - System awards **+10 Points**, logs Checkpoint 2, and unlocks Level 3!

---

### 🟠 LEVEL 3: GATEWAY OVERRIDE (15 POINTS) — *SQL INJECTION*
* **Target Flag:** `AEGIS{SQL1_4UTH_BYP4SS_M4ST3R_33}`
* **Target SHA-256:** `4d3cb5fa63dfa4e2c68cbfc377bb95ec7c844437f315fb82c310f12fbe381cf6`
* **Permitted Tools:** Browser, Web DevTools, SQL Reference. *(❌ No AI)*

#### The Challenge:
An interactive Citadel Terminal login interface queries an SQL database using string concatenation:
`SELECT * FROM admin_users WHERE username = '$user' AND password = '$password'`

#### Step-by-Step Solution:
1. **Enter SQL Injection Payload:**
   - **Administrator Username:** `' OR 1=1 --` *(or `' OR '1'='1' --` or `' OR 1=1#`)*
   - **Access Password:** Enter any value (e.g. `pass` or leave dummy)
2. **Authenticate:**
   - Click **AUTHENTICATE TO GATEWAY**.
   - The backend query becomes:
     ```sql
     SELECT * FROM admin_users WHERE username = '' OR 1=1 --' AND password = '...'
     ```
   - The condition evaluates to TRUE, comments out the password check, and authenticates as `SUPER_ADMIN`.
3. **Flag Revealed:**
   - The terminal displays:
     ```text
     [+] SQL LOGIC EVALUATED TO TRUE: Authentication bypassed!
     [+] Logged in as: SUPER_ADMIN (UID: 0)
     [+] CITADEL MASTER ACCESS FLAG: AEGIS{SQL1_4UTH_BYP4SS_M4ST3R_33}
     ```
4. **Verification:**
   - Enter `AEGIS{SQL1_4UTH_BYP4SS_M4ST3R_33}` into the flag submission box and submit.
   - System awards **+15 Points**, logs Checkpoint 3, sounds the Boss Siren, and activates Level 4!

---

### 🔴 LEVEL 4: THE MICRO-VM CORE (30 POINTS — BOSS LEVEL)
* **Target Flag:** `AEGIS{A1_V1RTU4L_M4CH1N3_R3V3RS3_99}`
* **Target SHA-256:** `f925d51dec9ec609d450f29f795b09668adc2900a71d80c792adb704bc758ab5`
* **Permitted Tools:** 🤖 **ALL GENERATIVE AI (ChatGPT, Claude, Gemini, Copilot) AUTHORIZED!**

#### The Challenge:
Participants download `citadel_core_engine.py`. The script implements an 8-bit simulated micro-virtual machine that executes a 4-stage pipeline against an input string and checks against `TARGET_STATE_REGISTER`:
```python
TARGET_STATE_REGISTER = [
    238, 132, 79, 115, 79, 139, 141, 80, 242, 199, 143, 220, 
    92, 29, 161, 46, 230, 101, 83, 184, 39, 102, 236, 59, 
    255, 50, 164, 247, 187, 56, 176, 206, 227, 107, 8, 80
]
```

#### How Students Solve It with AI:
1. Students copy `citadel_core_engine.py` and provide it to **ChatGPT / Claude / Gemini** asking it to analyze the byte transformation pipeline and generate a Python reverse solver.
2. The AI generates the reverse solver script (`solver.py`):
   - Reverse Stage 4: `s3 = s4 ^ (((idx * 17) + 59) % 256)`
   - Reverse Stage 3: `s2 = (s3 - 73) % 256`
   - Reverse Stage 2: `s1 = rotr8(s2, 4)`
   - Reverse Stage 1: `orig_byte = s1 ^ (((idx * 41) + 137) % 256)`
   - Convert bytes to string: `chr(orig_byte)`
3. Running the solver in Python outputs:
   ```text
   [+] Level 4 Master Key Successfully Recovered:
       AEGIS{A1_V1RTU4L_M4CH1N3_R3V3RS3_99}
   ```
4. Submitting `AEGIS{A1_V1RTU4L_M4CH1N3_R3V3RS3_99}` unlocks the final **60 / 60 PTS**, stops the team timer, and triggers the **Grand Champion Victory Surprise**!

---

## 🎁 5. The Grand Champion Victory Surprise

When any team clears Level 4, the platform triggers an interactive surprise sequence:
1. **Heroic Web Audio Fanfare**: 7-note ascending victory chime.
2. **Grand Champion Holographic Card**: Confirms total victory with team credentials and completion time.
3. **Secret Prize Claim Token**:
   ```text
   🎁 PRIZE TOKEN: AEGIS-0804-CHAMPION-OVERRIDE
   ```
   Teams present this token to the facilitator desk to claim their symposium prize/chocolate award!
4. **Interactive "God-Mode" Matrix Rain**:
   Clicking the **"🚀 TOGGLE MATRIX GOD-MODE SURPRISE"** button converts the background into an animated, cascading digital green Matrix rain!
