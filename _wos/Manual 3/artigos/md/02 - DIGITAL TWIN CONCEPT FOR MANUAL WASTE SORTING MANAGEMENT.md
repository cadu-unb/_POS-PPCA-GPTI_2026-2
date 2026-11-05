# Environment Protection Engineering

|Vol. 51|2025|
|---|---|
|DOI:10.37190/epe250104||

ROBERT GIEL (ORCID: 0000-0002-7406-0044)<sup>1</sup><br>ALICJA DĄBROWSKA (ORCID: 0000-0003-2526-6916)<sup>1</sup>

# DIGITAL TWIN CONCEPT

# FOR MANUAL WASTE SORTING MANAGEMENT

In recent years, increasing attention has been given to waste management. It is mainly related to the promotion of the Circular Economy as a key policy objective in the EU. The aim is to shift from a linear approach to a circular one, which is based on reuse and recycling. To enable recycling, it is necessary to separate waste mixtures into different fractions. Therefore, it is crucial to consider and optimize different waste sorting techniques. Despite advances in technology that have emerged as part of Industry 4.0, manual sorting is still widely used as support for automatic/mechanical sorting. Current manual sorting research is mainly focused on human health and ergonomics. There is a definite lack of studies dedicated to the management of this process which is critical for the transformation to a circular economy. Therefore the objective of the paper is to present the digital twin concept for manual waste sorting management. Four stages of research work have been introduced. Within these stages, the motion capture gloves for data collection from physical objects (workers) were proposed. Additionally simulation model for virtual representation was considered and a data exchange system for connection between physical objects and their virtual representations.

## 1. INTRODUCTION

Municipal waste is an integral part of non-industrial human activity. Given their increasing quantity over the years and their negative impact on the environment, the concept of Circular Economy has become widespread in recent years. According to this concept, efforts should be made to close the currently open material cycle and thus reuse materials after they have been consumed instead of landfilling them [1]. The critical action here is to separate the waste mixture into usable and unusable fractions for recycling [2]. Various sorting techniques make this possible. By not applying them or using them without taking optimization actions, the circularity assumption cannot be met.

> 1Wrocław University of Science and Technology, Faculty of Mechanical Engineering, Department of Operation and Maintenance of Technical Systems, Wybrzeże Wyspiańskiego 27, 50-370 Wrocław, Poland, corresponding author: alicja.dabrowska@pwr.edu.pl

Municipal waste sorting techniques are generally divided into automatic/mechanical and manual [3]. Despite the growing number of new sensor-based technologies dedicated to waste sorting, manual sorting is still widely used worldwide [4, 5]. This is mainly due to the highly time-varying physical and chemical characteristics of the items contained in the waste mixture, which require the flexibility of the solutions used in terms of the necessity for frequent adjustment [6]. Many new technologies that have developed as part of Industry 4.0 [7] are still supported by manual techniques that are cost-effective in comparison to the required investment for automated sorting [8] and demonstrate the required flexibility in adapting to the frequently changing physical and chemical characteristics of the waste.

While automated techniques are the subject of many studies (e.g., new methods are being developed for the automatic recognition and classification of waste [9] or factors affecting the efficiency of vision systems are being investigated [10]), research on manual techniques is mainly limited to issues of ergonomics and harmful working conditions. A summary of recent manual sorting studies is presented in Table 1.

T a b l e 1

Summary of municipal waste manual sorting research

|Objective|Level<br>of detail|Research field|Ref.|
|---|---|---|---|
|Ergonomic assessment in waste sorting jobs|workstation|ergonomics|[11]|
|Bacterial air quality assessment in waste sorting cabins|sorting cabin|human health|[12]|
|Ergonomic evaluation of the worktable<br>for waste sorting|workstation|ergonomics|[13]|
|Health risk assessment of sorters|sorting plant|human health|[14]|
|Assessment of occupational exposure<br>to dust, endotoxin, and microorganisms|sorting plant|human health|[15]|
|Simulation model development<br>for decision-making support at the waste-sorting plant|sorting plant|resource management<br>and waste sorting planning|[16]|
|Performance evaluationofamaterial recoveryfacility|sorting plant|performance evaluation|[17]|

The most common topic of research in the area of manual sorting is the negative impact of working conditions on human health. This problem was already considered in the 1990s. [18]. However, it is still relevant today. The research in this area includes a comparison of occupational exposure levels to dust, endotoxin, and microorganisms at modern and traditional sorting plants. Other works considered the health effects of particulate matter and health risk assessment or bacterial air quality assessment in manual sorting cabins with particle size distribution of bacterial aerosol determination.

In the context of ergonomics, the design of a work table for waste sorting tasks [13] was considered. With the use of digital human modeling, work posture simulation, and biomechanical evaluation were performed. As a result, the appropriate height range of the sorting table and the position of the hoppers were determined. Despite this, a comparative study with different ergonomic assessment methods was performed to assess the risk of work-related musculoskeletal disorders and to identify ergonomic improvement proposals for sorting jobs [11].

Besides the issues of ergonomics and the impact of working conditions on health, a separate, rarely considered topic is the modeling aimed at performance evaluation. A simulation model was developed for decision-making support in terms of planning sorting processes [16]. Waste quantity supplied on different days, waste mass flow in kg/s, and deviation of waste value were considered in the form of random variables. In general, manual sorting efficiency in the form of the amount of sorted waste in Mg was considered and the dependence of this efficiency on the amount of processed waste was studied. A more detailed approach was presented [15], where it was assumed that each manual sorter has a recovery efficiency. In the case of more than one sorter, recovery efficiency was calculated as the geometric sum of individual efficiencies. The basis of this approach was the work of Testa [19], in which a genetic algorithm was used in the context of finding the optimal configuration of sorting plant elements. In terms of manual sorting, the issue of personnel allocation was considered. The given models consider the sorting system holistically with a general view of the manual sorting system.

The greatest disadvantage of the existing methods dedicated to manual sorting is the lack of real-time analysis capabilities. This makes it impossible to manage the manual sorting process in real-time in terms of the number of required workers determination, workers allocation, changing the number of fractions picked up at specific stations and ongoing performance evaluation.

A state-of-the-art indicates that manual sorting requires the development of a new method that allows real-time monitoring of the sorting process and fast response to frequent changes in the characteristics of the processed waste stream. The solution to the identified problem is to consider the concept of a digital twin (DT). Therefore, the objective of the paper is to present the digital twin concept for manual sorting in the context of its management.

## 2. MANUAL SORTING DIGITAL TWIN CONCEPT

Digital twins are identified as one of the enabling technologies in the Industry 4.0 concept [20]. There are three basic components of their architecture: physical object, virtual representation of that object, and bi-directional data connection [21]. Thus, consideration of DTs requires the following actions:

- characterization and decomposition of a physical object,

- data collection system development,

- development of the physical object’s virtual copy,

- bi-directional connection formation.

The bi-directional connection between a physical object and its digital copy can be considered in three ways that differ in handling the data flow. Thus, three subcategories of DTs are distinguished by integration level: digital model, digital shadow, and digital twin [22] (Fig. 1). The lowest level of integration (digital model) indicates the presence of only manual data flow. The higher level (digital shadow) introduces an automatic data flow from the physical object to the digital one. The highest level (digital twin) eliminates the manual flow of data.

Fig. 1. Digital twin subcategories based on integration level

DTs are used in many industries, including among others manufacturing, automotive, aerospace, agriculture, mining, healthcare, and military [23]. They can be implemented in any phase of the object’s life cycle. In the design phase iterative optimization, data integrity, and virtual evaluation and verification can be provided. During manufacturing, it is possible to use DT for real-time monitoring, production planning and control, workpiece performance prediction, process optimization, and asset management. In the operation phase, fault detection and diagnosis, state monitoring, performance prediction, and predictive maintenance are enabled. The last phase of the life cycle, on the other hand, is very often ignored in studies on the subject of DTs despite the possibility of implementing this technology [24].

Consideration of the DT concept in the context of manual waste sorting requires, as a first step, characterizing the process and identifying current problems with its management. There are two types of manual sorting: positive sorting and negative sorting. Positive sorting involves separating the desired materials from the waste mixture. Negative sorting, on the other hand, is aimed at removing undesirable materials from the waste mixture [19]. Regardless of the type of manual sorting considered, the process requires human participation. Workers (sorters) in a standing position are located on one or both sides of the conveyor belt on which the waste is transported. Each workstation is equipped with receivers of picked materials, i.e. chutes and/or waste bags. An example of a manual sorting cabin is shown in Fig. 2.

Fig. 2. Example of a manual waste sorting cabin

The latest solutions for manual sorting management are limited to automated control systems allowing mainly to change the parameters of the conveyor-based transport system. The challenge, on the other hand, is the acquisition of data on the processed stream and workers. In the context of the waste stream, only the total weight of waste received for processing on a given day and the volumetric size of the stream (controlled by a feeder, which is usually a bag opener) at the system input are known. In the case of workers, it is only possible to verify their productivity by the amount of waste sorted into chutes and/or bags. It is thus possible to monitor productivity for several days. Such an approach makes it impossible to react quickly to the high variability of waste stream characteristics and to assess the performance of sorting booth workers on an ongoing basis. It is also challenging to consider the productivity of each worker separately in a short time horizon. The outlined management problems justify the consideration of the DT concept.

Fig. 3. Digital twin concept for manual waste sorting

Given the provided characteristics, management of the manual sorting process requires data on the waste stream (morphology and size), conveyor parameters (speed), and workers (productivity and sorting accuracy). A more extensive analysis can further take into account working conditions in the form of temperature or dust. Due to the presence of a human in the process of manual sorting, the concept of a DT in this case is not limited to technical objects (the most commonly considered application of DT in the literature), but must also take into account the human being. Therefore, the issue under consideration corresponds to the human digital twin. The concept of a digital twin for manual waste sorting, including the required three stages of research work is shown in Fig. 3.

## 3. RESEARCH AIMED AT THE DEVELOPMENT OF MANUAL WASTE SORTING DIGITAL TWIN

Taking into account the basic components of the DT and the characteristics of the manual waste sorting process, the stages of preliminary research work necessary for the development of the manual waste sorting DT are as follows:

_Stage I. Physical representation of the waste sorting cabin under laboratory conditions_ . The physical object is the first component of the DT requiring consideration in terms of key elements for process management. In case the physical system cannot be interfered with, it is necessary to replicate it under laboratory conditions. The system’s representation under laboratory conditions includes a conveyor belt, sorting stations with stream receivers (containers), a steam generator, and human sorters. In addition, it is necessary to provide a processed waste stream, that is, to prepare samples of various waste fractions, which will be fed to the conveyor belt with the use of a stream generator.

At this stage of the work, it is also necessary to specify the data sources necessary to manage the manual sorting process. Key from the point of view of the manual sorting process are sorter-, waste stream- and conveyor-related data. Waste stream-related data can be collected based on a flow sensor (for volume flow rate determination) and a RGB camera (for waste morphology detection). Conveyor-related data can be derived from encoders. Sorter-related data, on the other hand, are related to hand movements and their orientation in space. Motion capture gloves can enable tracking of the indicated parameters. Devices of this type are often used in human digital twin research [25]. Motion capture gloves are equipped with bend sensors (to perceive finger movement on the bending axis) and pressure sensors on the thumbs.

_Stage II. Virtual representation of the sorting cabin._ The second component of the DT is a digital copy of the physical object. The sorting cabin, which is replicated under laboratory conditions, requires mapping in a virtual environment in the form of a simulation model. Important at this stage is the selection of appropriate software that will allow further integration of the model with the physical object. The simulation model of the sorting cabin can be made using Flexsim software. An example representation of the sorting cabin is shown in Fig. 4.

Fig. 4. Virtual representation of a manual waste sorting cabin

In addition to the representation of the system elements, it is also necessary to take into account the possibility of later modification of the system parameters and analysis of the results. The variability of stream characteristics (morphology, volume flow size), conveyor speeds, and the possibility of changing the number and allocation of workers must be taken into account. In addition, the model must return values for assessment indicators such as productivity and sorting accuracy for each worker.

_Stage III. The connection between physical and virtual objects._ The third stage focuses on merging the results of the work from stages I and II.

Fig. 5. Connection between physical and virtual objects based on motion capture gloves

A relational database should be used to merge them. It is necessary at this stage of work to verify the correctness of the connection due to, for example, the possibility of delays in data transfer. The connection based on the example of motion capture gloves is shown in Fig. 5.

_Stage IV. Manual sorting process optimization._ Obtaining the benefits of a DT requires incorporating optimization into the developed model. It is necessary here to take the following actions:

• selection of decision variables (waste stream size, conveyor speed, number of workers, workers allocation, number of fractions picked at every workstation),

• development of objective functions aimed at maximizing sorting accuracy and maximizing productivity,

- implementation of reinforcement machine learning algorithms.

Fig. 6. Manual waste sorting digital twin scheme

The presented concept of the DT including data sources and DT applicability is shown in Fig. 6.

## 4. SUMMARY AND CONCLUSIONS

The article presents a part of the research findings on the waste management field and more specifically, the problems of waste sorting. The management problems of the manual waste sorting process outlined in the article, justified consideration of the DT concept for real-time process control, performance evaluation, and optimization. Therefore, four research stages were presented to develop a manual waste sorting DT.

Waste sorting plants are rarely considered as an application area for key Industry 4.0 technologies. Research in recent years has focused mainly on new sorting technologies based on machine learning algorithms. The implementation of DT to manage the manual sorting process will translate into:

- the ability to collect data in real-time, which is currently realized in the long term,

- evaluation of each worker in terms of productivity and sorting accuracy,

- optimization of the process by changing the arrangement and number of workers,

- significantly increased the efficiency of separating recyclable fractions from the

- waste stream.

The proposed DT concept is not only to optimize the process in real time but also to explore the potential possibilities of modernization and conduct experimental research in the developed model.

### REFERENCES

- [1] REJEB A., SUHAIZA Z., REJEB K., SEURING S., TREIBLMAIER H., _The Internet of Things and the circular economy: A systematic literature review and research agenda_ , J. Clean. Prod., 350, 1–19. DOI: 10.1016/j. jclepro.2022.131439.

- [2] ROZENSTEIN O., PUCKRIN E., ADAMOWSKI J., _Development of a new approach based on mid-wave infrared spectroscopy for post-consumer black plastic waste sorting in the recycling industry_ , Waste Manage., 2017, 68, 38–44. DOI: 10.1016/j.wasman.2017.07.023.

- [3] WILTS H., GARCIA B.R., GARLITO R.G., GÓMEZ L.S., PRIETO E.G., _Artificial intelligence in the sorting of municipal waste as an enabler of the circular economy_ , Resources, 2021, 10 (4), 1–9. DOI: 10.3390/ resources10040028.

- [4] BOURTSALAS A.C., THEMELIS N.J., _Materials and energy recovery at six European MBT plants_ , Waste Manage., 2022, 141, 79–91. DOI: 10.1016/j.wasman.2022.01.024.

- [5] LUBONGO C., ALEXANDRIDIS P., _Assessment of performance and challenges in use of commercial automated sorting technology for plastic waste_ , Recycling, 2022, 7 (2), 1–26. DOI: 10.3390/recycling7020011.

- [6] CIMPAN C., MAUL A., JANSEN M., PRETZ T., WENZEL H., _Central sorting and recovery of MSW recyclable materials. A review of technological state-of-the-art, cases, practice and implications for materials recycling_ , J. Environ. Manage., 2015, 156, 181–199. DOI: 10.1016/j.jenvman.2015.03.025.

- [7] WERBIŃSKA-WOJCIECHOWSKA S., WINIARSKA K., _Maintenance performance in the Age of Industry 4.0. A bibliometric performance analysis and a systematic literature review_ , Sensors, 2023, 23 (3). DOI: 10.3390/s23031409.

- [8] LENORT R., WICHER P., _Methodology for investment decision-making in the area of automated waste sorting systems_ , Prz. Elektrotech., 2012, 88 (10B).

- [9] HENRIKSEN M.L., KARLSEN C.B., KLARSKOV P., HINGE M., _Plastic classification via in-line hyperspectral camera analysis and unsupervised machine learning_ , Vib. Spectr., 2022, 118. DOI: 10.1016/j. vibspec.2021.103329.

- [10] KÜPPERS B., SEIDLER I., KOINIG G., POMBERGER R., VOLLPRECHT D., _Influence of throughput rate and input composition on sensor-based sorting efficiency_ , Detritus, 2020, 9, 59–67. DOI: 10.31025/26114135/2020.13906.

- [11] CUNHA J., CARNEIRO P., COLIM A., _Ergonomic assessment in waste sorting jobs with different methods_ , Stud. Syst. Decis. Control, Springer, Cham 2020, 461–469.

- [12] BRĄGOSZEWSKA E., BIEDROŃ I., HRYB W., _Microbiological air quality and drug resistance in airborne bacteria isolated from a waste sorting plant located in Poland. A case study_ , Microorg., 2020, 8 (2), 1–11. DOI: 10.3390/microorganisms8020202.

- [13] EMMATTY F.J., PANICKER V. V., BARADWAJ K.C., _Ergonomic evaluation of work table for waste sorting tasks using digital human modelling_ , Int. J. Ind. Ergon., 2021, 84, 1–8. DOI: 10.1016/j.ergon.2021.103146.

- [14] BARKHORDARI A., GUZMAN M., EBRAHIMZADEH G., SOROOSHIAN A., DELIKHOON M., JAMSHIDI RASTANI M., GOLBAZ S., FAZLZADEH M., NABIZADEH R., NOROUZIAN BAGHANI A., _Characteristics and health effects of particulate matter emitted from a waste sorting plant_ , Waste Manage., 2022, 150, 244–256. DOI: 10.1016/j.wasman.2022.07.012.

- [15] ERIKSEN E., AFANOU A.K., MADSEN A.M., STRAUMFORS A., GRAFF P., _An assessment of occupational exposure to bioaerosols in automated versus manual waste sorting plants_ , Environ. Res., 2023, 218, 1–12. DOI: 10.1016/j.envres.2022.115040.

- [16] GIEL R., MŁYŃCZAK M., PLEWA M., _Logistic support model for the sorting process of selectively collected minicipal waste_ , Adv. Int. Syst. Comput., 2015, 365, 305–318. DOI: 10.1007/978-3-319-19216-1.

- [17] IP K., TESTA M., RAYMOND A., GRAVES S.C., GUTOWSKI T., _Performance evaluation of material separation in a material recovery facility using a network flow model_ , Res. Cons. Rec., 2018, 192–205. DOI: 10.1016/j.resconrec.2017.11.021.

- [18] NERSTING L., MALMROS P., SIGSGAARD T., PETERSEN C., _Biological health risk associated with resource recovery, sorting of recycle waste and composting_ , Grana, 1991, 30 (2), 454–457. DOI: 10.1080/00173139109432008.

- [19] TESTA M., _Modeling and design of material recovery facilities. Genetic algorithm approach_ , Massachusetts Institute of Technology, Massachusets, 2018.

- [20] LIU X., JIANG D., TAO B., XIANG F., JIANG G., SUN Y., KONG J., LI G., _A systematic review of digital twin about physical entities, virtual models, twin data, and applications_ , Adv. Eng. Inform., 2022, 55, 1–18. DOI: 10.1016/j.aei.2023.101876.

- [21] JONES D., SNIDER C., NASSEHI A., YON J., HICKS B., _Characterising the Digital Twin. A systematic literature review_ , CIRP J. Manuf. Sci. Technol., 2020, 29, 36–52. DOI: 10.1016/j.cirpj.2020.02.002.

- [22] SINGH M., FUENMAYOR E., HINCHY E.P., QIAO Y., MURRAY N., DEVINE D., _Digital Twin. Origin to future_ , Appl. Syst. Innov., 2021, 4 (2), 1–20. DOI: 10.3390/asi4020036.

- [23] ATTARAN M., CELIK B.G., _Digital Twin. Benefits, use cases, challenges, and opportunities_ , Dec. Anal. J., 2023, 6, 1–10. DOI: 10.1016/j.dajour.2023.100165.

- [24] LIU M., FANG S., DONG H., XU C., _Review of digital twin about concepts, technologies, and industrial applications_ , J. Manuf. Syst., 2021, 58, 346–361. DOI: 10.1016/j.jmsy.2020.06.017.

- [25] SHAROTRY A., JIMENEZ J.A., MEDIAVILLA F.A.M., WIERSCHEM D., KOLDENHOVEN R.M., VALLES D., _Manufacturing operator ergonomics. A conceptual Digital Twin approach to detect biomechanical fatigue_ , IEEE Access, 2022, 10, 12774–12791. DOI: 10.1109/ACCESS.2022.3145984.
