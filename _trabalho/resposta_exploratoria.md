# Resposta exploratória: Reciclagem (R3) × Privacidade (P)

Base: GptiResumo, PaeeAle (artigo das duas disciplinas) e SIPA-Privacidade. O GptiResumo tem recall de cerca de 95% na conversão, e o slide 7 (entregas) saiu embaralhado. Conferir nos PDFs antes de citar prazos e códigos.

## 1. O que a orientação pede

- A célula do grupo é R3-Reciclagem × P-Privacidade.
- No GptiResumo o código correspondente aparece como `GPH.SIPA/RSRSR3-CC` (real) e `GPH.SIPA/DSRSR3-CC` (digital). Na linha de Privacidade seria algo como `…R3.P`. Isto é inferência.
- Entregáveis do slide 7:
  - P2A/P2B: descrição do sistema real (RSQ) e do digital (DSQ);
  - P3A–D: guia de projetos estendido com SIPA;
  - P4A/P4B: pré-projeto, com necessidades e lacunas, business case, plano de benefícios, TAP e plano do projeto.
- Não está claro qual desses é a entrega atual do grupo. Ver seção 6.

## 2. Insumos que os .md já dão

**Reciclagem (R3)**
- Função: C1 coleta seletiva, T1 triagem, T2 transformação, C2 comercialização.
- Descrição F/S/P/C: função α, estrutura β, processo γ, contexto δ.
- Atores: cooperativas de catadores, instalações de reciclagem (IRR), veículos, redes de comercialização.
- Base legal: Lei 12.305/2010 e Portaria MMA 1.250/2024.

**Privacidade (P)**
- LGPD Art. 2: sete fundamentos, agrupados em quatro concentrações:
  - α1 Consent;
  - α2 Interaction OutIn;
  - α3 Interaction InOut;
  - α4 Supervision.
- Conceitos úteis: dado pessoal e sensível, titular, controlador, operador, encarregado, ANPD (Art. 55-J) e NIST Privacy Framework (risco de privacidade não é só de cibersegurança).

**Digital twin**
- O DTC define três tipos: digital, shadow (fluxo de dados em um sentido) e twin (fluxo nos dois sentidos).
- A CPT tem 61 capacidades em 6 grupos. Para privacidade, as relevantes são TW.PR, TW.SC, TW.EX, MG.DG, MG.EL e DS.AI.

## 3. O que é realista em 20–40 h

| Entregável | O que é | Horas |
|---|---|---|
| A. Descrição R3 (RSQ → DSQ) | F/S/P/C do real e do digital para C1/T1/T2/C2. Classifica a maturidade pretendida (digital, shadow ou twin) por função, com justificativa. | 6–8 |
| B. Mapa de dados pessoais de R3 | Inventário por função: titulares (cooperados, catadores autônomos, cidadãos na coleta, compradores), dados (cadastro, produção individual, saúde e segurança, pagamentos, localização de veículos, imagens de esteira) e fluxo entre atores. | 6–8 |
| C. Análise de privacidade × α1–α4 | Para cada função, aplica as quatro concentrações. Inclui base legal provável (Art. 7/11), controlador e operador, riscos NIST e mitigações, e um RIPD simplificado. | 8–10 |
| D. Mapeamento às capacidades DTC | Quais capacidades da CPT a DSQ-R3 precisa para atender B e C (TW.*, MG.DG, DS.*), em tabela de rastreabilidade: necessidade, risco, capacidade. | 3–4 |
| E. Contrato de intercomunicação | Ver seção 4. | 3–4 |
| F. Síntese e apresentação | Texto final e slides. | 4–5 |

Total: cerca de 30–38 h.

**Opcional, se sobrar tempo (8–10 h):** protótipo mínimo com dados sintéticos, só para ilustrar. Por exemplo, um esquema de dados com pseudonimização e um painel de produção por cooperativa. É a parte que mais gasta tempo e menos pesa como argumento. Só vale se a disciplina cobrar algo demonstrável.

**Fora de alcance (citar como trabalho futuro):**
- construir um twin real;
- integrar sensores;
- coletar dados de campo com as cooperativas;
- parecer jurídico formal;
- preencher o tetraedro bibliométrico inteiro.

## 4. Intercomunicação entre grupos

A estrutura parece uma grade de 4 componentes (DM, R2, R3, DS) por 4 lentes SIPA (S, I, P, A). Isto é leitura a partir de "4 grupos com Reciclagem e 4 com Privacidade". O grupo estaria em R3 × P. Dois eixos de troca:

- **Mesmo componente, outras lentes (R3 × S, I, A):**
  - Usar a mesma descrição RSQ/DSQ de R3 (entregável A), para as quatro lentes falarem do mesmo sistema.
  - Pedir deles o que impacta privacidade: dados que a inovação ou a análise de negócios quer coletar.
- **Mesma lente, outros componentes (DM, R2, DS × P):**
  - Padronizar o formato do inventário de dados e da análise α1–α4, para consolidar a privacidade do sistema inteiro.
  - Pontos de contato prováveis entre componentes: mobilizador digital, reúso e aterro, com o fluxo de resíduo e de dados da reciclagem.

**Contrato mínimo a propor (cerca de 2 páginas):**
1. Glossário comum: RSQ, DSQ, F/S/P/C, nomes dos atores.
2. Template de inventário de dados pessoais, com as mesmas colunas para todos.
3. Template α1–α4, igual para todos.
4. Lista de interfaces R3 ↔ outros componentes (quem envia, que dado, com que frequência).
5. Ponto de sincronização: um canal e um dia fixo.

## 5. Sugestão de sequência

1. Enviar o contrato (E) aos outros grupos cedo, porque ele destrava a consistência entre todos.
2. A → B → C → D, nessa ordem, pois cada um alimenta o seguinte.
3. F ao final, com folga para ajustar à resposta dos outros grupos.

## 6. Perguntas abertas

1. Qual é o entregável e o prazo? P2A/P2B, P3 ou P4?
2. "Reciclagem 1" e "Privacidade 2" são o mesmo grupo em duas classificações, ou 1 e 2 são números de grupo diferentes?
3. Existe formato exigido, como template do guia GPH.SIPA ou número de páginas?
4. Os outros grupos de Privacidade já definiram template, ou o grupo pode propor o seu?
