def read_all_pages_return(pdf_path):
    print("Using return: loading all pages at once...")
    doc = []
    for page_num in range(1, 11):  # Simulate 10 pages
        doc.append(f"[Page {page_num}] This is the content of page {page_num}.\n")
    return doc

# Usage
pages = read_all_pages_return("care rating.pdf")
for i, page in enumerate(pages):
    print(f"Loaded Page {i+1}")
    print(page)
    print("-" * 40)