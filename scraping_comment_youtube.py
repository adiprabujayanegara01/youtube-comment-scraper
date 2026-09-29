"""
Scraping komentar YouTube -> CSV / JSON
Install dependensi: pip install youtube-comment-downloader
"""

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from itertools import islice
from pathlib import Path

from youtube_comment_downloader import YoutubeCommentDownloader

DEFAULT_URL = "https://www.youtube.com/watch?v=kIsyUVZhLIw"
SORT_OPTIONS = {"popular": 0, "recent": 1}  # 0 = teratas, 1 = terbaru
FIELDS = [
    "comment_id", "username", "comment", "time",
    "time_iso", "likes", "is_reply", "hearted", "channel_id",
]


def extract_video_id(url: str) -> str:
    """Ambil ID video dari berbagai format URL YouTube."""
    match = re.search(r"(?:v=|youtu\.be/|shorts/|embed/|live/)([A-Za-z0-9_-]{11})", url)
    return match.group(1) if match else "video"


def to_iso(timestamp) -> str:
    """Ubah timestamp (detik) menjadi format tanggal ISO, kosong jika tidak ada."""
    try:
        return datetime.fromtimestamp(float(timestamp)).isoformat(timespec="seconds")
    except (TypeError, ValueError, OSError):
        return ""


def clean_row(c: dict) -> dict:
    """Ubah data mentah komentar menjadi baris yang rapi."""
    return {
        "comment_id": c.get("cid", ""),
        "username": c.get("author", "Unknown"),
        "comment": (c.get("text") or "").replace("\r", " ").strip(),
        "time": c.get("time", "Unknown"),  # biasanya "2 days ago"
        "time_iso": to_iso(c.get("time_parsed")),
        "likes": c.get("votes", "0"),
        "is_reply": bool(c.get("reply", False)),
        "hearted": bool(c.get("heart", False)),
        "channel_id": c.get("channel", ""),
    }


def parse_args():
    p = argparse.ArgumentParser(description="Scraping komentar YouTube")
    p.add_argument("url", nargs="?", default=DEFAULT_URL, help="URL video YouTube")
    p.add_argument("--sort", choices=SORT_OPTIONS, default="popular",
                   help="Urutan komentar (default: popular)")
    p.add_argument("--limit", type=int, default=None,
                   help="Batasi jumlah komentar (default: semua)")
    p.add_argument("--no-replies", action="store_true",
                   help="Lewati balasan komentar")
    p.add_argument("--format", choices=["csv", "json"], default="csv",
                   help="Format output (default: csv)")
    p.add_argument("-o", "--output", help="Nama file output")
    return p.parse_args()


def main():
    args = parse_args()
    video_id = extract_video_id(args.url)
    output = Path(args.output or f"youtube_comments_{video_id}.{args.format}")

    downloader = YoutubeCommentDownloader()
    try:
        comments = downloader.get_comments_from_url(
            args.url, sort_by=SORT_OPTIONS[args.sort]
        )
    except Exception as e:
        sys.exit(f"Gagal mengakses video: {e}")

    if args.limit:
        comments = islice(comments, args.limit)

    rows = []
    csv_file = None
    writer = None

    try:
        # CSV ditulis bertahap, sehingga data tidak hilang jika proses terhenti.
        # utf-8-sig agar emoji/karakter Indonesia tampil benar saat dibuka di Excel.
        if args.format == "csv":
            csv_file = open(output, "w", newline="", encoding="utf-8-sig")
            writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
            writer.writeheader()

        for comment in comments:
            if args.no_replies and comment.get("reply"):
                continue
            row = clean_row(comment)
            rows.append(row)
            if writer:
                writer.writerow(row)
            if len(rows) % 100 == 0:
                print(f"  ...{len(rows)} komentar terkumpul", end="\r", flush=True)

    except KeyboardInterrupt:
        print("\nDihentikan pengguna, menyimpan data yang sudah terkumpul...")
    except Exception as e:
        print(f"\nTerjadi error saat scraping: {e}\nMenyimpan data yang sudah terkumpul...")
    finally:
        if csv_file:
            csv_file.close()

    if args.format == "json":
        with open(output, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)

    if rows:
        print(f"Berhasil menyimpan {len(rows)} komentar ke {output}")
    else:
        print("Tidak ada komentar yang berhasil diambil "
              "(komentar dinonaktifkan atau URL tidak valid).")


if __name__ == "__main__":
    main()