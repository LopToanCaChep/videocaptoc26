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
                
            de_num = row['De'].zfill(2)
            if de_num not in sessions_dict:
                sessions_dict[de_num] = {
                    "num": de_num,
                    "title": row['Ten_De'],
                    "videos": []
                }
                
            if row['ID_Youtube']:
                sessions_dict[de_num]["videos"].append({
                    "name": row['Ten_Phan'],
                    "id": row['ID_Youtube'],
                    "desc": row.get('Mo_Ta', '')
                })

    # Chuyển thành danh sách và ẩn hết các đề chẵn (chỉ giữ lại các đề lẻ từ 1 đến 15)
    final_sessions = []
    for i in range(1, 16):
        if i % 2 == 0:  # Bỏ qua và ẩn toàn bộ đề chẵn
            continue
        d_num = str(i).zfill(2)
        if d_num in sessions_dict:
            final_sessions.append(sessions_dict[d_num])
        else:
            final_sessions.append({
                "num": d_num,
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
