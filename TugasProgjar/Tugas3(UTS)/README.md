# Tugas 3 (UTS)
```
Nama : Mujahid Khairuddin
NRP : 05111640000169
Kelas : Pemrograman Jaringan F
```


## Cara Penggunaan
Untuk run program, bisa download semua file di folder ini

**Server**
```
    1. Untuk run program, "python3 server.py [port]". Pastikan penggunaan port antara server dengan client sama. Contohnya "python3 server.py 9000".
    2. Program akan bekerja. Untuk mengakhiri, saya menggunakan Ctrl+C.
```

**Client**
```
    1. Pastikan sudah run program server dulu.
    2. Untuk run program, "python3 client.py [server_ip] [port]". Pastikan port sama dengan port server. Contohnya "python3 client.py localhost 9000".
    3. Ada beberapa perintah yang digunakan di client, diantaranya
        - get : untuk mengambil file dari direktori server. Cara menggunakannya "get [nama_file.ekstensi]". Contohnya "get cmyk.png". File yang masuk ke direktori client nama filenya akan berubah menjadi "Received-nama_file.ekstensi"
        - put : untuk menyimpan file ke direktori server.  Cara menggunakannya "put [nama_file.ekstensi]". Contohnya "put doc.pdf". Tidak ada perubahan nama pada direktori server, nama sesuai dengan yang dikirim client.
        - exit : untuk menutup program.
```