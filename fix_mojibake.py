import sys
import re

replacements = {
    'Ä ang cáº\xadp nháº\xadt': 'Đang cập nhật',
    'ðŸš€': '🚀',
    'ðŸ‘½': '👽',
    'Sáº¯p cÃ³': 'Sắp có',
    'ChÃºc báº¡n há»\x8dc táºp hiá»‡u quáº£!': 'Chúc bạn học tập hiệu quả!',
    'HoÃ\xa0n thÃ\xa0nh': 'Hoàn thành',
    'TÆ° Ä‘á»™ng: Báº\xadt': 'Tự động: Bật',
    'TÆ° Ä‘á»™ng: Táº¯t': 'Tự động: Tắt',
    'Buá»•i': 'Buổi'
}

with open('template.txt', 'r', encoding='utf-8-sig') as f:
    text = f.read()

for k, v in replacements.items():
    text = text.replace(k, v)

# Update descriptions
text = text.replace(
    'document.getElementById(\'np-desc\').textContent = "Chúc bạn học tập hiệu quả!";',
    'document.getElementById(\'np-desc\').textContent = currentVideo.desc || "Chúc bạn học tập hiệu quả!";'
)
text = text.replace(
    'document.getElementById(\'np-desc\').textContent = "ChÃºc báº¡n há»\x8dc táºp hiá»‡u quáº£!";',
    'document.getElementById(\'np-desc\').textContent = currentVideo.desc || "Chúc bạn học tập hiệu quả!";'
)

# Fix JS issues for interactions: 
# The user mentioned "không tương tác được" (not interactive).
# Let's check `buildSessions` in `template.txt`. 
# Toggle session needs to find `.session-items`, but wait, the toggle JS is:
# function toggleSession(titleEl) {
#    const sessionEl = titleEl.closest('.session');
#    sessionEl.classList.toggle('closed');
# }
# This is fully intact.

with open('template.txt', 'w', encoding='utf-8-sig') as f:
    f.write(text)

print('Fixed mojibake in template.txt!')
