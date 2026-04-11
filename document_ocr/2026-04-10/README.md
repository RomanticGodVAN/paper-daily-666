# Document AI and OCR — 2026-04-10

- Papers: 5
- Skipped as duplicates: 0

## 1. Symbiotic-MoE: Unlocking the Synergy between Generation and Understanding

- arXiv: `2604.07753`
- Link: https://arxiv.org/abs/2604.07753
- Announcement date: 2026-04-10
- Categories: cs.CL, cs.CV, cs.LG
- Tags: multimodal MoE, generation-understanding synergy, OCRBench, LMM
- Reason: Multimodal MoE framework evaluated on OCRBench, indicating OCR/document understanding as a core task. Central to document AI research.

### Abstract

Empowering Large Multimodal Models (LMMs) with image generation often leads to catastrophic forgetting in understanding tasks due to severe gradient conflicts. While existing paradigms like Mixture-of-Transformers (MoT) mitigate this conflict through structural isolation, they fundamentally sever cross-modal synergy and suffer from capacity fragmentation. In this work, we present Symbiotic-MoE, a unified pre-training framework that resolves task interference within a native multimodal Mixture-of-Experts (MoE) Transformers architecture with zero-parameter overhead. We first identify that standard MoE tuning leads to routing collapse, where generative gradients dominate expert utilization. To address this, we introduce Modality-Aware Expert Disentanglement, which partitions experts into task-specific groups while utilizing shared experts as a multimodal semantic bridge. Crucially, this design allows shared experts to absorb fine-grained visual semantics from generative tasks to enrich textual representations. To optimize this, we propose a Progressive Training Strategy featuring differential learning rates and early-stage gradient shielding. This mechanism not only shields pre-trained knowledge from early volatility but eventually transforms generative signals into constructive feedback for understanding. Extensive experiments demonstrate that Symbiotic-MoE achieves rapid generative convergence while unlocking cross-modal synergy, boosting inherent understanding with remarkable gains on MMLU and OCRBench.

## 2. Automatic Generation of Executable BPMN Models from Medical Guidelines

- arXiv: `2604.07817`
- Link: https://arxiv.org/abs/2604.07817
- Announcement date: 2026-04-10
- Categories: cs.AI, cs.LG, cs.SE
- Tags: medical guidelines, document parsing, BPMN generation, LLM
- Reason: End-to-end pipeline converting healthcare policy documents into executable models. Central task is document parsing and structured extraction.

### Abstract

We present an end-to-end pipeline that converts healthcare policy documents into executable, data-aware Business Process Model and Notation (BPMN) models using large language models (LLMs) for simulation-based policy evaluation. We address the main challenges of automated policy digitization with four contributions: data-grounded BPMN generation with syntax auto-correction, executable augmentation, KPI instrumentation, and entropy-based uncertainty detection. We evaluate the pipeline on diabetic nephropathy prevention guidelines from three Japanese municipalities, generating 100 models per backend across three LLMs and executing each against 1,000 synthetic patients. On well-structured policies, the pipeline achieves a 100% ground-truth match with perfect per-patient decision agreement. Across all conditions, raw per-patient decision agreement exceeds 92%, and entropy scores increase monotonically with document complexity, confirming that the detector reliably separates unambiguous policies from those requiring targeted human clarification.

## 3. AtlasOCR: Building the First Open-Source Darija OCR Model with Vision Language Models

- arXiv: `2604.08070`
- Link: https://arxiv.org/abs/2604.08070
- Announcement date: 2026-04-10
- Categories: cs.AI, cs.CV
- Tags: OCR, Darija, vision language models, text recognition
- Reason: Central task is building an OCR model for Darija using VLMs, directly targeting optical character recognition.

### Abstract

Darija, the Moroccan Arabic dialect, is rich in visual content yet lacks specialized Optical Character Recognition (OCR) tools. This paper introduces AtlasOCR, the first open-source Darija OCR model built by fine-tuning a 3B parameter Vision Language Model (VLM). We detail our comprehensive approach, from curating a unique Darija-specific dataset leveraging both synthetic generation with our OCRSmith library and carefully sourced real-world data, to implementing efficient fine-tuning strategies. We utilize QLoRA and Unsloth for parameter-efficient training of Qwen2.5-VL 3B and present comprehensive ablation studies optimizing key hyperparameters. Our evaluation on the newly curated AtlasOCRBench and the established KITAB-Bench demonstrates state-of-the-art performance, challenging larger models and highlighting AtlasOCR's robustness and generalization capabilities for both Darija and standard Arabic OCR tasks.

## 4. Revise: A Framework for Revising OCRed text in Practical Information Systems with Data Contamination Strategy

- arXiv: `2604.08115`
- Link: https://arxiv.org/abs/2604.08115
- Announcement date: 2026-04-10
- Categories: cs.AI
- Tags: OCR correction, document understanding, Document AI, error correction
- Reason: Explicitly targets OCR error correction for document understanding and management, core Document AI contribution.

### Abstract

Recent advances in Large Language Models (LLMs) have significantly improved the field of Document AI, demonstrating remarkable performance on document understanding tasks such as question answering. However, existing approaches primarily focus on solving specific tasks, lacking the capability to structurally organize and manage document information. To address this limitation, we propose Revise, a framework that systematically corrects errors introduced by OCR at the character, word, and structural levels. Specifically, Revise employs a comprehensive hierarchical taxonomy of common OCR errors and a synthetic data generation strategy that realistically simulates such errors to train an effective correction model. Experimental results demonstrate that Revise effectively corrects OCR outputs, enabling more structured representation and systematic management of document contents. Consequently, our method significantly enhances downstream performance in document retrieval and question answering tasks, highlighting the potential to overcome the structural management limitations of existing Document AI frameworks.

## 5. ParseBench: A Document Parsing Benchmark for AI Agents

- arXiv: `2604.08538`
- Link: https://arxiv.org/abs/2604.08538
- Announcement date: 2026-04-10
- Categories: cs.CV
- Tags: document parsing, benchmark, tables, charts, semantic correctness
- Reason: Explicitly introduces a document parsing benchmark for AI agents, targeting semantic correctness in enterprise documents - core document AI contribution.

### Abstract

AI agents are changing the requirements for document parsing. What matters is \emph{semantic correctness}: parsed output must preserve the structure and meaning needed for autonomous decisions, including correct table structure, precise chart data, semantically meaningful formatting, and visual grounding. Existing benchmarks do not fully capture this setting for enterprise automation, relying on narrow document distributions and text-similarity metrics that miss agent-critical failures. We introduce \textbf{ParseBench}, a benchmark of ${\sim}2{,}000$ human-verified pages from enterprise documents spanning insurance, finance, and government, organized around five capability dimensions: tables, charts, content faithfulness, semantic formatting, and visual grounding. Across 14 methods spanning vision-language models, specialized document parsers, and LlamaParse, the benchmark reveals a fragmented capability landscape: no method is consistently strong across all five dimensions. LlamaParse Agentic achieves the highest overall score at \agenticoverall\%, and the benchmark highlights the remaining capability gaps across current systems. Dataset and evaluation code are available on \href{https://huggingface.co/datasets/llamaindex/ParseBench}{HuggingFace} and \href{https://github.com/run-llama/ParseBench}{GitHub}.
