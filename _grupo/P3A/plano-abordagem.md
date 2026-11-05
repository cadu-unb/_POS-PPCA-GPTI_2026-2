# P3A — Plano de abordagem

Grupo SIPA de **Privacidade** (nosso grupo: Privacidade 2; componente SRS: Reciclagem 1). Este plano diz o que será feito, em que ordem e com que fontes. Nada aqui foi executado ainda.

**Prazo registrado no Aprender3: 06/11/2026, às 12h. Peso: 10%.** O envio é do líder, com a identificação do grupo nos nomes dos arquivos.

## 1. O que a atividade pede

O `enunciado.md` (nosso entendimento) e o `resumo-aprender3.md` (extraído do Aprender3) concordam no essencial:

1. **Incluir no PMBOK 8 os 4 domínios de desempenho SIPA** e distribuí-los nas 4 concentrações de domínios existentes:

   | Novo domínio | Concentração | Domínios existentes da concentração |
   | --- | --- | --- |
   | A — Análise de negócios com decisões ajustadas a riscos | CO — Consolidação | Governança |
   | S — Sustentabilidade | BI — Nascimento | Escopo e Cronograma |
   | I — Inovação | ME — Meios | Finanças e Recursos |
   | **P — Privacidade** | **WH — Quem** | **Partes Interessadas e Riscos** |

2. **(a) Aderência às 5 áreas de foco** do PMBOK 8: Iniciação (IN), Planejamento (PL), Execução (EX), Monitoramento e Controle (MC), Encerramento (CL).
3. **(b) Aderência aos 6 princípios** do PMBOK 8: 1AHV (visão holística), 2FOV (foco em valor), 3QPD (qualidade nos processos e entregas), 4BAL (líder responsável), 5SPA (sustentabilidade em todas as áreas), 6BEC (cultura empoderada).
4. **Justificar a necessidade da extensão**, em quatro aspectos: caracterização da necessidade; critérios para desenvolvimento; publicação e formato; desenvolvimento e manutenção.
5. **Listar à parte** as conexões do novo domínio com processos de *outras* concentrações, para a consolidação geral (P3C).
6. **Formato dos arquivos** (em português e em inglês): pôster de 1 página por idioma; relatório técnico-científico de 20 a 30 páginas por idioma, no formato do Relatório Final do PMBOK 8 (saída *Final report* de *Close Project or Phase*, seção 2.1.6.9 do Guia); relato de lições aprendidas de 1 a 2 páginas por idioma. Total: 6 arquivos.

## 2. Pontos ainda em aberto

Esses pontos mudam o tamanho do trabalho. Precisam de decisão do grupo, ou de resposta do professor, antes de fechar o texto.

| # | Ponto | Origem | Decisão proposta |
| --- | --- | --- | --- |
| 1 | **Quantos domínios cada grupo trata?** A ementa diz 4 por grupo SIPA, com 4 conjuntos de sistemas. Um parágrafo de entrega diz "um novo domínio" e atribui a elaboração ao "grupo de componente SRS". | `resumo-aprender3.md`, seção P3A | Aprofundar **Privacidade → Quem**. Tratar S, I e A em nível de mapa (linha na tabela de aderência), sem desenvolver processos. Perguntar ao professor, e ajustar se a resposta for "só um". |
| 2 | **Princípios agora ou só na P3C?** O enunciado pede aderência aos 6 princípios, mas o texto de apoio diz que a inclusão dos princípios será abordada na P3C. | idem | Fazer a análise **(b)** por privacidade, de forma curta. Entregar a análise dos outros três domínios só como mapa. |
| 3 | O título da atividade fala em "PMBOK6". | idem | **Decidido:** tratar como **PMBOK 8**, inclusive para o formato do relatório. |
| 4 | O PDF do PMBOK 8 lista **7 domínios existentes** (Governança, Escopo, Cronograma, Finanças, Partes Interessadas, Recursos, Riscos). A concentração CO tem só Governança. | PMBOK 8 | Seguir o agrupamento do curso (tabela acima) e citar o PMBOK 8 como fonte dos 7 domínios. |
| 5 | Quem é o líder e quem envia? | enunciado | Definir antes da revisão final. |

## 3. Abordagem geral

A tese do documento: **o PMBOK 8 trata privacidade de forma implícita (risco, comunicação e partes interessadas), e isso não basta para projetos que tratam dados pessoais.** A extensão cria o domínio **Privacidade** na concentração **Quem**, colado a Partes Interessadas e Riscos, por duas razões:

- O titular dos dados é uma parte interessada que o PMBOK 8 trata como "usuário final" ou "outras partes interessadas". Falta nome, direito e canal próprios para ele.
- O risco de privacidade não se reduz ao risco de cibersegurança. O NIST Privacy Framework diz que gerir risco cibernético contribui para gerir risco de privacidade, mas não basta: há riscos de privacidade que surgem do próprio processamento de dados, sem incidente de segurança (`documentos/SIPA/02.2.03IpgSipaPrivacidade2026S.md`, slides 5–6).

Etapas, em ordem:

1. **Diagnóstico (o que o PMBOK 8 já diz).** Ler os domínios Partes Interessadas (7 processos) e Riscos (6 processos) e anotar onde cada um toca dados pessoais. Registrar também o que falta: não há "dado pessoal", "titular", "base legal" nem "encarregado" no vocabulário dos processos.
2. **Justificativa da extensão.** Redigir os quatro aspectos pedidos (necessidade, critérios, publicação e formato, desenvolvimento e manutenção), usando a base legal e normativa do guia SIPA: LGPD (inclusive a Emenda Constitucional 115/2022 e a ANPD), GDPR, FIPPs, NIST Privacy Framework e NIST IR 8062 (engenharia de privacidade).
3. **Desenho do domínio Privacidade.** Propor os processos do novo domínio (seção 5), cada um com nome, propósito, entradas, saídas e a área de foco em que ocorre.
4. **Matriz de aderência (a).** Domínio × 5 áreas de foco, com uma frase de justificativa por célula.
5. **Matriz de aderência (b).** Domínio × 6 princípios, com uma frase por célula.
6. **Conexões para a P3C.** Lista separada de ligações com processos de Governança, Escopo, Cronograma, Finanças e Recursos.
7. **Ligação com o nosso sistema.** Mostrar com o percurso do dado pessoal na reciclagem por cooperativas (P2B, Figura 1) que a lacuna é concreta. É o exemplo que sustenta a justificativa.
8. **Montagem dos 6 arquivos**, em português primeiro e inglês depois.

## 4. Matrizes de aderência (modelos a preencher)

### (a) Privacidade × áreas de foco

| Área de foco | Atividade de privacidade esperada | Processo do novo domínio |
| --- | --- | --- |
| IN — Iniciação | *(a preencher)* | |
| PL — Planejamento | *(a preencher)* | |
| EX — Execução | *(a preencher)* | |
| MC — Monitoramento e controle | *(a preencher)* | |
| CL — Encerramento | *(a preencher)* | |

O PMBOK 8 mapeia cada processo existente a uma área de foco (Tabela 2-1 do Guia). O novo domínio deve seguir o mesmo padrão. Exemplo da própria estrutura de Riscos: planejar, identificar e analisar ficam em Planejamento; implementar respostas em Execução; monitorar em Monitoramento e controle.

### (b) Privacidade × princípios

| Princípio | Como a privacidade o sustenta |
| --- | --- |
| 1AHV — Visão holística | *(a preencher)* |
| 2FOV — Foco em valor | *(a preencher)* |
| 3QPD — Qualidade nos processos e entregas | *(a preencher)* |
| 4BAL — Líder responsável | *(a preencher)* |
| 5SPA — Sustentabilidade em todas as áreas | *(a preencher)* |
| 6BEC — Cultura empoderada | *(a preencher)* |

Pontos de apoio no PMBOK 8 (seção 3.2): a visão holística é sustentada por todos os domínios; qualidade e foco em valor ligam-se sobretudo a Governança, Escopo, Riscos, Cronograma, Finanças e Partes Interessadas; "líder responsável" cruza Governança, Partes Interessadas e Riscos. Esses três últimos são os vizinhos do novo domínio, o que reforça a escolha da concentração Quem.

## 5. Proposta de processos do domínio Privacidade (hipótese de trabalho)

Os nomes abaixo são **rascunho do grupo**, ainda sem validação. Seguem o padrão verbo + objeto do PMBOK 8.

| Processo proposto | Área de foco | Liga-se a (existente) |
| --- | --- | --- |
| Identificar dados pessoais e titulares | IN / PL | Identify Stakeholders; Identify Risks |
| Planejar a gestão de privacidade (bases legais, finalidades, papéis) | PL | Plan Risk Management; Plan Communications Management |
| Avaliar o impacto à privacidade (relatório de impacto) | PL | Perform Risk Analysis |
| Planejar as respostas e os controles de privacidade | PL | Plan Risk Responses |
| Gerir o engajamento e os direitos dos titulares (consentimento, acesso, correção, eliminação) | EX | Manage Stakeholder Engagement; Manage Communications |
| Implementar controles e tratar incidentes de dados pessoais | EX | Implement Risk Responses |
| Monitorar a conformidade e os riscos de privacidade | MC | Monitor Risks; Monitor Stakeholder Engagement |
| Encerrar o tratamento (retenção, eliminação, descarte) | CL | Close Project or Phase |

Estrutura de referência para cada processo, como nas demais seções do Guia: entradas, ferramentas e técnicas, saídas, considerações de adaptação (*tailoring*), interações com outros domínios e verificação de resultados.

## 6. Estrutura do relatório (20 a 30 páginas por idioma)

Modelo: Relatório Final do PMBOK 8 (*Final report*, seção 2.1.6.9 do Guia). Ele resume o desempenho do projeto em oito itens: descrição resumida; objetivos de escopo e evidência de conclusão; objetivos de qualidade; objetivos de custo; validação do produto final; cronograma e realização de benefícios; atendimento das necessidades de negócio; riscos e questões encontrados e como foram tratados. A distribuição abaixo é aproximada e deve ser conferida contra esses itens:

| Seção | Páginas |
| --- | --- |
| Resumo e palavras-chave | 1 |
| 1. Introdução e objetivo | 2 |
| 2. Metodologia (fontes, critério de proposição) | 2 |
| 3. Diagnóstico: privacidade no PMBOK 8 | 4–5 |
| 4. Justificativa da extensão (4 aspectos) | 4–5 |
| 5. Domínio Privacidade na concentração Quem (processos) | 6–8 |
| 6. Aderência às 5 áreas de foco | 2 |
| 7. Aderência aos 6 princípios | 2 |
| 8. Conexões com outras concentrações (insumo da P3C) | 1–2 |
| 9. Domínios S, I e A em nível de mapa (se confirmado o ponto 1) | 1–2 |
| 10. Conclusão e trabalhos futuros | 1 |
| Referências e apêndices | 1–2 |

**Pôster (1 página por idioma):** tese em uma frase, figura do novo domínio dentro da concentração Quem, as duas matrizes resumidas e a lista de processos.

**Lições aprendidas (1 a 2 páginas por idioma):** o que funcionou, o que não funcionou, o que faríamos diferente, e as inconsistências do enunciado (seção 2).

## 7. Fontes disponíveis no repositório

| Uso | Arquivo |
| --- | --- |
| Domínios, processos, princípios, áreas de foco | `documentos/PMBOK8/PMBOK® Guide 8th Edition (Project Management Institute).md` (domínio Partes Interessadas: seção 2.5; Riscos: 2.7; princípios: capítulo 3 do Standard; Tabela 2-1) |
| Base legal e normativa de privacidade | `documentos/SIPA/02.2.03IpgSipaPrivacidade2026S.md` |
| Contexto SIPA e tabelas do DTC | `documentos/SRS/GptiResumo2026S.md` |
| Domínios irmãos (para o mapa de S e I) | `documentos/SIPA/02.2.01IpgSipaSustentabilidade2026S.md`, `02.2.02IpgSipaInovação2026S.md` |
| Literatura (privacidade e gêmeos digitais) | `_wos/Manual 3/artigos/md/` (16 artigos) e `_wos/referencias.bib` |
| Exemplo concreto | `_grupo/P2B/` (Figura 1, percurso do dado pessoal) |
| Formato do relatório | PMBOK 8, seção 2.1.6.9 (*Close Project or Phase*, saída *Final report*), no mesmo arquivo do Guia |

Os PDFs do PMBOK 8 e do guia SIPA têm texto extraído por conversão. Para citar página ou trecho, conferir no PDF original.

## 8. Cronograma

Hoje é 04/11 e o prazo é 06/11, às 12h. Restam cerca de dois dias, então a prioridade é o núcleo (privacidade → Quem) em português; o restante vem depois.

| Quando | Entrega |
| --- | --- |
| 04/11, noite | Resolver os pontos 1 e 5 (mensagem ao professor; definir o líder). Fechar o diagnóstico (etapa 1) e a lista de processos (seção 5). |
| 05/11, manhã | Justificativa (etapa 2) e matrizes (a) e (b). |
| 05/11, tarde | Conexões para a P3C. Relatório em português completo. Pôster em português. |
| 05/11, noite | Lições aprendidas. Versões em inglês. Revisão cruzada. |
| 06/11, até 10h | Conferência final dos 6 arquivos e dos nomes. Envio pelo líder, com folga até as 12h. |

## 9. Riscos

| Risco | Efeito | Resposta |
| --- | --- | --- |
| Escopo ambíguo (ponto 1) | Retrabalho, ou entrega a menos | Decisão proposta na seção 2; perguntar cedo. |
| Prazo curto para 6 arquivos | Versão em inglês fraca ou ausente | Escrever em português já em estrutura que traduz bem; usar a lista de pendências. |
| Processos propostos sem apoio na literatura | Texto parecer opinião | Citar o guia SIPA (LGPD, GDPR, FIPPs, NIST) e os artigos do Manual 3 em cada processo. |
| Formato do relatório (*Final report* do PMBOK 8) pensado para fechar projeto, não para propor extensão | Itens do modelo sem correspondência no nosso texto | Seguir a estrutura da seção 6 e dizer no relatório quais itens do modelo se aplicam e quais não. |
| Citações do PMBOK 8 imprecisas | Perda de credibilidade | Conferir página no PDF antes de citar. |
