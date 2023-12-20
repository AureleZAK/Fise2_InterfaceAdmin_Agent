"""
Module: coverage.py

This module contains functions to extract coverage percentage from an HTML coverage report.
"""


from bs4 import BeautifulSoup


# Replace 'path/to/your/index.html' with the actual path to your HTML coverage report
HTML_PATH = 'htmlcov/index.html'

def extract_coverage_percentage(file_path):
    """
    Extracts coverage percentage from an HTML coverage report.

    Args:
    - html_path (str): The path to the HTML coverage report.

    Returns:
    - coverage_percentage (str or None): The extracted coverage percentage or None if not found.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Identify the HTML element that contains the coverage percentage
    # Replace 'your-coverage-element-id' with the actual ID or class of the element
    coverage_element = soup.find(id='pc_cov')

    if coverage_element:
        # Extract the text content (coverage percentage)
        coverage_percentage_found = coverage_element.get_text(strip=True)
        return coverage_percentage_found
    return None

# Get the coverage percentage
coverage_percentage = extract_coverage_percentage(HTML_PATH)
print(coverage_percentage)
