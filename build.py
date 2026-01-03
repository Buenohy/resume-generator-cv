import yaml
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import sys

def generate_pdf(target_company=None):
    with open('content.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if target_company:
        print(f"Gerando versão para: {target_company}")
        data['resumo'] = f"Engenheiro de software interessado em resolver problemas na {target_company}. " + data['resumo']
    
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    html_string = template.render(data)

    nome_arquivo = f"CV_SeuNome_{target_company if target_company else 'Geral'}.pdf"
    
    HTML(string=html_string, base_url='.').write_pdf(nome_arquivo)
    print(f"Sucesso! Arquivo criado: {nome_arquivo}")

if __name__ == "__main__":
    empresa = sys.argv[1] if len(sys.argv) > 1 else None
    generate_pdf(empresa)