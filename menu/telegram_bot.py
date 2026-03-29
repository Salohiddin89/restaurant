import urllib.request
import urllib.parse
import json
from django.conf import settings


def send_telegram_message(text):
    """Telegram bot orqali admin ga xabar yuborish"""
    try:
        token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_ADMIN_CHAT_ID

        if token == 'YOUR_BOT_TOKEN_HERE' or chat_id == 'YOUR_CHAT_ID_HERE':
            print("⚠️  Telegram token yoki chat_id sozlanmagan!")
            return False

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = urllib.parse.urlencode({
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'HTML'
        }).encode('utf-8')

        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read())
            return result.get('ok', False)
    except Exception as e:
        print(f"Telegram xato: {e}")
        return False


def notify_new_message(contact_message):
    """Yangi xabar kelganda adminni xabardor qilish"""
    text = (
        f"🔔 <b>Yangi xabar keldi!</b>\n\n"
        f"👤 <b>Ism:</b> {contact_message.full_name}\n"
        f"💬 <b>Xabar:</b>\n{contact_message.message}\n\n"
        f"🕐 <b>Vaqt:</b> {contact_message.created_at.strftime('%d.%m.%Y %H:%M')}"
    )
    return send_telegram_message(text)
