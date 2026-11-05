# P3D — Plano de melhorias (pós-revisão crítica)

**Origem:** revisão crítica completa do relatório P3D (PT e EN), do pôster e das lições, feita sob o perfil de `.agent/pesquisador.md` (pesquisador sênior em gestão de projetos de TIC alinhada ao PMBOK 8, com foco em privacidade e gêmeo digital aplicado à gestão de projetos). Este plano **complementa** o [`plano-abordagem.md`](plano-abordagem.md); não o substitui. O plano irmão da P3A está em [`../P3A/plano-melhorias.md`](../P3A/plano-melhorias.md).

**Status (05/11/2026):** plano escrito; parte dos itens já foi aplicada, conforme o registro abaixo. **Legenda:** ✅ feito · 🟡 feito em parte (o que falta está na coluna ao lado) · ⬜ a fazer. Quando um item for concluído, marcar com ✅ aqui e na coluna de ID das tabelas da seção 3.

## Registro de execução

| Item | Estado | Feito | Falta |
|---|---|---|---|
| **P3D-01** Declaração de uso de IA | 🟡 | ✅ Texto com a norma **COPE** (*Authorship and AI tools*, 13/02/2023) em `TEX/ferramentas/aviso_ia.py` (fonte única). ✅ **Subseção "Uso de inteligência artificial" nas considerações finais** do relatório (PT e EN; MD, TEX e `style2`), com chave no preâmbulo `\avisofinaltrue`/`\avisofinalfalse`. ✅ Caixa de declaração na capa mantida, **desligada por padrão** (`\avisocapatrue` liga). ✅ Nota de rodapé curta nos 4 pôsteres (MD, TEX e `style2`). ✅ Nas lições, só uma linha pequena no fim do arquivo (MD e TEX). | ⬜ Grupo confirmar a **grafia dos nomes dos modelos** ("ChatGPT Astral 6 Sol e Sonnet 5.5, ambos no modo alto"). ⬜ Confirmar que "o grupo é responsável pelo conteúdo" reflete a prática. ⬜ Conferir o título e a data da página do COPE (não abriu na verificação, erro 403) e acrescentar a data de acesso. ⬜ Se a IA também **redigiu ou traduziu** trechos, ampliar a declaração (opção B do plano da P3A §11.2). ⬜ Decidir se o uso do arquivo do PMBOK 8 (aviso de acesso restrito na p. 2) entra na declaração. |
| **P3D-01b** Integrantes e professores | ✅ | ✅ Quatro integrantes e os dois professores (Dr. João Mello da Silva e Dr. Edison Ishikawa) em capas, pôsteres e lições; lista em `../README.md`. | |
| **P3D-12** Relatório final (§13) | 🟡 | ✅ "Entrega na data prevista" trocada por "entrega prevista para 06/11/2026". | ⬜ "Conferência documental feita" e "nomes e contagens conferidos" dependem de o grupo ter conferido no PDF; ⬜ trocar o risco (iv); ⬜ tornar concreta a linha de necessidades de negócio. |
| **P3D-10** Coluna de princípios | 🟡 | ✅ Coluna renomeada para "Princípio oficial (código usado na disciplina)". | ⬜ Linha por princípio com o que o Standard destaca; ⬜ citar a refinação de 12 para 6 princípios. |
| **P3D-15** Rótulo "2.x.3" | ✅ | ✅ Agora "2.x.3, exceto Governança, que é a 2.1.7". | |
| **P3D-19** Referências | 🟡 | ✅ GDPR com o Jornal Oficial da UE (L 119, 4/5/2016); ✅ **Reed et al.**: iniciais corrigidas para "REED, A.; ANGOLIA, M.; BAHAM, C.; IGAH, R." conforme o BibTeX do grupo (páginas 402–427, v. 54, DOI 10.17705/1CAIS.05415 já estavam certos). | ⬜ [6] Silvius-Zuchi sem páginas/DOI; ⬜ [4] sem ISBN; ⬜ "SOX ou GDPR" cita só o GDPR; ⬜ numeração PT × EN. |
| **P3D-05** Fontes externas | 🟡 | ✅ Existência e metadados de Reed et al. confirmados pelo grupo. | ⬜ Conferir no artigo as frases atribuídas a ele (ex.: "400 profissionais") e as demais fontes. |
| Demais itens (P3D-02 a 04, 06 a 09, 11, 13, 14, 16 a 18, 20, 21) | ⬜ | | A fazer, conforme a seção 5. |
| Melhorias fora do plano, pedidas pelo grupo | ✅ | ✅ Tabelas 3, 7 e 8 do P3A reorganizadas (PT e EN); ✅ Figuras 4 e 5 do P3A menores e com fonte maior; ✅ versões `style2` de relatórios e pôsteres (P3A e P3D, PT e EN) e `compilar.sh style2`; ✅ limpeza dos temporários em `compilar.sh`; ✅ espaçamento título/autores dos pôsteres; ✅ `_grupo/README.md`; ✅ Tabelas 7 e 12 e Figura 1 do P3D ajustadas; ✅ ajustes de tabela e figura **portados para o gerador** (`ajustes_tabelas.py`), então a regeneração não os perde. | |

> ✅ **Regeneração do LaTeX sem perda (resolvido em 05/11).** Os ajustes de tabela (P3A: Tabelas 3, 7 e 8; P3D: Tabelas 7 e 12) e a caixa tracejada da Figura 1 do P3D agora vivem no gerador: `ferramentas/ajustes_tabelas.py` roda dentro de `gerar_tex.py`, e a Figura 1 está em `fig1`. Testei regenerar duas vezes e comparar com a versão ajustada à mão: figuras idênticas e, nos relatórios, só diferem as linhas de integrantes e professores da "Nota de natureza" (que vêm do Markdown) e uma diferença de arredondamento de largura. O risco anterior era de gravidade moderada: só afetava quem rodasse `gerar_tex.py`, e se notava na hora.

**Prazo da entrega:** 06/11/2026, 12h (peso 10%). Envio pelo líder.

**Como ler a confiança dos achados.** O texto de cada achado vem da revisão. Conferi por conta própria no PMBOK 8 do repositório apenas os itens marcados com ✔. Os demais são do revisor e devem ser reconferidos ao aplicar a correção.

---

## 1. Diagnóstico em uma tela

O núcleo factual é sólido: o revisor não achou erro nas 40 linhas do inventário, nas contagens por domínio e por área de foco, nos números de seção, nas 42 conexões entre princípios e domínios, nem nos passos e operações do *tailoring*. A paridade PT/EN é boa. A maior virtude do texto é separar o que é do PMI do que é interpretação do grupo.

O problema central: **o relatório descreve o PMBOK 8 em vez de guiar a decisão de adaptá-lo**, e é isso que o enunciado pede com ênfase ("sob medida"). Fragilidades principais:

1. **Tailoring descritivo.** O texto resume o capítulo 3 e descarta a parte decisória que o PMI fornece: a *direção* de cada fator (inovação alta → adaptativa; regulamentação → preditiva etc.) e a regra de governança por abordagem (P3D-04 ✔).
2. **Foco do pesquisador** (gêmeo digital aplicado à gestão de projetos): a frase de que o PMBOK 8 não menciona gêmeo digital está correta (0 ocorrências ✔), mas é apoiada em uma generalização frágil sobre "construção civil" e confunde o gêmeo do **produto** com o da **gestão** (P3D-03).
3. **Autoria e integridade:** as quatro concentrações são atribuídas ao "trabalho", mas vêm do enunciado; declaração de IA não aplicada; §13 afirma o que ainda não ocorreu; quatro fontes externas não verificáveis no repositório.
4. **Formato:** 28 páginas sem um quadro-resumo de uma página, embora o pôster prometa "PMBOK 8 em uma página".

| # | Dimensão | Nota | Justificativa resumida |
|---|---|---|---|
| 1 | Aderência ao enunciado/plano | 7,0 | Cobre tudo; desequilíbrio nos princípios; falta consulta rápida; sem siglas CO/BI/ME/WH |
| 2 | Fidelidade ao PMBOK 8 | 8,5 | Números e nomes verificados; omissões relevantes e paráfrase quase integral da Tabela 3-1 |
| 3 | Argumentação e rigor | 6,5 | Separa oficial de interpretativo; matriz 6×7 e "42 conexões" informam pouco |
| 4 | Tailoring / gestão de projetos | 5,5 | Fiel, porém descritivo; faltam direção dos fatores e diagnóstico aplicável |
| 5 | Foco do pesquisador (DT + privacidade) | 4,5 | Não faz a ponte; confunde DT-produto com DT-da-gestão |
| 6 | Estrutura e formato | 6,5 | Redundância (40 linhas + mapa + tabela de áreas + concentrações); sem quadro-resumo |
| 7 | Consistência interna e entre artigos | 8,0 | Sem contradição numérica PT/EN/pôster/lições/P3A |
| 8 | Referências e citação | 5,5 | PMBOK bem citado; 4 de 5 fontes externas não verificáveis |
| 9 | Linguagem e apresentação | 7,5 | Claro e sóbrio; tabelas longas; parênteses em PT na versão EN |
| 10 | Integridade | 5,0 | IA não declarada; §13 e método a confirmar; autoria em branco |

## 2. Critérios de priorização

Cada item recebe uma **classe** e um **esforço** (S ≤ 30 min, M ≤ 2 h, L > 2 h):

- **B — Bloqueante:** risco de contestação de integridade ou de entrega incompleta. Resolver antes do envio.
- **S — Substância:** muda a utilidade ou a cobertura. Resolver se houver tempo; senão, assumir o limite no texto (§13 e Lições).
- **A — Acabamento:** forma, consistência, referências. Pode ficar para uma segunda versão.

Regra: **prazo curto não autoriza afirmar o que não é verdade.** Sem tempo para corrigir um achado de substância, o texto declara a limitação.

## 3. Frentes de ataque

### Frente A — Integridade e conformidade (Bloqueante)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| 🟡 **P3D-01** | Aplicar a declaração de uso de IA nos 6 arquivos (MD e TEX; relatório, pôster e lições, PT e EN), conforme o plano da P3A §11. O grupo escolhe a opção A ou B e **confirma a grafia dos nomes dos modelos**. A frase "o grupo revisou o conteúdo e é responsável por ele" só entra se for verdade. **Registrar também o uso do arquivo do PMBOK 8**: a página 2 do PDF traz aviso de acesso restrito e de que o texto não deve ser usado para treinar IA (PMBOK, linha 41); o uso foi de leitura e análise, e convém dizê-lo. | `entregas/MD/*`, `entregas/TEX/*` | S | `grep -rn "AVISO-IA"` acha 1 trecho por arquivo; mesmo texto em PT e EN |
| ✅ **P3D-01b** | Preencher os integrantes (`\integrantes` na capa dos originais). Os `style2` já usam os quatro nomes da P2A; conferir se é o mesmo grupo. | `TEX/*_Relatorio_PT.tex`, `*_Report_EN.tex` | S | Capa sem colchetes |
| 🟡 **P3D-12** | Corrigir o Relatório final (§13): "entrega na data prevista" antecipa um fato (a entrega é 06/11, 12h); "conferência documental feita" e "nomes e contagens conferidos" exigem registro de que a conferência foi feita **no PDF**, não só no Markdown convertido (a do revisor foi no Markdown). Reescrever como "prevista" e só manter "conferidos" depois de o grupo conferir. Trocar o risco (iv) "ausência de gêmeo digital no PMBOK 8" (não é risco encontrado por uma síntese) por um risco real: texto convertido embaralhado. Tornar concreto o item "necessidades de negócio atendidas", hoje vago e sem demandante. | `MD` §13 | S | Nenhuma frase no passado sobre o que ainda não ocorreu |

### Frente B — Autoria e fidelidade ao PMI (Substância)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| **P3D-02** | **Reatribuir as concentrações.** O texto diz "agrupamento analítico deste trabalho" e "elaboração própria", mas o enunciado define A→Consolidação, S→Nascimento, I→Meios, P→Quem. Trocar por "agrupamento adotado na disciplina (GPTI/PPCA) para ler os domínios; não é classificação do PMI". Reservar "elaboração própria" ao que é do grupo (ex.: a coluna de concentração da tabela de 40 linhas). Aplicar em Resumo, §1 (Fig. 1), §7.1, §10, legenda da Fig. 5, Lições e pôster, PT e EN. **A mesma frase existe na P3A** ("organização adotada neste trabalho"): alinhar as duas. | `MD` PT/EN, pôster, lições; ver também `../P3A/plano-melhorias.md` | S | Nenhuma ocorrência de "deste trabalho" para as concentrações |
| 🟡 **P3D-10** | **Renomear a coluna "Código e princípio oficial"**: os códigos 1AHV, 2FOV, 3QPD, 4BAL, 5SPA e 6BEC não estão no PMBOK 8; vêm do enunciado da P3A. Passar a "Princípio oficial; código usado na disciplina". Acrescentar uma linha por princípio com o que o Standard destaca (*Project Impact*, *Principle in Action*) e citar a refinação de 12 para 6 princípios (prefácio e apêndice X5). | `MD` §4 | S a M | Coluna renomeada; 12→6 mencionado |
| **P3D-18** | Alinhar siglas e nome ao enunciado: CO/BI/ME/WH e "Análise de Negócios com Decisões Ajustadas a Riscos". | `MD`, figuras | S | Siglas presentes e consistentes com a P3A |
| **P3D-14** | **Condensar a Tabela 3-1.** As 8 situações do PMI estão parafraseadas quase uma a uma, embora o relatório diga que não reproduz trechos extensos. Reduzir a 4 a 5 situações ou rotular "adaptado de [4, Tabela 3-1]"; aspas só para termos oficiais. Os 40 nomes de processo são necessários. | `MD` §9.4 | S | Tabela condensada e atribuída |

### Frente C — Tailoring operacional (Substância; o maior ganho de utilidade)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| **P3D-04** ✔ | **Dar direção aos fatores.** A tabela de §5.2 lista só os nomes dos fatores; o PMBOK 8 (§4.3) dá a tendência de cada um, que o texto descartou. Converter em tabela **fator → tendência** (preditiva/adaptativa), com o aviso do PMI de que vários fatores coexistem. Exemplos verificados (§4.3.1 ✔): inovação alta → adaptativa; certeza de requisitos → preditiva; facilidade de mudança baixa → preditiva; regulamentação forte → preditiva; segurança (*safety*) rigorosa → preditiva; feedback frequente → adaptativo. Conferir no texto os demais fatores de projeto e de organização (financiamento incerto, estrutura hierárquica, cultura que aceita incerteza, equipe de 3 a 9 pessoas). | `MD` §5.2 | M | Tabela com direção; aviso de coexistência |
| **P3D-04b** ✔ | **Regra de governança por abordagem** (PMBOK linha 3712 ✔): leve para adaptativos, moderada ou combinada para híbridos, abrangente para grandes portfólios, programas e projetos preditivos. Acrescentar a distinção entre governança estruturada e autogovernança (linhas ~3774–3778, do revisor). | `MD` §7.2 | S | Regra citada em §7.2 |
| **P3D-04c** | Trazer 3 a 4 linhas sobre o que foi omitido: os **níveis de híbrido** (Disciplined Agile, linhas ~2570–2575), o **triângulo invertido** (Fig. 4-3: escopo, prazo e orçamento fixos × variáveis) e a diferença entre **linha de base integrada** preditiva e adaptativa (linhas ~2395–2400). | `MD` §5.1 | S | Três itens presentes |
| **P3D-04d** | **Diagnóstico aplicável.** Tornar o "filtro de adequação" (§9.3, passo 1) um instrumento: critérios de cultura, dinâmica da equipe e fatores do projeto; combinar a Tabela 3-1 com o passo 4 em um fluxo *situação → diagnóstico → operação → processo afetado*. | `MD` §9.3, §9.4 | M | Fluxo único com um exemplo encadeado |
| **P3D-11** | **Trocar os exemplos das cinco operações** por um exemplo encadeado, com **gatilho e critério** ("quando adicionar? quando remover?"). O exemplo "remover *Plan Sourcing Strategy*" ignora que o PMI não trata aquisição como domínio (apêndice X4: "*Procurement is not classified as a separate performance domain*" ✔) e que essa é a única entrada de contratação nos 40 processos. Um dos exemplos pode ser de gêmeo digital **da gestão** (ver P3D-03). | `MD` §9.2 | M | Exemplo encadeado; sem exemplo trivial |
| **P3D-16/17** | Corrigir paráfrases enviesadas: "poucos processos podem deixar decisões críticas sem tratamento" → o PMI diz "*Too few processes can lead to ineffective project management*" (✔, linha 6772); "baixa tolerância a risco" → "*low risk appetite*". Distinguir **segurança** (*safety*, §5.2) de **segurança da informação** (*security*, §11 e §3.4.3.1). | `MD` §5.2, §9, §11 | S | Termos alinhados ao original |

### Frente D — Foco do pesquisador: ponte para gêmeo digital e privacidade (Substância)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| **P3D-03** | **Reformular a frase sobre a literatura de gêmeos digitais.** "A literatura sobre gêmeos digitais em gestão de projetos concentra-se hoje em construção civil" se apoia em uma única revisão (Manzoor et al. [2]), que trata de fatores de implantação de DT como tecnologia em projetos de construção, não de DT aplicado à gestão de projetos; o próprio `_wos/` do grupo mostra literatura de DT em reciclagem, saúde, automotivo e privacidade. Trocar por "nesta síntese não foi localizada literatura de DT aplicado à gestão de projetos fora do contexto de construção (busca por X; fonte Y)" ou retirar a generalização. Manter a frase de que o PMBOK 8 não menciona gêmeo digital (0 ocorrências ✔). **Separar DT-produto de DT-da-gestão** e dizer qual interessa. | `MD` §2, §11, §12, §13 | M | Sem generalização sem busca; os dois níveis distintos |
| **P3D-03b** ✔ | **Caixa de ponte (5 a 8 linhas), rotulada "leitura do grupo".** O PMBOK 8 já abre a porta, sem citar gêmeo digital: a Governança "frequentemente usa tecnologia e ferramentas orientadas a dados, com rastreamento, análise e relatório em tempo real" (linha 3710 ✔); há cenários *what-if* e avaliação de mudanças de linha de base (linha ~1765); a Tabela X3-1 lista usos de IA por domínio (análise preditiva, relatórios automáticos); o Standard §2.5 exige exatidão dos dados e neutralidade das saídas (linha ~1599). O material da disciplina define o gêmeo como representação "sincronizada a frequência e fidelidade específicas" (`documentos/SRS/GptiResumo2026S.md`, slide 4), o que conversa com cadência de entrega e com a pergunta do tailoring (frequência de sincronização do gêmeo ≈ frequência de monitoramento do projeto). Dizer onde um DT da gestão se encaixaria: *Monitor and Control Project Performance*, *Assess and Implement Changes*, *Develop Schedule*, *Perform Risk Analysis*. | `MD` §2 ou §9 | M | Caixa presente e rotulada |
| **P3D-09** ✔ | **Completar a tabela de §11 (privacidade/segurança/IA no PMBOK 8).** Faltam: as "restrições legais" (segurança, proteção de dados, linha 7297 ✔) como fator externo na seção 4 do Guide, e não só no Standard §2.2.1; a sensibilidade e confidencialidade da informação no plano de comunicações (linhas 8479–8481 ✔, e linha ~7191 do revisor); o uso de LLM/IA em partes interessadas (linha ~5843); o Standard §2.5 (alinhar com TI para salvaguardar informação e ameaças cibernéticas, linha ~1599); X3.1/X3.2, Tabela X3-1 e GenAI em riscos (linha ~6687). Trocar "Standard §2.2.1" por "Standard §2.2.1; Guide, seção 4". Apontar que as saídas de comunicação e os registros de partes interessadas manipulam dados de pessoas (ligação com Quem), sem propor processo novo. | `MD` §11 | S | 3 a 4 linhas novas; citação corrigida |

### Frente E — Fontes e referências (Substância)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| 🟡 **P3D-05** | **Verificar as fontes externas.** Noll e Beecham, Reed et al., Silvius-Zuchi e Silvius, Manzoor et al. e a ISO 21502 não estão em `_wos/` nem em `documentos/`; o revisor não pôde conferir "400 profissionais", "cerca de dois terços" nem "seis formas de combinar". Abrir cada fonte, conferir cada frase e **anexar o PDF ou o trecho** ao repositório, citando página. Rebaixar para "leitura do grupo" as inferências: a associação da ISO 21502 à "cadência de entrega"; "o PMBOK 8 combina os dois enfoques [princípios + processos]"; a ligação entre o "filtro de adequação" do PMI e os "critérios de adequação" de Silvius-Zuchi. | `MD` §5.1, §5.2, §9.3, §12; `_wos/` | M | Cada frase com fonte conferida ou rebaixada |
| 🟡 **P3D-19** | Referências: [6] sem páginas nem DOI; [7] (GDPR) sem o ato (OJ L 119, 4.5.2016); [4] sem ISBN; "SOX ou GDPR [7]" cita só o GDPR (nada para SOX). PT e EN têm numeração diferente por ordenação alfabética, e pôster e lições citam por esse número: manter a regra ou fixar a mesma ordem nos dois idiomas. | `MD`, `TEX` | S | Referências completas; numeração coerente |

### Frente F — Estrutura, formato e acabamento (Acabamento)

| ID | Ação | Onde | Esforço |
|---|---|---|---|
| **P3D-06** | **Inserir um quadro-resumo de uma página logo após o Resumo** (6 princípios, 5 áreas, 7 domínios com contagens e passos de tailoring), como o pôster "PMBOK 8 em uma página" promete. Remover a tabela de 5 linhas de §6 (os totais ficam no mapa 7×5); encurtar §13; opcional: levar a tabela dos 40 processos a apêndice e deixar no corpo um resumo por domínio. O plano pede 20 a 30 páginas, mas o enunciado fala em "sumário"; hoje são 28. | `MD`, `TEX` | M |
| **P3D-07** | **Matriz 6×7 e "42 conexões".** As 42 conexões são 6×7 por construção (cada seção §3.x.3 lista os sete domínios): "42 conexões conferidas" não é resultado. Destacar (negrito ou sombra) só as conexões que o §3.2 chama de "mais fortes"; declarar que 5SPA e 6BEC têm texto parcialmente repetido no PMBOK; trocar "42 conexões conferidas" por "toda célula tem texto expresso". Em 3.7.3 há dois parágrafos iniciais além dos sete itens: dizer. | `MD` §8, Fig. 3, §13 | S a M |
| **P3D-08** | **Figura 4** (ciclo de adaptação): a legenda cita "Figura 3-1" do Guide, mas as setas de retorno e a ligação "cinco operações → só o passo 3" não são verificáveis no texto convertido; pelo Guide §3.4.2, o ajuste à organização também usa "adicionar, remover e reconfigurar". Conferir as Figuras 3-1 e 3-3 no **PDF** e marcar na legenda o que é do grupo ("setas tracejadas e ligação das operações: leitura do grupo"). | `MD`, `gerar_tex.py` (fig) | S |
| **P3D-13** | **Cobertura da edição.** Em duas linhas de §2, listar os apêndices X1 (colaboradores), X2 (PMOs), X3 (IA), X4 (aquisição) e X5 (evolução da edição) e dizer o que cada um traz; mencionar a decisão de não ter domínio de aquisição (✔). | `MD` §2 | S |
| ✅ **P3D-15** | §7.2: "considerações de adaptação (2.x.3 do Guide)" seguido de "§§2.1.7, 2.2.3 …": trocar por "2.x.3, exceto Governança (2.1.7)". | `MD` §7.2 | S |
| **P3D-20** | Resíduos e forma: remover os comentários "Desenho futuro" das Figuras 1 a 5 no Markdown (já há TikZ); na versão EN, tirar os parênteses em português da tabela de 40 processos (§7.1); Lições: o item 2 diz que a Tabela 2-1 convertida não indica a área, mas a linha de Governança a traz (reformular: "para os outros seis domínios, a área vem das figuras de visão geral"); incluir nas Lições a dificuldade real (texto convertido embaralhado, conferência no PDF), como o plano pede. | `MD` PT/EN, Lições | S |
| **P3D-21** | **Possível discrepância na própria fonte** (do revisor, **não confirmada por mim**): o texto convertido de §1.1 do Guide parece dizer "eight project performance domains", contra sete no restante. Pode ser artefato da conversão ou erro do PMI. Conferir no PDF; não afeta nenhuma contagem do artigo. | PDF do PMBOK 8 | S |

## 4. Decisões que dependem do grupo ou do professor

| # | Decisão | Quem | Efeito |
|---|---|---|---|
| D1 | Opção **A ou B** da declaração de IA; grafia oficial dos modelos; a frase "o grupo revisou e responde" é verdadeira? Registrar o uso do arquivo do PMBOK 8? | Grupo | Libera P3D-01 |
| D2 | O grupo **conferiu no PDF** nomes, contagens e seções do PMBOK 8? Quem? | Grupo | Libera a frase de verificação em §13 (P3D-12) |
| D3 | Nomes dos integrantes | Grupo | Libera P3D-01b |
| D4 | Quanto da **ponte para gêmeo digital** entra na P3D (caixa de 5 a 8 linhas ou nada), sem desviar do escopo "sumário" | Grupo | Define P3D-03b |
| D5 | **Quadro-resumo e apêndice:** aceitar mexer na estrutura (P3D-06)? | Grupo | Define a Frente F |
| D6 | Reatribuição das concentrações: confirmar com o professor que a origem é a disciplina (P3D-02), e alinhar a P3A | Professor ou grupo | Libera P3D-02 |
| D7 | Quem é o líder e quem envia | Grupo | Ponto do plano |

## 5. Ordem de ataque

Considera o prazo de 06/11, 12h, e a regra da seção 2.

**1. Obrigatório (cerca de 30 min):** P3D-01, 01b, 12; D1 a D3.

**2. Rápidas de ganho alto (cerca de 1 h):** P3D-02, 10, 18, 15, 17, 20.

**3. Conteúdo (cerca de 2 a 3 h):** P3D-04 (com 04b, 04c) e P3D-03 (com 03b). **Se o prazo apertar, faça só a tabela de §5.2 com direção dos fatores e a regra de governança** (P3D-04 e 04b): são as duas edições que mais elevam a utilidade para o tema pedido.

**4. Verificação de fontes (cerca de 1 a 2 h, em paralelo):** P3D-05 e P3D-08, e a checagem no PDF do P3D-21.

**5. Se sobrar tempo:** P3D-06, 07, 09, 11, 13, 14, 19.

**6. Fechamento:** edições em PT e EN com paridade → regenerar o LaTeX → compilar → conferir visualmente as figuras → `grep AVISO-IA` e comparação de números PT/EN antes de enviar.

## 6. Como aplicar sem perder trabalho (pipeline)

- **Fonte de conteúdo é o Markdown** (`entregas/MD/`). Texto novo entra lá primeiro, em PT e EN.
- O LaTeX original é gerado por `TEX/ferramentas/gerar_tex.py`, que reescreve relatório, lições e figuras; os `*_style2.tex` são gerados dos originais por `gerar_style2.py`.
- ✅ **Regenerar é seguro:** os ajustes das Tabelas 7 e 12 e da Figura 1 estão no gerador (`ajustes_tabelas.py`, `fig1`), e o aviso de IA, os integrantes e os professores também (`aviso_ia.py`, `MEMBERS`). Só continua valendo para edições feitas à mão em texto corrido dos `.tex`: essas se perdem; faça-as no Markdown.
- Ordem sugerida: editar MD (PT e EN) → `python ferramentas/gerar_tex.py` → `bash compilar.sh` → conferir PDFs.

## 7. Verificação antes do envio (checklist)

- [ ] Declaração de IA presente, uma vez por arquivo, texto idêntico em PT e EN.
- [ ] Capa sem marcador de nomes.
- [ ] §13 não afirma nada no passado sobre o que ainda não ocorreu; a conferência foi feita no PDF.
- [ ] As concentrações aparecem como "adotadas na disciplina", com CO/BI/ME/WH; a P3A diz o mesmo.
- [ ] Coluna de princípios diz "oficial; código usado na disciplina"; refinação 12→6 citada.
- [ ] Tabela fator → tendência e regra de governança por abordagem presentes.
- [ ] Frase sobre literatura de DT reformulada; DT-produto × DT-da-gestão distinguidos; "o PMBOK 8 não menciona gêmeo digital" mantida.
- [ ] Fontes externas conferidas ou rebaixadas; PDFs/trechos anexados.
- [ ] PT e EN com a mesma estrutura e os mesmos números.
- [ ] Sem comentários "Desenho futuro" no MD e sem parênteses em português no EN.
- [ ] Compilação sem erros; relatório com 20 a 30 páginas; Figura 1 e tabelas dentro das margens.

## 8. O que esta revisão não verificou

- A conferência do PMBOK foi feita no **texto convertido** (com trechos embaralhados); as figuras e a coluna de áreas da Tabela 2-1 ficam sem leitura direta no PDF.
- Noll e Beecham, Reed et al., Silvius-Zuchi e Silvius, Manzoor et al. e a ISO 21502 (fora do repositório).
- A checagem P3D↔P3A foi por busca de termos, não por leitura integral.
- Os números de linha citados pelo revisor para algumas passagens (por exemplo, a de "40 *nonprescriptive processes*", que ele situa na linha 11124, onde o texto atual fala de 79% dos respondentes) devem ser reconferidos ao citar.
- P3D-21 (possível "eight domains" no §1.1 do Guide): não localizei a frase com a busca que tentei.

## 9. Riscos deste plano

| Risco | Resposta |
|---|---|
| Tentar tudo e estourar o prazo | Seguir a ordem da seção 5; assumir limitações em §13 e nas Lições |
| Inserir o quadro-resumo e a tabela de direção sem rever o pôster e a Fig. 3 | Rever pôster, Fig. 3 e lições depois de P3D-04 e P3D-06 |
| Regenerar o LaTeX e perder ajustes de tabela e figura | Seção 6 |
| Ampliar a ponte de gêmeo digital e desviar do escopo "sumário" | Limitar a uma caixa de 5 a 8 linhas, rotulada "leitura do grupo" (D4) |
| Revisão feita por agente: erro de leitura de fonte | Reconferir cada achado sem ✔ na fonte antes de alterar o texto |

---

*Aguardando instruções para aplicar.*
