import os
import shutil
import argparse
import sys

def copy_file(src_file_path, dst_root):
    """
    Функція копіює файл у директорію призначення, створюючи піддиректорію за розширенням файлу.
    """
    try:
        # Отримуємо ім'я файлу та розширення
        file_name = os.path.basename(src_file_path)
        _, ext = os.path.splitext(file_name)
        
        # Якщо розширення порожнє, використовуємо спеціальну директорію
        if ext:
            # Видаляємо початкову крапку, щоб назва була чистою (наприклад, "txt" замість ".txt")
            subdir = ext[1:].lower()
        else:
            subdir = "no_extension"
        
        # Формуємо повний шлях до піддиректорії у директорії призначення
        dst_subdir = os.path.join(dst_root, subdir)
        
        # Якщо піддиректорія не існує, створюємо її
        if not os.path.exists(dst_subdir):
            os.makedirs(dst_subdir, exist_ok=True)
        
        # Формуємо кінцевий шлях до файлу в директорії призначення
        dst_file_path = os.path.join(dst_subdir, file_name)
        
        # Копіюємо файл із збереженням метаданих
        shutil.copy2(src_file_path, dst_file_path)
        print(f"Скопійовано: {src_file_path} -> {dst_file_path}")
        
    except Exception as e:
        print(f"Помилка при копіюванні файлу {src_file_path}: {e}")

def traverse_and_copy(src_dir, dst_dir):
    """
    Рекурсивно обходить директорію src_dir та копіює всі знайдені файли до директорії dst_dir.
    """
    try:
        # Отримуємо список елементів у директорії
        for entry in os.listdir(src_dir):
            full_path = os.path.join(src_dir, entry)
            
            # Якщо елемент є директорією, викликаємо функцію рекурсивно
            if os.path.isdir(full_path):
                traverse_and_copy(full_path, dst_dir)
            # Якщо елемент є файлом, копіюємо його
            elif os.path.isfile(full_path):
                copy_file(full_path, dst_dir)
    except PermissionError as pe:
        print(f"Помилка доступу до директорії {src_dir}: {pe}")
    except Exception as e:
        print(f"Помилка обробки директорії {src_dir}: {e}")

def parse_arguments():
    """
    Функція парсить аргументи командного рядка.
    Перший аргумент - шлях до вихідної директорії.
    Другий (необов’язковий) аргумент - шлях до директорії призначення (за замовчуванням 'dist').
    """
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів із сортуванням за розширенням.")
    parser.add_argument("src_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dst_dir", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Перевірка чи існує директорія джерела
    if not os.path.exists(args.src_dir):
        print(f"Вихідна директорія '{args.src_dir}' не існує.")
        sys.exit(1)
    if not os.path.isdir(args.src_dir):
        print(f"'{args.src_dir}' не є директорією.")
        sys.exit(1)

    # Якщо директорія призначення не існує, створюємо її
    if not os.path.exists(args.dst_dir):
        try:
            os.makedirs(args.dst_dir, exist_ok=True)
        except Exception as e:
            print(f"Не вдалося створити директорію призначення '{args.dst_dir}': {e}")
            sys.exit(1)
    
    traverse_and_copy(args.src_dir, args.dst_dir)

if __name__ == "__main__":
    main()
