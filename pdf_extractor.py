#!/usr/bin/env python3
"""
PDF Table Extractor

This script helps extract tables from PDF files and saves them as Excel files.
I created this tool to help process financial and business PDFs that contain 
important tabular data.

"""

import os
import logging
import argparse
from typing import List, Dict

import pandas as pd
import pdfplumber

# Set up logging to track what's happening
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PDFTableExtractor:
    """
    A helpful tool to extract tables from PDF files and save them as Excel.
    I made this class as simple as possible while keeping all the important functionality.
    """
    
    def __init__(self, pdf_path: str, output_dir: str = "output"):
        """
        Start up our PDF table extractor.
        
        Args:
            pdf_path: Where to find the PDF file
            output_dir: Where to save the Excel files (defaults to "output")
        """
        self.pdf_path = pdf_path
        self.output_dir = output_dir
        self._check_files_and_folders()
        
    def _check_files_and_folders(self) -> None:
        """Make sure we have everything we need before starting."""
        # First, check if the PDF exists
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"Hey, I couldn't find the PDF file: {self.pdf_path}")
            
        # Make sure it's actually a PDF
        if not self.pdf_path.lower().endswith('.pdf'):
            raise ValueError("Oops! The file needs to be a PDF")
            
        # Create output folder if needed
        os.makedirs(self.output_dir, exist_ok=True)
        
    def extract_tables(self) -> List[Dict]:
        """
        The main function that gets all tables from the PDF.
        Returns a list of tables with their data and location info.
        """
        found_tables = []
        
        try:
            # Open and process the PDF
            with pdfplumber.open(self.pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    tables_on_page = page.extract_tables()
                    
                    for table_num, table in enumerate(tables_on_page, 1):
                        if table:  # Make sure we have actual data
                            # Convert to a pandas DataFrame for easier handling
                            table_data = pd.DataFrame(table[1:], columns=table[0])
                            
                            # Clean up column names
                            table_data.columns = table_data.columns.str.strip()
                            
                            # Keep track of where we found this table
                            found_tables.append({
                                'data': table_data,
                                'page': page_num,
                                'table_num': table_num
                            })
                            
                            logger.info(f"Found table {table_num} on page {page_num}")
                            
        except Exception as error:
            logger.error(f"Had some trouble with the PDF: {str(error)}")
            raise
            
        if not found_tables:
            logger.warning("Didn't find any tables in the PDF")
            
        return found_tables
    
    def save_tables(self, tables: List[Dict]) -> None:
        """
        Save each table we found as a separate Excel file.
        
        Args:
            tables: List of tables with their data and location
        """
        for table in tables:
            # Create a descriptive filename
            excel_name = f"table_page{table['page']}_num{table['table_num']}.xlsx"
            save_path = os.path.join(self.output_dir, excel_name)
            
            try:
                # Save to Excel without the index numbers
                table['data'].to_excel(save_path, index=False)
                logger.info(f"Saved the table to {save_path}")
            except Exception as error:
                logger.error(f"Couldn't save the table to {save_path}: {str(error)}")
                raise
    
    def extract_and_save(self) -> None:
        """
        Do everything in one go - extract tables and save them.
        This is the main function you'll probably want to use.
        """
        tables = self.extract_tables()
        if tables:
            self.save_tables(tables)
            logger.info(f"All done! Successfully saved {len(tables)} tables")
        else:
            logger.warning("No tables found to save")

def main():
    """
    Handle running this as a command-line tool.
    Makes it easy to use - just run: python pdf_extractor.py your_file.pdf
    """
    parser = argparse.ArgumentParser(
        description="A friendly tool to extract tables from PDFs and save them as Excel files"
    )
    parser.add_argument("pdf_path", help="The PDF file you want to process")
    parser.add_argument(
        "--output-dir", 
        default="output", 
        help="Where to save the Excel files (default: output)"
    )
    
    args = parser.parse_args()
    
    try:
        extractor = PDFTableExtractor(args.pdf_path, args.output_dir)
        extractor.extract_and_save()
    except Exception as error:
        logger.error(f"Something went wrong: {str(error)}")
        raise

if __name__ == "__main__":
    main()
