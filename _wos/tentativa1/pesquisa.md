## Proposto

Certo. Primeiro medimos **reciclagem de resíduos sólidos**; depois cruzamos com gêmeos digitais e IoT. Privacidade fica para o próximo tetraedro.

Uso Função, Estrutura, Processo e Contexto como **lentes para organizar e avaliar resultados**, não como quatro termos obrigatórios unidos por `AND`: isso poderia eliminar estudos relevantes. Na abordagem de Gharajedaghi, função trata dos resultados, estrutura dos componentes e relações, processo das atividades, e contexto do ambiente do sistema. [Gharajedaghi, *Systems Thinking*](https://www.sciencedirect.com/book/9780123859150/systems-thinking)

| Lente | Neste primeiro tetraedro |
|---|---|
| Função | Reciclar, recuperar materiais, valorizar resíduos |
| Estrutura | Instalações, equipamentos, redes e sistemas de informação |
| Processo | Coleta, triagem, separação, processamento, monitoramento |
| Contexto | Tipos de resíduos sólidos e condições em que a reciclagem ocorre |

**Primeira rodada na busca avançada da WoS:** execute estes quatro blocos separadamente.

**1 — Contexto**
```text
TS=("solid waste*" OR "municipal waste*" OR "urban waste*" OR "post-consumer waste*" OR "electronic waste*" OR "e-waste")
```

**2 — Função**
```text
TS=(recycl* OR "material recover*" OR "resource recover*" OR valoriz* OR valoris*)
```

**3 — Gêmeos digitais**
```text
TS=("digital twin*")
```

**4 — IoT**
```text
TS=("internet of things" OR IoT)
```

No **Histórico de buscas**, combine os conjuntos e anote três contagens: `1 AND 2`, `1 AND 2 AND 3` e `1 AND 2 AND 4`. A WoS permite combinar conjuntos com `AND` e `OR`. [Ajuda oficial da busca avançada](https://webofscience.zendesk.com/hc/en-us/articles/20130361503249-Advanced-Search-Query-Builder)

Mantenha mesma coleção e mesmo intervalo de anos nas três contagens. Envie os números e qual coleção usou. Com isso ajustamos amplitude; depois examinamos amostra de títulos e resumos para medir pertinência e coesão.

## Resultados

### Apenas

- **1 — Contexto**
R: 112,123

- **2 — Função**
R: 426,477

- **3 — Gêmeos digitais**
R: 37,376

- **4 — IoT**
R: 199,760 

### 2 a 2

- 1 and 2
R: 26,188

- 1 and 3
R: 76 

- 1 and 4
R: 590

- 2 and 3
R: 396

- 2 and 4
R: 1,064

- 3 and 4
R: 4,632

### 3 a 3

- 1 AND 2 AND 3
R: 35

- 1 AND 2 AND 4
R: 181

- 2 AND 3 AND 4
R: 56


# Novo

Seja 5:

```text
TS=(WEEE OR "construction and demolition waste*" OR "demolition waste*" OR "end-of-life product*" OR "spent batter*" OR "plastic waste*" OR "metal scrap*")
```