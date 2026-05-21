

# Rebuttal

Dear Reviewers, ACs, and PCs:

We are glad to receive valuable and constructive comments from all the reviewers. We have made a substantial effort to clarify reviewers' doubts and enrich our experiments in the rebuttal phase.
In our responses, **Table R**xx or **Figure R**xx refers to the new **R**ebuttal results in the supplementary materials. We have uploaded the revised manuscript according to all reviewers' suggestions. We put the new experimental results and discussion at the end of the revised manuscript. We also provided supplementary materials, which separate the newly added context for your convenience.
Below is a summary of our response: 

 
## Rebuttal to Reviewer H151  
  
We greatly appreciate Reviewer H151 for providing a detailed summary of our strengths. 
And greatly appreciate Reviewer H151 for proposing these insightful questions and providing these constructive suggestions. 
Below, we provide our responses to the comments, denoted by [W] for weaknesses and [Q] for questions.



**Response to W1:** 
ManiF-SMC is deliberately label-agnostic (uses only x during unlearning), which cuts the reliance on label information. 
Although it slightly reduces RA/TA, it makes ManiF-SMC suitable to more complex scenario such as Semantic communication, where the users can only access the encoder when the semantic communication system is deployed. 
In Fig. 8 in Appx, We also provide some fine-tuning skills with label to mitigate the utility degradation.



**Response to W2:**
The number of similar samples (k) provides a trade-off of unlearning effect and model utility preservation. 
Larger k preserves more model utility, but it also mitigates unlearning effect. The margin value $\alpha$ for original ManiF is important, but for ManiF-SMC, the $\alpha$ is replaced by an adaptive value $\alpha_w(a,p,n)$ guided by the model connectivity.
Hence, the original margin value will not influence ManiF-SMC too much; the margin automatically scales to the local manifold geometry.

  

**Response to W3:**
Thank you for your suggestions. 
We also evaluate on the larger TinyImageNet (200 classes) and show ManiF-SMC achieves effective forgetting with competitive RA/TA and far lower runtime than retraining (Figs. 4-5).


**Response to W4:**  
In our extensive retraining experimental observation, unlearning will make target sample close to the manifold representation position of other similar samples in the remaining dataset. In revision, we will present a corresponding figure and add a section to discuss about the observation. 

 

**Response to Q1:** 
Yes. We use the same unlearning set across all baselines and ManiF-SMC for the fairness.

  
**Response to Q2:** 
Thank you, we will bold the best performance values in the revision.
  
 
 
**Response to Q3:** 
We sincerely thank the Reviewer's question. 
In Algorithm 1 and our experiments, S_k is the top k similar samples in the remaining set to the erased one.
When calculating the centroid, we use all samples of S_k.
When choosing the positive sample, we only randomly sample one data point in S_k with replacement.

 
 

  
  
## Rebuttal to Reviewer nB5v  
  
  
We greatly thank Reviewer nB5v for acknowledging the contributions, soundness, and presentation quality of our paper. And we sincerely appreciate Reviewer nB5v for proposing these insightful comments. Below, we provide our responses to the comments, denoted by [W] for weaknesses. 

 
**Response to W1:** We greatly appreciate the Reviewer's insightful comment. 
In Sec. 4.2, w is the learnable control point of the Bezier path. 
When training with Eq.(4), we connect the original model and unlearned model and the initial model w with the weight as Eq.(4). 
t is the connect parameter from 0 to 1. In our experiment, we directly set it as 0.5 for simplicity. 
We will add these implementation details in the experimental setting, corresponding to our code, for exact reproducibility.

 
**Response to W2:** 
We sincerely thank the Reviewer's insightful comment. 
Beyond small datasets, we evaluate on TinyImageNet (200 classes) (Fig. 4~5), where ManiF-SMC achieves effective forgetting with competitive RA/TA and much lower runtime than retraining. Moreover, we also conducted new experiments for Vision Transformer (ViT) on MNIST for the image generative task. Results are provided as follows, indicating the unlearning effectiveness of our method. 

The **Tab.R1** of evaluating unlearning for ViT on MNIST.
| Model|MIA (before unl.)| MIA (after unl.)|MSE, remaining set (before)|MSE, remaining set (after)|MSE, test set (before)|MSE test set (after)|   
|---|---|---|---|---|---| ---|  
|ViT|62.00%| 67.00%| 0.0439|0.0443 |0.0442|0.0445|  
 

**Response to W3:** 
We sincerely appreciate the Reviewer's insightful comment.
The mismatch occurs because we have not updated the latest results on MNIST in the Table 8 in Appendix. 
Results in Table 8 are our previous experimental results (older code commit), but it is also effective for unlearning, which can also confirm the effectiveness of the proposed method.

 
**Response to W4:** 
Thank you for pointing this out.
We (all coauthors) have carefully proofread this paper and carefully revised this paper to reduce grammatical errors as much as possible. 
We also invite a native-English editor to proofread the revision to reduce such kinds of errors.


 
  
## Rebuttal to Reviewer ACuk  

We greatly appreciate your thoughtful review, which highlights our work's strengths and raises valuable questions and suggestions. We have responded to all of your comments, categorized by **[W]** for weaknesses and **[Q]** for questions. However, due to the space limitation, we can only present some of them here. Please respond to us so that we can present other responses.
 
**Response to W1:** 
Boundary unlearning [R1] targets class-level forgetting by shifting decision boundaries. Our goal is sample-level approximate unlearning and we usually don't need to shift the boundary.
We revised the Related Work section and provided the discussion about [R1].

[R1]. Chen, Min, et al. "Boundary unlearning: Rapid forgetting of deep networks via shifting the decision boundary." CVPR 2023.

 
  
**Response to W2:** 
We appreciate the Reviewer's comment. 
Mode connectivity serves as a tool to rapidly ensemble a new model to generate the local manifold for the top-k most similar samples $S_k$, without needing the unlearned data. It is a little bit like rapidly retraining the model for $S_k$ to generate the local manifold to guide the local margin. We place a single learnable control point $w$ on a Bezier path between the original and unlearned models, and optimize only $w$ while freezing $\theta_o$ and $\theta_u$. Updating $w$ on the S_k with the assistance of $\theta_o$ and $\theta_u$ performs a contrained, low-capacity local re-fit that rapidly reshapes the representation neighborhood around the erased samples, ensuring both local manifold retraining and model utility preservation.

We will clarity this in Sec. 4.2 and add a paragraph to support that the path-restricted update recovers the local manifold while limiting utility degradation.

  
  
**Response to W3 and Q1:** 
In section 4.2, Eq.(4) is applied to train the mode connectivity model to generate the local manifold representation for the adaptive margin calculation. We can train a connectivity curve, such as, $t \in [0,1]$ with step equal to 0.1, i.e., the curve with checkpoints in $\{0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1\}$. 
In our experiments, we use the checkpoint of $t = 0.5$, which is best for the unlearning effect.
We also provide the experiments of the curve in the following table to demonstrate the results.

The **Tab.R1** of evaluating the checkpoints on the connectivity curve on MNIST

| t | MIA|  RA  | TA  |   
| ---- | ---- | ---- | ---- |  
| 0.1     | 59.00%  | 99.63%   |  99.21%  |   
| 0.3     | 60.50%  | 99.65%   | 99.23%   | 
| 0.5     | 61.50%  | 99.57%   | 99.14%   |  
| 0.7     | 58.50%  | 99.58%   | 99.19%   |  
| 0.9     | 58.00%  | 99.62%   | 99.21%   |       

Q1 rebuttal. While the authors present the empirical performance of the connectivity model, they do not provide an intuitive or theoretical justification for why the Bézier curve formulation is suitable for the unlearning task. I suggest that the authors elaborate on this aspect to enhance the conceptual clarity.

We revised Section 4.2 and added an intuition about why we use mode connectivity to rapidly generate the local manifold representation for the unlearned sample.

Ideally, if we have a retrained model, we can calculate the optimal margin $\alpha$ from the triplet loss. 
However, we don't have the retrained model. Could we have a fast replacement? We propose to use the local mode connectivity [12, 47] to reconstruct a local manifold representation for the top-k most similar samples near the unlearned sample.

**Intuition.** 
In our problem, we need a model to reconstructs a local representation that is largely free of the unlearned samples' influence to guide the margin calculation. 
From [12, 47], we know mode connectivity can quickly ensemble a new model for two poisoned models based on a few benign samples to cancel residual negative influence (e.g., backdoors and poisoning). 
We leverage exactly that to rebuild the local manifold for the top-k neighbors and use it to set an adaptive margin.

 
**Response to Q2:** 
Model connectivity is used to rapidly ensemble a new model trained with only $S_k$ to generate the local manifold representation around the unlearned sample for the adaptive margin calculation for the unlearning method.

Q2 rebuttal. The manuscript outlines the functionality of model connectivity but lacks sufficient empirical or theoretical evidence to substantiate its necessity or effectiveness.

In Fast Geometric Ensembling (FGE)[12], Garipove et al proved that mode connectivity with Bezier optimizes a parametric curve to minimize the expected loss along the path. Once such a low-loss path exists, sampling a few points along the path gives an ensemble at almost no extra training cost. In [], they proved that this mode connectivity optimization for fast geometric ensembling can effectively mitigate the negative influence of original poisoned models.

We use the property of mode connectivity to quickly ensemble a new model to rapidly generate local manifold representations for the top-k remaining samples near the unlearned sample. The new generated local manifold representations will be used to guide the adaptive margin calculation for manifold contrastive forgetting (ManiF). Our empirical results show that ManiF with the adaptive margin (calculated by the mode connectivity ensembled model) achieves better unlearning and utility preservation than ManiF with a fixed margin, especially when unlearning a large amount of samples. We provide some results as follows.


The part of **Tab.2** Ablation evaluation of the adaptive margin by self-mode-connectivity (SMC) on MNIST.
| Unlearning sample size|MIA (ManiF, Fixed Margin)| MIA (ManiF-SMC, adaptive margin)|RA (ManiF)|RA (ManiF-SMC)|TA (ManiF)|TA (ManiF-SMC)|   
|---|---|---|---|---|---| ---|  
|200|60.50%| 61.50%| 99.57%|99.58% |99.12%| 99.14%|  
|400|59.00%|61.00%|99.47%| 99.48%|99.10%|99.11%|
|600|58.33%| 62.28%| 99.43%|99.47% | 99.04%| 99.10%|  
|800|59.37%|61.23%|99.08%| 99.43%|99.02%|99.12%|
|1000|59.20%|63.09%|98.93%| 99.41%|98.87%|99.09%|


**Response to Q3:** 
Originally, we use the centroid of the whole class (which is fixed) and push the unlearned samples away from this centroid. However, in our extensive experiments of retraining, we observed that the unlearned sample should be pushed away from its original representation position, and the new unlearned representation of the unlearned sample (in the retrained model without this sample) will be close to other retained samples that exhibit similarity to it. Hence, we choose the average of representations of top-k similar samples as the centroid. We push it was from the unlearned sample while close to the positive samples of a similar set, which is consistent with our experimental observation. We will add a paragraph in Sec. 3.2 to clarify the motivation.
 
**Response to Q4:** 
When representations are learned to have high manifold capacity (MMCRs), classes form tight and separable manifolds as introduced in Sec. 3.1. This makes representation-only unlearning feasible and reliable. This observation is also what leads us to "forget on the manifold", rather than via task gradients.
For ManiF, the manifold capacity can be used to guide the margin calculation, but it is still a fixed value, not as good as ManiF-SMC with an adaptive margin value calculated by nearby local manifold representation via mode connectivity.



Q4 rebuttal. I am satisfied with their answer to this question.
We appreciate your comments and are glad that our response answered your question.
 
**Response to Q5:** 
The value k is the size of the top-k most similar dataset in the remaining set, $S_k$.
In Eq.(4), $t$ is the path parameter (along a quadratic Bezier curve) that indexes where we are between the two endpoint models $\theta_u$ (at $t=0$) and $\theta_o$ (at $t=1$). And it is also used to calculate the connecting weight for the learned control point w.

Q5 rebuttal. It would be helpful if the authors explicitly defined the parameter 
 in the paper to facilitate better comprehension for readers.

We thank the reviewers comments and suggestions. In the revision in Section 4.2, we added these explanation in the paper.
After Eq. (4), we added "$t$ is the path parameter (along a quadratic Bezier curve) that indexes where we are between the two endpoint models $\theta_u$ (at $t=0$) and $\theta_o$ (at $t=1$). And it is also used to calculate the connecting weight for the learned control point w." 

Then, after introducing the top-k most similar dataset, we added "The value k is the size of the top-k most similar dataset in the remaining set, $S_k$."

  
## Rebuttal to Reviewer v7a6  
  
We thank you very much for the very insightful comment, which highlights our work's strengths and raises valuable questions and suggestions. Below, we provide our point-to-point responses to the comments, denoted by **[W]** for weaknesses and **[Q]** for questions.

**Response to W1 and Q2:** 
The advantage of our method compared to GA-type methods is that we unlearn models without needing the original task (label) information.
We only focus on the learned manifold representation, which cuts off the reliance on the original task, making the unlearning method suitable to more complex scenarios, such as semantic communication, where the users only have access to the sending encoder after the semantic communication system is deployed. We revised and added a new section to discuss it in our revision to reduce the confusion. 

**Response to W2:** 
We revised the paper by adding a discussion paragraph with the representation-focused unlearning methods [R2, R3] in the Related Work Section.
While [R2, R3] processing unlearning on the learned representation, they still need the label (original task information) to guide the unlearning process.
Compared with [R2, R3], we use maximum manifold capacity representations (MMCRs) to ensure that the learned representations form tight, well-separated class manifolds.
This makes our representation-only unlearning feasible and reliable.
  
[R2]. Sepahvand, Nazanin Mohammadi, et al. "Selective unlearning via representation erasure using domain adversarial training." ICLR25'.
[R3]. Wang, Weiqi, et al. "Machine unlearning via representation forgetting with parameter self-sharing." TIFS23'.
 
**Response to W3:** 
We added a new paragraph in the Related Work to highlight the difference. While GA-based methods also incorporate regulation terms to prevent model degradation, we should explain that our unlearning method is task agnostic and can be executed based solely on representation.
 
**Response to Q1:** 
Yes, this unlearning method is also transferable to other representation learning frameworks.
We provide the experimental results for InforNCE (contrastive learning) and information bottleneck (IB) (representation learning) as follows.

The **Tab.R2** of evaluating the other learning methods on MNIST.
| Methods|MIA (before unl.)| MIA (after unl.)|RA (before)|RA (after)|TA (before)|TA (after)|   
|---|---|---|---|---|---| ---|  
|IB|51.99%| 61.00%| 99.49%|99.47% | 98.96%| 98.91%|  
|InfoNCE|50.50%|53.50%|99.39%| 99.40%|98.91%|98.83%|
 
