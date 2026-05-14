import csv
import json
import sys
from pathlib import Path

def main():
    root_dir = Path(__file__).parent
    csv_path = root_dir / 'quan_ly_video.csv'
    template_path = root_dir / 'template.txt'
    output_path = root_dir / 'index.html'

    if not csv_path.exists():
        print(f"Lỗi: Không tìm thấy file {csv_path.name}")
        sys.exit(1)
        
    if not template_path.exists():
        print(f"Lỗi: Không tìm thấy file {template_path.name}")
        sys.exit(1)

    # Đọc dữ liệu từ CSV
    sessions_dict = {}
    
    with open(csv_path, encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Trang_Thai'] != 'Hien':
                continue
                
            buoi_num = row['Buoi'].zfill(2)
            if buoi_num not in sessions_dict:
                sessions_dict[buoi_num] = {
                    "num": buoi_num,
                    "title": row['Ten_Buoi'],
                    "videos": []
                }
                
            if row['ID_Youtube']:
                sessions_dict[buoi_num]["videos"].append({
                    "name": row['Ten_Phan'],
                    "id": row['ID_Youtube']
                })

    # Chuyển thành danh sách và đảm bảo đủ 15 buổi
    final_sessions = []
    for i in range(1, 16):
        b_num = str(i).zfill(2)
        if b_num in sessions_dict:
            final_sessions.append(sessions_dict[b_num])
        else:
            final_sessions.append({
                "num": b_num,
                "title": "",
                "videos": []
            })

    # Đọc template và inject
    with open(template_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Format JSON đẹp
    json_data = json.dumps(final_sessions, ensure_ascii=False, indent=4)
    
    # Replace placeholder
    new_html = html_content.replace('%INJECT_DATA%', json_data)

    # Ghi ra index.html
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"✅ Đã build thành công {output_path.name} từ CSV!")

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    main()
