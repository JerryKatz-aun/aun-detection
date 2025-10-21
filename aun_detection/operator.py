# aun_detection/operator.py
"""
∿ aun-detection: AI Mimicry Detection using Symbolic Collapse Logic

This module defines the core aun_filter() function, which compares
two cryptographic strings (wallets, keys, certificates, etc.) and
detects symbolic or structural mimicry using simple similarity metrics.
"""

import math

def aun_filter(A: str, B: str, t: float = 0.9, s_min: int = 5):
    """
    Compare two strings for AI-generated mimicry.

    Parameters:
        A (str): First string (e.g. real wallet address)
        B (str): Second string (suspected mimic)
        t (float): Similarity threshold (0–1). Higher = stricter.
        s_min (int): Minimum string length for comparison.

    Returns:
        None if mimicry detected (collapse event ∿)
        Tuple (similarity_score, 'PASS') otherwise
    """

    # Normalize
    A, B = A.strip(), B.strip()

    # Quick check: short strings not valid for detection
    if len(A) < s_min or len(B) < s_min:
        return None

    # Ensure equal length (pad shorter one)
    max_len = max(len(A), len(B))
    A = A.ljust(max_len)
    B = B.ljust(max_len)

    # Compute Hamming similarity
    matches = sum(a == b for a, b in zip(A, B))
    similarity = matches / max_len

    # Collapse logic: if too similar but not identical → mimic
    if 0.0 < similarity < 1.0 and similarity >= t:
        print("∿ Collapse detected: structural mimicry.")
        return None  # collapse event

    # If perfectly different, or below threshold → safe
    return (similarity, "PASS")

