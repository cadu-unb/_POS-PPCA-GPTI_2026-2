Contents lists available at ScienceDirect

# Journal of Manufacturing Systems

journal homepage: www.elsevier.com/locate/jmansys

### Technical paper

## A modular Digital Twin architecture for the data-driven reactive planning of disassembly systems<sup>\$</sup>

Lasse Streibel ∗, Tino Schluetter, Stefanie Albers , Finn-Augustin Brunnenkant , Christina Reuter

_Technical University of Munich, TUM School of Engineering and Design, Institute for Machine Tools and Industrial Management, Boltzmannstr. 15, Garching n. Munich, 85748, Germany_

#### A B S T R A C T

#### A R T I C L E I N F O

|_Keywords:_|Disassembly is key to circular production, enabling end-of-life products to be recovered through reuse,|
|---|---|
|Reactive disassembly planning<br>Digital Twin<br>Remanufacturing<br>Circular economy<br>Process planning<br>Scheduling|remanufacturing, or recycling. However, disassembly is characterized by high uncertainty about product con-<br>dition and process feasibility, which requires dynamic, product-specific planning. While predictive disassembly<br>planning anticipates uncertainties, disassembly systems must additionally be able to adapt their plans in real<br>time when deviations occur. This is addressed by Reactive Disassembly Planning (RDP), which enables the<br>dynamic adaptation of disassembly processes and schedules during disassembly. However, unlocking RDP’s<br>full potential requires complex decision-making based on comprehensive real-time data. To support such<br>data-driven RDP, a modular Digital Twin architecture is presented that integrates all decision-making steps<br>into an automated, real-time planning pipeline. The architecture is instantiated and deployed as a Digital<br>Twin in a learning-factory disassembly system to demonstrate the feasibility and end-to-end operation of<br>the proposed modules and connectors. Its potential is illustrated in a representative scenario, in which the<br>instantiated Digital Twin achieves a 78% reduction in lead time and a 2% increase in profit compared to<br>operating without RDP, and a 529% profit increase compared to a rule-based process-termination strategy.<br>These results serve as illustrative proof of applicability, indicating that data-driven RDP via Digital Twins<br>can support efficient, resilient disassembly operations and thereby strengthen the business case for circular<br>factories and the transition to more sustainable production.|

##### 1. Introduction

Sustainable production is among the most cost-effective and successful approaches for achieving economic development while minimizing environmental impacts and improving human well-being [1]. A key solution within sustainable production is circular production, which operationalizes circular-economy principles in production to extend product lifecycles, reduce resource input, and close material loops [2,3]. Circular production also directly addresses critical supplyside risks, including raw-material scarcity, price volatility, and prolonged lead times, while supporting demand-side requirements such as mass customization [4].

Disassembly is a necessary prerequisite for circular production, as it enables end-of-life (EOL) value recovery via practices such as remanufacturing, reuse, or recycling [5,6]. Due to this crucial role, disassembly has become an increasingly important focus of research in recent decades [5,7].

At the same time, disassembly has characteristics that fundamentally differ from those of assembly. First, disassembly is not the simple reverse of assembly. Assembly steps are often not fully reversible and can make disassembly take longer, require additional tools, or even be impossible to perform non-destructively [8]. Second, uncertainty about the condition of components complicates disassembly, as parts are often damaged or corroded, depending on the life cycle of each EOL product [9]. Third, the goal state of disassembly is not predefined, as complete disassembly is technically or economically infeasible in many cases. Therefore, the optimal disassembly level must be determined [9]. These characteristics require disassembly systems to perform individual disassembly processes for each specific EOL product instance. Since disassembly creates less value than assembly, disassembly plans must be carefully evaluated and selected beforehand to ensure economically viable, efficient processes [9,10]. Such _predictive disassembly planning_ anticipates uncertainties in product condition and process parameters [11]. However, due to uncertainty, disassembly systems must also

- \$ This article is part of a Special issue entitled: ‘Towards Circular Factories’ published in Journal of Manufacturing Systems.

- ∗ Corresponding author.

- _E-mail address:_ lasse.streibel@iwb.tum.de (L. Streibel).

https://doi.org/10.1016/j.jmsy.2026.08.013

Available online 10 September 2026

Received 21 March 2026; Received in revised form 23 July 2026; Accepted 30 August 2026

0278-6125/© 2026 The Authors. Published by Elsevier Ltd on behalf of The Society of Manufacturing Engineers. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/by-nc/4.0/ ).

**Fig. 1.** Concept of a reactive disassembly planner [13].

be able to adapt plans when conditions deviate from the initial assumptions of predictive planning, such as defects or missing components. This is achieved through _Reactive Disassembly Planning (RDP)_ , which enables the dynamic adaptation of disassembly plans in response to observed plan deviations [12] (see Fig. 1).

RDP identifies alternative disassembly plans by combining process and schedule adaptations [14]. Process adaptations refer to changes in the disassembly level, the disassembly sequence, and the EOL option for each component [15]. Schedule adaptations refer to controlling the material flow through the disassembly system [14]. Solution alternatives are then evaluated based on their technological feasibility and economic and ecological efficiency. This includes, for example, evaluating all relevant costs and the potential value of the disassembly output, as well as the availability of resources and the utilization of the disassembly system [16]. Due to the specific characteristics of disassembly, conventional production planning methods cannot be applied to RDP [14]. Instead, dedicated data-driven approaches for RDP are seen as promising for optimizing disassembly to be more cost-effective and sustainable [17,18]. However, such data-driven RDP approaches bring new challenges (CHs):

- _CH1:_ RDP involves both process adaptations and schedule adaptations, for which multiple decision-making steps must be executed (Deviation Detection, Identification, Evaluation, and Plan Application). A wide range of data-driven methods is available to support these steps. However, for data-driven RDP, these individual steps and methods must be integrated into a fully automated, end-to-end decision-making pipeline.

- _CH2:_ Data-driven RDP approaches require a virtual representation of the physical disassembly system. This virtual representation must be sufficiently comprehensive in both scope and detail to enable decisions that account for all relevant factors [18].

- _CH3:_ Since decisions in RDP depend on the current state of the disassembly system, the virtual representation must be synchronized with it. At the same time, the decisions made must be communicated back to the disassembly system (see Fig. 1). Data-driven RDP, therefore, requires a bidirectional real-time connection between the physical disassembly system and its virtual representation.

Digital Twins are a smart production technology that directly addresses these challenges. A Digital Twin is defined as the virtual representation of a physical system that is updated through the exchange of information between the physical and virtual systems [19]. This connected structure enables data-driven decision-making based on realtime data about the state of physical systems. While Digital Twins are already widely studied in linear production, concepts for disassembly remain limited. Despite its significant potential to improve disassembly efficiency and, therefore, circular production, no Digital Twins that address CH1–CH3 currently exist. At the same time, the specific characteristics of disassembly hinder the simple transfer of Digital Twins from linear production, as such systems are designed for known products and predefined process goals rather than for planning tasks such as determining the disassembly depth or assigning yields to EOL options during execution. Thus, RDP requires specific Digital Twins to enable automated, data-driven decision-making for its specific planning tasks. For such Digital Twins, a modular architecture is particularly suitable, as RDP comprises multiple planning tasks that can be supported by various data-driven methods and are subject to ongoing research. Such a modular architecture allows individual solution components to be implemented, improved, or replaced without redesigning the entire Digital Twin.

To address this need, this article answers two research questions (RQs):

- RQ1: Which modules are required in a Digital Twin for datadriven RDP?

- RQ2: How can these modules be connected to form a fully automated, end-to-end decision-making pipeline?

Guided by these questions, the article presents a modular Digital Twin architecture for data-driven RDP. The architecture enables an automated, real-time decision-making pipeline that comprises all steps of RDP, from Deviation Detection to Plan Adaptation. This supports targeted future research in RDP and guides practitioners in implementing RDP in industrial disassembly systems. Ultimately, this contributes to making disassembly systems more efficient and resilient, supporting production companies in becoming more circular and sustainable. To achieve these objectives, this article makes the following key contributions:

- The article provides theoretical frameworks for future research on Digital Twins for RDP and combines the general Digital Twin concept by VanDerHorn and Mahadevan [19] with the general concept of RDP by Zussman and Zhou [13]. In doing so, the article addresses calls in the literature to improve the efficiency of disassembly systems and circular production by enabling dynamic, data-driven decision-making to make these systems more reactive [17,20,21].

- The article introduces a novel Digital Twin architecture comprising six modules and six connectors that form a fully automated, data-driven decision-making pipeline for RDP. In contrast to existing research, which addresses single planning tasks (e.g., dynamic scheduling) in isolation or remains theoretical, the architecture provides a flexible platform for integrating various data-driven methods into a comprehensive, reactive disassembly planner connected to physical disassembly systems.

- The architecture is practically implemented and applied in a Learning Factory case study, validating its functionality. Initial application experiments demonstrate that data-driven RDP can increase the efficiency and resilience of disassembly systems.

The article is organized as follows. After this introduction in Section 1, related work is analyzed in Section 2. In Section 3, the research methodology that was used to design the Digital Twin architecture is described. Next, the Digital Twin architecture is presented in Section 4, including detailed descriptions of the modules and connectors. Afterwards, the validation of the architecture within a case study is described and discussed in Section 5. Finally, Section 6 concludes this article and presents future research perspectives.

##### 2. Related work

Before reviewing the literature, four related terms used throughout this article are briefly clarified. _Process-based_ and _schedule-based_ describe how a specific element of an RDP approach (e.g., a solution identification or evaluation method) is implemented, i.e., whether it operates on the disassembly process or on the schedule. _Process-oriented_ and _scheduling-oriented_ describe the overall focus of an RDP approach when one of the two dimensions is dominant, while the approach may nonetheless include elements of both.

**Fig. 2.** Categorization of RDP approaches.

##### 2.1. Data-driven RDP

Data-driven RDP approaches can be distinguished from experiencebased ones, which rely on the implicit and subjective knowledge of humans [22,23]. Additionally, data-driven RDP approaches can be categorized according to the extent to which they consider process and schedule adaptations. Fig. 2 shows this categorization, which is used for orientation in the following sections. In this context, _explicit_ adaptations result from deliberate RDP mechanisms that determine an adapted disassembly plan from a solution space in response to a deviation. _Implicit_ adaptations, in contrast, refer to predefined reactions that follow fixed rules.

The majority of existing approaches address either process or schedule adaptations in isolation. Research on _process adaptations_ remains scarce. Laili et al. [24] address the reprogramming of robotic disassembly processes in the case of unexpected deviations. They employ a matrix-based interference model, along with Bee Colony Optimization (BCO), to explicitly adapt the disassembly sequence, which is one part of _Reactive Disassembly Process Planning (RDPP)_ . Zussman and Zhou [13], Gao et al. [25], and Ren et al. [26] all rely on disassembly Petri nets (DPNs) on which they apply analytical search algorithms, fuzzy reasoning, or reinforcement learning (RL) for _RDPP_ . They additionally consider the assignment of EOL options. All three design their methods to be connected with disassembly systems, but do not discuss the required architectures in detail. In contrast to RDPP, predictive disassembly process planning (DPP), especially its sub-discipline, disassembly sequence planning, is a highly active field of research [7]. While it does not account for initial conditions based on real-time data or the need for fast computation, the problem statement and methods of DPP are similar to those used in RDPP. A wide range of heuristic approaches has been proposed to optimize disassembly sequences under constraints such as tool changes, part dependencies, operational costs, and environmental objectives. Optimization is typically performed using metaheuristics such as Particle Swarm Optimization (PSO) [27], Ant Colony Optimization (ACO) [28], BCO [29], or hybrid methods [30]. Common data modeling methods include DPNs, AND/OR graphs, and hierarchical structures. While graph-based methods dominate in DPP, approaches for RDPP mainly rely on the more comprehensive DPNs [7].

The execution of processes in disassembly systems, and thus scheduling aspects, are neither considered in RDPP nor in DPP.

Research on _schedule adaptations_ focuses on adapting material flows or capacities in response to deviations. Wang et al. [31] present an RLbased _dynamic scheduling_ method for hybrid, multi-station disassembly systems. It reacts to system-level deviations, such as station failures and bottlenecks, and optimizes task allocation across workstations while dynamically adjusting the number of active manual workstations. Li et al. [32] present a decomposition-based multi-objective RL method for _dynamic scheduling_ . The approach reacts to uncertain processing times and worker absences by iteratively fitting reward-weight configurations. The optimization balances lead-time minimization and energy-consumption reduction. Process adaptations are not considered in these approaches, as the disassembly processes are assumed to be predetermined and fixed.

Following the idea that integrated process planning and scheduling is superior to isolated decision-making [33], selected publications aim for integrating process and schedule adaptations. Hrdina [17] proposes a _process-oriented RDP_ approach for manual, work-sharing disassembly systems. The approach aims to execute a predefined disassembly order program as economically as possible under stochastic disassembly conditions. The system is controlled at the station level, where, for each remaining cycle time, all feasible disassembly processes are generated in a decision tree. All alternatives are evaluated, and the one with the highest expected economic profit is selected. This is then communicated to the disassembly system as updated work instructions. The approach focuses on adapting process plans at the station level. System aspects, such as scheduling, are considered implicitly, while an implementation architecture is identified as a potential area for future research. Streibel et al. [34] propose a data-driven approach for RDP. Deviations are formalized as problems derived from the current state of the disassembly system. Solution alternatives, comprising both process and schedule adaptations, are then generated through a structured procedure that involves identification, simulation-based evaluation, and selection based on economic and environmental metrics. To enhance responsiveness for recurring deviations, problem–solution pairs are stored in a case base, enabling their reuse through case-based reasoning. While the contribution aims for _integrated RDP_ , it focuses on the methodological design of the planning approach and does not include a system architecture for its implementation. Wurster et al. [35] propose a _scheduling-oriented RDP_ approach for disassembly systems that include both manual and autonomous workstations and are modeled as a flexible job shop. Using RL, the system aims to handle deviations in product types and conditions, as well as station failures. An RL agent based on a DPN selects disassembly steps and assigns stations. While the approach involves selecting process steps, it does so implicitly, using rules that consider station skills, precedence, and product condition, until complete disassembly is achieved. Determining the disassembly level and assigning yields to EOL options are not addressed.

In summary, publications on RDP remain scarce compared to those on predictive disassembly planning, despite the literature recognizing its potential. Most publications either address reactive process planning or schedule adaptations in isolation, focusing on the underlying algorithms. While first integrated approaches were proposed, they remain limited and do not provide overarching architectures for implementing and integrating multiple data-driven methods into a comprehensive decision-making pipeline.

##### 2.2. Digital Twins for disassembly systems

Research on _Digital Twins for disassembly systems_ has remained relatively rare compared to the extensive research on Digital Twins in manufacturing [36], but has received increasing attention in recent years. Mouflih et al. [37] propose a knowledge-based Digital Twin for the sustainability evaluation and selection of disassembly plans in the incoming inspection of EOL products. While the framework incorporates product lifecycle data and initial inspection results, it does not address reactive planning. Dvorak et al. [38] present a conceptual framework for digital-twin-based disassembly scheduling. The framework aims to account for individual worker skills and product conditions. It comprises initial concepts for modules related to a data model, a solver, simulation, and learning. The modules focus on human behavior, for example, by simulating worker fatigue, but remain abstract. No detailed architecture for implementation is described. The decision support remains limited to task allocation as one aspect of dynamic scheduling. Jiao et al. [39] propose a cloud platform framework based on a Digital Twin that addresses disassembly scheduling. The framework includes data interconnections to detect schedulingrelated deviations and performs simulation-based dynamic scheduling if an impact threshold is exceeded. Similar to Dvorak et al. [38], the modules remain abstract and limited to dynamic scheduling. Rocca et al. [40] present a laboratory application case study that demonstrates how technology, such as simulation models acting as Digital Twins, can support disassembly systems. The case study includes real-time data exchange with a physical disassembly line and terminates orders in response to quality deviations. However, this rule-based schedule adaptation is limited to a single type of deviation with a predefined response.

Besides these Digital Twins for disassembly systems, there are _Digital Twins for remanufacturing and recycling systems_ , which include disassembly as a single process step within the respective systems. Kerin et al. [41] present a generic asset model for implementing product Digital Twins in remanufacturing. Functional requirements for a product Digital Twin are derived, and a Unified Modeling Language (UML) model is proposed. While the model is implemented as a Digital Twin in an exemplary use case, the implementation focuses on predicting product condition. Goodall et al. [42] present a real-time simulation framework for operational and tactical decision support in remanufacturing. The framework comprises an adaptive simulation model, a unified information model for product, process, and resource data, and a data integration service layer. The approach focuses on what-if analyses and does not include a virtual-to-physical connection or the real-time generation and selection of plan adaptations. Li et al. [43] design a Digital Twin architecture for electronics recycling workshops that models different recycling processes, including disassembly, as separate Digital Twins. While disassembly-related process and planning optimization are mentioned, the corresponding modules are not further elaborated on.

The analysis shows that the first Digital Twins for disassembly systems are emerging. Unlike Digital Twins for remanufacturing and recycling systems, Digital Twins for disassembly systems address the complexity of disassembly systems, including divergent, instance-specific material flows involving various EOL options. Currently, however, these Digital Twins are limited to predictive planning or schedule adaptations. In addition, they are either tailored solutions for specific use cases or general concepts without clearly specified interfaces for integrating RDP methods. There is no modular Digital Twin architecture that supports all aspects of data-driven RDP and is compatible with the variety of available methods.

##### 2.3. Conclusion of related work

Based on the descriptions and analyses in the aforementioned literature, Digital Twins are playing an increasingly important role in supporting decision-making in disassembly. The potential for RDP, however, remains untapped.

Regarding CH1, existing RDP approaches employ a wide range of methods, each specifically addressing either RDPP or dynamic scheduling. Integrated approaches remain rare and currently either simplify certain aspects or remain methodological. Existing works on Digital Twins for disassembly also do not integrate the full decision-making pipeline of RDP, but focus on schedule adaptations.

To address CH2, a wide range of data modeling methods exists for disassembly planning. Research on RDP mostly relies on Petri nets. However, the exact scope and level of detail depend on whether the approach is centered on process planning, schedule adaptations, or both. The same applies to computation models. Common methods in existing research include RL, metaheuristics, mathematical programming, and simulation. Again, the exact scope and level of detail of the computations depend on the approach’s individual focus. Digital Twins for disassembly enable virtual representation by connecting such models, but do not yet address RDP.

Finally, existing work on RDP does not address CH3. While some publications mention the need to integrate methods with disassembly systems, they remain vague and limited to single aspects of RDP. Methods are validated using simulation models or theoretical examples, but are not bidirectionally connected to physical disassembly systems in real time. In contrast, existing works on Digital Twins for disassembly address this connection but either concentrate on schedule adaptations, incoming inspection, or implementation details of specific use cases. No approach aims to support RDP in total, considering both process and schedule adaptations.

Synthesizing the state of research on addressing CH1 to CH3, the following research deficits (RDs) can be derived:

- _Integration of RDP methods into a combined, real-time capable and fully automated decision-making pipeline (RD1):_ RDP requires a real-time decision-making pipeline that detects deviations, generates alternative disassembly plans, evaluates these alternatives, and applies the most suitable one to the disassembly system. Existing research addresses individual steps of this pipeline in isolation, offering a variety of methods. The first partially integrated approaches exist, but either remain methodological or rely on simplifying assumptions that limit applicability.

- _Design of a modular Digital Twin architecture as a platform for RDP (RD2):_ The implementation of data-driven RDP requires a Digital Twin as the system’s virtual representation. This representation must be sufficiently comprehensive, bidirectionally synchronized in real time, and capable of implementing the complete RDP decision-making pipeline. Existing research on Digital Twins for disassembly remains limited to supporting only specific aspects of RDP. As a result, no existing Digital Twin architecture can comprehensively implement RDP through flexibly integrating variations of existing data-driven methods.

To unlock the potential of data-driven RDP and enhance the efficiency of disassembly systems, a modular Digital Twin architecture is necessary to enable an end-to-end decision-making pipeline. The required modular architecture is not realized in existing research. Due to the inherent characteristics of disassembly systems, it is also not transferable from linear production. Consequently, a dedicated, modular Digital Twin architecture must be designed to enable the implementation of data-driven RDP in physical disassembly systems.

##### 3. Research methodology

The research methodology followed the procedure for implementing Digital Twins, as outlined by VanDerHorn and Mahadevan [19]. This framework was selected for its established, literature-based definition of Digital Twins and its integrated implementation methodology, which ensures consistency between the conceptual design and practical application. At the same time, the Digital Twin definition is compatible with other classifications, such as by Kritzinger et al. [44]. The procedure comprises the four steps of _Outcome Identification_ , _Scope Definition_ , _Virtual Representation_ , and _Data Interconnection_ . The following summarizes the rationale and intermediate results for each step. By executing all steps, the overall modular Digital Twin architecture was designed, which is described in detail in Section 4.

The first step, _Outcome Identification_ , defines measurable, quantifiable, targeted outcomes for the Digital Twin. This allows the value proposition of a Digital Twin to be defined by its ability to drive positive change toward the targeted outcome [19]. From the motivation of RDP, the following intended outcomes were derived:

- _Increasing the efficiency of disassembly systems:_ This objective is achieved by maximizing the value retention of components and minimizing non-value-adding activities through the optimal tailoring of disassembly plans to each individual product instance based on real-time data.

- _Enhancing the resilience of disassembly systems:_ This objective is achieved by minimizing the number of disassembly processes that become infeasible due to deviations from the initial disassembly plan by allowing the system to return to a feasible and efficient disassembly plan in a timely manner.

Through the _Scope Definition_ of the Digital Twin in the second step, both the portion of the physical reality to be represented and the appropriate level of abstraction are specified. In line with the objective of supporting RDP, the physical reality was defined as the internal disassembly system at the workstation and operation level [18], which comprises disassembly stations, intra-factory logistics, and buffers [14, 45]. External interfaces such as procurement, inbound logistics, and downstream remanufacturing or recycling were treated as boundary conditions [14,45]. From a decision-making perspective, the scope was defined by the RDP problem space. This comprises both the problems (deviations from the disassembly plan) and the measures that can be taken to address the problems (adapting the disassembly plan). During disassembly, deviations can be product-, process-, or resourcerelated [18]. Product-related deviations encompass deviations in product or component conditions, as well as deviations in product structures, including the type, number, and hierarchy of their components. Process-related deviations refer to deviations in yields, including their type, number, and condition, as well as deviations in feasibility or duration. Finally, resource-related deviations refer to deviations in the availability of resources, including personnel, equipment, and tools [18]. The measures available for RDP, according to Hrdina [17], are orderrelated, process-related, or resource-related. Order-related measures include adapting the order sequence or reallocating steps to resources. Process-related measures comprise adapting the disassembly sequence, the disassembly steps, the level of disassembly, or the selection of tools. Finally, resource-related measures include employees supporting each other flexibly and adapting personnel capacity on a short-term basis. However, resource-related measures should be avoided from an organizational perspective and only serve as secondary measures [17].

The third step, _Virtual Representation_ , comprises the design and implementation of data and computational models, as well as visualization. As Section 2 shows, there is extensive prior work on the virtual representation of disassembly systems, including both data models for their description and computational models for decision-making [7]. Therefore, taking into account the objective definition and the system boundaries derived in the preceding steps, the fundamental elements for implementing RDP were identified and abstracted into basic modules of a Digital Twin by mapping them to the framework by VanDerHorn and Mahadevan [19]. These modules were then described in terms of their inputs, processes, and outputs. Additionally, variants for implementation were synthesized from existing literature.

Finally, the _Data Interconnection_ in the fourth step enables the integration of the modules into a decision-making pipeline implemented through a Digital Twin, thereby linking them to the physical disassembly system. In this step, the interfaces between the identified modules were determined. Next, requirements regarding how data is to be collected, the frequency of collection, and how the data is exchanged between the physical and virtual elements were derived following VanDerHorn and Mahadevan [19]. Subsequently, appropriate connectors [46] were developed to implement these requirements, following the design-by-contract principle of Meyer [47].

The modules and connectors that resulted from the described procedure were ultimately combined into the modular architecture and are described in detail in the following section.

##### 4. Digital Twin architecture

Fig. 3 provides an overview of the modular Digital Twin architecture. Using the figure for orientation, Sections 4.1 and 4.2 provide a detailed description of the modules (Ms) and connectors (Cs) that comprise the architecture.

##### 4.1. Modules

The architecture consists of six functional modules (Ms): the Disassembly System (M1), Predictive Data (M2), Data Model (M3), Solution Identification (M4), Solution Selection (M5), and Visualization (M6). Each module is a physical or virtual Digital Twin element that fulfills a specific function by transforming a defined set of inputs into a defined set of outputs, following defined processes. These functional definitions are independent of any specific implementation. Hence, the following sections specify each module in terms of its inputs, processes, outputs, and exemplary implementation variants from existing literature (Fig. 2).

##### 4.1.1. Disassembly system (M1)

_Input:_ Following the definition by Zussman and Zhou [13], a disassembly system that is connected to a reactive disassembly planner receives two main inputs: On the physical level, the system receives EOL products that should be disassembled. On the informational level, it receives disassembly plans and adaptations of those plans from the reactive disassembly planner.

_Process:_ The primary task of the Disassembly System is to take EOL products and process them by performing disassembly steps [13]. To perform this task, disassembly systems comprise multiple disassembly stations, intra-factory logistics, and buffers (see Section 3). From the perspective of RDP, the Disassembly System has two additional tasks. First, it observes the products, processes, and resources in the system. Second, it translates disassembly plans and their adaptations into actions.

_Output:_ On a physical level, the outputs of the Disassembly System are reusable parts, secondary materials, and waste. Additionally, on an informational level, the system must provide its observations to RDP [13].

_Implementation:_ In practice, disassembly systems can be implemented in many different forms, ranging from single-person, fixed-location disassembly systems to work-sharing configurations such as disassembly lines or flexible job shops [17,48]. While work-sharing structures can improve the economic efficiency of disassembly, they impose higher requirements on planning and control [17]. Accordingly, single-person, fixed-location disassembly systems may only require process adaptations, whereas in flexible job shops, schedule adaptations become relevant. Although the modular Digital Twin architecture can be applied to all of these system types, the specific design of the individual planning modules must be aligned with the requirements of the respective disassembly system. Finally, disassembly systems vary in their degree of automation. Manual disassembly systems still dominate, but semi-automatic and, in some domains, even mostly automated disassembly systems already exist [49]. While Visualization plays a crucial role in communicating with human workers (see Section 4.1.6), connecting RDP to robot-level control layers becomes relevant in mostly automated systems. Similarly, the degree of automation affects the design of connectors, i.e., C2 and C6.

**Fig. 3.** Overview of the modular Digital Twin architecture, comprising modules (Ms) and connectors (Cs)

##### 4.1.2. Predictive Data (M2)

_Input:_ Predictive Data is obtained from various heterogeneous inputs that provide disassembly information on products, processes, resources, and orders. This includes product design (e.g., bill of materials), longterm and short-term predictive disassembly planning (e.g., factory layout and process plans), product lifecycles (e.g., expected product conditions), and markets (e.g., EOL values of components) [16,23]. In this context, predictive means that the data is determined a priori and independently of a specific EOL product instance [16,50].

_Process:_ The module collects heterogeneous inputs and transforms them into a standardized, structured, and machine-readable format that captures predictive information across the relevant dimensions. Predictive Data represents assumptions about a given disassembly process and is distinguished from real-time data collected from the Disassembly System, which reflects actual observations. Over time, however, Predictive Data may change, e.g., by updating predictions based on observations, resulting in a learning Digital Twin [50,51]. While the data requirements of a Digital Twin depend on its use case-specific outcome [19], the general information requirements of RDP can be divided into the four dimensions of products, processes, resources, and orders [7,18]. For products, their general condition as well as the condition, type, hierarchy, and count of their components and any achievable subassemblies must be provided. Processes must be defined in terms of their yields (condition, type, and count), their steps (feasibility, duration, count, type, and sequence), their tools (allowed and selected tools), and their assignment to stations. This applies not only to the selected but also to all feasible processes [52], so that a solution space can be provided to RDP. Resources comprise stations, workers, and tools, which must each be defined in terms of their counts, capabilities (e.g., performable steps and buffer capacities), availabilities, and interrelationships (e.g., allowed material flows and transport distances). Finally, information on orders and their planning and control must be provided. Orders must be described by their counts, types, and sequences. In addition, material flow control rules (e.g., push or pull principles), logistics logic (e.g., on request or periodically), scheduling logic (e.g., fixed schedule or flexible), objective functions (e.g., maximize profit or minimize cost), and optimization parameters (e.g., runtime limits) must describe how orders are planned and controlled. Depending on the objective function and the design of other modules (i.e., M4 and M5), additional evaluation data may be required, such as energy consumption, material content, or CO2 footprints.

_Output:_ The output of the module is a set of data structures, providing predictive information on products, processes, resources, and orders in a machine-readable way.

_Implementation:_ The implementation of collecting and transforming Predictive Data strongly depends on the specific use case. Since manually collecting heterogeneous data sources is time-consuming, recent developments in knowledge graphs and large language models are promising for automating this process [53]. For structuring the data, methods should be selected to cover the required information while ensuring compatibility with the methods used within the Data Model and the computational models of the Digital Twin [7]. This could include, for example, providing liaison diagrams and hypergraphs in addition to bills of materials, as they can both model product structure and be converted into Petri nets that facilitate process modeling and planning [54].

##### 4.1.3. Data Model (M3)

_Input:_ The Data Model receives Predictive Data from M2 and realtime data from M1 as input.

_Process:_ The Data Model retains all variables that describe the current, and if necessary, also historical states, of the Disassembly System at the chosen level of abstraction [19]. While it must cover the same information requirements as M2, it differs in that it is realtime-synchronized with the Disassembly System through continuous integration of observations. Hence, it describes specific product, process, resource, and order instances derived from the Predictive Data. From a product perspective, this includes the actual observed condition, type, hierarchy, count, and location of components for specific parts, whether complete products, subassemblies, or individual components,

###### L. Streibel et al.

that are present in the Disassembly System. For all ongoing processes within the Disassembly System, their already retrieved and still expected yields (condition, type, and count), their already completed and still planned steps (feasibility, duration, count, type, and sequence), their currently used and still planned tools (allowed and selected tools), their current and planned assignment to stations, and the alternatively feasible processes must be represented. In addition to their Predictive Data, all resources within the Disassembly System must be represented by their current state, e.g., capability and availability. Finally, the Predictive Data on orders must be enriched with the current counts, types, sequences, and progress of orders, as well as their links to specific instances, such as parts, present in the Disassembly System [55].

_Output:_ The output of the module is a synchronized, virtual representation of the current state of the Disassembly System, retaining all variables that are required for a given use case.

_Implementation:_ For modeling disassembly systems, a wide range of established graph-based, matrix-based, Petri-net-based, and other methods exists, each differing in its scope and focus [7]. While methods can be flexibly combined to cover all required information [55], consistency must be ensured between the Predictive Data, the Data Model, and the computational models. For example, when using Petri-netbased algorithms for RDPP, processes should also be planned and modeled as Petri nets [52]. In existing literature, Petri-net-based methods dominate for data modeling in RDP [7]. However, approaches based on knowledge graphs receive increasing attention and may provide an alternative in the future [7,53].

##### 4.1.4. Solution Identification (M4)

_Input:_ The Solution Identification module receives a Problem Description that represents the current state of the Disassembly System, including the currently valid disassembly plan and the triggering deviation, as input from C4.

_Process:_ Based on the Problem Description, the module identifies one or multiple solution alternatives in response to a deviation by applying RDP measures to the current disassembly plan. These solution alternatives correspond to adapted disassembly plans that restore feasibility and aim to improve performance in the face of the given deviation. Depending on the RDP approach, Solution Identification can be processbased, schedule-based, or integrated (see Fig. 4). Process-based Solution Identification involves applying process-related measures, i.e., adapting the disassembly sequence, the type of disassembly steps, the level of disassembly, or the selection of tools. The original schedule is maintained. Schedule-based Solution Identification applies order-related measures, i.e., adapting the order sequence and reallocating disassembly steps to available resources. The original disassembly process is maintained. Integrated approaches combine both process-based and schedule-based measures [33].

_Output:_ The output of the module is one or multiple Solution Descriptions. Depending on the RDP approach, a Solution Description comprises either an adapted disassembly process plan for the affected order, an adapted schedule for the Disassembly System, or both. In addition, information can be provided to M6 to visualize the Solution Identification process or its output.

_Implementation:_ Depending on the type, various methods exist for implementing Solution Identification (see Table 1).

##### 4.1.5. Solution Selection (M5)

_Input:_ The Solution Selection module receives a set of alternative Solution Descriptions as input from M4, as well as the Problem Description and use case-specific evaluation data, including evaluation criteria, from C4. Evaluation data in this context may comprise single-criterion (e.g., maximizing profit) or weighted, multi-criteria objective functions (e.g., maximizing profit (70%) while minimizing lead time (30%)), as well as data on these criteria (e.g., cost rates and market prices).

_Process:_ The module selects the most suitable solution alternative for a given Problem Description by evaluating all available alternatives

**Fig. 4.** Design of Solution Identification (M4) and Solution Selection (M5) depending on the RDP approach.

**Table 1**

Examples of methods for Solution Identification (M4).

|Approach|Methods|
|---|---|
|Schedule-based|Rule-based [40]|
||RL [31,32]|
||Exact analytical [13,17]|
|Process-based|RL [26]|
||Fuzzy reasoning [25]|
||Metaheuristics [24]|
|Integrated|RL [35]<br>Case-based reasoning [34]|

_Note_ : Methods are classified according to the type of measures applied, as defined in Section 4.1.4.

using use case-specific criteria and the corresponding evaluation data. Matching the approach chosen for M4, Solution Selection can be performed in a process-based, schedule-based, or integrated manner (see Fig. 4). Process-based solution evaluation is applied after process-based Solution Identification. It evaluates process plans using process-related criteria such as disassembly time [56], disassembly profit [16], or energy consumption [57]. Schedule-based solution evaluation is applied after schedule-based Solution Identification. It evaluates schedules using resource-related criteria such as utilization [31], job completion time [32], or resource costs [35]. Integrated evaluation is required after integrated Solution Identification, and can also be applied after non-integrated Solution Identification to achieve more integrated decision-making. It evaluates solution alternatives holistically, considering their impact on the process and schedule, for example, by assessing the overall performance of the Disassembly System.

_Output:_ The outputs of the solution evaluation module are the evaluation results of the alternative Solution Descriptions, along with the selection of one of those alternatives. While the evaluation results can be used for learning, e.g., in M3–M5, the selected alternative is provided to C6 for application to the Disassembly System. Additionally, information can be provided to M6 to visualize the Solution Selection process or its output, e.g., evaluation results.

**Table 2**

Examples of methods for Solution Selection (M5).

|Approach|Methods|
|---|---|
|Schedule-based|RL internal [31,32,35]<br>Simulation [38–40]|
|Process-based|Analytical value-based [13,17]<br>RL internal [26]<br>Fuzzy reasoning [25]<br>Activity-based costing [58]|
|Integrated|Simulation [42,43,59]<br>Case similarity [34]|

_Note_ : Methods are classified according to the type of measures applied, as defined in Section 4.1.5.

_Implementation:_ Depending on the type, various methods exist for implementing Solution Selection (see Table 2).

##### 4.1.6. Visualization (M6)

_Input:_ Visualization provides decision-makers with a clear interpretation of data to increase confidence in decisions. Most often, visualization in Digital Twins uses the data in the Data Model as input [19]. However, data from computational models in M4 and M5 can also be visualized to improve transparency of the RDP decision-making process. Additionally, when implemented in manual or semi-automated disassembly systems, visualization plays a crucial role within humanmachine interfaces [17]. There, input is either data supporting the collection of observations or adapted disassembly plans resulting from RDP.

_Process:_ When using the Data Model as input, Visualization transforms data into visual representations, such as trend or distribution charts, that show the general behavior of the Disassembly System. In the physical-to-virtual direction of human-machine interfaces, Visualization supports humans in translating their observations into data [60]. In the virtual-to-physical direction, Visualization communicates the currently valid disassembly plan, including any adaptations made by RDP, back to the human [60].

_Output:_ In general, the output of Visualization is information in visual, easily interpretable representations that improve the acceptance and value of the Digital Twin [19]. When visualizing the Data Model, the focus is on creating transparency regarding the behavior of the Disassembly System, supporting learning and long-term decision-making. For human-machine interfaces, the output of Visualization should be effective and efficient communication between humans and the Digital Twin.

_Implementation:_ Besides general approaches, such as dashboards, process mining has received recent attention for improving the transparency of disassembly systems through process visualization and exploration [60–62]. For human-machine interfaces, touchscreens or augmented reality can support the collection of user input on observations by displaying inspection instructions. Such means can guide users with reference cases or provide feedback on how to provide data. The communication of adapted disassembly plans can be supported visually, for example, by enriching the plan with three-dimensional drawings, reference images, or selective highlighting of plan adaptations [60].

##### 4.2. Connectors

The six modules are integrated to form a decision-making pipeline via six connectors (Cs): Initialization (C1), Observation (C2), Deviation Detection (C3), Problem Description (C4), Solution Description (C5), and Plan Adaptation (C6). Each connector serves as an interface. It receives a defined set of inputs from preceding modules or connectors, transforms them through specified processes, and provides the resulting outputs to subsequent modules or connectors. The following sections specify the connectors in terms of their inputs, processes, and outputs.

Where available, exemplary implementation variants from existing literature are presented. Otherwise, novel implementation concepts are presented.

##### 4.2.1. Initialization (C1)

_Input:_ The Initialization connector takes the set of data structures provided by M2 as input.

_Process:_ The connector parses the inputs, transforms them into the format required by the respective data modeling methods used in M3, and initializes these data modeling methods with the Predictive Data. At the Digital Twin’s startup, this is done to initialize the overall Data Model, e.g., instantiating all resources in the Disassembly System with their general information, such as capabilities and layout. Additionally, new instances in the Data Model must be initialized each time they are created, i.e., new order, product, and process instances whenever a new order is created.

_Output:_ The outputs of the connector are instances within M3 that are initialized with Predictive Data, e.g., a product instance with its predicted bill of materials.

_Implementation:_ The implementation depends on the specific data structures used in M2 and the data modeling methods used in M3. For example, Tang et al. [52] use multiple Petri nets in M3, which are initialized each time a new product arrives in the incoming inspection. Streibel et al. [55] combine Petri nets with other data modeling methods in M3. Resource data is initialized once from a semi-structured file containing data on the Disassembly System to instantiate the resource model. Predictive Data on products and processes is initialized repeatedly from multiple data structures, e.g., a Process Plan Colored Timed Petri Net adapted from Tang [63], whenever a new order is received. For Digital Twins that rely on knowledge graph-based data models, Initialization includes knowledge graph creation and data enrichment [53].

##### 4.2.2. Observation (C2)

_Input:_ As input, the connector receives observations from M1 regarding part identification, part inspection, location and timestamp tracking, as well as additional user input [60].

_Process:_ The connector provides the physical-to-virtual data interconnection, continuously synchronizing M3 with M1. Observations from M1 are collected as data, which is then structured to enable further processing. Each new observation is compared to the current information in M3. When a new observation deviates from the current information in M3, M3 is updated with the new information.

_Output:_ The output of this connector is twofold. The first output consists of instances within M3 that are continuously synchronized with the state of the physical Disassembly System. Second, a stream of structured data describing any updates in M3 is provided to C3 for Deviation Detection.

_Implementation:_ The design of this connector combines the architecture for integrating real-time data into Digital Twins for RDP by Streibel et al. [60] with the synchronization module presented by Streibel et al. [55]. This results in an event-driven publish–subscribe approach [64], where a database acts as a broker between the publisher M1 and the subscriber M3 (see Fig. 5). Depending on the level of digitization in M1, input data collection can be implemented through manual entry via human-machine interfaces, automated methods such as sensor measurements, or a combination of both. Various technologies are available for this purpose, both in linear production [65] and in disassembly systems [60]. For data structuring, a central database stores data as multiple event logs: The order event log records the Initialization and attributes of disassembly orders [60]. The material flow event log records the movement of parts between resources, as well as the creation and disappearance of parts resulting from the execution of disassembly steps [66]. The product event log records product- and part-specific observations during disassembly, e.g., damaged or missing components. The process event log records the start and completion of disassembly steps, including their inputs and yields. Finally, the resource event log records resource-related events such as changes in availability [60]. On each new entry, the database sends standardized data packages describing the observed event to the synchronization module [55]. Based on the content of a data package, the synchronization module categorizes it as an order event, material flow event, product event, process event, or resource event. Depending on the categorization, the data is passed to a corresponding algorithm, referred to as an event handler [55]. The event handlers process the data and, if it deviates from the current data in M3, apply each event to the corresponding part of M3. For instance, a material flow event handler may process entry and exit events at specific resources to update the location attribute of part entities. A process event handler may dynamically remove a branch from an EPN if a subassembly is reported as missing [55]. The specific design of the event handlers depends on the data modeling methods used in M3. Whenever an update is applied to M3, the responsible event handler sends a primitive event [67] to C3. This event describes a single update in M3 and includes metadata such as an event type and a timestamp, along with a payload containing the specific change data.

**Fig. 5.** Design of the Observation connector (C2)

##### 4.2.3. Deviation Detection (C3)

_Input:_ The input for the Deviation Detection consists of the stream of primitive events generated by C2.

_Process:_ The connector serves as the triggering logic, determining whether an update to M3 is a deviation that requires RDP. It continuously screens the stream of primitive events for patterns that represent a deviation. For this pattern recognition, it must consider use-casespecific thresholds, since not every deviation should trigger RDP in every use case.

_Output:_ The output of this connector is a trigger signal that initiates the RDP decision-making pipeline of M4 and M5.

_Implementation:_ The connector is implemented through a complex event processing (CEP) engine [68], which is shown in Fig. 6. To process primitive events, the CEP engine uses an event pattern catalog, which serves as the system’s rule base. This catalog categorizes deviations and maps them to digital triggers using logical operators such as sequences, aggregations, thresholds, or negations. The catalog must be initialized for each application, depending on the specific requirements that should trigger RDP. For product-related deviations, this could include a deviation in component condition that surpasses certain quality thresholds or impacts the feasible EOL options. Such a deviation could be recognized by a primitive event _ComponentConditionChanged_ whose metadata value for the observed condition surpasses the defined thresholds. For process-related deviations, exceeding the maximum defined processing time in a disassembly step can be detected from the time difference between the primitive events _ProcessStepStart_ and _ProcessStepEnd_ . As a third example, resource-related deviations, such as resources becoming unavailable, could trigger RDP when a primitive event _ResourceAvailabilityChanged_ is recognized for a resource that is currently assigned to an ongoing disassembly plan. The event pattern catalog can be continuously extended and adjusted based on experience and collected data, enabling the Digital Twin to learn.

Upon detecting a match between the incoming event stream and one of the defined patterns, the CEP engine creates a higher-level _Complex Event_ . This complex event describes the occurrence of a deviation, the affected orders for which RDP should be performed, and, optionally, additional details on the deviation. It is provided to M4 and M5 to trigger the specific decision-making processes, depending on the implementation of these modules.

##### 4.2.4. Problem description (C4)

_Input:_ The connector receives two inputs. First, it receives a complex event from C3, which triggers a new RDP decision-making process. Second, it retrieves data from M3.

_Process:_ The connector provides the data required for the RDP decision-making processes in M4 and M5. Therefore, it creates a snapshot of all relevant data from M3 at the moment RDP is triggered. This ensures data consistency throughout the decision-making process, preventing race conditions when M3 is updated during an ongoing process. From this snapshot, the connector derives and transforms data into the specific formats required by the methods used to implement M4 and M5.

_Output:_ The output is a structured, machine-readable Problem Description that is a decoupled snapshot of all relevant data included in M3 on the state of M1 at the point in time when the RDP process was triggered. This output is provided to M4 and M5 in the required format.

_Implementation:_ The implementation of the connector depends on the design and implementation of M3–M5.

Using process-based M4, implemented as a Petri net-based metaheuristic, and M3, including corresponding Petri nets, as an example, C4 could provide a snapshot of the Petri net of the affected order to M4. This would provide process information, including current progress, feasible next steps, and step attributes such as processing times. At the same time, for integrated M5, implemented as a simulation, additional data would be transformed into a simulation configuration file and provided to M5. This could include current parts and their physical locations, resource availability, and external evaluation data such as market prices and energy consumption.

**Fig. 6.** Design of the Deviation Detection connector (C3)

##### 4.2.5. Solution description (C5)

_Input:_ The input for this connector is one or multiple Solution Descriptions provided by M4.

_Process:_ The connector serves as the bridge between M4 and M5, handing over the identified set of solution alternatives for subsequent evaluation. Each solution alternative represents an adapted disassembly plan to address the detected deviation.

_Output:_ The output of the connector is a set of alternative Solution Descriptions that is passed to M5. Depending on the RDP approach, a Solution Description comprises either an adapted disassembly process plan for the affected order, an adapted schedule for the Disassembly System, or both.

_Implementation:_ The implementation of the connector depends on the design and implementation of M4 and M5. Taking process-based M4 and integrated M5 as an example, the connector could provide a set of alternative disassembly process plans, each comprising a feasible sequence of disassembly steps for the affected order, to M5 for subsequent evaluation and selection.

##### 4.2.6. Plan adaptation (C6)

_Input:_ The input for this connector is one selected solution alternative that is provided by M5 and linked to a corresponding Problem Description.

_Process:_ The connector applies the selected solution to M1 and M3, thereby closing the RDP decision-making loop. For updating M3, the connector first archives the obsolete plan, along with the Problem Description and the RDP results, into an immutable history log to enable state monitoring [19]. Afterwards, the connector updates M3 to incorporate the adapted plan. Additionally, the adapted plan is applied and communicated to M1.

_Output:_ The outputs of the connector are an updated M3 that considers the Plan Adaptations and the communication of the adapted disassembly plan to M1, enabling M1 to follow this adapted plan.

_Implementation:_ The specific implementation of the connector depends on the interface available for receiving adapted disassembly plans in M1. While in manual or semi-automatic disassembly systems, Plan Adaptations must be translated into work instructions or visualizations (see M6). In automatic systems, translation into robotic control sequences may be required. Additionally, the information that must be communicated (i.e., process adaptations, schedule adaptations, or both) depends on the RDP approach. Streibel et al. [60] use a database table, referred to as the work instruction queue, to implement Plan Adaptation and communication for RDP. This table contains entries for all disassembly steps to be performed by the resources, based on the current orders in the Disassembly System. It is accessed by all resources in the Disassembly System. Entries can be reserved and removed by resources when they are completed, while new steps can be added, e.g., by the incoming inspection when new orders are created. Utilizing this architecture, the connector can apply and communicate Plan Adaptations by manipulating the work instruction queue. This includes adding entries (e.g., when disassembling a subassembly originally planned for reuse), removing entries (e.g., not disassembling a component that is damaged), and changing entries (e.g., assigning a step to a different resource when the original one has become unavailable). In addition, the work instruction queue allows for temporarily locking entries affected by ongoing RDP to prevent resources from working on them before an RDP decision is made.

##### 5. Case study

To validate the architecture, it was practically implemented and applied as a Digital Twin for process-oriented RDP in the _Smart Production Lab_ of the Institute for Machine Tools and Industrial Management at the Technical University of Munich. The Smart Production Lab provides a Learning Factory environment [69] including a disassembly use case specifically designed for research validation [70]. Part of this use case is a remote-controlled car with 55 components, serving as the representative EOL product and allowing the creation of 160 different product instances.

Section 5.1 describes how the architecture was implemented, using the presented connectors and one exemplary design for each module. Afterwards, Section 5.2 describes an initial application study conducted to gain insights into the potential efficiency gains from data-driven RDP enabled by Digital Twins.

##### 5.1. Implementation

Fig. 7 provides an overview of the implemented Digital Twin, which is described in the following. The physical Disassembly System (M1) comprises one entry station for incoming inspection, five manual disassembly stations, and one warehouse. Each disassembly station has different, defined capabilities to enforce work sharing. The material flow is manual, flexible, and follows the push principle. For yields, the two EOL options _reuse/remanufacturing_ and _recycling_ are distinguished. In addition to an incoming buffer, the actual workbench, and an outgoing buffer, each station has a buffer for each of the two EOL options. Each station is equipped with a digital humanmachine interface running industrial-grade manufacturing execution software from Tulip Interfaces. In addition, the Disassembly System is equipped with a real-time locating system (RTLS) from Kinexon [66]. As Predictive Data (M2), multiple files are provided. A bill of materials, including evaluation data such as expected EOL values and component conditions, is provided as an Excel file for all product instances. A module definition matrix is provided as an Excel file to identify parts based on their components, and vice versa [71]. An Extended Petri Net (EPN) for disassembly as introduced by Brunnenkant et al. [54] contains predictive process data and is provided as a Petri Net Markup Language (PNML) file. Predictive disassembly process plans and corresponding text-based work instructions linked to transitions in the EPN are provided in a PostgreSQL table. Finally, a JavaScript Object Notation (JSON) file containing semi-structured data provides predictive resource data, such as capabilities, cost rates, and buffer sizes.

All virtual elements (M3–M5 and C2–C6) were implemented in Python 3.9 and executed on consumer-grade hardware equipped with an Apple M1 Pro chip and 16 GB of RAM. For M3, the Data Model for RDP Digital Twins presented by Streibel et al. [55] was implemented. The Data Model comprises order, product, part, component, station, process, Petri net, place, token, arc, and transition classes, covering the information requirements of system-level RDP. On startup, the Data Model is initialized (C1) with predictive resource data by instantiating the station class. The other Predictive Data is read repeatedly, either whenever a new order is received (bill of materials and EPN) or whenever components need to be translated into parts or vice versa (module definition matrix). In this case, Initialization is performed by instantiating the order, product, part, component, process, Petri net, place, token, arc, or transition class. For the Observation connector (C2), data is collected both manually via the human-machine interfaces at the stations (e.g., defect components) and automatically via the RTLS (e.g., part location). All data is structured in a PostgreSQL database, which passes updates through a listen-notify connection to a synchronization module. The synchronization module updates M3 through event handlers and provides primitive events as JSON data packages to C3. For C3, a CEP engine was implemented, including a predefined event pattern catalog comprising triggering event patterns such as disassembly steps reported as infeasible, disassembly steps with processing time exceeding the planned duration by more than 30%, or resources becoming unavailable while currently having steps assigned. In addition to sending complex events to C4, a locking mechanism for the human-machine interfaces at the disassembly stations was implemented. To prevent ongoing processes and ensure data consistency during RDP, the steps of the affected order are locked, and a waiting screen is displayed on the stations currently working on it. Upon receiving a triggering complex event from C3, C4 provides a snapshot of M3 as a data transfer object to both M4 and M5, which begin their respective configurations in parallel. For M4, a reactive process planning metaheuristic was implemented for process-based Solution Identification. The metaheuristic operates on the current EPN for the affected order, based on the snapshot provided by C4. It identifies a set of alternative process plans that continue from the current progress and ranks them in a Pareto-based archive. The ten most promising alternatives, based on the heuristic values, are provided to M5 as a data transfer object (C5). M5 is implemented as an integrated Solution Selection, using real-time material flow simulation based on the SimPy framework. Although C4 initiates the simulation configuration based on the provided snapshot, the creation of scenarios awaits the solution alternatives provided by M4. All scenarios are simulated and evaluated based on the simulation data and additional evaluation data included in the snapshot, e.g., EOL values. One solution is selected using normalized index-based aggregation of the indicators _total profit (I1)_ , _lead time (I2)_ , _circularity (I3)_ , and _total utilization time (I4)_ in equal weighting. Circularity is defined as the share of parts assigned to reuse/remanufacturing, while the total utilization time is the sum of all processing times in the system. While the first three indicators represent a process-oriented perspective on the triggering order, the fourth indicator captures the system-wide impact of each implementation strategy. Finally, the Plan Adaptation connector (C6) was implemented as an algorithm that manipulates a work instruction queue table. The connector translates the selected process plan alternative and the resulting material flow from the simulation model into updated work instructions. After this update is successfully committed, the lock caused by C3 is released, triggering an immediate refresh on the human-machine interfaces to display the adapted disassembly plan. In addition to visual elements in the human-machine interfaces, further Visualization was implemented to increase the transparency of the Disassembly System. First, M3 was connected to interactive live dashboards running on Streamlit, providing real-time insights into active orders, utilization, and warehouse inventory. Second, Celonis process mining software was used to create process models and historical processing time distribution charts, supporting exploratory analysis and further increasing transparency.

##### 5.2. Application

The implemented architecture was evaluated through a practical application study comprising various scenarios and a stress test. The scenarios described various initial states of the Disassembly System, in which then all relevant types of deviations were introduced to trigger RDP. The stress test included dedicated scenarios that aimed to maximize computational effort by triggering RDP for multiple orders in parallel, thereby testing the robustness of the architecture.

From the tested scenarios, the following example is highlighted to demonstrate the practical application and the detailed decision-making process triggered by the Digital Twin. In the scenario, three orders were processed simultaneously within the Disassembly System (see Fig. 8, top). Order 2 is a high-quality EOL car, planned to be almost fully disassembled to retrieve components for reuse and remanufacturing. It is currently located at Station S2, where the disassembly of the front axle assembly is reported as infeasible due to a damaged screw through manual entry. After C2 collects event data describing the deviation from Station S2, C3 detects the event as a deviation, triggers RDP for Order 2, and locks all corresponding entries in the work instruction queue. Next, C4 creates a snapshot of M3 that includes all three orders currently in the Disassembly System. Based on this snapshot, M4 explores the EPN of Order 2 starting from its current position. In parallel, M5 configures a simulation environment. Within 5.09 s, M4 generates ten valid alternative process plans that circumvent the infeasible disassembly step and passes them to M5. In M5, one simulation scenario for each alternative is instantiated from the configured simulation environment and run in parallel. After an additional 1.34 s, one solution alternative is selected. Finally, C6 updates the work instruction queue entries for Order 2 with the adapted plan and releases their lock. After a total reaction time of 6.58 s, M1 continues disassembling Order 2 based on the adapted disassembly plan.

The decision made by the implemented Digital Twin was compared with two other levels of RDP implementation (see Fig. 8, bottom). The first implementation _(no RDP)_ proceeds with the original disassembly plan despite any deviations. The disassembly of the front axle assembly is performed despite the observed damaged screw, taking 900 s. Afterwards, the disassembly plan is completed as initially planned. This results in an economic profit of 152.07 e, a lead time of 1245 s, and a circularity of 93.62% for Order 2. The total utilization time of the system is 1935 s, mainly driven by the additional effort required to disassemble the front axle assembly. The resulting prolonged occupancy of Station S2 has significant impacts on the material flow. Order 3 is unable to proceed to Station S2 after completing operations at Station S1, resulting in a system-wide backlog. Downstream, Stations S3–S5 experience idle time because parts are not delivered on time.

The second implementation _(rule-based RDP)_ terminates the disassembly process upon any deviation, similar to the implementation by Rocca et al. [40]. Hence, in the given scenario, the entire chassis is assigned to recycling as a single subassembly. Including the process before the deviation, this results in a total profit of 24.67 e, a total lead time of 107 s, and a circularity of 12.77% for Order 2. The total utilization time of the system is 797 s. While this implementation achieves the shortest lead time and quickly clears Station S2, allowing the material flow to continue, it foregoes the significant value potential of the remaining 51 components of Order 2.

**Fig. 7.** Overview of the implemented Digital Twin for process-oriented RDP.

The third implementation refers to the described Digital Twin for process-oriented RDP, combining explicit process adaptations with implicit schedule adaptations. The adapted plan avoids disassembling the front axle subassembly. Instead, it continues with the disassembly of the rear tires, both suspension subassemblies, and shock absorber components directly from the chassis subassembly. This results in a total profit of 155.19 e, a lead time of 269 s, and a circularity of 85.11% for Order 2. The total utilization time of the system is 959 s. The adapted steps are performed at Stations S3–S5, clearing Station S2 and allowing the material flow to continue. Compared to no RDP, the Digital Twin increases profit by 2% and reduces lead time by 78%, while achieving a 9% lower circularity and a 50% lower utilization time. While the revenue is lower than in the predictive disassembly plan, higher profits are achieved by avoiding the disassembly of the front axle assembly, thereby saving time and labor costs. This makes up for the revenues lost by not disassembling the front axle assembly. Compared to terminating the disassembly process in response to the deviation, the Digital Twin increases profit by 529% and circularity by 466%, while increasing lead time by 151% and utilization time by 20%.

##### 5.3. Discussion

The case study demonstrates that the proposed Digital Twin architecture can be successfully implemented and applied in practice. From an architectural perspective, the case study shows that the architecture successfully addresses the challenges of data-driven RDP. It integrates the individual steps of RDP and existing methods for their implementation into a fully automated, end-to-end decision-making pipeline (CH1). By combining modules that serve as data and computational models explicitly designed for RDP, the architecture provides a virtual representation of the physical Disassembly System that is sufficiently comprehensive in both scope and detail (CH2). Finally, by implementing the presented connectors, a bidirectional, real-time connection between the virtual representation and the physical Disassembly System is established (CH3). From an application perspective, comparing different RDP implementation levels shows that the Digital Twin achieves its intended outcomes in the case study setting. By increasing profits and profits per time unit relative to both other implementations, the efficiency of the case study Disassembly System could be successfully improved. Additionally, the affected order did not have to be terminated, and the Disassembly System remained operational with no significant impact on material flow. This demonstrates how RDP can enhance the resilience of disassembly systems.

##### 5.3.1. Benefits

The presented architecture makes a significant contribution to the state of research by integrating the various existing methods into a structured framework that addresses the entire RDP decision-making process. The architecture defines modules and connectors with clear interfaces and functions, breaking RDP down into distinct subproblems while linking them to existing methods and approaches. This provides a platform for implementing RDP as an integrated system rather than as isolated planning functionalities. In addition, the modular design supports the integration, improvement, or replacement of individual method components as research on data-driven RDP continues to evolve. At the same time, the modular design makes the architecture inherently scalable: individual modules can be deployed independently or distributed across multiple compute nodes, and the data pipeline supports horizontal scaling to handle increased throughput from larger disassembly systems or more complex products. By categorizing different RDP approaches, targeted future research is supported, and practitioners are guided. The case study provides further support for the potential of data-driven RDP to improve the efficiency and resilience of disassembly systems. This is highly relevant to circular production as disassembly is a significant cost driver, and current non-reactive disassembly systems require substantial labor to process products that prove non-reusable. Additionally, data-driven RDP externalizes decision-making from human workers, making decisions less subjective and more transparent, while also helping companies address skilled labor shortages. From an economic perspective, the Learning Factory validation demonstrates that the architecture can be successfully implemented with consumer-grade hardware and a modest initial investment, lowering the barrier to entry for small and medium-sized enterprises (SMEs), which constitute the majority of the disassembly industry.

**Fig. 8.** Practical application.

##### 5.3.2. Limitations

The evaluation scope was restricted to a Learning Factory with a representative but limited set of scenarios, product variants, and event patterns. While the Learning Factory realistically replicates core disassembly operations and process execution, it simplifies several real-world industrial conditions: (1) time pressures are lower due to reduced throughput requirements; (2) operator-related factors such as skill variability and fatigue are not captured; (3) the products are not truly end-of-life, meaning that varying product conditions, wear, and degradation are only modeled rather than physically present; and (4) disassembly steps and tooling are simplified and require significantly shorter execution times than most industrial disassembly operations. The presented comparisons (i.e., no-RDP and a rule-based termination strategy) serve as pragmatic baselines to illustrate system effects, but they do not constitute comprehensive benchmarks and should therefore not be generalized. Beyond these evaluation boundaries, several fundamental limitations affect the proposed architecture. A key limitation is the dependency on data quality. If predictive data is not available in the correct format, creating it can be time-consuming (e.g., process models and knowledge graphs). Inaccuracies or incompleteness in input data directly affect the quality of planning decisions, as the datadriven modules rely on complete and accurate information to generate optimal solutions. This limitation extends to the level of modeling detail. When relying on analytical methods, the system can only address deviations and reactive measures that are explicitly modeled across all relevant modules. Thus, it is critical to either cover all aspects of the RDP problem space [18] relevant to the specific use case or to rely on methods that support fuzzy reasoning and inference in unexpected extreme scenarios or rare events not covered in the design phase, e.g., through case-based reasoning [34]. Additionally, the architecture relies on real-time data collection. While manual entry is possible, it requires additional human effort. Although automatic systems are available, they require dedicated infrastructure. At the implementation level, ensuring module compatibility poses practical challenges. While the architecture defines clear module interfaces, practical implementation requires ensuring that selected methods and their implementations are compatible with these interfaces, meaning interoperability depends on the specific choices and implementations of data-driven methods within each module. Hardware requirements and computational complexity represent another limitation. Validation was performed on consumer-grade hardware, achieving response times in the single-digit seconds range for the Learning Factory Disassembly System. However, computational complexity increases for complex products, and larger disassembly systems place a higher load on the data pipeline. Although the modular architecture provides scalability by separating individual modules, its practical scalability to large-scale industrial systems with hundreds of products and parallel disassembly stations is yet to be investigated. In particular, potential computational overhead from coordinating multiple parallel planning workflows and workstations in large-scale systems requires further investigation. Related to computational performance, the real-time capability for bidirectional data synchronization must be sufficient to avoid disrupting the disassembly process [72], which depends on the Disassembly System’s cycle time (e.g., minutes for automotive disassembly versus seconds for electronics). Therefore, feasibility studies must consider the characteristics of the Disassembly System in question. Moreover, the technical and methodological complexity of the system requires specialized competencies for implementation and ongoing maintenance, which may pose challenges, particularly for SMEs with limited in-house expertise. Finally, robustness mechanisms for noisy, missing, or delayed observations were limited to basic validation checks and fallback rules, indicating an area requiring further development for industrial deployment. Together, these aspects limit the direct transferability of the current results to industrial deployments and require further investigation of properties such as performance under broader disturbance patterns, industrial interoperability, and behavior at an industrial scale.

##### 6. Conclusions and future research

This article presents a modular Digital Twin architecture for datadriven RDP, enabling an automated, real-time decision-making pipeline that covers all steps from Deviation Detection to Plan Adaptation. By integrating six modules and six connectors into a modular framework, the architecture provides a flexible platform for combining existing and novel data-driven methods into a comprehensive RDP pipeline that is connected to physical disassembly systems. The article, thereby, answers which modules are required for a Digital Twin to support data-driven RDP (RQ1) and how these modules can be connected to form an automated, data-driven decision-making pipeline (RQ2). In addition, theoretical frameworks for Digital Twins in RDP are introduced, providing support for targeted future research and guiding practitioners in the design and implementation of such Digital Twins. The case study demonstrates the practical feasibility of the architecture. While the Learning Factory simplifies several industrial conditions (see Section 5), the case study supports the idea that the efficiency of disassembly systems can be improved through data-driven RDP, thereby making them more reactive. The results further highlight the architecture’s potential to enhance the resilience of disassembly systems, helping production companies become more circular and sustainable.

In summary, the results successfully address the research deficits in integrating RDP methods into a combined, real-time-capable, and fully automated decision-making pipeline (RD1) and in designing a modular Digital Twin architecture as a platform for RDP (RD2).

Building on this contribution, future research should develop novel methods for implementing the present modules and, especially, strive for integrated RDP approaches that simultaneously optimize process and schedule adaptations. While integrated approaches are conceptually superior to isolated process-based or schedule-based methods, they significantly increase solution space complexity and computational requirements. Therefore, a key research challenge is to investigate whether integrated RDP can meet the real-time constraints of production environments, or whether adaptive mechanisms are required that automatically balance the level of integration with computational feasibility depending on problem characteristics. Learning capabilities should be integrated across modules, such as Solution Identification and evaluation, to enable the Digital Twin to accumulate knowledge and improve over time without manual guidance. Moreover, validation should be extended beyond the learning-factory setting through systematic sensitivity and scalability studies that vary product complexity, deviation frequency, and trigger concurrency, thereby characterizing runtime and resource consumption as functions of parallel event handling, the number of parallel workstations, and cycle time requirements. In particular, future studies must assess whether the modular architecture introduces computational overhead that limits real-time performance in large-scale industrial systems and whether bidirectional data synchronization remains sufficiently fast to avoid disrupting disassembly processes across different industrial settings. In addition, the architecture should be benchmarked against different implementations of the individual modules, e.g., metaheuristics and artificial intelligence methods such as reinforcement learning, to better assess its performance. This should extend the evaluation beyond economic indicators to include sustainability criteria such as carbon footprint, energy consumption, and disassembly quality. Finally, robustness should be strengthened by explicitly accounting for noisy, missing, and delayed observations, along with conducting targeted stress tests of computational and network performance. Further industrial evaluations are required to increase the technology readiness level and to quantify the practical benefits of RDP under realistic operational constraints, including true end-of-life product conditions with physical wear and degradation, operator variability, higher throughput demands, and longer process execution times. Such studies should also assess transferability to other industries beyond disassembly, such as repair, remanufacturing, refurbishment, and recycling, as they also face the challenge of adapting processes in real time to unexpected production conditions. Finally, data mining on collected data, for example, process mining on event logs, can support predictive planning and enable the derivation or refinement of EPNs from observed executions.

##### Nomenclature

|**Abbreviation**|**Definition**|
|---|---|
|ACO|Ant Colony Optimization|
|BCO|Bee Colony Optimization|
|C1–C6|Connectors 1–6|
|CEP|Complex Event Processing|
|CH1–CH3|Challenges 1–3|
|DPN|Disassembly Petri Net|
|DPP|Disassembly Process Planning|
|EOL|End of Life|
|EPN|Extended Petri Net|
|I1–I4|Indicators 1–4|
|JSON|JavaScript Object Notation|
|M1–M6|Modules 1–6|
|PNML|Petri Net Markup Language|
|PSO|Particle Swarm Optimization|
|RD1–RD2|Research Deficits 1–2|
|RDP|Reactive Disassembly Planning|
|RDPP|Reactive Disassembly Process Planning|
|RL|Reinforcement Learning|
|RQ1–RQ2|Research Questions 1–2|
|RTLS|Real-Time Locating System|
|SME|Small and Medium-sized Enterprise|
|UML|Unified Modeling Language|

##### CRediT authorship contribution statement

**Lasse Streibel:** Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Software, Resources, Project administration, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. **Tino Schluetter:** Writing – review & editing, Validation, Software, Methodology, Conceptualization. **Stefanie Albers:** Writing – review & editing, Validation. **Finn-Augustin Brunnenkant:** Writing – review & editing, Conceptualization. **Christina Reuter:** Writing – review & editing, Supervision.

##### Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

##### Data availability

The data that support the findings of this study are available upon reasonable request.

##### References

- [1] Küfeoğlu S. SDG-12: Responsible consumption and production. In: Emerging technologies : value creation for sustainable development. Cham: Springer International Publishing; 2022, p. 409–28. http://dx.doi.org/10.1007/978-3-03107127-0_14.

- [2] Bocken N, Miller K, Evans S. Assessing the environmental impact of new circular business models. In: New business models – exploring a changing view on organizing value creation. Toulouse, France; 2016.

- [3] Acerbi F, Sassanelli C, Taisch M. A maturity model enhancing data-driven circular manufacturing. Prod Plan Control 2025;36(7):970–88. http://dx.doi.org/ 10.1080/09537287.2024.2322608.

- [4] Rajput S, Singh SP. Industry 4.0 model for circular economy and cleaner production. J Clean Prod 2020;277:123853. http://dx.doi.org/10.1016/j.jclepro. 2020.123853.

- [5] Alfaro-Algaba M, Ramirez FJ. Techno-economic and environmental disassembly planning of lithium-ion electric vehicle battery packs for remanufacturing. Resour Conserv Recycl 2020;154:104461. http://dx.doi.org/10.1016/j.resconrec.2019. 104461.

- [6] Kristensen HS, Mosgaard MA. A review of micro level indicators for a circular economy – moving away from the three dimensions of sustainability? J Clean Prod 2020;243:118531. http://dx.doi.org/10.1016/j.jclepro.2019.118531.

- [7] Streibel L, Brunnenkant F-A, Reinbold N, Lindholm N, Jordan P, Bluvstein G, Zaeh MF, Reuter C. Systematic review of data modelling methods for systemlevel disassembly planning and control. Int J Sustain Eng 2025;18(1):2563271. http://dx.doi.org/10.1080/19397038.2025.2563271.

- [8] Pullen D, Kara S, Pornprasitpol P, Kaebernick H. A selective disassembly methodology for end-of-life products. Assem Autom 2005;25(2):124–34. http: //dx.doi.org/10.1108/01445150510590488.

- [9] Lambert A. Disassembly sequencing: A survey. Int J Prod Res 2003;41(16):3721–59. http://dx.doi.org/10.1080/0020754031000120078.

- [10] Tang Y, Zhou M, Zussmann E, Caudill R. Disassembly modeling, planning, and application. J Manuf Syst 2002;21(3):200–17. http://dx.doi.org/10.1016/s02786125(02)80162-5.

- [11] Bentaha ML, Battaïa O, Dolgui A. A stochastic formulation of the disassembly line balancing problem. In: Emmanouilidis C, Taisch M, Kiritsis D, editors. Advances in production management systems. competitive manufacturing for innovative products and services. Berlin, Heidelberg: Springer Berlin Heidelberg; 2013, p. 397–404.

- [12] Geiger D, Zussmann E, Lenz E. Probabilistic reactive disassembly planning. CIRP Ann 1996;45(1):49–52. http://dx.doi.org/10.1016/S0007-8506(07)63015-7.

- [13] Zussman E, Zhou MC. Design and implementation of an adaptive process planner for disassembly processes. IEEE Trans Robot Autom 2000;16(2):171–9. http: //dx.doi.org/10.1109/70.843173.

- [14] Wiendahl H-P, Seliger G, Perlewitz H, Bürkner S. A general approach to disassembly planning and control. Prod Plan Control 1999;10(8):718–26. http: //dx.doi.org/10.1080/095372899232542.

- [15] Kang K-W, Doh H-H, Park J-H, Lee D-H. Disassembly leveling and lot sizing for multiple product types: a basic model and its extension. Int J Adv Manuf Technol 2016;82(9–12):1463–73. http://dx.doi.org/10.1007/s00170-012-4570-9.

- [16] Zussman E. Planning of disassembly system. Assem Autom 1995;15(4):20–3. http://dx.doi.org/10.1108/01445159510103100.

- [17] Hrdina J. Beitrag zur steuerung von arbeitsteiligen demontagesystemen [contribution to the control of division-of-labor disassembly systems]. In: Forschungsberichte aus dem Institut für Arbeitswissenschaft und Betriebsorganisation der Universität Karlsruhe, vol. 43, Aachen: Shaker; 2014.

- [18] Streibel L, Jordan P, Zäh M. Digitaler zwilling zur reaktiven demontageplanung [digital twin for reactive disassembly planning]. ZWF Z Wirtsch Fabr 2024;119(11):858–62. http://dx.doi.org/10.1515/zwf-2024-1153.

- [19] VanDerHorn E, Mahadevan S. Digital twin: generalization, characterization and implementation. Decis Support Syst 2021;145:113524. http://dx.doi.org/10. 1016/j.dss.2021.113524.

- [20] Liu Q, Trevisan AH, Yang M, Mascarenhas J. A framework of digital technologies for the circular economy: Digital functions and mechanisms. Bus Strat Env 2022;31(5):2171–92. http://dx.doi.org/10.1002/bse.3015.

- [21] Seegrün A, Kruschke T, Mügge J, Hardinghaus L, Knauf T, Riedelsheimer T, Lindow K. Sustainable product lifecycle management with digital twins: A systematic literature review. Procedia CIRP 2023;119:776–81. http://dx.doi.org/ 10.1016/j.procir.2023.03.124.

- [22] Tang Y, Zhou M, Gao M. Fuzzy-Petri-net-based disassembly planning considering human factors. IEEE Trans Syst Man Cybern A Syst Hum 2006;36(4):718–26. http://dx.doi.org/10.1109/TSMCA.2005.853508.

- [23] Meng K, Cao Y, Peng X, Prybutok V, Youcef-Toumi K. Smart recovery decisionmaking for end-of-life products in the context of ubiquitous information and computational intelligence. J Clean Prod 2020;272:122804. http://dx.doi.org/ 10.1016/j.jclepro.2020.122804.

- [24] Laili Y, Tao F, Pham DT, Wang Y, Zhang L. Robotic disassembly re-planning using a two-pointer detection strategy and a super-fast bees algorithm. Robot Comput-Integr Manuf 2019;59:130–42. http://dx.doi.org/10.1016/j.rcim.2019. 04.003.

- [25] Gao M, Zhou M, Tang Y. Intelligent decision making in disassembly process based on fuzzy reasoning petri nets. IEEE Trans Syst Man Cybern B Cybern : A Publ IEEE Syst Man Cybern Soc 2004;34(5):2029–34. http://dx.doi.org/10.1109/ tsmcb.2004.833331.

- [26] Ren Y, Guo H, Li Y, Li J, Meng L. A self-adaptive learning approach for uncertain disassembly planning based on extended Petri net. IEEE Trans Ind Inf 2023;19(12):11889–97. http://dx.doi.org/10.1109/TII.2023.3253877.

- [27] Kheder M, Trigui M, Aifaoui N. A disassembly sequence planning approach based on particle swarm optimization. In: Haddar M, Chaari F, Benamara A, Chouchane M, Karra C, Aifaoui N, editors. Design and modeling of mechanical systems—III. Cham: Springer International Publishing; 2018, p. 1017–25.

- [28] Feng Y, Zhou M, Tian G, Li Z, Zhang Z, Zhang Q, Tan J. Target disassembly sequencing and scheme evaluation for CNC machine tools using improved multiobjective ant colony algorithm and fuzzy integral. IEEE Trans Syst Man Cybern Syst: Syst 2019;49(12):2438–51. http://dx.doi.org/10.1109/TSMC.2018. 2847448.

- [29] Huang X, Zhang X, Gao Y, Zhan C. Solving a stochastic multi-objective sequence dependence disassembly sequence planning problem with an innovative bees algorithm. Automation 2024;5(3):432–49. http://dx.doi.org/10.3390/ automation5030025.

- [30] Fu Y, Zhou M, Guo X, Qi L, Sedraoui K. Multiverse optimization algorithm for stochastic biobjective disassembly sequence planning subject to operation failures. IEEE Trans Syst Man Cybern Syst: Syst 2022;52(2):1041–51. http: //dx.doi.org/10.1109/TSMC.2021.3049323.

- [31] Wang J, Liang Q, Li M, Qu Z, Zhang Y. Dynamic scheduling in flexible and hybrid disassembly systems with manual and automated workstations using reward-shaping enhanced reinforcement learning. Eng Appl Artif Intell 2025;150:110588. http://dx.doi.org/10.1016/j.engappai.2025.110588.

- [32] Li F, Ma R, Du J, Han H. Decomposition-based multi-objective reinforcement learning for dynamic disassembly job shop scheduling with urgency guidance. Swarm Evol Comput 2025;97:102040. http://dx.doi.org/10.1016/j.swevo.2025. 102040.

- [33] Morad N, Zalzala AMS. Genetic algorithms in integrated process planning and scheduling. J Intell Manuf 1999;10(2):169–79. http://dx.doi.org/10.1023/A: 1008976720878.

- [34] Streibel L, Jordan P, Zaeh MF. Data-driven approach for decision-making in reactive disassembly planning to enable case-based reasoning. Procedia CIRP 2024;130:1117–23. http://dx.doi.org/10.1016/j.procir.2024.10.215.

- [35] Wurster M, Michel M, May MC, Kuhnle A, Stricker N, Lanza G. Modelling and condition-based control of a flexible and hybrid disassembly system with manual and autonomous workstations using reinforcement learning. J Intell Manuf 2022;33(2):575–91. http://dx.doi.org/10.1007/s10845-021-01863-3.

- [36] Abumadi FA, Semeraro C, Olabi AG, Dassisti M. Key research challenges in digital twin applications for demanufacturing. IFAC-PapersOnLine 2022;55(10):2551–6. http://dx.doi.org/10.1016/j.ifacol.2022.10.093.

- [37] Mouflih C, Gaha R, Durupt A, Bosch-Mauchand M, Martinsen K, Eynard B. Decision support framework using knowledge based digital twin for sustainable product development and end of life. Proc Des Soc 2023;3:1157–66. http: //dx.doi.org/10.1017/pds.2023.116.

- [38] Dvorak J, Wurster M, May MC, Lanza G. A systematic approach to task assignment and production planning in disassembly with employee skills. Procedia CIRP 2023;120:958–63. http://dx.doi.org/10.1016/j.procir.2023.09.107.

- [39] Jiao J, Yuan G, Liu X, Tian G, Pham DT. Digital twin-driven dynamic scheduling cloud platform for disassembly workshop. In: Fera M, Caterino M, Macchiaroli R, Pham DT, editors. Advances in remanufacturing. Cham: Springer Nature Switzerland; 2024, p. 265–79.

- [40] Rocca R, Rosa P, Sassanelli C, Fumagalli L, Terzi S. Integrating virtual reality and digital twin in circular economy practices: a laboratory application case. Sustainability 2020;12(6). http://dx.doi.org/10.3390/su12062286.

- [41] Kerin M, Hartono N, Pham DT. Optimising remanufacturing decision-making using the bees algorithm in product digital twins. Sci Rep 2023;13(1):701. http://dx.doi.org/10.1038/s41598-023-27631-2.

- [42] Goodall P, Sharpe R, West A. A data-driven simulation to support remanufacturing operations. Comput Ind 2019;105:48–60. http://dx.doi.org/10.1016/ j.compind.2018.11.001.

- [43] Li J, Zheng H, Bao J. Development of digital twin-based WEEE recycling workshop: initial approaches and future challenges. In: 2022 6th international conference on robotics and automation sciences. 2022, p. 231–7. http://dx.doi. org/10.1109/ICRAS55217.2022.9842043.

- [44] Kritzinger W, Karner M, Traar G, Henjes J, Sihn W. Digital twin in manufacturing: a categorical literature review and classification. IFAC-PapersOnLine 2018;51(11):1016–22. http://dx.doi.org/10.1016/j.ifacol.2018.08.474.

- [45] Ohlendorf M. Simulationsgestützte Planung und Bewertung von Demontagesystemen [Simulation-based planning and evaluation of disassembly systems] [Ph.D. thesis], Technische Universität Carolo-Wilhelmina zu Braunschweig; 2006.

- [46] Allen R, Garlan D. A formal basis for architectural connection. ACM Trans Softw Eng Methodol 1997;6(3):213–49. http://dx.doi.org/10.1145/258077.258078.

- [47] Meyer B. Applying ‘design by contract’. Computer 1992;25(10):40–51. http: //dx.doi.org/10.1109/2.161279.

- [48] Ehm F. Sequencing and scheduling in disassembly shops: A review of problem formulations and solution approaches. J Remanufacturing 2025;16(1):2. http: //dx.doi.org/10.1007/s13243-025-00158-7.

- [49] Lu Y, Pei W, Peng K. State of the art of automatic disassembly of WEEE and perspective towards intelligent recycling in the era of industry 4.0. Int J Adv Manuf Technol 2023;128(7–8):2825–43. http://dx.doi.org/10.1007/s00170-02312043-3.

- [50] Reveliotis SA. Uncertainty management in optimal disassembly planning through learning-based strategies. IIE Trans 2007;39(6):645–58. http://dx.doi.org/10. 1080/07408170600897536.

- [51] Grochowski DE, Tang Y. Parameter estimation for optimal disassembly planning: The Delta Centre-Ville at Montréal, Quebec, Canada October 7-10, 2007/ IEEE. Montreal, Quebec: Omni Press; 2007, http://dx.doi.org/10.1109/ICSMC.2007. 4413878.

- [52] Tang Y, Zhou M, Caudill R. An integrated approach to disassembly planning and demanufacturing operation. IEEE Trans Robot Autom 2001;17(6):773–84. http://dx.doi.org/10.1109/70.975899.

- [53] Bluvstein G, Daub R. Information extraction and knowledge modeling for disassembly processes. Proc Comput Sci 2026;277:1992–2000. http://dx.doi.org/ 10.1016/j.procs.2026.02.237, 7th International Conference on Industry of the Future and Smart Manufacturing (former International Conference on Industry 4.0 and Smart Manufacturing).

- [54] Brunnenkant F-A, Streibel L, Tan K, Reuter C, Zaeh MF. Scalable modeling of destructive and non-destructive disassembly with extended Petri nets for disassembly process planning. Procedia CIRP 2026;140:581–6. http://dx.doi.org/ 10.1016/j.procir.2026.05.098, 33rd CIRP Conference on Life Cycle Engineering (LCE 2026).

- [55] Streibel L, Brunnenkant F-A, Becker J, Jordan P, Wagner S, Salimbeni S, Reuter C. Synchronized data model to enable digital twins for reactive disassembly planning. Proc CIRP 2026;146:249–54. http://dx.doi.org/10.1016/j.procir. 2026.03.270, CIRP Conference on Manufacturing Systems (CIRP CMS).

- [56] Liu J, Xu Z, Xiong H, Lin Q, Xu W, Zhou Z. Digital twin-driven robotic disassembly sequence dynamic planning under uncertain missing condition. IEEE Trans Ind Inf 2023;19(12):11846–55. http://dx.doi.org/10.1109/TII.2023.3253187.

- [57] Ren Y, Jin H, Zhao F, Qu T, Meng L, Zhang C, Zhang B, Wang G, Sutherland JW. A multiobjective disassembly planning for value recovery and energy conservation from end-of-life products. IEEE Trans Autom Sci Eng 2021;18(2):791–803. http://dx.doi.org/10.1109/TASE.2020.2987391.

- [58] Bras B, Emblemsv˚ ag J. The use of activity-based costing, uncertainty, and disassembly action charts in demanufacture cost assessments. In: Proceedings of the SME advances in design automation conference. Boston, Massachusetts; 1995, p. 285–93.

- [59] Jordan P, Zhang H, Wegmann M, Streibel L, Reuter C, Zaeh MF. Simulation framework for evaluating pool sequencing and shop floor dispatching rules in disassembly. In: 2025 IEEE international conference on industrial engineering and engineering management. 2025, p. 73–80. http://dx.doi.org/10.1109/ IEEM63636.2025.11357707.

- [60] Streibel L, Albers S, Schluetter T, Dorsel JH, Jordan P, Lindholm N, Zaeh MF. Integrating real-time data into digital twins for reactive disassembly planning. IFAC-PapersOnLine 2025;59(10):304–9. http://dx.doi.org/10.1016/j.ifacol.2025. 09.053.

- [61] Castiglione C. Automated generation of digital models for manufacturing systems: The event-centric process mining approach. Comput Ind Eng 2024;197:110596. http://dx.doi.org/10.1016/j.cie.2024.110596.

- [62] Jordan P, Piendl D, Kroeger S, Streibel L, Haider C, Zaeh MF. Enabling the material flow analysis in disassembly systems using object-centric process mining. Procedia CIRP 2025;134:271–6. http://dx.doi.org/10.1016/j.procir.2025.03.019, 58th CIRP Conference on Manufacturing Systems 2025.

- [63] Tang Y. Unified colored timed Petri net models for the adaptive control of disassembly systems. In: 2008 IEEE international conference on automation science and engineering. 2008, p. 638–43. http://dx.doi.org/10.1109/COASE. 2008.4626438.

- [64] Dizdarević J, Carpio F, Jukan A, Masip-Bruin X. A survey of communication protocols for internet of things and related challenges of fog and cloud computing integration. ACM Comput Surv 2019;51(6):1–29. http://dx.doi.org/10.1145/ 3292674.

- [65] Ćwikła G. Methods of manufacturing data acquisition for production management - a review. Adv Mater Res 2013;837:618–23. http://dx.doi.org/10.4028/www. scientific.net/AMR.837.618.

- [66] Jordan P, Streibel L, Lindholm N, Maroof W, Vernim S, Goebel L, Zaeh MF. Demonstrator-based implementation of an infrastructure for event data acquisition in disassembly material flows. Procedia CIRP 2025;134:277–82. http://dx. doi.org/10.1016/j.procir.2025.03.040, 58th CIRP Conference on Manufacturing Systems 2025.

- [67] Flouris I, Giatrakos N, Deligiannakis A, Garofalakis M, Kamp M, Mock M. Issues in complex event processing: status and prospects in the big data era. J Syst Softw 2017;127:217–36. http://dx.doi.org/10.1016/j.jss.2016.06.011.

- [68] Rosa-Bilbao J, Boubeta-Puig J. Model-driven engineering for complex event processing: a survey. In: Burgueño L, Gogolla M, Paige R, editors. J Object Technol 2022;21(4):4:1–13. http://dx.doi.org/10.5381/jot.2022.21.4.a10.

- [69] Bernhard O, Streibel L, Rammo J-P, Geng P, Stang J, Wegmann M, et al. Smart production lab: Transforming a lean learning factory into a modular, digital, circular, and robotic production laboratory. In: Proceedings of the 16th conference on learning factories. 2026, [in press].

- [70] Streibel L, Brunnenkant F-A, Eichmann M, Lindholm N, Jordan P, Bernhard O, et al. Disassembly use case for teaching, training, and research validation in circular production learning factories. In: Proceedings of the 16th conference on learning factories. Bolzano, Italy; 2026, [in press].

- [71] Ullerich C, Buscher U. Flexible disassembly planning considering product conditions. Int J Prod Res 2013;51(20):6209–28. http://dx.doi.org/10.1080/ 00207543.2013.825406.

- [72] Huber A. Demontageplanung und -steuerung [disassembly planning and control]. In: Magdeburger Schriften zur Wirtschaftsinformatik, Aachen: Shaker Verlag; 2001.
