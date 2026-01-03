from pypdf import PdfReader
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "CV_Gabriel_Bueno_General.pdf"

try:
    reader = PdfReader(filename)
    print(f"--- SIMULANDO LEITURA DO ATS PARA: {filename} ---\n")
    
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    
    if len(full_text.strip()) == 0:
        print("❌ PERIGO: O PDF parece vazio ou é uma imagem! O ATS não vai ler nada.")
    else:
        print("✅ SUCESSO: Texto extraído corretamente.")
        print(f"   Total de caracteres lidos: {len(full_text)}")
    
    print("\n--- TESTE DE PALAVRAS-CHAVE CRÍTICAS ---")
    
    keywords = ["React", "Next.js", "TypeScript", "Software Engineer", "Gabriel Bueno Hygino"]
    
    for word in keywords:
        if word.lower() in full_text.lower():
            print(f"✅ Encontrado: {word}")
        else:
            print(f"❌ ERRO CRÍTICO: Não encontrei '{word}' no texto extraído!")

except FileNotFoundError:
    print("Arquivo não encontrado.")