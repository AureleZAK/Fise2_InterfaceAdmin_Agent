from bs4 import BeautifulSoup

# Replace 'path/to/your/index.html' with the actual path to your HTML coverage report
html_path = 'htmlcov/index.html'

def extract_coverage_percentage(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Identify the HTML element that contains the coverage percentage
    # Replace 'your-coverage-element-id' with the actual ID or class of the element
    coverage_element = soup.find(id='pc_cov')

    if coverage_element:
        # Extract the text content (coverage percentage)
        coverage_percentage = coverage_element.get_text(strip=True)
        return coverage_percentage
    else:
        return None

# Get the coverage percentage
coverage_percentage = extract_coverage_percentage(html_path)
print(coverage_percentage)