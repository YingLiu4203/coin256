#!/usr/bin/env python3
"""
Example: Generating 256 bits of randomness using Python's secrets module

This demonstrates the proper way to generate cryptographically secure random data,
equivalent to flipping a coin 256 times.
"""

import secrets

def generate_256_bit_key():
    """
    Generate a 256-bit (32-byte) cryptographically secure random key.
    
    Returns:
        tuple: (bytes, hex_string, binary_string)
    """
    # Generate 32 random bytes (256 bits)
    random_bytes = secrets.token_bytes(32)
    
    # Convert to hexadecimal representation
    hex_string = random_bytes.hex()
    
    # Convert to binary representation
    binary_string = ''.join(format(byte, '08b') for byte in random_bytes)
    
    return random_bytes, hex_string, binary_string


def simulate_coin_flips(num_flips=256):
    """
    Simulate flipping a coin num_flips times.
    
    Args:
        num_flips: Number of coin flips to simulate (default: 256)
    
    Returns:
        tuple: (binary_string, hex_string)
    """
    # Generate random bits (0 or 1 for each flip)
    flips = [secrets.randbelow(2) for _ in range(num_flips)]
    
    # Convert to binary string
    binary_string = ''.join(str(bit) for bit in flips)
    
    # Convert binary string to bytes then to hex
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        byte_array.append(int(byte, 2))
    
    hex_string = byte_array.hex()
    
    return binary_string, hex_string


def main():
    print("=" * 60)
    print("256-Bit Cryptographic Key Generation Example")
    print("=" * 60)
    print()
    
    # Method 1: Using secrets.token_bytes
    print("Method 1: Using Python's secrets module")
    print("-" * 60)
    key_bytes, key_hex, key_binary = generate_256_bit_key()
    
    print(f"Raw bytes: {key_bytes}")
    print(f"\nHex representation ({len(key_hex)} characters):")
    print(key_hex)
    print(f"\nBinary representation ({len(key_binary)} bits):")
    print(key_binary[:64] + "...")  # Show first 64 bits
    print(f"(Total: {len(key_binary)} bits)")
    print()
    
    # Method 2: Simulating coin flips
    print("\nMethod 2: Simulating 256 coin flips")
    print("-" * 60)
    flip_binary, flip_hex = simulate_coin_flips(256)
    
    print(f"Binary representation ({len(flip_binary)} bits):")
    print(flip_binary[:64] + "...")  # Show first 64 bits
    print(f"\nHex representation ({len(flip_hex)} characters):")
    print(flip_hex)
    print()
    
    # Show entropy calculation
    print("\nEntropy Information")
    print("-" * 60)
    print(f"Bits of entropy: 256")
    print(f"Possible combinations: 2^256")
    print(f"Approximate value: 1.16 × 10^77")
    print(f"For comparison: ~10^80 atoms in the observable universe")
    print()
    
    print("=" * 60)
    print("Both methods produce cryptographically secure 256-bit keys!")
    print("=" * 60)


if __name__ == "__main__":
    main()
