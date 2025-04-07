import os
import tkinter as tk
from tkinter import filedialog

# Klasör yapısını metin olarak oluşturur
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
        output += f"{'│   ' * indent}[Erişim Engellendi]\n"
    return output

# Kullanıcının kaydedeceği dosya adını alır (.md olarak)
def select_output_file():
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    filetypes = [("Markdown files", "*.md")]
    filepath = filedialog.asksaveasfilename(
        title="Çıktı dosyasını kaydet (.md)",
        defaultextension=".md",
        filetypes=filetypes
    )
    root.destroy()
    return filepath

# Klasör seçme penceresi
def select_folder():
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Bir klasör seçin")
    root.destroy()
    return folder_path

# Yapıyı .md dosyasına yazar
def export_to_md(base_path, output_file):
    tree = list_dir(base_path)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("```md\n")
        f.write(tree)
        f.write("```\n")
    print(f"✅ Markdown dosyası oluşturuldu → {output_file}")

# Ana akış
if __name__ == "__main__":
    selected_path = select_folder()
    if selected_path and os.path.isdir(selected_path):
        output_file = select_output_file()
        if output_file:
            export_to_md(selected_path, output_file)
        else:
            print("❌ Dosya kaydetme iptal edildi.")
    else:
        print("❌ Geçersiz klasör seçimi.")
