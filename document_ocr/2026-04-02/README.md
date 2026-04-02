# Document AI and OCR — 2026-04-02

- Papers: 5
- Skipped as duplicates: 0

## 1. A Reliability Evaluation of Hybrid Deterministic-LLM Based Approaches for Academic Course Registration PDF Information Extraction

- arXiv: `2604.00003`
- Link: https://arxiv.org/abs/2604.00003
- Announcement date: 2026-04-02
- Categories: cs.AI, cs.CL, cs.IR
- Tags: information extraction, PDF parsing, table understanding
- Reason: Central task is information extraction from academic PDF documents (KRS documents) with tables and metadata, directly targeting document parsing and structured content extraction.

### Abstract

This study evaluates the reliability of information extraction approaches from KRS documents using three strategies: LLM only, Hybrid Deterministic - LLM (regex + LLM), and a Camelot based pipeline with LLM fallback. Experiments were conducted on 140 documents for the LLM based test and 860 documents for the Camelot based pipeline evaluation, covering four study programs with varying data in tables and metadata. Three 12 - 14B LLM models (Gemma 3, Phi 4, and Qwen 2.5) were run locally using Ollama and a consumer grade CPU without a GPU. Evaluations used exact match (EM) and Levenshtein similarity (LS) metrics with a threshold of 0.7. Although not applicable to all models, the results show that the hybrid approach can improve efficiency compared to LLM only, especially for deterministic metadata. The Camelot based pipeline with LLM fallback produced the best combination of accuracy (EM and LS up to 0.99 - 1.00) and computational efficiency (less than 1 second per PDF in most cases). The Qwen 2.5:14b model demonstrated the most consistent performance across all scenarios. These findings confirm that integrating deterministic and LLM methods is increasingly reliable and efficient for information extraction from text based academic documents in computationally constrained environments.

## 2. Q-Mask: Query-driven Causal Masks for Text Anchoring in OCR-Oriented Vision-Language Models

- arXiv: `2604.00161`
- Link: https://arxiv.org/abs/2604.00161
- Announcement date: 2026-04-02
- Categories: cs.CV
- Tags: OCR, text anchoring, vision-language models, benchmark
- Reason: Explicitly targets OCR as a foundational capability, introduces a new OCR framework (Q-Mask) for text-region grounding, and includes a benchmark for text anchoring. Central contribution is in OCR and document understanding.

### Abstract

Optical Character Recognition (OCR) is increasingly regarded as a foundational capability for modern vision-language models (VLMs), enabling them not only to read text in images but also to support downstream reasoning in real-world visual question answering (VQA). However, practical applications further require reliable text anchors, i.e., accurately grounding queried text to its corresponding spatial region. To systematically evaluate this capability, we introduce TextAnchor-Bench (TABench), a benchmark for fine-grained text-region grounding, which reveals that both general-purpose and OCR-specific VLMs still struggle to establish accurate and stable text anchors. To address this limitation, we propose Q-Mask, a precise OCR framework built upon a causal query-driven mask decoder (CQMD). Inspired by chain-of-thought reasoning, Q-Mask performs causal visual decoding that sequentially generates query-conditioned visual masks before producing the final OCR output. This visual CoT paradigm disentangles where the text is from what the text is, enforcing grounded evidence acquisition prior to recognition and enabling explicit text anchor construction during inference. To train CQMD, we construct TextAnchor-26M, a large-scale dataset of image-text pairs annotated with fine-grained masks corresponding to specific textual elements, encouraging stable text-region correspondences and injecting strong spatial priors into VLM training. Extensive experiments demonstrate that Q-Mask substantially improves text anchoring and understanding across diverse visual scenes.

## 3. OmniSch: A Multimodal PCB Schematic Benchmark For Structured Diagram Visual Reasoning

- arXiv: `2604.00270`
- Link: https://arxiv.org/abs/2604.00270
- Announcement date: 2026-04-02
- Categories: cs.CV
- Tags: diagram understanding, PCB schematics, visual reasoning, parsing
- Reason: Targets structured diagram visual reasoning for PCB schematics, involving parsing into machine-readable graphs. This aligns with diagram parsing and document understanding, though it's engineering-focused; the core contribution is in parsing visual documents.

### Abstract

Recent large multimodal models (LMMs) have made rapid progress in visual grounding, document understanding, and diagram reasoning tasks. However, their ability to convert Printed Circuit Board (PCB) schematic diagrams into machine-readable spatially weighted netlist graphs, jointly capturing component attributes, connectivity, and geometry, remains largely underexplored, despite such graph representations are the backbone of practical electronic design automation (EDA) workflows. To bridge this gap, we introduce OmniSch, the first comprehensive benchmark designed to assess LMMs on schematic understanding and spatial netlist graph construction. OmniSch contains 1,854 real-world schematic diagrams and includes four tasks: (1) visual grounding for schematic entities, with 109.9K grounded instances aligning 423.4K diagram semantic labels to their visual regions; (2) diagram-to-graph reasoning, understanding topological relationship among diagram elements; (3) geometric reasoning, constructing layout-dependent weights for each connection; and (4) tool-augmented agentic reasoning for visual search, invoking external tools to accomplish (1)-(3). Our results reveal substantial gaps of current LMMs in interpreting schematic engineering artifacts, including unreliable fine-grained grounding, brittle layout-to-graph parsing, inconsistent global connectivity reasoning and inefficient visual exploration.

## 4. A Benchmark of State-Space Models vs. Transformers and BiLSTM-based Models for Historical Newspaper OCR

- arXiv: `2604.00725`
- Link: https://arxiv.org/abs/2604.00725
- Announcement date: 2026-04-02
- Categories: cs.CV, cs.LG
- Tags: OCR, historical newspapers, state-space models, benchmark
- Reason: Central task is OCR for historical newspapers, comparing models for text recognition. Directly targets OCR with a focus on degraded print and complex layouts, fitting document AI inclusion rules.

### Abstract

End-to-end OCR for historical newspapers remains challenging, as models must handle long text sequences, degraded print quality, and complex layouts. While Transformer-based recognizers dominate current research, their quadratic complexity limits efficient paragraph-level transcription and large-scale deployment. We investigate linear-time State-Space Models (SSMs), specifically Mamba, as a scalable alternative to Transformer-based sequence modeling for OCR. We present to our knowledge, the first OCR architecture based on SSMs, combining a CNN visual encoder with bi-directional and autoregressive Mamba sequence modeling, and conduct a large-scale benchmark comparing SSMs with Transformer- and BiLSTM-based recognizers. Multiple decoding strategies (CTC, autoregressive, and non-autoregressive) are evaluated under identical training conditions alongside strong neural baselines (VAN, DAN, DANIEL) and widely used off-the-shelf OCR engines (PERO-OCR, Tesseract OCR, TrOCR, Gemini). Experiments on historical newspapers from the Biblioth\`eque nationale du Luxembourg, with newly released >99% verified gold-standard annotations, and cross-dataset tests on Fraktur and Antiqua lines, show that all neural models achieve low error rates (~2% CER), making computational efficiency the main differentiator. Mamba-based models maintain competitive accuracy while halving inference time and exhibiting superior memory scaling (1.26x vs 2.30x growth at 1000 chars), reaching 6.07% CER at the severely degraded paragraph level compared to 5.24% for DAN, while remaining 2.05x faster. We release code, trained models, and standardized evaluation protocols to enable reproducible research and guide practitioners in large-scale cultural heritage OCR.

## 5. PixelPrune: Pixel-Level Adaptive Visual Token Reduction via Predictive Coding

- arXiv: `2604.00886`
- Link: https://arxiv.org/abs/2604.00886
- Announcement date: 2026-04-02
- Categories: cs.AI, cs.CL, cs.CV
- Tags: document understanding, efficiency optimization, visual token reduction
- Reason: Paper explicitly targets document understanding applications, proposes method to accelerate document/GUI processing by pruning redundant patches, and benchmarks on document tasks.

### Abstract

Document understanding and GUI interaction are among the highest-value applications of Vision-Language Models (VLMs), yet they impose exceptionally heavy computational burden: fine-grained text and small UI elements demand high-resolution inputs that produce tens of thousands of visual tokens. We observe that this cost is largely wasteful -- across document and GUI benchmarks, only 22--71\% of image patches are pixel-unique, the rest being exact duplicates of another patch in the same image. We propose \textbf{PixelPrune}, which exploits this pixel-level redundancy through predictive-coding-based compression, pruning redundant patches \emph{before} the Vision Transformer (ViT) encoder. Because it operates in pixel space prior to any neural computation, PixelPrune accelerates both the ViT encoder and the downstream LLM, covering the full inference pipeline. The method is training-free, requires no learnable parameters, and supports pixel-lossless compression ($\tau{=}0$) as well as controlled lossy compression ($\tau{>}0$). Experiments across three model scales and document and GUI benchmarks show that PixelPrune maintains competitive task accuracy while delivering up to 4.2$\times$ inference speedup and 1.9$\times$ training acceleration. Code is available at https://github.com/OPPO-Mente-Lab/PixelPrune.
