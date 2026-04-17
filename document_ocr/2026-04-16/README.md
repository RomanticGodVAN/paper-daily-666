# Document AI and OCR — 2026-04-16

- Papers: 3
- Skipped as duplicates: 0

## 1. Evaluating the Evaluator: Problems with SemEval-2020 Task 1 for Lexical Semantic Change Detection

- arXiv: `2604.13232`
- Link: https://arxiv.org/abs/2604.13232
- Announcement date: 2026-04-16
- Categories: cs.CL
- Tags: OCR noise, benchmark evaluation, lexical semantic change
- Reason: Paper discusses OCR noise as a significant data quality issue affecting benchmark performance in lexical semantic change detection. OCR is explicitly addressed as a core problem.

### Abstract

This discussion paper re-examines SemEval-2020 Task 1, the most influential shared benchmark for lexical semantic change detection, through a three-part evaluative framework: operationalisation, data quality, and benchmark design. First, at the level of operationalisation, we argue that the benchmark models semantic change mainly as gain, loss, or redistribution of discrete senses. While practical for annotation and evaluation, this framing is too narrow to capture gradual, constructional, collocational, and discourse-level change. Also, the gold labels are outcomes of annotation decisions, clustering procedures, and threshold settings, which could potentially limit the validity of the task. Second, at the level of data quality, we show that the benchmark is affected by substantial corpus and preprocessing problems, including OCR noise, malformed characters, truncated sentences, inconsistent lemmatisation, POS-tagging errors, and missed targets. These issues can distort model behaviour, complicate linguistic analysis, and reduce reproducibility. Third, at the level of bench-mark design, we argue the small curated target sets and limited language coverage reduce realism and increase statistical uncertainty. Taken together, these limitations suggest that the benchmark should be treated as a useful but partial test bed rather than a definitive measure of progress. We therefore call for future datasets and shared tasks to adopt broader theories of semantic change, document pre-processing transparently, expand cross-linguistic coverage, and use more realistic evaluation settings. Such steps are necessary for more valid, interpretable, and generalisable progress in lexical semantic change detection

## 2. MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning

- arXiv: `2604.13579`
- Link: https://arxiv.org/abs/2604.13579
- Announcement date: 2026-04-16
- Categories: cs.CL
- Tags: DocVQA, long documents, visual question answering, agentic workflow
- Reason: Paper explicitly addresses long document visual question answering with vision-aware agents. Central task is document VQA, fitting inclusion rules.

### Abstract

Conventional Retrieval-Augmented Generation (RAG) systems often struggle with complex multi-hop queries over long documents due to their single-pass retrieval. We introduce MM-Doc-R1, a novel framework that employs an agentic, vision-aware workflow to address long document visual question answering through iterative information discovery and synthesis. To incentivize the information seeking capabilities of our agents, we propose Similarity-based Policy Optimization (SPO), addressing baseline estimation bias in existing multi-turn reinforcement learning (RL) algorithms like GRPO. Our core insight is that in multi-turn RL, the more semantically similar two trajectories are, the more accurate their shared baseline estimation becomes. Leveraging this, SPO calculates a more precise baseline by similarity-weighted averaging of rewards across multiple trajectories, unlike GRPO which inappropriately applies the initial state's baseline to all intermediate states. This provides a more stable and accurate learning signal for our agents, leading to superior training performance that surpasses GRPO. Our experiments on the MMLongbench-Doc benchmark show that MM-Doc-R1 outperforms previous baselines by 10.4%. Furthermore, SPO demonstrates superior performance over GRPO, boosting results by 5.0% with Qwen3-8B and 6.1% with Qwen3-4B. These results highlight the effectiveness of our integrated framework and novel training algorithm in advancing the state-of-the-art for complex, long-document visual question answering.

## 3. Doc-V*:Coarse-to-Fine Interactive Visual Reasoning for Multi-Page Document VQA

- arXiv: `2604.13731`
- Link: https://arxiv.org/abs/2604.13731
- Announcement date: 2026-04-16
- Categories: cs.CL
- Tags: DocVQA, multi-page documents, OCR-free, visual reasoning
- Reason: Paper explicitly targets multi-page Document VQA with OCR-free agentic framework. Strong hits on OCR and DocVQA, central to document understanding.

### Abstract

Multi-page Document Visual Question Answering requires reasoning over semantics, layouts, and visual elements in long, visually dense documents. Existing OCR-free methods face a trade-off between capacity and precision: end-to-end models scale poorly with document length, while visual retrieval-based pipelines are brittle and passive. We propose Doc-$V^*$, an \textbf{OCR-free agentic} framework that casts multi-page DocVQA as sequential evidence aggregation. Doc-$V^*$ begins with a thumbnail overview, then actively navigates via semantic retrieval and targeted page fetching, and aggregates evidence in a structured working memory for grounded reasoning. Trained by imitation learning from expert trajectories and further optimized with Group Relative Policy Optimization, Doc-$V^*$ balances answer accuracy with evidence-seeking efficiency. Across five benchmarks, Doc-$V^*$ outperforms open-source baselines and approaches proprietary models, improving out-of-domain performance by up to \textbf{47.9\%} over RAG baseline. Other results reveal effective evidence aggregation with selective attention, not increased input pages.
