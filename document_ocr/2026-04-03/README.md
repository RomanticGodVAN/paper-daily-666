# Document AI and OCR — 2026-04-03

- Papers: 3
- Skipped as duplicates: 0

## 1. A Role-Based LLM Framework for Structured Information Extraction from Healthy Food Policies

- arXiv: `2604.01529`
- Link: https://arxiv.org/abs/2604.01529
- Announcement date: 2026-04-03
- Categories: cs.AI, cs.MA
- Tags: information extraction, policy documents, structured extraction
- Reason: Core task is structured information extraction from unstructured policy documents using LLMs, targeting document understanding and extraction of structured content.

### Abstract

Current Large Language Model (LLM) approaches for information extraction (IE) in the healthy food policy domain are often hindered by various factors, including misinformation, specifically hallucinations, misclassifications, and omissions that result from the structural diversity and inconsistency of policy documents. To address these limitations, this study proposes a role-based LLM framework that automates the IE from unstructured policy data by assigning specialized roles: an LLM policy analyst for metadata and mechanism classification, an LLM legal strategy specialist for identifying complex legal approaches, and an LLM food system expert for categorizing food system stages. This framework mimics expert analysis workflows by incorporating structured domain knowledge, including explicit definitions of legal mechanisms and classification criteria, into role-specific prompts. We evaluate the framework using 608 healthy food policies from the Healthy Food Policy Project (HFPP) database, comparing its performance against zero-shot, few-shot, and chain-of-thought (CoT) baselines using Llama-3.3-70B. Our proposed framework demonstrates superior performance in complex reasoning tasks, offering a reliable and transparent methodology for automating IE from health policies.

## 2. CASHG: Context-Aware Stylized Online Handwriting Generation

- arXiv: `2604.02103`
- Link: https://arxiv.org/abs/2604.02103
- Announcement date: 2026-04-03
- Categories: cs.CV, cs.LG
- Tags: handwriting generation, online handwriting, stroke synthesis
- Reason: Central task is online handwriting generation at sentence level, directly targeting handwritten content creation which falls under handwritten text/document generation.

### Abstract

Online handwriting represents strokes as time-ordered trajectories, which makes handwritten content easier to transform and reuse in a wide range of applications. However, generating natural sentence-level online handwriting that faithfully reflects a writer's style remains challenging, since sentence synthesis demands context-dependent characters with stroke continuity and spacing. Prior methods treat these boundary properties as implicit outcomes of sequence modeling, which becomes unreliable at the sentence scale and under limited compositional diversity. We propose CASHG, a context-aware stylized online handwriting generator that explicitly models inter-character connectivity for style-consistent sentence-level trajectory synthesis. CASHG uses a Character Context Encoder to obtain character identity and sentence-dependent context memory and fuses them in a bigram-aware sliding-window Transformer decoder that emphasizes local predecessor--current transitions, complemented by gated context fusion for sentence-level context.Training proceeds through a three-stage curriculum from isolated glyphs to full sentences, improving robustness under sparse transition coverage. We further introduce Connectivity and Spacing Metrics (CSM), a boundary-aware evaluation suite that quantifies cursive connectivity and spacing similarity. Under benchmark-matched evaluation protocols, CASHG consistently improves CSM over comparison methods while remaining competitive in DTW-based trajectory similarity, with gains corroborated by a human evaluation.

## 3. De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory Rules

- arXiv: `2604.02276`
- Link: https://arxiv.org/abs/2604.02276
- Announcement date: 2026-04-03
- Categories: cs.AI, cs.CL, cs.LG
- Tags: structured extraction, regulatory documents, rule parsing
- Reason: Central task is extracting structured rules from regulatory documents, directly targeting document parsing and structured content extraction from documents.

### Abstract

Regulatory documents encode legally binding obligations that LLM-based systems must respect. Yet converting dense, hierarchically structured legal text into machine-readable rules remains a costly, expert-intensive process. We present De Jure, a fully automated, domain-agnostic pipeline for extracting structured regulatory rules from raw documents, requiring no human annotation, domain-specific prompting, or annotated gold data. De Jure operates through four sequential stages: normalization of source documents into structured Markdown; LLM-driven semantic decomposition into structured rule units; multi-criteria LLM-as-a-judge evaluation across 19 dimensions spanning metadata, definitions, and rule semantics; and iterative repair of low-scoring extractions within a bounded regeneration budget, where upstream components are repaired before rule units are evaluated. We evaluate De Jure across four models on three regulatory corpora spanning finance, healthcare, and AI governance. On the finance domain, De Jure yields consistent and monotonic improvement in extraction quality, reaching peak performance within three judge-guided iterations. De Jure generalizes effectively to healthcare and AI governance, maintaining high performance across both open- and closed-source models. In a downstream compliance question-answering evaluation via RAG, responses grounded in De Jure extracted rules are preferred over prior work in 73.8% of cases at single-rule retrieval depth, rising to 84.0% under broader retrieval, confirming that extraction fidelity translates directly into downstream utility. These results demonstrate that explicit, interpretable evaluation criteria can substitute for human annotation in complex regulatory domains, offering a scalable and auditable path toward regulation-grounded LLM alignment.
