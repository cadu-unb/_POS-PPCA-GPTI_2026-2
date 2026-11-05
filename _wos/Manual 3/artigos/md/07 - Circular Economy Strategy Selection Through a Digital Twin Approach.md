_Article_

# Circular Economy Strategy Selection Through a Digital Twin Approach

**Marta Rinaldi<sup>1,\*</sup>, Mario Caterino<sup>2</sup>, Marcello Fera<sup>2</sup>, Raffaele Abbate<sup>3</sup>, Umberto Daniele<sup>3</sup> and Roberto Macchiaroli<sup>2</sup>**

- 1 Department of Industrial Engineering, University of Salerno, 84084 Fisciano, Italy

- 2 Department of Engineering, University of Campania Luigi Vanvitelli, 81031 Aversa, Italy; mario.caterino@unicampania.it (M.C.); marcello.fera@unicampania.it (M.F.); roberto.macchiaroli@unicampania.it (R.M.)

- 3 Enginfo Consulting Srl, Corso S. D’Amato, 87/89, 80022 Arzano, Italy; rabbate@enginfo.it (R.A.); udaniele@enginfo.it (U.D.)

- Correspondence: marinaldi@unisa.it

### Abstract

This study investigated the impact of different reverse logistics strategies on the economic and environmental performance of a system within the rubber flooring sector. A simulation tool was developed to replicate the behavior of a real production system, focusing on the transition from linear to circular processes. By considering multiple factors influencing system performance, this research offers an overview of the sustainability of various RL strategies and provides realistic estimates for different scenarios. Three key factors were used to evaluate each strategy’s response: transportation distance, flooring thickness, and returned flooring quality. The findings suggest that an environmental advantage generally favors on-site inspections at the customer’s location to assess the returned product’s condition, regardless of distance. However, centralizing inspections at the manufacturer’s facility is more economically advantageous when distances are short, particularly when the company prioritizes recycling over other circular economy practices. Based on these results, practical implications and guidelines are proposed to help companies balance cost-effectiveness with sustainability, optimizing their operations within a circular economy framework.

Academic Editor: Arkadiusz Gola

Received: 24 February 2025 Revised: 17 June 2025 Accepted: 18 June 2025 Published: 21 June 2025

**Keywords:** remanufacturing; recycling; reverse logistics; simulation; case study

## 1. Introduction

**Citation:** Rinaldi, M.; Caterino, M.; Fera, M.; Abbate, R.; Daniele, U.; Macchiaroli, R. Circular Economy Strategy Selection Through a Digital Twin Approach. _Appl. Sci._ **2025** , _15_ , 7016. https://doi.org/10.3390/ app15137016

The current industrial landscape is undergoing a transformative shift driven by an urgent need to address sustainability challenges. In recent years, the global environmental crisis, manifested through escalating greenhouse gas emissions, resource depletion, and ecological degradation, has underscored the necessity for industries to adopt environmentally conscious practices. The industrial sector, which is responsible for a significant proportion of global emissions and waste generation, holds a crucial role in achieving sustainability targets. However, other sectors also strongly contribute to increasing such emissions, like the transportation sector, which need to be improved [1].

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/ licenses/by/4.0/).

In this context, international agreements and legislative frameworks such as the Paris Agreement [2] in 2015 and the European Climate Law [3] have provided a compelling impetus for action. The European Climate Law, for instance, mandates a net reduction in greenhouse gas emissions by at least 55% by 2030, while establishing legally binding goals to achieve carbon neutrality by 2050. Several approaches can be used to reach these objectives, like the use of low-carbon passenger transportation structures. These regulatory milestones reflect the increasing alignment of governmental policy with the principles of sustainable development, emphasizing the integration of environmental stewardship within economic and industrial strategies, while also paying attention to social aspects [4].

Among the most promising approaches to addressing these challenges is the adoption of a Circular Economy (CE) paradigm. Unlike traditional linear economic models, which are based on extraction, production, consumption, and disposal [5], CE advocates for a regenerative system designed to minimize waste and maximize resource efficiency. This shift towards circularity represents a significant evolution in industrial production, offering both environmental and economic benefits. The main applications of CE principles are in the strategies for reusing or recycling materials. Recycling usually operates on products in the disposal phase and aims to recover the raw materials without preserving the original functionality of the product. Reuse aims to maintain the original functionalities of the product and, depending on the final quality level of the product required, can be achieved using five different strategies [6]: direct reuse, repairing, reconditioning, refurbishing, and remanufacturing (in ascending order according to the final quality level of the product).

The implementation of circular strategies has gained momentum within the industrial sector, especially for the environmental benefits they have been demonstrated to bring. For example, remanufacturing a product has the potential to reduce the use of raw materials and waste disposal up to 80% compared to new products [7], while reducing CO2 emissions by 87% [8].

However, adopting CE strategies is often complicated because of the high investments needed to transform a factory based on a linear economy approach into one based on a circular approach. In fact, their implementation in real-world industrial settings often requires significant restructuring of supply chains, manufacturing processes, and business models. Additionally, industries must contend with uncertainties surrounding the costs and feasibility of these transitions, particularly in sectors reliant on complex production systems [9].

To address these challenges effectively, industries must rely on robust decision-making frameworks informed by quantitative evaluations of sustainability. Simulations have emerged as a powerful tool for evaluating the feasibility and effectiveness of implementing CE strategies since they allow for the creation of virtual models of production systems, enabling the exploration of different scenarios and their potential outcomes without making costly changes to real-world operations. By integrating sustainability-focused key performance indicators (KPIs), such as energy consumption, carbon emissions, and resource utilization, simulations provide a dynamic platform for assessing how CE practices can influence both environmental and economic performance [10,11]. Through this approach, decision-makers can gain insights into critical trade-offs [12], identify bottlenecks [13], predict failures [14] and explore the most effective strategies for aligning production systems with sustainability goals.

Recently, different studies have proposed decision-making frameworks [15] and simulation models [16] to test the feasibility of implementing CE strategies that can be used in real-world applications across various contexts and sectors. However, there are no studies that specifically evaluated CE strategies in the rubber flooring sector. This gap highlights the need for further exploration. In fact, this sector generates large volumes of rubber waste, making it a promising candidate for CE interventions that could enhance sustainability, reduce environmental impacts, and promote resource efficiency [17]. These aspects highlight the potential for CE strategies to transform the rubber flooring industry, making it more sustainable and resource efficient. Further research and analysis are essential to develop comprehensive frameworks and models that can guide the implementation of CE principles in this sector [18].

To address this gap, the aim of this research was to leverage simulation tools to evaluate the economic and environmental impact of adopting CE strategies in the field of industrial rubbers used as floors in several environments. A DES model was developed using AnyLogic Version 8.8.6, which is known for its effectiveness in simulating production and supply chain dynamics.

The problem and simulated processes were grounded in a real-world context and data obtained from a rubber flooring company in Italy. This case study was used to explore the implementation of various CE strategies within the rubber flooring sector and to evaluate their practical applicability, which has not been performed previously. First, the “as-is” scenario, in which a production system based on the linear economy principles is adopted, was created to validate the logics and rules of the production process, using data and information from a real application. Hence, two “to-be” scenarios were simulated with different strategies in the reverse logistics phase, which were compared to identify the most sustainable one. Both the reusing and recycling practices were included in the “to-be” scenarios. Specifically, remanufacturing was selected from among all the reuse practices to achieve the highest possible quality level for the final product. Among the various challenges faced by companies pursuing CE practices, this work focused on the uncertainty surrounding the quality of recovered materials. The simulation model will perform quality control for choosing the most suitable practice (remanufacturing, recycling, or disposal).

Based on the results of this analysis, practical implications and considerations are outlined, along with specific recommendations for potential implementation strategies. Accordingly, the discussion section serves as a practical guideline for professionals in the rubber flooring sector to identify and adopt the most suitable CE strategies.

The remainder of the paper is organized as follows: the next section provides an analysis of the relevant literature. Section 3 details the research methodology. The results are presented in Section 4, and Section 5 discusses the main implications. The last section concludes with the limitations and future directions.

## 2. Literature Review

The concept of the CE has emerged as a transformative model aimed at addressing the inefficiencies of traditional linear economies. As described by Kirchherr et al. [19], CE represents an economic system that eliminates the “end-of-life” (EoL) concept for products, mainly through the application of the 3R paradigm: reduce, recover, recycle. It aims to minimize the use of resources and energy in production and consumption processes to reduce environmental impacts by extending products’ life cycle (recover) or transforming EoL products into raw materials for new production cycles (recycle).

The CE principles are applied in strategies like direct reuse, reconditioning, remanufacturing, and recycling. However, the implementation of these strategies in industrial environments is often very complicated. Firstly, the degree of difficulty of implementing the processes associated with these strategies increases with the desired quality and performance of the product. For example, reconditioning aims to return a product to a satisfactory working condition, with a lower overall performance and shorter expected lifespan than the original [6], while remanufacturing returns a used product into a state in which it has at least the same performance and lifespan of a new product [20,21]. This makes remanufacturing the best strategy among the reuse strategies, but also the most complex, since it requires several operations, ranging from the complete disassembly of the product to reprocessing, reassembling, and testing. Additionally, these operations can be further complicated by the inherent uncertainties that EoL products have. In fact, each product entering in the CE loop has its own story of usage and inherent quality. Consequently, during the execution of the CE process, some unpredictable difficulties may arise, included unexpected hazards for workers during reprocessing [22] depending on the specific conditions of products. This creates uncertainty in the process flow and costs, and on the efficacy of product recovery [23].

Furthermore, there is still a low acceptance rate for products subjected to CE processes among customers, who perceive reused products as lower quality compared to new products, which is not adequately offset by a decrease in the purchase price [24].

These problems may reduce the incentive for stakeholders to invest in CE strategies, as they perceive the payback period of the investment to be very long.

Despite these difficulties, entire industrial segments are starting to invest in transitioning towards a CE paradigm. Companies like Philips have adopted “circular lighting”, offering light as a service where products are leased and components are reused or refurbished, significantly reducing waste. Similarly, IKEA has committed to becoming a circular business by 2030, focusing on designing products that can be repaired, reused, and recycled, while also introducing furniture rental services to extend product life cycles [25]. However, to make circularity profitable, companies must adopt opportune strategies for each operation in the process. For example, reverse logistics (RL) represents a cornerstone to realizing a profitable and environmentally friendly CE strategy, facilitating the return and recovery of products, components, and materials from end users back into the CE supply chain [26]. Without RL, circularity would not be possible. However, RL also represents a cost because it requires transportation means, infrastructures for collection points, labor for sorting materials, and incentives to end users to encourage product returns [27]. Hence, opportunely managing RL is pivotal for the effectiveness of the entire CE strategy. The same can be said for other operations in a CE strategy. Inspection evaluates the quality of EoL products to assess the convenience of applying a CE strategy and applying it appropriately, which can make the difference between profits and losses for a company [28]. Regarding remanufacturing, an efficient disassembly has been demonstrated to reduce the overall costs [29], but it is product-dependent and requires product-related decisions such as the level of disassembly [30].

It is clear that the variability of the CE strategies in each operation determines the profitability of circular operations. High-quality products at the point of return typically require minimal processing, reducing the costs of disassembly, cleaning, and repair. These high-quality returns are more likely to be quickly and efficiently reintegrated into production cycles, leading to faster recovery of value and lower operational expenses. Conversely, products of low quality introduce significant variability into the process, often necessitating extensive operations, higher energy consumption, or complete material breakdown, which can escalate costs and increase lead times.

To reduce this variability, simulations have emerged as a useful tool. Guevara-Rivera et al. [31] combined agent-based modeling and system dynamics (SD) to develop a simulation model to aid stakeholders understanding the implications of transitioning from a linear to a circular economy before the real-world implementation. The model was applied to a Mexican food bank and to a confectionary factory [32]. Their results showed the utility of a simulation model in visualizing the mid- and long-term impacts of CE strategies and how these can lead to both economic and environmental benefits if implemented strategically. Charnley et al. [33] used discrete event simulations (DESs) and SD to reproduce a remanufacturing process. A DES was used to improve decision-making for remanufacturing electric motors on shop floors, while SD allowed for the exploration of the remanufacturing system behavior over time. The study demonstrated that using simulations based on real sensor data reduced the processing times and associated costs and improved the accuracy in predicting the product quality. Goodall et al. [34] introduced a data-driven simulation framework to model remanufacturing operations with high levels of uncertainty, such as varying product returns, conditions, and processes. The framework was applied to a waste electrical and electronic equipment (WEEE) facility that remanufactures items like mobile phones, laptops, and hard drives, where it demonstrated its capability to help face sudden changes in the industrial environment, such as fluctuating staffing levels, process updates, and inventory. Okorie et al. [35] discussed combining different simulation models to move towards the concept of “smart remanufacturing”, a paradigm based on the use of digital technologies (such as Internet of Things or data-driven analysis). The authors focused on evaluating SD, DESs, and agent-based simulations, and concluded that a hybrid simulation model is the best solution for analyzing complex CE environments. Many studies focused on simulating CE production factories to optimize the scheduling of operations considering the quality uncertainty of EoL products [36–38]. Ref. [36] focused on quality evaluations for recycled automobile engines [37] and the profit optimization for a company that remanufactures laptops and desktops, while Ref. [38] demonstrated that the Monte Carlo simulation-based approach was useful for improving the overall CE system efficiency, without considering a specific application. The life cycle extension of electric vehicle (EV) batteries also represents a hot theme. In this field, simulations have been used for different purposes. In [39], the authors proposed a DES approach to simulate the life cycle of batteries and vehicles separately, enabling an analysis of the supply and demand for remanufactured batteries. The results highlighted that integrating remanufactured batteries into the system extends vehicle lifetimes and reduces the environmental footprint of battery production, demonstrating the effectiveness of the simulation approach. In [40], the authors used SD to explore the interplay between manufacturers, retailers, and government policies in closed-loop supply chains for EV batteries. Interestingly, the simulation showed that enhanced recycling technologies led to higher profits in recycling operations, increasing both the collection prices and collection volumes. In the research by Lieder et al. [41], the authors changed the perspective, going from a facility-focused to a customer-focused approach. They used an agent-based simulation model to reproduce the customers’ behavior and assess the acceptance of new CE business models, thereby accelerating CE implementation. Socio-demographic factors, product utility functions, social network structures, and inter-agent communication were the variables used to simulate two CE approaches, one allowing customers to return products after use in exchange for a percentage of the original purchase price or other incentives, and another where the manufacturer maintains the products and customers only pay to use the product rather than owning it. The results of the simulation demonstrated how the first approach favored customers who prioritized cost savings over environmental benefits, while the main challenge of the second approach was the cost retention, with customers frequently switching back to competitive or traditional sales offers due to the higher perceived cost.

The review of the literature highlighted that simulations are widely used in the field of CE strategies to evaluate the advantages and the possible drawbacks of different policies in several industrial sectors. To the best of the authors’ knowledge, there are no studies that used simulations to evaluate the implementation of CE strategies in the industrial rubber flooring sector. Some industrial initiatives, such as the CISUFLO project [42] for sustainable floor coverings, IOBAC’s adhesive-free flooring solutions [43], and the Circular Flooring Partnership by Tarkett and IKEA [44], highlight the industry’s commitment to promoting reuse, recycling, and sustainable manufacturing. However, while these practical applications showcase the potential of CE principles, the scientific research on this specific sector remains limited. Recently, Parvaresh and Amini [45] introduced a 9R framework based on interviews with industrial stakeholders to promote a more sustainable and circular economy in the flooring sector, while Wiesinger et al. [46] analyzed the chemical compositions of industrial floors, discussing the implications of the findings on the transition to a safe and circular economy and highlighting the challenges of identifying and removing hazardous chemicals from recycled floors.

It is clear that these papers do not represent a sufficient sample to fill the knowledge gap. Hence, the present study is the first attempt to use a simulation approach to evaluate the economic and environmental impacts of implementing CE strategies in the rubber industrial flooring sector.

## 3. Materials and Methods

The research methodology employed in this study combines simulation modeling and case study-based research. A simulation-based approach was chosen due to the wellestablished potential of this technique for examining the behavior and performance of supply chain and industrial systems, particularly when assessing changes over time. The production process analyzed in this study was grounded in a real-world context, with data provided by a company located in Italy. The information supplied by the company was utilized to investigate the implementation of various CE practices and reverse logistics (RL) strategies within the rubber flooring sector, with the aim of assessing their suitability and sustainability for practical adoption. This approach aligns with the case study methodology, which is commonly used to explore new phenomena in contexts where the effects are heavily influenced by specific contextual conditions.

The research followed several key steps. The first step involved a review of recent studies (Section 2) to analyze the existing evidence and identify gaps regarding CE practices and reverse logistics strategies for their practical implementation. The second step involved analyzing a real-world process to better understand the operational flow and to identify the key parameters of the process (Section 3.1.1). This analysis also led to the identification of potential industrial practices for remanufacturing and recycling specifically within the rubber flooring sector, and insights into the design and characteristics of CE processes (Section 3.1.2). Based on the insights gained from these steps, the “to-be” scenarios were created and tailored to the characteristics of the specific sector under consideration. The proposed reverse logistics strategies are described in Section 3.2, including the logic behind the simulation model and the design of the experiments.

The final step of the research involved analyzing and organizing the results of the simulations to assess the impact of the proposed RL strategies (Section 4). The main findings and implications derived from these results are presented in Section 5, along with recommendations for potential practical implementation.

### 3.1. “As-Is” Scenario

This sub-section describes the “as-is” process to understand the characteristics of the production phases. This information was used to identify the CE practices that could be applied to the sector under investigation.

### 3.1.1. Linear Process

The production process of rubber flooring consists of two stages: compound preparation and molding. The compound is obtained through two key stages. In the first stage, the elastomer (rubber) is softened and mixed with other liquid and solid components. In the second stage, the compound is refined to improve homogeneity, and additional additives, such as accelerators, are introduced to prepare for the next processing steps. Once prepared, the compound is transferred to the warehouse.

The molding line consists of a series of sequential processes and operations that lead to the production of the final product. These operations are as follows.

The extrusion operation marks the starting point of the production process. During this phase, pressure and heat are applied to the raw material, forming a continuous shape and imparting the necessary physical and mechanical properties. The key parameters in this stage include speed and temperature, which must be continuously monitored to ensure the desired performance of the flooring product. Next, the product passes through one or more rotating rollers in the calendaring process, which produces sheets of varying thicknesses. The main variables to monitor in this phase to meet the required quality standards include the speed of the calendaring machine, the temperature of the calendar, sheet thickness, and sheet width. Following calendaring, the grinding operation is performed to refine the product and its surface to the desired shape. The key parameters of this stage include the material removal rate, grinder speed, and electronic absorption. After grinding, the vulcanization process is carried out. The critical parameters to monitor during vulcanization include the speed, temperature, imprint paper type, and paper consumption. Once vulcanization is complete, the rubber product is gradually cooled to stabilize its structure. Subsequently, the product is coated with an opacifying substance to enhance its opacity and improve its physical properties. Then, the product undergoes corona treatment, an effective method for increasing the surface tension of the material. The key variables for this process include the speed and power settings. Finally, the coating and curing operation are performed before the cutting process.

A discrete event simulation (DES) model was developed using AnyLogic software, which is recognized for its effectiveness in simulating complex system behaviors. Figure 1 illustrates a scheme of the model, where each block represents a process through which the raw material is transformed until it meets the final product specifications.

**Figure 1.** “as-is” simulation model.

The first block (source) is used to generate the raw material entering the system. In this regard, the compound preparation is treated as a black box within the simulation process; therefore, it is not simulated, but it outputs the raw material that proceeds to the subsequent stages of processing. The arrival rate simulates the rate of the raw material’s entry into the system, and it was modeled according to the data provided by the company. The next block (dummy operation) is a dummy work center, which is included in the model to assign two different labels to the products to distinguish between different thicknesses and weights of the products produced by the company. Thickness represents a critical parameter for the company that affects production costs and CO2 emissions; weight, which is directly linked to thickness, is essential for calculating the transportation costs and the associated environmental impact. These labels are assigned according to the probability that a given product is requested by the customers. The labels allow the different processing times and energy consumption levels for all the machines in the following block to be set “as-is” process). The “as-is” process block is used to reproduce the manufacturing process, and it includes all the operations described above, each with their own key parameters. The final block (End) represents a decision point that determines whether the flooring should undergo the cutting operation. If the decision is to proceed with cutting, the material will undergo the die-cutting process and then be sent to the tile warehouse. Alternatively, if the cutting operation is not required, the material will be sent directly to the flooring warehouse. The data inserted reflects the probability that a given product will be cut before being stocked.

The simulation model was run with a one-minute time step for the 25 replications in a typical working day. The “as-is” system was replicated using the real data provided by the company, and the results were used to validate the model. This step allowed for a comparison between the simulation results and the actual process results, ensuring the accuracy of the applied logic.

### 3.1.2. From a Linear to Circular Model

Transitioning from a linear to a circular model is a complex process. Converting a linear production system into a circular one requires a fundamental rethinking of how resources are utilized, optimized, and recovered within the system. To support circular economy implementation, products should be designed for easy disassembly and reuse. Starting with these concepts, the remanufacturing and recycling processes were characterized and tailored to the product, process, and sector under investigation.

To understand the logics used to design the “to-be” scenarios, the main stages of a remanufacturing process are described below with a specific focus on the sector being investigated.

Pre-Disassembly: This is a preparatory phase. It involves inspecting and assessing the product’s condition when it is returned to the company. Based on this evaluation, decisions are made on whether to proceed with remanufacturing, recycling, or disposal. The goal is to assess the product’s quality to identify the most suitable process. The key operations include testing the product to determine its state, which informs the next steps: (1) continuing with remanufacturing if the quality of the rubber flooring is high, (2) recycling if the quality is good, but insufficient to ensure that the new flooring meets the ‘as good as new’ condition, or (3) disposing if the quality is too low for any CE practice.

Disassembly: If remanufacturing is selected, the flooring undergoes disassembly, which, in general, is the most complex and critical phase. The components are separated, and each one is inspected to determine if a maintenance phase is needed. In this specific case, disassembly consists of removing the top layer of the floor (sheet), which has a standardized thickness that does not depend on the thickness of the flooring.

Repair or Maintenance: The components undergo maintenance operations to restore them to a condition close to that of new products. These operations vary, with simpler cases requiring only cleaning and painting. This step was implemented in this study according to the considered characteristics of the product. In particular, the removed sheet is disposed of, and a new sheet is produced to replace the old one; the remaining part of the floor undergoes the following operation.

Reassembly: In this stage, the components are reassembled to form the product. The reassembled component may be identical to the original or upgraded, depending on the customer specifications. In this case, reassembly consists of gluing the new sheet that will form the top layer of the floor.

Post-Assembly: The final phase involves testing the reassembled product to ensure that it meets the required quality standards.

If recycling is selected during the pre-disassembly phase, the flooring undergoes a specific treatment to recycle the material, which will subsequently be used in the production of a new floor to be sold on the market. The process begins with devulcanization, which breaks the chemical bonds between the elastomer and the additives. Then, a grinding operation is performed, which is crucial for reducing the material to a controlled size and for converting the devulcanized floor into recycled raw material. The “as-is” process, as outlined in the previous section, will then be applied, resulting in the production of a floor made from recycled raw materials.

Finally, if disposal is selected during the pre-disassembly phase, no treatment is applied to the flooring which is directly disposed of.

### 3.2. “To-Be” Scenarios

The “to-be” scenarios represent alternative strategies that were evaluated to identify the most sustainable approach, considering the characteristics of the examined system.

Two scenarios were identified in collaboration with the management team of the company involved in this study. The selection was based on practical considerations related to the specific characteristics of the production process and the nature of the rubber flooring sector. In particular, due to the large size and handling constraints of the product, it is operationally feasible to conduct the inspection phase directly at the customer’s site, where the flooring is recovered at the end of its life cycle. This approach contrasts with the more conventional reverse logistics model in which products are transported back to the manufacturer for inspection. Given the lack of existing literature specifically addressing CE strategies in the rubber flooring sector, the two proposed scenarios were prioritized based solely on their operational feasibility and the insights obtained through interviews with the company management. As such, they represent the most realistic and potentially implementable options according to current industry practices and logistical constraints.

Thus, the objective was to simulate two distinct scenarios, which differed in the reverse logistics strategy employed. The primary distinction lay in the execution of several process stages at the manufacturer’s facility, rather than at the customer’s location, where the flooring was recovered at the end of its life cycle.

The key difference between the two scenarios concerns the logistic flow of the flooring. The first aspect involves the execution of the Pre-Disassembly phase, which can occur either at the manufacturer’s facility or at the customer’s location. This phase is crucial for assessing the quality of the flooring and determining the appropriate CE practice—recycling, remanufacturing, or disposal. Indeed, the uncertainty related to the quality of the returned product is a critical factor in evaluating the product’s suitability for remanufacturing. For both scenarios, the same assumptions regarding the quality of the flooring, as described in Section 3.1.2, were applied.

In the first scenario, referred to as “to-be 1”, the flooring is returned to the manufacturer’s facility before the inspection phase. This incurs shipping costs to recover the returned product with the aim of assessing the condition of the flooring and determining the appropriate CE practice. In the second scenario, “to-be 2”, the operator visits the customer’s location to inspect and, if necessary, collect the flooring for further processing. In this case, only the operator’s travel costs are considered.

The “to-be” scenarios were compared to assess the most sustainable reverse logistics strategy in terms of both economic and environmental sustainability.

### 3.2.1. “To-Be 1”: Inspection at the Manufacturer’s Facility

Figure 2 show the flow chart of the “to-be 1” scenario in which the Pre-Disassembly operation (quality control) is carried out at the manufacturer’s facility.

Each blue block represents an operation to be carried out. In this scenario, the flooring is returned to the manufacturer’s facility for inspection to determine the appropriate CE practice to be implemented. The process starts with the return of the flooring, which is represented by the green ‘RL’ block. A quality control check is then performed on the returned product, and based on the results, the next steps are determined. This decisionmaking process is represented by the blue diamond shape, indicating a decision point.

**Figure 2.** “to-be 1” operational flows (blue blocks) and logistic flows (green blocks).

At this stage, depending on the outcome of the quality control, a specific CE practice is selected (orange blocks), and the flooring undergoes different operations and treatments. Low-quality flooring does not undergo any treatment and is directly disposed of. Goodquality flooring is processed for recycling the materials, which are then used to produce new flooring for sale on the market. The process description (orange ‘recycling’ block) is provided in Section 3.1.2. As the final step, the flooring produced from recycled material is shipped to the end user (green ‘LOGISTICS’ block).

Flooring of excellent quality is processed for remanufacturing (orange ‘remanufacturing’ block), and the resulting flooring is sold on the market. Several operations, as outlined in Section 3.1.2, are performed. Afterward, the remanufactured flooring is shipped to the end user.

Figure 3 shows the scheme of the simulation model, with the pink block highlighting the dummy operations that assign 3 labels: ‘thickness’ and ‘weight’, which are also used in the “as-is” model to reflect the differences in the products produced by the company, and ‘quality’ that reflects the quality of the returned flooring. The red block represents the “as-is” process, the yellow block represents the process related to sheet production, and the blue one represents the flooring shipment. Finally, the green block shows the RL phase, which is performed before the inspection phase.

**Figure 3.** “to-be 1” simulation model.

3.2.2. “To-Be 2”: Inspection at the Customer’s Location

The ‘“to-be 2” scenario involves the operator visiting the customer’s location to perform the quality control directly on site, in contrast to the previous approach, where the Pre-Disassembly operation is carried out at the manufacturing facility. The flow chart is shown in Figure 4.

**Figure 4.** “to-be 2” operational flows (blue blocks) and logistic flows (green blocks).

As in the “to-be 1” scenario, the diamond shape represents a decision point that determines the appropriate CE practices based on the flooring’s quality.

If the flooring is suitable for recycling (i.e., it is of good quality), it must be shipped to the manufacturer’s facility (green ‘RL’ block), where the recycling and production processes take place. In this case, the steps from material recycling to flooring shipment follow the same process as in the previous scenario. The key distinction is that only good-quality flooring is shipped to the manufacturing facility, while low-quality flooring is not purchased. Therefore, this strategy enables the company to cover the operator’s travel expenses, while potentially benefiting from cost savings if the flooring is of bad quality.

If the flooring is of excellent quality, the operator removes the top layer directly at the customer’s location. The remaining part of the flooring is assembled with a new sheet, which is shipped from the manufacturer’s facility where it is produced. The shipping of the new sheet is represented by a green block. Once this phase is complete, no further shipment of the finished product occurs, as reassembly and post-assembly operations are carried out at the customer’s location. Compared to the “to-be 1” scenario, for flooring undergoing remanufacturing, only the new sheet is produced at the manufacturer’s facility and then transported to the customer’s location, eliminating the need to transport the entire flooring back to the manufacturer’s facility.

Figure 5 represents the Anylogic model, where the blocks assigning labels are highlighted in pink, the “as-is” process is highlighted in red, the production process related to the sheet is highlighted in yellow, and the shipments are highlighted in blue. Finally, the green block shows the RL phase, which is performed after the inspection phase.

**Figure 5.** “to-be 2” simulation model.

### 3.2.3. Design of Experiment

As already asserted, the aim of this study was to evaluate the sustainability of two RL strategies and assess their suitability in practice. Three factors were identified to evaluate the response of the system. The following key factors that may have a potential impact on the performance of the system were considered: the distance between manufacturer and customer, the flooring thickness, and the quality of the returned flooring. These factors were selected based on their direct relevance to the operational, economic, and environmental performance of the reverse logistics process in this specific industrial context. In particular, they reflect the main sources of variability that were identified through discussions with industry experts and company management and are considered to be the most critical in shaping the outcomes of the two scenarios under study.

Two possible distances from the manufacturing facility to the customer location were simulated. Additionally, eight different quality scenarios were considered, each simulating a different percentage of returned flooring in low-, medium- and high-quality conditions. These scenarios were simulated to provide a comprehensive overview of the potential end-of-life conditions of the flooring. Finally, the effect of flooring thickness was evaluated. Three different thickness scenarios were defined, each with different demands for low-, medium-, and high-thickness flooring. These scenarios were used to assess the probability of customer demand for a specific thickness, which has a direct impact on both the production and transportation phases.

For each experiment, the simulation model provides the results for the two “to-be” scenarios. Overall, 128 different experiments were designed. Each one was replicated 25 times using a one-minute time step to simulate a typical working day. For each scenario, the average values across replications were calculated and used for the key performance indicators to ensure the consistency and robustness of the comparison of the reverse logistics strategies.

Tables 1–3 provide an overview of the data used for each scenario. Table 1 presents two transportation distance scenarios representing short and long return distances between the customer and manufacturer. These distances were used to evaluate how logistics impact both economic costs and CO2 emissions in each reverse logistics strategy. Table 2 defines eight quality scenarios that had varying proportions of returned flooring classified as high, medium, or low quality. These scenarios influence the choice of a CE strategy (remanufacturing, recycling, or disposal) and allow for the assessment of how the product condition affects profitability and sustainability. Table 3 shows four scenarios reflecting the customer demand distributions for flooring with different thicknesses. Since thickness affects the product weight, these scenarios were used to analyze its impact on production costs, transportation efficiency, and overall system performance.

**Table 1.** Distance scenarios.

|**Scenario**|**Distance [km]**|
|---|---|
|Scenario 1|300|
|Scenario 2|1000|

**Table 2.** Quality scenarios.

|**Scenario**|**High Quality [%]**|**Medium Quality [%]**|**Low Quality [%]**|
|---|---|---|---|
|Scenario 1|50%|30%|20%|
|Scenario 2|50%|40%|10%|
|Scenario 3|60%|20%|20%|
|Scenario 4|60%|30%|10%|
|Scenario 5|70%|20%|10%|
|Scenario 6|70%|10%|20%|
|Scenario 7|80%|10%|10%|
|Scenario 8|80%|15%|5%|

**Table 3.** Thickness scenarios.

|**Scenario**|**Low Thickness [%]**|**Medium Thickness [%]**|**High Thickness [%]**|
|---|---|---|---|
|Scenario 1|33.3%|33.3%|33.3%|
|Scenario 2|60%|20%|20%|
|Scenario 3|20%|60%|20%|
|Scenario 4|20%|20%|60%|

The following key performance indicators (KPIs) were used to assess the sustainability of the “to-be” scenarios:

- Average profit [EUR/kg];

- Average CO2 emissions [kgCO2/kg].

The average profit represents the mean profit per kg of flooring produced and reflects the economic efficiency of the strategy. The average CO2 emissions measure the carbon dioxide emissions per kg of flooring, providing an estimate of the environmental impact. Both KPIs are critical for identifying the most sustainable strategy.

Profit is determined by accounting for all the costs incurred during production and the total revenue. Revenue is calculated based on the flooring sold, including both those that have undergone the remanufacturing process and are sold at a lower price, as well as those made from recycled material, which are sold at a higher price than the manufactured flooring. The costs include the cost of the raw materials, labor costs, energy costs, and transportation costs (both logistics and RL phases). The total cost is calculated by summing the following components:

- Raw material costs: unit cost (EUR/kg) _×_ quantity (kg);

- Labor costs: unit labor cost (EUR/h) _×_ number of hours (h);

- Energy costs: unit energy cost (EUR/kWh) _×_ energy consumption (kWh);

- Transportation costs: based on the distance covered (km) and the quantity (kg) transported.

The CO2 emission is calculated by considering the total amount of CO2, including emissions generated from manufacturing, remanufacturing, and recycling. For production processes, the energy consumed was converted into CO2 emissions using the Carbon Emission Signature (CES), a specific coefficient that translates energy consumption into kgCO2 [47]. CO2 emissions due to transportation (both logistics and RL phases) were then calculated according to Rinaldi et al. [48], which were added to compute the total amount of CO2 emissions.

The selection of the KPIs in the digital twin model was guided by both practical relevance and alignment with the existing literature on CE strategy evaluation [10,11]. Average profit and CO2 emissions were prioritized as they directly reflect the economic and environmental dimensions critical to industrial decision-making. These indicators were also chosen for their measurability using real company data and their ability to differentiate between outcomes across multiple scenarios. These indicators were supported by the design of a comprehensive experimental framework that tested 128 scenarios, ensuring the robustness of the selected KPIs in evaluating reverse logistics strategies.

All the “to-be” scenarios were simulated using the real data provided by the company, which was also used for the “as-is” simulation. The simulation model was run with a one min time step to replicate a typical working day.

## 4. Results

This study evaluated two RL strategies using a digital twin model developed in AnyLogic based on real operational data from a rubber flooring manufacturer. Three main variables were used to capture the system’s performance under different conditions: transportation distance, flooring thickness, and the quality of the returned products. A full factorial design of experiments was employed, comprising 128 simulation scenarios. The outcomes were assessed using two key performance indicators—average profit and average CO2 emissions per kilogram of product—which were selected to reflect both economic and environmental sustainability. This section presents the results of the simulations and the analysis of how the different factors influence the system’s performance and the effectiveness of each RL strategy.

The first analysis evaluated the impact of the three factors on the environmental and economic performance of the system; the results of the simulations were analyzed focusing on a single factor at a time while keeping the other factors constant.

Regarding the impact of thickness, Figure 6 shows the performance when the probability that the customer requests a flooring of a certain thickness varied (four thickness scenarios).

**Figure 6.** Impact of thickness on performance and strategy.

A clear trend emerged as the percentage of floors with a greater thickness (and consequently higher weight) increased (thickness #4), leading to a rise in the average profit. This trend held true for both the “to-be 1” and “to-be 2” scenarios. This can likely be attributed to the fact that the increase in weight led to higher revenue, which outweighed the additional production and transport costs associated with the increase in thickness. However, a similar conclusion could not be drawn when considering the average CO2 emissions. In this case, it was evident that the thickness did not have a clear impact under the same RL scenario, but it was clear that thickness is an important element in the RL strategy when evaluating environmental sustainability since thickness impacts the logistics and RL processes.

Regarding the impact of distance, Figure 7 shows the performance when the distance was varied (two distance scenarios).

As expected, the impact of distance on performance is significant. As the distance increases, both economic and environmental performance deteriorates, as evidenced by a decrease in average profit and an increase in CO2 emissions. Notably, the effect is more pronounced in the “to-be 1” scenario, indicating a higher dependency of this scenario on logistics operations.

**Figure 7.** Impact of distance on performance and strategy.

Figure 8 shows the last analysis on the performance varying the flooring quality (eight quality scenarios).

**Figure 8.** Impact of quality on performance and strategy.

It can be observed that the net profit decreased as the percentage of top-quality flooring increased (moving from quality #1 to quality #8). This was because the top-quality flooring is sold at a lower price compared to flooring that has undergone recycling processes. This trend was more evident in the “to-be 2” scenario, where the logistics costs had a weaker impact on economic performance.

Furthermore, as the percentage of top-quality flooring increased, implying the implementation of remanufacturing processes and consequently lower energy consumption compared to recycling operations, the CO2 emissions tended to have a progressively lower environmental impact, which was clearly observed with both RL strategies.

The last analysis focused on the impact of quality on performance and strategy. Specifically, the objective was to understand how increasing the weight of the remanufactured product affects the system by comparing the two RL strategies and calculating the frequency at which each strategy was successful as the percentage of high-quality products increased. The comparison was made considering 16 scenarios at a time, starting from scenarios with a percentage of remanufacturing equal to 50% to scenarios characterized by the maximum percentage of high-quality products (80%). Figure 9 shows the number of times one scenario was more advantageous than the others from an economic or environmental perspective. The results show that the type of CE practice adopted did not significantly influence the profit; in fact, the two strategies were largely equivalent, with no clear difference. However, regarding environmental sustainability, the CE practice had a considerable effect, revealing a clear trend in which “to-be 2” emerged as the least impactful strategy. This can be easily explained by the reduced number of trips required.

**Figure 9.** Impact of remanufacturing process on performance and strategy.

## 5. Discussion

This study explored the effects of different reverse logistics (RL) strategies on the economic and environmental performance of a system within the rubber flooring sector that has adopting various CE practices. By considering multiple factors, we aimed to understand how these elements influence sustainability.

The following discussion highlights the key findings of this study, the practical implications, and potential directions for future research.

### 5.1. Main Findings

The results of the simulation demonstrated that when only 50% of returned flooring is suitable for remanufacturing, the two RL strategies showed different economic and environmental outcomes. Centralizing inspection at the manufacturer’s facility tended to be more cost-effective—especially for short distances—due to the lower operational complexity, time requirement, and costs. However, this approach is generally less sustainable because it involves more transportation, increasing carbon emissions. On the other hand, conducting inspections at the customer’s location reduced transport-related emissions and costs, especially for long distances. Although this approach introduces additional expenses for operator travel and on-site work, it was often both economically and environmentally beneficial when the transportation distances were significant. As the share of high-quality returned flooring increased and low-quality returns decreased, more products were eligible for recycling rather than being discarded. This resulted in more items needing to be transported back to the manufacturer, particularly for recycling. For short distances, the best strategy became less obvious and depended heavily on the flooring thickness, which affected the transport and processing efficiency. When the distances grew, the environmental impacts from logistics rose sharply, even if the economic gains remained steady due to the continued need to transport items for recycling. Thus, the trade-off between sustainability and cost-effectiveness is influenced by a combination of factors, including the distance involved, the quality of the flooring, and the operational requirements of each strategy.

When 60% of the flooring was of top quality, more products went through remanufacturing. In this case, if this was performed at the customer’s location, only a new surface sheet needed to be shipped, reducing the overall logistics efforts. This makes on-site remanufacturing more sustainable—even for short distances—compared to centralized processing. If the percentage of medium-quality returns (recycling candidates) increased, neither strategy was clearly more sustainable. Again, factors like product thickness and distance played a crucial role. Economically, on-site inspections tended to offer better savings by avoiding unnecessary transportation, even though they involved more labor.

With 70% high-quality returns, on-site inspections offered the best environmental results in almost all cases, as they avoided multiple long-distance trips. This benefit, however, was offset if low-quality returns increased, as these must still be transported and discarded or recycled. From a cost perspective, identifying low-quality products on-site helps to avoid unnecessary shipping and disposal costs. In contrast, centralized strategies require transporting all returns, even for products that are later discarded, thus increasing the costs.

Finally, when 80% of returns were high-quality, the environmental advantage of onsite inspections became even more evident, regardless of distance. The only exception was short-distance scenarios with very few low-quality returns. Economically, on-site inspection was more cost-effective in these conditions, as it eliminates the need to ship the entire product back to the factory.

In summary, when a high percentage of products can be remanufactured, on-site inspections are both economically and environmentally preferable. They reduce transportation costs and emissions, even when considering the extra labor and travel involved. The best strategy ultimately depends on distance, return quality, and product characteristics like thickness.

### 5.2. Final Remarks, Practical Implications, and Managerial Insights

Based on the results of this analysis, some practical implications and guidelines are proposed. The aim is to help companies to choose the best strategy within a CE context.

### 1. Prioritize on-site inspections to reach environmental sustainability

For companies seeking to reduce their environmental footprint within a CE framework, conducting on-site inspections (at the customer’s location) typically represents the most sustainable approach. This strategy significantly minimizes transportation needs by eliminating the need to transport flooring back and forth between the customer site and the manufacturer’s facility. This is especially true when the remanufacturing practice is prevalent and it can be also performed on-site, as the focus on reusing and extending the life cycle of materials aligns with the environmental principles of waste reduction and resource efficiency. On-site inspections further optimize sustainability by ensuring that only flooring requiring remanufacturing is processed, while materials deemed unsuitable for reuse can be immediately discarded or repurposed, avoiding unnecessary transportation. Additionally, this practice reduces the energy consumption associated with the logistics of transporting large volumes of flooring.

This conclusion aligns with several studies in the literature that emphasize the role of localized decision-making and flexible reverse logistics in achieving environmental efficiency. For example, Goodall et al. [34] and Huster et al. [39] demonstrated how simulation-based frameworks can support the optimization of remanufacturing under uncertain return conditions, showing that targeted, data-informed collection strategies can reduce environmental impacts. Similarly, Li et al. [40] confirmed that minimizing unnecessary transportation in closed-loop supply chains significantly contributes to reducing carbon footprints. Our findings also echo the results of Okorie et al. [35], who stressed that integrating real-time information in remanufacturing planning, enabled through hybrid simulation approaches, leads to smarter, more sustainable operations, particularly in decentralized settings.

When evaluating the environmental advantages of on-site inspections, companies should also consider the potential environmental impact of the remanufacturing process itself. In some cases, remanufacturing may have a significant environmental footprint, especially when high-energy processes are involved. Therefore, adopting an integrated approach that balances the environmental costs of both logistics and remanufacturing is essential for achieving optimal sustainability outcomes.

Moreover, it is important for companies to continually monitor and assess the environmental impacts of their strategies. Technological advancements in both transportation and remanufacturing processes can further enhance the sustainability of on-site inspection, making it an even more viable strategy as innovation progresses in the field of circular economy practices.

While on-site inspections provide substantial environmental benefits, these advantages are maximized when combined with other CE practices, such as effective waste management, energy-efficient remanufacturing processes, and optimized transportation logistics. Future research and practice should explore the integration of these factors to create comprehensive, sustainable systems for product life cycle management.

The observed trade-off between centralized vs. on-site inspections in reverse logistics operations can be generalized to other industries dealing with bulky and transport EoL products, which are frequently found in sectors such as those that manufacture furniture, appliances, and automotive components. Manufacturers could implement an initial screening mechanism—either via customer self-reporting tools or rapid on-site inspection protocols—to categorize returned products by quality. This enables targeted routing for remanufacturing, recycling, or disposal, reducing unnecessary transport and processing costs.

### 2. Short distances can justify recycling at the manufacturer’s facility

Short distances between the manufacturer and the customer can significantly influence the sustainability and economic viability of different CE practices. When the distances between the manufacturer and the customers are short, it may be more beneficial to prioritize recycling rather than other CE practices. Despite the higher environmental impact of recycling processes, the reduced transportation costs make recycling the more economical and environmentally favorable option in such cases.

The environmental impact of recycling, particularly in terms of energy consumption and emissions, is often considerable due to the complex and energy-intensive nature of many recycling processes. However, when transportation distances are minimal, the overall environmental footprint is substantially reduced. The decreased need for extensive transportation mitigates the carbon emissions typically associated with long-haul logistics, making recycling a more environmentally favorable option in such circumstances.

This finding is consistent with the simulation results presented by Zhang et al. [38], where the Monte Carlo-based analysis demonstrated that when logistical costs are low, such as in scenarios with short travel distances, recycling can emerge as a viable option even when energy consumption is relatively high.

Economically, short transportation distances can also make recycling more profitable due to the higher prices of recycled products. This is particularly relevant in cases where the volume of products requiring recycling is significant, and where the cost of manufacturing would otherwise impose a heavier financial burden.

It is important to recognize that the choice between recycling and other CE practices should be based on a comprehensive analysis of both environmental and economic factors, including transportation costs, energy consumption, and the specific requirements of the remanufacturing process. Companies should also take into account the evolving nature of recycling technologies, which may increasingly reduce the environmental impact of recycling and improve its economic viability in the future. Thus, while recycling is typically associated with a higher environmental impact, short distances can make it a more favorable option, both environmentally and economically, when transportation costs are minimized. In cases where customers are geographically close to the manufacturing facility, centralizing inspection and recycling operations can yield economic benefits despite the higher energy intensity of recycling—a situation that often occurs in local or regional supply chains across various industries. Managers can thus prioritize recycling for local returns while reserving on-site remanufacturing for long-distance clients. However, the findings suggest that no models are universally optimal. Managers should consider adopting flexible, hybrid strategies that can be dynamically adjusted based on product quality, transportation distance, and expected volume of returns.

Future research should explore the integration of these factors and investigate how short-distance logistics can be optimized within circular economy strategies to achieve better sustainability outcomes.

### 3. Consider the quality of the returned item as the main driver

When a significant proportion of flooring requires remanufacturing, the strategy can have considerable implications for both environmental and economic performance. In these cases, the savings generated from reducing transportation costs—by conducting on-site inspections and avoiding the need to transport entire flooring units—can often outweigh the additional costs incurred for operator travel and labor. On-site inspections reduce the need for long-distance transport of flooring, thereby minimizing the associated emissions, energy consumption, and logistical costs. Furthermore, remanufacturing a large volume of flooring on site aligns with the CE principles, as it promotes material reuse while reducing the carbon footprint of transport.

This result is aligned with that of prior studies that emphasized the role of remanufacturing volume and scale in determining the optimal strategy. For instance, Lander et al. [29] show that disassembly and remanufacturing processes only become economically feasible and operationally efficient beyond certain volume thresholds. The results achieved in this study support this view by demonstrating that high volumes of top-quality returns enable on-site remanufacturing to be a cost-saving option due to reduced transportation needs and localized processing. Furthermore, Goodall et al. [34] underlined that flexibility in remanufacturing systems—such as adapting operations based on return volume and product condition—can enhance responsiveness and efficiency. This reinforces the strategic value of dynamic, volume-sensitive decision-making, as illustrated in our simulation results.

From an economic perspective, while the costs of operator travel and additional labor for on-site inspections must be considered, these are often compensated by the avoidance of transportation of the flooring and related handling costs. The higher the volume of flooring requiring remanufacturing, the greater the potential savings from minimizing transportation-related expenses. Consequently, this approach can contribute to the optimization of both environmental and economic performance, making it a strategically sound choice in scenarios with substantial remanufacturing needs.

In contrast, when only a small proportion of the flooring requires remanufacturing, it may be more efficient to conduct inspections at the manufacturer’s facility. This is particularly relevant when the volume of flooring to be inspected and processed does not justify the additional costs associated with transporting operators to the customer’s location and conducting the remanufacturing there. In such scenarios, the cost involved in on-site inspections—such as time, logistics coordination, and labor costs—may outweigh the potential savings from reducing transportation.

Moreover, the manufacturer’s facility is typically better equipped to handle a variety of remanufacturing processes and can achieve higher efficiencies due to economies of scale, which may not be achievable in on-site operations for smaller volumes. By centralizing the inspection and remanufacturing activities at the manufacturer’s location, companies can optimize operational efficiency and minimize the overall cost per unit of remanufactured flooring.

The decision to prioritize on-site inspections or centralize operations at the manufacturer’s facility should be based on a thorough analysis of remanufacturing volumes. When large volumes of flooring require remanufacturing, on-site inspections are likely to yield better environmental and economic outcomes. Conversely, for smaller volumes, centralizing operations at the manufacturer’s facility remains a more efficient option.

In conclusion, the volume of remanufactured flooring plays a key role in determining the most appropriate strategy for optimizing the balance between sustainability and economic viability. A comprehensive approach that integrates remanufacturing volume with logistical considerations is crucial for maximizing the effectiveness CE practices in the flooring sector. The conclusion that the quality of the returned product significantly influences the optimal CE strategy (remanufacturing vs. recycling vs. disposal) extends to any sector engaging in product recovery operations, which frequently occurs in industries such as the electronics, automotive, and industrial equipment industries. This reinforces the importance of quality-based decision-making frameworks for CE implementations.

### 4. Digital twins and dynamic decision-making help improve sustainability

To maximize the effectiveness of CE practices, companies must adopt a dynamic and flexible decision-making approach that integrates both environmental and economic considerations. The optimal strategy is not static and depends on several factors that can vary over time, such as transportation distance, the quality of the flooring materials, and the specific required characteristics of the product. As these factors can fluctuate, it is crucial for companies to regularly reassess their strategies to ensure that they are selecting the most efficient approach for each situation.

A flexible decision-making framework allows companies to adapt their strategies in real time based on changing operational conditions. For example, when transportation distances are short, prioritizing recycling or centralizing inspections may be more environmentally and economically favorable. Conversely, for long-distance logistics, inspection and remanufacturing processes at the customer’s facility could minimize transportation costs and environmental impacts. By continuously evaluating these variables, companies can ensure that their strategies remain aligned with both their sustainability goals and economic objectives.

The importance of adaptive decision-making has been consistently highlighted in recent literature. Okorie et al. [35] argued that combining multiple simulation approaches (e.g., DESs, SD, and agent-based modeling) allows companies to handle complex, variable CE environments more effectively, especially in contexts with fluctuating return flows and uncertain product conditions. Similarly, Lieder et al. [41] used agent-based models to simulate dynamic customer behaviors and policy effects, and showed how data-driven flexibility enhances the adoption and performance of CE strategies.

To support dynamic decision-making, companies should leverage simulation approaches through the implementation of decision-support tools or software. These tools can analyze a wide range of scenarios and provide insights into how best to optimize logistics, inspection processes, and remanufacturing volumes. By integrating data on transportation distances, product quality, remanufacturing requirements, and other relevant factors, companies can model various strategies and predict their impacts on both environmental sustainability and economic performance. Simulation models can help companies assess how changes in one variable, such as an increase in remanufacturing volume or a shift in transportation distance, will influence the overall performance. This approach not only improves the accuracy of decision-making but also enhances the company’s ability to respond to emerging trends, shifts in customer demand, and regulatory changes.

Furthermore, by adopting decision-support tools, companies can track key performance indicators related to environmental sustainability, operational efficiency, and costeffectiveness. This continuous monitoring of performance allows for iterative improvements and ensures that companies can stay competitive in a rapidly evolving CE landscape.

In conclusion, companies aiming to integrate sustainable practices into their operations should adopt flexible, data-informed strategies that account for the variability of key factors. The methodology used was demonstrated to be a robust approach for testing CE strategy scenarios. This digital twin framework is broadly applicable to manufacturing systems in order to assess the environmental and economic trade-offs prior to physical implementation. By utilizing decision-support systems to analyze and optimize these factors, companies can enhance their operational efficiency, improve their environmental performance, and ensure that their practices align with long-term sustainability goals. Managers are encouraged to embed simulation tools like the proposed digital twin model into operational planning processes. These tools can be updated with real-time data to adapt CE strategies to changing customer behaviors, market demands, or regulatory pressures.

## 6. Conclusions

The study highlights the importance of evaluating reverse logistics strategies in a CE landscape and considering both economic and environmental performance. On-site inspections at customers’ locations offer significant environmental benefits by reducing transportation. However, short transportation distances may make recycling at the manufacturer’s facility more cost-effective, despite the higher environmental impact. Large remanufacturing volumes benefit from on-site inspections, while small volumes may be more efficiently handled at the manufacturer’s facility. The study highlights the importance of dynamic, data-driven decision-making through using simulation tools to optimize logistics and CE practices, thereby balancing sustainability with cost-effectiveness.

Future studies should focus on the further validation of the proposed model across diverse industrial contexts to ensure its generalizability and robustness in various operational environments. This would involve testing the model in industries with different workflows, constraints, and decision-making structures. Additionally, future works could incorporate sensitivity testing of key variables—such as transportation cost coefficients, quality distribution assumptions, and carbon intensity factors—to assess the stability of the model’s recommendations under varying conditions. Finally, integrating real-time data into the model is crucial for enhancing its responsiveness and relevance in dynamic settings. Such integration would enable the model to support adaptive decision-making processes, allowing organizations to respond more effectively to changing conditions and operational uncertainties.

**Author Contributions:** Conceptualization, M.R., M.C. and M.F.; methodology, M.R., M.C. and R.A.; software, M.R.; validation, M.R. and R.A.; formal analysis, M.F.; investigation, M.C. and M.F.; resources, U.D. and R.M.; data curation, M.C.; writing—original draft preparation, M.R.; writing—review and editing, R.M.; supervision, U.D. and R.M.; project administration, U.D. All authors have read and agreed to the published version of the manuscript.

**Funding:** This research was conducted within the framework of the SIIP “Sustainable Intelligent Industrial Planning” project funded by Ministero delle Imprese e del Made in Italy (MIMIT) under Grant Agreement No. F/310195/01-04/X56. The authors acknowledge that this output only reflects their views, and the funding authority cannot be held responsible for any use of the information contained herein.

**Institutional Review Board Statement:** Not applicable.

**Informed Consent Statement:** Not applicable.

**Data Availability Statement:** The data presented in this study are available on request from the corresponding author due to privacy or ethical restrictions.

**Acknowledgments:** The authors gratefully acknowledge the support of the company involved for its collaboration and contribution to this study.

**Conflicts of Interest:** Authors Raffaele Abbate and Umberto Daniele were employed by the company Enginfo Consulting Srl. The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## References

1. Lu, F.; Hao, H.; Bi, H. Evaluation on the development of urban low-carbon passenger transportation structure in Tianjin. _Res. Transp. Bus. Manag._ **2024** , _55_ , 101142. [CrossRef]

2. Paris Agreement. In _Report of the Conference of the Parties to the United Nations Framework Convention on Climate Change (21st Session, 2015: Paris)_ ; HeinOnline: Getzville, NY, USA, 2017; Volume 4, p. 2.

3. Regulation (EU) 2021/1119 of the European Parliament and of the Council of 30 June 2021 Establishing the Framework for Achieving Climate Neutrality and Amending Regulations (EC) No 401/2009 and (EU) 2018/1999 (‘European Climate Law’). _Off. J. Eur. Union_ **2021** , _243_ , 1–17.

4. Fantozzi, I.C.; Di Luozzo, S.; Schiraldi, M.M. The Impact of University Challenges on Students’ Attitudes and Career Paths in Industrial Engineering: A Comparative Study. _Sustainability_ **2024** , _16_ , 1600. [CrossRef]

5. Neves, S.A.; Marques, A.C. Drivers and barriers in the transition from a linear economy to a circular economy. _J. Clean. Prod._ **2022** , _341_ , 130865. [CrossRef]

6. Gharfalkar, M.; Ali, Z.; Hillier, G. Clarifying the disagreements on various reuse options: Repair, recondition, refurbish and remanufacture. _Waste Manag. Res._ **2016** , _34_ , 995–1005. [CrossRef] [PubMed]

7. Manco, P.; Caterino, M.; Rinaldi, M.; Macchiaroli, R. A sustainability-oriented methodology to compare production strategies: The case of AM-based remanufacturing. _J. Clean. Prod._ **2023** , _423_ , 138594. [CrossRef]

8. Arnold, M.; Palomäki, K.; Le Blévennec, K.; Koop, C.; Geerken, T.; Jensen, P.; Colgan, S. _Contribution of Remanufacturing to Circular Economy_ ; Eionet Report-ETC/WMGE; European Environment Agency: Copenhagen, Denmark, 2021; Volume 10.

9. Ghisellini, P.; Ulgiati, S. Circular economy transition in Italy. Achievements, perspectives and constraints. _J. Clean. Prod._ **2020** , _243_ , 118360. [CrossRef]

10. Han, F.; Sun, M.; Jia, X.; Klemeš, J.J.; Shi, F.; Yang, D. Agent-based model for simulation of the sustainability revolution in eco-industrial parks. _Environ. Sci. Pollut. Res._ **2022** , _29_ , 23117–23128. [CrossRef]

11. de Paula Ferreira, W.; Armellini, F.; De Santa-Eulalia, L.A. Simulation in industry 4.0: A state-of-the-art review. _Comput. Ind. Eng._ **2020** , _149_ , 106868. [CrossRef]

12. Caterino, M.; Greco, A.; D’ambra, S.; Manco, P.; Fera, M.; Macchiaroli, R.; Caputo, F. Simulation Techniques for Production Lines Performance Control. _Procedia Manuf._ **2020** , _42_ , 91–96. [CrossRef]

13. Leoni, L.; Cantini, A.; BahooToroody, F.; Khalaj, S.; De Carlo, F.; Abaei, M.M.; BahooToroody, A. Reliability estimation under scarcity of data: A comparison of three approaches. _Math. Probl. Eng._ **2021** , _2021_ , 5592325. [CrossRef]

14. Leoni, L.; De Carlo, F.; Abaei, M.M.; BahooToroody, A.; Tucci, M. Failure diagnosis of a compressor subjected to surge events: A data-driven framework. _Reliab. Eng. Syst. Saf._ **2023** , _233_ , 109107. [CrossRef]

15. Zils, M.; Howard, M.; Hopkinson, P. Circular economy implementation in operations & supply chain management: Building a pathway to business transformation. _Prod. Plan. Control._ **2025** , _36_ , 501–520.

16. Bressanelli, G.; Perona, M.; Saccani, N. Challenges in supply chain redesign for the Circular Economy: A literature review and a multiple case study. _Int. J. Prod. Res._ **2019** , _57_ , 7395–7422. [CrossRef]

17. Ravichandran, M.; Vimal, K.E.K.; Kumar, V.; Kulkarni, O.; Govindaswamy, S.; Kandasamy, J. Environment and economic analysis of reverse supply chain scenarios for remanufacturing using discrete-event simulation approach. _Environ. Dev. Sustain._ **2024** , _26_ , 10183–10224. [CrossRef] [PubMed]

18. Hsieh, H.-H.; Yao, K.-C.; Wang, C.-H.; Chen, C.-H.; Huang, S.-H. Using a Circular Economy and Supply Chain as a Framework for Remanufactured Products in the Rubber Recycling Industry. _Sustainability_ **2024** , _16_ , 2824. [CrossRef]

19. Kirchherr, J.; Reike, D.; Hekkert, M. Conceptualizing the circular economy: An analysis of 114 definitions. _Resour. Conserv. Recycl._ **2017** , _127_ , 221–232. [CrossRef]

20. Caterino, M.; Fera, M.; Macchiaroli, R.; Pham, D.T. Cloud remanufacturing: Remanufacturing enhanced through cloud technologies. _J. Manuf. Syst._ **2022** , _64_ , 133–148. [CrossRef]

21. Panagou, S.; La Cava, G.; Fruggiero, F.; Mancusi, F. Selective complexity determination at cost based alternatives to re-manufacture. In _IFIP International Conference on Advances in Production Management Systems_ ; Springer Nature: Cham, Switzerland, 2023; pp. 215–228.

22. Leoni, L.; De Carlo, F.; Sgarbossa, F.; Paltrinieri, N. Comparison of risk-based maintenance approaches applied to a natural gas regulating and metering station. _Chem. Eng. Trans._ **2020** , _82_ , 115–120.

23. Liu, C.; Yang, Y.; Liu, X. A holistic sustainability framework for remanufacturing under uncertainty. _J. Manuf. Syst._ **2024** , _76_ , 540–552. [CrossRef]

24. Jakowczyk, M.; Quariguasi Frota Neto, J.; Gibson, A.; Van Wassenhove, L.N. Understanding the market for remanufactured products: What can we learn from online trading and Web search sites? _Int. J. Prod. Res._ **2017** , _55_ , 3465–3479. [CrossRef]

25. Mahalakshmi, S.; Nallasivam, A.; Kumar, H.; Kautish, S.; Madan, S. From Assembly to Reassembly: Ikea’s Circular Design for a Sustainable Future. In _Utilizing Technology for Sustainable Resource Management Solutions_ ; IGI Global: Hershey, PA, USA, 2024; pp. 261–280.

26. Mallick, P.K.; Salling, K.B.; Pigosso, D.C.; McAloone, T.C. Closing the loop: Establishing reverse logistics for a circular economy, a systematic review. _J. Environ. Manag._ **2023** , _328_ , 117017. [CrossRef]

27. Dat, L.Q.; Linh, D.T.T.; Chou, S.-Y.; Yu, V.F. Optimizing reverse logistic costs for recycling end-of-life electrical and electronic products. _Expert Syst. Appl._ **2012** , _39_ , 6380–6387. [CrossRef]

28. Errington, M.; Childe, S.J. A business process model of inspection in remanufacturing. _J. Remanuf._ **2013** , _3_ , 7. [CrossRef]

29. Lander, L.; Tagnon, C.; Nguyen-Tien, V.; Kendrick, E.; Elliott, R.J.; Abbott, A.P.; Edge, J.S.; Offer, G.J. Breaking it down: A techno-economic assessment of the impact of battery pack design on disassembly costs. _Appl. Energy_ **2023** , _331_ , 120437. [CrossRef]

30. Smith, S.; Hsu, L.-Y.; Smith, G.C. Partial disassembly sequence planning based on cost-benefit analysis. _J. Clean. Prod._ **2016** , _139_ , 729–739. [CrossRef]

31. Guevara-Rivera, E.; Osorno-Hinojosa, R.; Zaldívar-Carrillo, V.H. A simulation methodology for circular economy implementation. In Proceedings of the 2020 10th International Conference on Advanced Computer Information Technologies (ACIT), Deggendorf, Germany, 16–18 September 2020; IEEE: Piscataway, NY, USA, 2020; pp. 43–48.

32. Guevara-Rivera, E.; Osorno, R.H.; Zaldivar-Carrillo, V.; Perez-Ortiz, H. Dynamic simulation methodology for implementing circular economy: A new case study. _J. Ind. Eng. Manag._ **2021** , _14_ , 850–862. [CrossRef]

33. Charnley, F.; Tiwari, D.; Hutabarat, W.; Moreno, M.; Okorie, O.; Tiwari, A. Simulation to enable a data-driven circular economy. _Sustainability_ **2019** , _11_ , 3379. [CrossRef]

34. Goodall, P.; Sharpe, R.; West, A. A data-driven simulation to support remanufacturing operations. _Comput. Ind._ **2019** , _105_ , 48–60. [CrossRef]

35. Okorie, O.; Charnley, F.; Ehiagwina, A.; Tiwari, D.; Salonitis, K. Towards a simulation-based understanding of smart remanufacturing operations: A comparative analysis. _J. Remanuf._ **2020** , _14_ , 45–68. [CrossRef]

36. He, P. Optimization and Simulation of Remanufacturing Production Scheduling under Uncertainties. _Int. J. Simul. Model._ **2018** , _17_ , 734–743. [CrossRef]

37. Stamer, F.; Sauer, J. Optimizing quality and cost in remanufacturing under uncertainty. _Prod. Eng._ **2024** , _19_ , 369–390. [CrossRef]

38. Zhang, R.; Ong, S.; Nee, A. A simulation-based genetic algorithm approach for remanufacturing process planning and scheduling. _Appl. Soft Comput._ **2015** , _37_ , 521–532. [CrossRef]

39. Huster, S.; Glöser-Chahoud, S.; Rosenberg, S.; Schultmann, F. A simulation model for assessing the potential of remanufacturing electric vehicle batteries as spare parts. _J. Clean. Prod._ **2022** , _363_ , 132225. [CrossRef]

40. Li, X.; Mu, D.; Du, J.; Cao, J.; Zhao, F. Game-based system dynamics simulation of deposit-refund scheme for electric vehicle battery recycling in China. _Resour. Conserv. Recycl._ **2020** , _157_ , 104788. [CrossRef]

41. Lieder, M.; Asif, F.M.; Rashid, A. Towards Circular Economy implementation: An agent-based simulation approach for business model changes. _Auton. Agents Multi-Agent Syst._ **2017** , _31_ , 1377–1402. [CrossRef]

42. Available online: https://cordis.europa.eu/project/id/101003893 (accessed on 23 February 2025).

43. Available online: https://circulareconomy.europa.eu/platform/en/good-practices/iobac-adhesive-free-flooring-tiles-whichcan-be-readily-reused-and-recycled (accessed on 23 February 2025).

44. Available online: https://circulareconomy.europa.eu/platform/en/good-practices/circular-flooring-partnership-tarkett-ikea (accessed on 23 February 2025).

45. Parvaresh, F.; Amini, M.H. Application of circular economy for sustainable waste management in the carpet industry. _Int. J. Res. Ind. Eng._ **2024** , _13_ , 188–206.

46. Wiesinger, H.; Bleuler, C.; Christen, V.; Favreau, P.; Hellweg, S.; Langer, M.; Pasquettaz, R.; Schönborn, A.; Wang, Z. Legacy and Emerging Plasticizers and Stabilizers in PVC Floorings: Impacts of an Industrial Transition and Recycling. _Environ. Sci. Technol._ **2024** , _58_ , 1894–1907. [CrossRef]

47. Jeswiet, J.; Kara, S. Carbon emissions and CES™in manufacturing. _CIRP Ann._ **2008** , _57_ , 17–20. [CrossRef]

48. Rinaldi, M.; Caterino, M.; Fera, M.; Manco, P.; Macchiaroli, R. Technology selection in green supply chains-the effects of additive and traditional manufacturing. _J. Clean. Prod._ **2021** , _282_ , 124554. [CrossRef]

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
