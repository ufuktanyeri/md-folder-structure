import os

def list_dir(path, indent=0):
    output = ""
    prefix = "│   " * (indent - 1) + "├── " if indent > 0 else ""
    output += f"{prefix}{os.path.basename(path)}/\n"
    try:
        for item in sorted(os.listdir(path)):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                output += list_dir(full_path, indent + 1)
            else:
                file_prefix = "│   " * indent + "└── "
                output += f"{file_prefix}{item}\n"
    except PermissionError:
        pass
    return output

def export_to_md(base_path, output_file="structure.md"):
    tree = list_dir(base_path)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("```md\n")
        f.write(tree)
        f.write("```\n")
    print(f"Yapı '{output_file}' dosyasına yazıldı.")

# 🔧 Örnek kullanım
if __name__ == "__main__":
    export_to_md("uyap-toplu-indir")  # 👈 Dilersen burayı input() ile de yapabiliriz
