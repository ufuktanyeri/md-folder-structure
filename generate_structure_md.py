import os
import fnmatch
import tkinter as tk
from tkinter import filedialog, messagebox

# .gitignore içeriğini oku
def load_gitignore_patterns(base_path):
    ignore_file = os.path.join(base_path, ".gitignore")
    if not os.path.isfile(ignore_file):
        return set()

    with open(ignore_file, "r", encoding="utf-8") as f:
        return {
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        }

# ignore edilen dosya/klasör eşleşmesini kontrol et
def is_ignored(name, patterns):
    return any(fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(f"./{name}", pattern) for pattern in patterns)

# Klasör yapısını oluştur (girintili sade görünüm)
def list_dir(path, indent=0, ignore_patterns=None):
    ignore_patterns = ignore_patterns or set()
    output = "    " * indent + f"{os.path.basename(path)}/\n"

    try:
        for item in sorted(os.listdir(path)):
            if is_ignored(item, ignore_patterns):
                continue

            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                output += list_dir(full_path, indent + 1, ignore_patterns)
            else:
                output += "    " * (indent + 1) + f"{item}\n"
    except PermissionError:
        output += "    " * (indent + 1) + "[Erişim Engellendi]\n"

    return output

# Tk root oluşturucu
def create_hidden_root():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    return root

# Dosya kayıt diyaloğu
def select_output_file(default_name):
    root = create_hidden_root()
    filetypes = [
        ("Markdown files", "*.md"),
        ("Text files", "*.txt"),
        ("All files", "*.*"),
    ]
    filepath = filedialog.asksaveasfilename(
        title="Çıktı dosyasını kaydet",
        defaultextension=".md",
        initialfile=default_name,
        filetypes=filetypes
    )
    root.destroy()
    return filepath

# Klasör seçme diyaloğu
def select_folder():
    root = create_hidden_root()
    folder = filedialog.askdirectory(title="Bir klasör seçin")
    root.destroy()
    return folder

# Yapıyı dosyaya yaz
def export_to_md(base_path, output_file):
    ignore_patterns = load_gitignore_patterns(base_path)
    tree = list_dir(base_path, ignore_patterns=ignore_patterns)

    with open(output_file, "w", encoding="utf-8") as f:
        if output_file.endswith(".md"):
            f.write("```text\n")
            f.write(tree)
            f.write("```\n")
        else:
            f.write(tree)

    print(f"✅ Dosya oluşturuldu → {output_file}")

    # Bilgilendirme mesajı
    message_root = create_hidden_root()
    messagebox.showinfo("Başarılı", f"Dosya oluşturuldu:\n{output_file}")
    message_root.destroy()

# Ana akış
if __name__ == "__main__":
    selected_path = select_folder()
    if not selected_path or not os.path.isdir(selected_path):
        print("❌ Geçersiz klasör seçimi.")
        exit()

    base_name = os.path.basename(selected_path.rstrip("/\\"))
    default_name = f"{base_name}_folder_structure"
    output_file = select_output_file(default_name)

    if output_file:
        export_to_md(selected_path, output_file)
    else:
        print("❌ Dosya kaydetme iptal edildi.")
