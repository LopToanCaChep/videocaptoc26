import re

# 1. Read index_notion.html
with open('index_notion.html', 'r', encoding='utf-8') as f:
    notion_html = f.read()

scripts = re.findall(r'<script>.*?</script>', notion_html, re.DOTALL)
js_script = scripts[-1] # The last script block contains the logic

# 2. Add description logic to playVideo
js_script = js_script.replace(
    "document.getElementById('np-desc').textContent = \"Chúc bạn học tập hiệu quả!\";",
    "document.getElementById('np-desc').textContent = currentVideo.desc || \"Chúc bạn học tập hiệu quả!\";"
)

# 3. Read template_playboard.html
with open('template_playboard.html', 'r', encoding='utf-8') as f:
    playboard = f.read()

# Replace English titles
playboard = playboard.replace('<title>Scientific Learning Platform</title>', '<title>Video Cấp Tốc Toán 12 | Toán Cá Chép</title>')
playboard = playboard.replace('SCIENTIFIC LEARNING', 'CẤP TỐC 26')
playboard = playboard.replace('System initialized...', 'Hệ thống đã sẵn sàng...')
playboard = playboard.replace('https://lh3.googleusercontent.com/aida-public/AB6AXuApyNgkfVUK7WCyXoge4CHTvV_84HUh_OHyj5KalzFeMFWiNUqoDvsIA3nWuk9NkTN8oRJy7SMyrA1mslYab453j6-WO8HOd4hsn9wZGOVmGWu_zOQYySjshkige7suqD8XMBUsCRyWylDgWMOfGCm0NJ36GG2kjX6JiGHcQ-TNQM9RVOdjYLiiuefX9aWzak5l6eYLrZvlR8mY30KFAG_DnVFGshv3I5s1M5zuCqEN-YFWS-9P6ha85H74BAU-YHIpcOAPj0Ul7Ayt', './logo_captoc_96x96.png')

# 4. Inject script into playboard
pb_scripts = re.findall(r'<script>.*?</script>', playboard, re.DOTALL)
playboard = playboard.replace(pb_scripts[-1], js_script)

# 5. Apply CSS and JS tweaks for Space Theme exactly as before

# CSS empty session
css_session = """.session.closed .session-title .toggle-icon {
      transform: rotate(-90deg);
    }"""
css_session_new = """.session.closed .session-title .toggle-icon {
      transform: rotate(-90deg);
    }
    .session.empty {
      opacity: 0.3; /* Mờ đi khi trống */
      transition: opacity 0.3s ease;
    }
    .session.empty:hover {
      opacity: 1;
    }"""
playboard = playboard.replace(css_session, css_session_new)

# CSS vitem mr
css_vitem = """      margin-bottom: 0.75rem;
      cursor: pointer;"""
css_vitem_new = """      margin-bottom: 0.75rem;
      margin-right: 0.5rem; /* Thu gọn lại để không mất viền phải */
      cursor: pointer;"""
playboard = playboard.replace(css_vitem, css_vitem_new)

# CSS watched
css_watched = """    /* Watched State */
    .vitem.watched {
      background-color: rgba(0, 8, 36, 0.5);
      opacity: 0.6;
      border-style: dashed;
    }

    .vitem.watched .vitem-title {
      text-decoration: line-through;
      color: rgba(255,255,255,0.5);
    }"""
css_watched_new = """    /* Watched State */
    .vitem.watched {
      background-color: rgba(0, 8, 36, 0.5);
      opacity: 0.8;
      border-style: solid;
      border-color: #00f2fe; /* nét liền xanh dương neon */
    }

    .vitem.watched .vitem-title {
      color: rgba(255,255,255,0.7); /* Bỏ gạch ngang */
    }"""
playboard = playboard.replace(css_watched, css_watched_new)

# JS SESSIONS
playboard = re.sub(r'const SESSIONS = \[.*?\];', 'const SESSIONS = %INJECT_DATA%;', playboard, flags=re.DOTALL)

# JS empty class
js_empty = """<div class="session ${hasVideos ? '' : 'closed'}" id="session-${s.num}">"""
js_empty_new = """<div class="session ${hasVideos ? '' : 'closed empty'}" id="session-${s.num}">"""
playboard = playboard.replace(js_empty, js_empty_new)

# Wait, in index_notion.html the javascript HTML builder was slightly different!
# The HTML built in index_notion.html used Notion classes (like .tc-card), not the Space Theme classes!
# Ahhhh!!! This is the root of everything.
