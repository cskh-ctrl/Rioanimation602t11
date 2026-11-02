# Tai toan bo video Rio Animation bo 2 ve may (Windows PowerShell).
# Cach dung: chuot phai file nay > Run with PowerShell. Video nam trong thu muc RioAnimation_Bo2 canh file nay.
# 3 thu muc lon (01_Video_Dai_01-30, 02_Shorts_01-30, 03_Shorts_31-60), moi thu muc: video MP4 + 00_THONG_TIN_DANG_YOUTUBE.txt
# + 04_Anh_Bia_Phu_De (anh bia, phu de). Chay lai bat ky luc nao: file da tai du se bo qua.
$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"
$repo = "cskh-ctrl/rioanimation602t11"
$root = Join-Path $PSScriptRoot "RioAnimation_Bo2"
function Get-Rel($tag, $folder) {
  $rel = Invoke-RestMethod "https://api.github.com/repos/$repo/releases/tags/$tag"
  if (-not $folder) { $folder = $rel.name }
  $dir = Join-Path $root $folder; New-Item -ItemType Directory -Force -Path $dir | Out-Null
  foreach ($a in ($rel.assets | Where-Object { -not $_.name.StartsWith("info_") } | Sort-Object name)) {
    $f = Join-Path $dir $a.name
    if ((Test-Path $f) -and ((Get-Item $f).Length -eq $a.size)) { Write-Host "Da co: $($a.name)"; continue }
    Write-Host "Dang tai $folder / $($a.name) ..."
    Invoke-WebRequest $a.browser_download_url -OutFile $f
  }
}
foreach ($t in "g01","g02","g03") { Get-Rel $t $null }
Get-Rel "meta" "04_Anh_Bia_Phu_De"
Write-Host "Xong! Mo thu muc: $root"
