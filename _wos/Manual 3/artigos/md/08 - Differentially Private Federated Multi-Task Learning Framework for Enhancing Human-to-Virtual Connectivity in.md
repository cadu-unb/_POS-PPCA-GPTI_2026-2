## Differentially Private Federated Multi-Task Learning Framework for Enhancing Human-to-Virtual Connectivity in Human Digital Twin

This paper was downloaded from TechRxiv (https://www.techrxiv.org).

LICENSE

CC BY 4.0

SUBMISSION DATE / POSTED DATE

13-06-2023 / 14-06-2023

CITATION

Okegbile, Samuel; Cai, Jun; Zheng, Hao; Chen, Jiayuan; Yi, Changyan (2023). Differentially Private Federated Multi-Task Learning Framework for Enhancing Human-to-Virtual Connectivity in Human Digital Twin. TechRxiv. Preprint. https://doi.org/10.36227/techrxiv.23511720.v1

DOI

10.36227/techrxiv.23511720.v1

# Differentially Private Federated Multi-Task Learning Framework for Enhancing Human-to-Virtual Connectivity in Human Digital Twin

Samuel D. Okegbile, _Member, IEEE,_ Jun Cai, _Senior Member, IEEE,_ Hao Zheng, Jiayuan Chen, and Changyan Yi, _Member, IEEE_

**_Abstract_ —Ensuring reliable update and evolution of a virtual twin in human digital twin (HDT) systems depends on any connectivity scheme implemented between such a virtual twin and its physical counterpart. The adopted connectivity scheme must consider HDT-specific requirements including privacy, security, accuracy and the overall connectivity cost. This paper presents a new, secure, privacy-preserving and efficient humanto-virtual twin connectivity scheme for HDT by integrating three key techniques: differential privacy, federated multi-task learning and blockchain. Specifically, we adopt federated multitask learning, a personalized learning method capable of providing higher accuracy, to capture the impact of heterogeneous environments. Next, we propose a new validation process based on the quality of trained models during the federated multi-task learning process to guarantee accurate and authorized model evolution in the virtual environment. The proposed framework accelerates the learning process without sacrificing accuracy, privacy and communication costs which, we believe, are nonnegotiable requirements of HDT networks. Finally, we compare the proposed connectivity scheme with related solutions and show that the proposed scheme can enhance security, privacy and accuracy while reducing the overall connectivity cost.**

**_Index Terms_ —Blockchain, digital twin, federated multi-task learning, privacy, virtual twin.**

### I. INTRODUCTION

Digital twin (DT) continues to attract wide attention, especially in communications networks [1], healthcare [2], [3], and manufacturing [4], [5] because of its ability to improve the current systems by leveraging newly emerged algorithms including machine learning, optimization and artificial intelligence as well as communication technologies, such as edge intelligence, security and privacy-preservation. When adopted, DT is capable of allowing a digital representation of real-world equipment, process, objects or environment by creating corresponding virtual twins (VTs) in the virtual space [6]. Specifically, in human-centric systems such as medical cyber-physical systems, the human digital twin (HDT) facilitates the co-evolution of both humans and VTs [2], and thus can transform the current healthcare systems, environmental monitoring systems, and other applications by involving human behaviour and activities.

> S. D. Okegbile and J. Cai are with the Network Intelligence and Innovation Lab ( _NI_<sup>2</sup> _L_ ), Department of Electrical and Computer Engineering, Concordia University, Montreal QC H3G 1M8, Canada (Emails: samuel.okegbile@concordia.ca; jun.cai@concordia.ca).

> H. Zheng, J. Chen and C. Yi are with the College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing, Jiangsu, 211106, China (Emails: zhenghao@nuaa.edu.cn; jiayuan.chen@nuaa.edu.cn; changyan.yi@nuaa.edu.cn).

Generally, an HDT encompasses any human being, otherwise called a physical twin (PT), in the physical environment, its corresponding VT in the virtual environment, and a mapping between these two environments through reliable data links [2]. This mapping is expected to ensure continuous and reliable interactions between human-virtual twin pairs considering the dynamic nature of the physical environment. While HDT can significantly improve the quality of services and experiences in the physical environment, the diverse requirements [1]–[3], [6] in terms of latency, privacy, security, reliability, data rate, and other user-defined performance metrics make it very complicated and challenging to achieve a reliable mapping or connectivity between physical and virtual environments [7]. Furthermore, there are currently insufficient possibilities for the physical-virtual environment synchronizations to establish closed loops, a lack of highfidelity and quantification models as well as difficulties in obtaining accurate predictions of complex physical systems [4]. All these make HDT suffer in many aspects in terms of accuracy, security, privacy, synchronization and connectivity.

To address security and privacy issues, blockchain and federated learning (FL) techniques have been widely adopted in recent DT solutions [3], [8], [9] owing to their ability to support the training of machine learning models in a decentralized manner. However, the adoption of blockchain often relies on high latency and energy-intensive consensus algorithms [10], which cannot meet the specific requirements of HDT. In addition, although FL can address privacy concerns, privacy leakage is still possible. When clients synchronize their learned model parameters with the global server, an attacker may infer some data properties or recover the raw data based on this shared information [11], [12]. Moreover, conventional FL suffers from many challenges such as statistical heterogeneity, high computation and communication costs, and limited fault tolerance. Thus, an effective solution for HDT integrating blockchain and FL has to be proposed, which can accelerate the learning process without sacrificing accuracy, privacy and communication costs.

### A. Contributions

Although connectivity problems in HDT [3], DTempowered 6G networks [8] and DT edge networks [9] have earlier been studied, they may suffer from high latency that characterizes traditional blockchain-enabled systems, as well as data leakages and statistical heterogeneity issues that characterize the conventional FL schemes. In addition, synchronization accuracy is an important metric in HDT for sufficient performance evaluations. However, such a metric is difficult to obtain and has been neglected in previous works. Moreover, the effects of scheduled offloading rates with queueing constraints for a status update and privacy budget on both the synchronization cost and the overall HDT system performance have never been studied.

To address all these issues, in this paper, we proposed a new HDT framework, which integrates differential privacy, federated multi-task learning (FML) [11] and quality trainingbased validation process, a lightweight blockchain-enabled consensus method, in the presence of heterogeneous environments. The proposed framework finds the balance between synchronization accuracy and connectivity cost without compromising security and privacy which, we believe, are nonnegotiable requirements of HDT networks. To the best of our knowledge, such a framework that captures statistical heterogeneity, synchronization accuracy, synchronization cost and other related performance has never been presented. The contributions of this paper are thus summarized as follows:

- We propose a secure differentially private federated multitask learning (DPFML) framework for HDT by integrating the DPFML and a computational-efficient blockchainenabled validation process to provide a secure, privacypreserving and more accurate human-to-virtual twin connectivity solution.

- We analytically study the connectivity cost of the proposed DPFML-enabled connectivity scheme to investigate the influence of some important system parameters, including privacy budget, on synchronization cost as well as the long-term average connectivity cost, overall time cost and energy cost. To capture the validation cost inherent in blockchain, we propose a new consensus mechanism based on the quality of trained models during FL, called proof of model quality (PoMQ).

- Following this, we formulate a connectivity problem in the proposed DPFML-based framework as a Markov decision process (MDP) to minimize the connectivity cost. To solve the MDP, we propose a deep reinforcement learning (DRL) algorithm using the deep deterministicpolicy gradient (DDPG) approach.

- Finally, we compare the proposed framework with existing frameworks through simulation and demonstrate the ability of the proposed solution to offer synchronization accuracy and reduced connectivity cost without compromising security and privacy.

### B. Organization

The remainder of this paper is structured as follows. Section II reviews related works, while Section III introduces the details of the proposed system model. In Section IV, we present the analysis of the connectivity cost in terms of time, privacy and energy costs. The formulated MDP-based optimization problems and DRL-based solutions are presented in Section V. Section VI discuss the simulation results and the performance of the proposed scheme, while Section VII concludes this paper.

### II. RELATED WORK

In this section, we discuss some of the earlier presented related frameworks and solutions. For clarity, we categorized these existing works into three: the human digital twin, FL in DT applications and differentially private solutions for FL.

### A. Human digital twin

HDT is an emerging technology that is recently attracting more consideration in many domains, including medical, sports and manufacturing [13]. It relies on the concept of DT to create a virtual replica of human, body organs or habits in the virtual environment [2]. Note that DT provides enhanced system performance by combining both system models and analyses with real-time measurements for any individual system. It facilitates model evolutions over the lifecycle of any physical system while supporting the derivation of solutions with the ability to aid real-time optimizations of such a physical system.

Similar to DT, HDT possesses the potential to revolutionize the practice of human system integration by adopting realtime sensing and feedback to tightly couple measurements of human performance, behaviour, as well as the influence of environment throughout a product’s life cycle, on human modelling to improve system design and performance [13]. Unlike the VT in the conventional DT, however, human VTs often possess distinct underlying variability among each other as well as dependence between humans and products in the physical environment. Since each human VT (referred to as VT henceforth for simplicity) evolves with data from its counterpart PT, located in the physical environment, its design and implementation are known to be very difficult.

A DT solution was presented in [14] for elderly healthcare services, while [15] discussed a deep neural-based model for capturing bi-directional context relationships when predicting lung cancer. A software-based HDT was similarly presented in [16] for tracking fitness-related measurements describing an athlete’s behaviour on consecutive days, while the work in [17] presented a cardio twin architecture for the detection of ischemic heart disease. In [18], a DT ecosystem for health and well-being was presented. It is worth mentioning that, although the majority of [14]–[18] discussed the importance of connectivity in HDT, none of these works delved into investigating and modelling this connectivity scheme. In [3], an edge-assisted connectivity framework for HDT was presented. While the presented framework is interesting, statistical heterogeneity, synchronization accuracy and other related performance issues such as data leakages were not considered. This paper addresses these limitations by proposing a connectivity scheme that considered all important HDT-specific requirements including statistical heterogeneity, synchronization accuracy and data leakages.

### B. FL in DT applications

One of the underlying limitations of DT and HDT applications is privacy. Since every physical object must continuously share its data with its corresponding VT, privacy becomes an important concern. To address this, the work in [3] adopted FL to preserve data privacy in HDT networks. Similarly, FL was adopted in [7], [8] to learn a behavioural model from user data towards achieving low latency in DT-empowered 6G networks and in [9] to achieve efficient communication in DT edge networks since offloading all running data to the VT can incur a large amount of communication resource, cost, and time while leading to privacy issues. In a similar work, the authors in [19] carried out an optimization of FL using the DRL method to construct the DT-empowered industrial IoT model. The work proposed an asynchronous FL scheme that is capable of addressing the discrete effects caused by heterogeneous industrial IoT devices. A cooperative FL was developed in [20] to facilitate DT construction in resource-limited smart devices. An iterative double auction-based joint cooperative FL with an update verification scheme was designed.

In [21], an FL-based anomaly detection model was proposed using DT by utilizing edge cloudlets when running anomaly detection models locally, while the work in [22] presented a blockchain-enabled adaptive asynchronous FL paradigm for privacy-preserving and decentralized DT networks. However, these works do not consider possible data leakages in conventional FL algorithms which is important in HDT. Similarly, connectivity problems were only studied in HDT [3], and DT-enabled wireless networks [7]–[9], where the influence of statistical heterogeneity and synchronization accuracy on the connectivity cost was not considered. Sharing gradients as in federated averaging can lead to data leakage. As a result, cryptographic-based approaches have also been explored in some FL-based research [23] although such approaches are computationally inefficient in large-scale machine-learning models. Recently, differential privacy (DP) is being explored in FL to reduce the possibility of information leakages by hiding the contribution of each client during training thereby ensuring privacy guarantees.

### C. DP solutions for FL

DP solutions are efficient techniques that can provide privacy guarantees in machine learning [24]. It is therefore unsurprising that such approaches have recently been attracting a lot of interest in FL-based research. By adding artificial noise to the learned model parameters or datasets, DP can protect nodes’ privacy with limited computation. It, however, tends to reduce the overall accuracy as the privacy protection level increases. Thus, a trade-off exists between accuracy and privacy. In [12], a differentially private FL framework was adopted to prevent privacy leakages during data sharing to model the contribution, computation, communication, and privacy costs of each participant. Also, security and privacy concerns in the standard FL continue to hinder its wide adoption in urban applications, hence a differentially private asynchronous FL scheme was proposed in [25] for resource sharing in vehicular networks by integrating DP and FL techniques.

Table I

COMMON NOTATIONS USED

|Notation|Definition|
|---|---|
|$\mathcal{L}_i$|Learning task of local aggregator or client $i$|
|$M$|Total number of related local aggregators|
|$V$|Total number of validators|
|$D_i$; $D_i(t)$|Data size of client $i$; Data size of client $i$ at time $t$|
|$o_i$|Status update offloading scheduling rate of client $i$|
|$\varrho_i$|Service rate of client $i$|
|$\sigma$|Gaussian noise variance|
|$N_R$|Number of communication rounds|
|$G_S$|Local gradient sensitivity|
|$g^t$|Gradient|
|$\eta$|Learning rate|
|$N_E$|Number of local epochs|
|$\epsilon$; $\delta$|Privacy budget; Additive term|
|$\theta^{\mu}$|Weights parameter of the actor network|
|$\theta^{\mathcal{O}}$|Weights parameter of the critic network|
|$c_r$|CPUs required to execute a sample of training data|
|$c_i$|CPU frequency of any local aggregator $i$|
|$\kappa_i$|Coefficient dependency on the chip architecture|
|$\gamma$|Discount factor|
|$\theta_{off}$|Offloading threshold|
|$\theta_{pvy}$|Privacy cost threshold|
|$\theta_{cmp}$|Computation cost threshold|

While a differentially private FL framework can ensure privacy guarantees when adopted, the inherent issues of statistical heterogeneity are the main concern. Hence, any differentially private FL-based framework can suffer from accuracy degradation when used in a network with non-independent and identically distributed (non-iid) data. To address these issues associated with differentially private FL, especially in HDT, where data from PTs are arbitrarily heterogeneous with fundamental statistical heterogeneity issues, while also noting the presence of many external conditions that can influence the behaviour of each PT such as environment and genetic information, we propose DPFML framework following the privacy-aware multi-task learning approach, first discussed in [11]. This ensures a federated optimization of heterogeneous tasks while protecting the local model gradient information using DP.

A DPFML-enhanced framework can enable federated optimization of heterogeneous client tasks while protecting the local model gradient information through DP. Such a technique can prevent privacy leakage, and ensure accuracy, privacy and reduced communication costs when properly adopted. Since in HDT networks, many external factors may influence the performance of the entire system, while some unique structures may exist among different people [26], it is desirable to simultaneously achieve learning models for multiple related tasks through an efficient multi-task learning framework. The proposed DPFML-enabled HDT connectivity solution can learn customized context-aware policies from multiple users and environments in a privacy-preserving manner. The definitions of some common notations used throughout this paper are summarized in Table I.

### III. SYSTEM MODEL

We consider a DPFML-enabled HDT system, where the physical and the virtual environments are connected through a blockchain and FML-enabled connectivity scheme as shown in Fig. 1. Data are generated by each PT (based on its update scheduling rate), located in the physical environment, to maintain a reasonable synchronization with its counterpart VT, located in the virtual environment. The physical environment is equipped with multiple local aggregators (LAs) corresponding to different entities of the physical environment, such as the typical PT, genetic information, environmental factors, etc. Each LA is connected with various sensing devices for data capturing and produces both shared and task-specific parameters, from its locally trained model and based on its local data. The shared parameter is then offloaded to the global aggregator (GA) for aggregation following the standard FL during the first phase. At the beginning of the second phase, each LA will forward its locally trained task-specific model to the validators, located in the virtual environment, to evaluate its quality, before the VT model updating and evolution in the final phase. The main components of the system model are summarized as follows.

Figure 1. Overview of the system model.

- **Environment:** The physical environment depicts the realworld space, where every PT interacts with other entities within its environment and maintains a dependent relationship with such related entities. A virtual replica of each PT is maintained in the virtual environment.

- **Local Aggregator:** Also called client, each LA represents a distinct entity in the physical environment. Each of these clients consists of several sensing devices to regularly collect data from the physical environment. The collected data by each LA are aggregated, subject to its update scheduling rate _oi_ , and are used to support learning during the FML. In the proposed HDT framework, each LA is responsible for updating the corresponding aspect of its associated VT, using the task-specific models, after the training quality requirements have been satisfied.

- **Global aggregator:** The GA is a central server that facilitates aggregation of shared parameters during FML, and also provides the training requirement thresholds to validators during validation. At every communication round, the global model (which contains the aggregated shared parameters) is used to locally train each taskspecific model at each LA.

- **Validators:** Validators are essential components of the blockchain system that ensures the reliability of every update from each client before triggering the model evolution process in the virtual environment. Without this, the system cannot guarantee accurate and authorized model evolution of any corresponding VT. The blockchain also keeps the records of previous model evolution activities to ensure traceability. Since each LA is responsible for updating its associated VT, it becomes imperative to have an independent validation process.

- **Model evolution:** This is the process of updating any typical VT based on the task-specific parameters received from its counterpart physical pair. It is an important part of any HDT framework and its construction is beyond the scope of this current paper.

Assume that there are $M$ LAs, each with a learning task $\mathcal{L}_i, \forall i \in \{1, 2, ..., M\}$ as in Fig. 1. Each LA contains a training dataset $\mathcal{D}_i = \cup_{j=1}^{D_i}\{(x_{i,j}, y_{i,j})\}$, generated from different sensing devices as in [3], where $D_i$ is the data size, $x_{i,j}$ is the data of size $j$ collected by client $i$ and $y_{i,j}$ is the label of $x_{i,j}$. In practice, the general aim of the HDT framework is to maintain the VT of each physical entity (e.g., body organ, habit, eating pattern, etc.) in the virtual environment while capturing the dependence of such a physical entity on other related components observed in the physical environment. As a result, LAs in the HDT framework are related to each other (e.g., a dependence exists between any PT, and its environment and genetic information) such that locally trained models from different LAs share some common underlying representation. To capture this in the system modelling, the hard parameter sharing technique [27] can be incorporated into the standard FL to obtain FML. This hard parameter-sharing technique has been earlier adopted in neural networks. With this, the shared feature representation can be learned through joint optimization of different tasks via the parameter sharing in the proposed DPFML framework.

While model sharing among various LAs can reduce the effect of insufficient data and improve the overall system accuracy, it also comes with a risk of privacy leakages and statistical heterogeneity. The adoption of the DP technique ensures that privacy leakages are prevented through applications of Gaussian noises at each LAs. This, however, comes at the expense of accuracy. Thus, we incorporate a double-layer multi-task learning technique [11], where shared parameters are used to improve the training performance at each LA, while task-specific parameters are used to achieve personalization.

### A. Federated multitask learning model

To properly capture statistical heterogeneity, each LA learns a domain classifier to capture transferable feature representations (i.e., shared parameters) across tasks through the hard parameter-sharing technique. The transferable feature representations are offloaded to the GA every communication round for aggregation. After aggregation, the GA forwards the global model to all related LAs. Each LA uses this global model to improve the training of its task-specific models. The aim is to reinforce each task by taking advantage of the interconnections among related tasks while considering both the inter-task relevance and the inter-task difference. Each LA through its domain classifier classifies every feature as either a sharable or task-specific feature by minimizing the distribution difference [28] between its shared and global parameters. This distribution difference can be obtained following the maximum mean discrepancy [29] as

$$
M_{MD}(i, GA) = \left\| \frac{1}{n_i} \sum_{k=1}^{n_i} \Phi(x_i^k) - \frac{1}{n_{GA}} \sum_{l=1}^{n_{GA}} \Phi(x_{M+1}^l) \right\|_{\mathcal{H}}^{2}, \tag{1}
$$

where $n_i$ and $n_{GA}$ are the number of samples drawn from any LA $i$ and GA, respectively and $\Phi(.)$ is the nonlinear mapping into reproducing kernel Hilbert space $\mathcal{H}$. Also, $x_i^k, \forall k = \{1, ..., n_i\}$ and $x_{M+1}^l, \forall l = \{1, ..., n_{GA}\}$ are the feature vectors of LA $i$ and GA, respectively, while $||.||$ represents the norm. For each feature $x_i^k$ in $D_i$, the chances that $x_i^k$ is a sharable feature can be obtained through instance the weight

$$
\mathcal{Q}(x_i^k) = \frac{P(x_i^k \in \mathcal{D}_{\mathrm{shared}})}{1 - P(x_i^k \in \mathcal{D}_{\mathrm{shared}})}, \tag{2}
$$

where _D_ shared is a vector containing the sharable parameters. If we assume a logistic regression-based domain classifier, then the mapping Φ( _i,_ GA) maps the global feature vector to the local feature vector of LA _i_ , while Φ(GA _, i_ ) maps the local feature vector of LA _i_ to the global feature vector, such that

$$
\min_{\Phi(i,\mathrm{GA})} \left\| \mathrm{diag}(\mathcal{Q}_i)\left(x_i^k - x_{M+1}^l \Phi(i,\mathrm{GA})\right) \right\|_F^2 + \lambda \sum_{l=1}^{n_{GA}} \left\| \Phi_l(i,\mathrm{GA}) \right\|_F^2, \tag{3}
$$

$$
\min_{\Phi(\mathrm{GA},i)} \left\| x_i^k - x_{M+1}^l \Phi(\mathrm{GA},i) \right\|_F^2 + \lambda \sum_{k=1}^{n_i} \left\| \Phi_k(\mathrm{GA},i) \right\|_F^2, \tag{4}
$$

where diag( _._ ) transforms an input vector to a diagonal matrix, _||.||F_ is the Frobenius norm and _λ >_ 0 is the regularization parameter. At any round, features with less difference to the global parameter are classified as shared parameters and features with more difference are classified as task-specific parameters. Let the top layers of the double-layer multi-task learning framework, as presented in Fig. 2, capture the taskspecific features _Tf_ , while the lower ones capture the shared features _Sf_ . Then, we can define _Tf_ and _Sf_ as

$$
\begin{aligned}
\mathcal{T}_f &= \{\omega_1, \omega_2, ..., \omega_M\}, \\
\mathcal{S}_f &= \{\omega_{M+1,1}, \omega_{M+1,2}, ..., \omega_{M+1,M}\},
\end{aligned} \tag{5}
$$

where _ωi_ and _ωM_ +1 _,i_ represent the task-specific parameters and the shared parameters of any client _i_ , respectively. As shown in Fig. 2, the local optimization is carried out by each client subject to its local objective function _fi_ , given as

$$
f_i(\omega_i, \omega_{M+1}) = \frac{1}{D_i} \sum_{j=1}^{D_i} \ell(x_{i,j}, y_{i,j}, \omega_i, \omega_{M+1}), \tag{6}
$$

Figure 2. The method of federated multitask learning.

where _ℓ_ is the loss function and _ωM_ +1 is the global model. During the optimization process, _ωM_ +1 is shared among all clients, while the GA carries out the aggregation of local models at each communication round and then distributes it back to all clients after updating the global model. With this, each task aims to learn a function _fi_ , while the global objective is to minimize

$$
f(\omega_{M+1}) = \sum_{i=1}^{M} \Omega_i f_i(\omega_{M+1,i}, \omega_{M+1}), \tag{7}
$$

where $\Omega_i = \left[\frac{D_i}{\sum_{i=1}^{M} D_i}\right]$ captures the weight of the local model for each LA $i \in \{1, 2, ..., M\}$.

Let all participants (i.e., LAs and the GA) be honest but curious. As a result, it is possible that any participant may maliciously attempt to infer some vital information when interacting with other participants. To prevent such a potential privacy violation scenario, randomized noises such as Gaussian noise is introduced at the gradient level following the DP approach. With that, the gradient contribution of each LAs during communication and aggregation can be protected.

The proposed DPFML framework is summarized in Algorithm 1, where each of the $M$ LAs begins the FL process when at least any LA $i \in \{1, 2, ..., M\}$ has a status to update following its update scheduling rate $o_i$, subject to the approval of the GA. As soon as the GA approves the commencement of any status update, each related LA receives the global model $\omega_{M+1}^{t}$ from the GA and updates its locally trained model by computing the gradient for both shared and task-specific layers. Note that the Gaussian noise $n_{M+1,i} \sim \mathcal{N}(0, \sigma^2 G_S^2)$ is only added to the shared models since only the lower layers are shared to capture transferable feature representation. Thus, we reduce the effect of noise on the overall accuracy of the model. The convergence of Algorithm 1 is demonstrated through the simulation presented in Section VI.

DPFML framework ensures privacy guarantees without sacrificing much of the trained model accuracy. Such a framework aims to prevent any attacker or eavesdropper from extracting sensitive information during model exchanges among LAs and the GA. It relies on a common standard method when measuring privacy risk, called $(\epsilon, \delta) - \mathrm{DP}$, where $\epsilon > 0$ is the privacy budget and $\delta \in (0, 1)$ is the additive term. Hence, the possibility that $\epsilon - $ differential privacy is violated is captured by probability $\delta$. A lower $\epsilon$ suggests that the clients have a lower risk of privacy leakage. With DPFML, each client adds artificial Gaussian noise during local training at every round such that $(\epsilon, \delta) - \mathrm{DP}$ of its local datasets is always guaranteed. To ensure accuracy and convergence, the GA determines the privacy budget $\epsilon_{\min} \leq \epsilon \leq \epsilon_{\max}$. When $\epsilon < \epsilon_{\min}$, the added noise is too large thus the training cannot converge. Similarly, when $\epsilon > \epsilon_{\max}$, the added noise is too small and privacy cannot be protected. The GA may also specify the training data size $N_i$, and the corresponding reward $R_i$ to facilitate fairness during the validation process.

Note that any global model at each round includes aggregated uploaded noisy local models. At every communication round $0 \leq t \leq N_R - 1$, the global model is trained using the local models received from all LAs to find a global model parameter $\omega_{M+1}$ that minimizes global loss while ensuring privacy guarantee. With this

$$
\begin{aligned}
& \underset{\omega_{M+1} \in \{\omega_{M+1}^{t}, \forall t < N_R\}}{\arg\max} \; f(\omega_{M+1}) \\
& \text{s.t. } \Pr(\omega_{M+1,i} \in \mathbb{R}_d) \leq \exp(\epsilon) \Pr(\omega'_{M+1,i} \in \mathbb{R}_d) + \delta,
\end{aligned} \tag{8}
$$

where $Pr(\omega_{M+1,i} \in \mathbb{R}_d) \leq Pr(\omega'_{M+1,i} \in \mathbb{R}_d)$ captures the $(\epsilon, \delta) - \mathrm{DP}$ guarantees for $\omega_{M+1,i}$. The parameters $\omega_{M+1,i}, \omega'_{M+1,i} \in \mathbb{R}_d$ are generally called the neighbouring model parameters [24], such that the sensitivity function can be defined as

$$
\Delta_f = \max_{\omega_{M+1,i}, \omega'_{M+1,i}} \left\| f(\omega_{M+1,i} - f(\omega'_{M+1,i})) \right\|. \tag{9}
$$

### B. Blockchain-enabled validation model

HDT relies on accurate modelling of the VT to guarantee performance. However, some LAs may attempt to manipulate the system either by providing an untrained model or misleading data for model updating in the virtual environment. Similarly, a multidimensional information asymmetry [12] may also exist among participants, where selfish participants manipulate their costs to receive more rewards from the system. To ensure that the final model from each LA is accurate and has not been modified through malicious activities, we propose a PoMQ consensus mechanism which offers the validation process in terms of the quality of the trained model during FML rather than solving computational-inefficient hashing puzzles, as in the proof of work. With the PoMQ, the validation process can be carried out before model updating and evolution in the virtual environment. The PoMQ protocol is made up of $V$ validators located in the virtual environment. Multiple validators are necessary to eliminate the possibility of malicious validation. These validators are responsible for validating the training quality of each model. After validation, each validator broadcasts its validation decision to other validators to reach a consensus. A virtual model is updated using any learned model only if the majority of $V$ consent.

### **Algorithm 1** DPFML scheme.

> **Algorithm 1** (DPFML)<br>
> **INPUT:** $M$ clients, Gaussian noise variance $\sigma$, number of rounds $N_R$, local gradient sensitivity $G_S$ number of local epochs $N_E$, learning rate $\eta$.<br>
> **OUTPUT:** Global model $\omega_{M+1}^{t+1}$, task-specific model $\omega_i, \forall i$.<br>
> **INITIALIZE:** $\omega_i$, for all $i \in \{1, 2, ..., M\}$<br>
> **For** each round $t = 0$ to $N_R - 1$ **do**<br>
> &emsp;The GA broadcasts $\omega_{M+1}^{t}$ to all LAs<br>
> &emsp;**For** LA $i \in \{1, 2, ..., M\}$ **do**<br>
> &emsp;&emsp;Synchronize local parameters $\omega_{M+1,i}^{t} \leftarrow \omega_{M+1}^{t}$<br>
> &emsp;&emsp;**For** local epoch $L_E = 0$ to $N_E$ **do**<br>
> &emsp;&emsp;&emsp;Compute gradients for shared layers as $g_{M+1,i}^{t} = \partial_{\omega_{M+1}} f_i(\omega^{t})$<br>
> &emsp;&emsp;&emsp;Perturb gradients for shared layers as $\tilde{g}_{M+1,i}^{t} = g_{M+1,i}^{t} + n_{M+1,i}, \forall n_{M+1,i} \sim \mathcal{N}(0, \sigma^2 G_S^2)$<br>
> &emsp;&emsp;&emsp;Update parameters for shared layers as $\omega_{M+1,i}^{t+1} = \omega_{M+1,i}^{t} - \eta(\tilde{g}_{M+1,i}^{t})$<br>
> &emsp;&emsp;&emsp;Compute gradients for task-specific layers as $g_i^{t} = \partial_{\omega_i} f_i(\omega^{t})$<br>
> &emsp;&emsp;&emsp;Update parameters for task-specific layers as $\omega_i^{t+1} = \omega_i^{t} - \eta g_i^{t}$<br>
> &emsp;&emsp;**End For**<br>
> &emsp;**End For**<br>
> &emsp;Each LA offloads model weight $\omega_{M+1,i}^{t+1}$ to the GA<br>
> &emsp;The GA aggregates the received weights as $\omega_{M+1}^{t+1} = \frac{1}{M} \sum_{i=1}^{M} \omega_{M+1,i}^{t+1}$<br>
> **End For**<br>
> **RETURN** $\omega_{M+1}^{t+1}, \omega_i, \forall i$

The proposed PoMQ evaluates each learned model based on computation cost, communication cost and privacy cost. With this, validators can investigate whether the expenditure by each LA corresponds to the expected costs. The VT is, therefore, only updated when the consensus decision signifies conformity to the requirements. More details on the analysis of the validation process are provided in the next section.

### IV. ANALYSIS

In this section, we first analyze the proposed framework by investigating the physical-virtual environment connectivity cost from time, privacy and energy perspectives. We then obtain analysis for synchronization accuracy before presenting the resulting optimization problem in Section V.

### A. DPFML model

To ensure accurate VT model updating and evolution, data captured from its environment and other individuals with similar behaviour are also used through multi-task learning to improve the performance while boosting the effective sample size for each LA. At every round, each LA carries out local training following (6) and subsequently performs shared and task-specific features classification. The shared model is then offloaded to the GA for aggregation. It is worth noting that the cost of achieving a secure and privacy-preserving connectivity scheme may undermine its benefits. Thus, we aim to minimize the synchronization cost while ensuring accuracy and reliability. Compared to the local training time, the features extractions time at each LA is negligible. Thus, we focus on the local training time to estimate the required time, privacy and energy cost when updating any typical VT.

Let _cr_ and _ci_ represent the number of CPUs required to train one sample of training data and the CPU cycle frequency of any LA _i_ , respectively. The time cost for local model training over _NR_ rounds can be derived as

$$
T_{\mathrm{LA}}^{\mathrm{cmp}} = \max_{i \in [M]} \left( \sum_{t=0}^{N_R - 1} \frac{c_r D_i(t)}{c_i} \right), \tag{10}
$$

and the corresponding energy cost can be derived as

$$
E_{\mathrm{LA}}^{\mathrm{cmp}} = \sum_{i=1}^{M} \sum_{t=0}^{N_R - 1} \kappa_i c_0 D_i(t) c_i^2, \tag{11}
$$

where _κi_ is the capacitance coefficient depending on the chip architecture and _c_ 0 captures the number of floating operations required to train or compute each sample for _NE_ . Similarly, for global aggregation, the total time and energy costs can be respectively approximated as

$$
\begin{aligned}
T_{\mathrm{agg}}^{\mathrm{cmp}} &= \sum_{t=0}^{N_R - 1} \left( \frac{c_{agg} \sum_{i=1}^{M} |\omega_{M+1,i}(t)|}{c_{GA}} \right), \\
E_{\mathrm{agg}}^{\mathrm{cmp}} &= \sum_{t=0}^{N_R - 1} \kappa_{GA} c_0 \left( \sum_{i=1}^{M} |\omega_{M+1,i}(t)| \right) c_{GA}^2,
\end{aligned} \tag{12}
$$

where _c_ agg is the number of CPUs required to aggregate one unit of data and _cGA_ is the CPU cycle frequency of the GA.

During each round, each LA perturbs its shared model parameters through the DP technique. If we assumed Renyi DP [12], then the injected noise _σi_ to achieve ( _ϵ, δ_ ) _−_ DP guarantee for each LA after _NR_ -round training can be computed as

$$
\sigma_i = \left( \frac{14 \alpha \eta^2 N_E N_R}{|L_B| D_i \{\epsilon - \log\left(\frac{1}{\delta}\right) / (\alpha - 1)\}} \right)^{\frac{1}{2}}, \tag{13}
$$

where _|LB|_ is the size of the local mini-batch and _α_ = ([2 log(1 _/δ_ )] _/ϵ_ ) + 1 given that

$$
\alpha - 1 \leq \left[\frac{2\alpha_i^2}{3}\right] \log\left(\frac{1}{\alpha |L_B| / D_i (1 + \delta^2)}\right). \tag{14}
$$

From (13), it is clear that _σi_ depends on _ϵ_ , while _ϵ_ is inversely proportional to privacy protection. The strictest privacy is achieved when _ϵ_ = 0. Under this, it is impossible to differentiate any two locally trained models. Let the privacy cost be defined as the economical loss due to the potential privacy leakage which can be formulated as

$$
\psi = \frac{1}{\epsilon_{\max}} \sum_{i=1}^{M} \sum_{t=0}^{N_R - 1} \epsilon_i v_i |\omega_{M+1,i}(t)|, \tag{15}
$$

where _vi_ represents this economical loss per unit shared model from privacy leakage.

_B. Communication and validation model_

During FML, each LA offloads its shared model to the GA at the end of every round for aggregation. The total offloading time cost then can be calculated as

$$
T_{\mathrm{LA}}^{\mathrm{off}} = \sum_{t=0}^{N_R - 1} \max_{i \in [M]} \left( \frac{|\omega_{M+1,i}(t)|}{r_i(t)} \right), \tag{16}
$$

where _ri_ is the data rate between any LA _i_ and the GA, and can be obtained during round _t_ as

$$
r_i(t) = B_0 \log_2 \left( 1 + \frac{h_{i,\mathrm{GA}}(t) P_i(t)}{N} \right). \tag{17}
$$

The parameter _N_ is the thermal noise signal power, _B_ 0 is the bandwidth, _Pi_ depicts the offloading power of any LA _i_ and _hi,_ GA is the channel gain between any LA _i_ and the GA. From the GA to all LAs, the transmission time is assumed to be negligible due to ample resources available in the GA [9]. Hence, the focus is only on offloading. Similarly, the total energy cost during offloading of shared model parameters is given as

$$
E_{\mathrm{LA}}^{\mathrm{off}} = \sum_{i=1}^{M} \sum_{t=0}^{N_R - 1} t_i(t) \frac{N}{h_{i,\mathrm{GA}}(t) P_i(t)} \left[ \exp\left( \frac{r_i(t)}{B_0} - 1 \right) \right], \tag{18}
$$

where _ti_ is the time allocated to each LA.

After $N_R$-round training, any learned model $f_i(\omega_i)$ will be further validated by the group of validators following the PoMQ consensus protocol to determine whether the received model satisfies the pre-defined requirements. Given that the total communication cost, total training cost and total privacy cost incurred during the training of such a learned model, as received from the GA, are given as $C_{\mathrm{tot}}^{\mathrm{off}}$, $C_{\mathrm{tot}}^{\mathrm{cmp}}$ and $C_{\mathrm{tot}}^{\mathrm{pvy}}$ respectively. Then each validator $m_j \in [V]$ rates such a learned model $f_i(\omega_i)$ as

$$
R_{m_j}(i) = \begin{cases}
1 & \text{if } C_{\mathrm{tot}}^{\mathrm{off}}(i) \geq \theta_{\mathrm{off}},\ C_{\mathrm{tot}}^{\mathrm{cmp}}(i) \geq \theta_{\mathrm{cmp}}, \text{ and} \\
 & C_{\mathrm{tot}}^{\mathrm{pvy}}(i) \geq \theta_{\mathrm{pvy}} \\
0 & \text{otherwise,}
\end{cases} \tag{19}
$$

where the thresholds of offloading, computation and privacy costs are respectively given as _θ_ off, _θ_ cmp and _θ_ pvy. A learned model will be ultimately applied to the corresponding VT if

$$
2 \sum_{m_j=1}^{V} R_{m_j}(i) > V. \tag{20}
$$

To estimate the validation cost, we consider the transmission of the final learned model to the virtual environment for the validation, the computation process at each validator and the decision exchange among validators after validation. The total validation time cost of any model _fi_ ( _ωi_ ) is given as

$$
T_{\mathrm{val}}(i) = \frac{|\omega_{f,i}|}{r_i} + \max_{m_j \in [V]} \left\{ \frac{c_v |R_{m_j}(i)|}{c_{m_i}} + \frac{|R_{m_j}(i)|}{r_v} \right\}, \tag{21}
$$

where _|ωf,i|_ is the size of the final model _fi_ ( _ωi_ ) after _NR_ communication rounds, _cv_ is the number of CPUs required to validate one sample of the final learned model, _cmi_ is the validation capacity, _|Rmj_ ( _i_ ) _|_ is the size of the decision message and _rv_ is the data rate among validators, assumed to be constant owing to the pre-defined communication subchannels among validators. Similarly, the energy cost can be obtained as

$$
\begin{aligned}
E_{\mathrm{val}} ={}& \frac{N}{P_i h_{i,\mathrm{val}}} \left[ \exp\left( \frac{r_i}{B_0} - 1 \right) \right] + \\
& \sum_{m_j=1}^{V} \left\{ \frac{N}{P_j h_{j,k}} \left[ \exp\left( \frac{r_v}{B_0} - 1 \right) \right] + \kappa_v c_0 |R_{m_j}(i)| c_{m_i}^2 \right\}.
\end{aligned} \tag{22}
$$

### C. Connectivity cost

Connectivity cost captures the cost of updating the VT model every time an update is scheduled. It captures the cost of maintaining secure and reliable synchronizations between any PT and its counterpart VT. Since _M_ LAs participate in a model update, the connectivity cost includes the cost of FML at each participating node, the validation cost, the privacy cost as well as communication cost. Given any typical physicalvirtual twin pair, the overall time cost to complete a single status update can be obtained as

$$
\begin{aligned}
C_{\mathrm{time}} ={}& \sum_{t=0}^{N_R - 1} \left\{ \left( \frac{c_{agg} \sum_{i=1}^{M} |\omega_{M+1,i}(t)|}{c_{GA}} \right) + \right. \\
& \left. \max_{i \in [M]} \left( \frac{|\omega_{M+1,i}|}{r_i} + \frac{c_r D_i(t)}{c_i} \right) \right\} + \left( \frac{|\omega_{f,i}|}{r_i} + \right. \\
& \left. \max_{m_j \in [V]} \left\{ \frac{c_v |R_{m_j}(i)|}{c_{m_i}} + \frac{|R_{m_j}(i)|}{r_v} \right\} \right).
\end{aligned} \tag{23}
$$

Similarly, the overall energy cost to ensure synchronization of any single model update is obtained as

$$
\begin{aligned}
C_{\mathrm{ene}} ={}& \sum_{t=0}^{N_R - 1} \Bigl\{ \kappa_{GA} c_0 \left( \sum_{i=1}^{M} |\omega_{M+1,i}(t)| c_{GA}^2 \right) + \\
& \sum_{i=1}^{M} \left( \kappa_i c_0 D_i(t) c_i^2 + t_i(t) \frac{N}{h_{i,\mathrm{GA}}(t) P_i(t)} \left[ \exp\left( \frac{r_i(t)}{B_0} - 1 \right) \right] \right) \Bigr\} \\
& + \frac{N}{P_i h_{i,\mathrm{val}}} \left[ \exp\left( \frac{r_i}{B_0} - 1 \right) \right] + \\
& \sum_{m_j=1}^{V} \left\{ \frac{N}{P_j h_{j,k}} \left[ \exp\left( \frac{r_v}{B_0} - 1 \right) \right] + \kappa_v c_0 |R_{m_j}(i)| c_{m_i}^2 \right\}.
\end{aligned} \tag{24}
$$

Generally, the connectivity cost depends on the scheduling rate $o_i$. Given that $\mathcal{U}$ is the number of status updates that have been scheduled over a known time interval, its probability mass function can be expressed as

$$
P(\mathcal{U} | o_i) = \frac{\exp(-o_i) o_i^{\mathcal{U}}}{\mathcal{U}!}, \forall \mathcal{U} \in \mathbb{N}. \tag{25}
$$

*Proposition 1:* The long-term average connectivity cost per any arbitrary VT model update can be obtained as

$$
C_{\mathrm{conn}} = \lim_{\mathcal{U} \to \infty} \frac{1}{\mathcal{U}} \sum_{u=1}^{\mathcal{U}} \left( \frac{1}{\epsilon_{\max}} \sum_{i=1}^{M} \sum_{t=0}^{N_R - 1} \epsilon_i v_i |\omega_{M+1,i}^{u}(t)| + C_{\mathrm{time}}^{u} + C_{\mathrm{ene}}^{u} \right). \tag{26}
$$

*Proof:* The proof follows from (23) and (24). $\blacksquare$

### D. Synchronization accuracy

It is essential to investigate the synchronization accuracy. Unfortunately, such a metric is very difficult to define since it captures the degree of similarity between any PT and its counterpart VT at any time. If we consider that any final model after the validation process could capture the true corresponding update in the physical environment, then we may evaluate synchronization accuracy as a function of the synchronization time [30] and the FML loss. That is, lower synchronization time and FML loss depict higher synchronization accuracy. For this purpose, we define a new term called synchronization gap, which is the time since the last status update was generated in the physical environment. With this, the synchronization gap, at any known FML loss, is inversely proportional to accuracy.

To obtain the synchronization gap, we first consider each generated status update $u$ to intuitively pass through the FML learning and validation process following the first-come-first-serve (FCFS) approach. We further assume that this status update generation is the same as the status update arrival while the arrival and the service time (i.e., the time from arrival till model evolution or updating) follow random processes. The service time of any status depicts the time at which the VT is successfully updated using such a status update. Given that the inter-arrival time of status updates $X_{(u)}$ from any tagged LA is an independent and identically distributed (i.i.d.) exponential random variable with $E[X] = \frac{1}{o_i}$ [31]. Let $\varpi_k$ represents the times at which status is received at the tagged VT for its update, then at any time $t$, the index and the timestamp of the most recently received status are respectively given as

$$
\begin{aligned}
\mathcal{J}(t) &= \max\{k \mid \varpi_k \leq t\}, \\
u(t) &= \varpi_{\mathcal{J}(t)}.
\end{aligned} \tag{27}
$$

The synchronization gap at time _t_ can then be expressed as

$$
S_{\mathrm{gap}}(t) = t - u(t), \forall t \geq 0. \tag{28}
$$

In the absence of newly received model updates, the synchronization gap increases linearly with time and is reduced to a smaller value when a new model update is received. For any update _u_ , the processing time of any generated status update can be obtained as

$$
P_{\mathrm{time}}^{(u)} = W_{\mathrm{time}}^{(u)} + C_{\mathrm{time}}^{(u)}, \tag{29}
$$

where $W_{\mathrm{time}}^{(u)}$ is the waiting time for any status update $u$ and $C_{\mathrm{time}}^{(u)}$ is the service time of $u$ following (23). Obviously, $W_{\mathrm{time}}^{(u)} = 0$ if any status update $u$ is generated when the VT is already updated with previously generated status $u - 1$. However, if $u$ is generated when $u - 1$ is still in the system (i.e., $u - 1$ has not triggered an update of the VT), $W_{\mathrm{time}}^{(u)} = (P_{\mathrm{time}}^{(u-1)} - X_{(u)})^{+}$ captures the average waiting time. For explanation purpose, we assumed that $o_i$ follows the Poisson point process, while the service times of the rate $\varrho_i$ are similarly i.i.d. exponentials with average $C_{\mathrm{time}}^{(u)}$, then the average synchronization gap is provided in Proposition 2.

*Proposition 2:* The average synchronization gap when the status arrival rate is Poisson while the service times are i.i.d. exponentials can be calculated as

$$
S_{\mathrm{gap}}^{\mathrm{fc}} = C_{\mathrm{time}}^{(u)} \left\{ \frac{o_i C_{\mathrm{time}}^{(u)} (1 - o_i C_{\mathrm{time}}^{(u)}) + (1 - o_i C_{\mathrm{time}}^{(u)})}{o_i C_{\mathrm{time}}^{(u)} (1 - o_i C_{\mathrm{time}}^{(u)})} + \frac{(o_i C_{\mathrm{time}}^{(u)})^3}{o_i C_{\mathrm{time}}^{(u)} (1 - o_i C_{\mathrm{time}}^{(u)})} \right\}. \tag{30}
$$

_Proof:_ The proof follows from the probability density function of the system with Poisson process arrival rate and exponential service times given as

$$
\mathcal{D}_{\mathrm{fc}}(t) = \varrho_i \left(1 - \frac{o_i}{\varrho_i}\right) \exp\left( -\varrho_i \left[1 - \frac{o_i}{\varrho_i}\right] t \right). \; \blacksquare \tag{31}
$$

Note that (30) follows from a single-server FCFS queue with an infinite buffer size. Such a scheme, though simple, may not be suitable in the HDT system, where the VT is expected to capture the latest update in the counterpart PT. Instead of processing an old status, we can discard it and simply process the latest status. Following this and to obtain a low synchronization gap, we introduced a non-preemptive singleserver last-come-first-serve (LCFS) queue with a buffer of size 2 and queue displacement policy, where the system at any time can only consist of a maximum of two status updates – one currently under processing and the other on the queue. On the arrival of another status update, the newly arrived status displaces the status waiting on the queue as shown in Fig. 3.

Let the arrival and service follow Poisson and general distributions, respectively. We applied the classical embedding technique under the assumption that the queue system is stationary and sampled at certain epochs, such that service completion (i.e., the successful updates of a VT) has a Markovian property. With that, the synchronization gap can have the same distribution for all $t$ while the distribution of any $C_{\mathrm{time}}^{(u)}$ of rate $\varrho_i$ is given as $g$ with

$$
g(x) = \mathbb{P}\left(C_{\mathrm{time}}^{(u)} \leq x\right). \tag{32}
$$

_Proposition 3:_ If _C_ time is i.i.d. exponential in steady-state, the density of _S_ gap at any time _t_ can be obtained under a nonpreemptive single-server LCFS queue system with buffer size 2 and queue displacement as

$$
\begin{aligned}
\mathcal{D}_{S_{\mathrm{gap}}}^{\mathrm{lcfs}}(t) ={}& \frac{o_i[(\rho + 2)(\rho - 1)]t - \rho^2 + \rho + 3}{\rho^3 - 1} \exp(-\varrho_i t) \\
& + \frac{o_i(\rho + 1)t + \rho(\rho + 3) + 3}{\rho(\rho + 1) + 1} \exp(-\varrho_i [\rho + 1] t) \\
& - \frac{\rho}{\rho - 1} \exp(-o_i t),
\end{aligned} \tag{33}
$$

where $\rho = \frac{o_i}{\varrho_i}$ depicts the traffic intensity. *Proof:* The proof can be obtained by inverting the Laplace transform of $S_{\mathrm{gap}}(t)$ at any time $t = 0$, given as [32], [33]

$$
\begin{aligned}
\mathbb{E}\left[e^{-s S_{\mathrm{gap}}(0)}\right] ={}& \frac{\varrho_i}{\varrho_i + s} \left( \frac{2\varrho_i o_i + \varrho_i^2 + o_i^2 + \varrho_i s}{(\varrho_i + o_i)(o_i + \varrho_i + s)} \right) \left\{ \left( \frac{o_i}{s + o_i} \right) \right. \\
& \left( \frac{\varrho_i^2}{o_i^2 + o_i \varrho_i + \varrho_i^2} \right) \left( \frac{o_i + \varrho_i}{\varrho_i + o_i + s} \right) + \left( \frac{\varrho_i}{\varrho_i + s} \right) \left. \frac{o_i^2 + \varrho_i o_i}{o_i^2 + \varrho_i o_i + \varrho_i^2} \right\},
\end{aligned} \tag{34}
$$

where for _oi_ = _ϱi_ = 1,

Figure 3. A 2 buffer size non-preemptive single-server LCFS queue with queue displacement policy.

$$
\mathcal{D}_{S_{\mathrm{gap}}}^{\mathrm{lcfs}}(t) = \frac{1}{3}\left[(2t + 7)\exp(-2t) + (6t - 7)\exp(-t)\right], \tag{35}
$$

and $\lim_{o_i \to \infty} \mathcal{D}_{S_{\mathrm{gap}}}^{\mathrm{lcfs}}(t) = t\exp(-t)$. The synchronization gap in such a case can be expressed as

$$
S_{\mathrm{gap}}^{\mathrm{lcfs}} = \frac{o_i^4(2o_i + 7\varrho_i) + o_i^2 \varrho_i^2 (8o_i + 7\varrho_i) + \varrho_i^4 (4o_i + \varrho_i)}{o_i \varrho_i (o_i + \varrho_i)^2 (o_i^2 + \varrho_i o_i + \varrho_i^2)}. \tag{36}
$$

V. PROBLEM FORMULATION AND OPTIMIZATION

Asides from the synchronization gap, it is also important to reduce the occurrence of loss during the FML. This is expected to improve the synchronization accuracy at any time by simultaneously minimizing the two functions following

$$
\begin{aligned}
& \min_{o_i, V, M} \left( w_1 S_{\mathrm{gap}} + \frac{w_2}{D_i} \sum_{j=1}^{D_i} \ell(x_{i,j}, y_{i,j}, \omega_i, \omega_{M+1}) \right), \\
& \text{s.t. } o_i \in [0, 1], \\
& \phantom{\text{s.t. }} w_1 + w_2 = 1, \forall w_2 \gg w_1, \\
& \phantom{\text{s.t. }} \sum_{i \in [M]} i \leq M, \\
& \phantom{\text{s.t. }} \sum_{j}^{V} m_j \leq V.
\end{aligned} \tag{37}
$$

A simultaneous minimization of the synchronization gap and loss in (37) is not straightforward since the synchronization gap depends on not only the overall time cost, but also the FML. We can thus leverage the overall time cost to further reduce the synchronization gap in (36).

From (37), we know that an increase in the number of rounds _NR_ can improve the training accuracy at the expense of connectivity cost, while an increase in the privacy protection level (i.e., a lower _ϵ_ ) improves privacy, but decreases the accuracy. Moreover, if we increase the computation overhead (by increasing the added noise), we can have higher privacy but lower connectivity cost. That means a trade-off exists between accuracy and connectivity cost, accuracy and privacy, and connectivity cost and privacy, as shown in Fig. 4. In this section, we attempt to minimize the connectivity cost of the proposed DPFML-enabled HDT framework without compromising accuracy and privacy.

### A. Problem formulation

We aim to find the balance between synchronization accuracy, privacy cost and connectivity cost. The objective function can be formulated as

$$
O = \Theta_1 (C_{\mathrm{time}} + C_{\mathrm{ene}} + f_i(\omega_i, \omega_{M+1})) - (1 - \Theta_1) \Theta_2 \psi_{\mathrm{cost}}, \tag{38}
$$

where Θ1(0 _<_ Θ1 _<_ 1) represents the weight factor necessary to combine two objective functions and Θ2 captures the mapping factor to ensure that the two objectives functions are at the same scale. Note that to maximize the synchronization accuracy, we simply minimize the FML loss in (38), and take (36) as a baseline synchronization gap which can be further reduced through the time cost _C_ time. That is, given (36), the gap can be further reduced by minimizing _C_ time. Thus, the optimization problem is obtained as

$$
\begin{aligned}
& \min_{o_i, V, M, \epsilon, N_R} \left[ \Theta_1 (C_{\mathrm{time}} + C_{\mathrm{ene}} + f_i(\omega_i, \omega_{M+1})) - (1 - \Theta_1) \Theta_2 \psi_{\mathrm{cost}} \right], \\
& \text{s.t. } o_i \in [0, 1], \\
& \phantom{\text{s.t. }} \sum_{i \in [M]} i \leq M, \\
& \phantom{\text{s.t. }} \sum_{j}^{V} m_j \leq V, \\
& \phantom{\text{s.t. }} \epsilon_{\min} \leq \epsilon \leq \epsilon_{\max}, \\
& \phantom{\text{s.t. }} c_i^{\min} \leq c_i \leq c_i^{\max}, \forall i \in [M], \\
& \phantom{\text{s.t. }} c_{m_j}^{\min} \leq c_{m_j} \leq c_{m_j}^{\max}, \forall m_j \in [V],
\end{aligned} \tag{39}
$$

where $c_i^{\min}$ and $c_i^{\max}$ represent the minimum and maximum computation capacity of each LA respectively, while $c_{m_j}^{\min}$ and $c_{m_j}^{\max}$ are the minimum and maximum validation capacities of each validator respectively. Obviously, problem (39) is a nonconvex optimization problem and thus its solution is difficult to obtain in close form. In what follows, we transform the original problem into an MDP problem and provide solutions using the DRL algorithm.

### B. MDP problem and solution

We defined the tuple $(\mathcal{S}^{(t)}, \mathcal{A}^{(t)}, \mathcal{R}^{(t)})$, where $\mathcal{S}^{(t)}$, $\mathcal{A}^{(t)}$ and $\mathcal{R}^{(t)}$ are the state space, action space and reward, respectively, at each round $t$. In the proposed framework, the agent is the typical LA that aims to update its counterpart VT by collaborating with related LAs during the FML. Thus, the state space includes the achievable data rate $r$, the computation capacity $c$, the validation capacity $c_m$, the learned parameter $\omega(t)$ and the global loss value function $f(\omega_{M+1})$. The state space is given as

$$
\mathcal{S}^{(t)} = \{r(t), c(t), c_m(t), f(\omega_{M+1}(t))\}. \tag{40}
$$

Similarly, the action space includes the scheduling rate $o$, the number of validators $V$, the number of LAs $M$, the privacy budget $\epsilon$ and the number of rounds $N_R$. The action space is given as

$$
\mathcal{A}^{(t)} = \{o(t), V(t), M(t), \epsilon(t), N_R(t)\}, \tag{41}
$$

Figure 4. Trade-offs among important system parameters.

while the reward function is given as

$$
\mathcal{R}^{(t)} = -O(t), \tag{42}
$$

if all constraints in (39) are satisfied and zero if otherwise. Given that $\gamma \in [0, 1]$ is the discount factor, each agent aims to maximize the cumulative reward

$$
\mathbb{E}\left[ \sum_{t=0}^{N_R - 1} \gamma \mathcal{R}(\mathcal{S}^{(t)}, \mathcal{A}^{(t)}) \right]. \tag{43}
$$

### C. DRL solution using DDPG

To solve the MDP problem, we adopted the DDPG algorithm [34] owing to its ability to achieve improved performance, for continuous action space, compared to other algorithms. While Q-learning algorithms and their variants are suitable for low-dimensional, discrete state and action spaces, most of these algorithms do not easily converge to optimal behaviour. In addition, such models are susceptible to the curse of dimensionality when too many decision variables are involved [35]. The Deep Q network algorithm can handle problems in high-dimensional continuous state space, albeit under a discrete action space. DDPG algorithm generally relies on deep neural networks to create two approximation functions of the actor-critic algorithm. The actor network is described as a policy function $\mu(\mathcal{S}|\theta^{\mu})$ with parameter $\theta^{\mu}$ while the critic network is described as an action-value function $\mathcal{O}(\mathcal{S}, \mathcal{A}|\theta^{\mathcal{O}})$ with parameter $\theta^{\mathcal{O}}$.

Define the Bellman equation as

$$
\mathcal{O}^{\mu}(\mathcal{S}_t, \mathcal{A}_t) = \mathbb{E}\left[\mathcal{R}_t + \gamma \mathcal{O}^{\mu}(\mathcal{S}_{t+1}, \mu(\mathcal{S}_{t+1}))\right], \tag{44}
$$

where the loss of $\mathcal{O}(\mathcal{S}, \mathcal{A}|\theta^{\mathcal{O}})$ can be obtained, if $\mu'$ represents the target actor network, as

$$
\begin{aligned}
L(\theta^{\mathcal{O}}) ={}& \mathbb{E}_{\mu'}\left[\left(\mathcal{O}^{\mu}(\mathcal{S}_t, \mathcal{A}_t|\theta^{\mathcal{O}}) - \{\mathcal{R}_t + \right.\right. \\
& \left.\left. \gamma \mathcal{O}(\mathcal{S}_{t+1}, \mu(\mathcal{S}_{t+1})|\theta^{\mathcal{O}})\}\right)^2\right].
\end{aligned} \tag{45}
$$

To update the policy function _µ_ ( _S|θ_<sup>_µ_</sup> ), the chain rule is applied to the Bellman equation from the start distribution _J_ [34] based on the actor parameters

$$
\begin{aligned}
\nabla_{\theta^{\mu}} J \approx{}& \mathbb{E}_{\mu'}\left[\nabla_{\theta^{\mu}} \mathcal{O}(\mathcal{S}, \mathcal{A}|\theta^{\mathcal{O}})|_{\mathcal{S}=\mathcal{S}_t, \mathcal{A}=\mu(\mathcal{S}_t|\theta^{\mu})}\right] \\
={}& \mathbb{E}_{\mu'}\left[\nabla_{\mathcal{A}} \mathcal{O}(\mathcal{S}, \mathcal{A}|\theta^{\mathcal{O}})|_{\mathcal{S}=\mathcal{S}_t, \mathcal{A}=\mu(\mathcal{S}_t)} \; \nabla_{\theta^{\mu}} \mu(\mathcal{S}|\theta^{\mu})|_{\mathcal{S}=\mathcal{S}_t}\right].
\end{aligned} \tag{46}
$$

Figure 5. Structure of the DDPG.

To minimize loss, the parameter _▽θOL_ is estimated using the algorithmic differentiation technique [36], such that the actionvalue function _O_ ( _S, A|θ_<sup>_O_</sup> ) parameters are updated using the gradient descent as

$$
\theta^{\mathcal{O}} \leftarrow \theta^{\mathcal{O}} - \eta_{\mathrm{rate}}^{\mathrm{critic}} \nabla_{\theta^{\mathcal{O}}} L, \tag{47}
$$

given that $\eta_{\mathrm{rate}}^{\mathrm{critic}}$ is the learning rate of the critic network. In addition, the algorithmic differentiation technique is also adopted to obtain gradients $\nabla_{\mathcal{A}} \mathcal{O}(\mathcal{S}, \mathcal{A}|\theta^{\mathcal{O}})|_{\mathcal{S}=\mathcal{S}_t, \mathcal{A}=\mu(\mathcal{S}_t)}$ and $\nabla_{\theta^{\mu}} \mu(\mathcal{S}|\theta^{\mu})|_{\mathcal{S}=\mathcal{S}_t}$, such that

$$
\begin{aligned}
\nabla_{\theta^{\mu}} J \approx{}& \frac{1}{N_{\mathrm{batch}}} \sum_j \left[\nabla_{\mathcal{A}} \mathcal{O}(\mathcal{S}, \mathcal{A}|\theta^{\mathcal{O}})|_{\mathcal{S}=\mathcal{S}_t, \mathcal{A}=\mu(\mathcal{S}_t)} \right. \\
& \left. \nabla_{\theta^{\mu}} \mu(\mathcal{S}|\theta^{\mu})|_{\mathcal{S}=\mathcal{S}_t}\right],
\end{aligned} \tag{48}
$$

where _N_ batch is the mini-batch size selected by the agent during the learning process. Similarly,

$$
\theta^{\mu} \leftarrow \theta^{\mu} - \eta_{\mathrm{rate}}^{\mathrm{actor}} \nabla_{\theta^{\mathcal{O}}} J, \tag{49}
$$

where $\eta_{\mathrm{rate}}^{\mathrm{actor}}$ is the learning rate of the actor network. With these, the target critic and actor networks can be respectively obtained using the update rate $\tau^{\mathrm{rate}} \ll 1$ as

$$
\begin{aligned}
\theta^{\mathcal{O}'} &\leftarrow \tau^{\mathrm{rate}} \theta^{\mathcal{O}} + (1 - \tau^{\mathrm{rate}}) \theta^{\mathcal{O}'}, \\
\theta^{\mu'} &\leftarrow \tau^{\mathrm{rate}} \theta^{\mu} + (1 - \tau^{\mathrm{rate}}) \theta^{\mu'}.
\end{aligned} \tag{50}
$$

This work used multiple DDPG agents to simulate the proposed framework. Its general structure is shown in Fig. 5. The details of the simulation and results are provided in the Section VI.

## VI. NUMERICAL RESULTS

We first implemented the proposed DPFML framework by adopting TensorFlow and LEAF library [37] – an open-source library that provides the benchmark for federated learning. Since HDT data are expected to be non-iid, we used the CelebA datasets available in the LEAF library. To minimize the required connectivity cost in the proposed framework, we incorporated the DDPG algorithm into the DPFML framework. We compared the proposed framework with three other baseline frameworks: the conventional federated averaging (FeDAvg), the FeDAvg with DP (DPFedAvg) and the DPFML

Table II

PARAMETERS USED FOR SIMULATION with standard validation method (vDPFML). The vDPFML is simply an implementation of the proposed framework with a standard blockchain consensus algorithm instead of the proposed PoMQ consensus mechanism.

|Parameter|Value|
|---|---|
|$M$, $V$|$[1, 22]$|
|$D_i$|$[1, 5]$ MB|
|$c_r$, $c_v$|1 GHz|
|$c_i$|$[2, 3.5]$ GHz|
|$N_R$|$[10, 50]$|
|$\kappa_i$, $\kappa_{GA}$; $\kappa_v$|$10^{-27}$|
|$c_{agg}$|1 GHz|
|$c_{GA}$|20 GHz|
|$v_i$|$[0.01, 0.012, 0.014, 0.016]$|
|$\epsilon_{\max}$|50|
|$B_0$|1 MHz|
|$\lvert R_{m_j} \rvert$|10 MB|
|$c_{m_i}$|$[5, 12.5]$ GHz|
|$r_v$|2|
|$\eta_{\mathrm{rate}}^{\mathrm{critic}}$|0.001|
|$\eta_{\mathrm{rate}}^{\mathrm{actor}}$|0.0005|
|$N_{batch}$|10|
|$\gamma$|0.99|
|$\tau^{\mathrm{rate}}$|0.05|

We carried out several experiments and simulations to demonstrate the performance of the proposed framework. Except otherwise stated, the parameters used for simulations are presented in Table II. These parameters were selected based on similar works [3], [8], [9]. We set the sizes of the hidden layers in Fig. 5 as follows: _D_ 1 = 128, _D_ 2 = 32, _S_ 1 = 64, _S_ 2 = 32, _A_ 1 = 32, and _C_ 1 = 16.

In Fig. 6, we demonstrate the ability of the proposed DPFML scheme to reach convergence faster than other schemes. The highest loss is observed in the DPFedAvg scheme due to the incorporation of the privacy budget (as in the proposed DPFML and vDPFML schemes), through the addition of the Gaussian noise. The DPFML scheme achieved the least loss as _NR_ increases which justifies the suitability of the proposed scheme to perform efficiently in the presence of non-iid data. Although the FeDAvg has been demonstrated to perform well when iid datasets are used, we claim that data is HDT systems are expected to be non-iid. Thus, such a framework may not be suitable.

A similar result is observed in Fig. 7, where the loss is obtained as _ϵ_ increases. At a lower _ϵ_ , the loss is higher since a large amount of noise is added. As _ϵ_ increases, the loss is observed to reduce although remains constant for DPFeDAVg as _ϵ_ increases beyond 35. In addition, the standard FeDAvg remains fixed since privacy is not considered, thus the privacy budget was set to the maximum under such a case, i.e., _ϵ_ = _ϵ_ max, while the DPFML scheme showed improved performance compared to the other schemes. The proposed scheme ensures better performance without compromising privacy.

Next, we investigate the performance of the DPFML framework using accuracy as a metric. While the accuracy in

Figure 6. Performance in terms of the learning loss with respect to _NR_ .

Figure 7. Performance in terms of the learning loss with respect to _ϵ_ .

FeDAvg increases with _NR_ as shown in Fig. 8, the DPFedAvg continues to produce an accuracy closer to zero even as _NR_ increases. Conversely, the DPFML achieved the best accuracy within the first 100 rounds and remain almost constant afterwards. This confirms the ability of the DPFML framework to reach convergence with a limited number of communication rounds. Likewise, the proposed DPFML scheme produces an improved performance compared to the FeDAvg as _ϵ_ increases. This is depicted in Fig. 9. Although the standard FeDAvg produced a better accuracy when _ϵ_ is closer to zero, this is unsurprising since such an approach provides no privacy. With DPFeDAvg, the accuracy was observed to be very low. This further confirms that FeDAvg is unsuitable for HDT frameworks where privacy is an important constraint since such an approach underestimates privacy.

To compare the performance in terms of the average connectivity cost, we investigate the long-term average connectivity cost ( _U_ = 100) as a function of _ci_ . As presented in Fig. 10, the long-term average connectivity cost decreases as _ci_ increases in all cases since an improved computation capacity can reduce latency significantly thereby reducing the time cost. However, the DPFML scheme requires the lowest cost while the FeDAvG and DPFeDAvg require more cost to ensure the timely synchronization of any PT-VT pair. A similar result is obtained when long-term average connectivity cost was investigated as _cmi_ increases in Fig. 11, confirming that the standard validation process in blockchain may not be suitable in HDT systems because they require more time and energy to validate every transaction. In Fig. 12, we also confirmed that the connectivity cost indeed increases with _ϵ_ . Interestingly, the cost is highest when no privacy or less privacy constraint is implemented reflecting the level of potential threats.

Figure 8. Performance in terms of the learning accuracy with respect to _NR_ .

Figure 9. Performance in terms of the learning accuracy with respect to _ϵ_ .

Figure 10. Performance in terms of the average connectivity cost.

We note that the time cost in the DPFeDAvg is slightly higher than the conventional FeDAvg since the introduction of noise means more communication round is required to reach convergence than in its standard version. As shown in Fig. 13, the time cost increases with the _V_ since more cost is incurred to reach consensus as _V_ increases. With a minimum time cost for the DPFML, the synchronization gap is further reduced between any PT-VT pair. Interestingly, the energy cost increases in Fig. 14 as _ci_ increases since the agents have learnt the optimal parameters to ensure reduced cost and an increase in capacity can only increase the energy cost but cannot improve significantly the overall performance.

Figure 11. _C_ conn vs _cmi_ .

Figure 12. _C_ conn vs _ϵ_ .

### VII. CONCLUSION

HDT is a new technology that can transform many aspects of our current environment. To realize any HDT system, there must be reliable connectivity between any PT-VT pair to ensure timely synchronization between them. In this paper, we investigate the connectivity problem in the HDT framework and proposed the DPFML technique to achieve connectivity between any PT-VT pair. This is necessary since connectivity costs must be reduced to ensure timely synchronization without compromising privacy. To further reduce cost, we proposed a new consensus protocol, called the PoMQ, and formulated the connectivity problem as an MDP problem to allow optimization through the DDPG algorithm. We compared the proposed solution with the existing ones and conclude that the proposed scheme is suitable for HDT systems where datasets are expected to be non-iid while privacy and security are also essential parameters.

Figure 13. Performance in terms of the time cost.

Figure 14. Performance in terms of the energy cost.

### REFERENCES

- [1] L. U. Khan, W. Saad, D. Niyato, Z. Han, and C. S. Hong, “Digital-twinenabled 6G: Vision, architectural trends, and future directions,” _IEEE Communications Magazine_ , vol. 60, no. 1, pp. 74–80, Feb. 2022.

- [2] S. D. Okegbile, J. Cai, C. Yi, and D. Niyato, “Human Digital Twin for Personalized Healthcare: Vision, Architecture and Future Directions,” _IEEE Network_ , July 2022., DOI: 10.1109/MNET.118.2200071.

- [3] S. D. Okegbile, and J. Cai, “Edge-assisted human-to-virtual twin connectivity scheme for human digital twin frameworks,” _in IEEE VTC Conference_ , Helsinki, Jun. 2022, pp. 1–6.

- [4] B. Schleich, N. Anwer, L. Mathieu, and S. Wartzack, “Shaping the digital twin for design and production engineering,” _CIRP annals_ , vol. 66, no. 1, pp. 141–144, Jan. 2017.

- [5] X. Zhou, X. Xu, W. Liang, Z. Zeng, S. Shimizu, L. T. Yang, and Q. Jin, “Intelligent small object detection for digital twin in smart manufacturing with industrial cyber-physical systems,” _IEEE Transactions on Industrial Informatics,_ vol. 18, no. 2, pp. 1377–1386, Feb. 2021.

- [6] Y. Wu, K. Zhang, and Y. Zhang, “Digital twin networks: A survey,” _IEEE Internet of Things Journal_ , vol. 8, no. 18, pp. 13789–13804, May 2021.

- [7] Y. Lu, S. Maharjan, and Y. Zhang, “Adaptive edge association for wireless digital twin networks in 6G,” _IEEE Internet of Things Journal_ , vol. 8, no. 22, pp. 16219–16230, Jul. 2021.

- [8] Y. Lu, X. Huang, K. Zhang, S. Maharjan, and Y. Zhang, “Low-latency federated learning and blockchain for edge association in digital twin empowered 6G networks,” _IEEE Transactions on Industrial Informatics_ , vol. 17, no. 7, pp. 5098–5107, Jul. 2021.

- [9] Y. Lu, X. Huang, K. Zhang, S. Maharjan, and Y. Zhang, “Communicationefficient federated learning and permissioned blockchain for digital twin edge networks,” _IEEE Internet Things Journal_ , vol. 8, no. 4, pp. 2276– 2288, Feb. 2021.

- [10] S. D. Okegbile, J. Cai, and A. S. Alfa, “Performance analysis of blockchain-enabled data sharing scheme in cloud-edge computing-based IoT networks,” _IEEE Internet of Things Journal_ , vol. 9, no. 21, pp. 21520– 21536, Nov. 2022.

- [11] H. Wu, C. Chen, and L. Wang, “A theoretical perspective on differentially private federated multi-task learning,” Nov. 2020, arXiv:2011.07179.

- [12] M. Wu, D. Ye, J. Ding, Y. Guo, R. Yu, and M. Pan, “Incentivizing differentially private federated learning: A multidimensional contract approach,” _IEEE Internet of Things Journal_ , vol. 8, no. 13, pp. 10639– 10651, Jan. 2021.

- [13] M. E. Miller, and E. Spatz, “A unified view of a human digital twin,” _Human-Intelligent Systems Integration_ , vol. 4, pp. 23–33, Mar. 2022, DOI: https://doi.org/10.1007/s42454-022-00041-x.

- [14] Y. Liu, L. Zhang, Y. Yang, L. Zhou, L. Ren, F. Wang, R. Lui, Z. Pang, and M. Deen, “A novel cloud-based framework for the elderly healthcare services using digital twin,” _IEEE Access_ , vol. 7, pp. 49088–49101, Apr. 2019.

- [15] J. Zhang, L. Li, G. Lin, D. Fang, Y. Tai, and J. Huang, “Cyber resilience in healthcare digital twin on lung cancer,” _IEEE Access_ , vol. 8, pp. 20190011201913, Oct. 2020.

- [16] B. R. Barricelli, E. Casiraghi, J. Gliozzo, A. Petrini, and S. Valtolina, “Human digital twin for fitness management,” _IEEE Access_ , vol. 8, pp. 26637–26664, Feb. 2020.

- [17] R. Martinez-Velazquez, R. Gamez, and A. El Saddik, “Cardio Twin: A Digital Twin of the human heart running on the edge,” _in IEEE International Symposium on Medical Measurements and Applications_ , Istanbul, Jun. 2019, pp. 1–6.

- [18] A. El Saddik, H. Badawi, R. Velazquez, F. Laamarti, R. Diaz, N. Bagaria, and J. Arteaga-Falconi, “Dtwins: a digital twins ecosystem for health and well-being,” _IEEE COMSOC MMTC Commun. Front_ , vol. 14, pp. 39–43, May 2019.

- [19] W. Yang, W. Xiang, Y. Yang, and P. Cheng, “Optimizing Federated Learning with Deep Reinforcement Learning for Digital Twin Empowered Industrial IoT,” _IEEE Transactions on Industrial Informatics_ , Jul. 2022, DOI: 10.1109/TII.2022.3183465.

- [20] L. Jiang, H. Zheng, H. Tian, S. Xie, and Y. Zhang, “Cooperative federated learning and model update verification in blockchain empowered digital twin edge networks,” _IEEE Internet of Things Journal_ , vol. 9, no. 13, pp. 11154–11167, Jul. 2022.

- [21] D. Gupta, O. Kayode, S. Bhatt, M. Gupta, and A. S. Tosun, “Hierarchical federated learning based anomaly detection using digital twins for smart healthcare,” _in IEEE International Conference on Collaboration and Internet Computing_ , Atlanta, Dec. 2021, pp. 16–25.

- [22] Y. Qu, L. Gao, Y. Xiang, S. Shen, and S. Yu, “FedTwin: BlockchainEnabled Adaptive Asynchronous Federated Learning for Digital Twin Networks,” _IEEE Network_ , Jul. 2022, DOI: 10.1109/MNET.105.2100620.

- [23] T. Li, A. K. Sahu, A. Talwalkar, and V. Smith, “Federated learning: Challenges, methods, and future directions,” _IEEE Signal Processing Magazine_ , vol. 37, no. 3, pp.50–60, May 2020.

- [24] A. El Ouadrhiri, and A. Abdelhadi, “Differential privacy for deep and federated learning: A survey,” _IEEE Access_ , vol. 10, pp. 22359–22380, Feb. 2022.

- [25] Y. Lu, X Huang, Y. Dai, S. Maharjan, and Y. Zhang, “Differentially private asynchronous federated learning for mobile edge computing in urban informatics,” _IEEE Transactions on Industrial Informatics_ , vol. 16, no. 3, pp. 2134–2143, Sept. 2019.

- [26] V. Smith, C. K. Chiang, M. Sanjabi, and A. S. Talwalkar, “Federated multi-task learning,” _in Advances in neural information processing systems_ , Long Beach, CA, USA, vol. 30, 2017, pp. 1–11.

- [27] R. Caruana, “Multitask learning,” _Machine learning_ , vol. 28, no. 1 pp. 41–75, Jul. 1997.

- [28] F. Zhuang, Z. Qi, K. Duan, D. Xi, Y. Zhu, H. Zhu, H. Xiong, and Q. He, “A comprehensive survey on transfer learning,” _in Proceedings of the IEEE_ , vol. 109, no. 1, pp. 43–76, Jul. 2020.

- [29] K. M. Borgwardt, A. Gretton, M. J. Rasch, H.-P. Kriegel, B. Sch¨olkopf, and A. J. Smola, “Integrating structured biological data by kernel maximum mean discrepancy,” _Bioinformatics_ , vol. 22, no. 14, pp. 49–57, Jul. 2006.

- [30] J. C. Eidson, and K. B. Stanton, “Timing in cyber-physical systems: The last inch problem,” _in IEEE International Symposium on Precision Clock Synchronization for Measurement, Control, and Communication_ , Beijing, Oct. 2015, pp. 19–24.

- [31] S. Kaul, R. Yates, and M. Gruteser, “Real-time status: How often should one update?,” _in IEEE Proceedings IEEE INFOCOM_ , Mar. 2012, pp. 2731–2735.

- [32] G. Kesidis, T. Konstantopoulos, and M. A. Zazanis, “Age of information using Markov-renewal methods,” _Queueing Systems_ , pp. 1-36, Aug. 2022.

- [33] Y. Inoue, H. Masuyama, T. Takine, and T. Tanaka, “A general formula for the stationary distribution of the age of information and its application to single-server queues,” _IEEE Transactions on Information Theory_ , vol. 65, no. 12, pp. 8305–8324, Aug. 2019.

- [34] T. Lillicrap, J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Silver, and D. Wierstra, “Continuous control with deep reinforcement learning,” Sept. 2015, arXiv:1509.02971.

- [35] Y. Liang, C. Guo, Z. Ding, and H. Hua, “Agent-based modeling in electricity market using deep deterministic policy gradient algorithm,” IEEE transactions on power systems, vol. 35, no. 6, pp. 4180–4192, Jun. 2020.

- [36] A. G. Baydin, B. A. Pearlmutter, A. A. Radul, and J. M. Siskind, “Automatic differentiation in machine learning: A survey,” _Journal of Marchine Learning Research_ , vol. 18, no. 153, pp. 1–43, 2018.

- [37] S. Caldas et al., “LEAF: A benchmark for federated settings,” 2018, arXiv:1812.01097.
