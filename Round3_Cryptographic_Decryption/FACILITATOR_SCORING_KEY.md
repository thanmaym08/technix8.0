# 🔑 ROUND 3: FACILITATOR SCORING KEY & EVALUATION MANUAL
## ⚠️ CONFIDENTIAL // JUDGING PANEL ONLY — DO NOT DISTRIBUTE
### Target Track: MCA / Cybersecurity & Cryptography (Units 1 & 2)

---

## 🎯 MASTER SCORING ARCHITECTURE (45 TOTAL MARKS)
1. **Phase 1 (Cryptography Stage Quiz):** 15 Questions × 1 Mark = **15 Marks**
2. **Phase 2A (Easy Chit Decryption - Bowl 1):** 1 Chit = **10 Marks**
3. **Phase 2B (Hard Chit Decryption - Bowl 2):** 1 Chit = **20 Marks**
> **Total Maximum Possible Score:** **45 Marks**

---

# ⚡ PART 1: PHASE 1 QUIZ ANSWER KEY (QUESTIONS 1 – 15 + SPARES)

| Q# | Tier | Topic / Concept | Correct Option Text | Marks |
| :---: | :---: | :--- | :--- | :---: |
| **Q 01** | Easy | Symmetric Key Distribution | **Key distribution problem across untrusted communication channels** | 1 M |
| **Q 02** | Easy | Hash Avalanche Effect (Ultron Lore) | **The Avalanche Effect** | 1 M |
| **Q 03** | Easy | DES Effective Key Length | **56 bits** (64 bits minus 8 parity bits) | 1 M |
| **Q 04** | Easy | Stream vs Block Ciphers | **Stream Ciphers** | 1 M |
| **Q 05** | Easy | RSA Mathematical Basis | **Factoring large composite numbers into their two prime factors** | 1 M |
| **Q 06** | Medium | AES Key Sizes & Rounds | **128-bit (10 rounds), 192-bit (12 rounds), 256-bit (14 rounds)** | 1 M |
| **Q 07** | Medium | Diffie-Hellman Trapdoor (NEXUS Lore)| **The Discrete Logarithm Problem in multiplicative cyclic groups** | 1 M |
| **Q 08** | Medium | AES Non-Linear Step | **SubBytes (utilizing the multiplicative inverse in GF(2^8) & affine map)**| 1 M |
| **Q 09** | Medium | ECB Mode Prohibition | **Identical plaintext blocks produce identical ciphertext blocks** | 1 M |
| **Q 10** | Medium | DES Feistel Structure | **Splits into Left/Right 32-bit: L_i = R_{i-1} and R_i = L_{i-1} ⊕ F(...)** | 1 M |
| **Q 11** | Hard | RSA Euler's Totient φ(n) | **3120** (for p=61, q=53: (61-1)*(53-1) = 60 * 52 = 3120) | 1 M |
| **Q 12** | Hard | Small Exponent e=3 Attack | **Coppersmith's Low Public Exponent Attack / Håstad's Broadcast Attack** | 1 M |
| **Q 13** | Hard | Birthday Paradox Hash Collisions | **2^(n/2) operations** | 1 M |
| **Q 14** | Hard | Modern AEAD Cipher Mode | **Galois/Counter Mode (GCM)** | 1 M |
| **Q 15** | Hard | ECC vs RSA Security Efficiency | **Equivalent security with substantially smaller key sizes & lower compute**| 1 M |

### 🛡️ Reserve Tie-Breaker Questions (Spares 16 – 19)
* **SP-16 (Easy):** 3DES Meet-in-the-Middle bounds effective strength to **112 bits**.
* **SP-17 (Medium):** Cradle biometric payload non-denial is **Non-Repudiation** via digital signatures.
* **SP-18 (Hard):** Predictable CBC IV enables **Watermarking and Chosen-Plaintext Attacks (BEAST attack)**.
* **SP-19 (Hard):** Long-term key compromise defense is **Perfect Forward Secrecy (PFS)** via Ephemeral Diffie-Hellman.

---

# 🥣 PART 2: PHASE 2 CHIT DECRYPTION SOLUTIONS (UNITS 1 & 2)

---

## 🟢 BOWL 1: EASY CHITS (#E1 to #E10) — 10 MARKS EACH
* **Scoring Rubric:** Valid decryption working steps shown = **5 Marks** | Accurate recovered plaintext = **5 Marks** (Total: **10 Marks**).

### Chit #E1 — Caesar Shift Cipher (Unit 1)
* **Ciphertext:** `YPXVSR TVSXSGSP`
* **Key:** $k = 4$
* **Decryption Working:** Shift each letter backward by 4 ($P_i \equiv (C_i - 4) \pmod{26}$):
  - Y(24)-4 = U(20), P(15)-4 = L(11), X(23)-4 = T(19), V(21)-4 = R(17), S(18)-4 = O(14), R(17)-4 = N(13) -> `ULTRON`
  - T(19)-4 = P(15), V(21)-4 = R(17), S(18)-4 = O(14), X(23)-4 = T(19), S(18)-4 = O(14), G(6)-4 = C(2), S(18)-4 = O(14), P(15)-4 = L(11) -> `PROTOCOL`
* **✅ Final Plaintext:** `ULTRON PROTOCOL`

### Chit #E2 — Monoalphabetic Substitution Cipher (Unit 1)
* **Ciphertext:** `LZQKA ZGVTK`
* **Mapping:**
  ```
  Plain : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
  Cipher: Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
  ```
* **Decryption Working:** Reverse-lookup each cipher letter in the table:
  - L -> S, Z -> T, Q -> A, K -> R, A -> K -> `STARK`
  - Z -> T, G -> O, V -> W, T -> E, K -> R -> `TOWER`
* **✅ Final Plaintext:** `STARK TOWER`

### Chit #E3 — Vigenère Polyalphabetic Cipher (Unit 1)
* **Ciphertext:** `VDWVURMA SAGRHJDM`
* **Keyword:** `"VISION"` (V=21, I=8, S=18, I=8, O=14, N=13)
* **Decryption Working:** $P_i \equiv (C_i - K_i) \pmod{26}$:
  - V-V = A(0), D-I = V(21), W-S = E(4), V-I = N(13), U-O = G(6), R-N = E(4), M-V = R(17), A-I = S(18) -> `AVENGERS`
  - S-S = A(0), A-I = S(18), G-O = S(18), R-N = E(4), H-V = M(12), J-I = B(1), D-S = L(11), M-I = E(4) -> `ASSEMBLE`
* **✅ Final Plaintext:** `AVENGERS ASSEMBLE`

### Chit #E4 — One-Time Pad / Vernam Cipher (Unit 1)
* **Ciphertext:** `JYMYLKYZR`
* **Key:** `XQZVTRKMN` (X=23, Q=16, Z=25, V=21, T=19, R=17, K=10, M=12, N=13)
* **Decryption Working:** $P_i \equiv (C_i - K_i) \pmod{26}$:
  - J(9) - X(23) = -14 + 26 = 12 ('M')
  - Y(24) - Q(16) = 8 ('I')
  - M(12) - Z(25) = -13 + 26 = 13 ('N')
  - Y(24) - V(21) = 3 ('D')
  - L(11) - T(19) = -8 + 26 = 18 ('S')
  - K(10) - R(17) = -7 + 26 = 19 ('T')
  - Y(24) - K(10) = 14 ('O')
  - Z(25) - M(12) = 13 ('N')
  - R(17) - N(13) = 4 ('E')
* **✅ Final Plaintext:** `MINDSTONE`

### Chit #E5 — Rail Fence Transposition Cipher (Unit 1)
* **Ciphertext:** `PEEHRTC ATOTR` (13 characters)
* **Rails:** 3 Rails
* **Decryption Working:** Reconstruct 13-character zig-zag wave:
  - Rail 1 (positions 0, 4, 8, 12): P . . . E . . . E . . . H
  - Rail 2 (positions 1, 3, 5, 7, 9, 11): . R . T . C .   . A . T .
  - Rail 3 (positions 2, 6, 10): . . O . . . T . . . O . .
  - Read along zig-zag: P-R-O-T-E-C-T- -E-A-R-T-H
* **✅ Final Plaintext:** `PROTECT EARTH`

### Chit #E6 [SPARE-1] — Columnar Transposition (Unit 1)
* **Ciphertext:** `CAACE TTRHX IEMIX AVWAN`
* **Keyword:** `THOR` (Alphabetical order: H=1, O=2, R=3, T=4). 5 rows by 4 columns.
* **Decryption Working:**
  - 20 chars / 4 cols = 5 chars per col.
  - Col H (1st): C, A, A, C, E | Col O (2nd): T, T, R, H, X | Col R (3rd): I, E, M, I, X | Col T (4th): A, V, W, A, N
  - Map into T-H-O-R order:
    - Row 1: A C T I
    - Row 2: V A T E
    - Row 3: W A R M
    - Row 4: A C H I
    - Row 5: N E X X
  - Read row-by-row: `ACTIVATE WAR MACHINEX` (discard pad X)
* **✅ Final Plaintext:** `ACTIVATE WAR MACHINE`

### Chit #E7 [SPARE-2] — Playfair Cipher (Unit 1)
* **Ciphertext Digraphs:** `NI PO OU ZH CL ZE PZ`
* **Keyword:** `ULTRON`
* **Matrix Layout:**
  ```
  U  L  T  R  O
  N  A  B  C  D
  E  F  G  H  I
  K  M  P  Q  S
  V  W  X  Y  Z
  ```
* **Decryption Working:** Apply reverse Playfair rules:
  - NI -> D(1,4) E(2,0) = `DE`
  - PO -> S(3,4) T(0,2) = `ST`
  - OU -> same row left shift -> R(0,3) O(0,4) = `RO`
  - ZH -> Y(4,3) I(2,4) = `YI` (represents Y / J)
  - CL -> A(1,1) R(0,3) = `AR`
  - ZE -> V(4,0) I(2,4) = `VI`
  - PZ -> S(3,4) X(4,2) = `SX` (trailing pad)
  - Stream: `DE ST RO YI AR VI SX`
* **✅ Final Plaintext:** `DESTROY JARVIS`

### Chit #E8 [SPARE-3] — RC4 Stream Cipher (Unit 2)
* **Ciphertext (Hex):** `0x30 0x5E 0x19 0xC4 0x11 0x6F`
* **PRGA Keystream:** `0x7A 0x1F 0x4B 0x92 0x58 0x3C`
* **Decryption Working:** Compute bitwise XOR: $P_i = C_i \oplus K_i$:
  - 0x30 ^ 0x7A = 0x4A = 74 = 'J'
  - 0x5E ^ 0x1F = 0x41 = 65 = 'A'
  - 0x19 ^ 0x4B = 0x52 = 82 = 'R'
  - 0xC4 ^ 0x92 = 0x56 = 86 = 'V'
  - 0x11 ^ 0x58 = 0x49 = 73 = 'I'
  - 0x6F ^ 0x3C = 0x53 = 83 = 'S'
* **✅ Final Plaintext:** `JARVIS`

### Chit #E9 [SPARE-4] — Affine Cipher (Unit 1)
* **Ciphertext:** `U Z I P G`
* **Parameters:** $a = 5, b = 8$, Formula: $C \equiv (5P + 8) \pmod{26}$.
* **Modular Multiplicative Inverse:** $5^{-1} \equiv 21 \pmod{26}$ (since $5 \times 21 = 105 = 4 \times 26 + 1 \equiv 1$).
* **Decryption Formula:** $P_i \equiv 21 \cdot (C_i - 8) \pmod{26}$.
* **Decryption Working:**
  - $U = 20: 21 \times (20 - 8) = 21 \times 12 = 252 = 9(26) + 18 \implies 18 = \mathbf{S}$
  - $Z = 25: 21 \times (25 - 8) = 21 \times 17 = 357 = 13(26) + 19 \implies 19 = \mathbf{T}$
  - $I = 8: 21 \times (8 - 8) = 0 \implies 0 = \mathbf{A}$
  - $P = 15: 21 \times (15 - 8) = 21 \times 7 = 147 = 5(26) + 17 \implies 17 = \mathbf{R}$
  - $G = 6: 21 \times (6 - 8) = 21 \times (-2) = -42 = -2(26) + 10 \implies 10 = \mathbf{K}$
* **✅ Final Plaintext:** `STARK`

### Chit #E10 [SPARE-5] — Vernam Bitwise XOR Stream (Unit 1 / Unit 2)
* **Ciphertext (Hex):** `0x12  0x13  0x04  0x1C  0x1F`
* **Key Stream (ASCII):** `STARK` -> `[0x53, 0x54, 0x41, 0x52, 0x4B]`
* **Decryption Working:** Bitwise XOR $P_i = C_i \oplus K_i$:
  - $0x12 \oplus 0x53 = 00010010_2 \oplus 01010011_2 = 01000001_2 = 0x41 = 65 = \mathbf{'A'}$
  - $0x13 \oplus 0x54 = 00010011_2 \oplus 01010100_2 = 01000111_2 = 0x47 = 71 = \mathbf{'G'}$
  - $0x04 \oplus 0x41 = 00000100_2 \oplus 01000001_2 = 01000101_2 = 0x45 = 69 = \mathbf{'E'}$
  - $0x1C \oplus 0x52 = 00011100_2 \oplus 01010010_2 = 01001110_2 = 0x4E = 78 = \mathbf{'N'}$
  - $0x1F \oplus 0x4B = 00011111_2 \oplus 01001011_2 = 01010100_2 = 0x54 = 84 = \mathbf{'T'}$
* **✅ Final Plaintext:** `AGENT`

---

## 🔴 BOWL 2: HARD CHITS (#H1 to #H10) — 20 MARKS EACH
* **Scoring Rubric:** Mathematical derivation & working shown = **10 Marks** | Accurate recovered key/plaintext = **10 Marks** (Total: **20 Marks**).

### Chit #H1 — Hill Cipher (Unit 1)
* **Ciphertext:** `IE RR`
* **Key Matrix:** $K = \begin{pmatrix} 3 & 2 \\ 5 & 7 \end{pmatrix}$
* **Given Inverse Matrix:** $K^{-1} \equiv \begin{pmatrix} 3 & 14 \\ 9 & 5 \end{pmatrix} \pmod{26}$
* **Decryption Working:**
  - Digraph 1: `IE` -> $\begin{pmatrix} 8 \\ 4 \end{pmatrix}$
    $$\begin{pmatrix} 3 & 14 \\ 9 & 5 \end{pmatrix} \begin{pmatrix} 8 \\ 4 \end{pmatrix} = \begin{pmatrix} 24 + 56 \\ 72 + 20 \end{pmatrix} = \begin{pmatrix} 80 \\ 92 \end{pmatrix} \equiv \begin{pmatrix} 2 \\ 14 \end{pmatrix} = \begin{pmatrix} \text{C} \\ \text{O} \end{pmatrix} \pmod{26}$$
  - Digraph 2: `RR` -> $\begin{pmatrix} 17 \\ 17 \end{pmatrix}$
    $$\begin{pmatrix} 3 & 14 \\ 9 & 5 \end{pmatrix} \begin{pmatrix} 17 \\ 17 \end{pmatrix} = \begin{pmatrix} 51 + 238 \\ 153 + 85 \end{pmatrix} = \begin{pmatrix} 289 \\ 238 \end{pmatrix} \equiv \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} \text{D} \\ \text{E} \end{pmatrix} \pmod{26}$$
* **✅ Final Plaintext:** `CODE`

### Chit #H2 — DES & 3DES Block Cipher (Unit 2)
* **Given:** $L_1 = 1100_2$, $R_1 = 1010_2$, S-Box 1 input = $101010_2$.
* **Decryption Working:**
  1. Outer bits $b_1 b_6 = 10_2 = \text{Row } 2$.
  2. Inner bits $b_2 b_3 b_4 b_5 = 0101_2 = \text{Column } 5$.
  3. DES S-Box 1 lookup at Row 2, Column 5 yields $11 = \mathbf{1011_2}$. Thus $f(R_0, K_1) = 1011_2$.
  4. Feistel round equations:
     - $R_0 = L_1 = \mathbf{1100_2}$
     - $L_0 = R_1 \oplus f(R_0, K_1) = 1010_2 \oplus 1011_2 = \mathbf{0001_2}$.
  5. 3DES EDE mode decryption order: $P = D_{K1}(E_{K2}(D_{K3}(C)))$.
* **✅ Final Recovered Register:** `0001 1100` (Hex `0x1C` or $L_0 = 1, R_0 = 12$)

### Chit #H3 — AES / Rijndael Block Cipher (Unit 2)
* **Given:** State Column = `[0x76, 0x2B, 0xAF, 0x63]`, Round Key $K_{10} = `[0x50, 0x1A, 0xC3, 0x02]`.
* **Decryption Working:**
  1. AddRoundKey step: State $\oplus K_{10}$:
     - $0x76 \oplus 0x50 = 0x26$
     - $0x2B \oplus 0x1A = 0x31$
     - $0xAF \oplus 0xC3 = 0x6C$
     - $0x63 \oplus 0x02 = 0x61$
  2. InvSubBytes lookup (using table provided on chit):
     - $\text{InvSBox}[0x26] = 0x4D = \text{'M'}$
     - $\text{InvSBox}[0x31] = 0x49 = \text{'I'}$
     - $\text{InvSBox}[0x6C] = 0x4E = \text{'N'}$
     - $\text{InvSBox}[0x61] = 0x44 = \text{'D'}$
* **✅ Final Recovered Word:** `MIND` (or hex `0x4D 0x49 0x4E 0x44`)

### Chit #H4 — Blowfish Block Cipher (Unit 2)
* **Given:** $S_1[a] = 10, S_2[b] = 20, S_3[c] = 5, S_4[d] = 15$, $L_1 = 50$.
* **Decryption Working:**
  1. Compute Blowfish Round Function $F$:
     $$F(a,b,c,d) = ((S_1[a] + S_2[b] \bmod 2^{32}) \oplus S_3[c]) + S_4[d] \bmod 2^{32}$$
     $$F = ((10 + 20) \oplus 5) + 15 = (30 \oplus 5) + 15 = 27 + 15 = \mathbf{42}$$
  2. Invert Feistel round: $L_0 = L_1 \oplus F = 50 \oplus 42 = 00110010_2 \oplus 00101010_2 = 00011000_2 = \mathbf{24}$.
* **✅ Final Plaintext Value:** $F = \mathbf{42}$, $L_0 = \mathbf{24}$

### Chit #H5 — RC5 Block Cipher (Unit 2)
* **Given:** $A = \mathbf{0x9A}$ ($10011010_2$), $B = 3$, $S[0] = 0$.
* **Decryption Working:**
  - Inverse circular rotation formula: $A = ((A - S[0]) \ggg B) \oplus B$.
  - Bitwise circular right shift of 8-bit byte $0x9A$ by 3 positions:
    $10011010_2 \ggg 3 = 01010011_2 = \mathbf{0x53}$ (ASCII 'S').
  - Since $S[0] = 0$, $A = \mathbf{0x53}$ (decimal 83).
* **✅ Final Plaintext Register:** `0x53` (Character **`S`** / decimal `83`)

### Chit #H6 — IDEA Block Cipher (Unit 2)
* **Given:** Output sub-block $Y = 135$, Subkey $Z = 9$.
* **Pre-computed Inverse:** $Z^{-1} \equiv 9^{-1} \pmod{65537} = \mathbf{7282}$ (since $9 \times 7282 = 65538 \equiv 1 \pmod{65537}$).
* **Decryption Working:**
  $$X = (Y \cdot Z^{-1}) \pmod{65537} = (135 \times 7282) \pmod{65537}$$
  $$135 \times 7282 = 983070$$
  $$983070 = 14 \times 65537 + 15 \implies X = \mathbf{15}$$
* **✅ Final Recovered Plaintext:** **`15`**

### Chit #H7 — RSA Public-Key Algorithm (Unit 2)
* **Given:** $p = 5, q = 11 \implies n = 55$, $\phi(n) = 40$, $e = 3$, $c = 14$.
* **Decryption Working:**
  1. Compute $d \equiv e^{-1} \pmod{40}$: $3d \equiv 1 \pmod{40} \implies 3 \times 27 = 81 = 2(40) + 1 \implies \mathbf{d = 27}$.
  2. Decrypt: $m \equiv 14^{27} \pmod{55}$.
     - $14^2 = 196 \equiv 31$
     - $14^4 = 31^2 = 961 \equiv 26$
     - $14^8 = 26^2 = 676 \equiv 16$
     - $14^{16} = 16^2 = 256 \equiv 36$
     - $14^{27} = 14^{16} \times 14^8 \times 14^2 \times 14^1 = 36 \times 16 \times 31 \times 14 \equiv \mathbf{9} \pmod{55}$.
* **✅ Final Plaintext / Key:** **`9`** (Flag `KEY-09`)

### Chit #H8 — ElGamal Cryptosystem (Unit 2)
* **Given:** $p = 23, g = 5, y = 8, x = 6$, Ciphertext pair $(c_1 = 19, c_2 = 18)$.
* **Decryption Working:**
  1. Compute shared secret $s \equiv c_1^x \pmod p = 19^6 \pmod{23} = (-4)^6 = 4096 = 178(23) + 2 \equiv \mathbf{2} \pmod{23}$.
  2. Compute modular inverse $s^{-1} \pmod{23}$: $2 \times 12 = 24 \equiv 1 \pmod{23} \implies s^{-1} = \mathbf{12}$.
  3. Recover plaintext $m \equiv (c_2 \cdot s^{-1}) \pmod p = (18 \times 12) \pmod{23} = 216 = 9(23) + 9 \equiv \mathbf{9} \pmod{23}$.
* **✅ Final Plaintext Value:** **`9`** (Flag `ELGAMAL-09`)

### Chit #H9 [SPARE-4] — Diffie-Hellman Key Exchange (Unit 2)
* **Given Parameters:** Modulus $p = 31$, Generator $g = 3$, Alice's Private Key $a = 4$, Bob's Public Key $B = 13$.
* **Decryption Working:** Compute shared secret session key $K_{AB} \equiv B^a \pmod p = 13^4 \pmod{31}$:
  1. $13^2 = 169$. Since $169 = 5 \times 31 + 14$, $13^2 \equiv 14 \pmod{31}$.
  2. $13^4 = (13^2)^2 \equiv 14^2 = 196 \pmod{31}$.
  3. $196 = 6 \times 31 + 10 \implies 196 \equiv \mathbf{10} \pmod{31}$.
* **✅ Final Shared Secret Key:** **`10`** (or hex `0x0A` / integer 10)

### Chit #H10 [SPARE-5] — AES MixColumns Transformation in GF(2^8) (Unit 2)
* **Given:** State Column $S = [0x25, 0x12, 0x31, 0x1E]^T$, Matrix Row $[02, 03, 01, 01]$.
* **Formula:** $d_0 = (02 \bullet 0x25) \oplus (03 \bullet 0x12) \oplus (01 \bullet 0x31) \oplus (01 \bullet 0x1E)$ in $\text{GF}(2^8)$ with irreducible polynomial $m(x) = x^8 + x^4 + x^3 + x + 1$ (`0x11B`).
* **Decryption Working:**
  1. $02 \bullet 0x25$: Since MSB of $0x25$ is 0, shift left 1 bit: $0x25 \ll 1 = \mathbf{0x4A}$ ($01001010_2$).
  2. $03 \bullet 0x12 = (02 \bullet 0x12) \oplus 0x12$. Since MSB of $0x12$ is 0, $02 \bullet 0x12 = 0x24$. Thus $0x24 \oplus 0x12 = \mathbf{0x36}$ ($00110110_2$).
  3. $01 \bullet 0x31 = \mathbf{0x31}$ ($00110001_2$).
  4. $01 \bullet 0x1E = \mathbf{0x1E}$ ($00011110_2$).
  5. Bitwise XOR sum:
     - $0x4A \oplus 0x36 = 01001010_2 \oplus 00110110_2 = 01111100_2 = 0x7C$
     - $0x7C \oplus 0x31 = 01111100_2 \oplus 00110001_2 = 01001101_2 = 0x4D$
     - $0x4D \oplus 0x1E = 01001101_2 \oplus 00011110_2 = 01010011_2 = \mathbf{0x53}$
  6. ASCII character for byte $0x53$ (decimal 83) is **`'S'`**.
* **✅ Final Transformed Byte / Character:** **`0x53`** (Character **`S`**)
