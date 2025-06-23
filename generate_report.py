import csv
from fpdf import FPDF

#  Read data from the CSV
data = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

#  Create a PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# Add a title
pdf.cell(0, 10, "Employee Report", align='C', ln=True)

# Add total employee count
count = len(data)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Total Employees: {count}", ln=True)

# Add a table header
pdf.set_font("Arial", 'B', 12)
pdf.cell(40, 10, "Name", 1)
pdf.cell(40, 10, "Department", 1)
pdf.cell(40, 10, "Salary", 1, ln=True)

# Add data rows
pdf.set_font("Arial", '', 12)
for row in data:
    pdf.cell(40, 10, row["Name"], 1)
    pdf.cell(40, 10, row["Department"], 1)
    pdf.cell(40, 10, row["Salary"], 1, ln=True)

# Save the PDF
pdf.output("Report.pdf")

# Final message
print(" Done! Check the Report.pdf file.")
