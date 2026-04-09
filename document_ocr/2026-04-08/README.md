# Document AI and OCR — 2026-04-08

- Papers: 8
- Skipped as duplicates: 0

## 1. From PDF to RAG-Ready: Evaluating Document Conversion Frameworks for Domain-Specific Question Answering

- arXiv: `2604.04948`
- Link: https://arxiv.org/abs/2604.04948
- Announcement date: 2026-04-08
- Categories: cs.AI, cs.IR, cs.LG
- Tags: PDF parsing, OCR, document conversion, RAG preprocessing
- Reason: Central task is evaluating PDF-to-text conversion frameworks including OCR tools (DeepSeek OCR) for document preprocessing. Directly targets document parsing for downstream tasks.

### Abstract

Retrieval-Augmented Generation (RAG) systems depend critically on the quality of document preprocessing, yet no prior study has evaluated PDF processing frameworks by their impact on downstream question-answering accuracy. We address this gap through a systematic comparison of four open-source PDF-to-Markdown conversion frameworks, Docling, MinerU, Marker, and DeepSeek OCR, across 19 pipeline configurations for extracting text and other contents from PDFs, varying the conversion tool, cleaning transformations, splitting strategy, and metadata enrichment. Evaluation was performed using a manually curated 50-question benchmark over a corpus of 36 Portuguese administrative documents (1,706 pages, ~492K words), with LLM-as-judge scoring averaged over 10 runs. Two baselines bounded the results: na\"ive PDFLoader (86.9%) and manually curated Markdown (97.1%). Docling with hierarchical splitting and image descriptions achieved the highest automated accuracy (94.1%). Metadata enrichment and hierarchy-aware chunking contributed more to accuracy than the conversion framework choice alone. Font-based hierarchy rebuilding consistently outperformed LLM-based approaches. An exploratory GraphRAG implementation scored only 82%, underperforming basic RAG, suggesting that na\"ive knowledge graph construction without ontological guidance does not yet justify its added complexity. These findings demonstrate that data preparation quality is the dominant factor in RAG system performance.

## 2. MedGemma 1.5 Technical Report

- arXiv: `2604.05081`
- Link: https://arxiv.org/abs/2604.05081
- Announcement date: 2026-04-08
- Categories: cs.AI
- Tags: medical document understanding, EHR, lab reports, information extraction
- Reason: Explicitly targets medical document understanding (lab reports, EHRs) as a core capability. Includes information extraction from clinical documents.

### Abstract

We introduce MedGemma 1.5 4B, the latest model in the MedGemma collection. MedGemma 1.5 expands on MedGemma 1 by integrating additional capabilities: high-dimensional medical imaging (CT/MRI volumes and histopathology whole slide images), anatomical localization via bounding boxes, multi-timepoint chest X-ray analysis, and improved medical document understanding (lab reports, electronic health records). We detail the innovations required to enable these modalities within a single architecture, including new training data, long-context 3D volume slicing, and whole-slide pathology sampling. Compared to MedGemma 1 4B, MedGemma 1.5 4B demonstrates significant gains in these new areas, improving 3D MRI condition classification accuracy by 11% and 3D CT condition classification by 3% (absolute improvements). In whole slide pathology imaging, MedGemma 1.5 4B achieves a 47% macro F1 gain. Additionally, it improves anatomical localization with a 35% increase in Intersection over Union on chest X-rays and achieves a 4% macro accuracy for longitudinal (multi-timepoint) chest x-ray analysis. Beyond its improved multimodal performance over MedGemma 1, MedGemma 1.5 improves on text-based clinical knowledge and reasoning, improving by 5% on MedQA accuracy and 22% on EHRQA accuracy. It also achieves an average of 18% macro F1 on 4 different lab report information extraction datasets (EHR Datasets 2, 3, 4, and Mendeley Clinical Laboratory Test Reports). Taken together, MedGemma 1.5 serves as a robust, open resource for the community, designed as an improved foundation on which developers can create the next generation of medical AI systems. Resources and tutorials for building upon MedGemma 1.5 can be found at https://goo.gle/MedGemma.

## 3. Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation

- arXiv: `2604.05150`
- Link: https://arxiv.org/abs/2604.05150
- Announcement date: 2026-04-08
- Categories: cs.AI, cs.SE
- Tags: document intelligence, invoice processing, table extraction, KILE, LIR
- Reason: Explicitly targets document intelligence with evaluation on invoice datasets (DocILE). Core contribution includes document parsing for structured extraction.

### Abstract

We study compiled AI, a paradigm in which large language models generate executable code artifacts during a compilation phase, after which workflows execute deterministically without further model invocation. This paradigm has antecedents in prior work on declarative pipeline optimization (DSPy) and hybrid neural-symbolic planning (LLM+P); our contribution is a systems-oriented study of its application to high-stakes enterprise workflows, with particular emphasis on healthcare settings where reliability and auditability are critical. By constraining generation to narrow business-logic functions embedded in validated templates, compiled AI trades runtime flexibility for predictability, auditability, cost efficiency, and reduced security exposure. We introduce (i) a system architecture for constrained LLM-based code generation, (ii) a four-stage generation-and-validation pipeline that converts probabilistic model output into production-ready code artifacts, and (iii) an evaluation framework measuring operational metrics including token amortization, determinism, reliability, security, and cost. We evaluate on two task types: function-calling (BFCL, n=400) and document intelligence (DocILE, n=5,680 invoices). On function-calling, compiled AI achieves 96% task completion with zero execution tokens, breaking even with runtime inference at approximately 17 transactions and reducing token consumption by 57x at 1,000 transactions. On document intelligence, our Code Factory variant matches Direct LLM on key field extraction (KILE: 80.0%) while achieving the highest line item recognition accuracy (LIR: 80.4%). Security evaluation across 135 test cases demonstrates 96.7% accuracy on prompt injection detection and 87.5% on static code safety analysis with zero false positives.

## 4. Toward Unified Fine-Grained Vehicle Classification and Automatic License Plate Recognition

- arXiv: `2604.05271`
- Link: https://arxiv.org/abs/2604.05271
- Announcement date: 2026-04-08
- Categories: cs.CV
- Tags: OCR, text recognition, license plate recognition
- Reason: Central task is Automatic License Plate Recognition (ALPR), which is a core OCR application. Paper explicitly applies OCR models to license plate recognition.

### Abstract

Extracting vehicle information from surveillance images is essential for intelligent transportation systems, enabling applications such as traffic monitoring and criminal investigations. While Automatic License Plate Recognition (ALPR) is widely used, Fine-Grained Vehicle Classification (FGVC) offers a complementary approach by identifying vehicles based on attributes such as color, make, model, and type. Although there have been advances in this field, existing studies often assume well-controlled conditions, explore limited attributes, and overlook FGVC integration with ALPR. To address these gaps, we introduce UFPR-VeSV, a dataset comprising 24,945 images of 16,297 unique vehicles with annotations for 13 colors, 26 makes, 136 models, and 14 types. Collected from the Military Police of Paran\'a (Brazil) surveillance system, the dataset captures diverse real-world conditions, including partial occlusions, nighttime infrared imaging, and varying lighting. All FGVC annotations were validated using license plate information, with text and corner annotations also being provided. A qualitative and quantitative comparison with established datasets confirmed the challenging nature of our dataset. A benchmark using five deep learning models further validated this, revealing specific challenges such as handling multicolored vehicles, infrared images, and distinguishing between vehicle models that share a common platform. Additionally, we apply two optical character recognition models to license plate recognition and explore the joint use of FGVC and ALPR. The results highlight the potential of integrating these complementary tasks for real-world applications. The UFPR-VeSV dataset is publicly available at: https://github.com/Lima001/UFPR-VeSV-Dataset.

## 5. From Large Language Model Predicates to Logic Tensor Networks: Neurosymbolic Offer Validation in Regulated Procurement

- arXiv: `2604.05539`
- Link: https://arxiv.org/abs/2604.05539
- Announcement date: 2026-04-08
- Categories: cs.AI
- Tags: document understanding, form understanding, offer validation, neurosymbolic
- Reason: Central task is validating offer documents in regulated procurement. Explicitly involves extracting information from documents and making auditable decisions.

### Abstract

We present a neurosymbolic approach, i.e., combining symbolic and subsymbolic artificial intelligence, to validating offer documents in regulated public institutions. We employ a language model to extract information and then aggregate with an LTN (Logic Tensor Network) to make an auditable decision. In regulated public institutions, decisions must be made in a manner that is both factually correct and legally verifiable. Our neurosymbolic approach allows existing domain-specific knowledge to be linked to the semantic text understanding of language models. The decisions resulting from our pipeline can be justified by predicate values, rule truth values, and corresponding text passages, which enables rule checking based on a real corpus of offer documents. Our experiments on a real corpus show that the proposed pipeline achieves performance comparable to existing models, while its key advantage lies in its interpretability, modular predicate extraction, and explicit support for XAI (Explainable AI).

## 6. FinReporting: An Agentic Workflow for Localized Reporting of Cross-Jurisdiction Financial Disclosures

- arXiv: `2604.05966`
- Link: https://arxiv.org/abs/2604.05966
- Announcement date: 2026-04-08
- Categories: cs.CL
- Tags: document understanding, PDF parsing, financial reporting, form understanding
- Reason: Central task is extracting and summarizing financial disclosures from PDFs and other formats across jurisdictions. Explicitly involves filing acquisition and extraction.

### Abstract

Financial reporting systems increasingly use large language models (LLMs) to extract and summarize corporate disclosures. However, most assume a single-market setting and do not address structural differences across jurisdictions. Variations in accounting taxonomies, tagging infrastructures (e.g., XBRL vs. PDF), and aggregation conventions make cross-jurisdiction reporting a semantic alignment and verification challenge. We present FinReporting, an agentic workflow for localized cross-jurisdiction financial reporting. The system builds a unified canonical ontology over Income Statement, Balance Sheet, and Cash Flow, and decomposes reporting into auditable stages including filing acquisition, extraction, canonical mapping, and anomaly logging. Rather than using LLMs as free-form generators, FinReporting deploys them as constrained verifiers under explicit decision rules and evidence grounding. Evaluated on annual filings from the US, Japan, and China, the system improves consistency and reliability under heterogeneous reporting regimes. We release an interactive demo supporting cross-market inspection and structured export of localized financial statements. Our demo is available at https://huggingface.co/spaces/BoomQ/FinReporting-Demo . The video describing our system is available at https://www.youtube.com/watch?v=f65jdEL31Kk

## 7. PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer

- arXiv: `2604.06129`
- Link: https://arxiv.org/abs/2604.06129
- Announcement date: 2026-04-08
- Categories: cs.AI, cs.CV
- Tags: handwritten text recognition, text recognition, transformer architecture
- Reason: Handwritten text recognition is a core application and one of five domains tested. Central contribution is a model for sequence tasks including OCR.

### Abstract

This paper introduces the Polynomial Mixer (PoM), a novel token mixing mechanism with linear complexity that serves as a drop-in replacement for self-attention. PoM aggregates input tokens into a compact representation through a learned polynomial function, from which each token retrieves contextual information. We prove that PoM satisfies the contextual mapping property, ensuring that transformers equipped with PoM remain universal sequence-to-sequence approximators. We replace standard self-attention with PoM across five diverse domains: text generation, handwritten text recognition, image generation, 3D modeling, and Earth observation. PoM matches the performance of attention-based models while drastically reducing computational cost when working with long sequences. The code is available at https://github.com/davidpicard/pom.

## 8. The Character Error Vector: Decomposable errors for page-level OCR evaluation

- arXiv: `2604.06160`
- Link: https://arxiv.org/abs/2604.06160
- Announcement date: 2026-04-08
- Categories: cs.CV, cs.LG
- Tags: OCR evaluation, document understanding, page parsing, metrics
- Reason: Central contribution is OCR evaluation metric (Character Error Vector) specifically for page-level document understanding with validation on archival newspapers.

### Abstract

The Character Error Rate (CER) is a key metric for evaluating the quality of Optical Character Recognition (OCR). However, this metric assumes that text has been perfectly parsed, which is often not the case. Under page-parsing errors, CER becomes undefined, limiting its use as a metric and making evaluating page-level OCR challenging, particularly when using data that do not share a labelling schema. We introduce the Character Error Vector (CEV), a bag-of-characters evaluator for OCR. The CEV can be decomposed into parsing and OCR, and interaction error components. This decomposability allows practitioners to focus on the part of the Document Understanding pipeline that will have the greatest impact on overall text extraction quality. The CEV can be implemented using a variety of methods, of which we demonstrate SpACER (Spatially Aware Character Error Rate) and a Character distribution method using the Jensen-Shannon Distance. We validate the CEV's performance against other metrics: first, the relationship with CER; then, parse quality; and finally, as a direct measure of page-level OCR quality. The validation process shows that the CEV is a valuable bridge between parsing metrics and local metrics like CER. We analyse a dataset of archival newspapers made of degraded images with complex layouts and find that state-of-the-art end-to-end models are outperformed by more traditional pipeline approaches. Whilst the CEV requires character-level positioning for optimal triage, thresholding on easily available values can predict the main error source with an F1 of 0.91. We provide the CEV as part of a Python library to support Document understanding research.
