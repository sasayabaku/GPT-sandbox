@REM
cd /d %~dp0

python -m venv gpt-vision

call .\gpt-vision\Scripts\activate
pip install -r requirements.txt