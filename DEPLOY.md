# 🚀 PythonAnywhere Deploy Qilish Qo'llanmasi

## 1. PythonAnywhere ro'yxatdan o'ting
https://www.pythonanywhere.com/registration/register/beginner/

## 2. Bash Console oching
Dashboard → "New console" → "Bash"

## 3. Loyihani yuklang
```bash
# Papka yarating
mkdir -p ~/lazzat_restaurant
cd ~/lazzat_restaurant

# Zip faylni yuklab olgach:
unzip lazzat_restaurant.zip
```

## 4. Virtual muhit yarating
```bash
cd ~/lazzat_restaurant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 5. Ma'lumotlar bazasini sozlang
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
# Username, email, password kiriting
```

## 6. Static fayllarni yig'ing
```bash
python manage.py collectstatic --noinput
```

## 7. Web App sozlang
PythonAnywhere → Web → Add new web app:
- Python version: 3.10
- Framework: Django
- Path: /home/SIZNING_USERNAME/lazzat_restaurant
- Python version: 3.10

## 8. WSGI faylni tahrirlang
Web tab → WSGI configuration file ni bosing:

```python
import os
import sys

path = '/home/SIZNING_USERNAME/lazzat_restaurant'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'restaurant.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 9. Virtualenv yo'lini kiriting
Web tab → Virtualenv: /home/SIZNING_USERNAME/lazzat_restaurant/venv

## 10. Static va Media fayllar
Web tab → Static files:
- URL: /static/   → Directory: /home/USERNAME/lazzat_restaurant/staticfiles
- URL: /media/    → Directory: /home/USERNAME/lazzat_restaurant/media

## 11. settings.py ni yangilang
```python
ALLOWED_HOSTS = ['SIZNING_USERNAME.pythonanywhere.com']
DEBUG = False
```

## 12. Telegram Bot sozlash
1. @BotFather ga boring → /newbot → bot yarating → TOKEN oling
2. Botingizga /start yuboring
3. https://api.telegram.org/botTOKEN/getUpdates → chat_id oling
4. settings.py ga qo'shing:
   TELEGRAM_BOT_TOKEN = 'token_bu_yerga'
   TELEGRAM_ADMIN_CHAT_ID = 'chat_id_bu_yerga'

## 13. Reload qiling
Web tab → "Reload" tugmasi

## 14. Admin panelga kiring
https://SIZNING_USERNAME.pythonanywhere.com/admin/
- Username va parol bilan kiring
- Kategoriyalar va mahsulotlar qo'shing

## QR Kod yaratish
Har bir stol uchun: https://qr.io yoki https://qrcode-monkey.com
URL: https://SIZNING_USERNAME.pythonanywhere.com/menu/
