# Document AI and OCR — 2026-03-31

- Papers: 14
- Skipped as duplicates: 0

## 1. LITTA: Late-Interaction and Test-Time Alignment for Visually-Grounded Multimodal Retrieval

- arXiv: `2603.26683`
- Link: https://arxiv.org/abs/2603.26683
- Announcement date: 2026-03-31
- Categories: cs.AI, cs.CL, cs.CV, cs.IR
- Tags: multimodal retrieval, visually rich documents, layout
- Reason: Core contribution is retrieval from visually rich documents with complex layouts.

### Abstract

Retrieving relevant evidence from visually rich documents such as textbooks, technical reports, and manuals is challenging due to long context, complex layouts, and weak lexical overlap between user questions and supporting pages. We propose LITTA, a query-expansion-centric retrieval framework for evidence page retrieval that improves multimodal document retrieval without retriever retraining. Given a user query, LITTA generates complementary query variants using a large language model and retrieves candidate pages for each variant using a frozen vision retriever with late-interaction scoring. Candidates from expanded queries are then aggregated through reciprocal rank fusion to improve evidence coverage and reduce sensitivity to any single phrasing. This simple test-time strategy significantly improves retrieval robustness while remaining compatible with existing multimodal embedding indices. We evaluate LITTA on visually grounded document retrieval tasks across three domains: computer science, pharmaceuticals, and industrial manuals. Multi-query retrieval consistently improves top-k accuracy, recall, and MRR compared to single-query retrieval, with particularly large gains in domains with high visual and semantic variability. Moreover, the accuracy-efficiency trade-off is directly controllable by the number of query variants, making LITTA practical for deployment under latency constraints. These results demonstrate that query expansion provides a simple yet effective mechanism for improving visually grounded multimodal retrieval.

## 2. Aesthetic Assessment of Chinese Handwritings Based on Vision Language Models

- arXiv: `2603.26768`
- Link: https://arxiv.org/abs/2603.26768
- Announcement date: 2026-03-31
- Categories: cs.AI, cs.CL, cs.CV
- Tags: handwritten text, Chinese characters, aesthetic assessment
- Reason: Central task is assessment of handwritten Chinese characters, a form of handwritten text recognition.

### Abstract

The handwriting of Chinese characters is a fundamental aspect of learning the Chinese language. Previous automated assessment methods often framed scoring as a regression problem. However, this score-only feedback lacks actionable guidance, which limits its effectiveness in helping learners improve their handwriting skills. In this paper, we leverage vision-language models (VLMs) to analyze the quality of handwritten Chinese characters and generate multi-level feedback. Specifically, we investigate two feedback generation tasks: simple grade feedback (Task 1) and enriched, descriptive feedback (Task 2). We explore both low-rank adaptation (LoRA)-based fine-tuning strategies and in-context learning methods to integrate aesthetic assessment knowledge into VLMs. Experimental results show that our approach achieves state-of-the-art performances across multiple evaluation tracks in the CCL 2025 workshop on evaluation of handwritten Chinese character quality.

## 3. HighlightBench: Benchmarking Markup-Driven Table Reasoning in Scientific Documents

- arXiv: `2603.26784`
- Link: https://arxiv.org/abs/2603.26784
- Announcement date: 2026-03-31
- Categories: cs.CV
- Tags: table understanding, document understanding, scientific documents, benchmark
- Reason: Explicitly targets markup-driven table understanding in scientific documents.

### Abstract

Visual markups such as highlights, underlines, and bold text are common in table-centric documents. Although multimodal large language models (MLLMs) have made substantial progress in document understanding, their ability to treat such cues as explicit logical directives remains under-explored. More importantly, existing evaluations cannot distinguish whether a model fails to see the markup or fails to reason with it. This creates a key blind spot in assessing markup-conditioned behavior over tables. To address this gap, we introduce HighlightBench, a diagnostic benchmark for markup-driven table understanding that decomposes evaluation into five task families: Markup Grounding, Constrained Retrieval, Local Relations, Aggregation \& Comparison, and Consistency \& Missingness. We further provide a reference pipeline that makes intermediate decisions explicit, enabling reproducible baselines and finer-grained attribution of errors along the perception-to-execution chain. Experiments show that even strong models remain unstable when visual cues must be consistently aligned with symbolic reasoning under structured output constraints.

## 4. Story2Proposal: A Scaffold for Structured Scientific Paper Writing

- arXiv: `2603.27065`
- Link: https://arxiv.org/abs/2603.27065
- Announcement date: 2026-03-31
- Categories: cs.CL
- Tags: scientific paper writing, structured generation, document generation
- Reason: Targets structured scientific manuscript generation, a form of document generation/derendering.

### Abstract

Generating scientific manuscripts requires maintaining alignment between narrative reasoning, experimental evidence, and visual artifacts across the document lifecycle. Existing language-model generation pipelines rely on unconstrained text synthesis with validation applied only after generation, often producing structural drift, missing figures or tables, and cross-section inconsistencies. We introduce Story2Proposal, a contract-governed multi-agent framework that converts a research story into a structured manuscript through coordinated agents operating under a persistent shared visual contract. The system organizes architect, writer, refiner, and renderer agents around a contract state that tracks section structure and registered visual elements, while evaluation agents supply feedback in a generate evaluate adapt loop that updates the contract during generation. Experiments on tasks derived from the Jericho research corpus show that Story2Proposal achieved an expert evaluation score of 6.145 versus 3.963 for DirectChat (+2.182) across GPT, Claude, Gemini, and Qwen backbones. Compared with the structured generation baseline Fars, Story2Proposal obtained an average score of 5.705 versus 5.197, indicating improved structural consistency and visual alignment.

## 5. EuraGovExam: A Multilingual Multimodal Benchmark from Real-World Civil Service Exams

- arXiv: `2603.27223`
- Link: https://arxiv.org/abs/2603.27223
- Announcement date: 2026-03-31
- Categories: cs.AI, cs.CV
- Tags: multimodal benchmark, document images, layout, table, form
- Reason: Benchmark from real exam documents with visual structures like tables and forms; requires layout-aware reasoning.

### Abstract

We present EuraGovExam, a multilingual and multimodal benchmark sourced from real-world civil service examinations across five representative Eurasian regions: South Korea, Japan, Taiwan, India, and the European Union. Designed to reflect the authentic complexity of public-sector assessments, the dataset contains over 8,000 high-resolution scanned multiple-choice questions covering 17 diverse academic and administrative domains. Unlike existing benchmarks, EuraGovExam embeds all question content--including problem statements, answer choices, and visual elements--within a single image, providing only a minimal standardized instruction for answer formatting. This design demands that models perform layout-aware, cross-lingual reasoning directly from visual input. All items are drawn from real exam documents, preserving rich visual structures such as tables, multilingual typography, and form-like layouts. Evaluation results show that even state-of-the-art vision-language models (VLMs) achieve only 86% accuracy, underscoring the benchmark's difficulty and its power to diagnose the limitations of current models. By emphasizing cultural realism, visual complexity, and linguistic diversity, EuraGovExam establishes a new standard for evaluating VLMs in high-stakes, multilingual, image-grounded settings. It also supports practical applications in e-governance, public-sector document analysis, and equitable exam preparation.

## 6. Falcon Perception

- arXiv: `2603.27365`
- Link: https://arxiv.org/abs/2603.27365
- Announcement date: 2026-03-31
- Categories: cs.CV
- Tags: OCR, document understanding, benchmark
- Reason: Central contribution includes Falcon OCR model and evaluation on OCR/document benchmarks; explicitly targets OCR as core task.

### Abstract

Perception-centric systems are typically implemented with a modular encoder-decoder pipeline: a vision backbone for feature extraction and a separate decoder (or late-fusion module) for task prediction. This raises a central question: is this architectural separation essential or can a single early-fusion stack do both perception and task modeling at scale? We introduce Falcon Perception, a unified dense Transformer that processes image patches and text tokens in a shared parameter space from the first layer, using a hybrid attention pattern (bidirectional among image tokens, causal for prediction tokens) to combine global visual context with autoregressive, variable-length instance generation. To keep dense outputs practical, Falcon Perception retains a lightweight token interface and decodes continuous spatial outputs with specialized heads, enabling parallel high-resolution mask prediction. Our design promotes simplicity: we keep a single scalable backbone and shift complexity toward data and training signals, adding only small heads where outputs are continuous and dense. On SA-Co, Falcon Perception improves mask quality to 68.0 Macro-F$_1$ compared to 62.3 of SAM3. We also introduce PBench, a benchmark targeting compositional prompts (OCR, spatial constraints, relations) and dense long-context regimes, where the model shows better gains. Finally, we extend the same early-fusion recipe to Falcon OCR: a compact 300M-parameter model which attains 80.3% on olmOCR and 88.64 on OmniDocBench.

## 7. Data Organization Matters in Multimodal Instruction Tuning: A Controlled Study of Capability Trade-offs

- arXiv: `2603.27744`
- Link: https://arxiv.org/abs/2603.27744
- Announcement date: 2026-03-31
- Categories: cs.CV
- Tags: multimodal, OCR, document understanding, instruction tuning
- Reason: Explicitly studies OCR/document understanding as core capability in multimodal models; includes document QA and scene-text tasks.

### Abstract

Recent multimodal large language models (MLLMs) perform strongly on general visual understanding, diagram and chart reasoning, and document-centric perception. However, these abilities are learned from heterogeneous supervision sources with very different task structures and learning demands, and the effect of their temporal organization during training remains underexplored. We study whether data organization affects the trade-off among general understanding, structured reasoning, and fine-grained OCR/document understanding in multimodal instruction tuning. To isolate this factor, we use a controlled three-stage training framework in which the backbone, trainable modules, and optimization pipeline are fixed across all runs, and only the temporal arrangement of post-alignment supervision is changed. We compare four strategies: direct mixture, curriculum training, balanced sampling, and reverse curriculum. Experiments on general visual instruction following, diagram reasoning, chart reasoning, scene-text question answering, and document question answering show that data organization is a first-order design variable in multimodal adaptation. Curriculum training gives the best overall trade-off and the strongest structured reasoning performance. Balanced sampling is better for OCR-oriented capability but weakens the broader capability balance. Reverse curriculum performs worst in both final performance and optimization stability. Training-dynamics analysis further suggests that building general understanding and reasoning before introducing OCR-intensive supervision leads to smoother optimization and faster convergence. These findings highlight data scheduling as an explicit design dimension for multimodal model adaptation.

## 8. JaWildText: A Benchmark for Vision-Language Models on Japanese Scene Text Understanding

- arXiv: `2603.27942`
- Link: https://arxiv.org/abs/2603.27942
- Announcement date: 2026-03-31
- Categories: cs.AI, cs.CV
- Tags: scene text, benchmark, Japanese text, receipt KIE, handwriting OCR
- Reason: Explicitly targets Japanese scene text understanding with tasks including receipt KIE and handwriting OCR, central to document AI/OCR.

### Abstract

Japanese scene text poses challenges that multilingual benchmarks often fail to capture, including mixed scripts, frequent vertical writing, and a character inventory far larger than the Latin alphabet. Although Japanese is included in several multilingual benchmarks, these resources do not adequately capture the language-specific complexities. Meanwhile, existing Japanese visual text datasets have primarily focused on scanned documents, leaving in-the-wild scene text underexplored. To fill this gap, we introduce JaWildText, a diagnostic benchmark for evaluating vision-language models (VLMs) on Japanese scene text understanding. JaWildText contains 3,241 instances from 2,961 images newly captured in Japan, with 1.12 million annotated characters spanning 3,643 unique character types. It comprises three complementary tasks that vary in visual organization, output format, and writing style: (i) Dense Scene Text Visual Question Answering (STVQA), which requires reasoning over multiple pieces of visual text evidence; (ii) Receipt Key Information Extraction (KIE), which tests layout-aware structured extraction from mobile-captured receipts; and (iii) Handwriting OCR, which evaluates page-level transcription across various media and writing directions. We evaluate 14 open-weight VLMs and find that the best model achieves an average score of 0.64 across the three tasks. Error analyses show recognition remains the dominant bottleneck, especially for kanji. JaWildText enables fine-grained, script-aware diagnosis of Japanese scene text capabilities, and will be released with evaluation code.

## 9. Efficient Domain Adaptation for Text Line Recognition via Decoupled Language Models

- arXiv: `2603.28028`
- Link: https://arxiv.org/abs/2603.28028
- Announcement date: 2026-03-31
- Categories: cs.CV, cs.LG
- Tags: OCR, text line recognition, domain adaptation, historical documents
- Reason: Explicitly addresses optical character recognition for document digitization, with evaluation on historical documents.

### Abstract

Optical character recognition remains critical infrastructure for document digitization, yet state-of-the-art performance is often restricted to well-resourced institutions by prohibitive computational barriers. End-to-end transformer architectures achieve strong accuracy but demand hundreds of GPU hours for domain adaptation, limiting accessibility for practitioners and digital humanities scholars. We present a modular detection-and-correction framework that achieves near-SOTA accuracy with single-GPU training. Our approach decouples lightweight visual character detection (domain-agnostic) from domain-specific linguistic correction using pretrained sequence models including T5, ByT5, and BART. By training the correctors entirely on synthetic noise, we enable annotation-free domain adaptation without requiring labeled target images. Evaluating across modern clean handwriting, cursive script, and historical documents, we identify a critical "Pareto frontier" in architecture selection: T5-Base excels on modern text with standard vocabulary, whereas ByT5-Base dominates on historical documents by reconstructing archaic spellings at the byte level. Our results demonstrate that this decoupled paradigm matches end-to-end transformer accuracy while reducing compute by approximately 95%, establishing a viable, resource-efficient alternative to monolithic OCR architectures.

## 10. Transcription and Recognition of Italian Parliamentary Speeches Using Vision-Language Models

- arXiv: `2603.28103`
- Link: https://arxiv.org/abs/2603.28103
- Announcement date: 2026-03-31
- Categories: cs.AI, cs.DL, cs.IR
- Tags: OCR, parliamentary speeches, transcription, layout, entity linking
- Reason: Central task is OCR and transcription of scanned parliamentary documents with layout preservation and semantic annotation.

### Abstract

Parliamentary proceedings represent a rich yet challenging resource for computational analysis, particularly when preserved only as scanned historical documents. Existing efforts to transcribe Italian parliamentary speeches have relied on traditional Optical Character Recognition pipelines, resulting in transcription errors and limited semantic annotation. In this paper, we propose a pipeline based on Vision-Language Models for the automatic transcription, semantic segmentation, and entity linking of Italian parliamentary speeches. The pipeline employs a specialised OCR model to extract text while preserving reading order, followed by a large-scale Vision-Language Model that performs transcription refinement, element classification, and speaker identification by jointly reasoning over visual layout and textual content. Extracted speakers are then linked to the Chamber of Deputies knowledge base through SPARQL queries and a multi-strategy fuzzy matching procedure. Evaluation against an established benchmark demonstrates substantial improvements both in transcription quality and speaker tagging.

## 11. Quid est VERITAS? A Modular Framework for Archival Document Analysis

- arXiv: `2603.28108`
- Link: https://arxiv.org/abs/2603.28108
- Announcement date: 2026-03-31
- Categories: cs.AI, cs.DL, cs.IR
- Tags: OCR, layout analysis, historical documents, digitization pipeline
- Reason: Explicitly targets archival document analysis with integrated workflow for transcription, layout analysis, and semantic enrichment.

### Abstract

The digitisation of historical documents has traditionally been conceived as a process limited to character-level transcription, producing flat text that lacks the structural and semantic information necessary for substantive computational analysis. We present VERITAS (Vision-Enhanced Reading, Interpretation, and Transcription of Archival Sources), a modular, model-agnostic framework that reconceptualises digitisation as an integrated workflow encompassing transcription, layout analysis, and semantic enrichment. The pipeline is organised into four stages - Preprocessing, Extraction, Refinement, and Enrichment - and employs a schema-driven architecture that allows researchers to declaratively specify their extraction objectives. We evaluate VERITAS on the critical edition of Bernardino Corio's Storia di Milano, a Renaissance chronicle of over 1,600 pages. Results demonstrate that the pipeline achieves a 67.6% relative reduction in word error rate compared to a commercial OCR baseline, with a threefold reduction in end-to-end processing time when accounting for manual correction. We further illustrate the downstream utility of the pipeline's output by querying the transcribed corpus through a retrieval-augmented generation system, demonstrating its capacity to support historical inquiry.

## 12. MDPBench: A Benchmark for Multilingual Document Parsing in Real-World Scenarios

- arXiv: `2603.28130`
- Link: https://arxiv.org/abs/2603.28130
- Announcement date: 2026-03-31
- Categories: cs.AI, cs.CV
- Tags: document parsing, multilingual, benchmark, OCR
- Reason: Explicitly introduces benchmark for multilingual document parsing, directly central to document AI evaluation.

### Abstract

We introduce Multilingual Document Parsing Benchmark, the first benchmark for multilingual digital and photographed document parsing. Document parsing has made remarkable strides, yet almost exclusively on clean, digital, well-formatted pages in a handful of dominant languages. No systematic benchmark exists to evaluate how models perform on digital and photographed documents across diverse scripts and low-resource languages. MDPBench comprises 3,400 document images spanning 17 languages, diverse scripts, and varied photographic conditions, with high-quality annotations produced through a rigorous pipeline of expert model labeling, manual correction, and human verification. To ensure fair comparison and prevent data leakage, we maintain separate public and private evaluation splits. Our comprehensive evaluation of both open-source and closed-source models uncovers a striking finding: while closed-source models (notably Gemini3-Pro) prove relatively robust, open-source alternatives suffer dramatic performance collapse, particularly on non-Latin scripts and real-world photographed documents, with an average drop of 17.8% on photographed documents and 14.0% on non-Latin scripts. These results reveal significant performance imbalances across languages and conditions, and point to concrete directions for building more inclusive, deployment-ready parsing systems. Source available at https://github.com/Yuliang-Liu/MultimodalOCR.

## 13. MarkushGrapher-2: End-to-end Multimodal Recognition of Chemical Structures

- arXiv: `2603.28550`
- Link: https://arxiv.org/abs/2603.28550
- Announcement date: 2026-03-31
- Categories: cs.CV
- Tags: OCR, document parsing, chemical structure recognition, multimodal document understanding
- Reason: Central task is multimodal recognition of chemical structures from documents using dedicated OCR model and layout analysis, directly targeting document parsing and structured content extraction.

### Abstract

Automatically extracting chemical structures from documents is essential for the large-scale analysis of the literature in chemistry. Automatic pipelines have been developed to recognize molecules represented either in figures or in text independently. However, methods for recognizing chemical structures from multimodal descriptions (Markush structures) lag behind in precision and cannot be used for automatic large-scale processing. In this work, we present MarkushGrapher-2, an end-to-end approach for the multimodal recognition of chemical structures in documents. First, our method employs a dedicated OCR model to extract text from chemical images. Second, the text, image, and layout information are jointly encoded through a Vision-Text-Layout encoder and an Optical Chemical Structure Recognition vision encoder. Finally, the resulting encodings are effectively fused through a two-stage training strategy and used to auto-regressively generate a representation of the Markush structure. To address the lack of training data, we introduce an automatic pipeline for constructing a large-scale dataset of real-world Markush structures. In addition, we present IP5-M, a large manually-annotated benchmark of real-world Markush structures, designed to advance research on this challenging task. Extensive experiments show that our approach substantially outperforms state-of-the-art models in multimodal Markush structure recognition, while maintaining strong performance in molecule structure recognition. Code, models, and datasets are released publicly.

## 14. Navigating the Mirage: A Dual-Path Agentic Framework for Robust Misleading Chart Question Answering

- arXiv: `2603.28583`
- Link: https://arxiv.org/abs/2603.28583
- Announcement date: 2026-03-31
- Categories: cs.AI, cs.CV, cs.MM
- Tags: OCR, chart understanding, document VQA, visual document reasoning
- Reason: Core contribution is OCR-driven data path for chart question answering with explicit OCR component, targeting document-like chart interpretation and structured content extraction.

### Abstract

Despite the success of Vision-Language Models (VLMs), misleading charts remain a significant challenge due to their deceptive visual structures and distorted data representations. We present ChartCynics, an agentic dual-path framework designed to unmask visual deception via a "skeptical" reasoning paradigm. Unlike holistic models, ChartCynics decouples perception from verification: a Diagnostic Vision Path captures structural anomalies (e.g., inverted axes) through strategic ROI cropping, while an OCR-Driven Data Path ensures numerical grounding. To resolve cross-modal conflicts, we introduce an Agentic Summarizer optimized via a two-stage protocol: Oracle-Informed SFT for reasoning distillation and Deception-Aware GRPO for adversarial alignment. This pipeline effectively penalizes visual traps and enforces logical consistency. Evaluations on two benchmarks show that ChartCynics achieves 74.43% and 64.55% accuracy, providing an absolute performance boost of ~29% over the Qwen3-VL-8B backbone, outperforming state-of-the-art proprietary models. Our results demonstrate that specialized agentic workflows can grant smaller open-source models superior robustness, establishing a new foundation for trustworthy chart interpretation.
