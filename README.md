# ∿ aun-detection
[![PyPI version](https://img.shields.io/pypi/v/aun-detection.svg?color=blue)](https://pypi.org/project/aun-detection/)
[![Python versions](https://img.shields.io/pypi/pyversions/aun-detection.svg?color=brightgreen)](https://pypi.org/project/aun-detection/)
[![Downloads](https://static.pepy.tech/badge/aun-detection)](https://pepy.tech/project/aun-detection)
[![License](https://img.shields.io/pypi/l/aun-detection)](https://github.com/halifaxjerrykatz-dotcom/aun-detection/blob/main/LICENSE)

[![PyPI version](https://img.shields.io/pypi/v/aun-detection.svg?color=blue)](https://pypi.org/project/aun-detection/)
[![Python versions](https://img.shields.io/pypi/pyversions/aun-detection.svg?color=brightgreen)](https://pypi.org/project/aun-detection/)
[![GitHub release](https://img.shields.io/github/v/release/halifaxjerrykatz-dotcom/aun-detection?color=blue)](https://github.com/halifaxjerrykatz-dotcom/aun-detection/releases)
[![Downloads](https://static.pepy.tech/badge/aun-detection)](https://pepy.tech/project/aun-detection)
[![Downloads per month](https://static.pepy.tech/badge/aun-detection/month)](https://pepy.tech/project/aun-detection)
[📄 Whitepaper](https://github.com/halifaxjerrykatz-dotcom/aun-detection/raw/main/docs/whitepaper.pdf)

📦 **Install with:**  
`pip install aun-detection`

<p align="center">
  <img src="https://github.com/halifaxjerrykatz-dotcom/aun-detection/raw/main/docs/logo.png" alt="∿ aun-detection" width="80"/>
</p>
<p align="center"><em>A symbolic collapse logic filter for AI mimicry detection</em></p>

---

**The First AI Mimicry Filter for Digital Credentials**  
A symbolic collapse filter that detects structural mimicry in cryptographic inputs like wallet addresses, API keys, certificates, and more.

---

## ⚡ Quick Start

```bash
pip install aun-detection
```

```python
from aun_detection.operator import aun_filter

score = aun_filter("known_good_value", "suspect_value")

if score is None:
    print("🚨 Mimicry detected — credentials rejected.")
else:
    print(f"✅ Valid — dissimilarity score: {score:.4f}")
```

**Returns**
- `None`: mimicry detected (collapse threshold exceeded)
- `float`: dissimilarity score if credential passes

---

## 🔍 What It Does

AI can now generate credentials that *look* valid — near-perfect wallet, SSL, or API key spoofs.  
`aun-detection` collapses these mimics by analyzing structural logic rather than surface randomness.  
Use it for wallet validation, SSL integrity checks, API token screening, or CI/CD credential safety.

---

## 🚀 Features

- ∿ Symbolic filtering based on collapse logic  
- Detects AI-generated mimics of:
  - Wallet addresses  
  - SSL certificates  
  - API keys  
  - PKI credentials  
- Hamming + structural transform scoring  
- <3 ms detection runtime  
- Lightweight, explainable, no model training needed  

---

## 🤔 Why Symbolic Logic Instead of ML

- **Explainable:** every rejection has a deterministic mathematical cause  
- **Zero training data:** deploys instantly  
- **Fast:** <3 ms average runtime  
- **Deterministic:** identical input → identical output  

Unlike black-box models, ∿ filtering reveals how deception hides inside structure — not data.

---

## 🧠 Usage Example

```python
from aun_detection.operator import aun_filter

# Example: check for a spoofed wallet address
real_wallet = "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"
suspect_wallet = "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wl1"  # final '1' vs 'h'

result = aun_filter(real_wallet, suspect_wallet)

if result is None:
    print("🚨 Mimicry detected — credentials rejected.")
else:
    print(f"✅ Inputs passed. Dissimilarity score: {result}")
```

---

## 🛣️ Roadmap

- [ ] CLI integration for CI/CD pipelines  
- [ ] Web3 wallet validation API  
- [ ] Support for PGP / SSH fingerprints  
- [ ] Batch processing mode  

**Contributions welcome!**

---

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

<p align="center"><em>`aun-detection` is not a model — it’s a moment of collapse.</em><br/>
<em>In &lt; 3 ms, it tells you whether a credential stands as itself or folds back into its imitation.</em></p>
