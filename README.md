# pyagridata

A Python wrapper for accessing agricultural market data from the European Commission's AgriData API.

---

## ☑️ Overview

`pyagridata` provides a simple client for retrieving agricultural market data directly from the official European Commission AgriData API.

Main features:
- Safe and consistent HTTP requests with proper error handling  
- Unified interface to query multiple data categories (cereals, fruits, vegetables, etc.)  
- Installable directly from GitHub  

---

## 🚀 Installation

From GitHub:

```bash
pip install git+https://github.com/a1oysio/pyagridata.git@main
```

🧰 Quick Start

```python
from pyagridata import Client, HTTPError

client = Client()

try:
    data = client.cereals.get_prices(productCode="WHEAT", date="2025-07-01")
    print(data)
except HTTPError as err:
    print(f"API error: {err.status_code} — {err}")
```
## 📦 Project Structure

```
pyagridata/
├── pyagridata/
│   ├── __init__.py
│   ├── client.py       # BaseClient: low-level HTTP + error handling
│   ├── service.py      # Client: user-facing entrypoint, builds category services
│   ├── api.py
│   ├── enums.py
│   └── exceptions.py   # Error, HTTPError
├── LICENSE
├── pyproject.toml
├── setup.cfg
└── README.md
```

## 🛠 Requirements

- Python ≥ 3.9

- requests

## 📄 License

Distributed under the MIT License.
See the file LICENSE for more details.
