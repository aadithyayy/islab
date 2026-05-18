A collection of Python and Shell programs for **Information Security Lab**, implementing classical ciphers, public-key cryptography, digital signatures, and hash functions.

Each script is independent and can be executed separately for the corresponding lab exercise.

---

## 📘 Program Overview

### 🔐 Ciphers (`ciphers/`)

| File            | Description                                        | Key Concept                          |
| --------------- | -------------------------------------------------- | ------------------------------------ |
| `caesar.py`     | Encrypts and decrypts text using the Caesar cipher | Substitution, shift by key           |
| `vigenere.py`   | Implements the Vigenère cipher with a keyword      | Polyalphabetic substitution          |
| `playfair.py`   | Encrypts plaintext using the Playfair cipher       | Digraph substitution, 5×5 key matrix |
| `hill.py`       | Encrypts text using the Hill cipher                | Matrix multiplication mod 26         |
| `rail_fence.py` | Implements Rail Fence transposition cipher         | Zigzag row permutation               |
| `columnar.py`   | Implements Columnar Transposition cipher           | Column reordering by keyword         |

### 🔑 Public Key & Signatures (root)

| File          | Description                                          | Key Concept                                                     |
| ------------- | ---------------------------------------------------- | --------------------------------------------------------------- |
| `rsa.py`      | RSA key generation, encryption and decryption        | `sympy.gcd`, `mod_inverse`, `pow(m,e,n)`                        |
| `rsa_sign.py` | RSA digital signature — sign and verify a message    | `hashlib.sha256`, sign with private key, verify with public key |
| `sha.py`      | SHA-256 hash of two strings and bit-difference count | `hashlib.sha256`, XOR of hex digests                            |
| `filecopy.py` | Low-level file copy using OS system calls            | `os.open`, `os.read`, `os.write`                                |

### 🐚 Shell Scripts (`shell/`)

| File            | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| `user_mgmt.sh`  | User and group management commands                          |
| `file_perms.sh` | File permission and ownership operations (`chmod`, `chown`) |
| `firewall.sh`   | Basic firewall rules using `iptables` / `ufw`               |
| `sysinfo.sh`    | Displays system information (CPU, memory, disk)             |

> **Note:** Shell scripts require a Linux/Unix environment. Run with `bash <script>.sh` or grant execute permission first.

---

## ⚙️ Usage

1. Clone the repository:

```bash
git clone https://github.com/Binahaagit/is_lab.git
cd is_lab
```

2. Install required Python library:

```bash
pip install sympy
```

3. Run any Python program:

```bash
python rsa.py
```

4. Run a shell script:

```bash
bash shell/user_mgmt.sh
```

5. Follow the on-screen prompts to provide input.

---

## 📚 Key Functions & Modules Used

### 🔢 sympy

- `sympy.gcd(a, b)` — Compute GCD to find valid RSA public exponents
- `sympy.mod_inverse(e, phi)` — Compute modular inverse for RSA private key

### 🔒 hashlib

- `hashlib.sha256(msg.encode()).hexdigest()` — Generate SHA-256 hash of a string
- `int(hash, 16)` — Convert hex digest to integer for bitwise comparison or signing

### 🖥️ os (system calls)

- `os.open()` — Open a file using low-level OS file descriptor
- `os.read()` / `os.write()` — Read/write data at the OS level
- `os.close()` — Close file descriptor

### 🔣 Built-in

- `pow(base, exp, mod)` — Efficient modular exponentiation (used in RSA encrypt/decrypt/sign/verify)
- `bin(x).count('1')` — Count differing bits between two hashes (avalanche effect check)

---

## 📖 Concepts Covered

| Topic                                  | Programs                                             |
| -------------------------------------- | ---------------------------------------------------- |
| Classical substitution ciphers         | `caesar.py`, `vigenere.py`, `playfair.py`, `hill.py` |
| Transposition ciphers                  | `rail_fence.py`, `columnar.py`                       |
| Public-key cryptography (RSA)          | `rsa.py`                                             |
| Digital signatures                     | `rsa_sign.py`                                        |
| Hash functions & avalanche effect      | `sha.py`                                             |
| OS-level file operations               | `filecopy.py`                                        |
| Linux system & security administration | `shell/`                                             |
