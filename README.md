# ⚡ Calculadora de Consumo Elétrico Inteligente

> Atividade de Recuperação - Agenda 5 | Desenvolvimento de Sistemas I  
> **Autor:** Murilo Figueiredo Cordesco Domingues

Uma aplicação simples em Python desenvolvida para ajudar usuários a estimarem o consumo mensal de energia elétrica de seus aparelhos domésticos com base na potência e no tempo de uso diário.

---

## 🚀 Funcionalidades

- 🔌 **Entrada Interativa:** Recebe o nome do aparelho, potência em Watts (W) e tempo médio de uso diário em horas.
- 📐 **Cálculo Automático:** Aplica a fórmula padronizada para obter o consumo mensal em kWh.
- 🛡️ **Validação de Entrada:** Tratamento de erros para impedir a inserção de textos ou valores fora da realidade (ex.: mais de 24h por dia).
- 📊 **Saída Formatada:** Apresentação clara dos resultados no terminal.

---

## 🧮 Fórmula Utilizada

$$\text{Consumo Mensal (kWh)} = \frac{\text{Potência (W)} \times \text{Horas/Dia} \times 30}{1000}$$

---

## 💻 Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado no computador.

### Passo a Passo
1. Clone o repositório para a sua máquina:
   ```bash
   git clone [https://github.com/SEU-USUARIO/consumo-energia.git](https://github.com/SEU-USUARIO/consumo-energia.git)
