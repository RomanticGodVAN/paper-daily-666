# Document AI and OCR — 2026-04-14

- Papers: 6
- Skipped as duplicates: 0

## 1. AdaQE-CG: Adaptive Query Expansion for Web-Scale Generative AI Model and Data Card Generation

- arXiv: `2604.09617`
- Link: https://arxiv.org/abs/2604.09617
- Announcement date: 2026-04-14
- Categories: cs.AI, cs.IR
- Tags: information extraction, scientific papers, documentation generation
- Reason: Central task is extracting structured information from scientific papers to generate model/data cards.

### Abstract

Transparent and standardized documentation is essential for building trustworthy generative AI (GAI) systems. However, existing automated methods for generating model and data cards still face three major challenges: (i) static templates, as most systems rely on fixed query templates that cannot adapt to diverse paper structures or evolving documentation requirements; (ii) information scarcity, since web-scale repositories such as Hugging Face often contain incomplete or inconsistent metadata, leading to missing or noisy information; and (iii) lack of benchmarks, as the absence of standardized datasets and evaluation protocols hinders fair and reproducible assessment of documentation quality. To address these limitations, we propose AdaQE-CG, an Adaptive Query Expansion for Card Generation framework that combines dynamic information extraction with cross-card knowledge transfer. Its Intra-Paper Extraction via Context-Aware Query Expansion (IPE-QE) module iteratively refines extraction queries to recover richer and more complete information from scientific papers and repositories, while its Inter-Card Completion using the MetaGAI Pool (ICC-MP) module fills missing fields by transferring semantically relevant content from similar cards in a curated dataset. In addition, we introduce MetaGAI-Bench, the first large-scale, expert-annotated benchmark for evaluating GAI documentation. Comprehensive experiments across five quality dimensions show that AdaQE-CG substantially outperforms existing approaches, exceeds human-authored data cards, and approaches human-level quality for model cards. Code, prompts, and data are publicly available at: https://github.com/haoxuan-unt2024/AdaQE-CG.

## 2. Zero-Shot Synthetic-to-Real Handwritten Text Recognition via Task Analogies

- arXiv: `2604.09713`
- Link: https://arxiv.org/abs/2604.09713
- Announcement date: 2026-04-14
- Categories: cs.CV
- Tags: handwritten text recognition, zero-shot, synthetic-to-real
- Reason: Central task is handwritten text recognition, a core OCR task.

### Abstract

Handwritten Text Recognition (HTR) models trained on synthetic handwriting often struggle to generalize to real text, and existing adaptation methods still require real samples from the target domain. In this work, we tackle the fully zero-shot synthetic-to-real generalization setting, where no real data from the target language is available. Our approach learns how model parameters change when moving from synthetic to real handwriting in one or more source languages and transfers this learned correction to new target languages. When using multiple sources, we rely on linguistic similarity to weigh their contrubition when combining them. Experiments across five languages and six architectures show consistent improvements over synthetic-only baselines and reveal that the transferred corrections benefit even languages unrelated to the sources.

## 3. Multi-Head Attention based interaction-aware architecture for Bangla Handwritten Character Recognition: Introducing a Primary Dataset

- arXiv: `2604.09717`
- Link: https://arxiv.org/abs/2604.09717
- Announcement date: 2026-04-14
- Categories: cs.CV
- Tags: OCR, handwritten character recognition, Bangla, dataset
- Reason: Explicitly targets OCR for handwritten Bangla characters with new dataset.

### Abstract

Character recognition is the fundamental part of an optical character recognition (OCR) system. Word recognition, sentence transcription, document digitization, and language processing are some of the higher-order activities that can be done accurately through character recognition. Nonetheless, recognizing handwritten Bangla characters is not an easy task because they are written in different styles with inconsistent stroke patterns and a high degree of visual character resemblance. The datasets available are usually limited in intra-class and inequitable in class distribution. We have constructed a new balanced dataset of Bangla written characters to overcome those problems. This consists of 78 classes and each class has approximately 650 samples. It contains the basic characters, composite (Juktobarno) characters and numerals. The samples were a diverse group comprising a large age range and socioeconomic groups. Elementary and high school students, university students, and professionals are the contributing factors. The sample also has right and left-handed writers. We have further proposed an interaction-aware hybrid deep learning architecture that integrates EfficientNetB3, Vision Transformer, and Conformer modules in parallel. A multi-head cross-attention fusion mechanism enables effective feature interaction across these components. The proposed model achieves 98.84% accuracy on the constructed dataset and 96.49% on the external CHBCR benchmark, demonstrating strong generalization capability. Grad-CAM visualizations further provide interpretability by highlighting discriminative regions. The dataset and source code of this research is publicly available at: https://huggingface.co/MIRZARAQUIB/Bangla_Handwritten_Character_Recognition.

## 4. DocRevive: A Unified Pipeline for Document Text Restoration

- arXiv: `2604.10077`
- Link: https://arxiv.org/abs/2604.10077
- Announcement date: 2026-04-14
- Categories: cs.CV
- Tags: document-restoration, OCR, text-reconstruction, document-understanding
- Reason: Central task is document text restoration using OCR and document understanding techniques, explicitly targeting damaged document reconstruction.

### Abstract

In Document Understanding, the challenge of reconstructing damaged, occluded, or incomplete text remains a critical yet unexplored problem. Subsequent document understanding tasks can benefit from a document reconstruction process. In response, this paper presents a novel unified pipeline combining state-of-the-art Optical Character Recognition (OCR), advanced image analysis, masked language modeling, and diffusion-based models to restore and reconstruct text while preserving visual integrity. We create a synthetic dataset of 30{,}078 degraded document images that simulates diverse document degradation scenarios, setting a benchmark for restoration tasks. Our pipeline detects and recognizes text, identifies degradation with an occlusion detector, and uses an inpainting model for semantically coherent reconstruction. A diffusion-based module seamlessly reintegrates text, matching font, size, and alignment. To evaluate restoration quality, we propose a Unified Context Similarity Metric (UCSM), incorporating edit, semantic, and length similarities with a contextual predictability measure that penalizes deviations when the correct text is contextually obvious. Our work advances document restoration, benefiting archival research and digital preservation while setting a new standard for text reconstruction. The OPRB dataset and code are available at \href{https://huggingface.co/datasets/kpurkayastha/OPRB}{Hugging Face} and \href{https://github.com/kunalpurkayastha/DocRevive}{Github} respectively.

## 5. Improving Layout Representation Learning Across Inconsistently Annotated Datasets via Agentic Harmonization

- arXiv: `2604.11042`
- Link: https://arxiv.org/abs/2604.11042
- Announcement date: 2026-04-14
- Categories: cs.CV
- Tags: layout-analysis, document-understanding, table-detection
- Reason: Core contribution is document layout detection and annotation harmonization for document conversion pipelines.

### Abstract

Fine-tuning object detection (OD) models on combined datasets assumes annotation compatibility, yet datasets often encode conflicting spatial definitions for semantically equivalent categories. We propose an agentic label harmonization workflow that uses a vision-language model to reconcile both category semantics and bounding box granularity across heterogeneous sources before training. We evaluate on document layout detection as a challenging case study, where annotation standards vary widely across corpora. Without harmonization, na\"ive mixed-dataset fine-tuning degrades a pretrained RT-DETRv2 detector: on SCORE-Bench, which measures how accurately the full document conversion pipeline reproduces ground-truth structure, table TEDS drops from 0.800 to 0.750. Applied to two corpora whose 16 and 10 category taxonomies share only 8 direct correspondences, harmonization yields consistent gains across content fidelity, table structure, and spatial consistency: detection F-score improves from 0.860 to 0.883, table TEDS improves to 0.814, and mean bounding box overlap drops from 0.043 to 0.016. Representation analysis further shows that harmonized training produces more compact and separable post-decoder embeddings, confirming that annotation inconsistency distorts the learned feature space and that resolving it before training restores representation structure.

## 6. The Devil is in the Details -- From OCR for Old Church Slavonic to Purely Visual Stemma Reconstruction

- arXiv: `2604.11724`
- Link: https://arxiv.org/abs/2604.11724
- Announcement date: 2026-04-14
- Categories: cs.CV
- Tags: ocr, handwritten-text, historical-documents
- Reason: Central task is OCR for handwritten Church Slavonic manuscripts with detailed OCR evaluation.

### Abstract

The age of artificial intelligence has brought many new possibilities and pitfalls in many fields and tasks. The devil is in the details, and those come to the fore when building new pipelines and executing small practical experiments. OCR and stemmatology are no exception. The current investigation starts comparing a range of OCR-systems, from classical over machine learning to LLMs, for roughly 6,000 characters of late handwritten church slavonic manuscripts from the 18th century. Focussing on basic letter correctness, more than 10 CS OCR-systems among which 2 LLMs (GPT5 and Gemini3-flash) are being compared. Then, post-processing via LLMs is assessed and finally, different agentic OCR architectures (specialized post-processing agents, an agentic pipeline and RAG) are tested. With new technology elaborated, experiments suggest, church slavonic CER for basic letters may reach as low as 2-3% but elaborated diacritics could still present a problem. How well OCR can prime stemmatology as a downstream task is the entry point to the second part of the article which introduces a new stemmatic method based solely on image processing. Here, a pipeline of automated visual glyph extraction, clustering and pairwise statistical comparison leading to a distance matrix and ultimately a stemma, is being presented and applied to two small corpora, one for the church slavonic Gospel of Mark from the 14th to 16th centuries, one for the Roman de la Rose in French from the 14th and 15th centuries. Basic functioning of the method can be demonstrated.
