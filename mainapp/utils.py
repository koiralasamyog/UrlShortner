# mainapp/utils.py
import string
import qrcode
from io import BytesIO
import base64

BASE62 = string.digits + string.ascii_lowercase + string.ascii_uppercase

def encode_base62(num):
    if num == 0:
        return BASE62[0]
    arr = []
    base = len(BASE62)
    while num > 0:
        num, rem = divmod(num, len(BASE62))
        arr.append(BASE62[rem])
    arr.reverse()
    return ''.join(arr)

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=6,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"
