

# Rebuttal

Dear Reviewers, ACs, and PCs:

We are glad to receive valuable and constructive comments from all the reviewers. We have made a substantial effort to clarify reviewers' doubts and enrich our experiments in the rebuttal phase.
In our responses, **Table R**xx or **Figure R**xx refers to the new **R**ebuttal results in the supplementary materials. We have uploaded the revised manuscript according to all reviewers' suggestions. We put the new experimental results and discussion at the end of the revised manuscript. We also provided supplementary materials, which separate the newly added context for your convenience.
Below is a summary of our response: 

 
## Rebuttal to Reviewer aZe7  
  

We greatly appreciate Reviewer aZe7 for proposing these insightful questions and providing these constructive suggestions. 
Below, we provide our responses to the comments, denoted by [W] for weaknesses and [Q] for questions.

**Response to W1:** 
Thank you for this helpful comment. Our main claim is not that ManiF-SMC uniformly dominates all prior methods by a large numerical margin, but that it achieves competitive unlearning performance under a stricter and more practical information regime. In particular, ManiF-SMC operates purely in representation space, and is designed to reduce reliance on task labels. 
 
The paper compares against representative strong baselines, including GA, VBU, RFU, SalUn, and the gold-standard retraining. Figure 5 explicitly highlights an important fairness point: ManiF-SMC is the only compared method that unlearns without labels, while SalUn maintains stronger utility partly because it fine-tunes on retained data. 

**Response to W2:**
Thank you for this important comment. Approximate unlearning is generally harder to verify than exact unlearning, but it is not a specific flaw of ManiF-SMC. Our goal in this work is to design a practical approximate unlearning method that remains as consistent as possible with retraining behavior while operating in a weaker-access setting.
  
**Response to Q1:** 
Thank you for this constructive suggestion. We supplemented the evaluation of the squared differences between erased samples' representation and top-k similar remaining samples' representation before and after unlearning as follows. 
The results demonstrate that our method can effectively maps erased samples toward retained clusters across datasets.

The **Tab.R1** of average of squared differences between erased samples' representation and top-k similar remaining samples' representation on MNIST.
| Unlearning sample size|Average of squared differences (before unlearning)| Average of squared differences (after unlearning)|  
|---|---|---|
|200|16.046| 12.525| 
|400|14.176|12.921| 
|600|15.102| 12.913|   
|800|14.037|12.653| 
|1000|13.732|12.075| 
|1200|13.378 | 11.314|

**Response to Q2:** 
In our setting, batch unlearning is implemented by optimizations.
ManiF-SMC is formulated directly on an unlearning set, where the objective sums over all erased samples in the request. 
And, the method optimizes one shared unlearning objective for the whole batch rather than treating each sample independently.

 


  
  
## Rebuttal to Reviewer w3mc  
  
We sincerely appreciate Reviewer w3mc for reviewing our paper. Below, we provide our responses to the comments, denoted by [W] for weaknesses and [Q] for questions.

**Response to W1:** 
We will add a brief discussion clarifying that since the SMC is calculated based on the retained neighborhood data $S_k$ rather than retraining on the full retained dataset, the added cost is local and modest in practice. 

 
**Response to W2:** 
In the revision, we will supplement the key hyperparameters when introducing each baseline method in Appendix F. We set unlearning update ratio as 0.00001 for GA, the threshold $\lambda=0.2$ for VBU, the weight-masking to 50\% for SalUn, and the forgetting and remembering set ratio as 1:1 for RFU.


**Response to W3:** 
In the main experiments, we already evaluate batch unlearning with unlearning sample size (USS) ranging from 200 to 1200 across multiple datasets.

To evaluate multiple sequential unlearning requests, we further conduct experiments to unlearning 1 to 5 requests, each with 200 random unlearning samples. The results is provided as follows.  

The **Tab.R2** of ManiF-SMC unlearning with different requests on MNIST.
| Unlearning request times| MIA (%) | RA (%) | TA (%) |   
|---|---|---| --- |
|1|62.00| 99.59| 99.15 | 
|2|64.00|99.58| 99.18| 
|3|63.58| 99.48| 99.09| 
|4|64.31|99.35| 99.05| 
|5|63.93|99.54| 99.11| 
 


**Response to Q1:** 
To evaluate the high non-IID setting, we conduct additional experiments to unlearning 200 samples in one class on MNIST and CIFRAR10. We only show the results on CIFAR10 as the space limitation.

The **Tab.R3** of Unlearning non-IID samples of ManiF-SMC on CIFAR10.
| Unlearning Sample Size| MIA (%) | RA (%) | TA (%) | Unlearning Class Accuracy (%)| 
|---|---|---|---|---|
|200|75.49| 93.84| 77.65 | 72.11 |
|400|68.50| 94.18| 77.95| 73.16 |
|600|75.33| 93.86| 77.90| 67.33 |
|800|71.62| 94.48| 78.37| 77.60 |
|1000|64.49| 94.72| 78.80| 73.88|

**Response to Q2:** 
Thank you. The current paper already partially isolates the SMC overhead through the ManiF vs. ManiF-SMC ablation: for example, RT increases from 2.02s to 2.37s (200 samples) on CIFAR10, showing that SMC adds a moderate overhead. 
Here, we should explain that the SMC computation cost that we reported only includes the time to generate local manifold representation for adaptive margin calculation. The running time to find the top-k similar representations based on original model is omited because it could be implemented off-line.
 
  
## Rebuttal to Reviewer hyxn  

We greatly appreciate your thoughtful review, which highlights our work's strengths and raises valuable questions and suggestions. We have responded to all of your comments, categorized by **[W]** for weaknesses and **[Q]** for questions. 


**Response to W1:** 
Thank you for this thoughtful comment. The existing ablation (Section 5.4, table 3) shows the comparison of fixed-margin ManiF and the ManiF with SMC surrogate, where the fixed-margin ManiF calculating using the original neighbor embeddings. The results demonstrate that ManiF with SMC surrogate achieves better forgetting effectiveness and utility preservation than fixed margin calculated with original neighbor embeddings. At the same time, we would like to clarify that our goal is not to match the pre-unlearning geometry of the original model, but to approximate the post-unlearning / retrained retained-data geometry. 
SMC is a good way to generate a fast surrogate for the local retained geometry when the retrained model is not available. 
Simply using the original neighbor representations is also an approximate way but ManiF-SMC is better than ManiF with fixed margin. 
 

**Response to W2:** 
Thank you for this helpful comment. We agree that the main conceptual contribution of the paper begins with the reformulation of approximate unlearning in representation space and the resulting ManiF push-pull triplet-loss objective. In the revision, we would like to revise the title to remove the self mode connectivity. An example title could be "Approximate Machine Unlearning through Manifold Representation Forgetting."
 


 **Response to  Typos: "Priliminary", "Retriened"**  
We thank the reviewer's comments. We fixed these typos and carefully checked the whole paper to avoid the typos and grammar errors.
  
 
  
  
## Rebuttal to Reviewer evEi  
  
We thank the reviewer evEi very much for reviewing our paper. Below, we provide our point-to-point responses to the comments, denoted by **[W]** for weaknesses and **[Q]** for questions.

**Response to W1:** 
Thank you for this thoughtful and constructive comment. We would like to clarify that the current manuscript already provides more qualitative comparison than only Gradient Ascent (GA). Figure 1 introduces the retraining intuition by contrasting GA with retraining as an example, while Figure 4 further visualizes GA, VBU, SalUn, and ManiF-SMC on CIFAR10. To avoid the confusion and misunderstanding, in the revision, we will combine Figure 1 and Figure 4 and present them early.


**Response to W2:** 
Thank you for this thoughtful comment. For the retained-neighbor set, our intention is not to assume that the original representation is a perfect post-unlearning geometry, but to use it as a stable pre-unlearning semantic index for selecting candidate retained neighbors. The neighbor set is selected only from the retained data $S_r$, so forgotten samples are excluded from the candidate pool itself. Moreover, the original representation is used only for neighbor identification, the representation of the chosen samples will be updated during unlearning training.

Regarding SMC, in the paper, we state that, ideally, one would use the retrained model on $S_r$ to estimate the post-retraining centroid and choose the margin, but this model is unavailable. SMC is introduced as a fast replacement for that unavailable reference. We also conduct the ManiF vs. ManiF-SMC ablation (Section 5.4, table 3) to support for SMC's usefulness.


**Response to W3:** 
Thank you. The current manuscript already uses the standard multi-metric protocol for approximate unlearning and compares against Retraining, GA, VBU, RFU, and SalUn, with broader comparisons also appearing in Figure 4 and Table 1.
We will strengthen the revision by adding a direct retraining-alignment metric, making baseline inclusion more consistent across the main plots. Moreover, we conducted new experiments to evaluate generative model unlearning as follows, which demonstrates the utility preservation of our unlearning method.



We really appreciate reviewer evEi's reply and comments. Since the character limitation, we only provided limited materials in the previous rebuttal. Now, we supplemented more discussion and responses here.

For the concern of "point-by-point revisions were not provided", the KDD only allows the resubmission to have one page ahead the paper, so we summarize our revision in the resubmission. 
Since KDD has recorded the 2 versions (KDD26' Rounds 1 and 2), we can provide the detailed response and highlight the main changes of the revised manuscript by coloring the modified text in blue, and we can attach these after the appendix.

For the concern of "retraining baseline and retraining-alignment metric", we supplemented new retraining experiments on VAE model unlearning. We also supplemented a metric of the performance gap against Retraining for both classification model unlearning and generative model unlearning. 
The experimental results are provided in Tab. R4, Tab. R5, and Tab. R6, where our method, ManiF-SMC, always achieves the smaller performance gap with Retraining than other unlearning methods in most metrics.

The **Tab.R4** of unlearning VAEs Comparison between ManiF-SMC, VBU, and SalUn on CIFAR10.
A performance gap against Retraining is provided in (•).
| Methods | Unlearning Sample Size|MIA (%) |R-MSE |T-MSE |  
|---|---|---|---|---| 
|Retraining|200|55.50 |  0.00170| 0.00171 |  
|VBU|200|74.49 (18.99)| 0.00618 (0.00448)| 0.00626 (0.00455) |  
|SalUn|200|64.99 (9.49)| 0.00233 (0.00063)| 0.00239 (0.00068)|
|ManiF-SMC|200|54.00 (1.50)| 0.00192 (0.00022) | 0.00192 (0.00021)|  

The **Tab.R5** of performance summary of various unlearning methods on MNIST. 
A performance gap against Retraining is provided in (•).
| Methods | MIA(%)|  RA(%)  | TA(%)  |   
| ---- | ---- | ---- | ---- |  
| Retraining  | 63.00  | 99.49  |  99.23|   
| GA     | 64.50 (1.50) | 99.01 (0.48) | 98.81 (0.42) | 
| VBU     | 57.00 (6.00) | 99.37 (0.12) | 99.15 (0.08) | 
| RFU     | 53.50 (9.50) | 99.39 (0.10) | 99.28 (0.05) |  
| SalUn     | 55.00 (8.00) | 99.37 (0.12) | 99.22 (0.01)  |  
| ManiF (Our)    | 61.00 (2.00) | 99.55 (0.06)  | 99.10 (0.13) | 
| ManiF-SMC (Our)    | 62.00 (1.00) | 99.59 (0.10) | 99.15  (0.08) | 

The **Tab.R6** of performance summary of various unlearning methods on CIFAR10. 
A performance gap against Retraining is provided in (•).
| Methods | MIA (%)|  RA(%)  | TA(%)  |   
| ---- | ---- | ---- | ---- |  
| Retraining  | 61.00  | 99.28   |  82.48  |   
| GA     | 54.00 (7.00) | 97.83  (1.45) | 79.96  (2.52) | 
| VBU     | 56.00 (5.00) | 97.82  (1.46) | 80.23  (2.25) | 
| RFU     | 56.00 (5.00) | 98.57  (0.71) | 80.89  (1.59) |  
| SalUn     | 55.00 (6.00) | 98.85  (0.43) | 80.83 (1.65)  |  
| ManiF (Our)    | 56.00 (5.00) | 98.96 (0.32)  | 81.71  (0.77) | 
| ManiF-SMC (Our)    | 59.00 (2.00) | 99.04  (0.24) | 81.75  (0.73) | 


For the concern of "the neighbor-set contamination issue", we would like to explain that the neighbor samples sets have no contamination even they have some similar features because these samples are not requested to be unlearned by users and are independent against unlearned samples. 
The model and neighbor representations may have contamination issues because the model is originally trained with unlearned samples. The model and neighbor-representation contamination will motivate us to use a clean representation surrogate rather than original representation, which is also the motivation that we propose to use SMC to generate a new manifold representation.
Moreover, the SMC is trained as Eq.7 in the paper, where we usually set t = 0.5 and "w" is a new learnable initial model. Training a SMC surrogate as Eq.7 with t=0.5 enables the influence weight of original model $\theta_o$ be less than 0.5, which ensures that the SMC surrogate will less be influenced by the contamination issues than original models.

To evaluate the update of the new representations, we also supplemented the experiments of the squared differences between erased samples' representation and top-k similar remaining samples' representation before and after unlearning as follows. 


The **Tab.R1** of average of squared differences between erased samples' representation and top-k similar remaining samples' representation on MNIST.
| Unlearning sample size|Average of squared differences (before unlearning)| Average of squared differences (after unlearning)|  
|---|---|---|
|200|16.046| 12.525| 
|400|14.176|12.921| 
|600|15.102| 12.913|   
|800|14.037|12.653| 
|1000|13.732|12.075| 
|1200|13.378 | 11.314|