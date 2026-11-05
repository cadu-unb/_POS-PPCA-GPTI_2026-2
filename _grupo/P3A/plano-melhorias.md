# P3A — Plano de melhorias (pós-revisão crítica)

**Origem:** revisão crítica completa do relatório P3A (PT e EN), do pôster e das lições, feita sob o perfil de `.agent/pesquisador.md` (pesquisador sênior em gestão de projetos de TIC alinhada ao PMBOK 8, com foco em privacidade e gêmeo digital aplicado à gestão de projetos). Este plano **complementa** o [`plano-abordagem.md`](plano-aborda gem.md); não o substitui.

**Status (05/11/2026):** plano escrito; parte dos itens já foi aplicada, conforme o registro abaixo. **Legenda:** ✅ feito · 🟡 feito em parte (o que falta está na coluna ao lado) · ⬜ a fazer. Quando um item for concluído, marcar com ✅ aqui e na coluna de ID das tabelas da seção 3.

## Registro de execução

| Item | Estado | Feito | Falta |
|---|---|---|---|
| **P3A-01** Declaração de uso de IA | 🟡 | ✅ Texto com a norma **COPE** (*Authorship and AI tools*, 13/02/2023) em `TEX/ferramentas/aviso_ia.py` (fonte única). ✅ **Subseção "Uso de inteligência artificial" nas considerações finais** do relatório (PT e EN; MD, TEX e `style2`), com chave no preâmbulo `\avisofinaltrue`/`\avisofinalfalse`. ✅ Caixa de declaração na capa mantida, **desligada por padrão** (`\avisocapatrue` liga). ✅ Nota de rodapé curta nos 4 pôsteres (MD, TEX e `style2`). ✅ Nas lições, só uma linha pequena no fim do arquivo (MD e TEX). | ⬜ Grupo confirmar a **grafia dos nomes dos modelos** ("ChatGPT Astral 6 Sol e Sonnet 5.5, ambos no modo alto"). ⬜ Confirmar que "o grupo é responsável pelo conteúdo" reflete a prática. ⬜ Conferir o título e a data da página do COPE (não abriu na verificação, erro 403) e acrescentar a data de acesso. ⬜ Se a IA também **redigiu ou traduziu** trechos, ampliar a declaração (opção B do plano da P3A §11.2). ⬜ Decidir se o uso do arquivo do PMBOK 8 (aviso de acesso restrito na p. 2) entra na declaração. |
| **P3A-01b** Integrantes e professores | ✅ | ✅ Quatro integrantes e os dois professores (Dr. João Mello da Silva e Dr. Edison Ishikawa) em capas, pôsteres e lições; lista em `../README.md`. | |
| **P3A-02b** "Entrega na data prevista" | 🟡 | ✅ Trocada por "entrega prevista para 06/11/2026". | ⬜ A frase "nomes, contagens e seções conferidos" não foi alterada: depende de o grupo confirmar a conferência. |
| **P3A-13** Citações do PMBOK 8 | ✅ | ✅ Todas dizem "*Guide* §…" ou "*Standard* §…". | |
| **P3A-14** Resíduos e tradução | 🟡 | ✅ EN: "tailings" virou "rejects" (inclui a Figura 5). | ⬜ Comentários de produção e blocos Mermaid seguem nos MD (o gerador pode depender deles); ⬜ explicar a sigla R3. |
| **P3A-17** Referências | 🟡 | ✅ GDPR com o Jornal Oficial da UE (L 119, 4/5/2016). | ⬜ DTC sem URL/data de consulta; ⬜ ANPD "[s.d.]"; ⬜ ISBN do PMBOK 8; ⬜ Kritzinger e Deng fora do `.bib`. |
| Demais itens (P3A-02a, 02c, 03 a 12, 15, 16, 18 a 20) | ⬜ | | A fazer, conforme a seção 5. |
| Melhorias fora do plano, pedidas pelo grupo | ✅ | ✅ Tabelas 3, 7 e 8 do P3A reorganizadas (PT e EN); ✅ Figuras 4 e 5 do P3A menores e com fonte maior; ✅ versões `style2` de relatórios e pôsteres (P3A e P3D, PT e EN) e `compilar.sh style2`; ✅ limpeza dos temporários em `compilar.sh`; ✅ espaçamento título/autores dos pôsteres; ✅ `_grupo/README.md`; ✅ nota "P1–P8 são uma proposta acadêmica…" dos pôsteres **comentada** (TEX original, `style2` e MD, PT e EN; para reativar, tirar o `%` ou o `<!-- -->` das linhas marcadas `NOTA-COMENTADA`); ✅ Tabelas 7 e 12 e Figura 1 do P3D ajustadas; ✅ ajustes de tabela e figura **portados para o gerador** (`ajustes_tabelas.py`), então a regeneração não os perde. | |

> ✅ **Regeneração do LaTeX sem perda (resolvido em 05/11).** Os ajustes de tabela (P3A: Tabelas 3, 7 e 8; P3D: Tabelas 7 e 12) e a caixa tracejada da Figura 1 do P3D agora vivem no gerador: `ferramentas/ajustes_tabelas.py` roda dentro de `gerar_tex.py`, e a Figura 1 está em `fig1`. Testei regenerar duas vezes e comparar com a versão ajustada à mão: figuras idênticas e, nos relatórios, só diferem as linhas de integrantes e professores da "Nota de natureza" (que vêm do Markdown) e uma diferença de arredondamento de largura. O risco anterior era de gravidade moderada: só afetava quem rodasse `gerar_tex.py`, e se notava na hora.

**Prazo da entrega:** 06/11/2026, 12h (peso 10%). Envio pelo líder.

**Como ler a confiança dos achados.** O texto de cada achado vem da revisão. Conferi por conta própria no PMBOK 8 do repositório apenas os itens marcados com ✔. Os demais são do revisor e devem ser reconferidos ao aplicar a correção.

---

## 1. Diagnóstico em uma tela

O relatório é bem escrito, prudente e honesto quanto ao status de proposta do grupo; as contagens do PMBOK 8 (7 domínios, 40 processos, 7 + 6 processos em Quem) e as citações de LGPD, NIST e DTC que o revisor conferiu estão corretas. É entregável como **proposta acadêmica documental**. Como artigo, ainda é rascunho forte, com quatro fragilidades:

1. **Argumento central da lacuna** ignora a definição ampla de partes interessadas do próprio Guide (P3A-03 ✔).
2. **Integridade:** declaração de IA não aplicada; afirmações de método e de entrega sem sustentação; nomes dos integrantes em branco (P3A-01, 02).
3. **Gêmeo digital** é periférico: só aparece como produto do cenário de reciclagem; o gêmeo da gestão de projetos não é tratado, e a classificação do cenário como "gêmeo" é discutível (P3A-05, 06).
4. **Escopo:** só 1 dos 4 domínios SIPA foi desenvolvido, e as conexões com outras concentrações estão só no nível de domínio (P3A-07, 08).

| # | Dimensão | Nota | Justificativa resumida |
|---|---|---|---|
| 1 | Aderência ao enunciado/plano | 6,5 | Falta mapa de S, I e A; conexões rasas; IA não declarada; capa com marcador de nomes |
| 2 | Fidelidade ao PMBOK 8 | 8,5 | Contagens e nomes corretos; falha na definição de partes interessadas e na numeração Standard/Guide |
| 3 | Argumentação e rigor | 6 | Sobreposição com Riscos/Partes Interessadas; critério de "domínio próprio" não derivado do PMI; busca irreprodutível |
| 4 | Técnica de privacidade | 7 | LGPD/NIST/LINDDUN corretos; faltam encarregado, dado sensível, arts. 12, 14, 37, 50 |
| 5 | Foco do pesquisador (gêmeo digital) | 4,5 | Só o gêmeo do produto; tese do retorno automático é frágil |
| 6 | Estrutura e formato | 7 | Boa ordem; §10 aplica o Final report só em parte; tabelas repetidas |
| 7 | Consistência interna | 7,5 | Paridade PT/EN muito boa; divergências em Fig. 3, "tailings", siglas |
| 8 | Referências e citação | 6,5 | 17 fontes, todas citadas; pouca literatura; pilares fora do `.bib`; GDPR só no método |
| 9 | Linguagem e apresentação | 7,5 | Claro e cauteloso; excesso de tabelas e siglas |
| 10 | Integridade | 4,5 | IA não declarada; §10 afirma o que ainda não ocorreu |

## 2. Critérios de priorização

Cada item recebe uma **classe** e um **esforço** (S ≤ 30 min, M ≤ 2 h, L > 2 h):

- **B — Bloqueante:** risco de contestação de integridade ou de entrega incompleta. Resolver antes do envio.
- **S — Substância:** muda o argumento ou a cobertura. Resolver se houver tempo; senão, assumir o limite no texto (§10 e Lições).
- **A — Acabamento:** forma, consistência, referências. Pode ficar para uma segunda versão.

Regra: **prazo curto não autoriza afirmar o que não é verdade.** Quando não houver tempo de corrigir um achado de substância, o texto deve declarar a limitação, em vez de omiti-la.

## 3. Frentes de ataque

### Frente A — Integridade e conformidade (Bloqueante)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| 🟡 **P3A-01** | Aplicar a declaração de uso de IA nos 6 arquivos (MD e TEX). O grupo escolhe a opção A ou B do `plano-abordagem.md` §11.2 e **confirma a grafia dos nomes dos modelos**. A opção B só inclui "o grupo revisou o conteúdo e responde por ele" se for verdade. | `entregas/MD/*`, `entregas/TEX/*` (relatório, pôster, lições; PT e EN) | S | `grep -rn "AVISO-IA\|declaracaoia"` acha 1 trecho por arquivo; texto idêntico nas duas línguas |
| ✅ **P3A-01b** | Preencher os nomes dos integrantes (`\integrantes` na capa dos originais). Os `style2` já usam os quatro nomes da P2A; conferir se é o mesmo grupo. | `TEX/*_Relatorio_PT.tex`, `*_Report_EN.tex`; `ferramentas/gerar_tex.py` | S | Capa sem colchetes |
| **P3A-02a** | Reescrever as afirmações de método (§1 e §10): informar base, data, strings, filtros, nº de resultados e critério de seleção dos 6 estudos; ou reduzir a frase ao que realmente foi feito. Preencher as 7 condições da sessão em `_wos/tentativa3/registro-pesquisa.md` (hoje "a preencher"). | `MD` §1 e §10; `_wos/tentativa3/registro-pesquisa.md` | M | Um leitor consegue reproduzir a busca; ou a frase diz só "leitura dirigida de 6 estudos" |
| 🟡 **P3A-02b** | Corrigir §10: "entrega na data prevista" e "nomes, contagens e seções conferidos" afirmam o que ainda não ocorreu. Trocar por "prevista" e **só manter "conferidos" depois de o grupo conferir** (o `plano-abordagem.md` §10 lista isso como pendência). | `MD` §10 | S | Nenhuma frase no passado sobre algo ainda não feito |
| **P3A-02c** | Reportar o esforço da equipe ou declarar "não medido" (o Final report pede custo e variações; hoje o texto diz que o esforço não é informado). | `MD` §10 | S | Item de custo do Final report com resposta explícita |

### Frente B — Argumento central (Substância)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| **P3A-03** ✔ | **Reconhecer a definição ampla de partes interessadas.** O Guide inclui "all the people impacted by—or who feel they may be impacted by—the project" (PMBOK, linha 5581) e a Figura 2-31 lista comunidades locais, órgãos reguladores, usuários finais. Reposicionar a lacuna: o que falta não é reconhecer que o titular é uma parte interessada, e sim **os objetos de gestão que o tratamento de dados cria** (inventário, finalidade, hipótese legal, direitos, destino). Corrigir §2.1 e a frase de §2.1 que diz que a gestão de partes interessadas "identifica pessoas relevantes ao projeto". Corrigir também o argumento equivalente no `plano-abordagem.md` §3 (que chama o titular de "usuário final/outras partes interessadas"). | `MD` §1.1, §2.1; Lições §5; `plano-abordagem.md` §3 | M | O texto cita a definição do Guide e a lacuna é reformulada sem contradizê-la |
| **P3A-04** | **Acrescentar "Alternativas consideradas":** (i) camada de adaptação (*tailoring*) de privacidade nos domínios existentes; (ii) extensão de Partes Interessadas e Riscos; (iii) domínio próprio. Explicar por que (iii) e admitir que é **escolha de modelagem** (a concentração Quem é imposta pelo curso). Citar que o Guide diz que seus processos são "illustrative but not comprehensive" (PMBOK, linha 3662 ✔), o que sustenta que o PMI admite extensões. Admitir a sobreposição P1–P8 × processos existentes (a Lição 5 já diz que a contribuição está nas inclusões do §7.1). Justificar o critério "objeto de gestão identificável" mostrando que os 7 domínios atuais o satisfazem, ou assumir que é critério do grupo. | `MD` §2 ou §3 (nova subseção); Lições §5 | M | Existe subseção que compara as 3 alternativas e justifica a escolha |
| **P3A-04b** | Fortalecer o que é mais convincente: a tabela de **inclusões nos 13 processos existentes (§7.1)**. Considerar levá-la para antes da tabela dos oito processos, ou citá-la na tese. | `MD` §7.1, §1 | S | Tese menciona o §7.1 como contribuição principal |

### Frente C — Gêmeo digital (Substância)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| **P3A-05** ✔ | **Tratar o gêmeo da gestão de projetos.** O artigo só trata o gêmeo do **produto** (cenário de reciclagem). Acrescentar um parágrafo ou quadro curto em §4.5 e §8 com os dois níveis: gêmeo do produto × gêmeo do projeto (dados da equipe, produtividade, comunicações, desempenho, partes interessadas). Registrar que o **PMBOK 8 não menciona "digital twin"** (0 ocorrências ✔; o guia cobre IA em gestão no apêndice X3). Apontar a equipe do projeto como titular (Recursos e Governança) e deixar o aprofundamento para a P3C ou para pesquisa futura. | `MD` §4.5, §8; Lições | M | O texto distingue os dois gêmeos e diz explicitamente que o PMBOK 8 não os trata |
| **P3A-06** | **Corrigir a classificação do cenário.** O texto diz que o fluxo de indicadores por rota é "retorno automático do tipo gêmeo". Na Fig. 5 esse retorno vai para o aplicativo do morador, não atua automaticamente sobre o objeto físico; em Kritzinger o gêmeo exige fluxo automático de controle sobre o objeto. Reclassificar (sombra digital, ou gêmeo só se houver atuação automática) e **justificar a extensão** do conceito se mantido. Marcar como **hipótese** a tese "o retorno automático é onde a privacidade mais exige decisão" (Lição 6). Redesenhar a Fig. 5 para mostrar **titulares e fluxos de dados pessoais**, hoje ausentes (só Mobilização → Reciclagem → Destinação). | `MD` §4.5, §8; `TEX/ferramentas/gerar_tex.py` (`fig5`); Lições §6 | M | Classificação coerente com Kritzinger; Fig. 5 mostra titulares |

### Frente D — Cobertura do enunciado e da P3C (Substância)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| **P3A-07** ✔ | **Reescrever §7.2 no nível de processo.** A Tabela 2-1 coloca *Initiate Project or Phase*, *Manage Project Execution* e *Close Project or Phase* em **Governança** (seção 2.1.6 ✔). P1 (termo de abertura) e P8 (encerramento) dependem de Governança, mas §7.1 e §7.2 não mencionam esses processos e §7.2 diz que não propõe alterações nas outras concentrações. Listar interfaces por processo (ex.: *Initiate Project or Phase*, *Define Scope*, *Develop Schedule*, *Develop Budget*, *Acquire Resources*), com direção da dependência e ID, em formato reaproveitável pela P3C. | `MD` §7.2 | M | Tabela §7.2 com processo, direção e motivo; P1 e P8 ligados a Governança |
| **P3A-08** | **Decidir 1 × 4 domínios** com o professor (ponto 1 do `plano-abordagem.md` §2, ainda sem resposta). Se a resposta for "4", acrescentar uma **tabela-mapa de S, I e A** (domínio, concentração, áreas de foco principais, princípios mais ligados), em 1 a 2 páginas, como o plano previa (seção 9). Em qualquer caso, escrever em §1 qual foi a decisão. | `MD` §1 e nova seção; Lições §5 | S (decisão) a M (tabela) | Decisão registrada no texto; se "4", tabela-mapa existe |

### Frente E — Rigor técnico de privacidade e literatura (Substância)

| ID | Ação | Onde | Esforço | Pronto quando |
|---|---|---|---|---|
| **P3A-10** | **Fechar lacunas da LGPD.** Acrescentar ao §4.1: **encarregado** (art. 41; art. 5º, VIII), citado nos processos mas não definido nem atribuído; **dado pessoal sensível** (art. 5º, II; art. 11), usado no Perfil C mas ausente do §4.1. Citar o **art. 12** (anonimização, "meios técnicos razoáveis") no Perfil A. Mencionar **art. 14** (dados de crianças) e **art. 9º** (transparência) no cenário do aplicativo do morador. Considerar arts. 37, 46–50 como fundamento de P6/P7. Padronizar "hipótese legal" × "base legal". **GDPR** [16] aparece só no método: incluir ao menos um parágrafo comparando LGPD, GDPR e FIPPs (base do guia SIPA). | `MD` §1, §4.1, §4.3 | M | Encarregado e dado sensível no §4.1; art. 12 no Perfil A; parágrafo comparativo |
| **P3A-09** | **Calibrar o uso da literatura.** Os 6 estudos vêm de contextos diferentes (IoDT, nuvem com blockchain, casa inteligente, cidade inteligente, saúde, direito UE); nenhum trata reciclagem, cooperativas ou gestão de projetos. Trocar "os estudos convergem" e "prática recorrente/recomendada na literatura [5]" por formulações que reflitam o que cada fonte diz ("em [5]"). Registrar que Jørgensen e Ma [9] só foi conferido pela ficha-resumo, sem texto integral. Registrar a **lacuna** de literatura sobre privacidade em gestão de projetos e gêmeos digitais em gestão de projetos. | `MD` §2.3, §4.2.1; fichas em `_wos/` | M | Nenhuma generalização apoiada em uma só fonte |
| **P3A-09b** | Rever a coluna "Fundamento" (P3/P6/P8 mistura norma, guia e estudo): separar **fundamento normativo** (LGPD, NIST) de **evidência da literatura**. | `MD` §4.2.1 | S | Duas colunas ou marcação distinta |

### Frente F — Forma, consistência e formato (Acabamento)

| ID | Ação | Onde | Esforço |
|---|---|---|---|
| **P3A-11** | Fig. 3 não é um tetraedro (são 4 caixas com setas para uma elipse): renomear para "quatro dimensões" ou desenhar de fato. Resolver **colisão de siglas**: "P" = Privacidade, Processo (F/S/**P**/C) e prefixo P1–P8; "DM" = Desenvolvimento e manutenção (§3.4) e Mobilização Digital (Fig. 5). Citar a origem de PISO e F/S/P/C (material do curso) ou removê-los. | `MD` §4.4; `gerar_tex.py` (`fig3`) | S |
| **P3A-12** | §10 (Final report): dizer **quais dos 8 itens se aplicam e quais não** (o plano §9 pedia isso). Trocar o critério circular de escopo ("seções 3 a 7 produzidas") por critério externo (ex.: revisão cruzada PT/EN feita). Explicar que o *Final report* é saída de *Close Project or Phase*. | `MD` §10 | S |
| ✅ **P3A-13** | Citações do PMBOK ambíguas: "[13, §2.5.2]" não diz se é Guide ou Standard (no Standard, §2.5.2 é "Sponsor, Customer, or Product Owner"). Usar sempre "[13, Guide §…]" ou "[13, Standard §…]". | `MD` PT e EN | S |
| 🟡 **P3A-14** | Limpar resíduos de produção nos MD (comentários "Projeto da Figura", código Mermaid, menção a "projeção em Mermaid" na legenda da Fig. 3, enquanto a versão final é TikZ). EN: "rejeitos" virou "tailings" (termo de mineração); usar "rejects" ou "residual waste". Explicar a sigla R3. | `MD` PT e EN; pôster PT | S |
| **P3A-15** | Lições aprendidas: acrescentar 3 a 4 frases sobre as inconsistências do enunciado (ponto 1 em aberto; "PMBOK6" no título da atividade), o prazo curto e o uso de IA, como o plano §6 pedia. Marcar a Lição 6 como hipótese. | `Licoes_PT.md`, `Lessons_EN.md` | S |

**Item em comum com a P3D (revisão do artigo irmão).** O texto da P3A também atribui as quatro concentrações ao trabalho ("organização adotada neste trabalho"), mas elas vêm do enunciado da disciplina. Trocar por "agrupamento adotado na disciplina (GPTI/PPCA); não é classificação do PMI", como em [`../P3D/plano-melhorias.md`](../P3D/plano-melhorias.md) (P3D-02), e usar as siglas CO/BI/ME/WH. Esforço: S. Decisão D6 do plano da P3D.

### Frente G — Pôster, referências e extras (Acabamento)

| ID | Ação | Esforço |
|---|---|---|
| **P3A-16** | Pôster: incluir as duas matrizes resumidas (áreas de foco e princípios), como o plano §6 pedia; a Fig. 1 do pôster liga só Quem → P e não mostra Partes Interessadas e Riscos separados. Referências selecionadas sem [4], [9], [14], [15]. | M |
| 🟡 **P3A-17** | Referências: [6], [7], [8] (DTC) e [16] (GDPR) sem URL nem Jornal Oficial; sugestão: citar o Jornal Oficial da UE (OJ L 119, 4.5.2016) e a data de consulta das páginas do DTC. [1] (ANPD) com "[s.d.]"; [13] sem ISBN. Kritzinger [11] e Deng [4] fora de `_wos/referencias.bib`. | S |
| **P3A-18** | Excesso de tabelas (12 em ~8 mil palavras): conferir se os parágrafos de §5 e §6 acrescentam algo além da tabela; cortar repetição. | M |
| **P3A-19** | Resumo: bloco único de ~230 palavras sem números de resultado; reorganizar em objetivo, método, achado e limite, com os números (13 processos alterados, 8 propostos, 3 perfis). | S |
| **P3A-20** | Conferir se há versão do NIST Privacy Framework posterior à 1.0 (2020) e se há NIST IR 8062 atualizado. | S |

## 4. Decisões que dependem do grupo ou do professor

| # | Decisão | Quem | Efeito |
|---|---|---|---|
| D1 | Opção **A ou B** da declaração de IA; grafia oficial dos nomes dos modelos; a frase "o grupo revisou e responde" é verdadeira? | Grupo | Libera P3A-01 |
| D2 | **1 ou 4 domínios** SIPA no relatório (ponto 1 do plano) | Professor (ou decisão do grupo, assumida no texto) | Define P3A-08 |
| D3 | O grupo **conferiu** nomes, contagens e seções do PMBOK 8? Quem? | Grupo | Libera a frase de verificação em §10 |
| D4 | Nomes dos integrantes e esforço da equipe | Grupo | Libera P3A-01b e P3A-02c |
| D5 | Incluir o **gêmeo do projeto** (P3A-05) como seção nova ou só como parágrafo? | Grupo | Define o tamanho da Frente C |
| D6 | Quem é o líder e quem envia | Grupo | Ponto 5 do plano |

## 5. Ordem de ataque

Considera o prazo de 06/11, 12h, e a regra da seção 2.

**1. Bloqueios (cerca de 2 h):** P3A-01, 01b, 02a, 02b, 02c, D1 a D4.

**2. Núcleo do argumento (cerca de 3 a 4 h):** P3A-03, 04, 04b; depois P3A-06 e 05; depois P3A-07 e 08.

**3. Rigor (cerca de 1,5 h):** P3A-10, 09, 09b.

**4. Acabamento (cerca de 1,5 h):** P3A-11 a 15.

**5. Fechamento:** regenerar os arquivos, compilar, conferir páginas (20 a 30), nomes dos arquivos e envio.

**Se o tempo for curto**, o mínimo que reduz o risco de contestação é: P3A-01, 02, 03 e 04. Os itens de linguagem e figura (P3A-11, 14, 17 a 20) podem ficar para uma segunda versão, com a limitação declarada no §10.

## 6. Como aplicar sem perder trabalho (pipeline)

- **Fonte de conteúdo é o Markdown** (`entregas/MD/`). Mudança de texto entra lá primeiro, em PT e EN.
- O LaTeX original é **gerado** por `TEX/ferramentas/gerar_tex.py`, que reescreve relatório, lições e figuras. Os `*_style2.tex` são gerados dos originais por `gerar_style2.py`.
- ✅ **Regenerar é seguro:** os ajustes de tabela e de figura estão no gerador (`ajustes_tabelas.py`, `fig4`, `fig5`), e o aviso de IA, os integrantes e os professores também (`aviso_ia.py`, `MEMBERS`). Só continua valendo para edições feitas à mão em texto corrido dos `.tex`: essas se perdem; faça-as no Markdown.
- Ordem sugerida: editar MD (PT e EN) → `python ferramentas/gerar_tex.py` → reaplicar/portar ajustes de tabela → `bash compilar.sh` (figuras, originais e `style2`) → conferir PDFs.
- O pôster e as lições em LaTeX são escritos à mão (pôsteres) ou gerados (lições); ver o `TEX/README.md`.

## 7. Verificação antes do envio (checklist)

- [ ] Declaração de IA presente, uma vez por arquivo, texto idêntico em PT e EN (`grep -rn "AVISO-IA" _grupo/*/entregas`).
- [ ] Nenhum colchete de marcador (`[nomes dos integrantes do grupo]`) na capa.
- [ ] §10 não afirma nada no passado sobre o que ainda não ocorreu.
- [ ] A definição ampla de partes interessadas é citada (P3A-03) e a lacuna foi reformulada.
- [ ] Há tratamento explícito do gêmeo do produto × do projeto, e a frase "o PMBOK 8 não menciona gêmeo digital".
- [ ] P1 e P8 ligados a Governança em §7.2.
- [ ] Decisão sobre 1 × 4 domínios escrita em §1.
- [ ] PT e EN com a mesma estrutura e os mesmos números (contagem de `##`, `###`, figuras e tabelas).
- [ ] Citações do PMBOK dizem "Guide" ou "Standard".
- [ ] Sem resíduos de Mermaid e sem "tailings" no EN.
- [ ] Compilação sem erros; relatório com 20 a 30 páginas; 6 arquivos nomeados conforme o enunciado.
- [ ] Figuras legíveis (Figs. 4 e 5 em tamanho natural) e tabelas dentro das margens.

## 8. O que esta revisão não verificou

- Os links externos (ANPD, Planalto, EUR-Lex); o conteúdo da página da ANPD sobre o RIPD ficou não verificável.
- O texto integral de Jørgensen e Ma (só há ficha-resumo no repositório).
- A frase exata de Shaikh sobre "lacunas na implementação formal de práticas conformes ao GDPR e HIPAA".
- A existência de "criptografia de dados" na tabela de capacidades do DTC (o resumo do curso não a traz).
- Número de páginas dos PDFs compilados.
- As resoluções da ANPD citadas como sugestão (números e vigência não conferidos).
- Os padrões complementares sugeridos (ISO/IEC 27701, 29134, 29100, 31700) são **sugestões não verificadas**.

## 9. Riscos deste plano

| Risco | Resposta |
|---|---|
| Fazer tudo e estourar o prazo | Seguir a ordem da seção 5; assumir limitações no §10 e nas Lições em vez de omiti-las |
| Reescrever o argumento (P3A-03 e 04) e quebrar a coerência com tabelas e figuras | Rever Fig. 1, tabelas 1 e 8 e o pôster depois de P3A-03 e 04 |
| Regenerar o LaTeX e perder os ajustes de tabela | Seção 6 |
| Revisão feita por agente: erro de leitura de fonte | Reconferir cada achado marcado sem ✔ na fonte antes de alterar o texto |

---

*Aguardando instruções para aplicar.*
