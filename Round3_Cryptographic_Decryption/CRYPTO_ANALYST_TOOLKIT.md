# 🛠️ ROUND 3: CRYPTO ANALYST REFERENCE TOOLKIT
## Official Syllabus & Formula Reference (Units 1 & 2)
### Approved for Contestant Use during Phase 2 (Decryption Bowl Round)

---

### 1. English Alphabet Index (0-Indexed: A=0 to Z=25)

| Char | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Num** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

---

### 2. Standard ASCII Table (Hex, Decimal & Character Reference)

| Char | Dec | Hex | Binary | Char | Dec | Hex | Binary |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Space** | 32 | 0x20 | 00100000 | **N** | 78 | 0x4E | 01001110 |
| **A** | 65 | 0x41 | 01000001 | **O** | 79 | 0x4F | 01001111 |
| **B** | 66 | 0x42 | 01000010 | **P** | 80 | 0x50 | 01010000 |
| **C** | 67 | 0x43 | 01000011 | **Q** | 81 | 0x51 | 01010001 |
| **D** | 68 | 0x44 | 01000100 | **R** | 82 | 0x52 | 01010010 |
| **E** | 69 | 0x45 | 01000101 | **S** | 83 | 0x53 | 01010011 |
| **F** | 70 | 0x46 | 01000110 | **T** | 84 | 0x54 | 01010100 |
| **G** | 71 | 0x47 | 01000111 | **U** | 85 | 0x55 | 01010101 |
| **H** | 72 | 0x48 | 01001000 | **V** | 86 | 0x56 | 01010110 |
| **I** | 73 | 0x49 | 01001001 | **W** | 87 | 0x57 | 01010111 |
| **J** | 74 | 0x4A | 01001010 | **X** | 88 | 0x58 | 01011000 |
| **K** | 75 | 0x4B | 01001011 | **Y** | 89 | 0x59 | 01011001 |
| **L** | 76 | 0x4C | 01001100 | **Z** | 90 | 0x5A | 01011010 |
| **M** | 77 | 0x4D | 01001101 | **0..9** | 48..57| 0x30..0x39 | 00110000..00111001 |

---

## 🟢 UNIT 1 & 2: EASY ALGORITHMS REFERENCE

### 1. Caesar Shift Cipher (Unit 1)
* **Encryption:** $C_i \equiv (P_i + k) \pmod{26}$
* **Decryption:** $P_i \equiv (C_i - k) \pmod{26}$ *(add 26 if $C_i - k < 0$)*

### 2. Monoalphabetic Substitution Cipher (Unit 1)
Direct substitution mapping where each plaintext letter corresponds to a unique ciphertext character.
```
Plain : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Cipher: Q W E R T Y U I O P A S D F G H J K L Z X C V B N M
```

### 3. Vigenère Cipher (Unit 1)
Polyalphabetic shift repeated across a keyword $K$:
* **Decryption:** $P_i \equiv (C_i - K_{i \pmod{|K|}}) \pmod{26}$

### 4. One-Time Pad (OTP) / Vernam Cipher (Unit 1)
Perfect secrecy cipher combining random key letters of equal length:
* **Decryption:** $P_i \equiv (C_i - K_i) \pmod{26}$ (or bitwise $P_i = C_i \oplus K_i$)

### 5. Rail Fence Cipher (Unit 1)
Transposition across $D$ rows in a zig-zag wave. For 3 rails:
```
Rail 1: 0 . . . 4 . . . 8 . . . 12 . .
Rail 2: . 1 . 3 . 5 . 7 . 9 . 11 . 13 .
Rail 3: . . 2 . . . 6 . . . 10 . . . 14
```

### 6. Row-Column (Columnar) Transposition (Unit 1)
Plaintext is written horizontally in a matrix under a keyword. Columns are numbered in alphabetical order of keyword letters, and read out column-by-column. To decrypt: write into columns according to key order and read out row-by-row.

### 7. Playfair Cipher (Unit 1)
$5 	imes 5$ matrix generated from a keyword (I and J share a cell). Decrypt digraphs by:
1. **Same Row:** Shift each letter **left** by 1 position (wrap right).
2. **Same Column:** Shift each letter **up** by 1 position (wrap bottom).
3. **Rectangle:** Swap columns (take letter in same row, opposite corner).

### 8. RC4 Stream Cipher (Unit 2)
Stream cipher utilizing the KSA and PRGA to generate a pseudorandom keystream byte array $K$:
* **Decryption:** $P_i = C_i \oplus K_i$ *(bitwise XOR)*

### 9. Affine Cipher (Unit 1)
Combines multiplication and addition modulo 26:
* **Encryption:** $C_i \equiv (a \cdot P_i + b) \pmod{26}$ where $\gcd(a, 26) = 1$.
* **Decryption:** $P_i \equiv a^{-1} \cdot (C_i - b) \pmod{26}$ *(using modular inverse $a^{-1} \pmod{26}$)*.

### 10. Vernam Bitwise XOR Stream Cipher (Unit 1 / Unit 2)
Applies bitwise exclusive-OR ($\oplus$) between each 8-bit plaintext character byte and key byte:
* **Decryption:** $P_i = C_i \oplus K_i$.
* **Truth Table:** $0 \oplus 0 = 0$, $0 \oplus 1 = 1$, $1 \oplus 0 = 1$, $1 \oplus 1 = 0$.

---

## 🔴 UNIT 1 & 2: HARD ALGORITHMS REFERENCE

### 1. Hill Cipher (Unit 1)
For a $2 	imes 2$ Key Matrix $K = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
* **Determinant:** $\det(K) = (ad - bc) \pmod{26}$
* **Modular Multiplicative Inverse:** Find $(\det K)^{-1} \pmod{26}$ such that $\det(K) \times (\det K)^{-1} \equiv 1 \pmod{26}$.
* **Adjugate Matrix:** $\text{adj}(K) \equiv \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \pmod{26}$
* **Decryption Matrix:** $K^{-1} \equiv (\det K)^{-1} \cdot \text{adj}(K) \pmod{26}$
* **Decryption Equation:** $\begin{pmatrix} P_1 \\ P_2 \end{pmatrix} \equiv K^{-1} \begin{pmatrix} C_1 \\ C_2 \end{pmatrix} \pmod{26}$

**Modulo 26 Inverses Table:**
| $x$ | 1 | 3 | 5 | 7 | 9 | 11 | 15 | 17 | 19 | 21 | 23 | 25 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$x^{-1} \pmod{26}$** | 1 | 9 | 21 | 15 | 3 | **19** | 7 | 23 | 11 | 5 | 17 | 25 |

### 2. DES & 3DES — Data Encryption Standard (Unit 2)
16-round Feistel cipher.
* **Feistel Round Decryption:**
  $$R_{i-1} = L_i$$
  $$L_{i-1} = R_i \oplus f(R_{i-1}, K_i)$$
* **DES S-Box 1 Table (Input 6-bit $b_1 b_2 b_3 b_4 b_5 b_6$: Row = $b_1 b_6$, Col = $b_2 b_3 b_4 b_5$):**

| Row \ Col | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Row 0 (00)** | 14 | 4 | 13 | 1 | 2 | 15 | 11 | 8 | 3 | 10 | 6 | 12 | 5 | 9 | 0 | 7 |
| **Row 1 (01)** | 0 | 15 | 7 | 4 | 14 | 2 | 13 | 1 | 10 | 6 | 12 | 11 | 9 | 5 | 3 | 8 |
| **Row 2 (10)** | 4 | 1 | 14 | 8 | 13 | 6 | 2 | 11 | 15 | 12 | 9 | 7 | 3 | 10 | 5 | 0 |
| **Row 3 (11)** | 15 | 12 | 8 | 2 | 4 | 9 | 1 | 7 | 5 | 11 | 3 | 14 | 10 | 0 | 6 | 13 |

* **3DES EDE Mode:** Encryption: $C = E_{K3}(D_{K2}(E_{K1}(P)))$. Decryption: $P = D_{K1}(E_{K2}(D_{K3}(C)))$.

### 3. AES — Advanced Encryption Standard (Unit 2)
State matrix transformations across rounds:
* **AddRoundKey:** $\text{State} \oplus \text{RoundKey}$
* **InvSubBytes:** Substitute bytes using the Inverse S-Box.
* **InvShiftRows:** Row 0: no shift; Row 1: right 1; Row 2: right 2; Row 3: right 3.
* **MixColumns Transformation in $\text{GF}(2^8)$:** Multiplies state column by fixed matrix.
  - Multiplication by $02$ ($02 \bullet b$): Left shift $b$ by 1 bit (`b << 1`). If the original MSB of $b$ was 1, XOR with irreducible polynomial `0x1B`.
  - Multiplication by $03$ ($03 \bullet b$): $(02 \bullet b) \oplus b$.
  - Multiplication by $01$: Identity ($01 \bullet b = b$).

### 4. Blowfish (Unit 2)
16-round Feistel cipher with key-dependent S-boxes $S_1, S_2, S_3, S_4$:
* **Round Function:** $F(a, b, c, d) = ((S_1[a] + S_2[b] \bmod 2^{32}) \oplus S_3[c]) + S_4[d] \bmod 2^{32}$
* **Feistel Step:** $L_0 = R_1 \oplus F(R_0, K_1)$

### 5. RC5 Block Cipher (Unit 2)
Word-oriented cipher based on data-dependent circular bit rotations ($\lll$ and $\ggg$):
* **Half-Round Inversion:**
  $$B = ((B - S[2i+1]) \ggg A) \oplus A$$
  $$A = ((A - S[2i]) \ggg B) \oplus B$$

### 6. IDEA — International Data Encryption Algorithm (Unit 2)
Combines three algebraic groups on 16-bit words:
1. Bitwise XOR ($\oplus$)
2. Addition modulo $2^{16}$ ($\boxplus$) -> Inverse is $(-Z) \bmod 2^{16} = 2^{16} - Z$.
3. Multiplication modulo $2^{16}+1$ ($\odot$, where 0 represents $2^{16}$) -> Inverse is $Z^{-1} \bmod (2^{16}+1)$.

### 7. RSA Public-Key Cryptosystem (Unit 2)
* **Key Generation:**
  1. Select distinct primes $p, q$. Compute $n = p \cdot q$.
  2. Compute Euler's totient: $\phi(n) = (p - 1)(q - 1)$.
  3. Select public exponent $e$ such that $\gcd(e, \phi(n)) = 1$.
  4. Compute private exponent $d \equiv e^{-1} \pmod{\phi(n)}$ ($e \cdot d \equiv 1 \pmod{\phi(n)}$).
* **Decryption:** $M \equiv C^d \pmod n$

### 8. ElGamal Cryptosystem (Unit 2)
Based on Discrete Logarithms over cyclic group $\mathbb{Z}_p^*$:
* **Public Key:** $y = g^x \pmod p$ (where $x$ is private key, $g$ is generator, $p$ is prime).
* **Ciphertext Pair:** $(c_1, c_2) = (g^k \bmod p, \; m \cdot y^k \bmod p)$.
* **Decryption Procedure:**
  1. Compute shared secret: $s \equiv c_1^x \pmod p$.
  2. Find modular inverse $s^{-1} \pmod p$ such that $s \cdot s^{-1} \equiv 1 \pmod p$.
  3. Recover plaintext: $m \equiv (c_2 \cdot s^{-1}) \pmod p$.

### 9. Diffie-Hellman Key Exchange (Unit 2)
Enables two parties to establish a shared secret key across an insecure channel:
* **Public Parameters:** Prime $p$, Primitive Root / Generator $g$.
* **Private Keys:** Alice chooses $a$, Bob chooses $b$.
* **Public Values:** Alice sends $A = g^a \bmod p$, Bob sends $B = g^b \bmod p$.
* **Shared Secret Calculation:**
  $$K_{AB} \equiv B^a \pmod p \equiv (g^b)^a \equiv g^{ab} \equiv (g^a)^b \equiv A^b \pmod p$$
