# YouTube Comment Scraper

Tool sederhana berbasis Python untuk mengambil komentar dari video YouTube dan menyimpannya dalam format **CSV** atau **JSON**.

Project ini menggunakan library [`youtube-comment-downloader`](https://pypi.org/project/youtube-comment-downloader/) untuk mengambil data komentar tanpa menggunakan YouTube Data API secara langsung.

## ✨ Features

* Scrape komentar dari video YouTube
* Mendukung berbagai format URL YouTube
* Menyimpan hasil dalam format CSV atau JSON
* Mengurutkan komentar berdasarkan:

  * Popular / teratas
  * Recent / terbaru
* Membatasi jumlah komentar yang diambil
* Opsi untuk melewati balasan komentar
* Menyimpan informasi:

  * Comment ID
  * Username
  * Isi komentar
  * Waktu komentar
  * Waktu dalam format ISO
  * Jumlah likes/votes
  * Status reply
  * Status heart
  * Channel ID
* CSV menggunakan `utf-8-sig` agar karakter Indonesia dan emoji lebih kompatibel saat dibuka menggunakan Excel
* Data CSV ditulis secara bertahap sehingga data yang sudah berhasil dikumpulkan tetap tersimpan apabila proses dihentikan

## 📁 Project Structure

```text
youtube-comment-scraper/
│
├── scraping_comment_youtube.py
├── youtube_comments_kIsyUVZhLIw.csv
└── README.md
```

## 🛠️ Requirements

Pastikan sudah menginstal:

* Python 3.x
* `youtube-comment-downloader`

## 🚀 Installation

### 1. Clone repository

```bash
git clone https://github.com/USERNAME/youtube-comment-scraper.git
cd youtube-comment-scraper
```

Ganti `USERNAME` dengan username GitHub Anda.

### 2. Install dependency

```bash
pip install youtube-comment-downloader
```

Atau jika menggunakan `pip3`:

```bash
pip3 install youtube-comment-downloader
```

## ▶️ Usage

Format dasar:

```bash
python scraping_comment_youtube.py "URL_VIDEO_YOUTUBE"
```

Contoh:

```bash
python scraping_comment_youtube.py "https://www.youtube.com/watch?v=kIsyUVZhLIw"
```

Secara default, hasil akan disimpan sebagai:

```text
youtube_comments_kIsyUVZhLIw.csv
```

## 📌 Menentukan Urutan Komentar

### Komentar terpopuler

```bash
python scraping_comment_youtube.py "URL_VIDEO" --sort popular
```

### Komentar terbaru

```bash
python scraping_comment_youtube.py "URL_VIDEO" --sort recent
```

Default:

```text
popular
```

## 🔢 Membatasi Jumlah Komentar

Untuk mengambil misalnya 100 komentar:

```bash
python scraping_comment_youtube.py "URL_VIDEO" --limit 100
```

Contoh:

```bash
python scraping_comment_youtube.py "https://www.youtube.com/watch?v=kIsyUVZhLIw" --limit 500
```

## 💬 Mengabaikan Balasan Komentar

Gunakan:

```bash
python scraping_comment_youtube.py "URL_VIDEO" --no-replies
```

Dengan opsi tersebut, balasan terhadap komentar tidak akan dimasukkan ke hasil scraping.

## 📄 Output CSV

Untuk menyimpan hasil sebagai CSV:

```bash
python scraping_comment_youtube.py "URL_VIDEO" --format csv
```

CSV merupakan format default.

Kolom yang dihasilkan:

| Field        | Description                                   |
| ------------ | --------------------------------------------- |
| `comment_id` | ID komentar YouTube                           |
| `username`   | Username pembuat komentar                     |
| `comment`    | Isi komentar                                  |
| `time`       | Informasi waktu relatif komentar              |
| `time_iso`   | Timestamp dalam format ISO                    |
| `likes`      | Jumlah likes/votes                            |
| `is_reply`   | Menunjukkan apakah komentar merupakan reply   |
| `hearted`    | Menunjukkan apakah komentar mendapatkan heart |
| `channel_id` | ID channel pengguna                           |

## 🗂️ Output JSON

Untuk menyimpan hasil dalam JSON:

```bash
python scraping_comment_youtube.py "URL_VIDEO" --format json
```

Contoh:

```bash
python scraping_comment_youtube.py "https://www.youtube.com/watch?v=kIsyUVZhLIw" --format json
```

## 💾 Menentukan Nama File Output

Gunakan parameter `--output` atau `-o`.

Contoh CSV:

```bash
python scraping_comment_youtube.py "URL_VIDEO" -o hasil_komentar.csv
```

Contoh JSON:

```bash
python scraping_comment_youtube.py "URL_VIDEO" --format json -o hasil_komentar.json
```

## ⚙️ Command Options

| Option           | Description                    | Default                       |
| ---------------- | ------------------------------ | ----------------------------- |
| `url`            | URL video YouTube              | URL default di script         |
| `--sort`         | Urutan `popular` atau `recent` | `popular`                     |
| `--limit`        | Jumlah maksimum komentar       | Semua                         |
| `--no-replies`   | Mengabaikan balasan komentar   | Tidak aktif                   |
| `--format`       | Format `csv` atau `json`       | `csv`                         |
| `-o`, `--output` | Nama file output               | Otomatis berdasarkan video ID |

## 🧪 Example

Perintah berikut mengambil maksimal 1.000 komentar terbaru dan menyimpannya sebagai CSV tanpa replies:

```bash
python scraping_comment_youtube.py \
"https://www.youtube.com/watch?v=kIsyUVZhLIw" \
--sort recent \
--limit 1000 \
--no-replies \
--format csv \
-o comments.csv
```

## 📊 Example Dataset

Repository ini juga menyertakan contoh dataset hasil scraping:

```text
youtube_comments_kIsyUVZhLIw.csv
```

Dataset tersebut dapat digunakan untuk kebutuhan seperti:

* Exploratory Data Analysis (EDA)
* Analisis sentimen
* Analisis engagement
* Analisis topik komentar
* Text mining
* Natural Language Processing (NLP)
* Visualisasi data

## ⚠️ Disclaimer

Project ini dibuat untuk tujuan pembelajaran, penelitian, dan pengolahan data.

Pastikan penggunaan tool ini tetap mematuhi:

* Terms of Service YouTube
* Hak cipta dan privasi pengguna
* Ketentuan penggunaan data yang berlaku
* Peraturan atau kebijakan yang relevan

Jangan menggunakan hasil scraping untuk melakukan spam, penyalahgunaan data, atau aktivitas yang melanggar ketentuan platform.

## 👤 Author

**Adi Prabu Jayanegara**