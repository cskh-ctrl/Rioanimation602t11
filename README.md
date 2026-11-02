# Rio Animation - What If - Bo 2 (auto render)

90 video (30 video dai 16:9 + 60 Shorts 9:16) dung tu dong tu `data/scripts.json`
(chuyen tu file Rio_Animation_What_If_Bo2_30_Long_60_Shorts.xlsx):
giong Nam tieng Anh (Kokoro `am_michael`), hoat hinh 2D ve bang code (2D Studio), nhac + SFX tu tao.

- Render chay tren GitHub Actions (`.github/workflows/render.yml`), kich hoat khi sua `pipeline/trigger.txt`.
- Ket qua o muc **Releases**, 3 thu muc lon:
  - `01_Video_Dai_01-30`: 30 video dai MP4 + `00_THONG_TIN_DANG_YOUTUBE.txt`
  - `02_Shorts_01-30`: 30 Shorts MP4 + `00_THONG_TIN_DANG_YOUTUBE.txt`
  - `03_Shorts_31-60`: 30 Shorts MP4 + `00_THONG_TIN_DANG_YOUTUBE.txt`
  - `meta`: anh bia + phu de SRT tung video.
- Chay lai video loi: ghi `FORCE:long_3,short_12` vao `pipeline/trigger.txt` roi commit (video chua co se tu render khi commit trigger bat ky).

## Tai toan bo ve may (giu dung cau truc thu muc)
- Windows: tai file `tai_ve_windows.ps1`, chuot phai > Run with PowerShell.
- macOS: tai `tai_ve_mac.sh`, mo Terminal va chay `bash tai_ve_mac.sh`.
