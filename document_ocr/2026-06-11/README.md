# Document AI and OCR — 2026-06-11

- Papers: 6
- Skipped as duplicates: 0

## 1. A PubMed-Scale Dataset of Structured Biomedical Abstracts

- arXiv: `2606.11361`
- Link: https://arxiv.org/abs/2606.11361
- Announcement date: 2026-06-11
- Categories: cs.CL, cs.IR
- Tags: biomedical abstracts, structured parsing, information extraction
- Reason: Central task is parsing and structuring biomedical abstracts, a document parsing task.

### Abstract

Structured abstracts are important for biomedical literature processing, by facilitating information retrieval, text mining, and knowledge synthesis. However, a vast portion of abstracts indexed in PubMed remain unstructured, presenting a significant bottleneck for downstream text-processing workflows and applications. To resolve this limitation, we introduce Structured PubMed, a comprehensive corpus of section-labeled biomedical abstracts compiled from the complete PubMed database, encompassing over 23.2 million research-article records. The corpus is divided into two distinct subsets: a collection of 5.9 million author-structured abstracts parsed from official XML files, and an automatically labeled collection of 17.2 million originally unstructured abstracts structured via a verbatim-extraction Large Language Model pipeline. Every record is harmonized under a unified five-section schema and mapped to its original PubMed identifier, publication type, and publication date. This dataset can be utilized to train sentence-classification models, benchmark text-segmentation architectures, and perform large-scale, section-specific information extraction at an unprecedented PubMed-wide scale.

## 2. Towards Fully Automated Exam Grading: Fairness-Aware Recognition of Handwritten Answers with Foundation Models

- arXiv: `2606.11477`
- Link: https://arxiv.org/abs/2606.11477
- Announcement date: 2026-06-11
- Categories: cs.AI, cs.CV
- Tags: handwritten answer recognition, exam grading, VLM
- Reason: Central task is recognizing handwritten answers in exam forms, a form of OCR.

### Abstract

Correcting handwritten exams by hand is time-consuming and error-prone, particularly for large cohorts, while fully digital exams tend to force a didactic narrowing towards closed question formats. A practical middle ground keeps paper-based, problem-oriented tasks but records the assessment-relevant answers as single capital letters in a table that a machine can read. The open question is whether this reading can be made accurate and, above all, fair enough for unsupervised grading. Earlier automated approaches reached only about 88%--91% recognition -- too low -- and failed on the cases that matter most: answers placed outside the cell, crossed out, or written in cursive. We show that general-purpose vision-language foundation models (VLMs), which interpret the page rather than match pixel templates, close this gap. On a benchmark of 61 anonymised exams (3141 answer positions) the best model reaches 98.4% accuracy, well above the previous baseline. Crucially, we centre the evaluation on fairness: we distinguish false negatives (a correct answer marked wrong, which disadvantages the student) from false positives, and a lightweight prompt that supplies the reference solution as context lowers the false-negative rate to 0.58%. Under an exemplary grading scheme only three of the 61 exams would be graded worse, all caught by a student self-review step. Fully automated, fairness-aware exam grading at scale is therefore defensible; we release the anonymised benchmark to support reproducibility.

## 3. ERN-Net : Evolving Reason Node-Net for Document Binarization

- arXiv: `2606.11710`
- Link: https://arxiv.org/abs/2606.11710
- Announcement date: 2026-06-11
- Categories: cs.CV
- Tags: document binarization, document image processing
- Reason: Central task is document image binarization, a core OCR preprocessing step.

### Abstract

This paper presents ERN-Net, an Evolving Reason Node-Net for efficient document image binarization. ERN-Net enhances degradation-sensitive regions, such as faint strokes, broken characters, and noisy backgrounds, through evolving reason nodes and multi-scale reasoning. We further compare ResNet-101, ConvNeXt-Tiny, and ConvNeXt-Base, and find that ConvNeXt-Tiny provides the best practical trade-off between accuracy and memory usage. In addition, DIBCO-based pretraining improves binarization performance without increasing model memory consumption, requiring only about 1.5 additional training hours. Experiments on DIBCO-style benchmarks show that ERN-Net is effective under low-data and low-memory settings.

## 4. ParseFixer: An Agentic Framework for Document Parsing via Selective Multimodal Correction

- arXiv: `2606.11977`
- Link: https://arxiv.org/abs/2606.11977
- Announcement date: 2026-06-11
- Categories: cs.CV
- Tags: document parsing, Markdown recovery, multimodal correction
- Reason: Central task is document parsing from page images to structured Markdown.

### Abstract

In this report, we present our third-place solution for the DataMFM Challenge Track 1: Document Parsing. This track requires models to recover structured Markdown documents from document page images while preserving textual content and document structure. To address the complementary requirements of accurate content recovery and faithful structure reconstruction, we propose ParseFixer, an agentic framework for backbone parsing and selective correction. ParseFixer consists of two key modules: Full-Page Backbone Parsing (FBP) and Agentic Selective Correction (ASC). FBP produces stable initial Markdown outputs with MinerU2.5 Pro, while ASC detects high-value parsing failures and repairs them through a verify-and-rollback correction process. By placing selective multimodal correction after open-source backbone parsing, ParseFixer improves the recovery of key document elements without rewriting reliable backbone predictions. On the test set, our final system achieves an overall score of 61.78 and ranks third in Track 1, demonstrating its effectiveness for accurate document parsing. Our code will be released at: https://github.com/iLearn-Lab/CVPRW26-ParseFixer.

## 5. Holding the FP8 Quality Ceiling at 8-Bit Weights and Activations: INT8 and GGUF Post-Training Quantization of Ideogram 4.0 for Consumer GPUs

- arXiv: `2606.12280`
- Link: https://arxiv.org/abs/2606.12280
- Announcement date: 2026-06-11
- Categories: cs.LG
- Tags: OCR, document understanding
- Reason: Paper explicitly evaluates OCR text legibility preservation in quantized diffusion models, central to document AI.

### Abstract

Post-training quantization lets large text-to-image diffusion transformers run on consumer GPUs, yet the hardware-specific trade-offs are seldom measured directly. We quantize Ideogram 4.0 - a 9.3B flow-matching diffusion transformer (DiT), shipped as two separate-weight copies of a single-stream 34-layer backbone for classifier-free guidance and conditioned by a Qwen3-VL-8B encoder - for Ampere RTX 3090 GPUs, which lack FP8 tensor cores. Our INT8 W8A8 recipe (per-channel weights, per-token dynamic activations, SmoothQuant, and mixed-precision protection of a small high-fragility layer set) holds the FP8 quality ceiling: on a 200-prompt benchmark the paired same-seed bootstrap CI for INT8-FP8 includes zero on both Pick and CLIP, while INT8 improves on NF4 by $+1.9$ CLIP (95% CI $[+1.21,+2.64]$, excluding zero). A per-category OCR analysis, to our knowledge unreported for this model class, confirms text legibility is preserved, and an ablation isolates protection of the FFN down-projections as the dominant quality lever. Our GGUF Q4_K quantization beats NF4 at equal on-disk size and is the Pareto winner on the quality-memory frontier, with paired confidence intervals excluding zero (Q8_0 is quality neutral). Finally, we characterize where 8-bit quantization helps and where it does not: INT8's weights match FP8's footprint rather than shrink it, so a speed gain on Ampere awaits a fused INT8 kernel.

## 6. Doc-to-Atom: Learning to Compile and Compose Memory Atoms

- arXiv: `2606.12400`
- Link: https://arxiv.org/abs/2606.12400
- Announcement date: 2026-06-11
- Categories: cs.CL, cs.IR
- Tags: document understanding, document parsing
- Reason: Central task is document understanding via context distillation and compositional memory for long documents.

### Abstract

Long input sequences are central to document understanding and multi-step reasoning in Large Language Models, yet the quadratic cost of attention makes inference both memory-intensive and slow. Context distillation mitigates this by compressing contextual information into model parameters, and recent work such as Doc-to-LoRA amortizes context distillation into a single forward pass that generates one LoRA adapter per document. However, producing a single monolithic adapter for all queries leads to irrelevant-query interference, limited compositional recall, and poor scalability to long-document reasoning. To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms. Each atom is compiled into an independent micro-LoRA adapter and a provenance retrieval key. At inference time, a lightweight query router selects and assembles only the relevant atoms into a query-specific adapter, which is then injected into a frozen base model. The entire system is trained end-to-end through a multi-objective distillation framework. Experiments on six diverse QA benchmarks demonstrate that Doc2Atom outperforms Doc-to-LoRA baselines while reducing the memory cost of document internalization.
