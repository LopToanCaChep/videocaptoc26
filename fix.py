import re

with open('template.txt', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Logo
html = html.replace('https://lh3.googleusercontent.com/aida-public/AB6AXuApyNgkfVUK7WCyXoge4CHTvV_84HUh_OHyj5KalzFeMFWiNUqoDvsIA3nWuk9NkTN8oRJy7SMyrA1mslYab453j6-WO8HOd4hsn9wZGOVmGWu_zOQYySjshkige7suqD8XMBUsCRyWylDgWMOfGCm0NJ36GG2kjX6JiGHcQ-TNQM9RVOdjYLiiuefX9aWzak5l6eYLrZvlR8mY30KFAG_DnVFGshv3I5s1M5zuCqEN-YFWS-9P6ha85H74BAU-YHIpcOAPj0Ul7Ayt', './logo_captoc_96x96.png')

# 2. CSS empty session
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
html = html.replace(css_session, css_session_new)

# 3. CSS vitem mr
css_vitem = """      margin-bottom: 0.75rem;
      cursor: pointer;"""
css_vitem_new = """      margin-bottom: 0.75rem;
      margin-right: 0.5rem; /* Thu gọn lại để không mất viền phải */
      cursor: pointer;"""
html = html.replace(css_vitem, css_vitem_new)

# 4. CSS watched
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
html = html.replace(css_watched, css_watched_new)

# 5. JS SESSIONS
html = re.sub(r'const SESSIONS = \[.*?\];', 'const SESSIONS = %INJECT_DATA%;', html, flags=re.DOTALL)

# 6. JS empty class
js_empty = """<div class="session ${hasVideos ? '' : 'closed'}" id="session-${s.num}">"""
js_empty_new = """<div class="session ${hasVideos ? '' : 'closed empty'}" id="session-${s.num}">"""
html = html.replace(js_empty, js_empty_new)

# 7. JS Description
js_desc = """document.getElementById('np-desc').textContent = "Chúc bạn học tập hiệu quả!";"""
js_desc_new = """document.getElementById('np-desc').textContent = currentVideo.desc || "Chúc bạn học tập hiệu quả!";"""
html = html.replace(js_desc, js_desc_new)

with open('template.txt', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed template!')
