## Slide 1

Digital Twin Concept Development as a Bridge Between

Computing and Production Engineering: A Two-Course

Integration in Solid Waste Management

João Mello da Silva1, Mateus Halbe Torres1, Marcia Longen Zindel1, Marcelo Carneiro Gonçalves1

1University of Brasilia-UnB, Brazil

Emails: joao.mellos@gmail.com, mateusconsigo@gmail.com, marcialz@unb.br, marcelogoncalves@unb.br

Abstract

This paper proposes a design methodology for cross-level, interdisciplinary course integration at the University of Brasilia

(UnB), Brazil, connecting a graduate course in IT Project Management (GPTI, Applied Computing master’s program) with an

undergraduate Project Management course, Production Systems Project 1 (PSP1), in Production Engineering, through the

shared development of Digital Twin (DT) concepts for Brasilia’s Solid Waste Systems. The methodology builds on prior

experiences at UnB in connecting these courses through project-based interactions, now introducing DT as a structured

socio-technical coupling mechanism that simultaneously forces (i) operational grounding and (ii) disciplined digital project

framing. Using the real-world context of Brasília’s transition from closing an open dump site to recycling centers involving

cooperatives of waste pickers, performing Selective Collection, Triage, Transformation and Commercialization, GPTI

emphasizes DT as a project focus—clarifying scope, stakeholders, governance, risks, data requirements, implementation

roadmap, and success criteria—while deliberately immersing computing students in operational complexity so they must

design within real constraints. Conversely, PSP1 emphasizes the real system—mapping processes, constraints, and

improvement opportunities across triage centers and the supply-chain concept—while requiring production engineering

students to treat DTs as a technology-enabled intervention rather than an external add-on. The courses are coupled via

an active, collaborative supervision model in which IT master students’ mentor undergraduate teams as project leaders

and requirements facilitators, and both cohorts iteratively refine shared artifacts such as system maps, requirement

backlogs, risk registers, and validation criteria through joint problem-framing sessions and structured peer feedback. The

proposed methodology will be applied in the next course cycle and is intended to increase authenticity, student agency, and

systems thinking, yielding both a replicable course-integration approach and a set of contextualized digital twin conceptual

designs grounded in the operational realities and improvement needs of Brasília’s recycling centers.

Keywords: digital twin; project-based learning; active learning; engineering education; project management; solid waste

management; systems thinking.

1 Introduction

Engineering education venues centered on active learning approaches, such as Problem-Based Learning (PBL)

and Flipped Classroom, increasingly emphasize designs that preserve disciplinary depth while producing

authentic, interdisciplinary work and assessable evidence of learning through iterative artifacts and feedback

(Freeman et al., 2014; Gharajedaghi, 2011; Prince, 2004). This becomes particularly relevant for digitalization

initiatives such as digital twins, which require both operational literacy (processes, constraints, stakeholder

reality) and digital literacy (data, integration, governance, roadmap, validation).

This paper proposes a design methodology for a two-course integration at University of Brasília (UnB) that

will be implemented in the first semester of 2026. The methodology couples (i) a graduate IT Project

Management course (GPTI, Applied Computing master’s program) and (ii) an undergraduate Production

Engineering Project-management Course (Production Systems Project 1, PSP1). The shared challenge is the

conceptual development of Digital Twin (DT) solutions for solid waste systems in Brasilia, focusing on recycling

centers involving waste pickers and on improvement opportunities across the waste chain.

1

## Slide 2

Importantly, this is not the first time UnB has connected these two courses. The methodological novelty here

is to use DT as the bridge artifact and the shared socio-technical boundary object: a structure that

simultaneously forces operational grounding (PSP1) and disciplined digital project framing (GPTI), with

traceability from real needs to digital capabilities and validation criteria.

The paper contributes: (1) a replicable two-course integration architecture aligned with project approaches

and PBL; and (2) an artifact-centered digital twin concept-development workflow grounded in Digital Twin

Consortium (DTC) capability thinking and in PMBOK-oriented project artifact practices reflected in course

materials (Digital Twin Consortium, 2020; Mello da Silva & Ishikawa, 2026; University of Brasília, 2025).

2 Related work and conceptual background

2.1 Digital twins as socio-technical systems and IT/OT/ET convergence

DTC defines DT as a virtual representation of real-world entities and processes synchronized at a specified

frequency and fidelity, using real-time and historical data to represent the past and present and to simulate

predicted futures (Digital Twin Consortium, 2020). In this framing, a digital twin is not simply a model or

dashboard; it is a socio-technical system whose value emerges from how it supports decisions and

interventions in real operations. This matters in waste management, where variability (input material quality),

safety, labor constraints, logistics, and institutional governance orient what a digital system can credibly

recommend, automate, or optimize.

DTC’s emphasis on IT/OT/ET convergence provides a useful educational lens: Information Technology (data

collection, processing, storage, communication), Operational Technology (monitoring/control of physical

processes), and Engineering Technology (modeling and system design) must be integrated into a coherent

intervention (University of Brasília, 2025). Pedagogically, this pushes interdisciplinary collaboration: computing

students cannot treat operations as a “domain black box,” and production engineering students cannot treat

digitalization as an external layer that appears after process mapping.

2.2 IT/OT/ET convergence and why it is central to “Digital Twin-first”

DTs become most challenging and most valuable precisely when they sit at the intersection of IT (Information

Technology systems and data/analytics), OT (Operational Technology such as sensors, automation, and

industrial control), and ET (Engineering Technology such as models, design intent, and system engineering

artifacts) (Digital Twin Consortium, 2020). In practice, DT must reconcile heterogeneous data sources and time

scales: IT often operates on business rhythms and transactional correctness; OT operates on real-time constraints,

safety, and reliability; ET operates on design fidelity, physics, and lifecycle reasoning. When these worlds

converge, requirements also converge: integration and data services cannot be separated from trustworthiness,

and intelligence cannot be separated from governance and operational safety (Brazil, 2010; Gharajedaghi,

2011; Ministério do Meio Ambiente e Mudança do Clima, 2024).

The instructional design leverages this convergence to make students practice realistic reasoning. Real-life

System-in-Question (RSQ) and Digital System-in-Question (DSQ) boundaries must explicitly include where IT

ends and OT begins (e.g., what data is available, at what cadence, under what security constraints) and how

ET representations are maintained (e.g., whether the DSQ includes engineering models, assumptions, and their

versioning).

2

## Slide 3

CHAINS OF TECHNOLOGICALLY IMPLEMENTABLE CONFIGURATIONS TECHNOLOGICALLY IMPLEMENTABLE TECHNOLOGICALLY IMPLEMENTABLE TECHNOLOGICALLY IMPLEMENTABLE (IT/OT/ET) CONFIGURATIONS OF DSQ, (IT/OT/ET) CONFIGURATIONS OF DSQ, (IT/OT/ET) CONFIGURATIONS OF DSQ, (IT/OT/ET) OF DIGITAL SYSTEM IN QUESTION (DSQ) AT TIME t=0, COMPATIBLE WITH THE CURRENT COMPATIBLE WITH THE CURRENT COMPATIBLE WITH THE CURRENT USED AS REFERENCE FOR EFFORT IN PORTFOLIOS, PROGRAMS, STATE OF RSQ, SUCH THAT THE CHOICE STATE OF RSQ, SUCH THAT THE CHOICE STATE OF RSQ, SUCH THAT THE CHOICE OF ONE OR MORE OF THESE DSQ OF ONE OR MORE OF THESE DSQ OF ONE OR MORE OF THESE DSQ PROJECTS AND OPERATIONS TO ACHIEVE, AT TIME tn, THE DESIRED CONFIGURATIONS AS CONFIGURATIONS AS CONFIGURATIONS AS ... FUTURE STATE OF RSQ(tn). THE TECHNOLOGICALLY TECHNOLOGICALLY IMPLEMENTABLE TECHNOLOGICALLY IMPLEMENTABLE TECHNOLOGICALLY IMPLEMENTABLE (IT/OT/ET) REFERENCES FOR RSQ AT (IT/OT/ET) REFERENCES FOR RSQ AT (IT/OT/ET) REFERENCES FOR RSQ AT IMPLEMENTABLE (IT/OT/ET) CONFIGURATIONS OF DSQ, t1, RESULTS IN THE DESIRED FUTURE t2, RESULTS IN THE DESIRED FUTURE tn, RESULTS IN THE DESIRED FUTURE GENERATED AND MONITORED BY AI, AS PART OF CHAINS OF STATE FOR RSQ AT TIME tn. STATE FOR RSQ AT TIME tn. STATE FOR RSQ AT TIME tn. TECHNOLOGICALLY IMPLEMENTABLE (IT/OT/ET) DSQ CONFIGURATIONS IN THE VISION HORIZON, HAVE THE

| TIMEt1 |
|---|

| TIMEt2 |
|---|

| TIMEtn |
|---|

CHARACTERISTIC OF BEING UPDATED AT EVERY INSTANT BY AI, SO TAKING THE TECHNOLOGICALLY TAKING THE TECHNOLOGICALLY TAKING THE TECHNOLOGICALLY THAT ANY CHANGE IN ANY TECHNOLOGICALLY IMPLEMENTABLE IMPLEMENTABLE IMPLEMENTABLE IMPLEMENTABLE (IT/OT/ET) DSQ CONFIGURATION BEING USED AS REFERENCE FOR CONFIGURATIONS (IT/OT/ET) OF CONFIGURATIONS (IT/OT/ET) OF CONFIGURATIONS (IT/OT/ET) OF

RSQ, AT ANY POINT IN THE EFFORT REQUIRED TO ACHIEVE THE DSQ(t1) AS REFERENCE, MANAGE DSQ(t2) AS REFERENCE, MANAGE DSQ(tn) AS REFERENCE, MANAGE THE ACQUISITION OF THE ACQUISITION OF THE ACQUISITION OF NECESSARY FUTURE STATE, AT ANY INSTANT t, IS IMMEDIATELY IMPLEMENTABLE IMPLEMENTABLE IMPLEMENTABLE NOTIFIED TO MANAGEMENT EFFORT, ALLOWING FOR CONCRETE, CONFIGURATIONS (IT/OT/ET) OF CONFIGURATIONS (IT/OT/ET) OF CONFIGURATIONS (IT/OT/ET) OF

INSTANTANEOUS ACTIONS IN ANY COMPONENT OF THE PMBOK RSQ AT TIME t1, SO THAT THE RSQ AT TIME t2, SO THAT THE RSQ AT TIME tn, SO THAT THE DESIRED FUTURE STATE OF DESIRED FUTURE STATE OF DESIRED FUTURE STATE OF HIERARCHY, ENABLING "INSTANTANEOUS AGILITY". RSQ(t1) OCCURS, ACCORDING TO RSQ(t2) OCCURS, ACCORDING TO RSQ(tn) OCCURS, ACCORDING TO THE UPDATE OF RSQ(t1), VIA THE UPDATE OF RSQ(t2), VIA THE UPDATE OF RSQ(tn), VIA

EFFORT TO REACH THE DESIRED TECHNOLOGICALLY IMPLEMENTABLE FUTURE STATE INITIAL STATE OF THE SYSTEM IN QUESTION (REAL TWIN=RSQ) (TI/TO/TE) OF THE SYSTEM IN QUESTION (REAL TWIN=RSQ) AT TIME tn, APPROACHED TECHNOLOGICALLY IMPLEMENTABLE (IT/OT/ET) AT TIME ACCORDING TO THE PMBOK HIERARCHY OF PORTFOLIOS, PROGRAMS, t0=RSQ(t0) PROJECTS/EXTENSIONS AND OPERATIONS, TAKING AS REFERENCE THE INITIAL 1-EXISTING: TOTAL/PARTIAL TECHNOLOGICALLY IMPLEMENTABLE STATES (IT/OT/ET) OF THE DIGITAL TWINS OF 2-IMAGINED: TOTAL/PARTIAL THE SYSTEM IN QUESTION AT TIME t0=DSQ(t0) 3-NON-EXISTENT 1-EXISTING: TOTAL/PARTIAL 2-IMAGINED: TOTAL/PARTIAL 3-NON-EXISTENT

Figure 1. Digital Twin as Reference for Real Twin

As shown in Figure 1, DT is the central coupling mechanism and shared boundary object: it requires

operational grounding and capability-oriented digital specification in the same artifact package. A DT is most

strategic when used not just as a copy of the present, but as a reference for defending decisions and guiding

change toward defined future states, obtained from AI’s role in building nexus for scenario creation.

2.3 Capability-oriented specification

Student teams often propose a “platform” without clarifying required capabilities and dependencies. To

mitigate this, the methodology applies a capability-oriented specification approach grounded in the DTC

Capabilities Periodic Table (DTC/CPT), referenced in the GPTI plan (Mello da Silva & Ishikawa, 2026). The

DTC/CPT structures DT thinking into capability groups (DS-Data Services, IR-Integration, IC-Intelligence, UX-

User Experience, MG-Management, and TW-Trustworthiness). When teams incorporate AI agents to support

monitoring, reporting, or decision recommendations, the capability thinking is extended with the DTC AI

Agent Capabilities Periodic Table (AIA/CPT) (Mello da Silva & Ishikawa, 2025, 2026).

2.4 Active learning, and cross-level mentoring

The educational design aligns with evidence on PBL and Flipped Classroom active learning approaches: structured

problem solving, feedback, and iterative refinement generally outperform passive approaches in STEM contexts

(Freeman et al., 2014; Gharajedaghi, 2011; Prince, 2004). Cross-level coupling also aligns with peer

tutoring/near-peer learning literature, where near-peers can scaffold learning through guided questioning

and feedback when roles and safeguards preserve agency (Hmelo-Silver, 2004; Topping, 1996).

3

## Slide 4

3 Educational context and design goals

3.1 Courses and institutional context

The collaboration occurs at UnB, within two complementary programs: Applied Computing (graduate) and

Production Engineering (undergraduate). The graduate course (GPTI) targets IT project management with

explicit emphasis on teamwork, a systems approach, and PBL/Flipped classroom methods (Mello da Silva &

Ishikawa, 2026), focusing on the DT while the undergraduate course (PSP1) targets the RT. Both courses are also

directed to project management, emphasizing operational understanding, constraints, and improvement

opportunities.

3.2 Domain context: waste management and recycling centers

The RT is based on the RSQ, which in the current version of the courses is the recycling centers of Brasilia’s

solid waste system, mainly operated by cooperatives of waste pickers, with a focus on Selective Collection,

Triage, Value-adding Transformation opportunities, and Commercialization. Brazil’s National Solid Waste

Policy (Brazil, 2010) and the corresponding regulation (Ministério do Meio Ambiente e Mudança do Clima,

2024) are the ground of public relevance for this subject.

In the Brasília solid waste context adopted as the Real System in Question (RSQ/Real-life Twin), the student

work is grounded in the Law No. 12,305/2010, which establishes Brazil’s National Solid Waste Policy,

complemented by the regulatory framework of GM/MMA Ordinance No. 1,250 (December 13, 2024) (Brazil,

2010; Ministério do Meio Ambiente e Mudança do Clima, 2024). This ordinance establishes the Incentive

mechanism for the Recycling Industry and Production Chain. In line with Article 3, the RSQ is framed as a set

of stages that extend beyond basic sorting/beneficiation, explicitly including processing and manufacturing

as pathways for the industrial transformation of recyclable materials into higher value-added products. This

RSQ framing connects directly to the ordinance’s targets in Article 4—capacity building, training, and technical

advisory (including national and international exchanges); incubation of cooperatives and solidarity-based

social enterprises in recycling; implementation and adaptation of physical infrastructure for cooperatives and

waste-picker associations; acquisition of equipment for selective collection, beneficiation, treatment, and

recycling; organization and support for marketing networks and production chains; strengthening waste

pickers’ participation in recycling value chains; and technology development to add value to collection and

recycling work—and to Article 6 by treating waste-picker enterprises and/or autonomous waste pickers as a

structuring element of the execution scope. In this way, the RSQ/Real Twin is characterized not only by material

flows and operational constraints, but also by mandated forms of participation, capacity building, and value-

adding transformation, which in turn define the decision boundaries, governance needs, and evidence

requirements that the corresponding Digital System in Question (DSQ/Digital Twin) must respect when

representing and supporting the real system.

The Incentive mechanism for the Recycling Industry and Production Chain commission has received 952

project proposals in 2025, totaling 2,2 billion Brazilian reais in proposals aiming for investments throughout

27 Brazilian federal units (Ministério do Meio Ambiente e Mudança do Clima, 2025).

4 Two-course integration architecture

4.1 Role structure and coupling mechanism

The methodology uses an explicit role structure. As already stated, GPTI teams focus on project aspects of

4

## Slide 5

DSQs and DTs, while PSP1 teams have RSQs and RTs as targets.

The cross-course interaction is organized around a shared paired description of the RSQ as a RT and its

corresponding DSQ as a DT, with clearly defined reciprocal roles between cohorts. At the first class of PSP1,

graduate GPTI students send representatives to introduce to the undergraduate students core project-

management concepts, encompassing foundational DT framing, aligned with Digital Twin Consortium

concepts, and a practical method for producing a tailored project guide for DTs of solid waste systems

components, grounded in PMBOK editions (4th, 6th, 7th, and 8th) and the PMI Guide to Business Analysis

(PMI, 2017b), expressed in an adapted PMBOK-extension format (PMI, 2008, 2017a, 2021, 2025). To anchor

this transfer in concrete evidence rather than abstraction, GPTI representatives also present selected results

and lessons learned from the previous GPTI offering, accessed through the instructor, as worked examples of

how digital-twin project reasoning can be packaged and defended.

In the opposite direction, PSP1 sends representatives to the first class of GPTI to present the functional groups

corresponding to the four components (Selective Collection, Triage, Transformation and Commercialization)

of RSQ, as both a production system and a human activity system, emphasizing real operational flows,

constraints, coordination practices, and feasibility boundaries that the DSQ must respect, as in Figure 2.

In addition, PSP1 students share details relative to the legal and regulatory aspects regarding the RSQ,

explicitly framing Brazil’s National Solid Waste Policy (Law No. 12,305/2010) and the GM/MMA Ordinance No.

1,250 of 13 December 2024.

A key message communicated by GPTI to PSP1 is that project management is not “only PMBOK”: the

integration explicitly treats PMBOK guidance as a basis for tailoring and extends PMBOK8 to place the digital

twin as a central element, while foregrounding SIPA (S-Sustainability, I-Innovation, P-Privacy, and A-Business

Analysis) as essential lenses for socio-technical digital-twin projects in solid waste contexts.

Figure 2. Solid Waste System Functional groups CTTC

4.2 Deliverables as courses coupling points

Figure 3 operationalizes the coupling between GPTI and PSP1 through a shared deliverable chain that functions

as the interface between cohorts. On the GPTI side, the flow starts from PMBOK8 and evolves into an explicit

extension structure (PMBOK8 to GPH.SIPA.S), adding SIPA dimensions—S-Sustainability, I-Innovation, P-

Privacy, and A-Business Analysis—so that tailoring becomes an explicit methodological step rather than an

5

*[2 imagem(ns) omitida(s) nesta página]*

## Slide 6

informal adaptation. This extension is then advanced through group work (GPH.SIPA.S), moving from partial

outputs to a consolidated version and bridging toward PMBOK8 framing, while remaining anchored in

operational stakeholder perspectives (e.g., product developers, waste-picker cooperatives, and landfill

operators). In parallel, the RSQ is framed as both a production system and a human activity system by locating

solid waste within the broader sanitation system and structuring the solid-waste domain through P3RD

priorities (Prevention, Reduction, Reuse, Recycling, Disposal), complemented by the “Digital Mobilizer” role

that connects operational reality to digital project framing.

The coupling occurs at specific checkpoints where deliverables are intentionally designed as shared reference

points rather than shared submissions. TI01 consolidates early deliverables (P2A/P2B) that stabilize a common

RSQ description and stakeholder grounding, enabling PSP1 representatives to brief GPTI on functional groups

and constraints, and GPTI representatives to brief PSP1 on project management and digital-twin framing. TI02A

structures mid-semester deliverables (P3A/P3B/P3C/P3D) that translate the RSQ description into the extended

PMBOK logic (GPH.SIPA.S), culminating in a tailored project-management guide for solid-waste systems and

operational stakeholders. TI02B marks the late-stage coupling through P4A (delivery of the tailored guide) and

P4B (initial milestones and pre-project elements), including needs and gaps, business case, benefits

management plan, project charter, and a baseline project management plan. Finally, TE01 (P6C1/P6C2) is the

closing joint tele-event, where leaders from both courses present a structured synthesis of convergences

between RSQ and DSQ perspectives—mirroring the classes of both courses as a single coordinated team while

each course still completes its own independent final work.

| INDIVIDUAL ONLINE QUESTIONNAIRES | INDIVIDUAL ONLINE QUESTIONNAIRES | TI02A: DELIVERABLES P3A/3B/P3C/P3D |
|---|---|---|

TI02B→DELIVERABLE TI02B→DELIVERABLE P4B P4A

INICIAL MILESTONES PMBOK8→GPH.SIPA.S TAILORED PROJECT GPH.SIPA.S (TEAMS) OF TAILORED PROJECT S-SUSTAINABILITY MANAGEMENT GUIDE →GPH.SIPA.S+(PARTIAL) MANAGEMENT GUIDE I-INNOVATION PMBOK8 →COMPONENTS OF THE P-PRIVACY →GPH.SIPA (TOTAL) RSQ=RSRS=REAL-LIFE TWIN A-BUSINESS ANALYSIS WITH SYSTEM IN QUESTION= →PMBOK8 GPH.SIPA/SRSPRI.SIPA RISK-ADJUSTED DECISIONS REAL-LIFE TWIN RSQ=RSRS GPH.SIPA/RSRSPR1.SIPA-CC? GPH.SIPA/SRSDM.SIPA-CC SYSTEM IN QUESTION DESCRIPTION AND CORRESPONDING OPERATIONAL STAKEHOLDERS GPH.SIPA/SRSR2.SIPA-CC (SQ=SRS, INCLUDING OPERATIONAL RSQ DIGITAL TWIN >PRODUCT DEVELOPERS GPH.SIPA/SRSR3.SIPA-CC STAKEHOLDERS )→PARTIAL COLLEGES) =DSQ=DSRS GPH.SIPA/SRSDS-SIPA >COOPERATIVES OF WASTE PICKERS REAL-LIFE TWIN=RSQ=RSRS DSQ=DSRS=DIGITAL TWIN RSQ=RSRS=REAL-LIFE TWIN >BIODISGESTER SANITARY LANDFILL DIGITAL TWIN=DSQ=DSRS GPH.SIPA/DSRSPRI.SIPA GPH.SIPA/RSRSPR1.SIPA >DEVELOPERS OF PRODUCTS AND OPERATORS GPH.SIPA/DSRSPR1.SIPA-CC? GPH.SIPA/RSRSPR1.SIPA-CC? CORRESPONDING PRODUCTION PROCESSES GPH.SIPA/DSRSDM.SIPA-CC GPH.SPA/RSRSDM.SIPA-CC P&R1→RSRSPR1.SIPA & DSRSPR1.SIPA SOLID WASTE/ GPH.SIPA/DSRSR2.SIPA-CC GPH.SIPA/RSRSR2.SIPA-CC >COOPERATIVES OF WASTE PICKERS RESIDUES GPH.SIPA/DSRSR3.SIPA-CC GPH.SIPA/RSRSR3.SIPA-CC DM→RSRSDM.SIPA-CC & DSRSDM.SIPA-CC GPH.SIPA/DSRSDS-SIPA GPH.SIPA/RSRSDS.SIPA BASIC SANITARY SYSTEM=P3RD R2→RSRSR2.SIPA-CC & DSRSR2.SIPA-CC →PRE-PROJECT DSQ=DSRS=DIGITAL TWIN SYSTEM =WSDR P-PREVENTION R3→RSRSR3.SIPA-CC & DSRSR3.SIPA-CC NEEDS&GAPS GPH.SIPA/DSRSPR1.SIPA R1-REDUCTION >BIODIGESTER SANITARY LANDFILL OPER WATER=W BUSINESS CASE GPH.SIPA/DSRSPR1.SIPA-CC? DM-DIGITAL DS→RSRSDS.SIPA & DSRSDS.SIPA SEWAGE=S BENEFITS MANAGEMENT PLAN GPH.SIPA/DSRSDM.SIPA.CC MOBILIZER DRAINAGE/RAINWATER=D →PROJEC CHARTER-TAP GPH.SIPA/DSRSR2.SIPA-CC R2-REUSE RESIDUES/WASTE=R TI01→DELIVERABLES GPH.SIPA/DSRSR3.SIPA-CC →PROJECT MANAGEMENT R3-RECYCLING GPH.SIPA/DSRSDS.SIPA PLAN DS-DISPOSAL P2A/P2B

TE01→DELIVERABLES P6C1/P6C2: CLOSING TELE-EVENT→SYNTESIS MIRROWING CLASSES OF BOTH COURSES AS ONE TEAM

Figure 3. Deliverables

Although each course maintains its own internal assignments and assessment, the integration is sustained

through a small set of structured joint coordination touchpoints, involving team-leaders and college-leaders

presentations, under the guidance of teaching assistants (tutors). Due to different course schedules, the two

confirmed synchronized moments are the beginning and the end: PSP1 runs for 16 weeks and GPTI for 8

weeks, so GPTI starts mid-way through the PSP1 semester, which makes it fully feasible to align GPTI’s kickoff

with PSP1’s ongoing work and to ensure both courses conclude together. At the beginning of PSP1, the initial

domain and methodological context is introduced by representatives connected to GPTI (leveraging results

6

## Slide 7

and learning artifacts from the immediate previous GPTI offering, provided via the instructor), setting a

concrete baseline for how RSQ/DSQ reasoning and tailored project-management guidance will be treated.

To ensure operational grounding, capability thinking is complemented with a shared description pattern also

present in course materials: Function, Structure, Process, and Context (F/S/P/C) (Gharajedaghi, 2011; University

of Brasília, 2025). F/S/P/C provides a stable anchor for systems thinking: teams define boundaries, interfaces,

constraints, and decision points before deriving digital requirements. As shown in Figure 4, the process of

interconnection between the GPTI and PSP1 courses becomes operational mainly during task TI01,

encompassing deliverables P2A and P2B.

Figure 4. The two courses link – PSP1 and GPTI

During the middle of the semester, coordination is maintained through monitor-led meetings and, when

needed, additional meetings among student team leaders to prepare and refine the four joint presentation

themes—(i) RSQ/DSQ descriptions, (ii) PMBOK foundations and tailoring logic with the inclusion of SIPA and

DTC concepts, (iii) applying the tailored adapted PMBOK extension format to the corresponding RSQ/DSQ

descriptions, and (iv) the closing joint tele-event. The tele-event serves as the final cross-course presentation,

where PSP1 and GPTI teams explicitly surface convergences between operational system understanding and

digital-twin project framing, while preserving the independence of each course’s deliverables.

5 Conclusion

The two-course integration uses the Digital Twin not as an “extra topic,” but as a disciplined bridge that forces

mutual intelligibility between Applied Computing and Production Engineering. By pairing the Real System in

Question (RSQ/Real-life Twin) with its Digital System in Question (DSQ/Digital Twin) and by structuring

interaction through reciprocal representative sessions and a shared deliverable chain, the design makes cross-

level collaboration auditable: PSP1 contributes operational descriptions grounded in production-system and

human-activity realities (RSQ), while GPTI contributes with the Digital Twin Consortium framing. Both courses

operate based on project-tailoring logic anchored in PMBOK editions and extended through the inclusion of

7

*[1 imagem(ns) omitida(s) nesta página]*

## Slide 8

SIPA (Sustainability, Innovation, Privacy, and Business Analysis). The result is an integration that preserves

disciplinary depth while creating a common language for socio-technical design decisions, explicitly tied to

regulatory constraints and stakeholder participation in Brasília’s solid waste recycling context.

From an engineering-education perspective, the core contribution is a replicable coupling mechanism where

learning is made visible through structured checkpoints and deliverables rather than informal collaboration.

The cadence of joint presentations (system description, PMBOK foundations, applying the tailored guide to

the RSQ/DSQ pair, and the closing tele-event synthesis) provides a practical pathway for aligning PMBOK8

project approach and active learning principles with credible evidence of student reasoning and integration

quality. More broadly, the approach offers a transferable pattern for other domains in which digitalization

must be grounded in real operational constraints: when the coupling is anchored in a shared RSQ/DSQ

description and a tailored project-management guide, students practice not only “designing a technology,”

but also packaging, defending, and governing a socio-technical pathway that can realistically be executed.

6 Acknowledgements

This work was partially developed in the context of project 2023-1-DK01-KA220-HED-00165709,

“EGALITARIAN - Education, Digitalisation and Collaboration for Sustainability” which has been funded with

support from the European Commission. This publication reflects the views only of the authors, and the

Commission cannot be held responsible for any use which may be made of the information contained therein.

References Brazil. (2010). Lei nº 12.305, de 2 de agosto de 2010. Institui a Política Nacional de Resíduos Sólidos. Diário Oficial da União. https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2010/lei/l12305.htm Digital Twin Consortium. (2020). Digital Twin Consortium defines digital twin. Falchikov, N. (2001). Learning together: Peer tutoring in higher education. RoutledgeFalmer. Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. Proceedings of the National Academy of Sciences, 111(23), 8410–8415. Gharajedaghi, J. (2011). Systems thinking: Managing chaos and complexity: A platform for designing business architecture (3rd ed.). Morgan Kaufmann. Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? Educational Psychology Review. Mello da Silva, J., & Ishikawa, E. (2025). Digital Twin: AI Agent Capabilities Periodic Table (DT/AIACPT) [Course notes]. UnB. Mello da Silva, J., & Ishikawa, E. (2026). Plano GPTI: Gestão de Projetos de TI – PPCA0006 [Course syllabus]. UnB. Ministério do Meio Ambiente e Mudança do Clima. (2024, December 13). Portaria GM/MMA Nº 1.250. DOU. https://www.in.gov.br/en/web/dou/-/portaria-gm/mma-n-1.250-de-13-de-dezembro-de-2024- 601717295 Ministério do Meio Ambiente e Mudança do Clima. (2025). Lei de Incentivo à Reciclagem atrai R$ 2,2 bilhões em propostas. https://www.gov.br/mma/pt-br/noticias/lei-de-incentivo-a-reciclagem-atrai-r-2-2-bilhoes-em-propostas Prince, M. (2004). Does active learning work? A review of the research. Journal of Engineering Education, 93(3), 223–231. PMI (2008). A guide to the project management body of knowledge (PMBOK guide) (4th ed.). PMI (2017a). A guide to the project management body of knowledge (PMBOK guide) (6th ed.). PMI (2017b). The PMI Guide to Business Analysis. PMI (2021). A guide to the project management body of knowledge (PMBOK guide) (7th ed.). PMI (2025). A guide to the project management body of knowledge (PMBOK guide) (8th ed.). Topping, K. J. (1996). The effectiveness of peer tutoring in further and higher education: A typology and review of the literature. Higher Education, 32(3), 321–345. University of Brasília. (2025). Project Management Review Notes: PMBOK6 to Extended Formats [Course material]. University of Brasília. (2025). Resumo de Tarefas e Conteúdos (GPTI 2025S) [Course material].

8
