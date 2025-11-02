from flask import Flask, render_template, request, send_file, jsonify
from fpdf import FPDF
import os
from datetime import datetime
from io import BytesIO

app = Flask(__name__)

# -------------------------------------
# Detection Logic
# -------------------------------------
drug_keywords = [
    "mdma", "lsd", "mephedrone", "weed", "ganja", "ecstasy", 
    "acid", "snow", "molly", "coke", "dm for", "hit", 
    "available", "plug", "powder", "crystal","cocaine","meth","drugs","Drugs"
]

def detect_drug_content(text):
    text_lower = text.lower()
    detected = [word for word in drug_keywords if word in text_lower]
    if detected:
        # Improved confidence calculation based on:
        # 1. Number of keywords found (more keywords = higher suspicion)
        # 2. Keyword density in text (keywords per word)
        # 3. High-risk keywords (direct drug names vs. indirect terms)
        
        text_words = len(text.split())
        keyword_count = len(detected)
        
        # High-risk keywords (direct drug names)
        high_risk_keywords = ["mdma", "lsd", "mephedrone", "cocaine", "meth", "ecstasy", "molly", "coke"]
        high_risk_found = sum(1 for word in detected if word in high_risk_keywords)
        
        # Base confidence from keyword count (0-70%)
        # 1 keyword = 30%, 2-3 = 50%, 4-5 = 60%, 6+ = 70%
        if keyword_count == 1:
            base_confidence = 30
        elif keyword_count <= 3:
            base_confidence = 50
        elif keyword_count <= 5:
            base_confidence = 60
        else:
            base_confidence = 70
        
        # Add bonus for high-risk keywords (0-20%)
        risk_bonus = min(high_risk_found * 5, 20)
        
        # Add bonus for keyword density (0-10%)
        # If keywords make up more than 5% of text words, add bonus
        if text_words > 0:
            density = (keyword_count / text_words) * 100
            density_bonus = min(density * 0.5, 10)
        else:
            density_bonus = 0
        
        confidence = min(base_confidence + risk_bonus + density_bonus, 100)
        confidence = round(confidence, 2)
        
        return {
            "status": "Suspicious",
            "keywords": detected,
            "confidence": confidence
        }
    else:
        return {
            "status": "Safe",
            "keywords": [],
            "confidence": 0
        }

# -------------------------------------
# PDF Report Generator
# -------------------------------------
def generate_pdf_report(text, result):
    # Create PDF in memory
    pdf = FPDF()
    pdf.add_page()
    
    # Set margins for consistent alignment
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)
    pdf.set_top_margin(20)
    
    # Title - Centered
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 15, "Drug Detection Report", ln=True, align="C")
    pdf.ln(5)
    
    # Date - Left aligned with proper spacing
    pdf.set_font("Arial", size=11)
    pdf.cell(0, 8, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", ln=True, align="L")
    pdf.ln(10)
    
    # Input Message Section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Input Message:", ln=True, align="L")
    pdf.ln(2)
    pdf.set_font("Arial", size=11)
    pdf.set_left_margin(25)
    pdf.multi_cell(0, 7, text)
    pdf.set_left_margin(20)
    pdf.ln(10)
    
    # Detection Result Section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Detection Result:", ln=True, align="L")
    pdf.ln(2)
    pdf.set_font("Arial", size=11)
    pdf.set_left_margin(25)
    pdf.cell(0, 7, f"Status: {result['status']}", ln=True, align="L")
    pdf.ln(3)
    pdf.cell(0, 7, f"Detected Keywords: {', '.join(result['keywords']) if result['keywords'] else 'None'}", ln=True, align="L")
    pdf.set_left_margin(20)
    
    # Generate PDF bytes in memory (output() returns bytearray by default)
    pdf_bytes = pdf.output()
    return BytesIO(pdf_bytes)

# -------------------------------------
# Flask Routes
# -------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({"error": "Please enter a message first."}), 400
    
    result = detect_drug_content(text)
    return jsonify(result)

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.get_json()
    text = data.get('text', '')
    result = data.get('result', {})
    
    pdf_buffer = generate_pdf_report(text, result)
    return send_file(
        pdf_buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name="Forensic_Report.pdf"
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)

