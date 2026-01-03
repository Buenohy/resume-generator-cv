from pypdf import PdfReader
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "CV_Gabriel_Bueno_Google.pdf"

try:
    reader = PdfReader(filename)
    meta = reader.metadata

    print(f"\n--- METADADOS ENCONTRADOS EM: {filename} ---\n")
    
    if meta:
        for key, value in meta.items():
            clean_key = key.replace('/', '')
            print(f"[{clean_key}]: {value}")
    else:
        print("Nenhum metadado encontrado!")

    print("\n----------------------------------------------")

except FileNotFoundError:
    print(f"Erro: Arquivo '{filename}' não encontrado.")