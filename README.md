# Gerenciador-de-financas


## 4.1 Identificação
* **Nome completo do aluno:** Alexandre de Souza Mariano
* **Curso:** Análise e desenvolvimento de sistemas
* **Disciplina:** Programação de Computadores
* **Data:** 12/06/2026

---

## 4.2 Título do Projeto
** Sistema  de Finanças Pessoais via Terminal (Backend Engine)**

---

## 4.3 Descrição do Problema

O problema consiste em desenvolver um programa de terminal simples e eficiente, capaz de registrar as movimentações financeiras diárias, calcular o saldo atual e avisar o usuário caso ele gaste mais do que uma meta segura, ajudando no controle do orçamento pessoal.

---

## 4.4 Objetivo do Programa
O programa tem o objetivo de funcionar como um gerenciador financeiro acessível. Ele recebe os dados digitados pelo usuário, salva as informações em uma lista de dicionários enquanto o programa estiver rodando, calcula os totais e mostra alertas de risco na tela."

---

## 4.5 Descrição Geral da Solução
O sistema foi desenvolvido em Python utilizando funções para dividir e organizar o código. Cada transação é guardada como um dicionário, e todos esses dicionários ficam salvos dentro de uma lista principal. O menu do sistema roda dentro de um laço 'while' que só fecha quando o usuário pede

---

## 4.6 Estrutura do Programa
O código-fonte está organizado de forma modular através das seguintes funções:

* `calcular_totais()`: Varre a coleção de dados em memória utilizando laços de repetição, filtra os registros por tipo e retorna os agregados financeiros calculados (Receitas, Despesas, Saldo e Percentual Comprometido).
* `exibir_resumo()`: Atua como a camada de saída do dashboard no terminal. Exibe os resultados matemáticos processados e executa condicionais de segurança para exibição de alertas de risco.
* `registrar_transacao()`: Camada de input de dados do sistema. Realiza a captura de strings e floats, aplica regras de validação contra campos nulos, trata erros de conversão de tipos e faz o append do novo registro na lista.
* `extrato_detalhado()`: Itera sobre os registros armazenados e gera uma saída formatada em colunas alinhadas, simulando uma tabela pura de banco de dados.
* `executar_sistema()`: Orquestrador central e ponto de entrada da aplicação, contendo o loop principal (`Main Loop`) e o tratamento de rotas do menu.

---

## 4.7 Variáveis e Tipos de Dados

| Nome da Variável | Tipo de Dado | Finalidade |
| :--- | :--- | :--- |
| `transacoes` | Lista (`list`) de Dicionários | Atua como a estrutura central de persistência de dados em memória. |
| `total_receitas` | Decimal (`float`) | Acumulador aritmético dos valores categorizados como "Receita". |
| `total_despesas` | Decimal (`float`) | Acumulador aritmético dos valores categorizados como "Despesa". |
| `saldo` | Decimal (`float`) | Armazena o resultado da diferença entre a receita total e a despesa total. |
| `porcentagem_gasta`| Decimal (`float`) | Armazena a métrica percentual do orçamento comprometido. |
| `LIMITE_ALERTA_PERCENTUAL` | Constante (`float`) | Define a regra de negócio do limite crítico de segurança, fixada em `80.0`. |
| `novo_id` | Inteiro (`int`) | Identificador numérico exclusivo gerado incrementalmente para indexação. |

---

## 4.8 Fluxo do Programa
O fluxo de execução do sistema segue a ordem lógica abaixo:

1. **Inicialização:** O interpretador Python aloca a lista `transacoes` na memória com registros pré-existentes.
2. **Ciclo de Processamento Principal:**
   * A função `calcular_totais()` é invocada, limpando e reprocessando todos os valores da lista.
   * O dashboard de resumo é impresso na tela (`exibir_resumo()`).
   * **Avaliação de Gatilhos:** Caso a porcentagem gasta seja maior ou igual a 80%, um aviso de emergência é embutido na saída. Caso o saldo geral seja negativo, um alerta de perigo é exibido.
3. **Interação com o Usuário:** O menu exibe as opções e o programa aguarda a escolha de um endpoint de ação.
4. **Desvio Condicional:**
   * **Opção 1:** O fluxo desvia para `registrar_transacao()`, executa as validações, insere o objeto na lista e retorna ao passo 2.
   * **Opção 2:** O fluxo desvia para `extrato_detalhado()`, varre a lista exibindo a tabela completa e retorna ao passo 2.
   * **Opção 3:** Rompe o laço de repetição (`break`), finaliza o processo do terminal e encerra a aplicação.

---

## 4.9 Trechos Comentados do Código

### Tratamento de Exceções e Validação de Tipos
O bloco abaixo demonstra o tratamento robusto do backend para evitar falhas de execução (runtime errors) caso o usuário insira letras no campo numérico:

    try:
        valor = float(input("Valor da transação: R$ "))
        if valor <= 0:
            print("Erro: O valor deve ser maior que zero.")
            return
    except ValueError:
        print("Erro: Valor numérico inválido. Use pontos para centavos (Ex: 150.50).")
        return

### Lógica de ID Incremental Dinâmico
Para simular uma chave primária autoincrementável de banco de dados sem correr o risco de duplicar IDs, o sistema avalia o último índice de forma dinâmica:

    novo_id = transacoes[-1]["id"] + 1 if transacoes else 1

### Prevenção do Erro de Divisão por Zero
Na computação da métrica percentual, o motor valida se existem receitas antes de realizar a divisão, mitigando o erro crítico ZeroDivisionError:

    porcentagem_gasta = (total_despesas / total_receitas * 100) if total_receitas > 0 else 0.0

---

## 4.10 Exemplo de Execução

### Entrada de Dados (Registro de Despesa Crítica)

    Selecione a ação desejada (1-3): 1
    
    --- REGISTRAR NOVA TRANSAÇÃO ---
    Descrição da transação: Upgrade Placa de Vídeo
    Selecione o Tipo:
    1. Receita (Entrada)
    2. Despesa (Saída)
    Escolha (1 ou 2): 2
    Valor da transação: R$ 1300.00
    Categoria: Hardware
    
    Sucesso: Despesa 'Upgrade Placa de Vídeo' registrada com ID 3!

### Saída Gerada pelo Programa na Próxima Iteração

    =============================================
             DASHBOARD FINANCEIRO (BACKEND)   
    =============================================
     Total Receitas: R$ 3000.00
     Total Despesas: R$ 2500.00
     Saldo Atual   : R$ 500.00
     Orçamento Comprometido: 83.3%
    =============================================
     [ALERTA CRÍTICO]: Você comprometeu mais de 80% da sua renda!
    ---------------------------------------------
    1. Registrar Nova Transação
    2. Ver Extrato Detalhado
    3. Encerrar Sistema
    
    Selecione a ação desejada (1-3): 

**Explicação do Resultado:** O motor de backend capturou os dados, estruturou o novo dicionário e adicionou-o ao array na memória. Na iteração subsequente, a função de cálculo somou a nova despesa às anteriores (1200.00 + 1300.00 = 2500.00). O sistema calculou que 2500.00 representa 83.3% de 3000.00 (receitas) e, como este valor viola a barreira da constante LIMITE_ALERTA_PERCENTUAL (80%), o gatilho condicional disparou com sucesso a mensagem de alerta crítico na interface do console.

---

## 4.11 Conclusão
O desenvolvimento deste projeto consolidou os conceitos fundamentais de lógica estruturada através do ecossistema Python. A opção por focar estritamente na construção de um motor de backend via console isolou a lógica de negócio diante de distrações visuais, permitindo focar no rigor técnico de validação de dados e no controle de fluxo por funções modulares. 

A maior dificuldade residiu em garantir que operações inválidas feitas pelo usuário não causassem a quebra prematura do sistema, o que foi solucionado com estruturas defensivas de checagem condicional e captura de exceções. O projeto prova como estruturas simples (listas, dicionários e laços) combinadas com uma boa arquitetura lógica são perfeitamente capazes de resolver problemas gerenciais complexos do mundo real.




 
