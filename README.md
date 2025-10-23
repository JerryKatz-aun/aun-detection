[![PyPI version](https://img.shields.io/pypi/v/aun-detection.svg?color=blue)](https://pypi.org/project/aun-detection/)
[![Python versions](https://img.shields.io/pypi/pyversions/aun-detection.svg?color=brightgreen)](https://pypi.org/project/aun-detection/)
[![GitHub release](https://img.shields.io/github/v/release/halifaxjerrykatz-dotcom/aun-detection?include_prereleases&color=blue)](https://github.com/halifaxjerrykatz-dotcom/aun-detection/releases)
[![Downloads](https://static.pepy.tech/badge/aun-detection)](https://pepy.tech/project/aun-detection)
[![Downloads/month](https://static.pepy.tech/badge/aun-detection/month)](https://pepy.tech/project/aun-detection)
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

```python
from aun_detection.operator import aun_filter

# Two key-like inputs
key1 = "c87af89e12dd45abde"
key2 = "deab54dd21e98fa78c"  # a rotated + mirror
