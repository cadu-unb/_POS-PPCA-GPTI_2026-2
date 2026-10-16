## Slide 1

From Replica to Reference: Active Learning in Engineering Education for Digital Twin–Guided Real-System Evolution

1 1 1 1 João Mello da Silva , Mateus Halbe Torres , Edison Ishikawa , Ari Melo Mariano , César Antônio Ciuffo 2 Moreira

1 University of Brasília-UnB, Brazil 2 APEX Brasil, Brazil

Email: joao.mellos@gmail.com, mateusconsigo@gmail.com, edisonishikawa@gmail.com, arimariano@unb.br, cesar.moreira@apexbrasil.com.br

Abstract

This paper reports an active-learning application in a graduate IT project management course through a paradigm shift:

treating the Digital Twin (DT) as the reference model that drives real-system (Real-life Twin=RT) evolution, rather than a

subordinate replica validated against the present. Having PMBOK Guides and PMI BA Guide as major project management

references, the course focuses on developing a project management guide tailored for DT components of Brasilia’s

Solid Waste System, in an adapted PMBOK extension format. Distributed in groups, students work with a paired

representation of theReal System in Question (RSQ=RT) and its digital counterpart (DSQ=DT), initially describing both systems

in terms of Function, Structure, Process, and Context (F/S/P/C), showing interactions among these dimensions. To structure

what the DT provides, learners apply the Digital Twin Consortium Capabilities (DTC) Periodic Table (WHAT: DS–Data

Services, IR–Integration, IC–Intelligence, UX–User Experience, and MG–Management and TW–Trustworthiness). After

structuring how capabilities are put together, the groups map selected functions to DTC AI-agent capabilities (HOW: PW-

Perception/Knowledge, CG-Cognition/Reasoning, LA-Learning/Adaptation, IC-Interaction/Collaboration, AE-Action/Execution,

and GS-Governance/Safety), spanning conversational, workflow, autonomous, and collaborative agent modalities. Learning

activities are organized as twin-in-the-loop decision cycles: teams use DSQ to generate and compare implementable

configuration chains DSQ(t ), DSQ(t ), ..., DSQ(t ) that target a desired future state RSQ(t ), with each update explicitly 1 2 n n

informing the required portfolio/program/project/extension/ operations effort in the real system. Evaluation triangulates

rubric-based assessment of artifacts (traceability from F/S/P/C to WHAT/HOW choices, uncertainty and risk treatment,

and decision defensibility), concept measures of anticipatory systems reasoning, and reflective analyses of reference-

direction change (real to twin vs. twin to real). Expected results include a transferable instructional pattern for AI-enabled,

governance-aware digital twins and empirical insight into how “twin-first” framing strengthens risk-informed, future-

oriented engineering judgment.

Keywords: Active Learning; Digital twins; Anticipatory systems; Exploring New .

1 Introduction

Digital twins (DTs) have matured from “models that resemble reality” into socio-technical systems that

coordinate data, integrations, analytics, interfaces, governance, and trust to support decisions and execution.

The Digital Twin Consortium (DTC) emphasizes DT as a virtual representation of entities and processes

synchronized with its real counterpart at specified frequency and fidelity (Digital Twin Consortium, 2025). In

educational practice, however, DTs are still frequently framed as subordinate replicas, where the primary

success criterion is to mirror the present state. That framing is limiting because it under-weights the central

reason DTs matter in engineering and operations: they can be used to steer systems toward desired futures

under constraints, uncertainty, and risk.

This paper reports the initial phase, corresponding to the description of both, the Real System in Question

(Real-life Twin=RSQ=RT) and its corresponding Digital System in Question (Digital Twin=DSQ=DT), of an 1

## Slide 2

active-learning design for a graduate IT project management course that makes a deliberate reference-

direction change. Having PMBOK4, PMBOK6, PMBOK7 and PMBOK8 as major project management

references, the course focus is the development of a project management guide tailored for DT components

of Brasilia’s Solid Waste System, in an adapted PMBOK extension format. Instead of “Real-life Twin to Digital

Twin” validation being the main loop, students are guided to practice “Digital Twin to Real-life Twin”

reasoning: the DT becomes the reference model that drives real-system evolution over time. The course

context reinforces that the output cannot be merely conceptual; it must be execution-aware and governance-

aware, explicitly connecting Digital System in Question (DSQ) decisions to portfolio, program,

project/extensions, and operations work (Project Management Institute, 2008, 2017a, 2017b, 2021, 2025;

University of Brasília, 2025a). In this approach, students are assessed not by how sophisticated their models

look, but by how defensible their decisions are under uncertainty, and how implementable their evolution

pathway is.

2 Background and Conceptual Foundations

2.1 From digital replica to decision reference

A DT becomes strategically meaningful when it helps decision-makers choose among alternatives and justify

change sequencing. When students treat DT as a replica, their work tends to optimize fidelity against today’s

conditions; when they treat DT as a reference, their work tends to optimize decision defensibility toward a

future target. This matters because real systems are not static: constraints change, operations evolve, risks

materialize, and the information environment shifts. Treating the DT as a reference forces students to

articulate a desired future state and make the pathway explicit, rather than implicitly assuming that

improvement is the natural consequence of measurement.

2.2 RSQ/DSQ and F/S/P/C traceability

To keep the pattern auditable, students build a paired representation concept of Real Systems in Question

(RSQ) and DSQs. Both are described using Function, Structure, Process, and Context (F/S/P/C), making explicit

how changes in context propagate into feasible structures, processes, and functions (Gharajedaghi, 2011). The

course materials provide the conceptual scaffolding and deliverable expectations for this representation,

emphasizing traceability and disciplined articulation of system boundaries and requirements (University of

Brasília, 2025a, 2025b). F/S/P/C plays the role of the “argument spine” of the work: capabilities, agent

functions, and implementation steps must remain consistent with this system description.

2.3 Capability logic: WHAT and HOW

The pattern uses a two-layer capability logic to avoid tool-first thinking. First, students decide WHAT the twin

must provide using the Digital Twin Consortium Capabilities Periodic Table categories (Figure 1), which

encompass DS (Data Services), IR (Integration), IC (Intelligence), UX (User Experience), MG (Management), and

TW (Trustworthiness) (Digital Twin Consortium, 2025). Consistent with the table’s framing, these categories

can be read as a value progression from DATA to INFORMATION, KNOWLEDGE, KNOW-HOW and, ultimately,

BUSINESS WISDOM.

2

## Slide 3

Figure 1. Digital Twin Capabilities Periodic Table, WHAT: Data/Information/Knowledge/Know-how/Wisdom

Second, students decide HOW selected functions will be performed using the AI Agent Capabilities Periodic

Table categories (Figure 2) in the same format: PW (Perception & Knowledge), CG (Cognition & Reasoning),

LA (Learning & Adaptation), AE (Action & Execution), IC (Interaction & Collaboration), and GS (Governance &

Safety) (Digital Twin Consortium, 2025). This separation is especially important in educational settings where

generative AI can bias teams toward solutions that sound powerful but have unclear requirements, weak

governance, or poor execution realism. It is worthwhile emphasizing the role of the Organizational

Performance Matrix Readiness x Excellence of showing the GS-Governance & Safety capabilities

organizational excellence against the IC-Interaction & Collaboration capabilities organizational readiness.

Figure 2. Digital Twin Capabilities Periodic Table, HOW: Data/Information/Knowledge/Know-how/Wisdom

Figure 3 summarizes the two-layer capability logic used in the instructional pattern. At the WHAT (Twin) layer,

teams make a requirements-oriented selection of digital twin capability categories (DS/IR/IC/UX/MG/TW) to

justify what the DSQ must provide to support decisions (Digital Twin Consortium, 2025). At the HOW

(Twin/Agent) layer, teams make a requirements-oriented selection of AI-agent capability categories

(PW/CG/LA/AE/IC/GS) to justify how selected DSQ functions will be implemented to support decisions, with

the choice of agent modality (conversational, workflow, autonomous, or collaborative) explicitly constrained

by governance and safety requirements (Digital Twin Consortium, 2025).

3

*[2 imagem(ns) omitida(s) nesta página]*

## Slide 4

Figure 3. Digital Twin Capabilities Periodic Table: WHAT (Capabilities), HOW (AI Types), HOW (Capabilities)

2.4 IT/OT/ET convergence and why it is central to “Digital Twin-first”

DTs become most challenging and most valuable precisely when they sit at the intersection of IT (Information

Technology systems and data/analytics), OT (Operational Technology such as sensors, automation, and

industrial control), and ET (Engineering Technology such as models, design intent, and system engineering

artifacts) (Hollywood, 2020). In practice, the DT must reconcile heterogeneous data sources and time scales:

IT often operates on business rhythms and transactional correctness; OT operates on real-time constraints,

safety, and reliability; ET operates on design fidelity, physics, and lifecycle reasoning. When these worlds

converge, requirements also converge: integration and data services cannot be separated from

trustworthiness, and intelligence cannot be separated from governance and operational safety (Digital Twin

Consortium, 2025; Hollywood, 2020).

The instructional design leverages this convergence to make students practice realistic reasoning. RSQ/DSQ

boundaries must explicitly include where IT ends and OT begins (e.g., what data is available, at what cadence,

under what security constraints) and how ET representations are maintained (e.g., whether the DSQ includes

engineering models, assumptions, and their versioning). As shown in Figure 4, the “Digital Twin-first” framing

then becomes a disciplined way to coordinate convergence decisions: teams use DSQ(t1), DSQ(t2), ..., DSQ(tn)

to make explicit which integration and trust steps are prerequisites for higher-level intelligence and agent

autonomy, and which parts of the system must remain human-governed due to safety or ethical constraints.

4

*[2 imagem(ns) omitida(s) nesta página]*

## Slide 5

CHAINS OF TECHNOLOGICALLY IMPLEMENTABLE CONFIGURATIONS TECHNOLOGICALLY IMPLEMENTABLE TECHNOLOGICALLY IMPLEMENTABLE TECHNOLOGICALLY IMPLEMENTABLE (IT/OT/ET) CONFIGURATIONS OF DSQ, (IT/OT/ET) CONFIGURATIONS OF DSQ, (IT/OT/ET) CONFIGURATIONS OF DSQ, (IT/OT/ET) OF DIGITAL SYSTEM IN QUESTION (DSQ) AT TIME t=0, COMPATIBLE WITH THE CURRENT COMPATIBLE WITH THE CURRENT COMPATIBLE WITH THE CURRENT USED AS REFERENCE FOR EFFORT IN PORTFOLIOS, PROGRAMS, STATE OF RSQ, SUCH THAT THE CHOICE STATE OF RSQ, SUCH THAT THE CHOICE STATE OF RSQ, SUCH THAT THE CHOICE OF ONE OR MORE OF THESE DSQ OF ONE OR MORE OF THESE DSQ OF ONE OR MORE OF THESE DSQ PROJECTS AND OPERATIONS TO ACHIEVE, AT TIME tn, THE DESIRED CONFIGURATIONS AS CONFIGURATIONS AS CONFIGURATIONS AS ... FUTURE STATE OF RSQ(tn). THE TECHNOLOGICALLY TECHNOLOGICALLY IMPLEMENTABLE TECHNOLOGICALLY IMPLEMENTABLE TECHNOLOGICALLY IMPLEMENTABLE (IT/OT/ET) REFERENCES FOR RSQ AT (IT/OT/ET) REFERENCES FOR RSQ AT (IT/OT/ET) REFERENCES FOR RSQ AT IMPLEMENTABLE (IT/OT/ET) CONFIGURATIONS OF DSQ, t1, RESULTS IN THE DESIRED FUTURE t2, RESULTS IN THE DESIRED FUTURE tn, RESULTS IN THE DESIRED FUTURE GENERATED AND MONITORED BY AI, AS PART OF CHAINS OF STATE FOR RSQ AT TIME tn. STATE FOR RSQ AT TIME tn. STATE FOR RSQ AT TIME tn. TECHNOLOGICALLY IMPLEMENTABLE (IT/OT/ET) DSQ CONFIGURATIONS IN THE VISION HORIZON, HAVE THE

| TIMEt1 |
|---|

| TIMEt2 |
|---|

| TIMEtn |
|---|

CHARACTERISTIC OF BEING UPDATED AT EVERY INSTANT BY AI, SO TAKING THE TECHNOLOGICALLY TAKING THE TECHNOLOGICALLY TAKING THE TECHNOLOGICALLY THAT ANY CHANGE IN ANY TECHNOLOGICALLY IMPLEMENTABLE IMPLEMENTABLE IMPLEMENTABLE IMPLEMENTABLE (IT/OT/ET) DSQ CONFIGURATION BEING USED AS REFERENCE FOR CONFIGURATIONS (IT/OT/ET) OF CONFIGURATIONS (IT/OT/ET) OF CONFIGURATIONS (IT/OT/ET) OF

RSQ, AT ANY POINT IN THE EFFORT REQUIRED TO ACHIEVE THE DSQ(t1) AS REFERENCE, MANAGE DSQ(t2) AS REFERENCE, MANAGE DSQ(tn) AS REFERENCE, MANAGE THE ACQUISITION OF THE ACQUISITION OF THE ACQUISITION OF NECESSARY FUTURE STATE, AT ANY INSTANT t, IS IMMEDIATELY IMPLEMENTABLE IMPLEMENTABLE IMPLEMENTABLE NOTIFIED TO MANAGEMENT EFFORT, ALLOWING FOR CONCRETE, CONFIGURATIONS (IT/OT/ET) OF CONFIGURATIONS (IT/OT/ET) OF CONFIGURATIONS (IT/OT/ET) OF RSQ AT TIME t1, SO THAT THE RSQ AT TIME t2, SO THAT THE RSQ AT TIME tn, SO THAT THE INSTANTANEOUS ACTIONS IN ANY COMPONENT OF THE PMBOK DESIRED FUTURE STATE OF DESIRED FUTURE STATE OF DESIRED FUTURE STATE OF HIERARCHY, ENABLING "INSTANTANEOUS AGILITY". RSQ(t1) OCCURS, ACCORDING TO RSQ(t2) OCCURS, ACCORDING TO RSQ(tn) OCCURS, ACCORDING TO THE UPDATE OF RSQ(t1), VIA THE UPDATE OF RSQ(t2), VIA THE UPDATE OF RSQ(tn), VIA

EFFORT TO REACH THE DESIRED TECHNOLOGICALLY IMPLEMENTABLE FUTURE STATE INITIAL STATE OF THE SYSTEM IN QUESTION (REAL TWIN=RSQ) (TI/TO/TE) OF THE SYSTEM IN QUESTION (REAL TWIN=RSQ) AT TIME tn, APPROACHED TECHNOLOGICALLY IMPLEMENTABLE (IT/OT/ET) AT TIME ACCORDING TO THE PMBOK HIERARCHY OF PORTFOLIOS, PROGRAMS, t0=RSQ(t0) PROJECTS/EXTENSIONS AND OPERATIONS, TAKING AS REFERENCE THE INITIAL 1-EXISTING: TOTAL/PARTIAL TECHNOLOGICALLY IMPLEMENTABLE STATES (IT/OT/ET) OF THE DIGITAL TWINS OF 2-IMAGINED: TOTAL/PARTIAL THE SYSTEM IN QUESTION AT TIME t0=DSQ(t0) 3-NON-EXISTENT 1-EXISTING: TOTAL/PARTIAL 2-IMAGINED: TOTAL/PARTIAL 3-NON-EXISTENT

Figure 4. Digital Twin as Reference for Real Twin

3 Instructional Design

3.1 Course environment and active-learning structure

The pattern is designed for a graduate IT project management course in which teamwork is the default

learning unit and active learning is operationalized through structured workshops, problem-based learning,

and student-led artifact production (Guerra et al., 2017; University of Brasília, 2025a). Students are not treated

as passive recipients of frameworks; instead, they use frameworks to build a coherent, auditable argument

about system evolution. The pattern is compatible with the course’s broader emphasis on disciplined

execution and managerial reasoning, using PMI project management guidance as a shared language for

packaging work and defending decisions (Project Management Institute, 2008, 2017a, 2017b, 2021, 2025).

3.2 Twin-in-the-loop decision cycles and configuration chains

The learning workflow is organized as iterated twin-in-the-loop decision cycles. Teams first are exposed to an

established RSQ(t0) baseline and define DSQ(t0) as the initial twin scope with explicit synchronization cadence

and fidelity. They then define a desired future state RSQ(tn) and work backward through implementable steps.

Each step proposes a DSQ configuration DSQ(tk) that enables specific decision functions and governance

constraints and then derives the corresponding portfolio/program/project/extension/operations work

package required to produce the real-system changes toward RSQ(tk). Over multiple iterations, the chain

DSQ(t1), DSQ(t2), ..., DSQ(tn) becomes the structured AI artifact that encodes sequencing, dependencies,

trade-offs, and governance gates.

This structure is intentionally “execution coupled.” Instead of allowing students to design an idealized twin,

each DSQ step must explain what will change in real operations, which stakeholders are involved, what risks

are introduced or mitigated, and what trustworthiness and governance measures are required. This ties 5

## Slide 6

directly to the project’s management intent and aligns with the course’s deliverable framing (University of

Brasília, 2025b).

3.3 A transferable worked-example template

To support transfer across domains, teams instantiate a worked-example template. For the course being

reported in this paper, the concrete RSQs are the components of the Solid Waste System in Brasilia, Brazil.

Specifically for this case, the components of the RSQ were categorized in terms of four functional elements:

Selective Collection, Triage, Transformation and Commercialization. For any context, the template always

begins with a clear RSQ scope definition (including stakeholders and constraints), then defines DSQ scope

and fidelity, selects WHAT capabilities are required for decisions, maps HOW capabilities to agent functions,

and finally produces a sequenced configuration chain with packaging and risk treatment. While the domain

can vary widely (e.g., urban infrastructure, industrial process improvement, service systems), the learning

objective is invariant: disciplined, future-oriented, governance-aware decision-making through a DT-as-

reference lens.

As an input to the framework shown in Figure 4, the course flow begins with a review of PMBOK8, followed

by the evolution of PMBOK8 into an adapted PMBOK extension format (PMBOK8 to GPH.SIPA.S), through the

separate inclusion, via teamwork in “partial colleges” dedicated to each SIPA dimension (S-Sustainability, I-

Innovation, P-Privacy, and A-Business Analysis), so that tailoring becomes an explicit methodological step

rather than an informal adaptation. This PMBOK8 evolution, in an adapted PMBOK extension format is then

advanced, through teamwork in a “total college”, moving from partial outputs obtained by the “partial

colleges” by dimension SIPA, to a consolidated version involving all SIPA dimensions and bridging toward

PMBOK8 framing (GPH.SIPA.S+), while remaining anchored in operational stakeholder perspectives (e.g.,

product developers, waste-picker cooperatives, and landfill operators). In parallel, the RSQ is framed as both

a production system and a human activity system by locating solid waste within the broader sanitation system

and structuring the solid-waste domain through P3RD priorities (P-Prevention, R1-Reduction, R2-Reuse, R3-

Recycling, DS-Disposal), complemented by the “Digital Mobilizer” role that connects operational reality to

digital project framing.

4 Learning Artifacts and Deliverables

The deliverables in this pattern are designed to function as a single integrated argument rather than separate

assignments. The RSQ/DSQ F/S/P/C descriptions provide the system-level grounding and boundary clarity;

the WHAT selection provides a requirements rationale; the HOW mapping provides an implementation

rationale; and the DSQ configuration chain provides the evolution narrative and sequencing logic. Students

are expected to ensure that artifacts remain mutually consistent: capabilities must be traced to system needs,

integration and governance must be explicitly addressed, and the path from DSQ decisions to real-world

execution must be defensible.

Because the twin is treated as a decision reference, the quality of deliverables is judged primarily by

traceability and defensibility rather than by presentation polish. A strong submission makes explicit how

context constraints (e.g., privacy, safety, procurement) shape feasible structures and processes; it uses the

WHAT layer to explain why a capability is needed; it uses the HOW layer to justify which agent modalities are

appropriate; and it translates the resulting DSQ(t1), DSQ(t2), ..., DSQ(tn) chain into implementation work that

can be managed under realistic organizational constraints.

6

## Slide 7

5 Assessment and Evaluation

Evaluation triangulates three evidence streams: rubric-based assessment of artifacts, concept measures of

anticipatory reasoning, and reflective analyses of the reference-direction shift. The artifact rubric evaluates

traceability from F/S/P/C to WHAT/HOW choices, coherence of system boundaries, explicit uncertainty and

risk treatment, and decision defensibility. To operationalize this, the rubric uses a 0–4 scale per dimension (0

absent, 1 weak, 2 adequate, 3 strong, 4 exemplary) across the following dimensions: (i) RSQ/DSQ boundary

clarity and F/S/P/C completeness; (ii) traceability from F/S/P/C to WHAT selections; (iii) coherence between

WHAT selections and HOW mapping to agent capabilities; (iv) quality of DSQ configuration chain sequencing

and dependency reasoning; (v) explicit risk, uncertainty, and governance treatment; and (vi) implementability

of the portfolio/program/project/extension/operations packaging (Project Management Institute, 2008, 2017,

2021, 2025; University of Brasília, 2025a, 2025b). Instructors and/or teaching assistants can improve scoring

consistency by calibrating on two anchor submissions and discussing borderline cases before grading.

Concept measures are used to check whether students can reason about futures rather than merely describe

present conditions. Typical prompts include identifying leading indicators and feedback loops, articulating

decision criteria under uncertainty, and distinguishing between structural constraints and process variability.

Reflection is assessed through a structured memo in which students compare real to twin validation logic

against twin to real guidance logic and discuss how the change affects accountability, governance, and risk

posture. Risk management reasoning is supported by established risk frameworks and project management

guidance (International Organization for Standardization, 2018, 2019; Project Management Institute, 2017,

2021; University of Brasília, 2025b).

6 Discussion

The reference-direction shift changes what students optimize for. In a replica-first mindset, the dominant

criteria become representational fidelity of the present; in a reference-first mindset, the dominant criteria

become defensibility of a future-oriented pathway under change. This naturally elevates integration and

trustworthiness from optional concerns to gating concerns: in converged IT/OT/ET systems, the ability to

reason well depends on whether the DSQ has access to trusted data, robust integrations, and governance

mechanisms that prevent unsafe or unethical actions. The WHAT/HOW separation reinforces this, because

teams must make requirements explicit and then justify which agent modalities can be responsibly deployed

given the system’s constraints and risk posture.

The DSQ configuration chain is also pedagogically important because it externalizes sequencing,

dependencies, and decision trade-offs. Students learn that autonomy is not a switch; it is an incremental

capability that depends on integration maturity, data quality, operational constraints, and governance

readiness. This is precisely where IT/OT/ET convergence becomes an educational advantage: it forces teams

to confront that operational systems are not merely data problems and that engineering intent is not merely

documentation. The twin-in-the-loop cycles then become a method for reasoning about the interplay

between operational risk, technical feasibility, and managerial execution.

Limitations follow from the nature of design reports and course-based studies. Outcomes depend on cohort

maturity, domain choice, and the extent to which teams have access to realistic data and operational

stakeholders. If empirical learning gains are claimed, future work should include multi-cohort replication,

inter-rater reliability checks for rubric scoring, and validation of the anticipatory reasoning instrument. A

promising extension is to analyze which capability categories (especially TW in WHAT and governance/safety

in HOW) most strongly correlate with improvements in decision defensibility and sequencing realism.

7 Conclusion

This paper reported the initial phase, corresponding to the description of both, the Real System in Question

7

## Slide 8

(Real-life Twin=RSQ=RT) and its corresponding Digital System in Question (Digital Twin=DSQ=DT), of an

active-learning instructional design that deliberately moves the digital twin from subordinate replica to

decision reference, treating it as a driver of real-system evolution rather than merely an after-the-fact mirror.

The design combines RSQ/DSQ paired representation using F/S/P/C, a two-layer capability logic (WHAT via

the DTC Capabilities Periodic Table and HOW via AI-agent capability families), and twin-in-the-loop decision

cycles that generate an implementable DSQ configuration chain targeting a desired future RSQ state. By

explicitly foregrounding IT/OT/ET convergence, the pattern forces students to address integration,

trustworthiness, governance, and sequencing realism as central design constraints, strengthening risk-

informed and future-oriented engineering judgment in an execution-coupled educational setting.

Therefore, repeating the left hand-side of Figure 4: Chains of technologically implementable configurations

(IT/OT/ET) of Digital System in Question (DSQ) at time t=0, used as reference for effort in portfolios, programs,

projects and operations to achieve, at time tn, the desired future state of RSQ(tn). The technologically

implementable (IT/OT/ET) configurations of DSQ, generated and monitored by AI, as part of chains of

technologically implementable (IT/OT/ET) DSQ configurations in the vision horizon, have the characteristic of

being updated at every instant by AI, so that any change in any technologically implementable (IT/OT/ET)

DSQ configuration being used as reference for RSQ, at any point in the effort required to achieve the necessary

future state, at any instant t, is immediately notified to management effort, allowing for concrete,

instantaneous actions in any component of the PMBOK hierarchy, enabling "instantaneous agility".

Based on the digital twin approach described in this paper, the authors intend to conduct surveys with the

students to assess actual improvement and evolution of learners’ abilities regarding engineering decision-

making and thinking.

8 Acknowledgements

This work was partially developed in the context of project 2023-1-DK01-KA220-HED-00165709,

“EGALITARIAN - Education, Digitalization and Collaboration for Sustainability” which has been funded with

support from the European Commission-EC. This publication reflects the views only of the authors, and the

EC cannot be held responsible for any use which may be made of the information contained therein.

References Digital Twin Consortium. (2025). AI agent capabilities periodic table – interactive framework and toolkit. Retrieved February 8, 2026, from https://www.digitaltwinconsortium.org/initiatives/ai-agent-capabilities-periodic-table/ Digital Twin Consortium. (2025). Data and knowledge management in digital twin systems. Retrieved February 8, 2026, from https://www.digitaltwinconsortium.org/ Digital Twin Consortium. (2025). Digital twin consortium capabilities periodic table – worksheet (v1.2). Gharajedaghi, J. (2011). Systems thinking: Managing chaos and complexity: A platform for designing business architecture (3rd ed.). Morgan Kaufmann. Guerra, A., et al. (2017). Latin case [Online PDF]. Retrieved February 8, 2026, from https://vbn.aau.dk/ws/portalfiles/portal/262849868/Latin_Case_online.pdf Hollywood, P. (2020). Why convergence of IT/OT needs to include ET. ARC Advisory Group. Retrieved February 9, 2026, from https://www.arcweb.com/industry-best-practices/why-convergence-itot-needs-include-et International Organization for Standardization. (2018). ISO 31000 – Risk management. International Organization for Standardization. (2019). ISO 31010 – Risk management – Risk assessment techniques. Project Management Institute. (2008). A guide to the project management body of knowledge (PMBOK guide) (4th ed.). Project Management Institute. (2017a). A guide to the project management body of knowledge (PMBOK guide) (6th ed.). Project Management Institute. (2017b). The PMI Guide to Business Analysis. Project Management Institute. (2021). A guide to the project management body of knowledge (PMBOK guide) (7th ed.). Project Management Institute. (2025). A guide to the project management body of knowledge (PMBOK guide) (8th ed.). University of Brasília. (2025a). Gpti course plan (2025s) – graduate it project management (ppca/unb) [Internal course material]. University of Brasília. (2025b). Gpti task summary (2025s) – deliverables, capability tables, and evaluation [Internal course material].

8
