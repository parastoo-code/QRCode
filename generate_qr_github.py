import os
import qrcode

folder_name = "generated_qrcodes"
file_name = "github_01.png"
full_path = os.path.join(folder_name, file_name)
os.makedirs(folder_name, exist_ok=True)

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://github.com")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(full_path)

print(f"QR code saved successfully to: {os.path.abspath(full_path)}")
