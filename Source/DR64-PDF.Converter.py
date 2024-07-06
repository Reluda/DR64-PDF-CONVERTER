import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader
import docx
import pandas as pd

def convert_pdf_to_txt(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        for page in reader.pages:
            f.write(page.extract_text())
            f.write('\n')

def convert_pdf_to_docx(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    doc = docx.Document()
    for page in reader.pages:
        doc.add_paragraph(page.extract_text())
    doc.save(output_path)

def convert_pdf_to_xlsx(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    data = {'Page': [], 'Content': []}
    for i, page in enumerate(reader.pages):
        data['Page'].append(i + 1)
        data['Content'].append(page.extract_text())
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_path.set(file_path)

def convert_file():
    pdf_file = pdf_path.get()
    if not pdf_file:
        messagebox.showerror("Error", "Please select a PDF file")
        return

    output_format = format_var.get()
    output_file = filedialog.asksaveasfilename(defaultextension=f".{output_format}", filetypes=[(f"{output_format.upper()} files", f"*.{output_format}")])
    if not output_file:
        return

    try:
        if output_format == "txt":
            convert_pdf_to_txt(pdf_file, output_file)
        elif output_format == "docx":
            convert_pdf_to_docx(pdf_file, output_file)
        elif output_format == "xlsx":
            convert_pdf_to_xlsx(pdf_file, output_file)
        messagebox.showinfo("Success", f"File converted to {output_format.upper()} successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert file: {e}")

app = tk.Tk()
app.title("Daniel Renehan - Candidate - Workpro ID: 2598731")

pdf_path = tk.StringVar()
format_var = tk.StringVar(value="txt")

tk.Label(app, text="Select PDF file:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(app, textvariable=pdf_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_pdf).grid(row=0, column=2, padx=10, pady=10)

tk.Label(app, text="Select Output Format:").grid(row=1, column=0, padx=10, pady=10)
tk.OptionMenu(app, format_var, "txt", "docx", "xlsx").grid(row=1, column=1, padx=10, pady=10)

tk.Button(app, text="Convert", command=convert_file).grid(row=2, column=0, columnspan=3, pady=20)

app.mainloop()
