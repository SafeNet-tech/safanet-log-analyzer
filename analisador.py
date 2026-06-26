import os
import time

def analisar_logs(ficheiro_entrada, ficheiro_saida):
    print("=" * 60)
    print("           SAFANET LOG ANALYZER v1.0.0          ")
    print("        Otimização e Auditoria de Redes         ")
    print("=" * 60)
    
    if not os.path.exists(ficheiro_entrada):
        print(f"\n[ERRO] Ficheiro '{ficheiro_entrada}' não encontrado!")
        print("Certifica-te de que o ficheiro está na mesma pasta que este script.")
        return

    print(f"\n[+] A iniciar análise do ficheiro: {ficheiro_entrada}...")
    start_time = time.time()
    
    # Palavras-chave que indicam falhas críticas no sistema
    palavras_criticas = ["ERROR", "TIMEOUT", "FAIL", "DISCONNECTED", "CRITICAL"]
    
    linhas_processadas = 0
    erros_detetados = 0
    
    with open(ficheiro_entrada, 'r', encoding='utf-8') as entrada, \
         open(ficheiro_saida, 'w', encoding='utf-8') as saida:
         
        # Escreve o cabeçalho do relatório final
        saida.write("=" * 70 + "\n")
        saida.write("             RELATÓRIO DE ERROS ISOLADOS - SAFANET              \n")
        saida.write("=" * 70 + "\n\n")
        
        for linha in entrada:
            linhas_processadas += 1
            # Verifica se alguma palavra de erro está na linha (convertido para maiúsculas)
            if any(palavra in linha.upper() for palabra in palavras_criticas):
                saida.write(linha)
                erros_detetados += 1
                
        saida.write(f"\n\n" + "=" * 70 + "\n")
        saida.write(f"RESUMO DA AUDITORIA:\n")
        saida.write(f"- Total de linhas analisadas: {linhas_processadas}\n")
        saida.write(f"- Total de falhas críticas isoladas: {erros_detetados}\n")
        saida.write("=" * 70 + "\n")

    end_time = time.time()
    tempo_execucao = (end_time - start_time) * 1000 # em milissegundos

    # Resultado visual para o terminal (perfeito para o teu vídeo)
    print("[✓] Processamento concluído com sucesso!")
    print("-" * 45)
    print(f"-> Linhas analisadas: {linhas_processadas}")
    print(f"-> Eventos críticos isolados: {erros_detetados}")
    print(f"-> Relatório gerado: '{ficheiro_saida}'")
    print(f"-> Tempo de execução: {tempo_execucao:.2f} ms")
    print("-" * 45)
    print("Agência SafeNet - Automação & Dados")
    print("=" * 60)

if __name__ == "__main__":
    # Define os nomes dos ficheiros locais
    arquivo_bruto = "exemplo_log.txt"
    relatorio_final = "relatorio_erros.txt"
    
    analisar_logs(arquivo_bruto, relatorio_final)
