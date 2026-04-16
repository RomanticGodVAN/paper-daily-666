# Document AI and OCR — 2026-04-15

- Papers: 7
- Skipped as duplicates: 0

## 1. INDOTABVQA: A Benchmark for Cross-Lingual Table Understanding in Bahasa Indonesia Documents

- arXiv: `2604.11970`
- Link: https://arxiv.org/abs/2604.11970
- Announcement date: 2026-04-15
- Categories: cs.AI, cs.CL, cs.CV, cs.LG
- Tags: table VQA, document understanding, cross-lingual, benchmark
- Reason: Central contribution is a benchmark for table visual question answering on document images, directly targeting structured document understanding with explicit focus on table reasoning in documents.

### Abstract

We introduce INDOTABVQA, a benchmark for evaluating cross-lingual Table Visual Question Answering (VQA) on real-world document images in Bahasa Indonesia. The dataset comprises 1,593 document images across three visual styles (bordered, borderless, and colorful) with one or more than one tables, and 1,593 question-answer sets in four languages: Bahasa Indonesia, English, Hindi, and Arabic. This enables evaluation of Vision-Language Models (VLMs) in both monolingual (Bahasa documents with Bahasa questions) and cross-lingual settings (Bahasa documents with questions in other languages). We benchmark leading open-source VLMs (Qwen2.5-VL, Gemma-3, LLaMA-3.2) and GPT-4o and reveal substantial performance gaps, particularly on structurally complex tables and in low-resource languages. Fine-tuning a compact 3B and LoRA-finetuned 7B model on our dataset yields 11.6% and 17.8% improvements in accuracy. Providing explicit table region coordinates as additional input further improves performance by 4-7%, demonstrating the value of Spatial priors for table-based reasoning. Our findings underscore the importance of language-diverse, domain-specific datasets and demonstrate that targeted fine-tuning can significantly enhance VLM performance on specialized document understanding tasks. INDOTABVQA provides a valuable resource for advancing research in cross-lingual, structure-aware document understanding, especially in underrepresented regions of the world. Full dataset can be accessed in huggingface at: https://huggingface.co/datasets/NusaBharat/INDOTABVQA}

## 2. Empirical Evaluation of PDF Parsing and Chunking for Financial Question Answering with RAG

- arXiv: `2604.12047`
- Link: https://arxiv.org/abs/2604.12047
- Announcement date: 2026-04-15
- Categories: cs.CL, cs.IR
- Tags: PDF parsing, chunking, RAG, document understanding
- Reason: Systematically studies PDF parsing and chunking methods for financial QA, with explicit focus on parsing heterogeneous PDF content (tables, text, images) for document understanding.

### Abstract

PDF files are primarily intended for human reading rather than automated processing. In addition, the heterogeneous content of PDFs, such as text, tables, and images, poses significant challenges for parsing and information extraction. To address these difficulties, both practitioners and researchers are increasingly developing new methods, including the promising Retrieval-Augmented Generation (RAG) systems to automated PDF processing. However, there is no comprehensive study investigating how different components and design choices affect the performance of a RAG system for understanding PDFs. In this paper, we propose such a study (1) by focusing on Question Answering, a specific language understanding task, and (2) by leveraging two benchmarks from the financial domain, including TableQuest, our newly generated, publicly available benchmark. We systematically examine multiple PDF parsers and chunking strategies (with varied overlap), along with their potential synergies in preserving document structure and ensuring answer correctness. Overall, our results offer practical guidelines for building robust RAG pipelines for PDF understanding.

## 3. Towards Platonic Representation for Table Reasoning: A Foundation for Permutation-Invariant Retrieval

- arXiv: `2604.12133`
- Link: https://arxiv.org/abs/2604.12133
- Announcement date: 2026-04-15
- Categories: cs.AI
- Tags: table representation learning, permutation invariance, layout analysis
- Reason: Proposes novel table representation learning addressing layout permutation issues; central contribution is table structure understanding for robust retrieval, relevant to document table parsing.

### Abstract

Historical approaches to Table Representation Learning (TRL) have largely adopted the sequential paradigms of Natural Language Processing (NLP). We argue that this linearization of tables discards their essential geometric and relational structure, creating representations that are brittle to layout permutations. This paper introduces the Platonic Representation Hypothesis (PRH) for tables, positing that a semantically robust latent space for table reasoning must be intrinsically Permutation Invariant (PI). To ground this hypothesis, we first conduct a retrospective analysis of table-reasoning tasks, highlighting the pervasive serialization bias that compromises structural integrity. We then propose a formal framework to diagnose this bias, introducing two principled metrics based on Centered Kernel Alignment (CKA): (i) PI, which measures embedding drift under complete structural derangement, and (ii) rho, a Spearman-based metric that tracks the convergence of latent structures toward a canonical form as structural information is incrementally restored. Our empirical analysis quantifies an expected flaw in modern Large Language Models (LLMs): even minor layout permutations induce significant, disproportionate semantic shifts in their table embeddings. This exposes a fundamental vulnerability in RAG systems, in which table retrieval becomes fragile to layout-dependent noise rather than to semantic content. In response, we present a novel, structure-aware TRL encoder architecture that explicitly enforces the cognitive principle of cell header alignment. This model demonstrates superior geometric stability and moves towards the PI ideal. Our work provides both a foundational critique of linearized table encoders and the theoretical scaffolding for semantically stable, permutation invariant retrieval, charting a new direction for table reasoning in information systems.

## 4. Physics-Grounded Monocular Vehicle Distance Estimation Using Standardized License Plate Typography

- arXiv: `2604.12239`
- Link: https://arxiv.org/abs/2604.12239
- Announcement date: 2026-04-15
- Categories: cs.CV, eess.IV
- Tags: license plate OCR, vehicle distance estimation, typography-based ranging
- Reason: Core contribution includes robust license plate detection and OCR for metric ranging, directly targeting text recognition in images (scene text OCR).

### Abstract

Accurate inter-vehicle distance estimation is a cornerstone of Advanced Driver Assistance Systems (ADAS) and autonomous driving. While LiDAR and radar provide high precision, their high cost prohibits widespread adoption in mass-market vehicles. Monocular camera-based estimation offers a low-cost alternative but suffers from fundamental scale ambiguity. Recent deep learning methods for monocular depth achieve impressive results yet require expensive supervised training, suffer from domain shift, and produce predictions that are difficult to certify for safety-critical deployment. This paper presents a framework that exploits the standardized typography of United States license plates as passive fiducial markers for metric ranging, resolving scale ambiguity through explicit geometric priors without any training data or active illumination. First, a four-method parallel plate detector achieves robust plate reading across the full automotive lighting range. Second, a three-stage state identification engine fusing OCR text matching, multi-design color scoring, and a lightweight neural network classifier provides robust identification across all ambient conditions. Third, hybrid depth fusion with inverse-variance weighting and online scale alignment, combined with a one-dimensional constant-velocity Kalman filter, delivers smoothed distance, relative velocity, and time-to-collision for collision warning. Baseline validation reproduces a 2.3% coefficient of variation in character height measurements and a 36% reduction in distance-estimate variance compared with plate-width methods from prior work. Extensive outdoor experiments confirm a mean absolute error of 2.3% at 10 m and continuous distance output during brief plate occlusions, outperforming deep learning baselines by a factor of five in relative error.

## 5. MultiDocFusion: Hierarchical and Multimodal Chunking Pipeline for Enhanced RAG on Long Industrial Documents

- arXiv: `2604.12352`
- Link: https://arxiv.org/abs/2604.12352
- Announcement date: 2026-04-15
- Categories: cs.AI, cs.CL
- Tags: document parsing, OCR, hierarchical chunking, RAG
- Reason: Core contribution is multimodal document parsing pipeline with OCR and document structure reconstruction

### Abstract

RAG-based QA has emerged as a powerful method for processing long industrial documents. However, conventional text chunking approaches often neglect complex and long industrial document structures, causing information loss and reduced answer quality. To address this, we introduce MultiDocFusion, a multimodal chunking pipeline that integrates: (i) detection of document regions using vision-based document parsing, (ii) text extraction from these regions via OCR, (iii) reconstruction of document structure into a hierarchical tree using large language model (LLM)-based document section hierarchical parsing (DSHP-LLM), and (iv) construction of hierarchical chunks through DFS-based grouping. Extensive experiments across industrial benchmarks demonstrate that MultiDocFusion improves retrieval precision by 8-15% and ANLS QA scores by 2-3% compared to baselines, emphasizing the critical role of explicitly leveraging document hierarchy for multimodal document-based QA. These significant performance gains underscore the necessity of structure-aware chunking in enhancing the fidelity of RAG-based QA systems.

## 6. DocSeeker: Structured Visual Reasoning with Evidence Grounding for Long Document Understanding

- arXiv: `2604.12812`
- Link: https://arxiv.org/abs/2604.12812
- Announcement date: 2026-04-15
- Categories: cs.AI
- Tags: document understanding, multimodal reasoning, evidence grounding
- Reason: Central task is long document understanding with structured visual reasoning workflow

### Abstract

Existing Multimodal Large Language Models (MLLMs) suffer from significant performance degradation on the long document understanding task as document length increases. This stems from two fundamental challenges: 1) a low Signal-to-Noise Ratio (SNR), with crucial evidence buried in irrelevant pages; and 2) supervision scarcity, as datasets offering only final short answers provide a weak learning signal. In this paper, we address these challenges by proposing a paradigm that requires the model to execute a structured Analysis, Localization and Reasoning workflow. To instill this capability, we design a two-stage training framework: we first perform Supervised Fine-Tuning on high-quality data generated via an efficient knowledge distillation strategy. Subsequently, we employ an Evidence-aware Group Relative Policy Optimization which jointly optimizes for both evidence localization and answer accuracy. Additionally, we introduce a Evidence-Guided Resolution Allocation strategy to mitigate memory constraints of training on multi-pages documents. Extensive experiments demonstrate that DocSeeker achieves superior performance on both in-domain and out-of-domain tasks. We show it robustly generalizes from short-page training to ultra-long documents and is naturally synergistic with visual Retrieval-Augmented Generation systems, serving as a solid foundation for their implementation.

## 7. GlotOCR Bench: OCR Models Still Struggle Beyond a Handful of Unicode Scripts

- arXiv: `2604.12978`
- Link: https://arxiv.org/abs/2604.12978
- Announcement date: 2026-04-15
- Categories: cs.CL, cs.CV
- Tags: OCR, benchmark, multilingual, script evaluation
- Reason: Central contribution is OCR benchmark evaluating generalization across Unicode scripts

### Abstract

Optical character recognition (OCR) has advanced rapidly with the rise of vision-language models, yet evaluation has remained concentrated on a small cluster of high- and mid-resource scripts. We introduce GlotOCR Bench, a comprehensive benchmark evaluating OCR generalization across 100+ Unicode scripts. Our benchmark comprises clean and degraded image variants rendered from real multilingual texts. Images are rendered using fonts from the Google Fonts repository, shaped with HarfBuzz and rasterized with FreeType, supporting both LTR and RTL scripts. Samples of rendered images were manually reviewed to verify correct rendering across all scripts. We evaluate a broad suite of open-weight and proprietary vision-language models and find that most perform well on fewer than ten scripts, and even the strongest frontier models fail to generalize beyond thirty scripts. Performance broadly tracks script-level pretraining coverage, suggesting that current OCR systems rely on language model pretraining as much as on visual recognition. Models confronted with unfamiliar scripts either produce random noise or hallucinate characters from similar scripts they already know. We release the benchmark and pipeline for reproducibility. Pipeline Code: https://github.com/cisnlp/glotocr-bench, Benchmark: https://hf.co/datasets/cis-lmu/glotocr-bench.
