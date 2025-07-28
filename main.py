import fitz
import json
import os

def extract_relevant_sections(pdf_path, keywords):
    doc = fitz.open(pdf_path)
    results = []
    for i, page in enumerate(doc):
        text = page.get_text()
        for kw in keywords:
            if kw.lower() in text.lower():
                results.append({
                    "page": i + 1,
                    "text_snippet": text.strip()[:200]
                })
                break
    return results

def main():
    with open("persona_task.json", "r") as f:
        query = json.load(f)

    keywords = query.get("task_keywords", [])
    output = []

    for pdf_file in os.listdir("sample_docs"):
        if pdf_file.endswith(".pdf"):
            path = os.path.join("sample_docs", pdf_file)
            sections = extract_relevant_sections(path, keywords)
            output.append({
                "pdf": pdf_file,
                "sections": sections
            })

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
