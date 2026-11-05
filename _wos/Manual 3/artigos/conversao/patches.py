# Correções de ordem de leitura que o classificador de layout não resolve (texto antes dos marcadores).
PATCHES = {
    "d15": [
        (
            "Generally, the connectivity cost depends on the scheduling rate _oi_ . Given that _U_ is the number of status updates that have been scheduled over a known time interval, its probability mass function can be expressed as",
            r"""Generally, the connectivity cost depends on the scheduling rate $o_i$. Given that $\mathcal{U}$ is the number of status updates that have been scheduled over a known time interval, its probability mass function can be expressed as

$$
P(\mathcal{U} | o_i) = \frac{\exp(-o_i) o_i^{\mathcal{U}}}{\mathcal{U}!}, \forall \mathcal{U} \in \mathbb{N}. \tag{25}
$$

*Proposition 1:* The long-term average connectivity cost per any arbitrary VT model update can be obtained as

$$
C_{\mathrm{conn}} = \lim_{\mathcal{U} \to \infty} \frac{1}{\mathcal{U}} \sum_{u=1}^{\mathcal{U}} \left( \frac{1}{\epsilon_{\max}} \sum_{i=1}^{M} \sum_{t=0}^{N_R - 1} \epsilon_i v_i |\omega_{M+1,i}^{u}(t)| + C_{\mathrm{time}}^{u} + C_{\mathrm{ene}}^{u} \right). \tag{26}
$$

*Proof:* The proof follows from (23) and (24). $\blacksquare$""",
        ),
        (
            "_Proposition 1:_ The long-term average connectivity cost per any arbitrary VT model update can be obtained as status arrival rate is Poisson while the service times are i.i.d. exponentials can be calculated as",
            "*Proposition 2:* The average synchronization gap when the status arrival rate is Poisson while the service times are i.i.d. exponentials can be calculated as",
        ),
    ],
    "d07": [("ALL:~~√~~", "√")],
}
# d15: capitular colada e nota de afiliação no meio do primeiro parágrafo da introdução
PATCHES["d15"] += [
    (
        "**D** IGITALespeciallytwinin communications(DT) continues tonetworksattract wide[1], healthcareattention, [2], [3], and manufacturing [4], [5]",
        "Digital twin (DT) continues to attract wide attention, especially in communications networks [1], healthcare [2], [3], and manufacturing [4], [5]",
    ),
    (
        "healthcare systems, environmental\n\nS. D. Okegbile and J. Cai are with the Network Intelligence and Innovation Lab ( _NI_<sup>2</sup> _L_ ), Department of Electrical and Computer Engineering, Concordia University, Montreal QC H3G 1M8, Canada (Emails: samuel.okegbile@concordia.ca; jun.cai@concordia.ca).\n\nH. Zheng, J. Chen and C. Yi are with the College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing, Jiangsu, 211106, China (Emails: zhenghao@nuaa.edu.cn; jiayuan.chen@nuaa.edu.cn; changyan.yi@nuaa.edu.cn).\n\nmonitoring systems, and other applications by involving human behaviour and activities.",
        "healthcare systems, environmental monitoring systems, and other applications by involving human behaviour and activities.\n\n> S. D. Okegbile and J. Cai are with the Network Intelligence and Innovation Lab ( _NI_<sup>2</sup> _L_ ), Department of Electrical and Computer Engineering, Concordia University, Montreal QC H3G 1M8, Canada (Emails: samuel.okegbile@concordia.ca; jun.cai@concordia.ca).\n\n> H. Zheng, J. Chen and C. Yi are with the College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing, Jiangsu, 211106, China (Emails: zhenghao@nuaa.edu.cn; jiayuan.chen@nuaa.edu.cn; changyan.yi@nuaa.edu.cn).",
    ),
]

# d15: tabelas I e II com variáveis matemáticas (conferidas contra a página)
PATCHES["d15"] += [
    (
        "TABLE:|Notation|Definition|",
        r"""|Notation|Definition|
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
|$\theta_{cmp}$|Computation cost threshold|""",
    ),
    (
        "TABLE:|Parameter|Value|",
        r"""|Parameter|Value|
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
|$\tau^{\mathrm{rate}}$|0.05|""",
    ),
]

# artefatos simples de tabela em outros artigos
PATCHES["d05"] = [  # NASSS (03 - Using ...)
    ("|Comlex|Desirability|", "|Complex|Desirability|"),
    ("|p||Personalised and improved treatments||", "|||Personalised and improved treatments||"),
]
PATCHES["d06"] = [  # Modular DT (04 - A Modular ...)
    ("|Pbd|RL [26]|\n|rocess-ase|Fuzzy reasoning [25]|", "|Process-based|RL [26]|\n||Fuzzy reasoning [25]|"),
]
PATCHES["d07"] += [  # Ethical and Legal (04 - Ethical ...)
    ("|√<br>= Effectively Addresses the Challenge,|✗ = Limited or|No Coverage||", "|√ = Effectively Addresses the Challenge, ✗ = Limited or No Coverage|||"),
]
