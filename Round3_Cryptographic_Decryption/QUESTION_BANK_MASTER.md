# 📚 ROUND 3: MASTER QUESTION BANK & CIPHER DOSSIER
## Comprehensive Reference Manual for Faculty & Technical Leads (20 Chits + 19 Quiz Qs)
### Theme: Operation Ultron // Cryptographic Decryption & Protocol Analysis

---

## 🧭 Overview & Tournament Structure
Round 3 is the deciding technical event of the tournament, evaluating students on foundational through advanced cryptographic principles across two distinct phases:

1. **Phase 1: Cryptography Stage Quiz (15 Marks)**
   - 15 main questions + 4 spare reserve questions.
   - 1 Mark per question.
   - Paced at 45 seconds per question on the stage projector console.
   - Topics: Symmetric/Asymmetric, Hash Functions, DES/AES Internals, RSA Math, DHKE, ECC, Modern AEAD modes.
2. **Phase 2: Bowl Chit Decryption Challenge (30 Marks)**
   - Two bowls containing physical chits with intercepted cryptographic payloads.
   - Each team draws:
     - **1 Easy Chit** (from Bowl 1) -> **10 Marks** (5M Method + 5M Plaintext).
     - **1 Hard Chit** (from Bowl 2) -> **20 Marks** (10M Method + 10M Plaintext).
   - **10 Easy Chits** (5 Main + 5 Spares) and **10 Hard Chits** (5 Main + 5 Spares) provided.
   - All chits feature explicit formulas, pre-computed modular inverses, S-boxes, and step-by-step hints so teams can perform manual calculations cleanly on paper.

---

# ⚡ SECTION 1: PHASE 1 STAGE QUIZ (QUESTIONS 1 – 15 + SPARES)

### Question 01 [Tier: Easy | Marks: 1M]
**Topic:** Symmetric vs Asymmetric Fundamentals

> **Question:**  
> In classical symmetric cryptography, both sender and receiver use a single shared key. What primary operational challenge does this model introduce in large-scale networks?

**Options:**
- **A**: **[CORRECT]** Key distribution problem across untrusted communication channels
- **B**: Inability to perform high-speed hardware block encryption
- **C**: Vulnerability to Grover's quantum search algorithm only
- **D**: Requirement for a public-key certificate authority hierarchy

*Technical Rationale:* Symmetric cryptography requires both parties to securely share the secret key beforehand, creating the classic N*(N-1)/2 key exchange and distribution problem in large networks.

### Question 02 [Tier: Easy | Marks: 1M]
**Topic:** Cryptographic Hash Functions (Movie Tie-In: Ultron Consciousness Checksum)

> **Question:**  
> When verifying the integrity of Ultron's neural network code, modifying a single bit in the input source produces an unpredictable, drastic change across the entire output digest. What is this property called?

**Options:**
- **A**: **[CORRECT]** The Avalanche Effect
- **B**: Pre-image Resistance
- **C**: Homomorphic Expansion
- **D**: Differential Cryptanalysis

*Technical Rationale:* The avalanche effect is a crucial property of cryptographic hashes and block ciphers where a small change in the input (e.g., flipping 1 bit) changes approximately half of the output bits.

### Question 03 [Tier: Easy | Marks: 1M]
**Topic:** Data Encryption Standard (DES) Architecture

> **Question:**  
> The legacy Data Encryption Standard (DES) processes data in 64-bit blocks. What is the actual effective key length used for encryption after parity bits are discarded?

**Options:**
- **A**: **[CORRECT]** 56 bits
- **B**: 64 bits
- **C**: 48 bits
- **D**: 128 bits

*Technical Rationale:* Although a DES key is represented as 64 bits, every 8th bit is used as an odd-parity check bit, leaving only 56 effective bits for cryptographic security.

### Question 04 [Tier: Easy | Marks: 1M]
**Topic:** Block vs Stream Ciphers

> **Question:**  
> Which category of symmetric ciphers encrypts continuous plaintext bit-by-bit or byte-by-byte using a pseudorandom keystream combined via the XOR operation?

**Options:**
- **A**: **[CORRECT]** Stream Ciphers
- **B**: Block Ciphers
- **C**: Asymmetric Ciphers
- **D**: Permutation Networks

*Technical Rationale:* Stream ciphers (e.g., RC4, ChaCha20) generate a continuous pseudorandom keystream and XOR it directly with plaintext digits, making them ideal for real-time streaming audio/video.

### Question 05 [Tier: Easy | Marks: 1M]
**Topic:** RSA Asymmetric Cryptography Basics

> **Question:**  
> The security of the Rivest-Shamir-Adleman (RSA) public-key cryptosystem fundamentally relies on the mathematical difficulty of which computational problem?

**Options:**
- **A**: **[CORRECT]** Factoring large composite numbers into their two prime factors
- **B**: Solving the discrete logarithm problem over finite fields
- **C**: Finding shortest vectors in high-dimensional geometric lattices
- **D**: Computing modular square roots without quadratic residue clues

*Technical Rationale:* RSA's one-way trapdoor function relies on the integer factorization problem: multiplying two large primes p and q is easy, but factoring n = p*q is computationally infeasible for large key sizes.

### Question 06 [Tier: Medium | Marks: 1M]
**Topic:** Advanced Encryption Standard (AES) Parameters

> **Question:**  
> The Advanced Encryption Standard (AES) operates on a fixed 128-bit block size. What are its standard key sizes and their corresponding number of transformation rounds?

**Options:**
- **A**: **[CORRECT]** 128-bit (10 rounds), 192-bit (12 rounds), 256-bit (14 rounds)
- **B**: 64-bit (8 rounds), 128-bit (10 rounds), 256-bit (12 rounds)
- **C**: 128-bit (12 rounds), 192-bit (14 rounds), 256-bit (16 rounds)
- **D**: 128-bit (16 rounds), 256-bit (32 rounds), 512-bit (64 rounds)

*Technical Rationale:* AES (Rijndael) specifies a fixed block size of 128 bits with key lengths of 128, 192, and 256 bits requiring 10, 12, and 14 rounds respectively.

### Question 07 [Tier: Medium | Marks: 1M]
**Topic:** Diffie-Hellman Key Exchange (Movie Tie-In: Oslo NEXUS Hub)

> **Question:**  
> When JARVIS negotiates an ephemeral session key with the Oslo NEXUS Internet Hub using Diffie-Hellman, what mathematical trapdoor prevents an eavesdropper from calculating the shared secret?

**Options:**
- **A**: **[CORRECT]** The Discrete Logarithm Problem in multiplicative cyclic groups
- **B**: The computational difficulty of integer polynomial division
- **C**: The irreversibility of the Rijndael MixColumns matrix multiplication
- **D**: The avalanche expansion of Merkle-Damgård iterative compression

*Technical Rationale:* Diffie-Hellman security is based on the difficulty of the Discrete Logarithm Problem: given g, p, and g^a mod p, it is computationally hard to deduce the private exponent a.

### Question 08 [Tier: Medium | Marks: 1M]
**Topic:** AES Internal Round Transformations

> **Question:**  
> During a standard round of AES encryption, which specific transformation provides non-linear byte substitution to thwart linear and differential cryptanalysis attacks?

**Options:**
- **A**: **[CORRECT]** SubBytes (utilizing the multiplicative inverse in GF(2^8) and an affine map)
- **B**: ShiftRows (cyclically shifting the rows of the state array to the left)
- **C**: MixColumns (multiplying state columns by a fixed polynomial matrix)
- **D**: AddRoundKey (bitwise XORing the state matrix with the expanded round subkey)

*Technical Rationale:* SubBytes is the sole non-linear transformation in AES, mapping each byte using an invertible S-box constructed from the multiplicative inverse over Galois Field GF(2^8) followed by an affine transformation.

### Question 09 [Tier: Medium | Marks: 1M]
**Topic:** Block Cipher Modes of Operation (ECB Vulnerability)

> **Question:**  
> Why is Electronic Codebook (ECB) mode strictly prohibited for encrypting structured messages, database records, and bitmap images in production systems?

**Options:**
- **A**: **[CORRECT]** Identical plaintext blocks produce identical ciphertext blocks, preserving data patterns
- **B**: It requires a 128-bit cryptographically secure non-repeating Initialization Vector (IV)
- **C**: Bit errors in one ciphertext block propagate indefinitely across all subsequent blocks
- **D**: It does not support parallelized multi-threaded hardware processing

*Technical Rationale:* ECB encrypts each block independently without an IV or chaining. Identical 16-byte plaintext blocks yield identical ciphertext blocks, visually revealing high-level patterns (the famous ECB Tux penguin leak).

### Question 10 [Tier: Medium | Marks: 1M]
**Topic:** DES Feistel Network Architecture

> **Question:**  
> The DES algorithm is structured upon a Feistel Network. How does a Feistel structure process a 64-bit plaintext block during each iterative round?

**Options:**
- **A**: **[CORRECT]** It splits the block into Left (L) and Right (R) 32-bit halves: L_i = R_{i-1} and R_i = L_{i-1} ⊕ F(R_{i-1}, K_i)
- **B**: It multiplies all 64 bits simultaneously by a 4x4 matrix over a finite field GF(2^4)
- **C**: It applies an asymmetric modular exponentiation using the public key and round counter
- **D**: It compresses the 64-bit block into a 32-bit digest before appending a parity checksum

*Technical Rationale:* In a Feistel cipher, the block is divided into two 32-bit halves. The right half becomes the next round's left half, while the right half is updated by XORing the left half with the round function output F(R, K).

### Question 11 [Tier: Hard | Marks: 1M]
**Topic:** RSA Mathematics & Key Derivation

> **Question:**  
> In an RSA key generation procedure, an analyst selects two prime numbers p = 61 and q = 53. What is the value of Euler's totient function φ(n), which is required to calculate the private decryption exponent d?

**Options:**
- **A**: **[CORRECT]** 3120
- **B**: 3233
- **C**: 3116
- **D**: 3286

*Technical Rationale:* Euler's totient function for two distinct primes p and q is calculated as φ(n) = (p - 1) * (q - 1). Here, φ(n) = (61 - 1) * (53 - 1) = 60 * 52 = 3120.

### Question 12 [Tier: Hard | Marks: 1M]
**Topic:** Asymmetric Cryptanalysis (Movie Tie-In: Ultron Nuclear Protocol)

> **Question:**  
> Ultron attempts to tamper with digital launch commands signed using unpadded RSA with public exponent e = 3 sent across multiple nodes. What cryptographic attack exploits small public exponents when messages lack OAEP padding?

**Options:**
- **A**: **[CORRECT]** Coppersmith's Low Public Exponent Attack / Håstad's Broadcast Attack
- **B**: Bleichenbacher's Chosen-Ciphertext Padding Oracle Attack on PKCS#1 v1.5
- **C**: Shor's Quantum Polynomial Factoring Algorithm
- **D**: Meet-in-the-Middle Key Collision Cryptanalysis

*Technical Rationale:* When an unpadded RSA public exponent e is very small (e.g., e = 3) and the same message is encrypted to multiple recipients, Håstad's Broadcast Attack and Coppersmith's theorem allow recovering the plaintext using the Chinese Remainder Theorem.

### Question 13 [Tier: Hard | Marks: 1M]
**Topic:** Hash Collision Attacks & The Birthday Paradox

> **Question:**  
> According to the Birthday Paradox, finding any two arbitrary distinct messages m1 ≠ m2 such that Hash(m1) = Hash(m2) for an n-bit cryptographic hash output requires approximately how many hash evaluations?

**Options:**
- **A**: **[CORRECT]** 2^(n/2) operations
- **B**: 2^n operations
- **C**: 2^(n - 1) operations
- **D**: n^2 operations

*Technical Rationale:* Due to the mathematics of the birthday paradox, finding a collision (two arbitrary messages with identical hash) takes only O(2^(n/2)) evaluations, which is why a 128-bit hash (like MD5) offers only 64 bits of collision resistance.

### Question 14 [Tier: Hard | Marks: 1M]
**Topic:** Authenticated Encryption with Associated Data (AEAD)

> **Question:**  
> Which modern block cipher mode combines Counter (CTR) mode encryption with a Galois universal hash function to achieve both confidentiality and message integrity (AEAD) in high-throughput TLS 1.3 connections?

**Options:**
- **A**: **[CORRECT]** Galois/Counter Mode (GCM)
- **B**: Cipher Block Chaining with Message Authentication Code (CBC-MAC)
- **C**: Output Feedback Mode (OFB)
- **D**: Propagating Cipher Feedback Mode (PCBC)

*Technical Rationale:* AES-GCM (Galois/Counter Mode) provides Authenticated Encryption with Associated Data (AEAD) by combining CTR mode for encryption with GMAC for authentication, enabling high hardware throughput.

### Question 15 [Tier: Hard | Marks: 1M]
**Topic:** Elliptic Curve Cryptography (ECC) Advantages

> **Question:**  
> Why is Elliptic Curve Cryptography (ECC) widely adopted to replace legacy RSA in modern TLS certificates, cryptocurrency wallets, and mobile devices?

**Options:**
- **A**: **[CORRECT]** It offers equivalent security levels with substantially smaller key sizes and lower compute latency
- **B**: It is completely immune to quantum computers running Shor's algorithm
- **C**: It does not require modular arithmetic or finite field operations during key generation
- **D**: It allows symmetric multi-party hardware block streaming without an IV

*Technical Rationale:* A 256-bit ECC key provides equivalent cryptographic strength to a 3072-bit RSA key, drastically reducing memory usage, certificate transfer bandwidth, and processor power on mobile devices.

### Question 16 [Tier: Spare | Marks: 1M]
**Topic:** Triple DES (3DES) & Meet-in-the-Middle Attack

> **Question:**  
> [SPARE-01] Triple DES (3DES) executes an Encrypt-Decrypt-Encrypt (EDE) sequence using three 56-bit keys (168 bits total). Why is its effective cryptographic security bounded at only 112 bits?

**Options:**
- **A**: **[CORRECT]** Vulnerability to Meet-in-the-Middle (MitM) space-time tradeoff attacks
- **B**: Weak parity bits leaked during the intermediate DES decryption pass
- **C**: The Feistel function S-box saturation limit under differential analysis
- **D**: The Sweet32 birthday collision attack on 64-bit block ciphers

*Technical Rationale:* A Meet-in-the-Middle attack computes encryptions from one end and decryptions from the other, finding matching intermediate states in 2^112 operations, reducing 3DES effective strength from 168 to 112 bits.

### Question 17 [Tier: Spare | Marks: 1M]
**Topic:** Security Services (Movie Tie-In: Cradle Biometric Authorizations)

> **Question:**  
> [SPARE-02] Dr. Helen Cho's Regeneration Cradle requires a cryptographic proof that prevents the transmitting entity from falsely denying that they originated a signed medical synthesis payload. What security property is this?

**Options:**
- **A**: **[CORRECT]** Non-Repudiation
- **B**: Confidentiality
- **C**: Availability
- **D**: Forward Secrecy

*Technical Rationale:* Non-repudiation ensures that a sender cannot refute having sent a message or initiated a transaction, mathematically guaranteed through asymmetric private-key digital signatures.

### Question 18 [Tier: Spare | Marks: 1M]
**Topic:** Cipher Block Chaining (CBC) Initialization Vectors

> **Question:**  
> [SPARE-03] When implementing AES in Cipher Block Chaining (CBC) mode, what critical vulnerability is introduced if the Initialization Vector (IV) is predictable or repeated across multiple messages?

**Options:**
- **A**: **[CORRECT]** Watermarking and Chosen-Plaintext Attacks (e.g., BEAST protocol attack)
- **B**: Direct recovery of the 256-bit master symmetric encryption key
- **C**: Permanent collapse of the Galois multiplication lookup table
- **D**: Inversion of the SHA-256 HMAC integrity checksum

*Technical Rationale:* In CBC mode, if an attacker can predict the IV of the next message, they can construct a chosen plaintext that tests hypotheses about previous blocks, breaking IND-CPA security (as demonstrated in the BEAST attack).

### Question 19 [Tier: Spare | Marks: 1M]
**Topic:** Perfect Forward Secrecy (PFS)

> **Question:**  
> [SPARE-04] Which cryptographic design principle ensures that an adversary who records encrypted network traffic today and subsequently steals the server's master private key years later STILL cannot decrypt that recorded traffic?

**Options:**
- **A**: **[CORRECT]** Perfect Forward Secrecy (PFS) via Ephemeral Diffie-Hellman
- **B**: Zero-Knowledge Range Proofs
- **C**: Quantum Key Distribution (QKD)
- **D**: Homomorphic Asymmetric Masking

*Technical Rationale:* Perfect Forward Secrecy (PFS) generates unique, disposable session keys for every communication session using ephemeral Diffie-Hellman (DHE/ECDHE). Compromising the server's long-term key does not reveal past session keys.

---

# 🥣 SECTION 2: PHASE 2 CHIT CIPHER DOSSIER (20 CHITS TOTAL)

---

## 🟢 BOWL 1: EASY CHITS (#E1 to #E10) — 10 MARKS EACH

### Chit #E1 — Caesar Shift Cipher (Unit 1)
* **Tier & Marks:** Easy (10 Marks)
* **Cipher Category:** Caesar / Shift Cipher (Unit 1)
* **Scenario:** Ultron Drone Intercepted Tactical Command
* **Intercepted Ciphertext:** `YPXVSR TVSXSGSP`
* **Clue:** An intercepted tactical radio burst was encrypted with a constant Caesar key offset k = 4.
* **Formula & Hints:** Formula: P_i ≡ (C_i - k) mod 26. Shift each ciphertext letter backward by 4 positions in the alphabet (A=0, B=1 ... Z=25).

### Chit #E2 — Monoalphabetic Substitution Cipher (Unit 1)
* **Tier & Marks:** Easy (10 Marks)
* **Cipher Category:** Monoalphabetic Substitution Cipher (Unit 1)
* **Scenario:** Hydra Sub-Level Storage Override
* **Intercepted Ciphertext:** `LZQKA ZGVTK`
* **Clue:** Encrypted using a fixed, scrambled permutation of the 26-letter alphabet. Use the provided lookup table to reverse each character.
* **Formula & Hints:** Lookup Table: Plain A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ↔ Cipher Q W E R T Y U I O P A S D F G H J K L Z X C V B N M. Find each cipher letter and read the matching plain letter.

### Chit #E3 — Vigenère Polyalphabetic Cipher (Unit 1)
* **Tier & Marks:** Easy (10 Marks)
* **Cipher Category:** Vigenère Polyalphabetic Cipher (Unit 1)
* **Scenario:** Mind Stone Encrypted Telemetry Broadcast
* **Intercepted Ciphertext:** `VDWVURMA SAGRHJDM`
* **Clue:** The broadcast is protected by a polyalphabetic Vigenère cipher repeated with keyword 'VISION'.
* **Formula & Hints:** Formula: P_i ≡ (C_i - K_i) mod 26 where K = VISION (V=21, I=8, S=18, I=8, O=14, N=13). Subtract key letter shifts from ciphertext (add 26 if negative).

### Chit #E4 — One-Time Pad / Vernam Cipher (Unit 1)
* **Tier & Marks:** Easy (10 Marks)
* **Cipher Category:** One-Time Pad (OTP) / Vernam Cipher (Unit 1)
* **Scenario:** S.H.I.E.L.D. Secure Satellite Channel
* **Intercepted Ciphertext:** `JYMYLKYZR`
* **Clue:** A 9-character secret payload was combined with an equal-length truly random one-time key: 'XQZVTRKMN'.
* **Formula & Hints:** Formula: P_i ≡ (C_i - K_i) mod 26. Key: X(23) Q(16) Z(25) V(21) T(19) R(17) K(10) M(12) N(13). Subtract key from ciphertext modulo 26.

### Chit #E5 — Rail Fence Transposition Cipher (Unit 1)
* **Tier & Marks:** Easy (10 Marks)
* **Cipher Category:** Rail Fence Transposition (Unit 1)
* **Scenario:** Intercepted Ultron Distributed Hive Beacon
* **Intercepted Ciphertext:** `PEEHRTC ATOTR`
* **Clue:** A 13-character directive was scrambled across 3 electrical rails in an oscillating zig-zag wave pattern.
* **Formula & Hints:** Pattern across 3 rails: Rail 1 takes 4 chars (P,E,E,H), Rail 2 takes 6 chars (R,T,C, ,A,T), Rail 3 takes 3 chars (O,T,O). Trace the zig-zag wave: R1-R2-R3-R2-R1...

### Chit #E6 [SPARE-1] — Columnar Transposition Cipher (Unit 1)
* **Tier & Marks:** Easy (Spare) (10 Marks)
* **Cipher Category:** Row-Column Transposition Cipher (Unit 1)
* **Scenario:** Defense Grid Re-Routing Broadcast
* **Intercepted Ciphertext:** `CAACE TTRHX IEMIX AVWAN`
* **Clue:** A 20-character military command was written into 5 rows of 4 columns under keyword 'THOR' and read out column-by-column.
* **Formula & Hints:** Keyword THOR alphabetical column order: H=1, O=2, R=3, T=4. Place 5 letters per column in alphabetical order, sort columns back to T-H-O-R, then read across rows.

### Chit #E7 [SPARE-2] — Playfair Digram Cipher (Unit 1)
* **Tier & Marks:** Easy (Spare) (10 Marks)
* **Cipher Category:** Playfair Cipher (Unit 1)
* **Scenario:** Intercepted Tactical Infiltration Orders
* **Intercepted Ciphertext:** `NI PO OU ZH CL ZE PZ`
* **Clue:** Encrypted using a 5x5 Playfair keyword matrix keyed by 'ULTRON' (I and J share a cell).
* **Formula & Hints:** Matrix: [U,L,T,R,O / N,A,B,C,D / E,F,G,H,I / K,M,P,Q,S / V,W,X,Y,Z]. Decryption rules: Same row -> shift left; Same col -> shift up; Rectangle -> swap columns.

### Chit #E8 [SPARE-3] — RC4 Stream Cipher (Unit 2)
* **Tier & Marks:** Easy (Spare) (10 Marks)
* **Cipher Category:** RC4 Stream Cipher (Unit 2)
* **Scenario:** Encrypted Communication Link Recovery
* **Intercepted Ciphertext:** `0x30 0x5E 0x19 0xC4 0x11 0x6F`
* **Clue:** A 6-byte message stream was encrypted using an RC4 keystream generated by the Pseudo-Random Generation Algorithm (PRGA).
* **Formula & Hints:** Formula: Plaintext_Byte = Ciphertext_Byte ⊕ Keystream_Byte. Given PRGA Keystream: [0x7A, 0x1F, 0x4B, 0x92, 0x58, 0x3C]. Compute bitwise XOR for each byte.

### Chit #E9 [SPARE-4] — Affine Cipher (Unit 1)
* **Tier & Marks:** Easy (Spare) (10 Marks)
* **Cipher Category:** Affine Cipher (Unit 1)
* **Scenario:** Orbital Targeting Protocol Encryption
* **Intercepted Ciphertext:** `U Z I P G`
* **Clue:** An intercepted orbital telemetry burst was encrypted using the affine transformation C ≡ (5 · P + 8) mod 26.
* **Formula & Hints:** Decryption Formula: P_i ≡ a^(-1) · (C_i - b) mod 26. Given: a = 5, b = 8. Pre-computed modular inverse: 5^(-1) mod 26 = 21 (since 5 · 21 = 105 = 4 · 26 + 1 ≡ 1). Decryption: P_i ≡ 21 · (C_i - 8) mod 26. Alphabet: A=0, B=1 ... Z=25.

### Chit #E10 [SPARE-5] — Vernam Bitwise XOR Stream (Unit 1)
* **Tier & Marks:** Easy (Spare) (10 Marks)
* **Cipher Category:** Vernam Bitwise XOR Stream Cipher (Unit 1)
* **Scenario:** Emergency Transponder Stream Decryption
* **Intercepted Ciphertext:** `0x12  0x13  0x04  0x1C  0x1F`
* **Clue:** An emergency distress burst of 5 bytes was encrypted bit-by-bit using Vernam stream XOR with the ASCII key string 'STARK'.
* **Formula & Hints:** Formula: Plaintext_Byte P_i = C_i ⊕ K_i. Given Key 'STARK' in Hex ASCII: S = 0x53 (01010011_2), T = 0x54 (01010100_2), A = 0x41 (01000001_2), R = 0x52 (01010010_2), K = 0x4B (01001011_2). Compute bitwise XOR for each byte to recover the ASCII characters.

---

## 🔴 BOWL 2: HARD CHITS (#H1 to #H10) — 20 MARKS EACH

### Chit #H1 — Hill Cipher (Unit 1)
* **Tier & Marks:** Hard (20 Marks)
* **Cipher Category:** Hill Cipher (Unit 1)
* **Scenario:** Tactical Encryption Matrix Inversion
* **Intercepted Ciphertext:** `IE RR`
* **Clue:** A 4-letter defense token was encrypted using a 2x2 Hill matrix K = [[3, 2], [5, 7]] modulo 26.
* **Formula & Hints:** Decryption formula: P ≡ K^(-1) * C mod 26. Pre-computed inverse key matrix: K^(-1) ≡ [[3, 14], [9, 5]] mod 26. Compute vector multiplication for digraphs [I(8), E(4)] and [R(17), R(17)].

### Chit #H2 — DES & 3DES Block Cipher (Unit 2)
* **Tier & Marks:** Hard (20 Marks)
* **Cipher Category:** DES Feistel Network & S-Box (Unit 2)
* **Scenario:** Hardware Cryptographic Register Reconstruction
* **Intercepted Ciphertext:** `L_1 = 1100 (binary), R_1 = 1010 (binary) | S-Box 1 Input: 101010 (6 bits)`
* **Clue:** Recover the initial 8-bit input (L_0, R_0) before Round 1 of DES. Also explain the 3DES EDE decryption order.
* **Formula & Hints:** 1. S-Box 1 Input '101010': Outer bits 1&6 = 10_2 (Row 2), Inner bits 2-5 = 0101_2 (Col 5) -> S-Box 1 Row 2 Col 5 = 11 = 1011_2. 2. Feistel inverse: R_0 = L_1 = 1100_2, L_0 = R_1 ⊕ f(R_0) = 1010_2 ⊕ 1011_2 = 0001_2. 3. 3DES EDE Decryption order: D_K1(E_K2(D_K3(C))).

### Chit #H3 — AES / Rijndael Block Cipher (Unit 2)
* **Tier & Marks:** Hard (20 Marks)
* **Cipher Category:** AES State Matrix Operations (Unit 2)
* **Scenario:** Reversing AES Final Round Transformations
* **Intercepted Ciphertext:** `State Column: [0x76, 0x2B, 0xAF, 0x63] | Round Key K_10: [0x50, 0x1A, 0xC3, 0x02]`
* **Clue:** Reverse the final round of AES (where MixColumns is omitted) by applying InvShiftRows, InvSubBytes, and AddRoundKey.
* **Formula & Hints:** 1. AddRoundKey: State ⊕ K_10. For byte 1: 0x76 ⊕ 0x50 = 0x26. 2. InvSubBytes lookup (provided): InvSBox[0x26] = 0x4D ('M'), InvSBox[0x31] = 0x49 ('I'), etc. Recover the 4-byte plaintext word.

### Chit #H4 — Blowfish Block Cipher (Unit 2)
* **Tier & Marks:** Hard (20 Marks)
* **Cipher Category:** Blowfish Block Cipher (Unit 2)
* **Scenario:** Feistel Round Evaluation & Key-Dependent S-Boxes
* **Intercepted Ciphertext:** `Input Word: (a, b, c, d) | S_1[a]=10, S_2[b]=20, S_3[c]=5, S_4[d]=15 | L_1 = 50`
* **Clue:** Calculate the Blowfish round function F(a,b,c,d) and recover the previous left register L_0 = L_1 ⊕ F.
* **Formula & Hints:** Blowfish Round Formula: F(a,b,c,d) = ((S_1[a] + S_2[b] mod 2^32) ⊕ S_3[c]) + S_4[d] mod 2^32. Here: ((10 + 20) ⊕ 5) + 15 = (30 ⊕ 5) + 15 = 27 + 15 = 42. Then compute L_0 = 50 ⊕ 42.

### Chit #H5 — RC5 Block Cipher (Unit 2)
* **Tier & Marks:** Hard (20 Marks)
* **Cipher Category:** RC5 Block Cipher (Unit 2)
* **Scenario:** Data-Dependent Circular Bit Rotation Inversion
* **Intercepted Ciphertext:** `Register A = 0x9A, Register B = 3 (rotate amount) | Subkey S[0] = 0x00`
* **Clue:** Invert an RC5 half-round rotation to retrieve original 8-bit plaintext register A.
* **Formula & Hints:** RC5 Half-Round Decryption: A = ((A - S[0]) >>> B) ⊕ B. Given A = 0x9A (10011010_2). Rotate right circularly by 3 bits: 01010011_2 = 0x53 ('S'). Finally XOR with 0 (since S[0]=0).

### Chit #H6 — IDEA Block Cipher (Unit 2)
* **Tier & Marks:** Hard (20 Marks)
* **Cipher Category:** IDEA Block Cipher (Unit 2)
* **Scenario:** Modular Multiplication Inversion mod (2^16 + 1)
* **Intercepted Ciphertext:** `Output Sub-block Y = 135 | Subkey Z = 9 (modulo 65537)`
* **Clue:** IDEA mixes XOR, addition mod 2^16, and multiplication mod 65537. Invert the multiplication step to find plaintext sub-block X.
* **Formula & Hints:** Formula: X = (Y * Z^(-1)) mod 65537. Given pre-computed modular inverse: Z^(-1) = 9^(-1) mod 65537 = 7282 (since 9 * 7282 = 65538 ≡ 1 mod 65537). Calculate (135 * 7282) mod 65537.

### Chit #H7 — RSA Public-Key Algorithm (Unit 2)
* **Tier & Marks:** Hard (20 Marks)
* **Cipher Category:** RSA Algorithm (Unit 2)
* **Scenario:** Missile Defense Cryptographic Key Recovery
* **Intercepted Ciphertext:** `Public Primes: p = 5, q = 11 | Public Exponent: e = 3 | Ciphertext: c = 14`
* **Clue:** Derive the private key d and decrypt ciphertext c = 14 to reveal the plaintext integer m.
* **Formula & Hints:** 1. Compute n = p*q = 55, φ(n) = (p-1)*(q-1) = 40. 2. Find d where 3*d ≡ 1 mod 40 -> d = 27 (since 3*27 = 81 = 2*40 + 1). 3. Decrypt: m = c^d mod n = 14^27 mod 55. (Hint: 14^2 ≡ 31, 14^4 ≡ 26, 14^8 ≡ 16, 14^16 ≡ 36; 14^27 = 36*16*31*14 mod 55 = 9).

### Chit #H8 — ElGamal Cryptography (Unit 2)
* **Tier & Marks:** Hard (20 Marks)
* **Cipher Category:** ElGamal Cryptography (Unit 2)
* **Scenario:** Quantum-Safe Asymmetric Decryption
* **Intercepted Ciphertext:** `Prime p = 23, Generator g = 5 | Public Key y = 8, Private Key x = 6 | Ciphertext Pair: (c_1 = 19, c_2 = 18)`
* **Clue:** Decrypt the ElGamal ciphertext pair (c_1, c_2) using private key x = 6.
* **Formula & Hints:** Decryption Steps: 1. Compute shared secret: s = c_1^x mod p = 19^6 mod 23 = 2. 2. Find modular inverse s^(-1) mod 23: 2 * 12 = 24 ≡ 1 mod 23 -> s^(-1) = 12. 3. Recover plaintext: m = (c_2 * s^(-1)) mod p = (18 * 12) mod 23 = 216 mod 23 = 9.

### Chit #H9 [SPARE-4] — Diffie-Hellman Key Exchange (Unit 2)
* **Tier & Marks:** Hard (Spare) (20 Marks)
* **Cipher Category:** Diffie-Hellman Key Exchange (Unit 2)
* **Scenario:** S.H.I.E.L.D. Secure Session Key Derivation
* **Intercepted Ciphertext:** `Modulus p = 31, Generator g = 3 | Private Key a = 4 | Intercepted Public Key B = 13`
* **Clue:** Vision and Banner establish a secure link. Using public modulus p = 31, Alice's private key a = 4, and Bob's public value B = 13, calculate the shared secret session key K_AB.
* **Formula & Hints:** Formula: Shared Secret K_AB ≡ B^a mod p = 13^4 mod 31. Step-by-step modular squaring: 1. 13^2 = 169. Since 169 = 5 · 31 + 14, 13^2 ≡ 14 mod 31. 2. 13^4 = (13^2)^2 ≡ 14^2 = 196 mod 31. 3. Find 196 mod 31.

### Chit #H10 [SPARE-5] — AES MixColumns Transformation in GF(2^8) (Unit 2)
* **Tier & Marks:** Hard (Spare) (20 Marks)
* **Cipher Category:** AES MixColumns in GF(2^8) (Unit 2)
* **Scenario:** Rijndael Diffusion Layer Hardware Simulation
* **Intercepted Ciphertext:** `State Column: [0x25, 0x12, 0x31, 0x1E]^T | Matrix Row: [02, 03, 01, 01]`
* **Clue:** Calculate the first output byte d_0 of the AES MixColumns transformation in the Galois Field GF(2^8) with irreducible polynomial m(x) = x^8 + x^4 + x^3 + x + 1 (0x11B). Convert the resulting hex byte to its ASCII character.
* **Formula & Hints:** MixColumns Formula: d_0 = (02 • 0x25) ⊕ (03 • 0x12) ⊕ (01 • 0x31) ⊕ (01 • 0x1E). Rules in GF(2^8): 1. (02 • b): Left shift by 1 bit (if original MSB was 1, XOR with 0x1B). Since 0x25 MSB=0 -> 02 • 0x25 = 0x4A. 2. (03 • b) = (02 • b) ⊕ b. For 0x12: 02 • 0x12 = 0x24 -> 03 • 0x12 = 0x24 ⊕ 0x12 = 0x36. 3. 01 • b = b. Compute d_0 = 0x4A ⊕ 0x36 ⊕ 0x31 ⊕ 0x1E.
