[![PyPI version](https://img.shields.io/pypi/v/aun-detection.svg?color=blue)](https://pypi.org/project/aun-detection/)
[![Python versions](https://img.shields.io/pypi/pyversions/aun-detection.svg?color=brightgreen)](https://pypi.org/project/aun-detection/)
[![GitHub release](https://img.shields.io/github/v/release/halifaxjerrykatz-dotcom/aun-detection?color=blue)](https://github.com/halifaxjerrykatz-dotcom/aun-detection/releases)
[![Downloads](https://static.pepy.tech/badge/aun-detection?color=blue)](https://pepy.tech/project/aun-detection)
[![Monthly downloads](https://static.pepy.tech/badge/aun-detection/month?color=blue)](https://pepy.tech/project/aun-detection)
[📄 Whitepaper](https://github.com/halifaxjerrykatz-dotcom/aun-detection/raw/main/docs/whitepaper.pdf)

📦 **Install with:**
```bash
pip install aun-detection
```

<p align="center">
  <img src="https://github.com/halifaxjerrykatz-dotcom/aun-detection/raw/main/docs/logo.png" alt="∿ aun-detection" width="80"/>
</p>
<p align="center"><em>A symbolic collapse logic filter for AI mimicry detection</em></p>

# ∿ aun-detection

**The First AI Mimicry Filter for Digital Credentials**  
A symbolic collapse filter that detects structural mimicry in cryptographic inputs like wallet addresses, API keys, certificates, and more.

---

## 🔍 What It Does

AI can generate digital credentials that *look* legitimate — but aren't.  
`aun-detection` uses structural logic, not ML, to detect and collapse these mimics.

---

## 🚀 Features

- ∿ Symbolic filtering based on collapse logic  
- Detects AI-generated mimics of:
  - Wallet addresses  
  - SSL certificates  
  - API keys  
  - PKI credentials  
- Hamming + structural transform scoring  
- < 3ms detection runtime  
- Lightweight, explainable, no model training needed  

---

## 🧠 Usage Example

The `aun_filter()` function compares two string-like inputs — such as wallet addresses, API keys, or certificate fingerprints — and detects **mimicry**: patterns that are too structurally similar to trust.

```python
from aun_detection.operator import aun_filter

# Example: check for a spoofed wallet address
real_wallet = "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"
suspect_wallet = "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wl1"  # note the final '1' vs 'h'

result = aun_filter(real_wallet, suspect_wallet)

if result is None:
    print("🚨 Mimicry detected — credentials rejected.")
else:
    print(f"✅ Inputs passed. Dissimilarity score: {result}")
    print(f"✅ Inputs passed. Dissimilarity score: {result}")

    print(f"✅ Inputs passed. Dissimilarity score: {result}")


