# 🎯 ROUND 1: RAPID FACILITATOR CHEAT SHEET & ANSWER KEY
## Operation Ultron — S.H.I.E.L.D. Command Center Reference
### 🔒 CONFIDENTIAL // ORGANIZERS & EVALUATION COMMITTEE ONLY
*(Contains all answers for Main 30 Questions + 6 Reserve Tie-Breakers. Do NOT distribute to participants.)*

---

## ⚡ Master Answer Grid (At a Glance)

| # | Tier | Topic / Lore Area | Marks | Key | Trap Answer Warning |
| :-: | :---: | :--- | :-: | :-: | :--- |
| **01** | T1 | HTTPS Encrypted Port vs HTTP | **1 M** | **C** | **Port 443** (Students often pick B [Port 80 HTTP]) |
| **02** | T1 | CIA Triad: Ransomware Lockout | **1 M** | **B** | **Availability** (Avoid Confidentiality or Integrity) |
| **03** | T1 | **🎬 Movie: Tony's Original AI** | **1 M** | **B** | **J.A.R.V.I.S.** (Avoid F.R.I.D.A.Y. or K.A.R.E.N.) |
| **04** | T1 | Disguised Malware (Trojan Horse) | **1 M** | **B** | **Trojan Horse** (Worms replicate independently; Trojans disguise) |
| **05** | T1 | Multi-Factor Authentication (MFA) | **1 M** | **B** | **MFA** (Avoid Single Sign-On SSO) |
| **06** | T2 | ICMP Connectivity Test Utility | **1 M** | **B** | **`ping`** (Avoid `tracert` which traces hops) |
| **07** | T2 | **🎬 Movie: Wakandan Metal** | **1 M** | **B** | **Vibranium** (Avoid Adamantium / Wolverine) |
| **08** | T2 | Executive Spear-Phishing (Whaling) | **1 M** | **C** | **Whaling** (Targeting C-suite/leadership) |
| **09** | T2 | IDS Passive vs IPS Active Blocking | **1 M** | **B** | **IDS alerts; IPS actively blocks** |
| **10** | T2 | Symmetric Encryption Key Count | **1 M** | **A** | **One shared secret key** (Asymmetric uses two) |
| **11** | T3 | SQLi Backend Database Manipulation | **1 M** | **B** | **SQL Injection** (Avoid XSS) |
| **12** | T3 | **🎬 Movie: European Internet Hub** | **1 M** | **B** | **Oslo, Norway (NEXUS hub)** (Avoid London/Geneva) |
| **13** | T3 | Stored / Persistent XSS | **1 M** | **A** | **Stored XSS** (Saved in database, served to all) |
| **14** | T3 | ARP Cache Poisoning / MITM | **1 M** | **B** | **ARP lacks authentication, accepts unsolicited replies** |
| **15** | T3 | Password Salting vs Rainbow Tables | **1 M** | **B** | **Defeats precomputed Rainbow Tables** |
| **16** | T4 | Rogue Wi-Fi Hotspot (Evil Twin) | **1 M** | **A** | **Evil Twin Attack** (Spoofs legitimate SSID) |
| **17** | T4 | **🎬 Movie: Iron Man Backup AI** | **1 M** | **B** | **F.R.I.D.A.Y.** (Avoid JOCASTA or TADASHI) |
| **18** | T4 | Distributed Denial of Service (DDoS) | **1 M** | **B** | **DDoS via Botnet** (Coordinated zombie nodes) |
| **19** | T4 | Decoy Trap System (Honeypot) | **1 M** | **B** | **Honeypot** (Avoid Sandbox which is for detonation) |
| **20** | T4 | Asymmetric Encryption Key Choice | **1 M** | **B** | **Recipient's Public Key** (Confidentiality!) |
| **21** | T5 | Memory Overflow on Call Stack | **1 M** | **B** | **Stack Buffer Overflow** |
| **22** | T5 | **🎬 Movie: Cosmic Infinity Stone** | **1 M** | **C** | **The Mind Stone** (Inside Loki's scepter) |
| **23** | T5 | Unpatched / Unknown Vulnerability | **1 M** | **B** | **Zero-Day Vulnerability** |
| **24** | T5 | Nmap TCP SYN Half-Open Scan | **1 M** | **B** | **Sends RST after SYN-ACK without completing handshake** |
| **25** | T5 | Windows NTLM Pass-the-Hash (PtH) | **1 M** | **B** | **Pass-the-Hash** (Authenticates without plaintext) |
| **26** | T6 | Memory Offset Randomization (ASLR) | **1 M** | **B** | **ASLR** (DEP makes pages non-exec; ASLR randomizes) |
| **27** | T6 | **🎬 Movie: Net Burnout Avenger** | **1 M** | **B** | **The Vision** (Burns Ultron out of the net) |
| **28** | T6 | Ring 0 Stealth Malware (Rootkit) | **1 M** | **B** | **Kernel Rootkit** (Hides processes from Task Manager) |
| **29** | T6 | Cloud Instance Metadata SSRF | **1 M** | **B** | **Server-Side Request Forgery** (`169.254.169.254`) |
| **30** | T6 | BGP Route Hijacking Mechanism | **1 M** | **A** | **Announcing more specific prefix (Longest Prefix Match)** |

---

## 🛡️ Spare / Tie-Breaker Questions (Q31 – Q36)

| # | Tier | Topic / Lore Area | Marks | Key | Detailed Explanation |
| :-: | :---: | :--- | :-: | :-: | :--- |
| **31** | Res-1 | SSL Replacement Protocol | **1 M** | **A** | **Transport Layer Security (TLS)** replaced SSL. |
| **32** | Res-2 | **🎬 Movie: Ultron's Drone Base** | **1 M** | **B** | **Sokovia** (Home of Wanda & Pietro Maximoff). |
| **33** | Res-3 | Physical Security / Piggybacking | **1 M** | **B** | **Tailgating / Piggybacking** through secure doors. |
| **34** | Res-4 | **🎬 Movie: Dr. Helen Cho Machine** | **1 M** | **B** | **The Regeneration Cradle** (Vibranium tissue bonding). |
| **35** | Res-5 | Hash Collision (Birthday Paradox) | **1 M** | **B** | **Hash Collision Attack** (Two different inputs, same hash). |
| **36** | Res-6 | Architecture: "Never Trust, Verify" | **1 M** | **B** | **Zero Trust Architecture (ZTA)**. |

---

## 📈 Scoring & Verification Guidelines for Judges

1. **Answer Verification:**
   - Evaluators collect the physical **`TEAM_ANSWER_SHEET.md`** immediately after Q30 finishes.
   - Use the 30-question grid above to score submissions out of **30 Marks**.
2. **Tie-Breaker Activation:**
   - If two teams tie on total score, activate **Spare Questions 31 through 36** from the `index.html` Jump matrix (`JUMP ➔ SPARE / TIE-BREAKER RESERVE POOL`).
   - Highest score in the tie-breaker pool wins.
