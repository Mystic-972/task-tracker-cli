# Task Tracker CLI

Task Tracker CLI adalah aplikasi sederhana yang digunakan untuk mencatat dan mengelola tugas melalui terminal atau Command Prompt.

Dengan aplikasi ini, kamu bisa menambahkan tugas, mengubah tugas, menghapus tugas, mengubah status tugas, dan melihat daftar tugas berdasarkan statusnya.

## Struktur Folder

```text
task-tracker/
│
├── task_cli.py
├── tasks.json
└── README.md
```

## Requirements

Sebelum menjalankan program, pastikan Python sudah terinstall di komputer.

* Python 3.6 atau versi yang lebih baru
* Tidak membutuhkan library atau package tambahan karena program ini hanya menggunakan module bawaan Python

## Cara Menjalankan

Buka terminal atau CMD, lalu masuk ke folder project.

Untuk menambahkan tugas baru:

```bash
python task_cli.py add "Beli galon"
```

Untuk mengubah tugas yang sudah ada:

```bash
python task_cli.py update <id> "Beli galon dan gas"
```

Ganti `<id>` dengan ID tugas yang ingin diubah.

Untuk menghapus tugas:

```bash
python task_cli.py delete <id>
```

Untuk mengubah status tugas menjadi sedang dikerjakan:

```bash
python task_cli.py mark-in-progress <id>
```

Untuk menandai tugas sebagai selesai:

```bash
python task_cli.py mark-done <id>
```

Untuk melihat semua tugas:

```bash
python task_cli.py list
```

Kamu juga bisa menampilkan tugas berdasarkan status:

```bash
python task_cli.py list todo
```

```bash
python task_cli.py list in-progress
```

```bash
python task_cli.py list done
```

## Penyimpanan Data

Semua tugas disimpan di file `tasks.json`.

File tersebut akan dibuat secara otomatis ketika program membutuhkan penyimpanan data, jadi tidak perlu membuatnya secara manual.

Setiap tugas memiliki beberapa informasi:

* `id` — ID unik untuk setiap tugas
* `description` — isi atau nama tugas
* `status` — status tugas, yaitu `todo`, `in-progress`, atau `done`
* `createdAt` — waktu ketika tugas dibuat
* `updatedAt` — waktu terakhir tugas diubah

Data tugas akan tetap tersimpan di dalam `tasks.json` sehingga bisa digunakan lagi ketika program dijalankan kembali.

## Contoh

Menambahkan tugas:

```bash
python task_cli.py add "Belajar Python"
```

Kemudian melihat daftar tugas:

```bash
python task_cli.py list
```

Hasilnya kurang lebih seperti:

```text
ID: 1
Description: Belajar Python
Status: todo
Created: 2026-09-24 21:00:00
Updated: 2026-09-24 21:00:00
```

https://roadmap.sh/projects/task-tracker
