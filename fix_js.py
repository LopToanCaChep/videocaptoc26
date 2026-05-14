import sys
import re

with open('template.txt', 'r', encoding='utf-8-sig') as f:
    text = f.read()

# Fix CSS empty
css_session = """.session.closed .session-title .toggle-icon {
      transform: rotate(-90deg);
    }"""
css_session_new = """.session.closed .session-title .toggle-icon {
      transform: rotate(-90deg);
    }
    .session.empty {
      opacity: 0.3;
      transition: opacity 0.3s ease;
    }
    .session.empty:hover {
      opacity: 1;
    }"""
text = text.replace(css_session, css_session_new)

# Fix JS empty session rendering
js_empty = """<div class="session ${hasVideos ? '' : 'closed'}" id="session-${s.num}">"""
js_empty_new = """<div class="session ${hasVideos ? '' : 'closed empty'}" id="session-${s.num}">"""
text = text.replace(js_empty, js_empty_new)

# Fix PlayVideo signature to include description
playvideo_old = """function playVideo(id, name, sessionLabel, el) {"""
playvideo_new = """function playVideo(id, name, sessionLabel, desc, el) {"""
text = text.replace(playvideo_old, playvideo_new)

# Fix playVideo DOM update
desc_old = """document.getElementById('np-desc').textContent = "ChÃºc bạn học táº­p hiệu quả!";"""
desc_new = """document.getElementById('np-desc').textContent = desc || "Chúc bạn học tập hiệu quả!";"""
text = text.replace(desc_old, desc_new)

desc_old2 = """document.getElementById('np-desc').textContent = "Chúc bạn học tập hiệu quả!";"""
text = text.replace(desc_old2, desc_new)

# Fix buildSessions onclick
onclick_old = """onclick="playVideo('${v.id}','${v.name.replace(/'/g,"\\\\'")}', '${sessionLabelFull.replace(/'/g,"\\\\'")}', this)\""""
onclick_new = """onclick="playVideo('${v.id}','${v.name.replace(/'/g,"\\\\'")}', '${sessionLabelFull.replace(/'/g,"\\\\'")}', '${(v.desc || "").replace(/'/g,"\\\\'")}', this)\""""
text = text.replace(onclick_old, onclick_new)

# Let's ensure playNext also passes desc
playnext_old = """playVideo(next.id, next.name, next.session, next.el);"""
playnext_new = """playVideo(next.id, next.name, next.session, next.desc, next.el);"""
text = text.replace(playnext_old, playnext_new)

# And make sure buildSessions adds desc to playQueue
queue_old = """playQueue.push({ id: v.id, name: v.name, session: sessionLabelFull, el: null });"""
queue_new = """playQueue.push({ id: v.id, name: v.name, session: sessionLabelFull, el: null, desc: v.desc });"""
text = text.replace(queue_old, queue_new)

with open('template.txt', 'w', encoding='utf-8-sig') as f:
    f.write(text)

print("Fixed JS logic and CSS logic!")
