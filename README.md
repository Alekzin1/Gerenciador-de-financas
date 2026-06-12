# Gerenciador-de-financas

# CoreFin: Motor de Processamento e Gerenciamento de Fluxo de Caixa

## 4.1 Identificação
* **Nome completo do aluno:** Alexandre de Souza Mariano
* **Curso:** Análise e desenvolvimento de sistemas
* **Disciplina:** Programação de Computadores
* **Data:** 12/06/2026

---

## 4.2 Título do Projeto
**CoreFin - Sistema Avançado de Finanças Pessoais via Terminal (Backend Engine)**

---

## 4.3 Descrição do Problema
O controle financeiro pessoal exige o cálculo constante de variáveis dinâmicas que se alteram a cada nova entrada (receita) ou saída (despesa) de capital. Pequenos descompassos e a falta de visualização em tempo real do impacto dos gastos sobre a renda total geram endividamento e descontrole orçamentário. 

O problema consiste em construir um motor de backend robusto, baseado em console, capaz de centralizar dados de transações, calcular instantaneamente proporções de gastos em relação à renda total e disparar gatilhos visuais de segurança (alertas de criticidade) assim que limites prudenciais forem violados, sem depender de uma camada de interface gráfica complexa.

---

## 4.4 Objetivo do Programa
O sistema se propõe a atuar como um núcleo de processamento financeiro estruturado. Ele captura inputs do usuário através da linha de comando, armazena as informações temporariamente em coleções de objetos indexados em memória, computa agregados aritméticos de saldo e porcentagem de comprometimento e emite relatórios tabulares de extrato e alertas automáticos de risco orçamentário.

---

## 4.5 Descrição Geral da Solução
A solução foi inteiramente desenvolvida utilizando a linguagem **Python 3**, adotando o paradigma de **programação estruturada modular**. 

Os dados de cada transação são encapsulados em dicionários (`dict`) contendo chaves para propriedades específicas, os quais são armazenados sequencialmente em uma lista dinâmica principal (`list`), simulando o comportamento de uma tabela de banco de dados relacional. 

Toda a lógica de atualização baseia-se em funções puras de computação de dados. O fluxo principal é mantido por uma estrutura de repetição contínua (`while`) que atua como o roteador de comandos do sistema, avaliando as escolhas por meio de condicionais encadeadas.

---

## 4.6 Estrutura do Programa
O código-fonte está organizado de forma modular através das seguintes funções:

* `calcular_totais()`: Varre a coleção de dados em memória utilizando laços de repetição, filtra os registros por tipo e retorna os agregados financeiros calculados (Receitas, Despesas, Saldo e Percentual Comprometido).
* `exibir_resumo()`: Atua como a camada de saída do dashboard no terminal. Exibe os resultados matemáticos processados e executa condicionais de segurança para exibição de alertas de risco.
* `registrar_transacao()`: Camada de input de dados do sistema. Realiza a captura de strings e floats, aplica regras de validação contra campos nulos, trata erros de conversão de tipos e faz o append do novo registro na lista.
* `extrato_detalhado()`: Itera sobre os registros armazenados e gera uma saída formatada em colunas alinhadas, simulando uma tabela pura de banco de dados.
* `ejecutar_sistema()`: Orquestrador central e ponto de entrada da aplicação, contendo o loop principal (`Main Loop`) e o tratamento de rotas do menu.

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
O bloco abaixo demonstra o tratamento robusto do backend para evitar falhas de execução (*runtime errors*) caso o usuário insira letras no campo numérico:
```python
try:
    valor = float(input("Valor da transação: R$ "))
    if valor <= 0:
        print("Erro: O valor deve ser maior que zero.")
        return
except ValueError:
    print("Erro: Valor numérico inválido. Use pontos para centavos (Ex: 150.50).")
    return


 
