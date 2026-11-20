# 🛡️ ROUND 3: OPERATION CIPHER-BREACH // CRYPTOGRAPHIC DECRYPTION
## Stage Projector Console & Bowl Decryption Challenge
### Department of MCA & Ethical Hacking / Cyber Security Division

---

## 🧭 Event Overview & Pacing Architecture

Round 3 tests collegiate contestants across classical cipher principles and modern symmetric/asymmetric algorithms through two coordinated phases:

```
+--------------------------------------------------------------------------------------------------+
| PHASE 1: STAGE QUIZ (15 Marks)                 PHASE 2: BOWL CHIT DECRYPTION (30 Marks)          |
| 15 Live MCQ Questions (Easy -> Hard)           Team draws 1 Easy Chit (10M) + 1 Hard Chit (20M)  |
| 45s Projected Countdown Timer per question     10m (Easy) / 15m (Hard) solving time on stage HUD |
+--------------------------------------------------------------------------------------------------+
```

* **Target Audience:** MCA / B.Tech Cyber Security / Cryptography Students.
* **Total Marks:** **45 Marks** (15M Quiz + 10M Easy Chit + 20M Hard Chit).
* **Total Time:** ~45–60 Minutes.
* **Chit Pool:** **20 Total Chits** (10 Easy Chits + 10 Hard Chits: 5 Active + 5 Spares in each bowl).

---

## 🥣 Decryption Bowl Inventory (20 Chits Total)

### 🟢 Bowl 1: Easy Pool (10 Marks Each)
1. **Chit #E1:** Caesar Shift Cipher ($k=4$) -> `ULTRON PROTOCOL`
2. **Chit #E2:** Monoalphabetic Substitution Cipher -> `STARK TOWER`
3. **Chit #E3:** Vigenère Polyalphabetic Cipher (Key: `VISION`) -> `AVENGERS ASSEMBLE`
4. **Chit #E4:** One-Time Pad / Vernam Cipher (Key: `XQZVTRKMN`) -> `MINDSTONE`
5. **Chit #E5:** Rail Fence Transposition Cipher (3 Rails) -> `PROTECT EARTH`
6. **Chit #E6 [SPARE-1]:** Row-Column Transposition (Key: `THOR`) -> `ACTIVATE WAR MACHINE`
7. **Chit #E7 [SPARE-2]:** Playfair Digram Cipher (Key: `ULTRON`) -> `DESTROY JARVIS`
8. **Chit #E8 [SPARE-3]:** RC4 Stream Cipher (PRGA XOR) -> `JARVIS`
9. **Chit #E9 [SPARE-4]:** Affine Cipher ($C \equiv 5P + 8 \pmod{26}$) -> `STARK`
10. **Chit #E10 [SPARE-5]:** Vernam Bitwise XOR Stream (Key: `STARK`) -> `AGENT`

### 🔴 Bowl 2: Hard Pool (20 Marks Each)
1. **Chit #H1:** Hill Cipher ($2 	imes 2$ Matrix Decryption) -> `CODE`
2. **Chit #H2:** DES & 3DES (Feistel Inversion & S-Box 1 Lookup) -> `0001 1100` (`0x1C`)
3. **Chit #H3:** AES / Rijndael (InvShiftRows & InvSubBytes Lookup) -> `MIND`
4. **Chit #H4:** Blowfish Block Cipher (Round Function $F$ & Feistel Step) -> $F=42, L_0=24$
5. **Chit #H5:** RC5 Block Cipher (Data-Dependent Circular Bit Rotation) -> `0x53` (`'S'`)
6. **Chit #H6:** IDEA Block Cipher (Modular Multiplication mod $2^{16}+1$) -> `15`
7. **Chit #H7:** RSA Public-Key Cryptosystem ($m \equiv c^d \pmod n$) -> `9`
8. **Chit #H8:** ElGamal Cryptography (Discrete Logarithm Decryption) -> `9`
9. **Chit #H9 [SPARE-4]:** Diffie-Hellman Key Exchange ($K \equiv B^a \pmod p = 13^4 mod 31$) -> `10`
10. **Chit #H10 [SPARE-5]:** AES MixColumns in $	ext{GF}(2^8)$ ($02 ullet 0x25 \oplus \dots$) -> `0x53` (`'S'`)

---

## 🎛️ Stage Application Controls (`index.html`)

| Feature | Description | Shortcut |
| :--- | :--- | :---: |
| **Timer Reset** | Instantly resets the countdown to 45 seconds | `R` or `r` |
| **Pause / Resume** | Freezes the countdown timer for stage announcements | `Space` |
| **Grace Time** | Adds +15 seconds dynamically without restarting | `+` or `=` |
| **Auto-Advance** | Automatically triggers 3-second transition slide when timer hits 0 | Toggle in Header |
| **Jump Matrix** | Full-screen question grid to jump to any question or spare on the fly | `J` or `j` |
| **Phase Switcher** | Toggles between Phase 1 Stage Quiz and Phase 2 Chit Projector | Header Tab |
| **Chit Timer HUD**| Live 10m/15m countdown with `+2 Min` extension, pause, and reset | `Space`, `R`, `+` |
| **Audio SFX** | Beeps and chimes using Web Audio API | `M` or `m` |

---

## 📂 Deliverables & File Directory

* [`index.html`](file:///f:/CYBER%20EVENT%2023,34/Round3_Cryptographic_Decryption/index.html) — Interactive Dual-Phase Stage Application.
* [`PRINTABLE_CHIT_CARDS.html`](file:///f:/CYBER%20EVENT%2023,34/Round3_Cryptographic_Decryption/PRINTABLE_CHIT_CARDS.html) — 20 A4 Printable Cut-Out Chit Cards (10 pages, 2 chits/page).
* [`PRINTABLE_CHIT_CARDS.md`](file:///f:/CYBER%20EVENT%2023,34/Round3_Cryptographic_Decryption/PRINTABLE_CHIT_CARDS.md) — ASCII-bordered markdown cut-out template.
* [`FACILITATOR_SCORING_KEY.md`](file:///f:/CYBER%20EVENT%2023,34/Round3_Cryptographic_Decryption/FACILITATOR_SCORING_KEY.md) — Confidential evaluation key with full math solutions.
* [`CRYPTO_ANALYST_TOOLKIT.md`](file:///f:/CYBER%20EVENT%2023,34/Round3_Cryptographic_Decryption/CRYPTO_ANALYST_TOOLKIT.md) — Student reference sheet (ASCII, Mod-26 inverses, S-Boxes, formulas).
* [`TEAM_ANSWER_SHEET.md`](file:///f:/CYBER%20EVENT%2023,34/Round3_Cryptographic_Decryption/TEAM_ANSWER_SHEET.md) — Printable student submission form.
* [`QUESTION_BANK_MASTER.md`](file:///f:/CYBER%20EVENT%2023,34/Round3_Cryptographic_Decryption/QUESTION_BANK_MASTER.md) — Technical master bank.
* [`QUIZ_IMPORT_DATA.csv`](file:///f:/CYBER%20EVENT%2023,34/Round3_Cryptographic_Decryption/QUIZ_IMPORT_DATA.csv) & [`.json`](file:///f:/CYBER%20EVENT%2023,34/Round3_Cryptographic_Decryption/QUIZ_IMPORT_DATA.json) — Import data for Google Forms / Quizizz.
