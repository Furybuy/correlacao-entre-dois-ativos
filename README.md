## ⚠️ Disclaimer

> **ATENÇÃO:** O conteúdo deste repositório, bem como os códigos, análises e simulações gerados por ele, possuem caráter **estritamente educativo e informativo**. 
>
> * **Não constitui recomendação:** Nada aqui apresentado deve ser interpretado como recomendação de compra, venda, manutenção ou indicação de investimento para qualquer ativo financeiro (ações, FIIs, Fiagros, ETFs, etc.).
> * **Riscos de Mercado:** O mercado financeiro envolve riscos significativos de perda de capital. Desempenhos passados não são garantia de retornos futuros.
> * **Responsabilidade:** O autor não se responsabiliza por quaisquer decisões financeiras, lucros ou prejuízos decorrentes do uso das informações ou códigos contidos neste projeto. Antes de investir, faça sua própria análise ou consulte um profissional certificado pela CVM.

---

# 📊 Otimização de Portfólio e Fronteira Eficiente: SNAG11 vs. KNCA11

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Data Science](https://img.shields.io/badge/data-science-green.svg)
![Finance](https://img.shields.io/badge/finance-analytics-gold.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

Este projeto realiza uma análise quantitativa de ativos do mercado financeiro brasileiro utilizando dados reais do *Yahoo Finance*. O script automatiza o download do histórico de preços dos Fiagros **SNAG11** (Suno) e **KNCA11** (Kinea), calcula seus retornos diários, mede a correlação estatística entre eles e simula a **Fronteira Eficiente** de Markowitz para identificar a combinação ideal de risco e retorno.

> **📈 Insight Chave do Projeto:** A análise revela que o coeficiente de correlação entre o SNAG11 e o KNCA11 é de apenas **$\rho \approx 0.05$**. Isso indica uma quase completa **independência linear** (descorrelação), tornando este par de ativos uma excelente oportunidade para estratégias de diversificação dentro do setor de crédito privado do agronegócio.

---

## 📌 Sumário
- [Funcionalidades do Script](#-funcionalidades-do-script)
- [Fundamentação Matemática](#-fundamentação-matemática)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)

---

## 🚀 Funcionalidades do Script

1. **Extração Automática:** Download de dados históricos diretamente da API do `yfinance`.
2. **Engenharia de Recursos:** Cálculo da taxa de retorno diária através da variação percentual (`pct_change`) dos preços de fechamento.
3. **Análise Estatística:** * Cálculo da média dos retornos ($\mu$) e da volatilidade/desvio padrão ($\sigma$).
   * Cálculo do **Coeficiente de Correlação de Pearson** ($\rho$) com teste de hipótese ($p\text{-value}$).
4. **Cálculo de Risco de Carteira:** Simulação matemática do risco de um portfólio ponderado (ex: 70% SNAG11 e 30% KNCA11).
5. **Fronteira Eficiente:** Varredura algorítmica de 100 combinações possíveis de pesos (0% a 100%) para plotagem da curva de otimização de ativos.

---

## 📐 Fundamentação Matemática

O risco (volatilidade) de uma carteira composta por dois ativos é calculado utilizando a fórmula da variância de portfólios:

$$\sigma_{carteira} = \sqrt{w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2w_A w_B \rho_{AB} \sigma_A \sigma_B}$$

Onde:
* $w_A, w_B$: Pesos alocados em cada ativo ($w_A + w_B = 1$).
* $\sigma_A, \sigma_B$: Desvio padrão (volatilidade) dos retornos dos ativos $A$ e $B$.
* $\rho_{AB}$: Coeficiente de correlação de Pearson entre os retornos dos dois ativos.

---

## 🛠 Tecnologias Utilizadas

* **[yfinance](https://pypi.org/project/yfinance/):** Coleta de dados históricos de ativos financeiros.
* **[NumPy](https://numpy.org/):** Álgebra linear, manipulação de matrizes e vetores numéricos.
* **[Matplotlib](https://matplotlib.org/):** Geração de gráficos, customização de eixos duplos (`twinx`) e subplots.
* **[SciPy](https://scipy.org/):** Módulo estatístico avançado (`stats.pearsonr`) para cálculo da correlação e significância.

---

## 🔍 Análise dos Resultados e Comportamento dos Gráficos

Embora o **SNAG11** (Fiagro da Suno) e o **KNCA11** (Fiagro da Kinea) pertençam à mesma categoria de ativos — ambos são **Fiagros** focados em **CRAs (Certificados de Recebíveis do Agronegócio)** —, a análise quantitativa do script revela um comportamento dinâmico que quebra o senso comum de que *"ativos da mesma classe andam sempre juntos"*.

Abaixo estão os pontos-chave observados nas duas janelas gráficas geradas pelo código:

### 1. Descolamento de Preços e Retornos Diários (Janela 1)
* **Gráfico de Preços (Superior):** Ao plotar os preços de fechamento utilizando eixos $Y$ independentes (`twinx`), fica evidente que o comportamento de curto e médio prazo dos fundos é frequentemente descolado. Em vários momentos do histórico (2025–2026), enquanto um ativo apresenta viés de alta ou lateralização, o outro pode apresentar correções.
* **Gráfico de Retornos (Inferior):** O gráfico de retornos diários mostra que os "choques" de volatilidade (os dias de maiores altas ou quedas) não acontecem simultaneamente para ambos os fundos. As oscilações diárias parecem independentes, o que estatisticamente se traduz no **baixo Coeficiente de Correlação de Pearson ($\rho$ \approx 0.05$)** calculado pelo código.

### 2. Por que a correlação é baixa se ambos são Fiagros de CRA?
Mesmo operando no mesmo setor (Agronegócio) e sob a mesma estrutura jurídica (CRA), a baixa correlação entre o SNAG11 e o KNCA11 é explicada por fatores fundamentais da gestão de cada portfólio:
* **Indexadores Diferentes:** O mercado de CRAs se divide fortemente entre títulos atrelados ao **CDI** e títulos atrelados ao **IPCA** (inflação). Se um fundo possui maior exposição ao CDI e o outro à inflação, seus retornos vão divergir conforme a dança da taxa Selic e dos índices de preços.
* **Perfil de Crédito (*High Yield* vs. *High Grade*):** O risco das empresas tomadoras de crédito (as devedoras dos CRAs) varia drasticamente entre os fundos. A Kinea (KNCA) e a Suno (SNAG) possuem teses de crédito, pulverização de carteira e prazos médios (*duration*) completamente distintos.
* **Liquidez e Fluxo de Captação:** Momentos de emissões de novas cotas (subscrições) afetam o preço de tela de cada fundo de forma individualizada.

### 3. A Fronteira Eficiente e o Efeito da Diversificação (Janela 2)
O segundo gráfico gerado pelo script (Risco x Retorno) ilustra perfeitamente o benefício prático dessa baixa correlação através da **Teoria Moderna do Portfólio**:

* **A Curva Parabólica:** Como a correlação entre SNAG11 e KNCA11 é baixa (distante de $+1.0$), a linha que une os dois ativos na Fronteira Eficiente não é uma reta, mas sim uma **curva convexa**.
* **O Portfólio de Mínima Variância (PMV):** Essa curvatura prova matematicamente que existe uma combinação de pesos (ex: a simulação de 70% e 30% do código) onde o **risco final da carteira é menor do que o risco de investir em um único fundo sozinho**. 

> **💡 Conclusão da Análise:**
> Este estudo gráfico e estatístico comprova que a diversificação eficiente não é feita apenas mudando de classe de ativo (ex: sair de Fiagros e ir para Ações). É perfeitamente possível encontrar **descorrelação benéfica dentro da mesma classe de ativos**, permitindo ao investidor pulverizar o risco de crédito privado no agronegócio sem necessariamente abrir mão de previsibilidade de retorno.

