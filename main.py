import qrcode
import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser(description="QR Code Generator KV")
parser.add_argument("--url", required=True, help="URL to generate QR code")

args = parser.parse_args()
url = args.url

# Create directories
os.makedirs("qr_codes", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Generate QR code
qr = qrcode.make(url)

filename = f"qr_codes/qr_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
qr.save(filename)

# Write log
with open("logs/app.log", "a") as log:
    log.write(f"{datetime.now()} Generated QR code for {url}\n")

print(f"QR Code generated for {url}")
print(f"Saved at: {filename}")