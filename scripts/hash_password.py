#!/usr/bin/env python3
"""Utility to generate a hashed password for storing in teacher credentials.

Usage:
  python scripts/hash_password.py <plaintext-password>

Outputs the hashed password to stdout.
"""
import sys
from src.security import hash_password


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/hash_password.py <plaintext-password>")
        sys.exit(2)
    pwd = sys.argv[1]
    print(hash_password(pwd))


if __name__ == "__main__":
    main()
