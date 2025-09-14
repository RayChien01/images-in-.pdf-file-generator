import os

# 取得 rename.py 的所在資料夾
base_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(base_dir, "images")  # images 在 rename.py 同一層
output_file = os.path.join(base_dir, "imagelist.tex")

print("圖片資料夾：", folder)

with open(output_file, "w", encoding="utf-8") as f:
    for filename in sorted(os.listdir(folder)):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".pdf")):
            f.write(f"\\includegraphics[width=\\linewidth]{{images/{filename}}}\n")
            f.write("\\newpage\n")

print(f"{output_file} 已經生成完成！")
