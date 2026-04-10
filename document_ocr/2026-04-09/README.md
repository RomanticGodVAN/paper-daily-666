# Document AI and OCR — 2026-04-09

- Papers: 5
- Skipped as duplicates: 0

## 1. ARIA: Adaptive Retrieval Intelligence Assistant -- A Multimodal RAG Framework for Domain-Specific Engineering Education

- arXiv: `2604.06179`
- Link: https://arxiv.org/abs/2604.06179
- Announcement date: 2026-04-09
- Categories: cs.CL, cs.IR
- Tags: document parsing, diagram interpretation, multimodal RAG
- Reason: Core contribution includes structured document analysis pipeline with Docling for document parsing and diagram interpretation, central to document AI.

### Abstract

Developing effective, domain-specific educational support systems is central to advancing AI in education. Although large language models (LLMs) demonstrate remarkable capabilities, they face significant limitations in specialized educational applications, including hallucinations, limited knowledge updates, and lack of domain expertise. Fine-tuning requires complete model retraining, creating substantial computational overhead, while general-purpose LLMs often provide inaccurate responses in specialized contexts due to reliance on generalized training data. To address this, we propose ARIA (Adaptive Retrieval Intelligence Assistant), a Retrieval-Augmented Generation (RAG) framework for creating intelligent teaching assistants across university-level courses. ARIA leverages a multimodal content extraction pipeline combining Docling for structured document analysis, Nougat for mathematical formula recognition, and GPT-4 Vision API for diagram interpretation, with the e5-large-v2 embedding model for high semantic performance and low latency. This enables accurate processing of complex educational materials while maintaining pedagogical consistency through engineered prompts and response controls. We evaluate ARIA using lecture material from Statics and Mechanics of Materials, a sophomore-level civil engineering course at Johns Hopkins University, benchmarking against ChatGPT-5. Results demonstrate 97.5% accuracy in domain-specific question filtering and superior pedagogical performance. ARIA correctly answered all 20 relevant course questions while rejecting 58 of 60 non-relevant queries, achieving 90.9% precision, 100% recall, and 4.89/5.0 average response quality. These findings demonstrate that ARIA's course-agnostic architecture represents a scalable framework for domain-specific educational AI deployment.

## 2. LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources

- arXiv: `2604.06571`
- Link: https://arxiv.org/abs/2604.06571
- Announcement date: 2026-04-09
- Categories: cs.AI, cs.CL, cs.IR, cs.LG
- Tags: OCR, document parsing, PDF extraction, layout analysis
- Reason: Explicitly targets OCR and document parsing pipeline for heterogeneous documents (forms, posters, PDFs) with layout analysis.

### Abstract

Missing-person and child-safety investigations rely on heterogeneous case documents, including structured forms, bulletin-style posters, and narrative web profiles. Variations in layout, terminology, and data quality impede rapid triage, large-scale analysis, and search-planning workflows. This paper introduces the Guardian Parser Pack, an AI-driven parsing and normalization pipeline that transforms multi-source investigative documents into a unified, schema-compliant representation suitable for operational review and downstream spatial modeling. The proposed system integrates (i) multi-engine PDF text extraction with Optical Character Recognition (OCR) fallback, (ii) rule-based source identification with source-specific parsers, (iii) schema-first harmonization and validation, and (iv) an optional Large Language Model (LLM)-assisted extraction pathway incorporating validator-guided repair and shared geocoding services. We present the system architecture, key implementation decisions, and output design, and evaluate performance using both gold-aligned extraction metrics and corpus-level operational indicators. On a manually aligned subset of 75 cases, the LLM-assisted pathway achieved substantially higher extraction quality than the deterministic comparator (F1 = 0.8664 vs. 0.2578), while across 517 parsed records per pathway it also improved aggregate key-field completeness (96.97\% vs. 93.23\%). The deterministic pathway remained much faster (mean runtime 0.03 s/record vs. 3.95 s/record for the LLM pathway). In the evaluated run, all LLM outputs passed initial schema validation, so validator-guided repair functioned as a built-in safeguard rather than a contributor to the observed gains. These results support controlled use of probabilistic AI within a schema-first, auditable pipeline for high-stakes investigative settings.

## 3. FlowExtract: Procedural Knowledge Extraction from Maintenance Flowcharts

- arXiv: `2604.06770`
- Link: https://arxiv.org/abs/2604.06770
- Announcement date: 2026-04-09
- Categories: cs.AI, cs.CV
- Tags: OCR, diagram parsing, flowchart extraction, document understanding
- Reason: Central task is extracting procedural knowledge from flowcharts using OCR (EasyOCR) and diagram parsing, core document AI contribution.

### Abstract

Maintenance procedures in manufacturing facilities are often documented as flowcharts in static PDFs or scanned images. They encode procedural knowledge essential for asset lifecycle management, yet inaccessible to modern operator support systems. Vision-language models, the dominant paradigm for image understanding, struggle to reconstruct connection topology from such diagrams. We present FlowExtract, a pipeline for extracting directed graphs from ISO 5807-standardized flowcharts. The system separates element detection from connectivity reconstruction, using YOLOv8 and EasyOCR for standard domain-aligned node detection and text extraction, combined with a novel edge detection method that analyzes arrowhead orientations and traces connecting lines backward to source nodes. Evaluated on industrial troubleshooting guides, FlowExtract achieves very high node detection and substantially outperforms vision-language model baselines on edge extraction, offering organizations a practical path toward queryable procedural knowledge representations. The implementation is available athttps://github.com/guille-gil/FlowExtract.

## 4. Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models

- arXiv: `2604.06912`
- Link: https://arxiv.org/abs/2604.06912
- Announcement date: 2026-04-09
- Categories: cs.AI, cs.CV
- Tags: document understanding, OCR, multimodal LLM efficiency, adaptive perception
- Reason: Explicitly targets document understanding and OCR benchmarks as core applications, with substantial performance improvements reported.

### Abstract

MLLMs require high-resolution visual inputs for fine-grained tasks like document understanding and dense scene perception. However, current global resolution scaling paradigms indiscriminately flood the quadratic self-attention mechanism with visually redundant tokens, severely bottlenecking inference throughput while ignoring spatial sparsity and query intent. To overcome this, we propose Q-Zoom, a query-aware adaptive high-resolution perception framework that operates in an efficient coarse-to-fine manner. First, a lightweight Dynamic Gating Network safely bypasses high-resolution processing when coarse global features suffice. Second, for queries demanding fine-grained perception, a Self-Distilled Region Proposal Network (SD-RPN) precisely localizes the task-relevant Region-of-Interest (RoI) directly from intermediate feature spaces. To optimize these modules efficiently, the gating network uses a consistency-aware generation strategy to derive deterministic routing labels, while the SD-RPN employs a fully self-supervised distillation paradigm. A continuous spatio-temporal alignment scheme and targeted fine-tuning then seamlessly fuse the dense local RoI with the coarse global layout. Extensive experiments demonstrate that Q-Zoom establishes a dominant Pareto frontier. Using Qwen2.5-VL-7B as a primary testbed, Q-Zoom accelerates inference by 2.52 times on Document & OCR benchmarks and 4.39 times in High-Resolution scenarios while matching the baseline's peak accuracy. Furthermore, when configured for maximum perceptual fidelity, Q-Zoom surpasses the baseline's peak performance by 1.1% and 8.1% on these respective benchmarks. These robust improvements transfer seamlessly to Qwen3-VL, LLaVA, and emerging RL-based thinking-with-image models. Project page is available at https://yuhengsss.github.io/Q-Zoom/.

## 5. Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation

- arXiv: `2604.06950`
- Link: https://arxiv.org/abs/2604.06950
- Announcement date: 2026-04-09
- Categories: cs.CV
- Tags: OCR robustness, adversarial attacks, text recognition, multimodal security
- Reason: Central focus on OCR robustness gaps and text recognition vulnerabilities in adversarial contexts for MLLMs.

### Abstract

Multimodal Large Language Models (MLLMs) are increasingly being deployed as automated content moderators. Within this landscape, we uncover a critical threat: Adversarial Smuggling Attacks. Unlike adversarial perturbations (for misclassification) and adversarial jailbreaks (for harmful output generation), adversarial smuggling exploits the Human-AI capability gap. It encodes harmful content into human-readable visual formats that remain AI-unreadable, thereby evading automated detection and enabling the dissemination of harmful content. We classify smuggling attacks into two pathways: (1) Perceptual Blindness, disrupting text recognition; and (2) Reasoning Blockade, inhibiting semantic understanding despite successful text recognition. To evaluate this threat, we constructed SmuggleBench, the first comprehensive benchmark comprising 1,700 adversarial smuggling attack instances. Evaluations on SmuggleBench reveal that both proprietary (e.g., GPT-5) and open-source (e.g., Qwen3-VL) state-of-the-art models are vulnerable to this threat, producing Attack Success Rates (ASR) exceeding 90%. By analyzing the vulnerability through the lenses of perception and reasoning, we identify three root causes: the limited capabilities of vision encoders, the robustness gap in OCR, and the scarcity of domain-specific adversarial examples. We conduct a preliminary exploration of mitigation strategies, investigating the potential of test-time scaling (via CoT) and adversarial training (via SFT) to mitigate this threat. Our code is publicly available at https://github.com/zhihengli-casia/smugglebench.
