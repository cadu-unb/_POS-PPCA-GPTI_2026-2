# LogForum

**2024, 20 (3), 297-306**

> Scientific Journal  of  Logistics < <u>https://doi.org/10.17270/J.LOG.001054</u> http://www.logforum.net <u>p-ISSN 1895-2038</u> e-ISSN 1734-459X

ORIGINAL PAPER

## A DIGITAL TWIN FRAMEWORK FOR CYBER-PHYSICAL WASTE STREAM CONTROL SYSTEMS: TOWARDS REVERSE LOGISTICS 4.0

## Robert Giel, Alicja Dąbrowska

Department of Technical Systems Operation and Maintenance, Faculty of Mechanical Engineering, Wroclaw University of Science and Technology, Poland, Wroclaw, **Poland**

**ABSTRACT. Background:** With socio-economic development, an increase in waste generation is observed. In view of its negative impact on the environment and human health, it is becoming increasingly important to follow the waste hierarchy and perform research on reverse logistics. It is crucial to maximize the efficiency of the separation of the waste mixture into fractions which can be returned to the material cycle in the economy. The separation process is carried out in systems such as waste sorting plants, which are characterized by complexity and variable input waste stream composition. Therefore, research in this field is usually based on simplifying assumptions and static input-output data and limited in scope. There is a lack of studies dedicated to the real-time control of these systems.

**Methods:** We propose a Digital Twin framework for waste sorting systems to address the limitations of solutions available in the literature and to standardize the development of cyber-physical waste stream control systems. The proposed approach includes one of the key technologies of Industry 4.0, so it is in line with the Reverse Logistics 4.0 concept.

**Results:** The main components of the Digital Twin considered were a sensor-based waste stream monitoring system, a physical model of the sorting system, a simulation model and its integration with the physical model. The deployment of a Digital Twin in line with the presented framework is demonstrated using the example of a selected plastic waste sorting plant.

**Conclusions:** Based on the proposed approach, it is possible to include waste stream features (heterogeneity, composition uncertainty and high variability) in logistics decision-making in detail and in real time. The implementation of a Digital Twin can reduce the amount of waste sent to landfill and significantly increase the achieved recovery rates, thus increasing the amount of waste being reused and thereby contributing to the transformation to a circular economy.

**Keywords:** reverse logistics, cyber-physical system, waste management, waste sorting, Digital Twin

### INTRODUCTION

Reverse logistics refers to the sequence of activities necessary to collect used products from customers with the aim of either reusing, repairing, re-manufacturing, recycling, or disposing of them [Agrawal et al.  2015]. Recent studies show that it positively affects economic and environmental performance [Waqas et al. 2021] as well as competitiveness and society [Ivanova et al.  2022]. Industry 4.0 technologies can be used to solve research problems in many scientific fields, including reverse logistics. Sustainable management of material flows and activities aimed at value recovery and/or proper disposal of end-of-life products utilizing datadriven and smart technologies comprehensively defines the core of Reverse Logistics 4.0 [Sun et al.  2022]. The key processes to consider here are waste collection, sorting and pre-processing, transportation, value recovery and disposal. Within the municipal waste context, waste generated from non-industrial human activities is stored in waste bins. It is then collected by garbage trucks and transported to treatment facilities to address the recommended waste hierarchy and minimize disposal processes. Crucial from the point of view of the circular economy concept (from extraction of raw materials, production and consumption to reuse and recovery) are the treatment processes targeted at recovery and reduction of the impact of waste on the environment.

Copyright: Wyższa Szkoła Logistyki, Poznań, Polska **_Citation:_** _Giel R., Dąbrowska A., 2024. A Digital Twin framework for cyber-physical waste stream control system towards Reverse Logistics 4.0. LogForum 20 (3), 297-306,_ <u>https://doi.org/10.17270/J.LOG.001054</u> Received: 08.04.2024, Accepted: 22.06.2024, on-line: 01.09.2024

The initial step in waste treatment is the separation of waste into fractions that have or do not have value for recycling. Separation by manual and mechanical/automatic techniques is carried out in systems such as a Material Recovery Facility (MRF), a mechanicalbiological treatment plant (MBT) or a waste sorting plant. In these systems, the waste stream is transported by conveyors between elements separating the stream (e.g. manual sorting stations, air classifiers, eddy current separators, NIR separators). In addition to separating elements, there are also supporting elements such as shredders or balers that do not have a separating function but help with the initial and/or final stages of processing by reducing volume or particle size.

The major source of challenges with sorting systems management is the high, uncontrollable heterogeneity and composition variability of the municipal solid waste stream [Tanguay-Rioux et al.  2022]. These characteristics are repeatedly cited as a reason for the difficulties in optimizing waste processing to maximize the recovery of recyclable materials [Tanguay-Rioux et al.  2021].

Research in the field of waste sorting facilities mainly focuses on design issues (the design of emerging systems or the modernization of existing ones), the evaluation of various aspects, modeling and experimental studies, as summarized in Table 1.

Table 1. Summary of the main research topics in the field of municipal waste sorting plants

|Research topic|Problems considered|Methods/approaches|
|---|---|---|
|modelling|binary separation [Gutowski et al.  2007], multi-material<br>separation [Malima I. Wolf et al.  2010], recirculation [Malima<br>Isabelle Wolf et al.  2013]|Material Flow Analysis [Arena and Di<br>Gregorio  2014; Eriksen et al.  2018], Linear Circuit<br>Analysis [Luttrell et al.  2004], mechanistic models<br>[Tanguay-Rioux et al.  2022], simulation modelling<br>[Van Schaik et al.  2002]|
|assessment|technical [Cimpan et al.  2016; Feil et al.  2016; Mastellone et<br>al.  2017], environmental [Ardolino et al.  2017; Cherubini et<br>al.  2009; Hossain et al.  2017], and economic [Medina-<br>Mijangos et al.  2021; Oliveira Neto et al.  2017] aspects|Life Cycle Assessment|
|design|system localization [Pluskal et al.  2021] and  structure options<br>(configuration, number and type of elements) [Al-Athamin et<br>al.  2021], separation technologies [Heidari et al.  2019; Zhao<br>and Li  2022]|FEM, linear programming, TOPSIS, multi-indicator<br>analysis|
|experimental<br>studies|the impact of selected factors (e.g., throughput [Küppers et<br>al.  2020], seasonal variations [Ashkiki et al.  2019]) on system<br>performance|regression|

The main limitations of methods dedicated to waste sorting facilities are the following: fixed morphology and stream size, ignoring reliability issues, static input-output models, long time horizon, concentration on operational matters (without maintenance), single-criteria or multiindicator approaches, limited scale (most often only selected elements are studied in detail). In addition, the basis of currently available methods is historical data collected over a long time horizon with a low collection frequency (usually monthly reports). As a result, it is impossible to respond quickly to stream variability in the form of changes in system parameters aimed at maximizing operational and reliability indicators.

The indicated limitations of the methods available in the literature can be eliminated with the use of technologies enabling the Industry 4.0 concept. Those technologies can be used to address new research problems in many scientific fields. Consequently, it is observed that new terminology is being introduced in the literature to clearly indicate the relationship of the proposed solutions with Industry 4.0. In the considered field, the term Waste Management 4.0 has emerged as a cyber-physical integrated waste management system in which the physical waste infrastructure is connected with a digital platform through smart technologies for accurate, reliable and real-time data [Zaman  2022]. A summary of current solutions that are in line with this concept is provided in Sarc et al.  [2019]. Among other things, smart bins for the optimization of waste collection in the context of the Internet of Things, automated and intelligent waste segregation by image recognition and robotics, monitoring systems for landfill and composting were highlighted. In a similar review [Sarc et al.  2019], digitalization and the use of robotics in waste management were considered. The results were divided into four topics: collection and logistics, machines and waste treatment plants, business models and data tools. Under these headings, smart bins, selfautomated containers and vehicles, automatic image analysis, waste sorting by robotic technologies and real-time data recording and utilization were presented. It has been stated that digitalization and robotics in the waste management sector are still in their infancy (in comparison to other industrial sectors). It is noticeable that solutions in the area of waste sorting are focused on the implementation of robots and the development of automatic waste classification systems. The waste sorting plant has not yet been considered holistically as a cyber-physical system. Only in Konstantinidis et al.  [2022] has a multi-sensor cyber-physical sorting system been proposed, but the focus is on the robot-based sorting line.

Based on the above, it is reasonable to consider Digital Twin technology in the context of waste sorting facilities. The objective of this article is to present the framework for a cyberphysical waste stream control system, i.e., the Digital Twin of the waste sorting system.

### MATERIALS AND METHODS

The architecture of the Digital Twin indicates the presence of three basic components: the physical system, a digital copy of the physical system and a bidirectional connection between them. In line with this, ISO 23247 (Digital Twin Framework for Manufacturing) partitions a digital twinning system into four layers (Figure 1):

- observable manufacturing domain – all observable manufacturing resources such as personnel, equipment, material, process or environment. This domain is outside the scope of the Digital Twin framework, but is presented as a basis for its development,

- device communication domain – sensors for data collection from the observable manufacturing elements and for control of manufacturing devices,

- Digital Twin domain – management functionalities for digital twins such as visualization, synchronization, data analytics, simulation, and optimization,

- • user domain – hosting applications that analyze Digital Twin models for humans and systems.

Fig. 1. Domain-based Digital Twin reference model for manufacturing [ISO 23247]

The given framework is dedicated to manufacturing systems. However, it can be adapted to waste sorting systems by including their key elements and processes. By matching the general four-layer structure of the twinning system to waste sorting, the following is obtained (Figure 2):

- observable waste sorting system’s elements – adopted decomposition of the waste sorting system must take into account the following elements: waste stream, stream separators/sorters/classifiers, stream transporters and stream processors, human sorters (in the case of manual sorting),

- data collection and control – observable elements of the waste sorting system determine the need to collect three types of data: stream-related, machine-related

- and human-related (in the case of manual sorting),

- core entity – real-time performance evaluation, failure detection and process optimization in terms of sorting accuracy and efficiency provided by a digital representation of the observable waste sorting system’s elements,

- user entity – facilitation of user interaction with Digital Twin and with observable waste sorting system elements.

Fig. 2. The Digital Twin framework for a waste sorting system based on ISO 23247

### RESULTS

The framework for a waste sorting Digital Twin considered in the article arises from an ongoing research project entitled “Cyberphysical waste stream control system” (CyPhisCTRL) funded by the National Centre for Research and Development. The project aims to develop a cyber-physical waste sorting system, i.e., a Digital Twin. The stages of the research work considered in the project reflect successive layers of the Digital Twin. These stages are as follows:

Stage I. Replication of the sorting system under laboratory conditions (real scale) and data collection system development

Without access to an existing waste sorting system, it is necessary to replicate it under laboratory conditions. However, it should be noted that waste sorting systems are complex systems consisting of multiple conveyors connecting successive points of separation and processing of the waste stream. An example structure of such a system is shown in Figure 3.

Fig 3. Scheme of a sample waste sorting plant

Constraints of time, cost and space in the initial stage of the study are the reason for representing only a fragment of the sorting facility at real scale. This approach is sufficient to consider data collection for the device communication layer. Stream-related, machinerelated and optionally human-related (in the case of manual sorting) data are limited to monitoring the stream characteristics at various stages of processing, which can be simulated using the following three elements under laboratory conditions:

- waste stream generator – representation of the feeder for generating the initial waste stream and representation of the output streams from various stream separation elements,

- conveyor belt – representation of conveyors from different stages of stream processing by including height, width and speed adjustments,

- municipal waste stream – collected samples of municipal waste allowing representation of variable morphology. The study focuses on the plastics and metal waste stream, which is crucial from the point of view of recycling. Accordingly, five fractions were prepared that fit the waste category: blue, white and green PET, tetrapak and aluminum.

For the replicated system fragment, it is possible to consider a layer of device communication. The proposed measurement system assumes the use of an RGB camera and a lidar sensor. The lidar sensor can provide a data stream related to volume based on the Time of Flight method (Figure 4). In this way, the contour of waste moving on the conveyor belt will be measured. The reference area will be the contour of the conveyor belt without waste. The difference between the reference area (defined by the contour of the empty conveyor and the scan field) and the field bounded by the waste contour will provide information on the size of the waste stream.

Fig 4. Volume stream size measurement method with the use of lidar sensor

In addition to the flow sensor, an RGB camera can be used to monitor the morphology of the stream (content of individual fractions in the waste stream), as shown in Figure 5. Supervised machine learning algorithms (classifiers) are widely used in such tasks.

Fig 5. Example of RGB camera use for stream morphology detection based on a machine learning algorithm

Combining the data from the flow sensor and RGB camera will return the estimated morphology and volumetric size of the stream, which can be translated into the mass size of the stream in the next step. The collected streamrelated data can also be used to monitor machine performance and failures in the form of analysis of the stream going in and out of a given separation or processing point. For manual sorting, it is additionally necessary to consider the issue of a Human Digital Twin using, for example, motion capture gloves.

Stage II. Representation of the sorting system under laboratory conditions (miniature) and experimental research

A fragment of the actual waste sorting system is sufficient for the initial stage of research when considering the device communication layer. Ultimately, a Digital Twin should represent the entire system. The measurement system developed in Stage I must therefore be multiplexed and deployed at the input and output of each stream separating and processing element. In order to be able to consider the waste sorting system holistically in the research, it is proposed that a miniature sorting plant be built to replicate the physical system in the research stage and eliminate space limitations. It will be necessary to develop a physical model that realizes the sorting process at a given scale.

In a sorting system, we can distinguish between stream-separating elements (which change the composition of the stream and use the properties of stream components such as density sorting, flotation, optic, magnetic, electrical or manual sorting, classification, separation), stream-processing elements (which do not change the composition of the stream but allow the change of particle size: comminution by crushing, tearing, shearing, splitting, crushing, grinding, and compaction by pressing, briquetting, granulating) and stream transportation (moving the stream between separation and processing elements). All these elements should be represented in the adopted scale, and then equipped with a multiplied measurement system from Stage I.

The developed miniature sorting plant will not only permit the reproduction of a real sorting plant in laboratory conditions, but will also be a basis for experimental research, the results of which (in the form of dependencies between

_Giel R., Dąbrowska A., 2024. A Digital Twin framework for cyber-physical waste stream control system towards Reverse Logistics 4.0. LogForum 20 (3), 297-306,_ <u>https://doi.org/10.17270/J.LOG.001054</u> stream characteristics and system performance) will be implemented in a digital copy of the sorting plant.

Stage III. Digital Twin development

To create the Digital Twin (the key layer in the twinning system), it is necessary to map the physical system (the miniature system in our research) in a virtual environment in the form of a simulation model. The simulation model of the waste sorting system can be made using Flexsim software. An example representation of the sorting system is shown in Figure 6.

Fig 6. Virtual representation of a waste sorting system based on the example from Fig. 3

When building the model, it is necessary to take into account key parameters from the point of view of sorting plant management. Namely, the model must enable control of the given waste stream (its volume and mass size and morphology), the conveyor system (particularly its speed and direction of movement), and human resources (changing the number of sorters in the case of manual sorting, changing the number of operators of selected machines). In addition, it is important to take into account the possibility of modifying the structure of the system, which will translate into the possibility of modernizing the system by introducing new machines, eliminating those that are currently used or changing the configuration. From the point of view of system performance evaluation, it is necessary to take into account indicators such as the sorting efficiency of each sorting point, the efficiency of each point, and its utilization and availability, as well as the total amount of processed waste, total efficiency and availability. Finally, the developed model should be integrated with reinforcement learning algorithms functioning as system optimization units.

### DISCUSSION

In recent years, there has been an intense development of Digital Twins across various fields (transport, manufacturing, human-related science, etc.). Although this technology has already been standardized in norms dedicated to manufacturing, applying a general framework to areas other than manufacturing remains a challenge. The framework presented in this article is dedicated to waste sorting systems and fits into the field of reverse logistics, playing a crucial role in the context of the promotion of a circular economy. The presented concept not only identifies the basic elements of a Digital Twin but also outlines appropriate steps to be taken and indicates solutions that allow for implementation.

In waste management, the greatest difficulty is the uncertainty of the size and composition of the processed waste stream, which results from the lack of monitoring of its parameters at various stages of the process. The proposed framework identifies solutions to eliminate this limitation.

The latest research directions in the field of waste sorting focus on the development of waste sorting technologies (e.g., spectroscopy, sorting robots), thus concentrating only on isolated fragments of the system (e.g., the NIR separator). A comprehensive approach to waste sorting systems rarely appears and often relies on inaccurate data based on the mass of processed and sorted waste. Considering Digital Twin technology in the context of waste sorting systems is a novel approach, and the presented stages of work outline the steps that need to be taken when implementing a Digital Twin in any waste sorting system.

### SUMMARY AND CONCLUSIONS

The article presents the framework for a cyber-physical waste stream control system, i.e., a Digital Twin of a waste sorting facility. The research under consideration is part of the Reverse Logistics 4.0 concept assuming sustainable management of material flows involving data-driven and smart technologies. A general Digital Twin framework for manufacturing has been adapted to the waste sorting system, taking into account its specific challenges. Problems arising from the features of the waste stream (heterogeneity, composition uncertainty and high variability), which have not been sufficiently considered in the literature have been addressed.

The proposed approach could play a significant role in improving waste sorting systems. It can translate into the reduction of waste sent to landfill and significantly increase achieved recovery rates and thus the amount of waste being reused.

The presented framework and research stages focused on the implementation of Digital Twins form a basis for considering the management of waste sorting systems in line with Reverse Logistics 4.0. Concentrating solely on selected elements of the system (e.g., research on NIR sorters) is insufficient in light of the requirement to increase the recycling rate. This article presents an innovative approach to managing waste sorting plants utilizing key technologies of Industry 4.0.

### ACKNOWLEDGMENTS

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

### REFERENCES

- Agrawal S., Singh R. K., Murtaza Q., 2015, A literature review and perspectives in reverse logistics, Resources, Conservation and Recycling, 97, 76–92. <u>https://doi.org/10.1016/j.resconrec.2015.0 2.009</u>

- Al-Athamin E. A., Hemidat S., Al-Hamaiedeh H., Aljbour S. H., El-Hasan T., Nassour A., 2021, A techno-economic analysis of sustainable material recovery facilities: The case of Al-Karak solid waste sorting plant, Jordan, Sustainability (Switzerland), 13(23). <u>https://doi.org/10.3390/su132313043</u>

- Ardolino F., Berto C., Arena U., 2017, Environmental performances of different configurations of a material recovery facility in a life cycle perspective, Waste Management, 68, 662–676. <u>https://doi.org/10.1016/j.wasman.2017.05 .039</u>

- Arena U., Di Gregorio F., 2014, A waste management planning based on substance flow analysis, Resources, Conservation and Recycling, 85, 54–66. <u>https://doi.org/10.1016/j.resconrec.2013.0 5.008</u>

- Ashkiki A. R., Felske C., McCartney D., 2019, Impacts of seasonal variation and operating parameters on double-stage trommel performance, Waste Management, 86, 36–48. <u>https://doi.org/10.1016/j.wasman.2019.01 .026</u>

- Cherubini F., Bargigli S., Ulgiati S., 2009, Life cycle assessment (LCA) of waste management strategies: Landfilling, sorting plant and incineration, Energy, 34(12), 2116–2123. <u>https://doi.org/10.1016/j.energy.2008.08.0 23</u>

- Cimpan C., Maul A., Wenzel H., Pretz T., 2016, Techno-economic assessment of central sorting at material recovery facilities - The case of lightweight packaging waste, Journal of Cleaner Production, 112, 4387– 4397.

- <u>https://doi.org/10.1016/j.jclepro.2015.09. 011</u>

- Eriksen M. K., Damgaard A., Boldrin A., Fruergaard Astrup T., 2018, Quality Assessment and Circularity Potential of Recovery Systems for Household Plastic Waste, Journal of Industrial Ecology, 23(1). https://doi.org/10.1111/jiec.12822

- Feil A., Thoden van Velzen E. U., Jansen M., Vitz P., Go N., Pretz T., 2016, Technical assessment of processing plants as exemplified by the sorting of beverage cartons from lightweight packaging wastes, Waste Management, 48, 95–105. <u>https://doi.org/10.1016/j.wasman.2015.10 .023</u>

- Gutowski T., Dahmus J., Albino D., Branham M., 2007, Bayesian material separation model with applications to recycling, IEEE International Symposium on Electronics and the Environment, 233– 238. <u>https://doi.org/10.1109/ISEE.2007.36940 0</u>

- Heidari R., Yazdanparast R., Jabbarzadeh A., 2019, Sustainable design of a municipal solid waste management system considering waste separators: A real-world application, Sustainable Cities and Society, 47(February), 101457. <u>https://doi.org/10.1016/j.scs.2019.101457</u>

- Hossain M. U., Wu Z., Poon C. S., 2017, Comparative environmental evaluation of construction waste management through different waste sorting systems in Hong Kong, Waste Management, 69, 325–335. <u>https://doi.org/10.1016/j.wasman.2017.07 .043</u>

- Konstantinidis F. K., Sifnaios S., Tsimiklis G., Mouroutsos S. G., Amditis A., Gasteratos A., 2022, Multi-sensor cyber-physical sorting system (CPSS) based on Industry 4.0 principles: A multi-functional approach, Procedia Computer Science, 217(2022), 227–237. <u>https://doi.org/10.1016/j.procs.2022.12.21 8</u>

- Küppers B., Seidler I., Koinig G., Pomberger R., Vollprecht D., 2020, Influence of throughput rate and input composition on sensor-based sorting efficiency, Detritus, 9(March), 59–67. <u>https://doi.org/10.31025/26114135/2020.13906</u>

- Luttrell G. H., Kohmuench J. N., Mankosa M. J., 2004, Optimization of magnetic separator circuit configurations, Minerals and Metallurgical Processing, 21(3), 153– 157. https://doi.org/10.1007/bf03403318

- Mastellone M. L., Cremiato R., Zaccariello L., Lotito R., 2017, Evaluation of performance indicators applied to a material recovery facility fed by mixed packaging waste, Waste Management, 64, 3–11. <u>https://doi.org/10.1016/j.wasman.2017.02 .030</u>

- Medina-Mijangos R., Ajour El Zein S., Guerrero-García-Rojas H., SeguíAmórtegui L., 2021, The economic assessment of the environmental and social impacts generated by a light packaging and bulky waste sorting and treatment facility in Spain: a circular economy example, Environmental Sciences Europe, 33(1). <u>https://doi.org/10.1186/s12302-02100519-6</u>

- Oliveira Neto R., Gastineau P., Cazacliu B. G., Le Guen L., Paranhos R. S., Petter C. O., 2017, An economic analysis of the processing technologies in CDW recycling platforms, Waste Management, 60(2017), 277–289. <u>https://doi.org/10.1016/j.wasman.2016.08 .011</u>

- Pluskal J., Šomplák R., Nevrlý V., Smejkalová V., Pavlas M., 2021, Strategic decisions leading to sustainable waste management: Separation, sorting and recycling possibilities, Journal of Cleaner Production, 278. <u>https://doi.org/10.1016/j.jclepro.2020.123 359</u>

- Sarc R., Curtis A., Kandlbauer L., Khodier K., Lorber K. E., Pomberger R., 2019, Digitalisation and intelligent robotics in value chain of circular economy oriented waste management – A review, Waste Management, 95, 476–492.

<u>https://doi.org/10.1016/j.wasman.2019.06 .035</u>

- Sun X., Yu H., Solvang W. D., 2022, Towards the smart and sustainable transformation of Reverse Logistics 4.0: a conceptualization and research agenda, Environmental Science and Pollution Research, 29(46), 69275–69293. <u>https://doi.org/10.1007/s11356-02222473-3</u>

- Tanguay-Rioux F., Legros R., Spreutels L., 2021, On the limits of empirical partition coefficients for modeling material recovery facility unit operations in municipal solid waste management, Journal of Cleaner Production, 293, 126016.

- <u>https://doi.org/10.1016/j.jclepro.2021.126 016</u>

- Tanguay-Rioux F., Spreutels L., Héroux M., Legros R., 2022, Mixed modeling approach for mechanical sorting processes based on physical properties of municipal solid waste, Waste Management, 144(November 2021), 533–542. <u>https://doi.org/10.1016/j.wasman.2022.04 .025</u>

- Van Schaik A., Reuter M. A., Boin U. M. J., Dalmijn W. L., 2002, Dynamic modelling and optimisation of the resource cycle of passenger vehicles, Minerals Engineering, 15(11 SUPPL. 1), 1001–1016.

<u>https://doi.org/10.1016/S08926875(02)00080-8</u>

- Wolf Malima I., Colledani M., Gershwin S. B., Gutowski T. G., 2010, Modeling and design of multi-stage separation systems, Proceedings of the 2010 IEEE International Symposium on Sustainable Systems and Technology, ISSST 2010. <u>https://doi.org/10.1109/ISSST.2010.5507 744</u>

- Wolf Malima Isabelle, Colledani M., Gershwin S. B., Gutowski T. G., 2013, A network flow model for the performance evaluation and design of material separation systems for recycling, IEEE Transactions on Automation Science and Engineering, 10(1), 65–75. <u>https://doi.org/10.1109/TASE.2012.22035 94</u>

- Zaman A., 2022, Waste Management 4.0: An Application of a Machine Learning Model to Identify and Measure Household Waste Contamination—A Case Study in Australia, Sustainability (Switzerland), 14(5). <u>https://doi.org/10.3390/su14053061</u>

- Zhao Y., Li J., 2022, Sensor-Based Technologies in Effective Solid Waste Sorting : Successful Applications , Sensor Combination , and Future Directions, Environmental Science Technology, 56, 17531–17544. <u>https://doi.org/10.1021/acs.est.2c05874</u>

Robert Giel    ORCID ID: https://orcid.org/0000-0002-7406-0044 Department of Technical Systems Operation and Maintenance, Faculty of Mechanical Engineering, Wroclaw University of Science and Technology, Poland, Wroclaw, **Poland** e-mail: <u>robert.giel@pwr.edu.pl</u>

#### Alicja Dąbrowska

Department of Technical Systems Operation and Maintenance, Faculty of Mechanical Engineering, Wroclaw University of Science and Technology, Poland, Wroclaw, **Poland** e-mail: <u>alicja.dabrowska@pwr.edu.pl</u>
