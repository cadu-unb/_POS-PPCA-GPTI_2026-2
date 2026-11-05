## ScienceDirect

Procedia CIRP 119 (2023) 1071–1077

33rd <mark>CIRP Design Conference</mark>

# End-of-life decision support to enable circular economy in the automotive industry based on digital twin data

Janine Mügge<sup>a</sup>, Inka Rebekka Hahn<sup>a</sup>, Theresa Riedelsheimer<sup>a</sup>, Johannes Chatzis<sup>b</sup>, Joachim Boes<sup>b</sup>

_aFraunhofer Institute for Production Systems and Design Technology IPK, Pascalstraße 8-9, 10587 Berlin, Germany_

_btec4U-Ingenieurgesellschaft mbH, Saar-Lor-Lux-Straße 15, 66115 Saarbrücken, Germany_

* Janine Mügge. Tel.: +49 30 39006-299; fax: +49 30 3911037. _E-mail address:_ janine.muegge@ipk.fraunhofer.de

#### Abstract

With the EU Green Deal and the UN Sustainable Developments Goals, the vision of a greenhouse gas-neutral and resource-efficient economy is already firmly anchored in world politics. In this context, the automotive industry faces many challenges including the increasing scarcity of natural resources, a rising demand in terms of sustainable vehicle design, production and materials sourcing. Due to all this, end-of-life decisions regarding dismantling have become increasingly important. A high proportion of secondary materials will be required in the vehicles of the future. To response to these challenges, companies have turned their focus towards the circular economy as a central approach to close material loops. In the German research project “Catena-X” a new data ecosystem with digital twins is one enabler that is being developed. The digital twins represent a promising approach to the circular economy by ensuring transparent, product-specific and end-to-end data exchange throughout the entire product lifecycle, from the material sourcing to the eventual dismantling and recycling. As one particular and unique solution, a decision framework that facilitates the best circular strategy at the end of a vehicle’s life is developed and presented in this paper. The underlying data-driven decision support framework is based on circular economy KPIs. This includes material, components and specific vehicle KPIs to best identify the most suitable circular strategy. The framework was methodologically developed by an interdisciplinary team of partners, who are stakeholders throughout the value chain and participants in the Catena-X project. An integrated approach of user-centered design, an adapted version of the V-model and the Scaled Agile Framework were used for the methodology in the development of the solution. The paper presents the concept of a digital twin for a decision support system, that includes a central decision logic that also includes the relevant KPIs and a survey for evaluating the decision logic utilised with a chosen dismantling company.

© 2023 The Authors. Published by Elsevier B.V.

This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) Peer review under the responsibility of the scientific committee of the 33rd CIRP Design Conference

_Keywords:_ Digital Twin; Circular Economy; Sustainability; Catena-X; Decision Support

|**Nomenclature**|KPI      Key-Performance-Indicators|
|---|---|
|CE       circular economy|RQ       research question<br>VIN     vehicle identification number|
|DT       digital twin||
|EoL      end-of-life|**1. Introduction and Research App**|
|ELV     end-of-life vehicles||

> 2212-8271 © 2023 The Authors. Published by Elsevier B.V.

### 1. Introduction and Research Approach

As an indispensable part of a future-oriented and economy, sustainable value creation has gained importance over the last few years. The EU Green Deal and the UN Sustainable Development Goals serve as a roadmap to climate neutrality and a resource-efficient economy that will  drive  new, greener economic development [1,2]. The automotive industry faces these challenges as well. At the same time, the industry is forecasted to grow by 70 % worldwide by 2030 [3]. In order to still achieve the 1.5 °C climate target, mobility emissions need to be decreased by 50 % during this period [3]. Closed material cycles have been identified as being essential for reducing resource consumption and achieving climate protection targets [3]. A tightening of compliance regulations towards CE must be expected to occur [4,5].

> This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) Peer review under the responsibility of the scientific committee of the 33rd CIRP Design Conference 10.1016/j.procir.2023.03.150

The End-of-Life Vehicles Directive 2000/53/EC addresses the EoL treatment by setting clear targets in terms of quotas for recycling and recovery in the European Union [6]. Sustainable approaches throughout the entire lifecycle of a vehicle and the cooperation of all stakeholders can reduce the environmental impact, therefore  these will need to be considered [3,7]. In the research project Catena-X 28 partners currently address secure cross-company data exchange, CE and DTs under the banner of data sovereignty. The concept of a DT for the CE is a promising approach to build a datadriven ecosystem. It is based on vehicle-, component and/or material-specific information, which will open up new business opportunities and value creation models with the aim of using resources as efficiently as possible [7].

In Germany, there are around 500.000 ELV each year, which offer potential for reuse and recycling of components [8]. Reuse and recycling can improve the resilience of the automotive industry's value and supply chains, and reduce the demand of raw materials [3]. As part of Catena-X, a systematic survey with various stakeholders throughout the automotive supply chain was completed. The participants are materials and component suppliers, an OEM and a dismantling company. As a result, various challenges with regard to the implementation of CE have been identified. One of the biggest challenges, according to the interview results, is the decision on the most suited circular strategy that considers technically feasible and environmental targets. Currently, implicit knowledge of dismantlers is used to evaluate ELVs and their components with regard to inventory, customer demand and consideration of economic outlook such as market price. For this purpose, existing databases on vehicle type information such as Schwacke, IDIS, IMDS and AutoDAP are used. Thereby, further challenges are:

- There is no access to existing data on the relevant KPIs for CE from the actual lifecycle of components or assets

- There is no standardized calculation logic to determine the best CE-strategy option based on these KPIs considering the individual KPIs for different components or materials

- There is no platform or network for exchanging and managing the necessary data and information across companies and lifecycle phases while ensuring data sovereignty for data providers

In this paper, research results from Catena-X are presented ina conceptual framework for a DT-based decision logic regarding the appropriate circular strategy. The research attempts to address the following questions: "What data and information is needed to decide upon the technical feasibility of a CE-strategy for end-of-life vehicles? (RQ I)", "How can these KPIs be combined to lead to the most suited CE-strategy given any component or vehicle? (RQ II)" and "Which data needs to be provided from DTs, i.e. specific for an individual instance of a vehicle? (RQ III)”.

### 2. State of the Art

### 2.1. Digital twins in the automotive industry

DTs are increasingly established in many different areas of the automotive industry in order to understand or even predict the behavior and state of vehicles and their components. This paper takes the position that a DT is “a digital representation of an active unique product […] or unique product-service system (a system consisting of a product and a related service)” and their interlinkage including relevant data and information from the lifecycle as well as according to data analytics [9]. The main objective depends upon in the case of the user and it can address simulation, pure monitoring, intelligent optimization or feedback to design [10–12].

The life cycle of a vehicle can be depicted through the data and information collected and analyzed within DTs – from development, production to use, maintenance, repair and reuse, and recycling. Such DTs enable the prediction of behavior, the optimization of usage during operation and recycling, as well as the improvement of future product generations with feedback to design [11,13]. Depending on the application, different types of DTs are used [13,14].

To apply the concept of DTs in a cross-company databased network, the research project Catena-X was funded in 2021 to establish DTs for different use cases within the automotive industry. It is based on the principles of Gaia-X and addresses challenges regarding the accessibility and synchronicity of data model accuracy, communication channels as well as standardization [7]. With regard to the DT understanding, Catena-X refers to the definition of the Industrial Digital Twin Association as a virtual representation of assets and adheres to a series of coordinated properties [15,16]:

- The DT has at least one Catena-X-wide unique ID

- DTs are organized by a set of aspects, which can be extended over lifetime

- A single aspect can be connected to different heterogenous data sources

- The DT can represent asset types (e. g. virtual prototype of a vehicle) and asset instances (e. g. real vehicle)

- A DT can cover the whole asset lifecycle

- DT can provide individual asset and fleet-related knowledge

### 2.2. Digital twins for circular economy

Preut et al. present a concept of a DT for the CE and state that a DT can support the decision-making within the product life cycle to optimize CE parameters [17].

In CE, stages of the product life cycle matter as the first stage is the design, development and production of products, followed by evaluations and simulations to confirm value and sustainability of a part or product. This stage increases the resource efficiency and not only evaluates the current situation of a product but also considers the future of the product. Current and future product compliance is evaluated and issues that could arise regarding the sustainability of products due to problematic substances or materials that are later identified in a product are prevented in the future.

The use phase is to ensure qualified decisions regarding the EoL of a product are made by keeping DTs up to date, mapping physical instance of an asset with its DT and making sure to keep in mind, for example, if and when a remanufacturing is feasible, reuse is possible or when and if recycling is the most valuable solution [18]. Answers and decisions to the mentioned if/when questions are made based on data from the use phase regarding operational hours, failures and maintenance.

The last stage concerns itself with the case of no reusability and the scenario in which a product has no potential for a second life. The DT provides essential info for this stage since it lays out the material breakdown of products, ingredients and composition of a product, which can be crucial regarding sustainability and recyclability [19,20]. The future of DT in CE is also handled in the last stage: Upcoming regulatory requirements such as the mandatory use of recycled content in polymers and other materials show an increased need for detailed and more accurate materials information (as provided by DT) to distinguish recycled materials from virgin materials [20]. These sort of regulatory requirements have the potential advantage of creating more sustainable products in the future, therefore making DT an important part of CE [21].

### 2.3. Circular economy metrics

There has been a growing need for and increased research on CE Metrics over the last few years [22–24]. CE Metrics are used to quantify the implementation of the CE, for example by supporting internal decision-making such as the selection of a CE-strategy at the EoL [23,24]. There is a large number of CE metrics, which are focused on the micro, meso and macro levels [24,25]. In this paper, the focus will be on product-level (micro) evaluation.

Until now, only a few metrics for the evaluation of CE refer to all 9 R-Strategies, although they are indispensable for the implementation of CE [26]. Existing metrics mainly focus on recycling and recovery [22,24]. Only a few CE metrics focus on reuse and remanufacture decisions [24]. A literature review in the context of CE for metrics regarding the manufacturing sector showed a high amount of national-specific research focused on the evaluation of CE with the execution of life cycle assessment [27,28]. Other relevant indicators on product-level are Material Circularity Indicator (MCI) [23,24,29], Product-Level Circularity Metric (PCM) [24,30] or Circular Economy Indicator Prototype (CEIP) [24,31]. In the automotive industry, vehicle recycling rates are the main KPI from a CE perspective [32].

### 3. R-Strategy Assistant

The R-Strategy Assistant is based on the CE definition of the Ellen MacArthur Foundation. CE is defined as an economic model that pursues the goal of extending the lifetime of products and returning components and materials to the cycle at the end of their life [33]. Various approaches exist to implement CE, such as R-Strategies, which reduce resource and material consumption and introduce more circularity into the economy. The number of R-strategies varies in the literature between 3-10. The R-Strategy assistant is based on Potting's 9 Rs [26]. Fig. 1 locates the application of the R- Strategy Assistant within the automotive lifecycle and depicts the data and information flow based on DTs as well as the most relevant stakeholders.

Fig. 1. R-Strategy Assistant within the automotive lifecycle.

### 3.1. Methodical development

To systematically develop software- and data-based solutions within Catena-X, an integrated softwaredevelopment approach of user-centered design, based on the structure of the V-model for mechatronic systems and the Scaled Agile Framework was applied [34–37].  The application of a user-centric approach includes the development of personas and their user journeys [36]. Additionally, a wide-ranging research on the current state of CE, disassembly, R-Strategies and EoL processes was conducted in the literature and complemented by expert interviews. For the development of new solutions to address the challenges within the “as-is” status, case diagrams for several central features and the corresponding user stories have been developed [36,38].

In the following case, the focus is on the needs and requirements of the user. In the first step, the R-Strategy Assistant is developed for the dismantler. The goal of this persona is to determine the most suitable R-Strategy for each specific component of the ELV on instance-based data.

In addition to the identification of non-functional and functional requirements, the data requirements must be analyzed [39]. This requires a detailed specification of either generic or individual asset KPI, which can be provided by the DT of the component or vehicle. This also requires the consideration of existing KPIs and decision logic approaches. A functional model can then be deduced from the results [38].

The logic presented in the following paragraph has been validated with exemplary components of a vehicle and their real data with an application partner of the Catena-X network.

The current focus lies on the technical feasibility of the R- Strategies: Reuse, remanufacture, recycle and recover because these R-Strategies are widespread in the literature and they are the focus of regulatory requirements in the automotive industry [6,32].

### 3.2. Identification of instance-specific KPIs for digital twins

In order to evaluate which R-Strategy can be applied to individual components, instance-specific data must be available. This is achieved through the use of a DT. A DT throughout the product lifecycle enables the collection of instance-specific data on the product, and thus provides the missing EoL data for vehicle disassembly.

Currently the challenges in data collection include the incompleteness of supply chain data, inconsistency of data sources, data formats, context, data quality, lack of actual data for depicting dynamics, highly complex (partly manual) data collection, secure data storage and lack of company-external data [40]. Within Catena-X these challenges are addressed using DTs. In the following paper, it is defined when instancespecific DT data is necessary for vehicle dismantling and when product type-specific data is sufficient. In a first step, the logic of the technical feasibility is defined. The outcome of the technical feasibility is to analyze if an R-strategy has to be excluded at the beginning based on regulatory requirements regarding an R-Strategy or a defect in the functionality of specific components, as shown in Fig. 2. Based on the technical feasibility, the ecological considerations of specific R-Strategies will follow in the further development of the research project, which is not the consideration of this paper.

Fig. 2. Activity diagram of the technical feasibility in UML.

The first step is to identify the data and information required for R-Strategies. For this purpose, a literature research as well as expert interviews with stakeholders from the Catena-X network were conducted. The identified KPIs are shown in Table 1 and divided into instance-specific and product-type-specific indicators.

The process is started by entering the vehicle identification number (VIN) into the R-Strategy Assistant System, thereby requesting the corresponding Catena-X data (No.1 in Fig. 2). The registered companies in the Catena-X network act as data providers for this vehicle-specific data, as they register respective assets and sub-models [16]. Existing data models, the contracting, usage and access control policies and ultimately, the final data exchange are all handled via CatenaX shared services. As one main principle, within Catena-X, data is exchanged while maintaining data sovereignty. After the data request is successfully checked within the Catena-X network, DT data on the respective vehicle, its components, contained material as well as relevant state of health and history is provided for the first overall manual inspection and evaluation.

As a next step, the user is able to select the most relevant components for the R-Strategy decision (No. 2 in Fig. 2 ). Then, the current core module of decision logic is executed sequentially for the selected components to automatically determine technically feasible R-Strategies.

The core process contains the following steps: First, the basic reuse-potential, material composition and remaining lifetime are compared to specific thresholds and the disassembly capability is checked. If one or more of these criteria are not fulfilled, the component will only be assigned to recovery or recycling. If the component qualifies for disassembly, a manual visual inspection and a functional check are conducted. For components, where the visual condition is relevant, such as body parts and interior components, the visual inspection is conducted first. In contrast, components, for which the technical condition is of significant relevance, such as engines and gearboxes, are first subjected to a functional test. Afterwards, the user enters the results into the R-Strategy Assistant. This also allows the DT in the Catena-X network to be updated by adding new DT data (No. 3 Fig. 2). Thereafter, a quality comparison of the component condition with threshold values takes place. When the quality is insufficient for reuse, the technical check for remanufacturing is carried out chronologically: Assimilability, cleanability and restorability/upgradability. Finally, a possible strategy is given to the user as a result.

Table 1: Key-Performance-Indicators of the technical viability for the R- Strategy Assistant

|**I**|**nstance-specific KPIs (DT needed)**|
|---|---|
|KPI|Description|
|Remaining useful<br>lifetime|The remaining useful lifetime is calculated based on<br>the usage behavior of the vehicle and its<br>components as well as the original lifetime|
|Quality state|The quality state defines the state of health of an<br>individual component e.g. paint damages, dents, and<br>corrosion depending on the component type.|
|Assemblability|Assimilability the feasibility to reassemble the<br>component (e.g. for remanufacturing).|
|Cleanability|Cleanability indicates the feasibility to clean a<br>component.|
|Restorability/<br>Upgradability|Restorability/ Upgradability indicates the feasibility<br>to restore, upgrade or refurbish the component).|
||**Product-type specific KPIs**|
|Basic Reuse-<br>Potential|Basic Reuse-Potential, is fulfilled, when the<br>component is not part of an exclusion list, which<br>lists components that may not be reused, such as the<br>airbag.|
|Material<br>Composition|Material Composition includes the types of toxic<br>materials.|
|Disassembly<br>Capability|Disassembly Capability indicates if disassembly is<br>feasible for the different R-Strategies, e.g. non-<br>destructive disassembly for reuse.|

_3.3 Discussion_

Within the project Catena-X, the decision logic of the R- Strategy Assistant was specified based on requirements defined by a potential end user, a dismantling company. After the development, interviews were conducted with key users from the dismantling partner to validate the fulfillment of their requirements. The key users were interviewed and the decision logic was applied to actual components at their EoL: a vehicle door and a vehicle engine, which are shown in Fig. 3.

###  Door: Renault Megane Cabrio, mileage 205.486 km

- Engine: VW Golf 5 "BKC engine", mileage 190.660 km

First, KPIs were discussed, then the general process sequence and how it is applied to different components were analyzed. The exemplary application showed that the developed decision logic and analysis of the technical feasibility for different R-Strategies is consistent with the procedure of the dismantler and applies to various components.

The expert interviews showed that economic feasibility is indispensable in the subsequent overall decision. In particular, the time required for dismantling and the demand situation on the market, in addition other economic aspects, have a significant influence on the decisions made by the dismantler. Further potential is seen in the integration of environmental indicators, which help identify the R-Strategy with the least environmental impact, e.g. with a standardized life cycle assessment [41]. Furthermore, a survey of end users is not yet sufficient to validate the decision logic. In the next step, a case study should be conducted.

Fig. 3. (a) vehicle door; (b) vehicle engine, ©LRP-Autorecycling GmbH

### 4. Conclusion & Outlook

This paper provides an initial introduction to how instancespecific DT data can be used to recommend an appropriate R- Strategy at the end of a vehicle's lifecycle. The main outcome is the development of a decision logic for the technical feasibility of an R-Strategy as well as the identification of instance-specific KPIs where DTs are needed. A DT can help collect data throughout the product lifecycle and be used for decision-making, including the determination of remaining useful life.

One of the biggest challenges when using DT and sharing data is to comply with regulatory requirements and standards regarding data sovereignty. For this, rights and roles are defined in Catena-X to ensure that the data provider retains control and access rights over the data. In addition, the Eclipse

Data Space Connector enables peer-to-peer data exchange, which is decentralized and interoperable [42]. Further challenges when using DTs result when collecting data through the product lifecycle. The required data is scattered across several databases, applications and companies. Standardized data models must be developed in Catena-X to exchange the data.

The first survey showed that decision logic enables dismantling companies to optimize the decision process with regard to the possible R-Strategy for ELV by providing more specific data on components and vehicles. This provides databased decision support for the most suitable R-Strategy and supports different stakeholders throughout the product lifecycle, independent of their experience. In further research, the validation of the decision logic will be extended to other components and vehicle types with different dismantling partners and environmental indicators will be integrated.

In order to conclude DT as a part of an open and digital data ecosystem with standardized data models and interfaces as well as decision logic, enables the transition to a CE by improving the cross-company data exchange and traceability of indicators for specific vehicles and components. In this context, a DT for CE is capable of transparently providing, analyzing and predicting valuable information throughout the product lifecycle. In the long run, DT information can be used to design and create products that have a high potential to be reused or recycled, and at the same time use less primary resources and increase the use of  secondary resources.

### Acknowledgments

This article was published as part of the Catena-X project, which is funded by the Federal Ministry for Economic Affairs and Climate Action.

### References

- [1] European Commission. Communication from the Commission: A European Green Deal; 2019.

- [2] Assembly UG. Transforming our world: The 2030 agenda for sustainable development (A/RES/70/1). United Nations; 2015.

- [3] World Economic Forum. Raising Ambitions: A New Roadmap for the Automotive Circular Economy; 2020.

- [4] European Parliament (ed.). Amendments adopted by the European Parliament on 10 March 2022 on the proposal for a regulation of the European Parliament and of the Council concerning batteries and waste batteries, repealing Directive 2006/66/EC and amending Regulation (EU) 2019/1020 (COM(2020)0798 – C9-0400/2020 – 2020/0353(COD))1; 2022.

- [5] European Parlament and of the council (ed.). Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL concerning batteries and waste batteries, repealing Directive 2006/66/EC and amending Regulation (EU) No 2019/1020; 2023.

- [6] The European Parliament and the Council of the European Union. Directive 2000/53/EC of the European Parliament and of the Council of 18 September 2000 on end of life vehicles; 2002.

- [7] Catena-X Automotive Network e.V. The Vision of Catena-X. Available from: https://catena-x.net/en/vision-goals [July 04, 2022].

- [8] Zimmermann T, Sander K, Memelink R, Knode M, Freier M, Porsch L et al. Illegal Treatment of End-of-Life Vehicles: Assessment of the environmental, micro- and macroeconomic effects: German Environment Agency; 2022.

- [9] Stark R, Damerau T. Digital Twin. In: CIRP Encyclopedia of Production Engineering. Berlin, Heidelberg: Springer Berlin Heidelberg;

Imprint: Springer; 2019, p. 1–8.

- [10] Boschert S, Rosen R. Digital Twin—The Simulation Aspect. In: Mechatronic Futures: Springer, Cham; 2016, p. 59–74.

- [11] Riedelsheimer T, Lindow K, Stark R. Feedback to design with digital lifecycle-twins: literature review and concept presentation. In: Design for X. Contributions to the 29th DfX Symposium, p. 203–214.

- [12] Tao F, Cheng J, Qi Q, Zhang M, Zhang H, Sui F. Digital twin-driven product design, manufacturing and service with big data. The International Journal of Advanced Manufacturing Technology 2018;94(9):3563–76.

- [13] Singh M, Fuenmayor E, Hinchy E, Qiao Y, Murray N, Devine D. Digital Twin: Origin to Future. Applied System Innovation 2021;4(2):36.

- [14] Theresa Riedelsheimer, Pascal Lünnemann, Sebastian Wehking, Lisa Dorfhuber. Digital Twin Readiness Assessment: A study on the use of digital twins in the manufacturing industry; 2020.

- [15] Industrial Digital Twin Association. Inclusion of Module Type Package (MTP) Data into IDTA 02001-1-0 Inclusion of Module Type Package (MTP) Data into Asset Administration Shell: Submodel Template of the Asset Administration Shell; 2022.

- [16] Catena-X Automotive Network Consortium. Semantic Layer/Digital Twins. Available from: https://catena-x.net/de/angebote/digitalerzwilling [July 13, 2022].

- [17] Preut A, Kopka J-P, Clausen U. Digital Twins for the Circular Economy. Sustainability 2021;13(18):1–13.

- [18] Qi Q, Tao F. Digital Twin and Big Data Towards Smart Manufacturing and Industry 4.0: 360 Degree Comparison. IEEE Access 2018;6:3585– 3593.

- [19] Wang XV, Wang L. Digital twin-based WEEE recycling, recovery and remanufacturing in the background of Industry 4.0. International Journal of Production Research 2019;57(12):3892 - 3902.

- [20] Baldassarre B, Maury T, Mathieux F, Garbarino E, Antonopoulos I, Sala S. Drivers and Barriers to the Circular Economy Transition: The Case of Recycled Plastics in the Automotive Sector in the European Union. Procedia CIRP 2022;105:37–42.

- [21] The European Parliament and the Council of the European Union. Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL establishing a framework for setting ecodesign requirements for sustainable products and repealing Directive 2009/125/EC; 2022.

- [22] SYSTEMIQ, acatech. Making the Circular Economy Count; 2021.

- [23] Ellen MacArthur Foundation, ANSYS Granta. Circularity Indicators - An Approach to Measuring Circularity: Methodology; 2019.

- [24] Saidani M, Yannou B, Leroy Y, Cluzel F, Kendall A. A taxonomy of circular economy indicators. Journal of Cleaner Production 2019;207:542–59.

- [25] Kirchherr J, Reike D, Hekkert M. Conceptualizing the circular economy: An analysis of 114 definitions; 2017.

- [26] Potting J, Hekkert MP, Worrell E, Hanemaaijer A. Circular Economy: Measuring Innovation in the Product Chain: PBL Publishers; 2017.

- [27] Rieckhof R, Guenther E. Integrating life cycle assessment and material flow cost accounting to account for resource productivity and economicenvironmental performance. Int J Life Cycle Assess 2018;23(7):1491– 506.

- [28] Pauer E, Wohner B, Heinrich V, Tacker M. Assessing the Environmental Sustainability of Food Packaging: An Extended Life Cycle Assessment including Packaging-Related Food Losses and Waste and Circularity Assessment. Sustainability 2019;11(3):925.

- [29] Niero M, Kalbar PP. Coupling material circularity indicators and life cycle based indicators: A proposal to advance the assessment of circular economy strategies at the product level. Resources, Conservation and Recycling 2019;140:305–12.

- [30] Linder M, Sarasini S, van Loon P. A Metric for Quantifying ProductLevel Circularity. Journal of Industrial Ecology 2017;21(3):545–58.

- [31] Cayzer S, Griffiths P, Beghetto V. Design of indicators for measuring product performance in the circular economy. International Journal of Sustainable Engineering 2017;10(4-5):289–98.

- [32] International Organisation of standardization. Road vehicles - Recyclability and recoverability: Calculation method;13.030.50(ISO 22628:2001); 2001.

- [33] Ellen MacArthur Foundation. Towards the Circular Economy: Economic and business rationale for an accelerated transition. Journal of Industrial Ecology 2013(2.1):13–35.

- [34] Riedelsheimer T, Dorfhuber L, Stark R. User centered development of a Digital Twin concept with focus on sustainability in the clothing industry. Procedia CIRP 2020;90:660–5.

- [35] Riedelsheimer T, Gogineni S, Stark R. Methodology to develop Digital Twins for energy efficient customizable IoT-Products. Procedia CIRP 2021;98:258–63.

- [36] Patton J. User story mapping: Discover the whole story, build the right product. Beijing: O'Reilly; 2014.

- [37] Knaster R, Leffingwell D. SAFe 5.0 Distilled: Achieving Business Agility with the Scaled Agile Framework. 1st ed. Erscheinungsort nicht ermittelbar, Boston, MA: Addison-Wesley Professional; Safari; 2020.

- [38] Seemann J, Gudenberg JW von. Software design with UML 2 (Software-Entwurf mit UML 2): Object-oriented modeling with examples in Java (Objektorientierte Modellierung mit Beispielen in Java). 2nd ed. Berlin, Heidelberg: Springer-Verlag Berlin Heidelberg; 2006.

[39] Leffingwell D. Agile software requirements: Lean requirements practices for teams, programs, and the enterprise. Upper Saddle River, NJ, Munich, Boston, Indianapolis, San Francisco: Addison-Wesley; 2011.

- [40] Riedelsheimer T, Neugebauer S, Lindow K. Progress for Life Cycle Sustainability Assessment by Means of Digital Lifecycle Twins — A Taxonomy. In: EcoDesign and Sustainability II: Springer, Singapore; 2021, p. 329–345.

- [41] International Organisation of standardization. Environmental management - Life cycle assessment - Requirements and guidelines: ISO 14044; 2006.

- [42] Catena-X Automotive Network Consortium. Extended functionality through the Eclipse Data Space Connector (EDC). Available from: https://catena-x.net/en/angebote/edc-die-zentrale-komponente-fuer-die [February 12, 2023].
