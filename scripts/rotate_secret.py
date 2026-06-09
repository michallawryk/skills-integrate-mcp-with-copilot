#!/usr/bin/env python3
"""Generate a new SECRET_KEY and optionally write it to a .env file.

This repository ignores `.env`; to rotate your secret run this script and
place the printed value into your deployment environment or into a local
.env file (not committed).
"""
import secrets
import argparse
from pathlib import Path


def generate_secret(n_bytes: int = 32) -> str:
    return secrets.token_urlsafe(n_bytes)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-dotenv", action="store_true",
                        help="Write SECRET_KEY to a local .env file (overwrites SECRET_KEY if present).")
    args = parser.parse_args()

    new_secret = generate_secret()
    print(new_secret)

    if args.write_dotenv:
        env_path = Path(".env")
        content = []
        if env_path.exists():
            content = env_path.read_text().splitlines()

        # Replace or append
        updated = False
        for i, line in enumerate(content):
            if line.startswith("SECRET_KEY="):
                content[i] = f"SECRET_KEY={new_secret}"
                updated = True
                break
        if not updated:
            content.append(f"SECRET_KEY={new_secret}")

        env_path.write_text("\n".join(content) + "\n")
        print(f"Wrote new SECRET_KEY to {env_path}")


if __name__ == "__main__":
    main()
