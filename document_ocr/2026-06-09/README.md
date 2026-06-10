# Document AI and OCR — 2026-06-09

- Papers: 17
- Skipped as duplicates: 0

## 1. PulseBench-Tab: A Multilingual Benchmark for Table Extraction with Graph-Based Evaluation

- arXiv: `2606.07534`
- Link: https://arxiv.org/abs/2606.07534
- Announcement date: 2026-06-09
- Categories: cs.CL, cs.IR
- Tags: table extraction, benchmark, document image
- Reason: Central task is table extraction from document images; includes multilingual benchmark and evaluation metric.

### Abstract

We introduce PulseBench-Tab, an open multilingual benchmark for evaluating table extraction from document images. The benchmark comprises 1,820 human-annotated tables spanning 9 languages and 4 scripts (Latin, CJK, Arabic, Cyrillic), drawn from 380 real-world source documents including financial filings, government reports, and regulatory disclosures. Tables range from 2 to 1,183 cells, with 48.1% containing merged or spanning cells. Alongside the dataset, we propose T-LAG (Table Logical Adjacency Graph), a novel evaluation metric that models tables as directed graphs over cell adjacencies and computes structural and content fidelity in a single score via optimal bipartite matching. We evaluate 9 commercial and open-source table extraction systems across the benchmark and report per-language breakdowns. The full dataset, scoring code, and all provider outputs are publicly available.

## 2. Page image classifier fine-tuned on century-spanning archives of scanned documents for further content-specific processing

- arXiv: `2606.07558`
- Link: https://arxiv.org/abs/2606.07558
- Announcement date: 2026-06-09
- Categories: cs.AI, cs.CV, cs.DL
- Tags: document image classification, historical documents, OCR
- Reason: Central task is classifying scanned page images for downstream OCR; uses document image classifiers.

### Abstract

Purpose: Digitization projects in the humanities produce vast, heterogeneous archives of historical documents, making manual sorting impractical at scale. This work addresses the need for an automated system to classify scanned page images based on visual content type - text, tables, and graphics - enabling content-specific downstream processing such as Optical Character Recognition (OCR) or structured data extraction. Methods: An image classification system was developed and evaluated on a dataset of over 48,000 annotated historical page images from century-old Czech archaeological archives, refined through four successive annotation stages with domain-expert review. A Random Forest Classifier baseline was established using hand-crafted image features. Subsequently, deep learning architectures were fine-tuned and compared: Convolutional Neural Networks (EfficientNetV2, RegNetY), Vision and Document Image Transformers (ViT, DiT), and multimodal CLIP models. An 11-category label scheme was designed collaboratively with domain experts and evaluated via five-fold cross-validation. Results: The feature-based baseline achieved approximately 75% accuracy. Fine-tuned CNNs and Transformers substantially outperformed it, with RegNetY-16GF achieving 99.16% and ViT-large 99.12% Top-1 accuracy on the held-out test set. CLIP ViT-B/16 reached 99.14% with optimized text descriptions. Conclusion: Image-only models, particularly RegNetY-16GF, deliver near-perfect classification accuracy and produce consistent labels across 649,508 unlabeled archival pages with over 90% inter-model agreement. Fine-tuned CLIP, despite competitive test-set accuracy, showed under 65% agreement with image-only models on unlabeled data, making it less suitable for deployment. The final models, annotated dataset, and software are publicly available under open-source licenses.

## 3. PereStruct: Multimodal Semantic Assembly for Robust Historical Document Parsing

- arXiv: `2606.07661`
- Link: https://arxiv.org/abs/2606.07661
- Announcement date: 2026-06-09
- Categories: cs.CV, cs.DL
- Tags: historical document parsing, layout analysis, document understanding
- Reason: Central task is parsing historical documents with complex layouts; uses layout analysis and semantic assembly.

### Abstract

Parsing historical documents with complex, non-standard layouts remains a fundamental bottleneck in large-scale archival digitization. Unlike modern typography, historical newspapers exhibit severe physical degradation and highly irregular page structures that confound even state-of-the-art vision-language models, presenting severe out-of-distribution challenges. We address this gap with an automated pipeline specifically designed for parsing historical newspapers, documents characterized by particularly intricate multi-column layouts. Our approach combines a fine-tuned YOLO architecture for layout analysis and block detection, trained on 1,426 fully human-annotated scanned pages, with a novel semantic assembly module that reconstructs articles by jointly modeling lexical-semantic similarity via TF-IDF, visual embeddings from our fine-tuned YOLO, and geometric layout constraints. This multi-modal integration yields state-of-the-art performance, achieving an F1 score of 0.904 on block-to-article mapping. Notably, end-to-end evaluation against vision-language models (Qwen3.6-35B-A3B and Qwen3.6-Plus) demonstrates that PereStruct achieves substantially higher fidelity (BLEU approximately 0.96 vs 0.34), validating that modular architectures excel where generic VLMs fail on complex historical layouts. To support reproducibility and advance research in this domain, we release both the training corpus of 599 annotated pages and a curated PereStruct benchmark of 93 pages with expert-verified ground-truth block-to-article mappings. This framework establishes a robust foundation for high-fidelity digitization and semantic reconstruction of complex archival materials.

## 4. The CIFAR Synthetic Evidence Corpus for Detecting AI-Generated Evidence

- arXiv: `2606.07916`
- Link: https://arxiv.org/abs/2606.07916
- Announcement date: 2026-06-09
- Categories: cs.AI
- Tags: document understanding, AI-generated document detection, dataset
- Reason: Central task is detecting AI-generated evidentiary documents (receipts, forms, etc.), directly relevant to document AI.

### Abstract

The growing ability of generative models to produce realistic documents poses a direct challenge to evidentiary workflows in the justice system and the courts, where decisions increasingly depend on the authenticity of evidence such as receipts, communications, and administrative records. Unlike social media or academic settings, evidentiary documents are often only subtly altered, with small, localized edits that preserve overall plausibility while changing legal meaning. Yet progress on automated detection remains limited, largely due to the absence of suitable training and evaluation data especially suited for the justice system requirements. Existing resources are either focused on photos of human faces or natural scenery or on narrowly scoped academic or social media document types, and do not capture the structure, diversity, or manipulation patterns characteristic of real-world evidentiary data. As a result, current detection systems do not necessarily learn meaningful signals appropriate for the justice system. We introduce the CIFAR Synthetic Evidence Corpus, a dataset designed to enable rigorous evaluation of evidence verification under realistic and controlled conditions. The corpus spans multiple document families and a spectrum of manipulation strategies, from small field-level edits to complete document fabrication, and is constructed using a diverse set of state-of-the-art generative tools. It is organized to systematically vary both manipulation complexity and generation method, while enforcing source-level separation between training and test data to reflect real-world generalization challenges.

## 5. Arabic Sentence Segmentation Across Genres and Punctuation Conditions

- arXiv: `2606.08025`
- Link: https://arxiv.org/abs/2606.08025
- Announcement date: 2026-06-09
- Categories: cs.CL
- Tags: sentence segmentation, document parsing, Arabic NLP
- Reason: Directly addresses sentence segmentation across document genres and punctuation conditions, relevant to document parsing.

### Abstract

Sentence segmentation in Arabic is challenging due to ambiguous and inconsistent punctuation, with many texts lacking reliable sentence boundary markers. Existing approaches rely heavily on punctuation cues and are typically evaluated on well-formed text, limiting their robustness in realistic Arabic settings. To address this, we introduce AraSEG, a genre-diverse sentence segmentation corpus spanning eight genres and a wide range of punctuation and document structure conditions. Using AraSEG, we evaluate LLMs, lightweight encoder models, and dependency parser-based models under increasingly challenging segmentation settings. Our experiments show that lightweight encoders, and even dependency parser-based models, outperform LLMs in the most challenging settings. We further investigate the effects of training data size and genre diversity, finding that performance eventually saturates and cross-genre generalization remains challenging. We also demonstrate that accurate sentence segmentation substantially improves downstream dependency parsing. We make our code, data, and models publicly available.

## 6. How Small Can You Go? LoRA Fine-Tuning 270M-8B Models for Merchant Information Extraction in Financial Transactions

- arXiv: `2606.08051`
- Link: https://arxiv.org/abs/2606.08051
- Announcement date: 2026-06-09
- Categories: cs.AI, cs.LG
- Tags: information extraction, financial documents, merchant extraction
- Reason: Central task is extracting structured merchant info from financial transaction strings, a form of document information extraction.

### Abstract

Financial transaction processing requires extracting structured merchant information from noisy, abbreviated bank transaction strings at scale. Our current production system, a LoRA-fine-tuned LLaMA 3.1-8B, achieves 96.95% F1 on this task, but deploying 8-billion-parameter models imposes prohibitive memory, latency, and cost constraints. To identify more efficient alternatives, we conduct a deployment-focused study of 24 model variants spanning four model families: Gemma 3 (270M, 1B, 4B), Qwen 3.5 (0.8B, 2B, 4B), Aya (3.35B), and LLaMA 3.1-8B, systematically evaluating accuracy, inference throughput, training cost, and hardware behavior to assess production suitability. Our findings show that: (1) reproducing the LLaMA 3.1-8B fine-tune with a LoRA rank of 8 achieves 96.75% F1, only 0.20 points below the rank-32 baseline; (2) Qwen 3.5 4B with JSON-only prompting reaches 96.60% F1, within 0.35 points of the 8B baseline while using roughly half the parameters; (3) the 0.8B Qwen 3.5 model achieves 94.75% F1, matching models 2.5-4x larger and offering an attractive latency-accuracy trade-off; (4) chain-of-thought fine-tuning generally improves F1 by 0.3-1.8 points across most models, although Qwen 3.5 4B performs best with direct JSON-only prompting; and (5) Qwen 3.5 Think and Nothink training templates produce nearly identical results (F1 differences <0.004), indicating that explicit reasoning supervision is unnecessary for structured extraction tasks. We further deploy all 14 fine-tuned sub-8B models as Databricks Model Serving endpoints and observe that benchmark performance transfers reliably to production, with an average F1 change of only 0.8 points. Aya 3.35B, based on the Cohere2 architecture, is the sole exception, exhibiting a 3-5 point decline under serving conditions. Based on these results, we provide deployment recommendations across accuracy and latency requirements, ...

## 7. AgriGov: A Structured Multilingual Dataset Curation for Indian Government Schemes for Farmers

- arXiv: `2606.08272`
- Link: https://arxiv.org/abs/2606.08272
- Announcement date: 2026-06-09
- Categories: cs.AI, cs.CL
- Tags: document curation, multilingual dataset, government schemes
- Reason: Central task is curating structured multilingual dataset from government documents, relevant to document parsing and understanding.

### Abstract

AgriGov is a curated, trilingual (English-Hindi-Marathi) dataset designed to address the scarcity of domain-grounded multilingual resources for agricultural policies and farmer welfare schemes. Initially, we collected and structured data from 50 government schemes sourced from trusted portals using automated scraping techniques, organizing it into predefined semantic fields (e.g., title, eligibility, application process, documents, exclusions). Translations were performed using a pipeline combining Google Translate API, MarianMT, and human post-editing, resulting in a domain-specific Hindi-Marathi dataset comprising approximately 2100 source segments. To enhance coverage, we augmented this dataset with sentences from the Samanantar corpus, leading to approximately 8,000 sentence-aligned Hindi-Marathi parallel pairs. The dataset now offers robust resources for fine-tuning machine translation models in this domain. AgriGov is designed for applications in domain-adaptive machine translation, question answering, information retrieval, and summarization systems. Its key contribution is a schema-driven, human-corrected multilingual alignment pipeline that ensures domain fidelity, provides provenance, and supports reproducible experiments, enabling retrieval-augmented applications for farmer-facing tools.

## 8. TeamHerald@CHIPSAL 2026: Hate Speech Detection and Sentiment Analysis of Nepali Memes using Transformer-based Architectures and Ensemble Learning

- arXiv: `2606.08770`
- Link: https://arxiv.org/abs/2606.08770
- Announcement date: 2026-06-09
- Categories: cs.AI, cs.CL, cs.CV, cs.LG
- Tags: OCR, meme analysis, hate speech detection
- Reason: Central use of OCR for text extraction from memes; text-centric approach.

### Abstract

The analysis of internet memes in the Nepali language is complicated by frequent code-mixing and a lack of established baseline resources. While memes inherently combine visual and textual elements, this study focuses on a text-centric approach by extracting embedded text using an OCR layer and modeling it with Transformer-based architectures. We evaluate six distinct models and investigate the comparative effectiveness of Hard and Soft Voting ensemble strategies across two tasks: binary hate speech detection and three-class sentiment analysis. Experimental results show that a standalone decoder-only model achieved the highest performance for binary classification, whereas the Soft Voting ensemble performed best for the multi-class sentiment task, yielding a 15.8% relative improvement in Macro F1-score over the strongest standalone baseline. These findings suggest that ensemble strategies behave differently across binary and multi-class tasks, highlighting the importance of selecting aggregation methods suited to the classification objective.

## 9. DeepMine-Mamba: Mitigating Information Dilution in Mamba-Based State Space Models for Document Image Binarization

- arXiv: `2606.08781`
- Link: https://arxiv.org/abs/2606.08781
- Announcement date: 2026-06-09
- Categories: cs.CV
- Tags: document image binarization, OCR preprocessing
- Reason: Core task is document image binarization for text extraction.

### Abstract

Document image binarization aims to separate foreground text from degraded backgrounds while preserving thin, broken, and low-contrast strokes. Although deep learning methods have improved binarization performance, most existing approaches rely on convolutional, transformer-based, or generative architectures, while Mamba-based state space models remain largely unexplored for this task. In this work, we investigate Mamba-based feature propagation and observe that direct state-space propagation may dilute weak foreground cues during long-range modeling, especially faint ink traces, fragmented characters, and boundary-sensitive stroke details. To address this problem, we propose DeepMine-Mamba, a Mamba-based binarization framework equipped with a novel Anti-Dilution Gate that estimates propagation-induced feature changes and selectively restores stroke-sensitive local responses while suppressing unnecessary background enhancement. Experiments on DIBCO/H-DIBCO benchmarks under a strict leave-one-year-out protocol show that DeepMine-Mamba achieves competitive overall performance, with strong average FM and Fps across benchmark years. Ablation results further demonstrate that the Anti-Dilution Gate improves stroke preservation and reduces perceptually significant binarization errors.

## 10. Hybrid E-Assessment in Higher Education: Semi-Automated Grading of Paper-Based Written Examinations

- arXiv: `2606.08855`
- Link: https://arxiv.org/abs/2606.08855
- Announcement date: 2026-06-09
- Categories: cs.AI, cs.CV, cs.CY
- Tags: handwritten text recognition, e-assessment
- Reason: Central task is handwritten character recognition from exam forms.

### Abstract

This paper examines the limitations of fully digital and partially digital e-assessment approaches in summative examinations in higher education. The analysis focuses on the didactic narrowing caused by closed question formats and on organizational, technical, and legal constraints that become particularly relevant in large student cohorts. As an alternative, the paper proposes a hybrid e-assessment approach that retains paper-based, problem-oriented examination tasks while enabling semi-automated grading. Assessment-relevant intermediate results are encoded in a structured answer format, entered by students by hand, and subsequently captured from table fields. The central technical bottleneck is reliable recognition of handwritten characters under realistic examination conditions. Recent vision-capable large language models, combined with a two-pass validation principle and comparison against a solution key, can reduce misclassifications and thereby improve the validity, fairness, and scalability of summative assessment.

## 11. Intelligent Character Recognition of Handwritten Forms with Deep Neural Networks

- arXiv: `2606.08858`
- Link: https://arxiv.org/abs/2606.08858
- Announcement date: 2026-06-09
- Categories: cs.AI, cs.CV
- Tags: handwritten character recognition, form processing
- Reason: Core task is intelligent character recognition of handwritten forms.

### Abstract

The automatic processing of handwritten forms remains a challenging task, wherein detection and subsequent classification of handwritten characters are essential steps. We describe a novel approach, in which both steps -- detection and classification -- are executed in one task through a deep neural network. Therefore, training data is not annotated by hand, but manufactured artificially from the underlying forms and yet existing datasets. It can be demonstrated that this single-task approach is superior in comparison to the state-of-the-art two-task approach. The current study focuses on hand-written Latin letters and employs the EMNIST data set. However, limitations were identified with this data set, necessitating further customization. Finally, an overall recognition rate of 88.28 percent was attained on real data obtained from a written exam.

## 12. Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care

- arXiv: `2606.08982`
- Link: https://arxiv.org/abs/2606.08982
- Announcement date: 2026-06-09
- Categories: cs.AI
- Tags: medical document OCR, multimodal
- Reason: Explicitly includes medical document OCR as a core capability.

### Abstract

Baichuan-M4 is Baichuan Intelligence's clinical-grade medical large model, designed for continuous care rather than single-turn medical question answering. It is built as a coordinated medical agent system around three pillars: Baichuan-Harness, a unified runtime that keeps reinforcement-learning training and real-world deployment consistent while enforcing action constraints, tool use, long-term patient memory, and multi-agent coordination; a core reasoning model trained with a continuous-care reinforcement-learning framework that integrates span-level reward modeling (SPAR++), reasoning-path compression, curriculum learning, and stabilized policy optimization; and a clinical tool layer for patient-memory management, authoritative evidence-based retrieval, and multimodal medical perception across documents, X-rays, and dermatology. On a cross-dimensional medical evaluation suite, Baichuan-M4 attains leading results in static medical knowledge and safety, dynamic OSCE-style consultation, long-context clinical memory, evidence-based retrieval, medical document OCR, and multimodal image understanding, while lowering the hallucination rate to 3.3%.

## 13. Vision Language Model Helps Private Information De-Identification in Vision Data

- arXiv: `2606.09132`
- Link: https://arxiv.org/abs/2606.09132
- Announcement date: 2026-06-09
- Categories: cs.AI
- Tags: OCR, privacy, VLM
- Reason: Central task is OCR for sensitive text localization in images, with explicit OCR mention.

### Abstract

Visual Language Models (VLMs) have gained significant popularity due to their remarkable ability. While various methods exist to enhance privacy in text-based applications, privacy risks associated with visual inputs remain largely overlooked such as Protected Health Information (PHI) in medical images. To tackle this problem, two key tasks: accurately localizing sensitive text and processing it to ensure privacy protection should be performed. To address this issue, we introduce VisShield (Vision Privacy Shield), an end-to-end framework designed to enhance the privacy awareness of VLMs. Our framework consists of two key components: a specialized instruction-tuning dataset OPTIC (Optical Privacy Text Instruction Collection) and a tailored training methodology. The dataset provides diverse privacy-oriented prompts that guide VLMs to perform targeted Optical Character Recognition (OCR) for precise localization of sensitive text, while the training strategy ensures effective adaptation of VLMs to privacy-preserving tasks. Specifically, our approach ensures that VLMs recognize privacy-sensitive text and output precise bounding boxes for detected entities, allowing for effective masking of sensitive information. Extensive experiments demonstrate that our framework significantly outperforms existing approaches in handling private information, paving the way for privacy-preserving applications in vision-language models. Our dataset and code can be found here.

## 14. MUDIDI: A Two-Stage Framework for Multilingual Dictionary Digitization with Language Models

- arXiv: `2606.09435`
- Link: https://arxiv.org/abs/2606.09435
- Announcement date: 2026-06-09
- Categories: cs.CL
- Tags: OCR, document digitization, layout analysis
- Reason: Central task is multilingual dictionary digitization using OCR and layout understanding.

### Abstract

Multilingual dictionaries are among the most valuable documentary resources for low-resource and endangered languages, yet many remain available only as scans. For many decades, their digitization and conversion into a machine-readable format was nearly impossible due to language-specific scripts, complex multi-column layouts full of entries with abbreviations and cross-references. Recent vision-language models offer a promising solution, but it is unclear how well they preserve characters, markup, and process lexicographic structure. We introduce MUDIDI, a two-stage framework for multi-lingual dictionary digitization. Stage One evaluates the quality of character recognition and markup preservation; Stage Two focuses on dictionary entry segmentation with subsequent mapping into a machine-readable lexicographic schema, SIL's Multi-Dictionary Formatter. We also release a dataset that consists of human-annotated lexicographic entries collected from 30 public-domain dictionaries featuring diverse writing systems, language families, and formats. We benchmark OCR systems, general-purpose Large Language Models (LLMs), and Vision Language Models (VLMs) on the dataset, demonstrating superior performance of LLMs across most writing systems and languages in both stages, and provide practical guidelines on improving the results for more challenging scenarios. Finally, we show that supplementing additional information, such as dictionary introduction, to the LLMs can improve the quality of the digitized dictionary. Github: https://github.com/DavidSamuell/MUDIDI-Pipeline-for-Digitization-of-Multilingual-Dictionary/

## 15. Leveraging Morphology for Historical Script Metrological Analysis

- arXiv: `2606.09446`
- Link: https://arxiv.org/abs/2606.09446
- Announcement date: 2026-06-09
- Categories: cs.CV
- Tags: handwritten text recognition, document analysis, paleography
- Reason: Central task is handwritten text recognition and morphological analysis of historical documents.

### Abstract

Advances in handwritten text recognition have enabled large-scale transcription of historical documents, but still provide limited access to interpretable visual measurements for paleography, the study of historical scripts. In this paper, our main insight is that morphological script analysis, in particular the capacity to learn character prototypes from line-level transcriptions, enables the definition of scalable, meaningful, and stable paleographic measurements. More precisely, we leverage a transformer-based detection architecture together with a prototype-based line reconstruction module to learn prototypical characters and their occurrence, deformation, and positioning. Our contributions are twofold. First, we introduce a deep architecture and learning methodology that enables efficient character modeling with only line-level transcription supervision, significantly improving over the Learnable Typewriter baseline and enabling accurate character bounding box prediction, unlocking its potential for paleographic measurements. Second, we introduce and demonstrate the paleographical relevance of automatic measurements enabled by our architecture for characters, bi-grams, and spaces between graphical units. For this demonstration, we extend the annotations of the codex Paris, BnF, fr. 2813, commissioned in the late fourteenth century by Charles V and copied by four hands, to 160 pages. We visualize our measurements over these pages, showing how they enable us not only to differentiate graphical profiles, but also to discover and analyze subtle variations. This case study outlines the scalability of our approach and its frugality in terms of required training data, since a single column of text is sufficient to compute our measurements on each of the 160 pages. Data and code are publicly available at: https://malamatenia.github.io/morphology4metrology-analysis.

## 16. TABVERSE: Benchmarking Cross-Format Table Understanding in LLMs and VLMs

- arXiv: `2606.09578`
- Link: https://arxiv.org/abs/2606.09578
- Announcement date: 2026-06-09
- Categories: cs.AI, cs.CL, cs.IR
- Tags: table understanding, benchmark, document AI
- Reason: Central task is benchmarking table understanding across formats, directly relevant to document AI.

### Abstract

Large Language Models (LLMs) and Vision-Language Models (VLMs) are increasingly evaluated on table reasoning tasks, but the role of table representation remains under-explored. In practice, the same table content may appear in different structural formats, such as HTML, Markdown, and LaTeX, or as rendered images. However, existing evaluations often let content, format, layout, and modality vary together, making it difficult to isolate representation effects. We introduce TABVERSE, a controlled multimodal table benchmark that aligns the same table content across multiple structural formats and rendered images, with question category and difficulty tags. This design enables systematic evaluation of representation effects while holding table content fixed. We evaluate LLMs and VLMs across three tasks: Question Answering (QA), Structural Understanding Capability (SUC), and Structure Reconstruction (SR). Our results show that representation choice substantially affects table understanding. Models generally perform better with structured text than with rendered images, but the size of this gap depends on the task, model, and format. HTML is often the most robust text format, while row-sensitive structural tasks and syntactically usable LaTeX reconstruction remain challenging. These findings show that table representation is a key factor in reliable table evaluation.

## 17. POTATR: A Lightweight Image-to-Graph Model for Page-Level Table Extraction

- arXiv: `2606.09788`
- Link: https://arxiv.org/abs/2606.09788
- Announcement date: 2026-06-09
- Categories: cs.CV
- Tags: table extraction, document AI, OCR
- Reason: Central task is page-level table extraction from document images, directly relevant to document AI and OCR.

### Abstract

Large-scale document processing requires contextually aware table extraction (TE) that is both accurate and efficient. Yet current approaches require billions of parameters, hundreds of autoregressive steps, or costly API inference. Motivated by this, we introduce the Page-Object Table Transformer (POTATR), a lightweight 29M parameter image-to-graph model that extends the Table Transformer (TATR) for contextualized page-level TE. POTATR outperforms all models tested on the PubTables-v2 Single Pages benchmark -- including frontier MLLMs -- achieving $\textrm{GriTS}_\textrm{Con}$ of 0.964 while running over 130$\times$ faster at roughly 300$\times$ lower cost. Further, POTATR's output is spatially grounded: every recognized element has a bounding box, enabling visual verification and geometric text assignment. As a result, POTATR performs unified page-level TE while composing with other models, enabling extension to scanned documents via external OCR and to full-document TE via techniques like cross-page merging. Code and models will be released.
