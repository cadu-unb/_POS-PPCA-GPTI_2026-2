# Roteiro de apresentação — pôster P2B

**Duração sugerida:** cerca de 8 minutos e 15 segundos de fala, seguidos de perguntas.  
**Percurso no pôster:** título → 01 → 02 → 03 → 04 e fluxo de dados → 05.  
**Mensagem central:** lidos em conjunto, os três projetos descrevem uma cadeia de gêmeos digitais; por isso, a privacidade precisa ser tratada nas passagens entre os componentes, e não apenas dentro de cada um.

O texto entre aspas é uma sugestão de fala. As indicações entre colchetes são gestos ou lembretes ao apresentador.

## 0:00–0:45 — Abertura e problema

**[Aponte para o título e percorra com a mão os três componentes, da esquerda para a direita.]**

> “Este trabalho consolida três projetos sobre o Sistema de Resíduos Sólidos do Distrito Federal: o Mobilizador Digital, a reciclagem em cooperativas e a destinação final em aterro. Cada grupo descreveu seu próprio gêmeo digital. Nossa pergunta foi: o que aparece quando observamos os três como partes de uma mesma cadeia, especialmente do ponto de vista da privacidade? O resultado principal é que o dado pessoal não fica preso ao componente em que surge. Ele pode reaparecer no retorno de informações por rota, na coordenação entre gêmeos e até em mídias descartadas.”

## 0:45–1:55 — 01. A consolidação em números

**[Mostre os cinco números grandes; depois, a linha das buscas.]**

> “A síntese reúne três componentes e examina cada um em quatro dimensões: Função, Estrutura, Processo e Contexto, tanto no mundo físico quanto no digital. Usamos duas tabelas do Digital Twin Consortium como vocabulário de projeto. A CPT organiza 61 capacidades em seis categorias e responde **o que** o gêmeo precisa ter. A AIACPT organiza 45 capacidades em seis áreas e ajuda a explicar **como** os agentes atuam. O pôster mapeia quatro tipos de agentes para cada um dos três gêmeos, totalizando doze posições; no aterro, esses agentes são uma proposta, não uma implementação.”

> “As buscas dos grupos tiveram protocolos distintos: no Mobilizador, 148 registros levaram a quatro artigos selecionados; na Reciclagem, a busca-base teve 59.765 registros e 14 trabalhos com as quatro dimensões; no Aterro, 296 registros levaram a 109 triados. Esses números mostram a base usada por cada grupo. Como as buscas diferem, não devemos comparar os totais como se fossem uma mesma amostra.”

## 1:55–2:55 — 02. A lente F/S/P/C e a passagem de espelho a referência

**[Aponte para o tetraedro e, em seguida, compare as colunas “gêmeo real” e “gêmeo digital”.]**

> “A lente F/S/P/C evita reduzir o gêmeo a um painel. **Função** pergunta para que ele existe; **Estrutura**, do que ele é feito; **Processo**, como opera ao longo do tempo; e **Contexto**, em quais relações territoriais, institucionais e legais atua. No mundo físico temos pessoas, materiais, equipamentos, rotas e contratos. No digital, temos dados, modelos, ontologias, agentes e regras de compartilhamento. O gêmeo nasce como espelho da operação, mas pode se tornar referência para uma decisão futura: observar o estado atual, simular alternativas e justificar o próximo passo.”

> “Essa diferença importa para a privacidade. Informações dispersas no mundo físico podem ser reunidas no digital. A reunião de endereço, horário, peso, imagem ou pontuação pode formar um perfil identificável mesmo quando cada dado, isoladamente, parece pouco sensível.”

## 2:55–5:00 — 03. O papel de cada gêmeo

**[Siga as três colunas DM → R3 → D, sem tentar ler cada linha.]**

> “O **Mobilizador Digital**, ou DM, atua na origem: cidadãos, domicílios e separação de resíduos. Ele prevê e orienta mobilização, coleta e educação. Sua evolução vai do espelho ao gêmeo enriquecido e, por fim, à referência que indica o que fazer primeiro e por quê. O risco de privacidade já aparece no cadastro, na geolocalização, nas fotos e na pontuação por domicílio. O projeto reconhece a necessidade de aplicar a LGPD desde o desenho e de definir a granularidade do painel público.”

> “O **R3**, da reciclagem, acompanha a operação da cooperativa. A esteira, a pesagem e a produção por posto e turno passam a gerar informação para previsão e planejamento. O projeto propõe uma sequência de configurações, avançando de registro para sombra digital, rede e referência. Aqui há salvaguardas mais concretas: métricas por posto em vez de ranking individual, endereço mantido no DM com compartilhamento mínimo, processamento local de imagens e Relatório de Impacto à Proteção de Dados antes da configuração que usa câmera.”

> “O **D**, do aterro, trata da destinação final. Seu ponto específico é que a eliminação de dados também precisa ser verificável: celulares, discos e papéis podem chegar junto com o rejeito. O projeto propõe certificado de sanitização por lote, conforme a NIST SP 800-88, e um caminho do gêmeo do ativo ao gêmeo do projeto e a uma prova de conceito. Na literatura de destinação final analisada pelo grupo, a etapa em que os dados deveriam deixar de existir foi justamente a menos estudada sob a ótica da privacidade.”

## 5:00–5:50 — 04. Como entram os agentes de IA

**[Mostre a tabela de A1 a A4; indique a última coluna, com as regras de privacidade.]**

> “Os quatro tipos de agentes cumprem papéis diferentes. O **A1** conversa e presta atendimento. O **A2** acompanha fluxos, como agenda, pesagem e cadeia de custódia. O **A3** analisa riscos e recomenda ações. O **A4** coordena múltiplos agentes e organizações. A complexidade aumenta, mas a regra de decisão permanece: o agente recomenda e explica; uma pessoa valida decisões e divergências.”

> “Para o A4, a salvaguarda proposta é aprendizado federado sem troca de dados brutos, acompanhado de acordos de dados. Isso precisa valer para a rede inteira, não apenas para a cooperativa, porque a coordenação cruza informações de diferentes gêmeos e instituições.”

## 5:50–6:50 — O fluxo de informação pessoal

**[Siga as quatro caixas abaixo da tabela: Cidadão → DM; R3 → DM; A4; Rejeito → Aterro.]**

> “Este é o achado que só a leitura conjunta revela. Primeiro, cadastro, perfil, localização, foto e pontuação ficam associados ao domicílio no DM. Depois, o R3 devolve ao DM a qualidade da separação por rota. Quanto menor a rota, maior a possibilidade de aproximar essa informação de um domicílio específico. Em paralelo, os agentes A4 coordenam a rede e criam outro ponto de cruzamento entre organizações. Por fim, o rejeito pode carregar mídias e documentos com dados ainda legíveis até o aterro.”

> “Cada passagem pede uma medida própria: granularidade mínima testada contra reidentificação no retorno por rota; compartilhamento mínimo e acordos para a rede de agentes; e comprovação de sanitização para as mídias. O risco nasce também nas conexões entre gêmeos.”

## 6:50–8:15 — 05. Conclusões e próximos passos

**[Aponte para as quatro conclusões; finalize olhando para o público.]**

> “Concluímos quatro coisas. Primeiro, gêmeo real e digital têm composições diferentes: o digital reúne dados e modelos e pode apoiar decisões futuras. Segundo, as tabelas de capacidades se complementam: uma especifica o que o gêmeo tem; a outra, como seus agentes agem. Terceiro, o avanço de cada gêmeo precisa de estados futuros e critérios de passagem explícitos, incluindo privacidade: granularidade no DM, RIPD no R3 e sanitização verificável no aterro. Quarto, a privacidade é uma propriedade da cadeia inteira.”

> “O trabalho é uma **síntese de projetos e propostas**, sem validação de campo dos três gêmeos. Os próximos passos são unificar o registro dos tratamentos, firmar acordos de dados entre gêmeos, definir a granularidade do retorno por rota, testar o protocolo de sanitização e validar as soluções com cooperativa, serviço público e aterro piloto.”

> “Em uma frase: separados, os projetos descrevem três gêmeos; juntos, mostram onde a privacidade precisa ser governada ao longo de todo o percurso do dado. Obrigado. Fico à disposição para perguntas.”

## Respostas curtas para perguntas prováveis

**O que significa ‘da réplica à referência’?**  
Significa usar o gêmeo para comparar cenários e justificar um próximo estado desejado, além de representar a operação atual. A decisão final continua sob responsabilidade humana.

**Os doze agentes já estão funcionando?**  
Não. O pôster mapeia quatro tipos em cada um dos três gêmeos. Os agentes do aterro são propostos nesta fase, e nenhum dos três gêmeos foi validado em campo no estudo consolidado.

**Por que os números das buscas não podem ser comparados diretamente?**  
Os grupos usaram bases, períodos, termos e etapas de triagem diferentes. Os números documentam a origem das evidências de cada projeto; não medem, em escala comum, a maturidade dos componentes.

**Qual é a principal contribuição da consolidação?**  
Tornar visíveis dois pontos de passagem que um projeto isolado não cobre: o retorno da qualidade por rota do R3 para o DM e a coordenação entre gêmeos por agentes A4. A síntese também mostra a lacuna de verificação da eliminação de dados na destinação final.

## Fontes de preparação

- Pôster: [`out/P2B_Poster_A1_PT.pdf`](out/P2B_Poster_A1_PT.pdf).
- Texto de apoio: [`out/Projeto_GPTI_Entrega_P2B_PT-BR_EN.pdf`](out/Projeto_GPTI_Entrega_P2B_PT-BR_EN.pdf), especialmente método, discussão, limitações e conclusões.
