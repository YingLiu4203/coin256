# Chapter 2: Cryptographic Foundations

## Overview

This chapter explores the fundamental building blocks of cryptographic systems that enable information and property freedom.

## Core Cryptographic Primitives

### 1. Hash Functions

Hash functions are mathematical functions that convert input data of any size into a fixed-size output (hash or digest).

**Properties:**
- **Deterministic**: Same input always produces same output
- **Fast computation**: Efficient to calculate
- **Pre-image resistance**: Cannot reverse the function
- **Collision resistance**: Difficult to find two inputs with same output
- **Avalanche effect**: Small input change creates completely different output

**Common hash functions:**
- SHA-256 (Secure Hash Algorithm 256-bit)
- SHA-3
- BLAKE2

### 2. Symmetric Encryption

Symmetric encryption uses the same key for both encryption and decryption.

**Characteristics:**
- Fast and efficient
- Requires secure key exchange
- Examples: AES, ChaCha20

### 3. Asymmetric Encryption

Asymmetric encryption uses a pair of keys: public key (for encryption) and private key (for decryption).

**Characteristics:**
- Enables secure communication without prior key exchange
- Slower than symmetric encryption
- Foundation for digital signatures
- Examples: RSA, Elliptic Curve Cryptography (ECC)

### 4. Digital Signatures

Digital signatures prove authenticity and integrity of messages.

**Process:**
1. Create hash of message
2. Sign hash with private key
3. Anyone can verify with public key

**Properties:**
- Authentication: Proves sender identity
- Integrity: Detects message tampering
- Non-repudiation: Sender cannot deny signing

## Cryptographic Security

### Security Levels

- **128-bit security**: Requires 2^128 operations to break
- **256-bit security**: Requires 2^256 operations to break

### Real-world Context

To understand 256-bit security:
- More combinations than atoms in the observable universe
- Would take billions of years with all computing power on Earth
- Considered secure against quantum computers (for symmetric encryption)

## Mathematical Foundations

### Prime Numbers

Large prime numbers are essential for:
- RSA encryption
- Generating cryptographic keys
- Ensuring system security

### Elliptic Curves

Modern cryptographic systems often use elliptic curve mathematics:
- More efficient than traditional methods
- Smaller key sizes for equivalent security
- Used in Bitcoin and other cryptocurrencies

## Practical Applications

These cryptographic foundations enable:
- Secure messaging (Signal, WhatsApp)
- Cryptocurrency transactions
- Digital identity systems
- Secure web browsing (HTTPS/TLS)
- Password protection

## Exercises

1. Calculate the SHA-256 hash of your name
2. Understand the difference between symmetric and asymmetric encryption
3. Explore how digital signatures work with a simple example

## Next Steps

Continue to [Chapter 3: Randomness and Entropy](../chapter-03-randomness-entropy/) to understand how randomness creates security.

---

*This chapter is part of the Coin256 book. Contributions and improvements are welcome!*
