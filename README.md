# PDF Table Extractor

Hi! 👋 I created this Python tool to help extract tables from PDF files. It's particularly useful when you need to work with financial reports, research papers, or any PDF that contains important tabular data.

## What Does It Do?

This tool:
- Takes any PDF file as input
- Finds all the tables in it
- Saves each table as a separate Excel file
- Keeps everything organized by naming files based on page numbers

## Getting Started

1. First, clone this repository to your computer:
```bash
git clone <your-repo-url>
cd pdf-table-extractor
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## How to Use It

It's super simple! Just run:
```python
python pdf_extractor.py your_file.pdf
```

That's it! The tool will:
1. Create an 'output' folder (if it doesn't exist)
2. Find all tables in your PDF
3. Save each table as an Excel file in the output folder
4. Name files like 'table_page1_num1.xlsx' (meaning: first table on page 1)

Want to save files somewhere else? No problem:
```python
python pdf_extractor.py your_file.pdf --output-dir my_folder
like : python3 pdf_extractor.py stock_market_dataset.pdf 
```

## The Code

I've tried to keep the code clean and well-organized:
- `pdf_extractor.py`: The main script that does all the work
- `requirements.txt`: Lists all the packages you need

## What I Used

I chose these packages because they're reliable and get the job done:
- `pdfplumber`: For reading PDFs and finding tables
- `pandas`: For handling the table data
- `openpyxl`: For creating Excel files

## Testing

To run the tests:
```bash
pytest tests/
```

## Need Help?

If you run into any problems:
1. Make sure your PDF file exists and is readable
2. Check that you have all the required packages installed
3. Look at the error messages - I've tried to make them helpful!

## Future Improvements

I'm planning to add:
- Support for more complex table layouts
- Option to combine all tables into one Excel file
- Better handling of merged cells
- Preview of extracted tables before saving

## About Me

I'm a Python developer who loves making tools that solve real problems. This project was created as part of my internship application, where I focused on writing clean, maintainable code that others can easily understand and use.

