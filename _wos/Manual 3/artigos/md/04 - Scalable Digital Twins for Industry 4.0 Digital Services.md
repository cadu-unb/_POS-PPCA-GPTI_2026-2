## Production & Manufacturing Research

**An Open Access Journal**

**ISSN: 2169-3277 (Online) Journal homepage: www.tandfonline.com/journals/tpmr20**

# Scalable Digital Twins for industry 4.0 digital services: a dataspaces approach

#### Tomás Moreno, António Almeida, César Toscano, Filipe Ferreira & Américo Azevedo

**To cite this article:** Tomás Moreno, António Almeida, César Toscano, Filipe Ferreira & Américo Azevedo (2023) Scalable Digital Twins for industry 4.0 digital services: a dataspaces approach, Production & Manufacturing Research, 11:1, 2173680, DOI: 10.1080/21693277.2023.2173680

**To link to this article:** <u>https://doi.org/10.1080/21693277.2023.2173680</u>

© 2023 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group.

Published online: 06 Feb 2023.

Submit your article to this journal

Article views: 4870

View related articles

View Crossmark data

Citing articles: 24 View citing articles

###### ARTICLE

### Scalable Digital Twins for industry 4.0 digital services: a dataspaces approach

Tomás Moreno a,b, António Almeida a,b, César Toscano b, Filipe Ferreira b and Américo Azevedo a,b aFaculty of Engineering, University of Porto, Porto, Portugal; bINESC TEC, Porto, Portugal

###### ABSTRACT

###### ARTICLE HISTORY

The manufacturing industry faces a new revolution, grounded on the intense digitalization of assets and industrial processes and the increasing computation capabilities imposed by the new datadriven digital architectures. This reality has been promoting the Digital Twin concept and its importance in the industrial companies’ business models. However, with these new opportunities, also new threads may rise, mainly related to industrial data protection and sovereignty. Therefore, this research paper will demonstrate the International Data Spaces reference model’s application to overcome these limitations. Following a pilot study with a Portuguese machine producer/maintainer enterprise, this paper will demonstrate the development of a cutting and bending machine Digital Twin, leveraged on an International Data Spaces infrastructure for interoperability, for the plastic and metal industry and its importance to introduce this machine manufacturing company in a new businessto-business marketplace from the EU project Market 4.0.

##### 1. Introduction

###### _1.1. Context_

Received 9 March 2022 Accepted 23 January 2023

###### KEYWORDS

Digital Twin; International data spaces; Product life cycle; Asset administration shell

Industry 4.0 is designated as the fourth industrial revolution and is often associated with ‘smart manufacturing’ (Luthra & Mangla, 2018). It deviates from the others industrial revolutions by recurring to the employment of intelligent cyber-physical systems (CPS), Industrial Internet of Things (IIoT), Big Data, and other future-oriented technologies in a manufacturing environment (Li et al., 2017; Piccarozzi et al., 2018; Sanders et al., 2016; Thames & Schaefer, 2016). Supported by innovative digital technologies, Industry 4.0 aims to achieve fully integrated, automated, optimized, and intelligent production (Piccarozzi et al., 2018; Tissir et al., 2020). As a consequence, Industry 4.0 influenced the manufacturing industry’s business models in terms of product design, manufacture, and delivery (Luthra & Mangla, 2018). Manufacturing industries became built towards the customer experience, offering high customization levels (Aheleroff, Mostashiri, et al., 2021; Kritzinger et al., 2018) to meet individualization.

> © 2023 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/ licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

This revolutionary context of integrated industry (Luthra & Mangla, 2018) enabled the concept of the Digital Twin as a mean to connect the physical assets on the shop-floor with the digital space (Aheleroff, Xu, et al., 2021; Hermann et al., 2015) enabling innovative digital data-driven services (Rolle et al., 2019). With the connection between the physical and digital is possible to monitor (Lu et al., 2020), maintenance (Kritzinger et al., 2018; Rolle et al., 2019), and optimize (Rolle et al., 2019; Santos et al., 2019) the manufacturing processes. With the use of such technologies, the manufacturing processes should improve, decreasing the number of resources wasted, and unnecessary labor (Radziwon et al., 2014) in which the end-costumer can achieve higher levels of satisfaction (Aheleroff, Xu, et al., 2021). Industries that adopted these innovative technologies started to be referred to as smart factories (Hofmann & Rüsch, 2017).

###### _1.2. Motivation_

Manufacturing industries became increasingly competitive as a result of the exponential rise in globalisation (Hofmann & Rüsch, 2017; Luthra & Mangla, 2018; Tissir et al., 2020). In order to remain relevant in this highly competitive environment of industrial production, there is an economic need (Tissir et al., 2020) to stay up-to-date with today’s standard of digital data-driven architectures to provide a flexible response (Aheleroff, Xu, et al., 2021) and achieve higher productivity levels (Kritzinger et al., 2018). With Industry 4.0 is possible to use smart products and systems to obtain competitive advantages in the highly competitive industrial market (Aheleroff, Xu, et al., 2021), in that sense, smart manufacturing has become the direction of the world’s manufacturing industries (Leng et al., 2021). In this digitalization context, data and information are the fundamental aspects of these innovative technologies and the driver (International Data Spaces Association IDSA, 2019) for new opportunities and collaborations between industrial companies and services suppliers. Thus, when allowing data exchange between companies, it is possible to develop and implement digital data-driven services (International Data Spaces Association IDSA, 2019).

However, the implementation of these digital services in the manufacturing industry is a complex and data-dependent process, that requires trust and security measures (Qi et al., 2018). From this emerges the paradigm of data ownership (Bazaz et al., 2020). The presented paper contributes to the state-of-the-art by conceptualising a scalable Digital Twin model for manufacturing equipment that supports data sovereignty and security.

###### _1.3. Problem statement_

In such a competitive and demanding economic environment, manufacturing companies are compelled to explore new data-driven strategies capable of leveraging monitoring and decision-making capabilities with the ambition to reduce latency to identify problems and promote actions for continuous improvement. In this sense, it is mandatory to connect the digital to the manufacturing industry shop-floor and promote new digital data-driven services provided by external companies. This reality has promoted the Digital Twin concept to enable the physical-digital connection and provide new means to store, model, process and share manufacturing data.

However, new challenges and issues connected to the paradigm of data sovereignty and ownership raises as a result of this new setting. These issues stress the development of new implementation concepts that enable both machine/data owners and data-services providers to define data understanding standards as well as secure data communication protocols and channels. While simultaneously provide a clear representation of the physical machine throughout the entirety of its lifecycle.

###### _1.4. Research objectives_

This research aims to demonstrate how _Digital Twin_ and the _International Data Spaces_ concepts can be used to promote new business models, in a secure, interoperable, and trusted way, as well as showcasing these innovative concepts applied in a Portuguese case study, performed within the scope of the Market 4.0 European project. Contributing to the research on this domain, the following research questions were defined and proposed:

- **RQ1** : _How can the ‘Digital Twin’ and the ‘Asset Administration Shell’ concepts be applied at the production systems level to manage and control machines along their life cycle?_

- **RQ2** : _What new kinds of business models can be created leveraged on the secure and trustable data communication between physical machines and data-driven service providers_

- **RQ3** : _How can Digital Twin and new secure data communication infrastructures can leverage the introduction of new B2B marketplaces?_

##### 2. State-of-the-art

###### _2.1. Rami 4.0_

Impacted by Industry 4.0, manufacturing industries were revolutionized and globalized, this stressed the development of a Reference Architecture Model for the Industry 4.0 (RAMI 4.0) (Aheleroff, Xu, et al., 2021; Cai et al., 2017; Hofmann & Rüsch, 2017; Tissir et al., 2020) to ensure standardization between enterprises that use I4.0 Schweichhart (2019). RAMI 4.0 is a service-oriented architecture that combines the fundamental elements and IT of Industry 4.0 in a structured three-dimension layer model (Aheleroff, Xu, et al., 2021; Schweichhart, 2019).

As depicted in Figure 1, RAMI 4.0 is composed of three-axis, the product lifecycle (1), hierarchy levels in the factory (2), and the architecture (3). The product lifecycle is divided into type and instance. Type refers to the construction plan (i.e. development, construction, maintenance software. . .), covering the product lifecycle from the idea of the product to its manufacturing process (Federal Ministry for Economic Affairs and Energy, 2019; Schweichhart, 2019).

Hierarchy levels are separated in a bottom-top approach (Wang et al., 2017) composed of seven different levels (product, field device, control device, station, work centers, and enterprise), each representing functionalities within the factory (Schweichhart, 2019).

In the architecture, it is possible to decompose the smart factory into six different layers asset into six layers, asset (i.e. physical asset), integration (i.e. conversion to the digital world), communication (i.e. facilitates communication within elements), information (i.e. data), functional (i.e. functions and applications), and business (i.e. organization and business process) (Federal Ministry for Economic Affairs and Energy, 2019; Wang et al., 2017).

**Figure 1.** Reference architecture model for the industry 4.0 (Source: Federal Ministry for Economic Affairs and Energy (2019)).

###### _2.1.1. Asset administration shell_

Within the Industry 4.0 manufacturing context, the term Asset Administration Shell (AAS) starts to have its relevance in the technological world. The AAS aims to ‘enable partners in value creation networks to exchange meaningful information by conforming to a specified set of standardized elements’ (Belyaev et al., 2021). According to (Bader et al., 2020), an ‘asset’ can be categorized in everything that requires some sort of ‘connection’ for an Industry 4.0 solution (e.g. machines and their components, contracts, orders, and supply materials). Moreover, the AAS will be the identification card of an asset in Industry 4.0. Furthermore, it will be responsible to provide controlled access to said information and provide a representation of the entire lifecycle of the asset (Bader et al., 2020). Besides, the AAS provides a standardization within digitized industrial production where the formatting of data/information will be according to a specified set of standardized elements (Bader et al., 2020). Thereby, it will be composed of common standards of communication structures, rules for cyber-security, data protection, and language (Bader et al., 2020). This standardization enables unambiguously communication where the exchange of information assets can be easily understood by ensuring standardized semantics between all the participants of the data transitions (Ocker et al., 2021).

Literatures such as (Pribiš et al., 2021; Stojanovic et al., 2021) address the implementation of the AAS concept into the manufacturing process as a mean to connect the physical asset to its respective controller. The AAS is compatible with the OPC Unified Architecture and can be implemented as an OPC UA information model.

###### _2.2. Digital twin_

The use of Industry 4.0 technologies, such as Cyber-physical systems, Industrial Internet of Things, Cloud computing, and Big Data are shifting the manufacturing industry towards a smart manufacturing industry (Qi et al., 2018; Tao, Qi, et al., 2019). In that sense, the Digital Twin can be perceived as an opportunity to optimize the performance of a manufacturing process. In the Industry 4.0 context, manufacturing is evolving from knowledge-based manufacturing to smart manufacturing, in which ‘smart’ refers to the use of data-driven technologies (Tao, Qi, et al., 2019).

In these service-oriented technologies, data and information can be perceived as the common ground and the key element (Bazaz et al., 2020). In order to take advantage of the digital capabilities of cloud computing and artificial intelligence, it is crucial to connect the digital to the physical entity (Tao, Qi, et al., 2019). Thus, requiring the use of sensors to harvest data (on the physical entity) (Tao, Qi, et al., 2019) in real-time and transmitted through IIoT (the communication between the digital and physical) (Qi et al., 2018; Rosen et al., 2015) throughout the product’s lifecycle (Tao, Qi, et al., 2019).

Thereby the DT has intrinsic value in the operation stages but it is not limited to those. A DT can be used to bridge the gap between the design phase of an equipment and its respective operation stage (Schleich et al., 2017). Thus, a DT can be used to facilitate and validate the design of different products and systems (Tao, Sui, et al., 2019) resulting in a reduction of cost and lead time while improving the overall design stage through certification that the product to-be is within requirements and expectations (Silva et al., 2021).

When it comes to the manufacturing process, (Zhang et al., 2019) presents a reconfigurable modeling approach for Digital Twins that reduces the efforts (cost and time) of the development stages of the DT while also verifying the system performance of the DT to-be.

###### _2.2.1. Digital twin instances_

The Digital Twin is a highly researched field resulting in a high density of DT instantiations. This paper will address four different stages of maturity and follows the definitions presented by (Kritzinger et al., 2018) and (Aheleroff, Xu, et al., 2021)

**Digital Model** is the digital representation (model) of a non-existing physical entity, meaning that the digital entity will be the projection of a future physical entity (Kritzinger et al., 2018). This means that at the DM phase there is no communication between the physical and digital entity and all the processes and integration will be emulated.

**Digital Shadow** differs from the Digital Twin in the sense that it does not support bidirectional communication. In the DS the data will flow automatically from the physical entity to the digital but manual from the digital entity to the physical (Kritzinger et al., 2018).

**Digital Twin** is formed by three instances, the digital entity (1), the physical entity (2), and the communication between both entities (3) (Grieves, 2014; Rolle et al., 2019). The digital entity is the representation of the physical entity in a digital environment and is able to monitor, emulate and control the behavior of the physical. In the DT, the data will flow continuously, bidirectional, and in real-time between the entities.

**Digital Twin Predictive** is a Digital Twin that leverages the cyber capabilities to further analyze for predictions (Aheleroff, Xu, et al., 2021). It is composed of a digital replica (that exists in the cyberspace) of a physical object whereas communication occurs in real-time and bidirectionally.

###### _2.3. International data spaces_

With the recent progression in technology, smart devices are becoming ever more common and essential to remain competitive in the highly competitive industrial market (Rajendran & Pagel, 2020). Hence, a key resource of smart devices is data. As of now, most of data is highly protected and not easily shared with third parties. However, enterprises can gain from data exchanges; so, there is a need to establish a high level of trust whilst ensuring data confidentiality in data transactions (Huber et al., 2022).

International Data Spaces (IDS), formerly known as Industrial Data Spaces, was launched in 2015 with a Fraunhofer project. Since then the IDS Associations (IDSA)<sup>1</sup> further developed the notion proposed by Fraunhofer with the proposition of the IDS Reference Architecture Model (IDS-RAM) (Otto, 2022). IDS is defined in the IDS-RAM glossary as a ‘Distributed network of Data Endpoints (i.e. instantiations of the International Data Spaces Connector), allowing a secure exchange of data and guaranteeing Data Sovereignty’ (Otto et al., 2019).

Hence, the IDS initiative has the goal to create a safe data space in which industry enterprises can safely share their data assets (International Data Spaces Association IDSA, 2019) to a different enterprise within the IDS ecosystem. Whereas data spaces represent a data sharing notion that does not requires centralised storage, data remains at the source and is only exchanged when needed (Otto, 2022; Pettenpohl et al., 2022).

To achieve so, Figure 2 depicts some of the IDS components as well as their interactions with one another. The connector is a software component and it is used as the middleman between IoT devices and dataspaces (Nast et al., 2020). This component’s use ensures that data sovereignty is maintained in data exchanges (Pettenpohl et al., 2022). A market survey on open-source connectors was conducted at the time of this writing, and the main available options are as follows: Eclipse Dataspace Connector,<sup>2</sup> Dataspace Connector,<sup>3</sup> and TRUE CONNECTOR<sup>4</sup>

**Figure 2.** Interactions of IDS components according to the IDS-RAM (Source: Otto et al. (2019)).

The IDS enables the creation of a secure connection between IDS connectors in which data is shared safely and can only be accessed according to the terms defined by the participants (typically the data owner and data consumer), guaranteeing data sovereignty for the data owner (Otto et al., 2019). Therefore with the IDS, implementation of smart devices can be done in a safe manner allowing innovative business processes to be created (International Data Spaces Association IDSA, 2019).

###### _2.4. AAS-based digital twin: related work_

The Industrial Digital Twin Association<sup>5</sup> (IDTA), supported by the Federal Ministry for Economic Affairs and Climate Action of the Federal Republic of Germany, is an opensource community that perceives the Asset Administration Shell as the fundamental element of the Digital Twin.

Following the notion proposed by IDTA, Stojanovic et al. (2021) presents the Fraunhofer Advanced Asset Administration Shell Tools<sup>6</sup> (FAAAST) a service to create and manage digital twins compliant with the AAS standards.

In resemblance, Redeker et al. (2022) presented developments on a AAS compliant Digital Twin. Their research, also mentions the importance of secure and trustable data transactions between cross-company. Hence, Redeker et al. (2022) proposes the use of the Gaia-X<sup>7</sup> connectors to support I4.0 services.

Our notion of the Digital Twin of the future follows the line-of-work supported both by Redeker et al. (2022); Stojanovic et al. (2021), however, we conceptualize the digital twin as a modular, scalable, and distributed approach. Digital twins of complex systems can be seen as the aggregation of AAS and its components or elements (machines, robots, AGVs). This AAS reflect the status of each asset in real-time and in a standard way.

##### 3. Methodology

To conduct this project, a qualitative research methodology was applied. This research type relies on a smaller data sample to prove an innovative concept (Arabnia et al., 2018) going towards the project’s goals. Using qualitative research provides a flexible approach that can easily be adapted throughout the case study’s development (Bhandari, 2020). Furthermore, the research method to be used is this project is empirical research. This method aims to gain knowledge from a real situation. By employing this method is possible to establish a precise set of conclusions drawn from the case study (Arabnia et al., 2018).

Figure 3 synthesises the work-phases, whereas the presented paper will reflect the work done up until the _Decision 1_ .

Initially, an in-depth literature review was performed. In the third phase, the overall concept of the project was designed. The concepts presented in this work were applied in a case study in the fourth phase in order to generate empirical knowledge.

**Figure 3.** Planning of the work phases.

In Phase 5, a reflection of the proposed concept model’s implementation will be drawn. The concept will then be extended to a second case study to be given as future research in order to assess its flexibility and application.

##### 4. Concept model

###### _4.1. Requirement analysis_

As stated in the problem statement, from the context of the paper emerges the paradigm of data sovereignty, ownership, and interoperability. Grounded on this, a requirement analysis for the proposed architecture concept model was made. The requirements are divided into functional requirements (FR) and Non Functional Requirements (NFR).

###### _4.1.1. Functional requirements_

Functional Requirements defines what the concept aims to achieve; therefore, in the context of this paper, the following FR were defined:

- **FR1** - Control and monitor a physical product throughout its lifecycle;

- **FR2** - Generate new types of services along the value chain built on top of machine Digital Twin;

- **FR3** - Operationalize new business models and generate new selling models of manufacturing machines’

###### _4.1.2. Non functional requirements_

Non Functional Requirements describes how the developed concept should function, the following NFR were established:

- **NFR1** - Ensuring data sovereignty; Where the data assets generated by the manufacturing shop-floor (Enterprise A) remain in their own control even when employed by the service provider of digital data-driven services (Enterprise B).

- **NFR2** - Ensuring data security; Where the data assets must be protected and secure when transmitted from the location of the manufacturing shop-floor to the location of the service provider of digital data-driven services.

- **NFR3** - Ensuring data ownership; Where the data owner is able to create, access, modify and create revenue from their data assets.

- **NFR4** - Achieving semantic interoperability; Where data transactions can be done unambiguously, therefore the exchanged data assets can be easily understood by both participants.

- **NFR5** - Machine controller generates data logs regarding the manufacturing equipment status; Where the controller will generate data logs to provide a digital representation of the manufacturing equipment status along its entire lifecycle.

- **NFR6** - Machine controller generated data files in JSON format; Where the generated data logs from the machine controller are in a structured manner and ready to be used.

- **NFR7** - Process the affluence of data logs generated on the manufacturing shopfloor; Where enterprises, in order to leverage all of the Industry 4.0 technologies capabilities, must be prepared to process the affluence of data generated.

- **NFR8** - Data flow from the manufacturing shop-floor to the service provider of digital data-driven services; Where the data owner and the service provider should have a direct and trusted channel of communication.

- **NFR9** - Ensure traceability across the asset lifecycle; a clear image of the asset in all stages of the lifecycle should be provided

###### _4.2. Proposed architecture concept model_

Following the industry 4.0 paradigm, the concept presented in this paper aims to introduce innovative data-driven digital services that can now be introduced through the use of Digital Twins, backed up by a secure and reliable communication infrastructure based on IDS technologies, and the standardisation of information models based on the Asset Administration Shell.

**Figure 4.** Pyramid of the key concepts presented on this paper.

Figure 4, exhibits the four layers of key concepts presented in this Chapter, being Industry 4.0 the key enabler of innovation, serving as the foundation of this pyramid.

The second layer is the International Data Spaces layer and it is responsible to ensure data sovereignty, security, and ownership. This layer plays a key part in the concepts to be explored and serves as the basis for communication and data flows between different stakeholders.

Asset Administration Shell, the third layer is responsible for the standardization of the information models. On this layer it is guarantee a common ground, and common understanding, meaning that by resorting to the use of these technologies and their templates data transactions can be easily understood.

Finally, the fourth layer, the Digital Twin is employed as a means to process the abundance of data generated whilst connecting the physical-digital spaces.

**Figure 5.** Architecture concept model proposed in this paper.

Following the vision presented in Figure 4, this paper presents a data-driven architecture, that combines the four layers of concepts into a conceptual model that is built with the purpose to be easily adaptable into different manufacturing contexts.

Figure 5 exhibits the high-level architectural concept model presented in this paper, combining:

(1) **International Data Spaces** , as a secure and reliable channel of communication between machine owners and services providers. i.e. accountable of ensuring the communication between the physical machine in the machine owner location and the digital machine in the service provider location. This will reside in the communication layer and is composed of the IDS connectors on both locations. It is also responsible for the data exchange according to the contractual agreements imposed by both participants.

(2) **Asset Administration Shell** , as the means to standardize the information models among all potential users, enabling interoperability across the entire value chain. i.e. responsible for ensuring that the generated information models are standardized by recurring to the use of dictionaries.

(3) **Digital Twin** , as the digital representation of the machine, enabler of the digital capabilities, and the fusion between the physical-virtual. The Digital Twin is the result of the composition of all entities, the Physical Machine, the Digital Machine, and the Communication layer supported by the IDS initiative, all of this leveraging from the AAS to ensure common understanding.

Figure 5 showcases the Digital Twin and its three instances, (1) physical machine, (2) digital machine, and (3) the communication between both machines. The physical machine instance is composed of a machine as well as the required sensors, actuators, and a machine controller. The sensors harvest the data from the machine and the machine controller is in charge of generating files in accordance with the AAS specification. The actuators act upon the machine upon the feedback received. Data assets are received and prepared for use by digital data-driven services such as online dashboards, emulations, and artificial intelligence on the Digital Machine instance. Finally, the communication instance is composed of two IDS controllers at both of the locations.

###### _4.2.1. New services_

Levering onto the digital capabilities achieved through the Digital Twin, it is feasible to establish new types of additional product-service systems rather than the traditional selling of a physical product. Alternately, it is now possible to introduce services to; monitor the physical product digitally and remotely, automate processes and remotely act upon the physical product, enable corrective and predictive behaviors through artificial intelligence and remote maintenance assistance or/and automated scheduling of physical assistance when reaching certain levels of critical usage.

Likewise, these new types of product-services systems are composed of a set of innovative digital data-driven services. They will support the physical product users in defining conditioned/preventive maintenance plans, leveraging real-time physical product parameters while monitoring, calculating, and enhancing the visibility of the physical product overall equipment effectiveness (OEE) based on online dashboards. Part of the digital data-driven services will leverage the data and parameters collected in real-time from manufacturing machines to a platform that will compile and process the data to generate web-based dashboards and intelligence related to the physical product usage and performance. Moreover, these new services will support the physical product’s performance and maintenance by processing and accessing their data.

###### _4.2.2. New business models_

The innovative new product-services systems built within the Digital Twin platform allow for the machine manufacturers to provide digital data-driven type services. They are enhancing the customer experience whilst managing to capitalize from it. With this secure data exchange built from the physical product (PP) manufacturer to the PP customer, the PP manufacturer, in addition to selling the physical product, can now sell and provide innovative product-services systems that rely on the manufacturer data to generate additional revenue. This revenue can be from yearly subscription plans or selling product-services systems for a supplemental fee added to the PP cost. Moreover, it can utilize the new product-services systems to provide high-level assistance, giving the customer a straightforward way to schedule maintenance remotely, monitor and automate the PP processes with corrective and predictive type behaviors.

###### _4.3. International data spaces_

###### _4.3.1. Problem statement_

Herewith, when intending to implement digital data-driven services, data must flow from the manufacturing shop-floor to the aforementioned digital data-driven services.

Nevertheless, the implementation of these data-driven digital services requires specialized knowledge and tools which may require outsourcing. Thus, when promoting new digital data-driven services, the following requirements arise:

- **NFR1** - Ensuring data sovereignty;

- **NFR2** - Ensuring data security;

- **NFR3** - Ensuring data ownership;

- **NFR6** - Channel of communication;

Moreover, these proposed requirements stress the importance of developing secure channels of communication where data can be safely exchanged within enterprises at different locations, highlighting the IDS initiative’s interest in facing these proposed requirements.

###### _4.3.2. Simplified concept_

Conducive to these challenges, the concept presented in this paper aims to introduce an implementation concept of innovative data-driven digital services, supported by a secure and reliable communication infrastructure based on IDS technologies. The IDS is a safe data space in which industry enterprises can safely share their data assets with enterprises within the ecosystem. Moreover, it allows establishing a secure connection between IDS connectors.

**Figure 6.** Concept of the connection between IDS connectors.

Figure 6 displays a simplified version of a connection between two IDS connectors at different locations, location A and location B. By having two different connectors in two different locations, it is possible to build a secure and reliable communication channel amongst the connector at the location A and the connector at location B. Herewith, data can be safely shared between both locations. It is also showcased in Figure 6, the terminology, _data owner_ and _data consumer_ , whereas:

• **Data owner** is the legal entity over _the data to be used_ , for instance, the enterprise ‘A’ is generating manufacturing data in their machinery, therefore, enterprise ‘A’ is the data owner of said data and is able to enforce contractual agreements on the use of data and provide or deny access to third parties.

• **Data consumer** is the service provider of the digital data-driven services, it will be responsible to use the data assets provided by the data owner according to the contractual agreements made by both entities.

###### _4.3.3. Draft of the architecture model_

Figure 7 showcases the initial architectural draft designed in this paper in order to meet the needs of implementing secured and trusted communication channels between manufacturing industries and the service providers on the digital data-driven services.

It is possible to follow the route of data. Firstly, data will be created on the data owner’s location. This data creation depends on the manufacturing industry, it can range from data harvested on the manufacturing equipment through sensors to data generated from software/simulations to manual inputs. In this first draft, it will not be assumed the origin of data, it will only be presumed that the generated data is _raw manufacturing data_ to be processed that is stored and created at the data owner location. The _raw manufacturing data_ then must find its way to the IDS connector located at the data owner location; this connector will be responsible for sending the data assets to the provider’s IDS connector. Once on the consumer’s IDS connector, data is ready to be used by the digital data-driven services that can lead to the display of the processed data in interface service or even the return of the processed data assets to the data owner.

**Figure 7.** First architecture model with IDS (Based on: Otto et al. (2019)).

Furthermore, the data provider and the data consumer data exchange as well as the data usage contracts agreed by them will be logged in the IDS Clearing House. It is feasible for evolving organisations to leverage this module to resolve conflicts and provide financial reports for billing purposes. Our vision presupposes that the innovative data-driven services provided are meant to benefit the data provider, leveraged by a high level of trust between services provider and consumer. Nevertheless, data sovereignty and data usage are covered by the IDS ecosystem by contractual agreements.

The Identity Provider allows organisations within the IDS ecosystem to confirm their digital identity, ensuring that each data transaction is completed through the correct participants and, as a result, ensuring that data assets are safeguarded and only accessed by verified and authorised participants.

###### _4.4. Asset administration shell_

###### _4.4.1. Problem statement_

In today’s innovative and technological industrial world is evermore common the use of digital data-driven services recurring to the use of outsourced enterprises. This requires a secure and semantic interoperability connection between the data owner and the service provider of the digital data-driven services. A secured and trusted channel of communication can be achieved through the use of the International Data Spaces connectors nevertheless, the AAS concept can address the following requirements:

- **NFR4** - Achieving semantic interoperability;

- **NFR6** - Data files in JSON format;

- **NFR5** - Machine controller generates data logs;

- **NFR9** - Ensure traceability across the asset lifecycle;

These proposed requirements stress the importance of developing semantic interoperability within digitized industrial production enterprises. The following sections will discuss how the AAS can be an answer to the proposed requirements.

###### _4.4.2. Metamodel description_

The Asset Administration Shell will serve as the identification card of the physical product and provide a digital representation of it along its entire lifecycle. Utilizing the AAS makes it possible to achieve a common understanding within digitized industrial production enterprises. The AAS supports the use of external dictionaries such as eCl@ss and IEC CDD, easing the process of assigning semantic descriptions to the AAS properties

Figure 8 displays the simplified AAS metamodel. Here, an asset administration shell can be composed of multiple submodels. Each submodel can be composed of multiple submodel elements. Each submodel element can have one or more qualifiers (for simplification, proposes on the figure are only displayed certain qualifiers).

**Figure 9.** Information model of the asset administration shell.

**Figure 10.** Illustration of the requirements that enlightened the importance of the digital twin.

###### _4.4.3. Submodels_

The concept of the AAS used in this paper can be divided into four different submodels composed of similar information: Identification, technical data, operational data, and documentation. These are the fundamental elements of the AAS. In order to ensure semantic interoperability, the semantic description of the submodel and submodel components must be clearly defined and easily accessed (Belyaev et al., 2021).

Figure 9 displays a simplified version of the information model designed for the case study used in this paper. Herein, the Asset Administration Shell is divided into four submodels.

(1) **Submodel identification** : Here it will be defined information regarding the identification of the machine. This information includes the enterprise identification and the machine serial number. With these two informations, it is possible to link a machine to an enterprise and the serial number to associate to a specific machine within that enterprise.

(2) **Submodel Technical Data** : In this submodel, it is defined the characteristics of the machine, namely the type of machine, maximum and minimum length/thickness of the material to be processed, and the type of materials that can be processed in the machine (i.e. aluminum, steel, etc).

(3) **Submodel Operational Data** : Herewith, data is defined regarding the machine operation status, this may include information about the event type and status of the machine, time of starting or stopping, serial number associated with the product currently being manufactured, number of strokes, and error messages.

(4) **Submodel Documentation** : Finally, on this submodel, it will be made available to every user of the interaction the documentation necessary to easily comprehend the information being exchanged. This includes a dictionary-based instruction manual. For example, when defining a type of material allowed in a machine, each material has a numeral code. Through the use of the dictionary, it will be easily determined what type of material the code is referring to.

###### _4.4.4. Semantic interoperability_

To achieve semantic interoperability, every submodel element must have a semantic definition through the use of a _concept description_ . The use of standardized dictionaries such as IEC CDD or eCl@ss ease the process of the assignment of semantic description. When using a semantic definition provided by an external dictionary, the global id of the ConceptDescription can be the same global id used in the dictionary. The global IDs of the dictionaries are International Registration Data Identifier (IRDI). For instance, the IRDI in the IEC CDD dictionary of _Temperature_ is 0112/2///61360_4#AAE685#001. When searching for this global id in the dictionary, the information regarding this variable can easily be traced. By recurring to these, it is feasible to achieve unambiguous data exchanges with different enterprises. The main dictionaries used in the AAS context are eCl@ss and IEC CDD. Nevertheless, it may be necessary to rely on dictionaries tailored to a specific case study.

###### _4.5. Digital twin_

###### _4.5.1. Problem statement_

Today’s globalization of Industry 4.0 and its technologies (Tissir et al., 2020) steer to the need for manufacturing industries to adopt these technologies to survive the highly competitive environment. In order to meet individualization created by the globalization of the manufacturing industries, manufacturing industries become built towards the customer and offered high customization levels (Kritzinger et al., 2018). As a result of adopting these Industry 4.0 technologies, on a manufacturing shop-floor with multiple machine and process instances, meaningful data is constantly generated. Thus, as represented in Figure 10, an abundance of data will be created. In conclusion, two major requirements arise:

**Figure 11.** Illustration of the initial digital twin concept.

- **NFR7** - Process the affluence of data;

- **FR1** - Control and monitor a physical product;

These proposed requirements stress the importance of the use of innovative digital datadriven services in order to enterprises to remain relevant in the highly competitive industrial manufacturing environment and to process the affluence of data generated by their assets.

###### _4.5.2. Conceptualization of the digital twin model_

Figure 11 displays the initial vision developed for the Digital Twin concept model. In this, it is also possible to see the concepts of the Asset Administration Shell and the International Data Space introduced in this Digital Twin concept.

Therein, the DT will be used as a means to process the affluence of data generated from the machine on the manufacturing shop floor. By utilizing the IDS it is possible to build a secure and trusted channel of communication between the data owner and the service provider. Furthermore, thanks to the standardization enabled by the AAS, the service provider will be able to supply his digital data-driven services to every enterprise that follows the AAS standard. The data assets will be used to monitor, emulate and analyze the machine behavior in a digital and safe environment. In addition, this enables the concept of using the DT to measure key performance indicators of the machine, such as the OEE, to support the decision-making process of the end-user.

Thus, allowing the manufacturing companies to utilize the DT capabilities to improve their machines’ reliability, flexibility, and predictability. Likewise, the DT can assist in the maintenance of the machine by monitoring levels of usage to schedule maintenance when reaching pre-defined levels and through machine learning, detect patterns that lead other machines to a malfunction. The DT is able to improve the machine performance and provide high-level assistance to the end customer.

**Figure 12.** Lifecycles of the product stages of the physical product & digital twin.

###### _4.5.3. Digital thread_

The use of the Digital Thread as a crucial element to provide an integrated view of the physical product across its entire manufacturing lifespan will be covered in this subsection.

As represented in Figure 12, the physical product lifecycle (PPL) addresses the physical machine processes beginning with the machine’s design according on the client’s individual needs and following the evolution to an operational machine and can be divided into five main product stages:

- (1) _Design_ , i.e. the concept, design, and validation of the product;

- (2) _Production_ , i.e. the production and assembly of the physical product;

- (3) _Commissioning_ , i.e. the delivery and installation;

- (4) _Operation_ , i.e. the overall usage of the physical product;

- (5) _Recycling_ , i.e. the end of the PPL, including the product status assurance;

Digital twin Lifecycle (DTL) follows the conversion of a Digital Model of a machine to be built into a Digital Twin that will support an existing machine’s performance. Each of the product stages of the PPL will be supported by the product stages of the DTL, thus, the PPL and DTL are connected through the same color stages.

It is easily comprehended how the Digital Twin will support the physical product lifecycle stages by comparing each stage from the PPL to the DTL one at a time.

- (1) In the _Design stage_ , through the _development of a digital model_ it is possible to create innovative new products in a more efficient and informed manner (Tao, Qi, et al., 2019) and enables designers to visualize and materialize complex products (Qi et al., 2021).

- (2) Referring to the _Production stage_ , the _digital model instantiation_ is capable of validating products concepts and designs in a safe digital environment, supporting the product manufacturing stage without the need to build expensive physical prototypes (Qi et al., 2021) and providing high fidelity models to optimize the product assembly process.

- (3) When it comes to the _Commissioning stage_ , the _physical and digital object connection_ can be eased through the use of the DM to test the integration of the physical entity in the manufacturing process, reducing the risk of an unsuccessful implementation and the need for physical testing procedures. At this stage, it is possible to follow the conversion from a DM to a DT or DS.

- (4) Regarding the _Operation stage_ , the data will flow continuously and in real-time from the physical to the digital object. This real-time nature means that the digital object (in the DT or DS) can generate a picture of the real-world performance (Lu et al., 2020) from the manufacturing data gathered from the physical object. With this interface, it is possible to analyze the performance of the asset through machine learning, and it is possible to recognize patterns that had/might lead to a malfunction (Kritzinger et al., 2018) and schedule maintenance before reaching critical levels of usage. Additionally, in the Digital Twin instance specifically, because of the bidirectional communication, the digital object is able to control and act upon the physical object. Therefore, the DT is capable of automate highlevel tasks, resulting in a more independent, intelligent, reliable, and flexible manufacturing process.

- (5) Finally, at the _Recycling stage_ it is possible to determine the _product status assurance_ of different parts of the product through data harvested during the physical product lifecycle and determine which parts are still good to be used in future designs.

###### _4.6. Concept revision & summary_

Throughout this Chapter, it was developed an architecture concept model to fulfil the requirements proposed for this research. With the knowledge gathered and the concepts described in this Chapter, it is now possible to revisit the functional & non functional requirements and analyze their progress. Therefore, through this analysis, it is possible to define the success of the developed concept.

**FR1** - Control and monitor a physical product throughout its lifecycle;

- This can be achieved through the use of the Digital Twin. The DT leverages the IDS and the AAS – the IDS enables the creation of a secure channel of communication through the physical object to the digital object; and the AAS enables the deployment of AAS files that provide a picture of the physical product. Finally, the DT from the secure connection and generation of files regarding the equipment status is able to use the manufacturing data assets to control and monitor the physical product.

**FR2** - Generate new types of services along the value chain built on top of machine Digital Twin;

- The use of a manufacturing Digital Twin opened the possibility to introduce new types of services; monitoring and acting upon the physical product, automating processes, and enabling corrective and predictive behaviours.

**FR3** - Operationalize new business models and generate new selling models of manufacturing machines’;

- Machine manufacturers, in addition to selling the physical product, can now sell digital data-driven services built on top of the physical product. Allowing additional revenue to be made through subscription fees.

**NFR1 & NFR2 & NFR3** - Ensuring data sovereignty, security and ownership;

- International Data Spaces enables participants within its ecosystem to establish data transactions according to contractual agreements that ensure data sovereignty and ownership. Furthermore, only authorized participants can join the IDS ecosystem, and through the use of the module _Identity Provider_ , it is possible to guarantee that data transactions occur to the desired participant.

**NFR4** - Achieving semantic interoperability;

- Using standardized dictionaries it is possible to associate used variables with an IRDI that can be easily searched in the dictionary and thus, ensuring a common ground for variables definition.

**NFR5** - Machine controller generates data logs regarding the manufacturing equipment status;

- Through the use of the Asset Administration Shell, it is possible to generate AAStype files that can give a clear picture of the physical machine in a digital environment along its entire lifecycle. This can be achieved with proactive AAS, and additionally, it is possible to use passive AAS to create machine characteristics before their physical existence.

**NFR6** - Machine controller generated data files in JSON format;

- The AAS is capable of deploying JSON files.

**NFR7** - Process the affluence of data logs generated on the manufacturing shop-floor;

- The Digital Twin and its connection between the physical and the digital enable the use of data-driven services capable of dealing with the affluence of data generated on the manufacturing shop-floor.

**NFR8** - Data flow from the manufacturing shop-floor to the service provider of digital data-driven services;

- The use of the International Data Spaces initiative it is possible to install two IDS connectors, one at the manufacturing shop-floor location and the other at the service provider location, and create a channel of communication between both

**NFR9** - Ensure traceability across the asset lifecycle

- Through the use of the asset administration shell, it is possible to produce a representation of the asset across its lifecycle i.e. Digital Thread. This enables the generation of additional services across all product stages, while also offering a comprehensive picture of the asset’s whole lifespan.

##### 5. Case study

Within a volatile and complex circumstance, especially during such COVID-19 pandemic, specialized digital marketplaces for machines, components, and services for the metal industry are a new opportunity to bring together customers and technology providers. These specialized marketplaces may become a one-stop shop capable of supporting manufacturing companies during the production system configuration and throughout the whole machine lifecycle, providing services to increase machine OEE and lifespan.

Market4.0 (M4.0)<sup>8</sup> European project aims to create a new B2B industrial marketplace for machines and services that leverages the IDS initiative to ensure data sovereignty between suppliers and customers. This innovative marketplace will support industrial companies from the acquisition to the usage and recycling stage.

###### _5.1. Proposed architecture model_

The applied architecture model displayed in Figure 13 shows the integration between the data provider (i.e. the machine owner) and the data consumer (i.e. the Portuguese machine producer/maintainer company), ensuring data sovereignty to the data owner.

**Figure 13.** Illustration of the applied architecture model in the case study (Firstly introduced in: Moreno et al. (2021)).

In terms of architecture, the left side corresponds to the physical machine in the concept displayed in Figure 5. The modules installed in the machine owner location are:

- A machine from the Portuguese machine producer/maintainer company that generates real-time data to be consumed

- Machine Data Server, a repository that gathers and stores all files generated by the machine (i.e. a folder)

- DataSpace4Provider, an IDS-based framework which provides an application programming interface (API) easing the interactions with the respective IDS connector

- Monitor App, a python-based application which is responsible to monitor the contents of the machine data server

When it comes to the right side, it is possible to see the resemblance to the digital machine presented in Figure 5. The right side corresponds to the service provider of the digital data-driven services, and it includes the following modules:

- DataSpace4Consumer, an IDS-based framework which provides an application programming interface (API) easing the interactions with the respective IDS connector

- Data Preparation App, receives the contents sent to the consumer’s connector via PUSH and reconstructs the AAS

- Integrated performance and maintenance service (IPMS), responsible for displaying the machine’s generated data to the end-user in a graphical interface.

###### _5.2. Deployment of a passive asset administration shell_

This section will elaborate on the work done regarding the Asset Administration Shell in the case study. The software used to develop the AAS was the AASX Package Explorer. This software allows the creation of passive AAS. Nonetheless, as of now, this software is not ideal for the Digital Twin because it does not support the deployment of reacting and proactive AAS. At the time of this writing, there is still no viable public software capable of creating proactive AAS, however, there are a few open-sources options capable of deploying reacting AAS such as the Eclipse BaSyx Python SDK.<sup>9</sup> Nonetheless, the deployment of the AAS on this case study will only serve as a proof-of-concept, hence, only passive AAS were created. Future research aims to introduce the deployment of reactive and proactive AAS.

**Figure 14.** Example of an AAS from the case study.

Figure 14 displays an example of an Asset Administration Shell for the Case Study. On this, it was necessary to create an asset _‘Manufacturing Machine’_ that is linked with the AAS _‘Operational_AAS’_ . The AAS concept states that the AAS is composed of four different submodels, identification, technical data, operational data, and documentation. Furthermore, from the AAS is possible to export the desired submodel in a JSON-format.

###### _5.3. Communication framework – DataSpace4Provider & consumer_

In order to support the communication needs of the Digital Twin, this research leverage the implementation of two IDS Connectors, in particular through the one known as the DataspaceConnector. As presented in Figure 13, the communication framework is divided into two different instances of the DataSpaceApp4EDI:

- DataSpace4Provider – the usage of the word ‘provider’ refers to the entity that will provide the data to be used in the digital data-driven services. In order words, the ‘provider’ will be the owner entity of the physical machine.

- DataSpace4Consumer – whilst the usage of the word ‘consumer’ remits to the entity that will consume the provided data assets to be used in the digital data-driven services.

The DataSpace4Provider and the DataSpace4Consumer are deployed in separate virtual machines (VM). Ideally, VMs would not be required, the DataSpace4Provider could have been installed on the premises of the physical object whilst the DataSpace4Consumer within the digital platform. Nonetheless, the usage of the VMs enabled streamlining progress on multiple fronts whilst easing the process of assigning the required public IP addresses.

Both of the instances are composed of two main components, DataSpaceApp4EDI and the DataspaceConnector.

The IDS Connector used in the case study was the DataspaceConnector.<sup>10</sup> This selection reflex on a careful analysis made of the available IDS Connectors. In sum, this selection was made taking into consideration the following reasons:

- Actively supported by its developers

- Provision of good online documentation with all the necessary information to set up and use the connector

- Provision of a REST API to interact with custom-made Data Apps. This interface also provides good documentation using Swagger UI

- Ease of use and integration with the use case necessities

- and mainly be operational and implementing most of the IDS messages.

**Figure 15.** Snippet of the swagger UI documentation.

The DataSpaceApp4EDI is an IDS DataApp, specifically developed for the DataspaceConnector, aiming at orchestrating the actions done by the DataspaceConnector, in terms of data provision and data consumption, while providing a simple API to the Monitor App and Data Preparation Data, as depicted in Figure 13. By using the data elements defined by IDS (e.g. catalogs, data resources/representations and data artifacts), a unidirectional communication channel is established between two different instances of the DataSpaceApp4EDI. Data published on one side of the channel appears subsequently on the end side of the channel. An IDS data usage contract is automatically created, whereby the first DataSpaceApp4EDI instance (provider) allows the provisioned data to be accessed by the second instance of the DataSpaceApp4EDI (consumer). This process is implemented by the two DataSpaceApp4EDI instances, on top of the two IDS connectors they are attached to.

###### _5.3.1. Manufacturing data orchestration_

When it comes to the route of data from the generation in the physical asset to the usage of data as a manufacturing asset, the route flow principles are presented here.

**_5.3.1.1. Stage 1 - generation of data._** Firstly, logs referring to the machine processes are generated and serialized as JSON data, representing an AAS file, into a folder in a specific computer’s directory (running on Windows 10) from the tester enterprise. This involves making a remote connection directly from the Machine Controller to the folder directory of the computer.

**_5.3.1.2. Stage 2 - acknowledgement of data generation._** The Monitor App is responsible for monitoring the folder directory. Once an AAS file is created, the content is read. The Submodel Identification from the AAS, allows identifying the enterprise and the machine through the enterprise identification code and the machine serial number as well as the destination (i.e. the ID of the destiny connector).

**Figure 16.** Illustration of the application scheme regarding its installation and operation process.

**_5.3.1.3. Stage 3 - sending of AAS data._** At this stage, the Monitor App is responsible to publish the data assets to the DataSpaceApp4EDI of the provider. To do so, a POST request is made on the DataSpaceApp4EDI as represented by the Swagger UI documentation in Figure 15.

The ‘toPartnerId’ represents the ID of the connector which the data should be routed to. In this case, since the data has to be sent by the DataSpace4Consumer to the DataSpace4Provider, the ‘toPartnerId’ is thereby the latest.

The docTitle has to be unique within the dataspace, thereby, to simplify, the docTitle used is an identifier followed by a timestamp (ex: enterprise + (timestamp)).

Both, the ‘toPartnerId’ and the identifier used in the ‘docTitle’ are retrieved through the use of the Identification Submodel of the AAS.

Finally, the docTitle refers to the type of the data to be transmitted, being the most common, operational data.

**_5.3.1.4. Stage 4 - data provision and consumption in the IDS ecosystem._** The AAS data created in the previous step is moved to the local IDS connector, where it is published according to the IDS principles. A data usage contract is established, allowing access to the data to the specific IDS connector running on the DataSpace4Consumer domain. An IDS notification is then sent to the DataSpace4Consumer’s connector, which will trigger the contract agreement and subsequently the exchange of data from the provider’s connector to the consumer’s connector. The process is controlled by the two DataSpaceApp4EDI instances.

**_5.3.1.5. Stage 5 - reception of data._** Finally, at the latest stage, the Data Preparation App receives the JSON data from the DataSpaceApp4EDI, via a push request, and reconstructs the file. Making it usable for the digital data-driven services.

###### _5.4. Implementation and testing settings_

Following the case study’s development, it was now necessary to verify the veracity of the proposed concepts and applications in a real industrial environment. Within the case study context, one Portuguese Industrial Enterprise (PIE) and one Spanish Industrial Enterprise (SIE) were used as testers. Thus requiring the installation of the IDS connector and the enablers applications at the two different locations.

In Figure 16 it is possible to showcase the technical operation process. The scheme comprises three instances: PIE, SIE, and supplier (i.e. the Portuguese machine producer/ maintainer). Both the tester enterprise are composed of a machine with a machine controller, the machine data server, the Monitor App and DataSpace4Provider. The supplier comprises a Data Preparation App and the DataSpace4Consumer.

###### _5.5. Services_

###### _5.5.1. Integrated performance and maintenance service (IPMS)_

Integrated Performance and Maintenance Service, composed of innovative data-driven services, will support metal and plastic companies to define conditioned/preventive maintenance plans, leveraged on real-time machine parameters while monitoring, calculating, and enhancing visibility on machine OEE-based online dashboards. Part of the data-driven services available on this App will be leveraged on the data and parameters collected in real-time from manufacturing machines to a platform that will compile and process the data to generate web-based dashboards and intelligence related to machine usage and performance. Moreover, the IPMS architecture enables monitoring the machines while processing and accessing data generated by them.

**_5.5.1.1. Use case story._** The user wants to monitor their machine so that the user can log enter the web application Integrated Performance and Maintenance Service. Once on the page, the user will be asked to introduce their credentials. If the user does not have his login credential yet, he can click the ‘Request your login info’ link and be redirected to the login request form, which will send the client’s information to the service provider. When that process is concluded, the user will receive his login credential and be able to access the main page of the maintenance app.

After the successful login, the user will access all the production and maintenance functionalities. The user will select the desired machine in which he desires to overview the available data. Once a machine is selected, the user can interact with the dashboard to see detailed data. The user can choose _‘Productivity Monitor’_ to view production data or _‘Maintenance’_ to view maintenance data and/or schedule maintenance with the Portuguese machine manufacturing company.

On the _Productivity Monitor_ , firstly, the user will be displayed a list with information about the selected machine (e.g. refresh time, start log time, end log time, strokes in a log, machine status, working hours, and serial number). In addition, on the _Productivity Monitor_ , the user will also have access to several lists and charts, namely a: Product overview, product in time, machines mode in time, strokes and started in time, message overview, and messages in time.

Finally, the user on the _Maintenance_ can see the status of their machines’ maintenance list. When the current working hours reach one of the marks (500, 1000, 1500, 4000 hours), the icons will change (colour code, Green – OK, Yellow – Pending, and Red – Not OK). If the client gets a ‘Red’ a button will appear and it will be possible to contact the Portuguese machine producer/maintainer and schedule maintenance.

###### _5.5.2. Machine configurator app (MCA)_

The supply of manufacturing equipment is ever rising, and finding the desired machine is often associated with spending hours on research or direct contact with the manufacturing industries. Having the concept of Market 4.0 in mind, the MCA aims to introduce machinery in the Market 4.0 catalogue and enable metal and plastic companies to find and configure cutting and bending machines according to their specific needs in a straightforward manner.

For this to happen, it is necessary for the manufacturing industries in Market 4.0 to define the parameters referring to each machine’s general use. Said parameters include information regarding the machine: type and process variables such as minimum/maximum thickness, material to be processed, bending force/length, maximum size in each direction (x,y,z), cutting angle, and engine power. Machinery data will be available for the MCA through an IDS connector that ensures data protection. Furthermore, the MCA architecture supports the Machine Configurator App, this App will also be available in Market 4.0 and aims to create a direct connection between the customer and the Portuguese machine producer/maintainer with the same premise of the MCA.

**_5.5.2.1. Use case story._** The user wants to have access to a list of machines that fit their needs so that the user can enter the web application Machine Configurator App. Once entered on the web application, it will be asked to the user to specify the desired type of material to be processed (e.g. steel, aluminium, zinc), the sub-category of the selected (e.g. when selected steel, the user can then select stainless steel) and the tensile strength of said material. Afterwards, the user will be able to adjust the material measurements to be processed (e.g. thickness and length). The user will then be presented with a list of machines that fit their criteria and will be asked to select the desired machine. On this list of machines is possible to see a bar chart with five parameters (total force, length, accuracy, general speed, and structural performance) for each machine to obtain a better understanding of the machine’s capabilities.

After choosing a machine, the user can tailor machine components (e.g. mechanical add-ons, control system, tolls). When choosing an add-on, it is possible to see on a radar graph (composed by: total force, length, accuracy, general speed, structural performance, stroke range, energetic efficiency, software power, and ergonomics) how will the chosen add-on influence the machine stats. Finally, the user will send a quotation request for the machine he customized directly to the manufacturing company.

###### _5.6. Final feedback report_

This section will present the feedback received from the two manufacturing enterprises members of the Case Study Consortium. Both enterprises own machines from the Portuguese machine producer/maintainer present in this Case Study and leveraged from the proposed services for two weeks. The feedback was obtained through unstructured individual interviews regarding their experience with the two services.

###### _5.6.1. Portuguese industrial enterprise_

**_5.6.1.1. Integrated Performance and Maintenance Service._** PIE production department used the IPMS with a machine integrated and running on their facilities. The feedback received on this application was very positive. PIE found the real-time data displayed in the interactive dashboards very useful and that through the use of these dashboards, it was possible to track the status of the machine over time, with the idle, setup, and producing times. It was also commented that the cycle time display for a part to be produced was of great interest. With this indicator, it was possible to track and monitor the minimum, average and maximum cycle time of production, thus, allowing PIE to understand the potential for efficiency improvement in the production. When it comes to the maintenance functionalities of the IMPS, PIE finds it very helpful since the maintenance plan is self-tracked and easy to follow.

In terms of improvements, it was highlighted that it would be interesting to add additional filters as well as an integrated overall dashboard for the entire facility. Automatic notifications and predictive alerts would also be an interesting add-on to be developed and added to the maintenance functionalities of the IPMS.

Overall, the feedback received in the meeting was very positive. The IPMS proved to have great potential and can be further developed to be used in production with all the machines integrated into one single holistic dashboard.

**_5.6.1.2. Machine configurator app._** PIE used the Machine Configurator App to simulate the buying process of the Portuguese machine producer/maintainer and commented that it was well designed and with great usability. The selection of the best solutions for the requirements introduced was very helpful. It was also highlighted that the possibility of configuring several add-ons and checking the machine characteristics in real-time improvement was of great interest. PIE also enjoyed that it is possible to send the request for quotation directly to the manufacturer at the end of the process.

###### _5.6.2. Spanish industrial enterprise_

**_5.6.2.1. Integrated Performance and Maintenance Service._** SIE production department used the IPMS for some months on a production machine integrated and running on its premises. SIE found the product overview functionality a powerful tool that enables them to overview the number of parts, the maximum, average, and minimum production timer per product reference. It was also of great interest for SIE to calculate the total amount of time it took to produce an order and compare values with the potential minimum (optimal) production time. This allowed for SIE to have a window with the potential improvement time. Furthermore, it gave SIE the machine performance per product as well as the real improvement potential. Regarding the maintenance functionalities, SIE found it very helpful to track the machinery time usage and easy to follow.

When it comes to improvements, SIE noted that in the maintenance functionalities, some general parameters were not part of some machines and suggested having the maintenance plans not as general and more built to each machine.

**_5.6.2.2. Machine configurator app._** SIE used the Machine Configurator App to simulate the buying process of Machinery and commented that it was an innovative application of great interest. From their point of view, it was a remarkable alternative to traditional commercial catalogues and very helpful for them to start the evaluation and decision process of the best suitable machine to meet the company’s requirements. Furthermore,

SIE found it a powerful tool to support their decision-making process and start the commercial negotiation with the Portuguese machine producer/maintainer.

###### _5.7. Project limitations_

Throughout the project timeline, some challenges and/or limitations arose, this section aims to expose said challenges/limitations. The case study follows the three concepts presented in Chapter 4. The installation process of the IDS connectors and applications was also very limited, considering the pandemic limitation and travel restrictions.

When it comes to the Asset Administration Shell, this is an innovative concept, but it is also a newly developed concept. At the time of the Case Study timeline, there were limited frameworks capable of deploying reactive AAS. This limited the file generation made by the machine controller. For this reason, the generated file used is a JSON formatted file not entirely within the AAS standards.

In the Digital Twin concept, the initial design and plan was in fact for a functional DT but faced with the close deadlines and difficulty associated with a DT it was established a functional Digital Shadow.

##### 6. Main conclusions and future work

###### _6.1. Main conclusions_

Throughout this research paper, it was highlighted the importance of keeping up-to-date with Industry 4.0 technologies in order to remain competitive in the manufacturing environment. We live in a digitalization era that is enforcing the usage of digital datadriven services that uses data as a manufacturing asset. This raises the question of establishing secure data streams between the manufacturing shop floor and the providers of the digital data-driven services while still ensuring data security, ownership, and sovereignty. To further, this also stresses the need for standardization of services to achieve a common understanding in terms of the deployment of data.

To answer these questions, the presented paper proposes an adaptive architectural model for Digital Twins of manufacturing types of equipment within Industry 4.0. The architectural model leverages: (1) the usage of the International Data Spaces initiative to create secure channels of communications, ensuring data ownership, sovereignty, and security, (2) a conceptual implementation of the Asset Administration Shell to achieve interoperability. Through this, it is possible to safely connect the manufacturing shop floor with the digital space while on one hand, ensuring data security, ownership, sovereignty, and on the other hand, ensuring standardization of information models easing the implementation process of the digital data-driven services.

Overall, this paper successfully achieved and contributed to the development of a general DT architecture. Implemented in two different case studies, proving the flexibility and veracity. When revising the RQ previously defined it is possible to conclude:.

- **RQ1** : _How can the ‘Digital Twin’ and the ‘Asset Administration Shell’ concepts be applied at the production systems level to manage and control machines along their life cycle?_

The Digital Twin can be used to monitor a physical machine and leverage its digital capabilities to monitor and prevent a machine’s performance along its entire lifecycle. As stated in Figure 12, the DT can follow and support the physical machine in its entire lifecycle. Supporting the customization and design of a physical product through developing a digital model. The DM test the physical machine implementation, resulting in a reduced amount of physical testing on the manufacturing shop-floor. The installation of the physical object marks the conversion from DM into DT/DS. The Digital Twin can process the machine-generated data’s affluence and provide an interface for the machineowner to monitor remotely. DT can also gather maintenance and performance data to calculate KPIs such as the OEE. At the end of a machine’s lifecycle, the Digital Twin can provide information regarding machine parts that can be re-utilized. The use of AAS heavily benefits the Digital Twin throughout the physical product lifecycle.

Furthermore, through the usage of the Asset Administration Shell to deploy DTs, it is possible to achieve interoperability within digital data-driven service providers and manufacturing industries. Thus, constituting a common ground and common understating that can lead to the development of DT templates, easing the implementation and development phases of the DT. This AAS can be used within the OPC-UA protocol to expedite the communication with machines in a standardized way.

- **RQ2** : _What new kinds of business models can be created leveraged on the secure and trustable data communication between physical machines and data-driven service providers?_

This research question demonstrated the importance of IDS. With trusted communication channels between physical machines and digital data-driven services, it is possible to enhance the customer experience and capitalize on this. With secure data exchange, the machine manufacturer, in addition to selling a machine, can sell and provide data-driven services that will generate additional subscription revenue. Furthermore, it can utilize data-driven services to provide high-level assistance, giving the customer a straightforward way to schedule maintenance. Empowering the concept of smart product lifecycle management while promoting sustainable and green business models. These business models will leverage the usage of historical data to promote remanufacturing of the physical asset components in future designs, leading to a reduction in waste.

Section 5.5, introduced two services created in the Case Study that enabled the Portuguese machine producer/maintainer to generate new channels of revenue.

- **RQ3** : _How can Digital Twin and new secure data communication infrastructures can leverage the introduction of new B2B marketplaces?_

Through the deployment of Digital Twins complaints with the Asset Administration Shell concept, the standardization and interoperability requirements for industrial B2B marketplaces are met. Data economy, on the other hand, will serve as the foundation of B2B marketplaces given the usage of the International Data Spaces connector to support the communication layer of the Digital Twin. The introduction of new digital B2B marketplaces, thereby, enables to enhance and personalize the customer experience, whilst introducing resilience to overcome volatile and complex circumstances such as the COVID-19 pandemic bringing costumers and providers together.

###### _6.2. Future work_

Although the overall implementation of the developed concept was a success, there is still room and opportunity to improve. In Section 5.7 it was exposed room for improvement of the Case Study. Therefore, when it comes to future work, the focus points are:

• _Implementation of functional Digital Twin_ In the Case Study, it was formulated a functional Digital Shadow; nonetheless, in the near future, this should be updated to a functional Digital Twin that should be able to act upon the physical machine. Detect critical levels of usage and, through the digital capabilities, perform preventive maintenance.

• _Extending the research for reactives/proactives AAS_ There is still a need for public frameworks capable of deploying proactive AAS. Thereby, the AAS-related projects are going to be closely followed and analyzed to verify the ability to implement a software capable of deploying proactive/reactive AAS in our approach.

• Extend the presented model to other case studies The presented architectural model was developed with the aim to be easily adapted into different manufacturing contexts. Currently, the presented concept model is being used in a new case study, intending to verify and demonstrate the flexibility and veracity of the proposed model. The new case study’s scope consists of using Digital Twins to manage the power transformers’ (PT) lifecycle by digitalizing its entire lifecycle and providing digital data-driven services to generate new opportunities at each stage. Given the extended life span of power transformers, this opens new business opportunities for power transformers manufacturers to extend their services, in addition to selling a product it is possible to also sell a service that generates additional value for the power transformer owners and additional revenue streams to the manufacturers. This also enables innovative opportunities to provide predictive maintenance, identify patterns that might lead to malfunctions, and obtain the product status assurance of the different components that can be reclaimed for refurbishing or re-manufacturing.

##### Notes

1. <https://internationaldataspaces.org/>.

2. https://github.com/eclipse-dataspaceconnector/DataSpaceConnector.

3. https://github.com/International-Data-Spaces-Association/DataspaceConnector.

4. https://github.com/Engineering-Research-and-Development/true-connector.

5. https://industrialdigitaltwin.org/.

7. https://gaia-x.eu/.

8. http://market40.eu/.

6. https://github.com/FraunhoferIOSB/FAAAST-Service.

9. https://github.com/eclipse-basyx/basyx-python-sdk.

10. https://github.com/International-Data-Spaces-Association/DataspaceConnector.

##### Disclosure statement

##### Funding

No potential conflict of interest was reported by the authors.

This work is financed by National Funds through the Portuguese funding agency, FCT - Fundação para a Ciência e a Tecnologia, within project **LA/P/0063/2020.**

##### ORCID

##### References

Tomás Moreno http://orcid.org/0000-0001-8243-9583 António Almeida http://orcid.org/0000-0001-9203-5144 César Toscano http://orcid.org/0000-0002-6056-6917 Filipe Ferreira http://orcid.org/0000-0001-7824-3537 Américo Azevedo http://orcid.org/0000-0002-9659-5488

- Aheleroff, S., Mostashiri, N., Xu, X., & Zhong, R. Y. (2021). Mass personalisation as a service in industry 4.0: A resilient response case study. _Advanced Engineering Informatics_ , _50_ (June), 101438. https://doi.org/10.1016/j.aei.2021.101438

- Aheleroff, S., Xu, X., Zhong, R. Y., & Lu, Y. (2021). Digital twin as a service (DTaaS) in industry 4.0: An architecture reference model. _Advanced Engineering Informatics_ , _47_ (August 2020), 101225. https://doi.org/10.1016/j.aei.2020.101225

- Arabnia, H. R., Deligiannidis, L., & Tinetti, F. G. (2018). _Frontiers in education_ . Computer Science and Computer Engineering.

- Bader, S., Barnstedt, E., Bedenbender, H., Billman, M., Boss, B., & Braunmandl, A. (2020). Details of the asset administration shell part 1 - the exchange of information between partners in the value chain of industrie 4.0. _Plattform Industrie_ , _4_ (0), 473.

- Bazaz, S. M., Lohtander, M., & Varis, J. (2020). Availability of manufacturing data resources in digital twin. _Procedia Manufacturing_ , _51_ , 1125–1131. https://doi.org/10.1016/j.promfg.2020.10.158

- Belyaev, A., Block, C., Boss, B., Diedrich, C., Juhel, P., Hartmann, W., Hillermeier, O., Ondracek, N., Pfeifer, S., Scherenschlich, F., & Schmelter, J. (2021). Modelling the semantics of data of an asset administration shell with elements of ECLASS. 54. https://www.plattformi40.de/PI40/Redaktion/DE/Downloads/Publikation/Whitepaper_Plattform-Eclass.pdf?__blob= publicationFile&v=11

- Bhandari, P. (2020). An introduction to qualitative research. https://www.scribbr.com/methodol ogy/qualitative-research/

- Cai, Y., Starly, B., Cohen, P., & Lee, Y. S. (2017). Sensor data and information fusion to construct digital-twins virtual machine tools for cyber-physical manufacturing. _Procedia Manufacturing_ , _10_ , 1031–1042. https://doi.org/10.1016/j.promfg.2017.07.094

- Federal Ministry for Economic Affairs and Energy. (2019). _Plattform Industrie 4.0 - RAMI4.0 – a reference framework for digitalisation_ . Plattform Industrie 4.0.

- Grieves, M. (2014). Digital twin: Manufacturing Excellence through Virtual Factory Replication - a whitepaper by Dr. Michael Grieves. White Paper, March, 1–7.

- Hermann, M., Pentek, T., & Otto, B. (2015). Design principles for industrie 4.0 scenarios: A literature review. _Technische Universitat Dortmund_ , _1_ (1), 4–16. https://doi.org/10.13140/ RG.2.2.29269.22248

- Hofmann, E., & Rüsch, M. (2017). Industry 4.0 and the current status as well as future prospects on logistics. _Computers in Industry_ , _89_ , 23–34. https://doi.org/10.1016/j.compind.2017.04.002

- Huber, M., Wessel, S., Brost, G., & Menz, N. (2022). Building trust in data spaces. In B. Otto, M. ten Hompel, & S. Wrobel (Eds.), _Designing data spaces_ . Springer. https://doi.org/10.1007/ 978-3-030-93975-5_9

- IDSA. (2019). IDS – A STANDARD FOR DATA SOVEREIGNTY AND AN INDISPENSABLE ELEMENT OF DATA ECOSYSTEM. International Data Spaces Association. Whitepaper.

- Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. (2018). Digital twin in manufacturing: A categorical literature review and classification. _IFAC-PapersOnline_ , _51_ (11), 1016–1022. https://doi.org/10.1016/j.ifacol.2018.08.474

- Leng, J., Wang, D., Shen, W., Li, X., Liu, Q., & Chen, X. (2021). Digital twins-based smart manufacturing system design in industry 4.0: A review. _Journal of Manufacturing Systems_ , _60_ (May), 119–137. https://doi.org/10.1016/j.jmsy.2021.05.011

- Li, G., Hou, Y., & Wu, A. (2017). Fourth industrial revolution: Technological drivers, impacts and coping methods. _Chinese Geographical Science_ , _27_ (4), 626–637. https://doi.org/10.1007/s11769017-0890-x

- Lu, Y., Liu, C., Wang, K. I. K., Huang, H., & Xu, X. (2020). Digital Twin-driven smart manufacturing: Connotation, reference model, applications and research issues. _Robotics and computerintegrated manufacturing_ , _61_ , 101837. https://doi.org/10.1016/j.rcim.2019.101837

- Luthra, S., & Mangla, S. K. (2018). Evaluating challenges to industry 4.0 initiatives for supply chain sustainability in emerging economies. _Process Safety and Environmental Protection_ , _117_ , 168–179. https://doi.org/10.1016/j.psep.2018.04.018

- Moreno, T., Almeida, A., Ferreira, F., Caldas, N., Toscano, C., & Azevedo, A. (2021). Digital twin for manufacturing equipment in industry 4.0. _Advances in Transdisciplinary Engineering_ , _15_ , 362–367. https://doi.org/10.3233/ATDE210062

- Nast, M., Rother, B., Golatowski, F., Timmermann, D., Leveling, J., Olms, C., & Nissen, C. 2020. Work-in-progress: Towards an international data spaces connector for the internet of things. IEEE Int. Work. Fact. Commun. Syst. - Proceedings, WFCS. 2020-April. https://doi.org/10. 1109/WFCS47810.2020.9114503 .

- Ocker, F., Urban, C., Vogel-Heuser, B., & Diedrich, C. (2021). Leveraging the asset administration shell for agent-based production systems. _IFAC-PapersOnline_ , _54_ (1), 837–844. https://doi.org/ 10.1016/j.ifacol.2021.08.186

- Otto, B. (2022). The evolution of data spaces. In B. Otto, M. ten Hompel, & S. Wrobel (Eds.), _Designing data spaces_ . Springer. https://doi.org/10.1007/978-3-030-93975-5_1

- Otto, B., Steinbuß, S., Teuscher, A., Lohmann, S., Auer, S., Bader, S., Bastiaansen, H., Bauer, H., Birnstil, P., Böhmer, M., Bohn, J., Böge, G., Brettner, U., Brost, G., Ceballos, G., Cirullies, J., Corsi, E., Dalmolen, S., Danielsen, S., Duisberg, A., et al. (2019). International data spaces reference architecture model version 3.0. _April_ .

- Pettenpohl, H., Spiekermann, M., & Both, J. R. (2022). International data spaces in a nutshell. In B. Otto, M. ten Hompel, & S. Wrobel (Eds.), _Designing data spaces_ . Springer. https://doi.org/10. 1007/978-3-030-93975-5_3

- Piccarozzi, M., Aquilani, B., & Gatti, C. (2018). Industry 4.0 in management studies: A systematic literature review. _Sustainability (Switzerland)_ , _10_ (10), 1–24. https://doi.org/10.3390/su10103821

- Pribiš, R., Beňo, L., & Drahoš, P. (2021). Asset administration shell design methodology using embedded opc unified architecture server. _Electronics (Switzerland)_ , _10_ (20), 2520. https://doi. org/10.3390/electronics10202520

- Qi, Q., Tao, F., Hu, T., Anwer, N., Liu, A., Wei, Y., Wang, L., & Nee, A. Y. C. (2021). Enabling technologies and tools for digital twin. _Journal of Manufacturing Systems_ , _58_ (October 2019), 3–21. https://doi.org/10.1016/j.jmsy.2019.10.001

- Qi, Q., Tao, F., Zuo, Y., & Zhao, D. (2018). Digital twin service towards smart manufacturing. _Procedia CIRP_ , _72_ (June), 237–242. https://doi.org/10.1016/j.procir.2018.03.103

- Radziwon, A., Bilberg, A., Bogers, M., & Madsen, E. S. (2014). The smart factory: Exploring adaptive and flexible manufacturing solutions. _Procedia Engineering_ , _69_ , 1184–1190. https://doi. org/10.1016/j.proeng.2014.03.108

- Rajendran, S., & Pagel, E. (2020). Insights on next-generation manufacturing of smart devices using text analytics. _Heliyon_ , _6_ (7), e04491. https://doi.org/10.1016/j.heliyon.2020.e04491

- Redeker, M., Weskamp, J. N., Rössl, B., & Pethig, F. (2022). A digital twin platform for industrie 4.0. In E. Curry, S. Scerri, & T. Tuikka (Eds.), _Data Spaces_ . Springer. https://doi.org/10.1007/ 978-3-030-98636-0_9

- Rolle, R. P., Martucci, V. D. O., & Godoy, E. P. (2019). Digitalization of manufacturing processes: Proposal and experimental results. 2019 IEEE International Workshop on Metrology for Industry 4.0 and IoT, MetroInd 4.0 and IoT 2019 - Proceedings, June, 426–431. https://doi. org/10.1109/METROI4.2019.8792838

- Rosen, R., Von Wichert, G., Lo, G., & Bettenhausen, K. D. (2015). About the importance of autonomy and digital twins for the future of manufacturing. _IFAC-PapersOnline_ , _48_ (3), 567–572. https://doi.org/10.1016/j.ifacol.2015.06.141

- Sanders, A., Elangeswaran, C., & Wulfsberg, J. (2016). Industry 4.0 implies lean manufacturing: Research activities in industry 4.0 function as enablers for lean manufacturing. _Journal of Industrial Engineering and Management_ , _9_ (3), 811–833. https://doi.org/10.3926/jiem.1940

- Santos, R., Basto, J., Alcalá, S. G. S., Frazzon, E., & Azevedo, A. (2019). Industrial IoTintegrated with simulation -A digital twin approach to support real-time decision making. Proceedings of the International Conference on Industrial Engineering and Operations Management, July (pp. 816–828). IEOM Society International

- Schleich, B., Anwer, N., Mathieu, L., & Wartzack, S. (2017). Shaping the digital twin for design and production engineering. _CIRP Annals - Manufacturing Technology_ , _66_ (1), 141–144. https://doi. org/10.1016/j.cirp.2017.04.040

- Schweichhart, K. (2019). RAMI 4.0 reference architectural model for industrie 4.0. _InTech_ , _66_ (2), 15. Silva, H. D., Azevedo, M., & Soares, A. L. (2021). A vision for a platform-based digital-twin ecosystem. _IFAC-PapersOnline_ , _54_ (1), 761–766. https://doi.org/10.1016/j.ifacol.2021.08.088

- Stojanovic, L., Usländer, T., Volz, F., Weißenbacher, C., Müller, J., Jacoby, M., & Bischoff, T. (2021). Methodology and tools for digital twin management–The FA3ST approach. _IoT_ , _2_ (4), 717–740. https://doi.org/10.3390/iot2040036

- Tao, F., Qi, Q., Wang, L., & Nee, A. Y. C. (2019). Digital twins and cyber–physical systems toward smart manufacturing and industry 4.0: Correlation and comparison. _Engineering_ , _5_ (4), 653–661. https://doi.org/10.1016/j.eng.2019.01.014

- Tao, F., Sui, F., Liu, A., Qi, Q., Zhang, M., Song, B., Guo, Z., Lu, S. C. Y., & Nee, A. Y. C. (2019). Digital twin-driven product design framework. _International Journal of Production Research_ , _57_ (12), 3935–3953. https://doi.org/10.1080/00207543.2018.1443229

- Thames, L., & Schaefer, D. (2016). Software-defined cloud manufacturing for industry 4.0. _Procedia CIRP_ , _52_ (September), 12–17. https://doi.org/10.1016/j.procir.2016.07.041

- Tissir, S., Fezazi, S. E., & Cherrafi, A. (2020). Industry 4.0 impact on lean manufacturing: literature review. 2020 13th International Colloquium of Logistics and Supply Chain Management, LOGISTIQUA 2020, 2–4. https://doi.org/10.1109/LOGISTIQUA49782.2020.9353889

- Wang, Y., Towara, T., & Anderl, R. (2017). Topological approach for mapping technologies in reference architectural model industrie 4.0 (RAMI 4.0). _Lecture Notes in Engineering and Computer Science_ , _2_ , 982–990. 2078-0966.

- Zhang, C., Xu, W., Liu, J., Liu, Z., Zhou, Z., & Pham, D. T. (2019). A reconfigurable modeling approach for digital twin-based manufacturing system. _Procedia CIRP_ , _83_ , 118–125. https://doi. org/10.1016/j.procir.2019.03.141
