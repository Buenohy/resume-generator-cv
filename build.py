import yaml
import sys
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

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
            print("Warning: Key 'summary' not found in YAML. Skipping text injection.")
    else:
        print("Generating General version (no specific company targeted)...")

    env = Environment(loader=FileSystemLoader('.'))
    try:
        template = env.get_template('template.html')
    except Exception as e:
        print(f"Error loading template: {e}")
        return

    html_string = template.render(data)

    suffix = target_company if target_company else 'General'
    filename = f"CV_Gabriel_Bueno_{suffix}.pdf"
    
    try:
        HTML(string=html_string, base_url='.').write_pdf(filename)
        print(f"Success! File created: {filename}")
    except Exception as e:
        print(f"Error generating PDF: {e}")

if __name__ == "__main__":
    company_arg = sys.argv[1] if len(sys.argv) > 1 else None
    generate_pdf(company_arg)