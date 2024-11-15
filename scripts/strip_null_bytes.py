#!/usr/bin/env python3
"""Strip null bytes from corrupted output samples before archival."""
import sys
import os

def strip_nulls(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    cleaned = data.replace(b'\x00', b'')
    if len(data) != len(cleaned):
        print(f"Stripped {len(data) - len(cleaned)} null bytes from {filepath}")
        with open(filepath, 'wb') as f:
            f.write(cleaned)
    else:
        print(f"No null bytes found in {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: strip_null_bytes.py <file> [file ...]")
        sys.exit(1)
    for path in sys.argv[1:]:
        if os.path.exists(path):
            strip_nulls(path)
        else:
            print(f"File not found: {path}", file=sys.stderr)
