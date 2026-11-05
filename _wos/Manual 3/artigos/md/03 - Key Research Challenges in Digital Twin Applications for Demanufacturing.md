# ScienceDirect

IFAC PapersOnLine 55-10 (2022) 2551–2556

## Key Research Challenges in Digital Twin Applications for Demanufacturing

**Farah A. Abumadi<sup>1</sup>\*. Concetta Semeraro.<sup>1</sup> Abdul Ghani Olabi.<sup>2</sup> and Michele Dassisti<sup>3</sup>**

- _1 Department of Industrial and Management Engineering, University of Sharjah, Sharjah, United Arab Emirates (e-mail: (fabumadi@sharjah.ac.ae; csemeraro@sharjah.ac.ae)._

- _2 Department of Sustainable and renewable energy engineering, University of Sharjah, Sharjah, United Arab Emirates (e-mail: ( aolabi@sharjah.ac.ae )._

- _3 Department of Mechanics, Management & Mathematics (DMMM), Polytechnic University of Bari, Bari, Italy (e-mail: michele.dassisti@poliba.it)_

**Abstract** : Based on relevant studies, demanufacturing processes on end-of-life products may achieve around 70% material-saving, 60% energy-saving, and 50% cost-saving of the overall life-cycle cost. Despite these great benefits, many issues are still open in real-life applications, such as the unavailability of smart technology implementations that make more effective and efficient demanufacturing processes. The Digital twin application seems to be a promising tool to facilitate recycling, tracking, and managing such processes.

This paper reviews the state-of-the-art research on digital twins for manufacturing and demanufacturing. A comprehensive analysis of the key challenges in applying digital twins for the demanufacturing process and potential solutions for the current challenges are provided.

Copyright © 2022 The Authors. This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0/)

_Keywords_ : _Digital twin; Cyber-physical production system; Demanufacturing; Industry 4.0;_

### 1. INTRODUCTION

The manufacturing process consists of multiple steps to produce the products, and it involves raw materials and energy consumption. Many industries currently adopt the "take-makeuse-dispose" technique in the manufacturing process, which triggers a severe environmental threat and negatively affects sustainable development  (Dassisti, Siragusa and Semeraro, 2018). Therefore, it is essential to develop and implement an approach that promotes sustainable operations. Demanufacturing is a collection of various technologies, methods, and tools employed to reuse, recover, and upgrade the industrial materials and products after the end of their lifecycle to facilitate sustainable production and support Circular Economy businesses (Tolio _et al._ , 2017). Thus, Demanufacturing is a fundamental approach to sustainable production by reducing waste and increasing resource efficiency (Kerin and Pham, 2019). Moreover, employing a digital twin in demanufacturing phase will assist in reducing the manufacturing cost and promoting sustainable production (Wang _et al._ , 2020). Performing demanufacturing operations so far is a truly complex and challenging task due to uncertainty in the material feature, randomness in the end-oflife state, fluctuations of the quantities, and several other issues coming from the complexity introduced by the lifetime of products. The so-called smart revolution, introducing the concept of digitalization of the production, may significantly help overcome this operational complexity in demanufacturing either by improving the prediction capabilities in managing demanufacturing processes or by accumulating operational knowledge that is particularly useful for this kind of operation. Demanufacturing effectiveness strobly depends on knowing the input material state (say, the history of life-cycle of products is quite often unknown so far), which is the primary source of uncertainty. In regular manufacturing operations, raw materials in the input are considered a deterministic factor. The issue in performing effective demanufacturing processes is thus the initial input information concerning the product as interconnected with the available process technologies. The virtualization of production may help in overcoming this problem. By the way, it is well known that for manufacturing operations in many situations, production systems fail to respond to the incidents on the shop floor due to a lack of interconnection and interoperability between the manufacturing elements, namely machines, material, personnel, and information systems. A Cyber-physical system (CPS) addresses the interconnection issues by converging the physical systems with the cyber system. This convergence is attained by employing the three “c”: control, compute and communicate (Tao, Qi, _et al._ , 2019), (Liu _et al._ , 2017). The cyber-physical system involves multiple computational units that are highly connected with the physical world, in which the computational entities supervise and coordinate the physical processes (Rajkumar _et al._ , 2010). Currently, CPS is applied in various applications, such as smart manufacturing, medical devices, autonomous cars, and smart electric grid (Lozano and

> 2405-8963 Copyright © 2022 The Authors. This is an open access article under the CC BY-NC-ND license. Peer review under responsibility of International Federation of Automatic Control. 10.1016/j.ifacol.2022.10.093

Vijayan, 2020). Cyber-physical systems develop strongly interdependent physical and cyber systems resulting in highly robust and coordinated processes (Lee, 2015).

Moreover, CPS facilitates the integrity and traceability of the manufacturing processes. Cyber-physical production system (CPPS) is an extension of CPS that captures the systems and subsystems across all production domain, including logistics, operations, machines, and personnel considering the most recent development of information technologies, computer science and manufacturing techniques (Kagermann, Wahlster and Helbig, 2013). CPPS maintains a robust connection between machines, products, and personnel, enabling data acquisition and analysis through interfaces. Digital twin (DT) is an essential element of CPS and CPPS.

Compared to conventional engineering methods, the digital twin enhances the efficiency, speed, and accuracy of cyberphysical systems by digitally performing systems' analysis, optimization and evolutions. Digital twin technology may increase the system's efficiency, and it supports new paradigms such as the factory of the future and smart manufacturing systems (Holmes _et al._ , 2021). The Digital Twin emulates the physical systems along its entire lifecycle phases utilizing real-time data to enable the users to predict instantly and respond to any issue in the system (Fei _et al._ , 2018), (Semeraro _et al._ , 2021a). A DT is defined as the cyber model that emulates the actual physical objects by using sensor information, system models, input data (i.e., historical records, maintenance data, and real-time feedback), and communication potentiality to anticipate the system's performance and optimize it accordingly (Schluse _et al._ , 2018). The digital twin can help the manufacturer's decision by simulating the physical system's behavior during all lifecycle phases, which are the start of life (Design), mid of life (Production/Manufacturing), and ending of life (Service/Demanufacturing) (Semeraro _et al._ , 2021a). Extensive studies develop and apply the digital twin in manufacturing. However, very few studies consider creating a digital twin for processing products at their end of life (demanufacturing phase). The primary objective of this paper is to recognize the differences between the applications of the digital twin designed and developed in manufacturing and demanufacturing applications. The idea is to highlight the limitations and shortcomings of recent research in digital twin applications on manufacturing based on a systematic literature review to understand the potential development of such a smart technology for demanufacturing operations.

The content of this paper is structured as follows: the review methodology is explained in section 2. The state of the art of the digital twin for manufacturing and demanufacturing applications is presented in section 3, the critical challenges for digital twin demanufacturing applications in section 4, and the conclusion in section 5.

### 2. LITERATURE REVIEW METHODOLOGY

A systematic literature review was initiated with two research questions: RQ1) What are the main differences between developing the digital twin in manufacturing and demanufacturing; RQ2) What are the main challenges of applying digital twin in demanufacturing processes?

Scopus database was used to collect relevant papers in this field. Two research queries have been used. The paper selection on digital twin applications in manufacturing is based on the following query [("digital twin") AND ("manufacturing")], while the search query [("digital twin") AND  ("demanufacturing" OR "demanufacturing" OR "end of life")] is for selecting papers on digital twin applications in demanufacturing. The research results revealed over 1,599 documents regarding digital twin applications in manufacturing. However, there are only 26 documents regarding digital twin applications in demanufacturing. Figure 1 compares the number of papers on digital twin for manufacturing and demanufacturing applications.

*[Figura ou diagrama omitido.]*

Figure 1: Papers on Digital twin for manufacturing and demanufacturing applications

A text mining technique was performed using VOSviewer software® to compare the papers collected from each query and recognize the main differences. VOSviewer text mining results shown in Figures 2 and 3 indicate that the digital twin had various applications in manufacturing, such as aircraft, fault detection, cutting tools, industrial management, knowledge management, assembly machines, and product geometry. However, the digital twin applications found in demanufacturing mainly focused on waste reduction. Moreover, Figure 3 shows that digital twin applications for demanufacturing are linked to sustainability and promote sustainable production. Therefore, a thorough analysis should be conducted to capture the differences between applying digital twins in manufacturing and demanufacturing to define the key challenges that hinder digital twin application in demanufacturing. Moreover, the role of the digital twin in promoting sustainable production should be highlighted.

Figure 2: Outcomes of the Scopus database search of Digital twin for manufacturing applications

Figure 3: Outcomes of the Scopus database search of Digital twin for Demanufacturing applications

### 3. DIGITAL TWINS FOR MANUFACTURING and DEMANUFACTURING

According to (Tao and Zhang, 2017), the architecture of a digital-twin-driven CPPS can be conceived as made of _five layers: network,  physical, model, database, and application_ . The physical layer consists of sensors, materials, radio frequency identification (RFID), and Automated Guided Vehicles (AGV).

The _physical layers_ perform several tasks and respond to the manufacturing instructions. For instance, Distributed Numerical Control performs several tasks such as transferring the codes, collecting the machine status, transforming the machine status, transferring the data, and tracing the codes. Additionally, the physical layer collects and analyses real-time heterogeneous data according to the Internet of Things (IoT). The sensors and the networks assist in acquiring the big data "5V" characteristics: volume, velocity, veracity, variety, and value (Qi and Tao, 2018). _The network layer_ consists of the network infrastructure that unites the physical world with the virtual world. This layer utilizes multiple technologies such as Industrial Ethernet, Industrial Internet, Mobile Internet (5G), and Industrial Wireless Network. The network infrastructure should be reliable, convenient, and real-time capable. The isomorphism must be executed throughout the network protocol across the various systems. Moreover, the unified interfaces must be able to retrieve all the heterogeneous systems. The network layer incorporates several technologies such as WIFI, RFID, Bluetooth, Zigbee, and 4G/5G. The _databases layer_ consists of a comprehensive set of data associated with the manufacturing system, such as machine data, production data, products data, quality data, environmental data, and cost data. The database layer is the core layer of the digital-twin-driven CPPS in which the digital twin is designed based on the collected data. The database layer emphasizes the visualization and processing of data and establishes a unified connection between the heterogeneous data. Various manufacturing data such as MRP, MES ERP, and WMS can be retrieved from relational databases such as SQL and Oracle to the database management systems such as Hbase. Then, the data mining and analysis are performed in Hbase via several principles such as cluster analysis.

The _model layer_ consists of several models: the data Fusion Model, Shape and Geometric Model, Manufacturing Model, Production Definition Model, and Behavior and Rule Model. The product definition model utilizes Model-based Define technology (Quintana _et al._ , 2010). The Geometric and Shape Model includes several 3D modeling technologies such as Solidworks®, Inventor®, Unigraphics® or PTC®. Moreover, the Manufacturing Attribute Model includes several information models, such as Ontology and XML. The behavior and Rule Model may be built using UML, STEP, and IDEF(Qi and Tao, 2018). Data Fusion Model may be made using various technologies such as entity connecting technology, Ontology alignment technique, and relation inference technology.

Finally, the _application layer_ performs several services of the production system, such as job scheduling optimization, material delivery optimization, and real-time observation and controlling of the manufacturing processes.

Alternatively, a digital twin framework for manufacturing systems can interpret a DT in CPSS (Chen _et al._ , 2020) by considering six components: physical system, virtual systems, Data layer, Enterprise layer, and intelligent layer. To achieve the framework objectives, the following stages should be pursued. The first stage is to perform a logical mapping of all product attributes by classifying the value-added services that developed the product. The second stage is to create the products and processes models by utilizing digital platforms. The last stage is to establish a relational rule model which demonstrates the interaction between the physical process and the digital twin model. This will connect the product attributes to the service configurations creating a product-process digital twin information model. Moreover, (Grieves and Vickers, 2017) developed a digital twin architecture that creates a robust cyber-physical interaction. The architecture of the proposed DT consists of three main parts: the physical entity, the virtual replication, and the interaction between them.

Later, the architecture was expanded to six layers that include data and service, enabling extra analytical functionalities to the digital twin (Tao, Sui, _et al._ , 2019) (Zhang _et al._ , 2019). (Tao, Sui, _et al._ , 2019) proposed a digital twin-driven product design that assists in developing a product digital twin and optimizing the product design processes. (Zhang _et al._ , 2019) developed a data and knowledge-driven digital twin to be utilized in a manufacturing cell. The digital twin establishes autonomous manufacturing employing cell data to develop knowledge addressing manufacturing issues. The digital twin framework included five layers: the physical, digital, data, knowledge, and social layers. The proposed framework will potentially facilitate self-assessment, self-thinking, and self-decisionmaking. (Cheng _et al._ , 2018) build a digital twin model that supports a smart factory development. The digital twin creates data-driven production and management techniques that rely on data and information technology systems. In (Stark, Fresemann, and Lindow, 2019), a digital-factory twin employing information factories is presented. Here, the architecture of the digital twin is composed of eight dimensions. The first four dimensions describe the digital twin's environment: integration breath, connection approach, products lifecycle, and update occurrences. The last four dimensions describe the digital twin's behavior and capability: Digital twin richness, CPS smartness, simulation abilities, and human collaboration. In (Lu _et al._ , 2020) presented a reference model for a digital twin incorporated in a CPPS. Their digital twin model consists of data processing, communication, and information. Furthermore, (Semeraro _et al._ , 2019) presented a methodology for creating data-driven patterns to establish a modular method for digital modeling. The developed approach was applied to developing a digital twin prototype of a die casting process (Semeraro _et al._ , 2021b).

Most of the digital twin frameworks presented above do not focus on the demanufacturing operations so far. The big issue is here if the digital twin framework for manufacturing can be used for demanufacturing and enhance the process performance and effectiveness of the recycle/reuse/recover activities. Most Digital Twin's applications found in literature concerning demanufacturing currently focus on manufacturing waste management (Anand _et al._ , 2019). For instance, (Wang and Wang, 2019) created a demanufacturing framework for waste electrical and electronic equipment (WEEE) based on digital twin. (Chen and Huang, 2020) recommended a digital twin framework for the construction waste process to address demanufacturing issues. The main issue encountered was the technical issues associated with data integration. For this reason, the study proposed data integration and classifications modules. Moreover, the study suggests data warehouse technology as a practical approach to achieving data integration. A digital twin developed by (Scott-Emuakpor _et al._ , 2014) for component demanufacturing of gas turbines at the end of their lifetime. (Mandolla _et al._ , 2019) suggested a digital twin framework for aircraft component additive demanufacturing to reduce cost, reduce time to market, and ensuring superior quality. Moreover, (Shrivastava, Mukherjee, and Chakraborty, 2021) declare that employing demanufacturing in laser-based material deposition techniques. Demanufacturing will guarantee better microstructure, lesser heat affected zone, more minor cracks, and superior microstructure. Moreover, the research indicated that digital twin applications in laser-based demanufacturing or additive manufacturing would decrease the trial and error in selecting the optimal parameter by integrating machine learning and real-time data with multi-physics-based simulation. (Chen and Huang, 2021) explored the capability of the digital twin in addressing the information asymmetries issue in the demanufacturing industry through developing dynamical connections of information that represent real-time data. The study emphasized that several criteria such as data integration, information security, and organizations' demand should be considered for applying digital twin in the demanufacturing industry. Furthermore, (Zacharaki _et al._ , 2021) developed a simulation model utilizing the digital twin technique for foreseeing the errors, faults, and maintenance requirements for large industrial machines. The digital twin will collect and store all the information and status of the machine throughout its lifetime. As a result, the stakeholders will have enough information to remanufacture or repair the large machine at the end of its life cycle. Moreover, the study suggests original technologies that enable the manufacturers to reuse the equipment after their lifetime rather than dispose of them. The demanufacturing architecture consists of nine components: decision support framework, techniques, smart sensors system, health management, cost analysis, optimization planning, digital twin simulation, cybersecurity, and augmented reality. A study conducted by (Wang _et al._ , 2020) successfully integrates cyber-physical systems with digital twin to implement real-time control of the demanufacturing process to reduce the uncertainty of the process. (Xiang _et al._ , 2019) developed a novel architecture of digital twin-driven green manufacturing. The five-dimensional digital twin model highlighted the interactions between physical entities, virtual twins, and the green characteristics of green manufacturing elements. In addition, (Liu _et al._ , 2019) constructed a digital twin for demanufacturing processes to minimize the uncertainties in the process and integrate the information between virtual and actual operations.

### 4. KEY CHALLENGES OF DIGITAL TWIN IN DEMANUFACTURING APPLICATIONS

According to the above, we can summarize some potentialities of  incorporating digital twin in the demanufacturing processes: substantially, reduce manufacturing cost, reducing energy consumption as well as quickening inventory cycle of finished products (Wang _et al._ , 2020). Moreover, incorporating the digital twin in the demanufacturing may help to significantly reduce the uncertainty associated with the conditions and useful life of the product at the end of its lifecycle through integrating data about the product across its entire lifecycle and incorporating it in the digital twin.

Based on the above systematic review, it is concluded that the basic framework of the digital twin seems to be similar for the manufacturing and demanufacturing phases. The basic framework includes essential dimensions: the physical entity, virtual entity, communication channel, and user-specific outcome. However, the main differences between the digital twin applied in manufacturing and demanufacturing are based on data soundness, timeliness of process state: digital twin for manufacturing should focus on collecting recent data about the process, material, and machine status to enable real-time management and assist timely supporting the decision-makers. On the other side, the digital twin for demanufacturing should drive more historical data about the process and the products based on the smart-technologies availabilities. These historical data may include run cycles, usage patterns, failure data, and product information such as assembly/disassembly instructions. Moreover, the digital twin for manufacturing can be considered "raw-material state independent". The manufacturer will be able to decide on the input material knowing all the properties and design specifications, reducing the uncertainty in the process and making it relatively easier to develop the digital twin. In contrast, the digital twin for demanufacturing can be considered "rew-material statedependent". The manufacturer cannot decide correct demanufacturing processes as a function of the final destination of secondary matter provided it is a function of the life-cycle history of the products, thus raising the uncertainty in the process. Based on the above discussion, the following application challenges must be addressed to realize digital twin applications for demanufacturing.

### Research challenge #1

### INFORMATION EXCHANGE

The major challenge in applying digital twin in demanufacturing is the complexity of information exchange among elements in the demanufacturing process due to lack of knowledge. Moreover, poor communication between organizations and lack of close-loop demanufacturing makes the development of digital twin for demanufacturing more difficult. Thus, enterprises must focus on information documentation, formalization, and sharing through upstream and downstream parties, encouraging the utilization of products at the end of their lifecycle.

### Research challenge #2

### DATA INTEGRATION AND MANAGEMENT

Data integration is considered a core challenge for employing digital twins in demanufacturing applications. The data include data from different sensors and management information systems. The digital twin performs a simple transformation of information and is not extended to a multifaceted departmental network. For successfully applying the digital twin for demanufacturing, it is essential to create a platform that decouples the production data with the historical data. Thus, an enterprise-wide data integration network based on database technology should create an efficient digital twin for demanufacturing applications.

### Research challenge #3

### PROCESS UNCERTAINTY

The third challenge that hinders digital twin development for demanufacturing processes includes the incapability of reducing the uncertainty in the process, the absence of tracking management for the demanufacturing process, and the absence of smart enabling technologies directed toward multi-lifecycle demanufacturing. The demanufacturing process is regularly considered an inaccessible or isolated process instead of an integrated process, making it complicated to gather the basic information about machines or materials and acquire perceptual control of the production process.

### Research challenge #4

### LACK OF WELL-DEFINED ONTOLOGY

Ontologies are essential for ensuring an appropriate flow of information, information availability, data utilization, data transmission, and mutual flow of data. However, current research experiences a significant limitation in ontologies. Therefore, creating a well-defined and structured ontology will assist in developing a sufficient digital twin for demanufacturing applications.

### Research challenge #5

### COMPLEXITIES IN HANDLING BIG DATA

The inconsistency between gathered data from physical and virtual systems is considered as a vital challenge in digital twin for demanufacturing applications. The collected data does not incorporate sufficient details to comply with the required parameters. To address this challenge, data-driven digital twin framework for demanufacturing applications should be developed. Moreover, a structured data platforms and computing tools must be utilized.

### 5. CONCLUSION AND FUTURE WORK

This paper assessed the state-of-art of digital twin progress in manufacturing and demanufacturing applications. Moreover, a detailed assessment of the critical challenges and issues of applying digital twin in demanufacturing is discussed. To sum up, the most critical research challenge for developing a digital twin for demanufacturing applications is data integration across the whole product lifecycle among all stakeholders to establish a cooperative production process.

Based on the key challenges discussed in section 5, the future work will be to develop a shared database that integrates and records all the necessary data, including material content and machine status. The shared database could be used to develop the digital twin platform. It will enable companies to gather and analyze the data to optimize the demanufacturing process based on the machine status and the product type.

### REFERENCES

Anand, S. _et al._ (2019) 'Additive manufacturing simulation tools in education', in _2018 World Engineering Education Forum - Global Engineering Deans Council, WEEF-GEDC 2018_ . doi: 10.1109/WEEF-GEDC.2018.8629689.

Chen, G. _et al._ (2020) 'The framework design of smart factory in discrete manufacturing industry based on cyber-physical system', _International Journal of Computer Integrated Manufacturing_ , 33(1). doi: 10.1080/0951192X.2019.1699254. Chen, Z. and Huang, L. (2020) 'Digital Twin in Circular Economy: Demanufacturing in Construction', in _IOP Conference Series: Earth and Environmental Science_ . doi: 10.1088/1755-1315/588/3/032014.

Chen, Z. and Huang, L. (2021) 'Digital twins for informationsharing in demanufacturing supply chain: A review', _Energy_ , 220. doi: 10.1016/j.energy.2020.119712. Cheng, Y. _et al._ (2018) 'Cyber-physical integration for moving digital factories forward towards smart manufacturing: a survey', _International Journal of Advanced Manufacturing Technology_ , 97(1–4). doi: 10.1007/s00170-018-2001-2.

Dassisti, M., Siragusa, N. and Semeraro, C. (2018) 'Exergetic Model as a Guideline for Implementing the Smart-factory Paradigm in Small Medium Enterprises: The Brovedani Case', in _Procedia CIRP_ . doi: 10.1016/j.procir.2017.12.256.

Fei, T. _et al._ (2018) 'Digital twin-driven product design, manufacturing and service with big data', _The International Journal of Advanced Manufacturing Technology_ , 94(9–12), pp. 3563–3576.

Grieves, M. and Vickers, J. (2017) 'Digital twin: Mitigating unpredictable, undesirable emergent behavior in complex systems', in _Transdisciplinary perspectives on complex systems_ . Springer, pp. 85–113.

Holmes, D. _et al._ (2021) 'Digital Twins and Cyber Security – solution or challenge?', in. doi: 10.1109/seedacecnsm53056.2021.9566277. Kagermann, H., Wahlster, W. and Helbig, J. (2013) 'Securing the future of German manufacturing industry: Recommendations for implementing the strategic initiative INDUSTRIE 4.0', _Final report of the Industrie_ , 4(0).

Kerin, M. and Pham, D. T. (2019) 'A review of emerging industry 4.0 technologies in demanufacturing', _Journal of Cleaner Production_ . doi: 10.1016/j.jclepro.2019.117805. Lee, E. A. (2015) 'The past, present and future of cyberphysical systems: A focus on models', _Sensors_ , 15(3), pp. 4837–4869.

Liu, D. _et al._ (2019)' Operation paradigm for demanufacturing shop-floor based on digital twin', _Jisuanji Jicheng Zhizao Xitong/Computer Integrated Manufacturing Systems, CIMS_ , 25(6). doi: 10.13196/j.cims.2019.06.019.

Liu, Y. _et al._ (2017)' review on cyber-physical systems', _IEEE/CAA Journal of Automatica Sinica_ , 4(1), pp. 27–40.

Lozano, C. V. and Vijayan, K. K. (2020) 'Literature review on cyber physical systems design', in _Procedia Manufacturing_ . doi: 10.1016/j.promfg.2020.04.020.

Lu, Y. _et al._ (2020) 'Digital Twin-driven smart manufacturing: Connotation, reference model, applications and research issues', _Robotics and Computer-Integrated Manufacturing_ . doi: 10.1016/j.rcim.2019.101837.

Mandolla, C. _et al._ (2019) 'Building a digital twin for additive manufacturing through the exploitation of blockchain: A case analysis of the aircraft industry', _Computers in Industry_ , 109. doi: 10.1016/j.compind.2019.04.011.

Qi, Q. and Tao, F. (2018) 'Digital twin and big data towards smart manufacturing and industry 4.0: 360 degree comparison', _Ieee Access_ , 6, pp. 3585–3593. Quintana, V. _et al._ (2010) 'Will Model-based Definition replace engineering drawings throughout the product lifecycle? A global perspective from aerospace industry', _Computers in Industry_ , 61(5). doi: 10.1016/j.compind.2010.01.005.

Rajkumar, R. _et al._ (2010) 'Cyber-physical systems: The next computing revolution', in _Proceedings - Design Automation Conference_ . doi: 10.1145/1837274.1837461.

Schluse, M. _et al._ (2018) 'Experimentable Digital TwinsStreamlining Simulation-Based Systems Engineering for Industry 4.0', _IEEE Transactions on Industrial Informatics_ , 14(4). doi: 10.1109/TII.2018.2804917.

Scott-Emuakpor, O. _et al._ (2014) 'Material property determination of vibration fatigued DMLS and cold-rolled nickel alloys', in _Turbo Expo: Power for Land, Sea, and Air_ . American Society of Mechanical Engineers, p. V07AT28A008.

Semeraro, C. _et al._ (2019) 'Data-Driven Pattern-Based Constructs Definition for the Digital Transformation Modelling of Collaborative Networked Manufacturing Enterprises', in _IFIP Advances in Information and Communication Technology_ . doi: 10.1007/978-3-030-284640_44.

Semeraro, C. _et al._ (2021a) 'Digital twin paradigm: A systematic literature review', _Computers in Industry_ , 130. doi: 10.1016/j.compind.2021.103469.

Semeraro, C. _et al._ (2021b) 'Pattern-based digital twin for optimizing manufacturing systems: A real industrial-case application', in _IFAC-PapersOnLine_ . doi: 10.1016/j.ifacol.2021.08.157.

Shrivastava, A., Mukherjee, S. and Chakraborty, S. S. (2021) 'Addressing the challenges in demanufacturing by laser-based material deposition techniques', _Optics and Laser Technology_ . doi: 10.1016/j.optlastec.2021.107404.

Stark, R., Fresemann, C. and Lindow, K. (2019) 'Development and operation of Digital Twins for technical systems and services', _CIRP Annals_ , 68(1). doi:

10.1016/j.cirp.2019.04.024.

Tao, F., Sui, F., _et al._ (2019) 'Digital twin-driven product design framework', _International Journal of Production Research_ , 57(12), pp. 3935–3953.

Tao, F., Qi, Q., _et al._ (2019) 'Digital twins and cyber–physical systems toward smart manufacturing and industry 4.0: Correlation and comparison', _Engineering_ , 5(4), pp. 653–661. Tao, F. and Zhang, M. (2017) 'Digital twin shop-floor: a new shop-floor paradigm towards smart manufacturing', _Ieee Access_ , 5, pp. 20418–20427.

Tolio, T. _et al._ (2017) 'Design, management and control of demanufacturing and demanufacturing systems', _CIRP Annals_

_- Manufacturing Technology_ , 66(2). doi: 10.1016/j.cirp.2017.05.001.

Wang, X. V. and Wang, L. (2019) 'Digital twin-based WEEE recycling, recovery and demanufacturing in the background of Industry 4.0', _International Journal of Production Research_ , 57(12), pp. 3892–3902. doi:

10.1080/00207543.2018.1497819.

Wang, Y. _et al._ (2020) 'Big data driven Hierarchical Digital Twin Predictive Demanufacturing paradigm: Architecture, control mechanism, application scenario and benefits', _Journal of Cleaner Production_ , 248. doi:

10.1016/j.jclepro.2019.119299.

Xiang, F. _et al._ (2019) 'New paradigm of green manufacturing for product life cycle based on digital twin', _Jisuanji Jicheng Zhizao Xitong/Computer Integrated Manufacturing Systems, CIMS_ , 25(6). doi: 10.13196/j.cims.2019.06.018.

Zacharaki, A. _et al._ (2021) 'RECLAIM: Toward a New Era of Refurbishment and Demanufacturing of Industrial Equipment', _Frontiers in Artificial Intelligence_ , 3. doi: 10.3389/frai.2020.570562. Zhang, C. _et al._ (2019) 'A data- And knowledge-driven framework for digital twin manufacturing cell', in _Procedia CIRP_ . doi: 10.1016/j.procir.2019.04.084.
