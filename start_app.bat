@echo off
setlocal
echo ===================================================
echo      AEGIS SECURITY PLATFORM - DEPLOYMENT
echo ===================================================
echo.
echo [1/3] Initializing System Environment...

REM Get the absolute path of the script directory
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%aegis-security-platform\src\backend"

echo [2/3] Starting AEGIS Core Engine (Production Mode)...
echo       Host: 0.0.0.0
echo       Port: 8000
echo.
echo       NOTE: Do not close this window while using the system.
echo.

REM Start Backend (Serving Frontend)
start "AEGIS Backend" "..\..\..\.venv\Scripts\uvicorn.exe" app.main:app --host 0.0.0.0 --port 8000

echo [3/3] Launching Control Interface...
timeout /t 5 /nobreak >nul

echo Opening Dashboard...
start http://localhost:8000/dash

echo Opening API Documentation...
start http://localhost:8000/docs

echo.
echo ===================================================
echo      SYSTEM DEPLOYED SUCCESSFULLY
echo ===================================================
echo.
echo NOTE: The frontend (SPA) seems to be missing. 
echo       Access the Dashboard at /dash and API at /docs.
echo.
pause
