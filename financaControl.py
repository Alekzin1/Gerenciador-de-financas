

# Base de dados em memória (Lista de Dicionários)
# Já inicia com dois exemplos para você ter o que listar logo de cara
transacoes = [
    {"id": 1, "descricao": "Salário", "tipo": "Receita", "valor": 3000.00, "categoria": "Trabalho"},
    {"id": 2, "descricao": "Aluguel", "tipo": "Despesa", "valor": 1200.00, "categoria": "Moradia"}
]

# Configuração de limite de alerta (80% da renda gasta)
LIMITE_ALERTA_PERCENTUAL = 80.0


def calcular_totais():
    """Calcula o total de receitas, despesas e o saldo atual."""
    total_receitas = 0.0
    total_despesas = 0.0

    # Estrutura de repetição para varrer as transações
    for t in transacoes:
        if t["tipo"] == "Receita":
            total_receitas += t["valor"]
        elif t["tipo"] == "Despesa":
            total_despesas += t["valor"]

    saldo = total_receitas - total_despesas
    
    # Calcula a porcentagem do orçamento comprometido
    porcentagem_gasta = (total_despesas / total_receitas * 100) if total_receitas > 0 else 0.0

    return total_receitas, total_despesas, saldo, porcentagem_gasta


def exibir_resumo():
    """Exibe o dashboard financeiro atualizado no terminal."""
    receitas, despesas, saldo, pct = calcular_totais()
    
    print("\n" + "="*45)
    print("         DASHBOARD FINANCEIRO (BACKEND)   ")
    print("="*45)
    print(f" Total Receitas: R$ {receitas:.2f}")
    print(f" Total Despesas: R$ {despesas:.2f}")
    print(f" Saldo Atual   : R$ {saldo:.2f}")
    print(f" Orçamento Comprometido: {pct:.1f}%")
    print("="*45)

    # Estruturas condicionais para alertas de lógica de negócio
    if pct >= LIMITE_ALERTA_PERCENTUAL:
        print(" [ALERTA CRÍTICO]: Você comprometeu mais de 80% da sua renda!")
    if saldo < 0:
        print(" [PERIGO]: Seu saldo consolidado está NEGATIVO!")
    print("-" * 45)


def registrar_transacao():
    """Adiciona uma nova movimentação financeira com validações de backend."""
    print("\n--- REGISTRAR NOVA TRANSAÇÃO ---")
    
    descricao = input("Descrição da transação: ").strip()
    if not descricao:
        print("Erro: A descrição não pode ser vazia.")
        return

    print("Selecione o Tipo:")
    print("1. Receita (Entrada)")
    print("2. Despesa (Saída)")
    tipo = input("Escolha (1 ou 2): ").strip()
    
    if tipo == "1":
        tipo_txt = "Receita"
    elif tipo == "2":
        tipo_txt = "Despesa"
    else:
        print("Erro: Opção de tipo inválida.")
        return

    # Tratamento de exceção para garantir a entrada numérica correta
    try:
        valor = float(input("Valor da transação: R$ "))
        if valor <= 0:
            print("Erro: O valor deve ser maior que zero.")
            return
    except ValueError:
        print("Erro: Valor numérico inválido. Use pontos para centavos (Ex: 150.50).")
        return

    categoria = input("Categoria (Ex: Lazer, Alimentação, Salário): ").strip()
    if not categoria:
        categoria = "Geral"

    # Geração automática de ID incremental seguro
    novo_id = transacoes[-1]["id"] + 1 if transacoes else 1

    # Criação do objeto (Dicionário)
    nova_movimentacao = {
        "id": novo_id,
        "descricao": descricao,
        "tipo": tipo_txt,
        "valor": valor,
        "categoria": categoria
    }

    # Insere no "banco de dados"
    transacoes.append(nova_movimentacao)
    print(f"\nSucesso: {tipo_txt} '{descricao}' registrada com ID {novo_id}!")


def extrato_detalhado():
    """Lista todas as transações de forma tabular pura via terminal."""
    print("\n--- EXTRATO DETALHADO DO SISTEMA ---")
    if not transacoes:
        print("Nenhuma transação registrada no sistema.")
        return

    # Cabeçalho formatado espaciado
    print(f"{'ID':<4} | {'Descrição':<18} | {'Tipo':<8} | {'Valor':<12} | {'Categoria':<12}")
    print("-" * 65)
    
    # Loop para renderizar cada linha do extrato
    for t in transacoes:
        print(f"{t['id']:<4} | {t['descricao']:<18} | {t['tipo']:<8} | R$ {t['valor']:>9.2f} | {t['categoria']:<12}")
    print("-" * 65)


def executar_sistema():
    """Loop principal que atua como o orquestrador do terminal."""
    while True:
        exibir_resumo()
        print("1. Registrar Nova Transação")
        print("2. Ver Extrato Detalhado")
        print("3. Encerrar Sistema")
        
        opcao = input("\nSelecione a ação desejada (1-3): ").strip()

        if opcao == "1":
            registrar_transacao()
        elif opcao == "2":
            extrato_detalhado()
        elif opcao == "3":
            print("\nDesconectando do core do sistema... Sessão encerrada.")
            break
        else:
            print("\nAviso: Código de operação inválido. Escolha 1, 2 ou 3.")


# Ponto de entrada padrão do interpretador Python
if __name__ == "__main__":
    executar_sistema()
