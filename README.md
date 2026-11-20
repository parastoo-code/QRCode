# ساخت و خواندن QR Code با پایتون

چند اسکریپت ساده برای ساخت QR Code با کتابخانه‌ی `qrcode` و خواندن آن با `pyzbar`.
(با تشکر از آقای لاریان بابت کدهای اولیه)

## ساختار پروژه

```
qrcode_library_code/
├── simple_qr.py            # ساده‌ترین روش ساخت QR (لینک گوگل)
├── generate_qr.py          # ساخت QR با تنظیمات کامل (لینک python.org)
├── generate_qr_github.py   # ساخت QR برای لینک سایت دیگر (github.com)
├── decode_qr.py            # خواندن QR از روی تصویر
├── test_qr_opencv.py       # تست ساخت و خواندن QR با OpenCV
└── generated_qrcodes/
    └── github_01.png       # نمونه QR ساخته‌شده برای https://github.com
```

## نصب

```bash
pip install "qrcode[pil]"
pip install pyzbar Pillow
```

برای `test_qr_opencv.py` به `opencv-python` و `numpy` نیاز است:

```bash
pip install opencv-python numpy
```

> کاربران ویندوز معمولاً با نصب `pyzbar` مشکلی ندارند. روی لینوکس ممکن است لازم باشد بسته‌ی `libzbar0` هم نصب شود.

## نحوه اجرا

| هدف | دستور |
|-----|-------|
| ساخت QR ساده | `python simple_qr.py` |
| ساخت QR با تنظیمات (رنگ، تصحیح خطا، حاشیه) | `python generate_qr.py` |
| ساخت QR برای github.com | `python generate_qr_github.py` |
| خواندن QR از تصویر | `python decode_qr.py` |
| تست با OpenCV | `python test_qr_opencv.py` |

تصاویر ساخته‌شده در پوشه‌ی `generated_qrcodes` ذخیره می‌شوند و اگر این پوشه وجود نداشته باشد، خودکار ساخته می‌شود.

## تغییر لینک

در `generate_qr_github.py` مقدار داخل `qr.add_data(...)` را به لینک دلخواه تغییر دهید:

```python
qr.add_data("https://github.com")
```

## تنظیمات مهم QRCode

- `error_correction`: سطح تصحیح خطا (`ERROR_CORRECT_H` بالاترین سطح است).
- `box_size`: اندازه‌ی هر خانه به پیکسل.
- `border`: ضخامت حاشیه‌ی سفید دور QR (حداقل ۴ خانه استاندارد است).
- `fill_color` و `back_color`: رنگ QR و پس‌زمینه؛ برای خوانایی بهتر است رنگ QR تیره‌تر از پس‌زمینه باشد.

## نکته درباره decode_qr.py

این اسکریپت فایل `generated_qrcodes/python_01.png` را می‌خواند. برای خواندن QR دیگر، مسیر تصویر را در `Image.open(...)` عوض کنید، مثلاً `generated_qrcodes/github_01.png`.

## وضعیت تست

QR مربوط به `https://github.com` با OpenCV ساخته و دوباره خوانده شد و نتیجه دقیقاً همان لینک بود. اسکریپت‌های مبتنی بر `qrcode` و `pyzbar` (از جمله `generate_qr_github.py`) در محیط تست نصب نبودند و اجرا نشده‌اند؛ پس روی سیستم خودتان یک‌بار اجرایشان کنید.
