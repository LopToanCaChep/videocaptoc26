import sys

replacements = {
    'Cáº¥p Tá»‘c': 'Cấp Tốc',
    'ToÃ¡n': 'Toán',
    'CÃ¡ ChÃ©p': 'Cá Chép',
    'Pháº§n': 'Phần',
    'ChÃºc báº¡n há»\x8dc táºp hiá»‡u quáº£!': 'Chúc bạn học tập hiệu quả!',
    'ChÃºc báº¡n há»\x8dc táºp hiá»‡u quáº£': 'Chúc bạn học tập hiệu quả',
    'báº¡n': 'bạn',
    'hiá»‡u': 'hiệu',
    'quáº£': 'quả',
    'há»\x8dc': 'học',
    'táºp': 'tập',
    'Ä\x90ang cáºp nháºt': 'Đang cập nhật',
    'Buá»•i': 'Buổi',
    'https://lh3.googleusercontent.com/aida-public/AB6AXuApyNgkfVUK7WCyXoge4CHTvV_84HUh_OHyj5KalzFeMFWiNUqoDvsIA3nWuk9NkTN8oRJy7SMyrA1mslYab453j6-WO8HOd4hsn9wZGOVmGWu_zOQYySjshkige7suqD8XMBUsCRyWylDgWMOfGCm0NJ36GG2kjX6JiGHcQ-TNQM9RVOdjYLiiuefX9aWzak5l6eYLrZvlR8mY30KFAG_DnVFGshv3I5s1M5zuCqEN-YFWS-9P6ha85H74BAU-YHIpcOAPj0Ul7Ayt': './logo_captoc_96x96.png'
}

with open('template_backup.txt', 'r', encoding='utf-16') as f:
    text = f.read()

for k, v in replacements.items():
    text = text.replace(k, v)

# Re-apply the JS description change just in case
text = text.replace("document.getElementById('np-desc').textContent = \"Chúc bạn học tập hiệu quả!\";", "document.getElementById('np-desc').textContent = currentVideo.desc || \"Chúc bạn học tập hiệu quả!\";")

with open('template.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed template!')
