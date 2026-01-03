import yaml
import sys
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from pypdf import PdfReader, PdfWriter

def generate_pdf(target_company=None):
    try:
        with open('content.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print("Error: 'content.yaml' file not found.")
        return

    if target_company:
        print(f"Generating version for: {target_company}")
        if 'summary' in data:
            prefix = f"Software Engineer enthusiastic about driving impact at {target_company}. "
            data['summary'] = prefix + data['summary']
    else:
        print("Generating General version...")
        target_company = "General"

    env = Environment(loader=FileSystemLoader('.'))
    try:
        template = env.get_template('template.html')
    except Exception as e:
        print(f"Error loading template: {e}")
        return

    html_string = template.render(data)

    temp_filename = "temp_cv.pdf"
    try:
        HTML(string=html_string, base_url='.').write_pdf(temp_filename)
    except Exception as e:
        print(f"Error generating visual PDF: {e}")
        return

    final_filename = f"CV_Gabriel_Bueno_{target_company}.pdf"

    try:
        reader = PdfReader(temp_filename)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        meta = data.get('meta_ats', {})
        role = meta.get('role_target', 'Software Engineer')
        final_title = f"{role} - {target_company}" if target_company != "General" else role
        
        doc_language = data['info'].get('language', 'en-US')
        branding_identity = f"{data['info']['name']} - {role}"

        now = datetime.now()
        pdf_date = now.strftime("D:%Y%m%d%H%M%S")

        metadata_dict = {
            '/Title': final_title,
            '/Author': data['info']['name'],
            '/Subject': meta.get('subject', ''),
            '/Keywords': meta.get('keywords', ''),
            '/Creator': branding_identity,
            '/Producer': branding_identity,
            
            '/CreationDate': pdf_date,
            '/ModDate': pdf_date,

            '/Contributor': meta.get('contributor', data['info']['name']),
            '/Coverage': meta.get('coverage', ''),
            '/Identifier': meta.get('identifier', ''),
            '/Publisher': meta.get('publisher', ''),
            '/Relation': meta.get('relation', ''),
            '/Rights': meta.get('rights', ''),
            '/Source': meta.get('source', ''),
            '/Type': 'Resume',
            '/Language': doc_language,
            
            '/Target-Company': target_company,
            '/Target-Position': role,
            '/Relevance': 'High Priority', 
            
            '/Note': meta.get('notes', '')
        }

        writer.add_metadata(metadata_dict)

        with open(final_filename, "wb") as f_out:
            writer.write(f_out)

        os.remove(temp_filename)

        print(f"Success! Optimized ATS PDF created: {final_filename}")
        print(f"Metadata Title injected: {final_title}")

    except Exception as e:
        print(f"Error injecting metadata: {e}")

if __name__ == "__main__":
    company_arg = sys.argv[1] if len(sys.argv) > 1 else None
    generate_pdf(company_arg)