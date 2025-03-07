from fpdf import FPDF
import base64
import datetime

def create_pdf_report(student, percentage):
    pdf = FPDF()
    pdf.add_page()
    
    # Add header
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, "Ahmed's Educational System", 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, 'Gulbahar Petal Gali', 0, 1, 'C')
    pdf.line(10, 30, 200, 30)
    
    # Add student info
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Student Information:', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Name: {student['name']}", 0, 1)
    pdf.cell(0, 10, f"Age: {student['age']}", 0, 1)
    pdf.cell(0, 10, f"Class Applied: {student['class']}", 0, 1)
    pdf.cell(0, 10, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}", 0, 1)
    
    # Add scores
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Test Results:', 0, 1)
    pdf.set_font('Arial', '', 12)
    for section, score in student['scores'].items():
        pdf.cell(0, 10, f"{section}: {score}/2", 0, 1)
    
    # Add overall result
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, f"Overall Percentage: {percentage:.2f}%", 0, 1)
    
    return pdf

def get_pdf_download_link(pdf, filename):
    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">Download PDF Report</a>'
    return href 