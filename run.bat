@echo off
echo Installing dependencies...
python -m pip install flask fpdf2 --quiet
echo.
echo Starting Flask application...
echo Open your browser and go to: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py

