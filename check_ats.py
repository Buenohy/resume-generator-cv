import glob
import os
from pypdf import PdfReader

pattern = "CV_Gabriel_Bueno_*.pdf"
list_of_files = glob.glob(pattern)

if not list_of_files:
    print(f"❌ Nenhum arquivo encontrado com o padrão: {pattern}")
    print("Rode primeiro: python build.py Google")
    exit()

latest_file = max(list_of_files, key=os.path.getmtime)

print(f"\n📄 ANALISANDO ARQUIVO MAIS RECENTE: {latest_file}")
print("="*60)

try:
    reader = PdfReader(latest_file)
    
    print("🔍 [CHECK 1] METADADOS ATS:")
    meta = reader.metadata
    if meta:
        keys_to_check = ['/Title', '/Author', '/Keywords', '/CreationDate', '/Target-Company']
        for key in keys_to_check:
            val = meta.get(key, '❌ Ausente')
            print(f"   {key.replace('/', '')}: {val}")
    else:
        print("   ❌ Nenhum metadado encontrado!")

    print("\n🔍 [CHECK 2] LEITURA DE TEXTO (OCR):")
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    
    char_count = len(full_text.strip())
    if char_count < 100:
        print("   ❌ CRÍTICO: O PDF parece vazio ou é uma imagem (Pouco texto extraído).")
    else:
        print(f"   ✅ Texto extraído com sucesso ({char_count} caracteres).")
        
        keywords_check = ["React", "Software Engineer", "Bueno"]
        found_all = True
        for kw in keywords_check:
            if kw.lower() in full_text.lower():
                print(f"      ✅ Encontrado: '{kw}'")
            else:
                print(f"      ❌ Faltando: '{kw}'")
                found_all = False
        
        if found_all:
            print("\n🚀 CONCLUSÃO: O PDF está excelente para o ATS!")

except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")