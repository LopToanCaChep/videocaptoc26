@echo off
echo ==============================================
echo   DONG BO VIDEO CAP TOC LEN GITHUB
echo ==============================================

echo [1] Kiem tra schema bang validate_csv.py...
python ..\validate_csv.py video_captoc
if %errorlevel% neq 0 (
    echo [Loi] File CSV co van de, dung sync.
    pause
    exit /b %errorlevel%
)

echo.
echo [2] Dang build file index.html tu CSV...
python build_video.py
if %errorlevel% neq 0 (
    echo [Loi] Build that bai, dung sync.
    pause
    exit /b %errorlevel%
)

echo.
echo [3] Dang day du lieu len Github...
git add .
git commit -m "auto-sync: update video captoc web"
git push

echo.
echo [Thanh cong] Da cap nhat moi nhat len Web!
pause
