@echo off
echo Starting Feedback Board Setup...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH.
    pause
    exit /b
)

if not exist "venv" (
    echo Creating Virtual Environment...
    python -m venv venv
)

echo Activating Virtual Environment...
call venv\Scripts\activate

echo Installing Requirements...
pip install -r requirements.txt

echo Starting Server at http://127.0.0.1:8000
uvicorn app.main:app --reload
pause
