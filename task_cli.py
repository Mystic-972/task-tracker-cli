"""Task Tracker CLI

Contoh penggunaan:
  python task_cli.py add "Beli bahan makanan"
  python task_cli.py update 1 "Beli bahan makanan dan masak makan malam"
  python task_cli.py delete 1
  python task_cli.py mark-in-progress 1
  python task_cli.py mark-done 1
  python task_cli.py list
  python task_cli.py list done
  python task_cli.py list todo
  python task_cli.py list in-progress
"""

import sys
import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: File {TASK_FILE} rusak. Memulai dengan daftar tugas kosong.")
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def cmd_add(args):
    if len(args) < 1:
        print("Error: Deskripsi dibutuhkan untuk perintah add.")
        return
    description = args[0]
    tasks = load_tasks()
    task_id = generate_id(tasks)
    now = datetime.now().isoformat()
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tugas berhasil ditambahkan (ID: {task_id})")

def cmd_update(args):
    if len(args) < 2:
        print("Error: ID dan deskripsi baru dibutuhkan untuk perintah update.")
        return
    try:
        task_id = int(args[0])
    except ValueError:
        print("Error: ID harus berupa angka/integer.")
        return
    new_desc = args[1]
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print(f"Error: Tidak ada tugas dengan ID {task_id}.")
        return
    task["description"] = new_desc
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Tugas {task_id} berhasil diperbarui.")

def cmd_delete(args):
    if len(args) < 1:
        print("Error: ID dibutuhkan untuk perintah delete.")
        return
    try:
        task_id = int(args[0])
    except ValueError:
        print("Error: ID harus berupa angka/integer.")
        return
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Error: Tidak ada tugas dengan ID {task_id}.")
        return
    save_tasks(new_tasks)
    print(f"Tugas {task_id} berhasil dihapus.")

def cmd_mark(args, new_status):
    if len(args) < 1:
        print(f"Error: ID dibutuhkan untuk perintah mark-{new_status}.")
        return
    try:
        task_id = int(args[0])
    except ValueError:
        print("Error: ID harus berupa angka/integer.")
        return
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print(f"Error: Tidak ada tugas dengan ID {task_id}.")
        return
    task["status"] = new_status
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Tugas {task_id} ditandai sebagai '{new_status}'.")

def cmd_list(args):
    status_filter = None
    if len(args) >= 1:
        status_filter = args[0].lower()
        if status_filter not in {"todo", "in-progress", "done"}:
            print("Error: Filter status tidak valid. Gunakan todo, in-progress, atau done.")
            return
    tasks = load_tasks()
    if status_filter:
        tasks = [t for t in tasks if t["status"] == status_filter]
    if not tasks:
        print("Tidak ada tugas yang ditemukan.")
        return
    for t in tasks:
        print(f"[{t['id']}] {t['description']} – {t['status']} (Dibuat: {t['createdAt']}, Diperbarui: {t['updatedAt']})")

def main():
    if len(sys.argv) < 2:
        print("Error: Tidak ada perintah yang diberikan.")
        print("Perintah yang tersedia: add, update, delete, mark-in-progress, mark-done, list")
        return
    command = sys.argv[1]
    args = sys.argv[2:]
    
    if command == "add":
        description = " ".join(args).strip('"')
        cmd_add([description])
    elif command == "update":
        if len(args) < 2:
            print("Error: Penggunaan -> update <id> <deskripsi baru>")
            return
        task_id = args[0]
        new_desc = " ".join(args[1:]).strip('"')
        cmd_update([task_id, new_desc])
    elif command == "delete":
        cmd_delete(args)
    elif command == "mark-in-progress":
        cmd_mark(args, "in-progress")
    elif command == "mark-done":
        cmd_mark(args, "done")
    elif command == "list":
        cmd_list(args)
    else:
        print(f"Perintah tidak dikenal: {command}")
        print("Perintah yang tersedia: add, update, delete, mark-in-progress, mark-done, list")

if __name__ == "__main__":
    main()
