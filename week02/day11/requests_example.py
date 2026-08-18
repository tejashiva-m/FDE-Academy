"""Example using requests.

Run this from the project directory with the venv Python:

  .venv/bin/python3 requests_example.py

Do not run it with /usr/bin/python3 if you want the venv packages.
"""

import warnings

from urllib3.exceptions import NotOpenSSLWarning

# Suppress urllib3 LibreSSL/OpenSSL compatibility warning on macOS
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.headers["Content-Type"])
print(response.text[:300])

print(response.json())