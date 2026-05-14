"""
Script sửa lỗi mojibake trong template.txt
Nguyên nhân: UTF-8 bị đọc sai thành Latin-1/CP1252 rồi ghi lại thành UTF-8
Giải pháp: encode('cp1252').decode('utf-8') để khôi phục text gốc
"""
import re
import sys
from pathlib import Path

def fix_mojibake(text):
    """
    Sửa mojibake bằng cách thử encode CP1252 → decode UTF-8
    trên từng đoạn chứa ký tự non-ASCII.
    """
    # Tách text thành các phần: ASCII-only vs chứa non-ASCII
    # Regex tìm các cụm chứa ít nhất 1 ký tự non-ASCII liền kề
    parts = []
    last_end = 0
    
    # Tìm từng cụm ký tự non-ASCII (và ký tự ASCII xen kẽ)
    for match in re.finditer(r'[^\x00-\x7F](?:[^\x00-\x7F\n]|[\x20-\x7E])*[^\x00-\x7F]|[^\x00-\x7F]', text):
        start, end = match.span()
        # Thêm phần ASCII trước đó
        if start > last_end:
            parts.append(('ascii', text[last_end:start]))
        # Thử fix mojibake cho phần non-ASCII
        chunk = match.group()
        try:
            fixed = chunk.encode('cp1252').decode('utf-8')
            parts.append(('fixed', fixed))
        except (UnicodeEncodeError, UnicodeDecodeError):
            # Không phải mojibake, giữ nguyên
            parts.append(('keep', chunk))
        last_end = end
    
    # Thêm phần cuối cùng
    if last_end < len(text):
        parts.append(('ascii', text[last_end:]))
    
    return ''.join(p[1] for p in parts)


def main():
    root = Path(__file__).parent
    template_path = root / 'template.txt'
    
    if not template_path.exists():
        print("❌ Không tìm thấy template.txt")
        sys.exit(1)
    
    # Đọc file
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sửa mojibake
    fixed_content = fix_mojibake(content)
    
    # Kiểm tra có thay đổi không
    if content == fixed_content:
        print("ℹ️ Không tìm thấy mojibake nào cần sửa.")
        return
    
    # Hiển thị diff
    original_lines = content.splitlines()
    fixed_lines = fixed_content.splitlines()
    
    changes = 0
    for i, (orig, fix) in enumerate(zip(original_lines, fixed_lines), 1):
        if orig != fix:
            changes += 1
            print(f"  Dòng {i}:")
            print(f"    ❌ {orig.strip()[:80]}")
            print(f"    ✅ {fix.strip()[:80]}")
    
    print(f"\n📊 Tổng: {changes} dòng được sửa")
    
    # Ghi file đã sửa
    with open(template_path, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(fixed_content)
    
    print(f"✅ Đã sửa template.txt thành công!")


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    main()
