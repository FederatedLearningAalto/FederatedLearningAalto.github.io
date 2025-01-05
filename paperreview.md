---
title: "Paper Review Project"
layout: default
permalink: /paper-review/
---

# Paper Review 

The 2025 edition of the course CS-E4740 includes the option to complete a paper review instead (or on top) of the regular 
assignments. Completing a review will deepen your understanding of federated learning and improve your critical analysis 
skills. Below is a curated list of research papers for students to choose from. These papers focus on federated learning, 
covering foundational concepts, advanced techniques, and real-world applications. The main focus of your review should 
be how the methods presented in the paper relate to the theoretical concepts and algorithms covered in our course. 

## Instructions
1. **Choose a Paper:** Select a paper from the list below or propose one (with instructor approval).
2. **Review Structure:** Your review should include the following sections:
   - **Summary:** Summarize the main contributions and methodology.
   - **Comparison to Generalized Total Variation Framework:** Compare the proposed methods with the GTV minimization 
   framework discussed in the lectures and the [Federated Learning Book](https://github.com/alexjungaalto/FederatedLearning/blob/main/material/FLBook.pdf). Highlight similarities, differences, and how the methods build upon or diverge from the framework.
   - **Strengths:** Discuss what the paper does well.
   - **Weaknesses:** Point out limitations or areas for improvement.
3. **Deliverables:** 
   - A **slide deck** summarizing your review.
   - A **recorded slide talk** (maximum 10 minutes) explaining your findings.
4. **Submission Deadline:** [TBD]

## Paper List

### Foundational Papers

- McMahan, H. B., et al. (2017). "Communication-Efficient Learning of Deep Networks from Decentralized Data."
  - [DOI:10.48550/arXiv.1602.05629](https://arxiv.org/abs/1602.05629)
  - A pioneering work that introduces the concept of federated learning.

- Kairouz, P., et al. (2019). "Advances and Open Problems in Federated Learning."
  - [DOI:10.48550/arXiv.1912.04977](https://arxiv.org/abs/1912.04977)
  - A comprehensive survey of the state-of-the-art in federated learning and its challenges.

### Distributed Optimization for Federated Learning

- Smith, V., et al. (2017). "Federated Multi-Task Learning."
  - [DOI:10.48550/arXiv.1705.10467](https://arxiv.org/abs/1705.10467)
  - Extends federated learning to handle multiple related tasks across clients.

- 

### Federated Learning Flavours 

- Sattler, F., et al. (2019). "Clustered Federated Learning: Model-Agnostic Distributed Multi-Task Optimization under Privacy Constraints."
  - [DOI:10.48550/arXiv.1910.01991](https://arxiv.org/abs/1910.01991)
  - Introduces a clustered approach to federated learning for heterogeneous data.

- Ghosh, A., et.al. (2021). "An Efficient Framework for Clustered Federated Learning."
  - [arXiv:2006.04088](https://arxiv.org/abs/2006.04088)
  - Proposes the Iterative Federated Clustering Algorithm (IFCA) for clustered federated learning, which alternates 
between estimating cluster identities and optimizing model parameters for user clusters via gradient descent. 

- Sui, Y.,et.al. (2022). "Find Your Friends: Personalized Federated Learning with the Right Collaborators."
  - [arXiv:2210.06597](https://arxiv.org/abs/2210.06597)
  - Introduces FedeRiCo, a decentralized framework that enables clients in federated learning to select 
      optimal collaborators based on local data distributions.



### Federated Learning Applications

- Yang, Q., et al. (2019). "Federated Machine Learning: Concept and Applications."
  - [DOI:10.1145/3298981](https://doi.org/10.1145/3298981)
  - Provides practical insights and applications of federated learning in real-world scenarios.

- Li, T., et al. (2020). "Federated Optimization in Heterogeneous Networks."
  - [DOI:10.48550/arXiv.1812.06127](https://arxiv.org/abs/1812.06127)
  - Discusses optimization techniques for federated learning in settings with non-IID data.
  
- Douillard, A., et.al. (2023). "DiLoCo: Distributed Low-Communication Training of Language Models."
  - [DOI:10.48550/arXiv.2311.08105](https://arxiv.org/abs/2311.08105)
  - Proposes methods for distributed training of language models with reduced communication overhead.
  
- Mendes, N., et.al. (2024). "Federated Learning Framework for Prediction of Net Energy Demand in Transactive Energy Communities."
  - [DOI:10.1016/j.segan.2024.101522](https://doi.org/10.1016/j.segan.2024.101522)
  - Proposes a federated learning framework that enables accurate prediction of net energy demand in 
  transactive energy communities. The approach allows individual buildings to collaboratively train models 
  without sharing private data, enhancing both privacy and prediction accuracy. 

 - Q Arooj (2024), "FedWindT: Federated learning assisted transformer architecture for collaborative and secure wind power forecasting in diverse conditions."
 
 - Arooj, Q. (2024). "FedWindT: Federated Learning Assisted Transformer Architecture for Collaborative and Secure Wind Power Forecasting in Diverse Conditions."
  - [DOI:10.1016/j.energy.2024.133072](https://doi.org/10.1016/j.energy.2024.133072)
  - Introduces FedWindT, an innovative model that combines transformer neural architectures with federated learning to enhance wind power prediction.
 
- Doriguzzi-Corin, R., et.al. (2023). "FLAD: Adaptive Federated Learning for DDoS Attack Detection."
  - [DOI:10.1016/j.cose.2023.103597](https://doi.org/10.1016/j.cose.2023.103597)
  - Introduces FLAD, an adaptive federated learning approach designed to enhance DDoS attack detection. 
  
### Privacy and Security in Federated Learning

  - Geyer, R. et.al. (2017). "Differentially Private Federated Learning: A Client Level Perspective."
  - [arXiv:1712.07557](https://arxiv.org/abs/1712.07557)
  - Proposes an algorithm for client-sided differential privacy in federated learning, aiming to conceal individual 
     clients' contributions during training. 

- Bonawitz, K., et al. (2017). "Practical Secure Aggregation for Privacy-Preserving Machine Learning."
  - [DOI:10.1145/3133956.3133982](https://doi.org/10.1145/3133956.3133982)
  - Proposes a secure aggregation protocol to protect data during training.
  
 - Geiping, J., et.al. (2020). "Inverting Gradients – How Easy Is It to Break Privacy in Federated Learning?"
  - [arXiv:2003.14053](https://arxiv.org/abs/2003.14053)
  - Demonstrates that sharing parameter gradients in federated learning can lead to significant privacy breaches. 
  The authors show that it's possible to reconstruct high-resolution images from gradient information, even in trained 
  deep networks, challenging the assumption that federated learning inherently provides data privacy.


  

## Propose a Paper
If you wish to review a paper not listed here, please email [your email address] with the title, authors, and a brief justification for your choice.

---

Feel free to reach out with any questions or for further guidance!
