# Drug Trafficking Detection System

A Flask web application that analyzes text messages for potential drug-related content and generates forensic reports.

## Features

- Text analysis for drug-related keywords
- Real-time detection with confidence scores
- PDF report generation for forensic purposes
- Modern, responsive web interface

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. **Activate the virtual environment** (if using venv):
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or manually install:
   ```bash
   pip install flask fpdf2
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   - Open your web browser
   - Navigate to: `http://localhost:5000`
   - Or: `http://127.0.0.1:5000`

3. **Using the Application**:
   - Enter text in the message field
   - Click "Analyze Message" to detect drug-related content
   - If suspicious content is found, you can generate a PDF report
   - PDF reports are saved in the `reports/` directory

## Project Structure

```
Final year Project/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface
└── reports/              # Generated PDF reports (created automatically)
```

## API Endpoints

- `GET /` - Main web interface
- `POST /analyze` - Analyze text for drug content
  - Request: `{"text": "your message here"}`
  - Response: `{"status": "Suspicious"|"Safe", "keywords": [], "confidence": 0}`
- `POST /generate_pdf` - Generate PDF report
  - Request: `{"text": "message", "result": {...}}`
  - Response: PDF file download

## Notes

- The application runs in debug mode by default
- Reports are automatically saved with timestamps
- Detection is based on keyword matching with configurable sensitivity

## Deployment

This application can be deployed to various platforms. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

### Quick Deploy Options:

1. **Render** (Recommended) - [render.com](https://render.com)
   - Free tier available
   - Easy Flask deployment
   - Auto-deploy from GitHub

2. **Railway** - [railway.app](https://railway.app)
   - $5 free credit monthly
   - Always-on option
   - Simple setup

3. **PythonAnywhere** - [pythonanywhere.com](https://www.pythonanywhere.com)
   - Free tier for Python apps
   - Full Python environment

For complete deployment guide with step-by-step instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

## Troubleshooting

- **Port already in use**: The app automatically uses the `PORT` environment variable or defaults to 5000
- **Module not found**: Ensure dependencies are installed: `pip install flask fpdf2`
- **Reports not generating**: Check write permissions in the project directory
- **Deployment issues**: Check platform-specific logs and ensure all files are committed to Git

