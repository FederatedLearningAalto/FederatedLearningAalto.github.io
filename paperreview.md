---
title: "Paper Review Project"
layout: default
permalink: /paper-review/
---

# Paper Review 

The 2025 edition of the course **CS-E4740 Federared Learning** includes the option to 
complete a paper review instead (or on top) of the regular assignments. Completing 
a review will deepen your understanding of federated learning and improve your critical 
analysis skills. 

Below is a curated list of research papers for students to choose from. These papers 
focus on federated learning, covering foundational concepts, advanced techniques, 
and real-world applications. 

Your review should compare and interpret the chosen paper against the concepts in our course. 
Try to answer questions like: Which instance of GTVMin does the paper use? Which optimization 
method do the authors use to solve GTVMin? What is the ultimate performance criterion of the 
studied FL methods?

## Instructions
1. **Choose a Paper:** Select a paper from the list below or propose one (with instructor approval).
2. **Review Structure:** Your review should include the following sections:
   - **Summary:** Summarize the main contributions and methodology.
   - **Interpretation:** Interpret the paper in terms of the concepts taught in our course 
and the [Federated Learning Book](https://github.com/alexjungaalto/FederatedLearning/blob/main/material/FLBook.pdf). 
Try to answer questions like: Which variant (if any) of GTV minimization does the paper 
study? Does the paper discuss a specific choice for the federated learning network? What optimisation 
methods are used (e.g., gradient based methods)? 
   - **Strengths:** Discuss what the paper does well.
   - **Weaknesses:** Point out limitations or areas for improvement.
3. **Deliverables:** 
   - A **slide deck** summarizing your review.
   - A **recorded slide talk** (maximum 10 minutes) explaining your findings.
4. **Submission Deadline:** [TBD]

## Paper List

### Foundational Papers

- McMahan, H. B., et al. (2017). **"Communication-Efficient Learning of Deep Networks from Decentralized Data."**
  - [DOI:10.48550/arXiv.1602.05629](https://arxiv.org/abs/1602.05629)
  - A pioneering work that introduces the concept of federated learning. Proposes the Federated Averaging (FedAvg) algorithm. 

- Li, T., et al. (2020). **"Federated Optimization in Heterogeneous Networks."**
  - [DOI:10.48550/arXiv.1812.06127](https://arxiv.org/abs/1812.06127)
  - Proposed the FL algorithm FedProx. 
        
- Smith, V., et al. (2017). **"Federated Multi-Task Learning."**
  - [DOI:10.48550/arXiv.1705.10467](https://arxiv.org/abs/1705.10467)
  - Extends federated learning to handle multiple related tasks across clients.

- Konečný, J., et.al. (2016). **"Federated Optimization: Distributed Machine Learning for On-Device Intelligence."**
  - [arXiv:1610.02527](https://arxiv.org/abs/1610.02527)
  - Introduces federated optimization as a framework for training machine learning models across distributed and heterogeneous devices. 

### Federated Learning Systems and Implementation

- Sanchez-Iborra, R., & Skarmeta, A. F. (2020). **"TinyML-Enabled Frugal Smart Objects: Challenges and Opportunities."** *IEEE Circuits and Systems Magazine*, 20(3), 4–18.  
  - [DOI:10.1109/MCAS.2020.3005467](https://doi.org/10.1109/MCAS.2020.3005467)  
  - Explores the integration of TinyML into smart objects, addressing key challenges and opportunities for resource-constrained environments.

- Dutta, L., & Bharali, S. (2021). **"TinyML Meets IoT: A Comprehensive Survey."** *Internet of Things*, 16, 100461.  
  - [DOI:10.1016/j.iot.2021.100461](https://doi.org/10.1016/j.iot.2021.100461)  
  - Provides an extensive overview of the intersection of TinyML and IoT, discussing frameworks, applications, and challenges in deploying machine learning on IoT devices.

- Takezawa, Y., Sato, R., Bao, H., Niwa, K., & Yamada, M. (2023). **"Beyond Exponential Graph: Communication-Efficient Topologies for Decentralized Learning via Finite-time Convergence."** 
  - [PDF](https://papers.nips.cc/paper_files/paper/2023/file/f201b3f3d0f08c6ab46c36b9052c1b64-Paper-Conference.pdf)  
  -  This paper studies a novel topology (graph structure) for decentralized learning that achieves both a fast consensus rate and low communication cost.
  
- Biswas, S., Kermarrec, A.-M., Marouani, A., Pires, R., Sharma, R., & De Vos, M. (2024). **"Boosting Asynchronous Decentralized Learning with Model Fragmentation."** 
  - *arXiv e-prints*, Art. no. arXiv:2410.12918. [doi:10.48550/arXiv.2410.12918](https://doi.org/10.48550/arXiv.2410.12918)  
  - This paper proposes a novel approach to asynchronous decentralized learning using model fragmentation, which divides models into smaller components. 

- Xing, H., Simeone, O., & Bi, S. (2020). **"Decentralized Federated Learning via SGD over Wireless D2D Networks."**  
  - IEEE 21st International Workshop on Signal Processing Advances in Wireless Communications (SPAWC)*,  Atlanta, GA, USA, 2020, pp. 1-5.  
  - [doi:10.1109/SPAWC48557.2020.9154332](https://doi.org/10.1109/SPAWC48557.2020.9154332)

- Chaves, A. J., Martín, C., Kim, K. S., Shahid, A., & Díaz, M. (2024). **"Federated Learning Meets Blockchain: A Kafka-ML Integration for Reliable Model Training Using Data Streams."**  
  - *2024 IEEE International Conference on Big Data (BigData)*, Washington, DC, USA, pp. 7677-7686.  
  - [DOI:10.1109/BigData62323.2024.10826034](https://doi.org/10.1109/BigData62323.2024.10826034)  
  - This paper integrates Kafka-ML with blockchain to enhance traceability and robustness in federated learning systems, particularly for real-time data streams. The approach leverages asynchronous FL to improve efficiency and scalability.

### Distributed Optimization for Federated Learning

- Boyd, S., Parikh, N., & Chu, E. (2010). **"Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers."**
  - [Foundations and Trends® in Machine Learning, 3(1), pp. 1–122](https://web.stanford.edu/~boyd/papers/pdf/admm_distr_stats.pdf)
  - Provides a comprehensive review of the Alternating Direction Method of Multipliers (ADMM) and its applications in distributed optimization 
      and statistical learning. 

- Scaman, K., et.al. (2019). **"Optimal Convergence Rates for Convex Distributed Optimization in Networks."**
  - [Journal of Machine Learning Research, 20(159):1-31](https://jmlr.org/papers/v20/19-543.html)
  - This work provides a theoretical analysis of distributed optimization of convex functions using a network of 
  computing units (= a Federated Learning network). 

- Sarcheshmehpour, Y., et.al. (2021). **"Federated Learning from Big Data Over Networks."**
   - [ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing, pp. 3055-3059](https://doi.org/10.1109/ICASSP39728.2021.9414903)
   - Applies a generic primal-dual method from convex optimization to solve GTVMin. 
   
- Rikos, A. I., Jiang, W., Charalambous, T., & Johansson, K. H. (2024). **"Distributed Optimization with Finite Bit Adaptive Quantization for Efficient Communication and Precision Enhancement."**  
  - [arXiv:2409.05418](https://arxiv.org/pdf/2409.05418)  
  - This paper addresses the challenge of unconstrained distributed optimization where each node's local function exhibits strong convexity with Lipschitz continuous gradients. 
      The authors propose an algorithm that enables nodes to converge to the exact optimal solution while exchanging only 3-bit quantized messages, achieving linear convergence rates.

- Lin, C.-Y., Kostina, V., & Hassibi, B. (2022). **"Differentially Quantized Gradient Methods."**  
  - [IEEE Transactions on Information Theory, 68(9): 6078-6097](https://doi.org/10.1109/TIT.2022.3171173)  
  - This paper explores gradient descent methods with differential quantization, emphasizing techniques like error compensation, sigma-delta modulation, 
      and their applications in federated learning. The authors analyze convergence rates and propose methods achieving linear convergence with quantized communication.

- Liu, B., et al. (2024). **"Asynchronous Local-SGD Training for Language Modeling."**  
  - [arXiv:2401.09135](https://arxiv.org/abs/2401.09135)  
  - Investigates asynchronous Local-SGD for training language models, analyzing the impact of hardware heterogeneity, model size, 
     and optimization methods. Proposes a novel delayed Nesterov momentum update and adaptive local training steps to mitigate 
     convergence issues, achieving performance comparable to synchronous Local-SGD with improved wall-clock efficiency.

- Le Bars, J., et al. (2023). **"Refined Convergence and Topology Learning for Decentralized SGD with Data Heterogeneity."**  
  - [Proceedings of Machine Learning Research (PMLR)](https://proceedings.mlr.press/v206/le-bars23a/le-bars23a.pdf)  
  - Analyzes the convergence of D-SGD under data heterogeneity, introducing the concept of neighborhood heterogeneity, which 
     couples communication topology with data distribution differences. Proposes learning data-dependent topologies to mitigate 
     the adverse effects of data heterogeneity, enhancing convergence rates.



### Federated Learning Flavours 

- Sattler, F., et al. (2019). **"Clustered Federated Learning: Model-Agnostic Distributed Multi-Task Optimization under Privacy Constraints."**
  - [DOI:10.48550/arXiv.1910.01991](https://arxiv.org/abs/1910.01991)
  - Introduces a clustered approach to federated learning for heterogeneous data.

- Ghosh, A., et.al. (2021). **"An Efficient Framework for Clustered Federated Learning."**
  - [arXiv:2006.04088](https://arxiv.org/abs/2006.04088)
  - Proposes the Iterative Federated Clustering Algorithm (IFCA) for clustered federated learning, which alternates 
between estimating cluster identities and optimizing model parameters for user clusters via gradient descent. 

- Sui, Y.,et.al. (2022). **"Find Your Friends: Personalized Federated Learning with the Right Collaborators."**
  - [arXiv:2210.06597](https://arxiv.org/abs/2210.06597)
  - Introduces FedeRiCo, a decentralized framework that enables clients in federated learning to select 
      optimal collaborators based on local data distributions.

- Anonymous authors. (2025). **"Clusters Agnostic Network Lasso Bandits."**  
  - [OpenReview: KWUFlIMn8A](https://openreview.net/forum?id=KWUFlIMn8A)  
  - Proposes a framework leveraging network lasso to address multi-task contextual bandits with piecewise constant task preferences. 
      The model achieves sublinear regret by optimizing intra-cluster density and sparsity in inter-cluster connections. Theoretical guarantees include a novel oracle inequality and an upper bound on regret.

  
      

### Federated Learning Applications

- Yang, Q., et al. (2019). **"Federated Machine Learning: Concept and Applications."**
  - [DOI:10.1145/3298981](https://doi.org/10.1145/3298981)
  - Provides practical insights and applications of federated learning in real-world scenarios.
  
- Douillard, A., et.al. (2023). **"DiLoCo: Distributed Low-Communication Training of Language Models."**
  - [DOI:10.48550/arXiv.2311.08105](https://arxiv.org/abs/2311.08105)
  - Proposes methods for distributed training of language models with reduced communication overhead.
  
- Mendes, N., et.al. (2024). **"Federated Learning Framework for Prediction of Net Energy Demand in Transactive Energy Communities."**
  - [DOI:10.1016/j.segan.2024.101522](https://doi.org/10.1016/j.segan.2024.101522)
  - Proposes a federated learning framework that enables accurate prediction of net energy demand in 
  transactive energy communities.

- Arooj, Q. (2024). **"FedWindT: Federated Learning Assisted Transformer Architecture for Collaborative and Secure Wind Power Forecasting in Diverse Conditions."**
  - [DOI:10.1016/j.energy.2024.133072](https://doi.org/10.1016/j.energy.2024.133072)
  - Introduces FedWindT, an innovative model that combines transformer neural architectures with federated learning to enhance wind power prediction.
 
- Doriguzzi-Corin, R., et.al. (2023). **"FLAD: Adaptive Federated Learning for DDoS Attack Detection."**
  - [DOI:10.1016/j.cose.2023.103597](https://doi.org/10.1016/j.cose.2023.103597)
  - Introduces FLAD, an adaptive federated learning approach designed to enhance DDoS attack detection. 
  
- Rui Ye et.al. (2024). **"OpenFedLLM: Training Large Language Models on Decentralized Private Data via Federated Learning."**
  - https://arxiv.org/abs/2402.06954
  - Studies ollaborative and privacy-preserving LLM training on the underutilized distributed private data via federated learning (FL), where multiple data 
    owners collaboratively train a shared model without transmitting raw data.

- Jung, A., et.al. (2021). **"Local Graph Clustering With Network Lasso."**
  - [IEEE Signal Processing Letters, 28, 106-110](https://doi.org/10.1109/LSP.2020.3045832)
  - Formulates local graph clustering as an instance of GTVMin. 
  
### Robustness, Privacy and Cyber-Security of Federated Learning

- Lugosi, G., & Mendelson, S. (2021). **"Robust Multivariate Mean Estimation: The Optimality of Trimmed Mean."**
  - [The Annals of Statistics, 49(1), pp. 393–410](https://doi.org/10.1214/20-AOS1961)
  - Investigates robust estimation of the multivariate mean under heavy-tailed distributions. The paper introduces a 
  trimmed mean estimator and proves its optimality in terms of minimax rates. The results demonstrate that the proposed 
  method achieves robust performance even in the presence of outliers or heavy-tailed data.
  
- Damaskinos, G., et.al. (2018). **"Asynchronous Byzantine Machine Learning (the case of SGD)."**
  - [Proceedings of the 35th International Conference on Machine Learning (ICML), PMLR Volume 80, pp. 1145–1154](http://proceedings.mlr.press/v80/damaskinos18a/damaskinos18a.pdf)
  -  Proposes a framework for asynchronous stochastic gradient descent (SGD) that is resilient to Byzantine faults. 
  
- Chang, F.-C., et.al. (2022). **"Gradient Descent: Robustness to Adversarial Corruption."**
  - [OPT2022: 14th Annual Workshop on Optimization for Machine Learning](https://openreview.net/pdf?id=gNpieWW7xFR)
  - Investigates the robustness of gradient descent to adversarially corrupted gradients.

- Holland, M. J. (2021). **"Scaling-Up Robust Gradient Descent Techniques."**
  - [Proceedings of the Thirty-Fifth AAAI Conference on Artificial Intelligence (AAAI-21)](https://cdn.aaai.org/ojs/16940/16940-13-20434-1-2-20210518.pdf)
  - Explores robust gradient descent techniques designed to scale effectively in large-scale optimization problems, 
     with applications to adversarial and noisy environments.

- Geyer, R. et.al. (2017). **"Differentially Private Federated Learning: A Client Level Perspective."**
  - [arXiv:1712.07557](https://arxiv.org/abs/1712.07557)
  - Proposes an algorithm for client-sided differential privacy in federated learning, aiming to conceal individual 
     clients' contributions during training. 

- Bonawitz, K., et al. (2017). **"Practical Secure Aggregation for Privacy-Preserving Machine Learning."**
  - [DOI:10.1145/3133956.3133982](https://doi.org/10.1145/3133956.3133982)
  - Proposes a secure aggregation protocol to protect data during training.
  
- Geiping, J., et.al. (2020). **"Inverting Gradients – How Easy Is It to Break Privacy in Federated Learning?"**
  - [arXiv:2003.14053](https://arxiv.org/abs/2003.14053)
  - Demonstrates that sharing parameter gradients in federated learning can lead to significant privacy breaches. 
  The authors show that it's possible to reconstruct high-resolution images from gradient information, even in trained 
  deep networks, challenging the assumption that federated learning inherently provides data privacy.

- Duchi, J. C., Jordan, M. I., & Wainwright, M. J. (2016). **"Minimax Optimal Procedures for Locally Private Estimation."**
  - [arXiv:1604.02390](https://arxiv.org/pdf/1604.02390)
  -  The paper provides fundamental limits ("minimax bounds") for a range of estimation problems, including mean estimation 
      and linear regression, and introduces procedures that achieve these rates. The work highlights the trade-offs between privacy guarantees and statistical efficiency.

- Cai, T. T., Wang, Y., & Zhang, L. (2021). **"The Cost of Privacy: Optimal Rates of Convergence for Parameter Estimation with Differential Privacy."**
  - [The Annals of Statistics, 49(5), pp. 2825–2850](https://doi.org/10.1214/21-AOS2058)
  -  The paper derives fundamental limits ("minimax optimal rates of convergence") for mean estimation and linear regression, providing lower bounds and 
      proposing algorithms that achieve the optimal rates. The work establishes a comprehensive understanding of the cost of privacy in statistical estimation.
 
- Asi, H., Feldman, V., & Talwar, K. (2022). **"Optimal Algorithms for Mean Estimation under Local Differential Privacy."**
  - [arXiv:2205.02466](https://arxiv.org/pdf/2205.02466)
  - This paper investigates the problem of mean estimation under local differential privacy constraints. 
      The authors analyze existing algorithms and introduce optimized locally private randomizers.
      
- Duchi, J. C., Jordan, M. I., & Wainwright, M. J. (2014). **"Privacy Aware Learning."** 
  - [J. ACM, 61(6), Article 38](https://doi.org/10.1145/2666468) 
  - This paper explores methods for privacy-aware learning in the context of distributed data. 
      The authors propose frameworks that balance utility and privacy by leveraging formal privacy guarantees.

- Guangfeng Yan, Tan Li, Kui Wu, Linqi Song, (2024). **"Killing two birds with one stone: Quantization achieves privacy in distributed learning."**
  - [Digital Signal Processing, Vol 146](https://www.sciencedirect.com/science/article/pii/S1051200423004487)
  -  This paper studies the new trade-offs between communication, privacy, and learning performance 
     of stochastic gradient descent with noisy quantized gradients.

## Propose a Paper
If you wish to review a paper not listed here, please email course instructor with the title, 
authors, and a brief justification for your choice.

---

Feel free to reach out with any questions or for further guidance!
