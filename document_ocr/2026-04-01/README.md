# Document AI and OCR — 2026-04-01

- Papers: 6
- Skipped as duplicates: 0

## 1. Xuanwu: Evolving General Multimodal Models into an Industrial-Grade Foundation for Content Ecosystems

- arXiv: `2603.29211`
- Link: https://arxiv.org/abs/2603.29211
- Announcement date: 2026-04-01
- Categories: cs.AI, cs.CL, cs.CV
- Tags: OCR, multimodal, content moderation, adversarial OCR
- Reason: Explicit OCR focus in adversarial scenarios, central to document AI

### Abstract

In recent years, multimodal large models have continued to improve on general benchmarks. However, in real-world content moderation and adversarial settings, mainstream models still suffer from degraded generalization and catastrophic forgetting because of limited fine-grained visual perception and insufficient modeling of long-tail noise. In this paper, we present Xuanwu VL-2B as a case study of how general multimodal models can be developed into an industrial-grade foundation model for content ecosystems. The model adopts a compact InternViT-300M + MLP + Qwen3 1.7B architecture, balancing fine-grained visual perception, language-semantic alignment, and deployment cost within an approximately 2B-parameter budget. To balance business specialization with the retention of general capabilities, we developed a data iteration and curation mechanism and trained the model through a progressive three-stage pipeline: pre-training, mid-training, and post-training. Ablation studies and offline business evaluations show that Xuanwu VL-2B achieves an average score of 67.90 across seven OpenCompass multimodal metrics (vs. 64.27 for InternVL 3.5 2B), an average recall of 94.38% over seven independent business moderation tasks, and a weighted overall recall of 82.82% on policy-violating text in challenging adversarial OCR scenarios, outperforming Gemini-2.5-Pro (76.72%). These results show that, under a limited parameter budget, Xuanwu VL-2B achieves a practical balance among business alignment, visual perception, general capability retention, and deployment cost.

## 2. SiPaKosa: A Comprehensive Corpus of Canonical and Classical Buddhist Texts in Sinhala and Pali

- arXiv: `2603.29221`
- Link: https://arxiv.org/abs/2603.29221
- Announcement date: 2026-04-01
- Categories: cs.CL
- Tags: OCR, document AI, corpus creation, historical documents
- Reason: Central use of OCR for document corpus creation with historical manuscripts

### Abstract

SiPaKosa is a comprehensive corpus of Sinhala and Pali doctrinal texts comprising approximately 786K sentences and 9.25M words, incorporating 16 copyright-cleared historical Buddhist documents alongside the complete web-scraped Tripitaka canonical texts. The corpus was created through high-quality OCR using Google Document AI on historical manuscripts, combined with systematic web scraping of canonical repositories, followed by rigorous quality control and metadata annotation. The corpus is organised into language-specific subcorpora: Sinhala and Mixed Sinhala-Pali. We evaluate the performance of language models using ten pretrained models, with perplexity scores ranging from 1.09 to 189.67 on our corpus. This analysis shows that proprietary models significantly outperform open-source alternatives by factors of three to six times. This corpus supports the pretraining of domain-adapted language models, facilitates historical language analysis, and aids in the development of information retrieval systems for Buddhist scholarship while preserving Sinhala cultural heritage.

## 3. L-ReLF: A Framework for Lexical Dataset Creation

- arXiv: `2603.29346`
- Link: https://arxiv.org/abs/2603.29346
- Announcement date: 2026-04-01
- Categories: cs.CL
- Tags: OCR, optical character recognition, low-resource languages, lexical dataset
- Reason: OCR is core technical component for lexical dataset creation

### Abstract

This paper introduces the L-ReLF (Low-Resource Lexical Framework), a novel, reproducible methodology for creating high-quality, structured lexical datasets for underserved languages. The lack of standardized terminology, exemplified by Moroccan Darija, poses a critical barrier to knowledge equity in platforms like Wikipedia, often forcing editors to rely on inconsistent, ad-hoc methods to create new words in their language. Our research details the technical pipeline developed to overcome these challenges. We systematically address the difficulties of working with low-resource data, including source identification, utilizing Optical Character Recognition (OCR) despite its bias towards Modern Standard Arabic, and rigorous post-processing to correct errors and standardize the data model. The resulting structured dataset is fully compatible with Wikidata Lexemes, serving as a vital technical resource. The L-ReLF methodology is designed for generalizability, offering other language communities a clear path to build foundational lexical data for downstream NLP applications, such as Machine Translation and morphological analysis.

## 4. Few-shot Writer Adaptation via Multimodal In-Context Learning

- arXiv: `2603.29450`
- Link: https://arxiv.org/abs/2603.29450
- Announcement date: 2026-04-01
- Categories: cs.AI, cs.CV
- Tags: OCR, handwritten text recognition, HTR, writer adaptation
- Reason: Central focus on handwritten text recognition and OCR adaptation

### Abstract

While state-of-the-art Handwritten Text Recognition (HTR) models perform well on standard benchmarks, they frequently struggle with writers exhibiting highly specific styles that are underrepresented in the training data. To handle unseen and atypical writers, writer adaptation techniques personalize HTR models to individual handwriting styles. Leading writer adaptation methods require either offline fine-tuning or parameter updates at inference time, both involving gradient computation and backpropagation, which increase computational costs and demand careful hyperparameter tuning. In this work, we propose a novel context-driven HTR framework3 inspired by multimodal in-context learning, enabling inference-time writer adaptation using only a few examples from the target writer without any parameter updates. We further demonstrate the impact of context length, design a compact 8M-parameter CNN-Transformer that enables few-shot in-context adaptation, and show that combining context-driven and standard OCR training strategies leads to complementary improvements. Experiments on IAM and RIMES validate our approach with Character Error Rates of 3.92% and 2.34%, respectively, surpassing all writer-independent HTR models without requiring any parameter updates at inference time.

## 5. AutoFormBench: Benchmark Dataset for Automating Form Understanding

- arXiv: `2603.29832`
- Link: https://arxiv.org/abs/2603.29832
- Announcement date: 2026-04-01
- Categories: cs.CV
- Tags: form-understanding, benchmark, layout-analysis, document-parsing
- Reason: Explicitly focuses on form understanding benchmark with PDF document processing, layout analysis, and form element detection.

### Abstract

Automated processing of structured documents such as government forms, healthcare records, and enterprise invoices remains a persistent challenge due to the high degree of layout variability encountered in real-world settings. This paper introduces AutoFormBench, a benchmark dataset of 407 annotated real-world forms spanning government, healthcare, and enterprise domains, designed to train and evaluate form element detection models. We present a systematic comparison of classical OpenCV approaches and four YOLO architectures (YOLOv8, YOLOv11, YOLOv26-s, and YOLOv26-l) for localizing and classifying fillable form elements. specifically checkboxes, input lines, and text boxes across diverse PDF document types. YOLOv11 demonstrates consistently superior performance in both F1 score and Jaccard accuracy across all element classes and tolerance levels.

## 6. Diffusion-Based Feature Denoising with NNMF for Robust handwritten digit multi-class classification

- arXiv: `2603.29917`
- Link: https://arxiv.org/abs/2603.29917
- Announcement date: 2026-04-01
- Categories: cs.CV
- Tags: handwritten-text-recognition, digit-classification, robust-classification
- Reason: Central task is handwritten digit classification, which falls under handwritten text recognition in inclusion rules.

### Abstract

This work presents a robust multi-class classification framework for handwritten digits that combines diffusion-driven feature denoising with a hybrid feature representation. Inspired by our previous work on brain tumor classification, the proposed approach operates in a feature space to improve the robustness to noise and adversarial attacks. First, the input images are converted into tight, interpretable exemplification using Nonnegative Matrix Factorization (NNMF). In parallel, special deep features are extracted using a computational neural network (CNN). These integral features are combined into a united hybrid representation. To improve robustness, a step diffusion operation is used in the feature space by gradually adding Gaussian noise. A feature denoiser network is trained to reverse this operation and rebuild clean representations from tilted inputs. The courteous features are then applied for multi-class classification. The suggested method is evaluated in both baseline and adversarial settings using AutoAttack. The experimental outcome present that the diffusion-based hybrid model is both effective and robust, the CNN baseline models outperforming while maintain powerful classification performance. These results explain the activity of feature-level diffusion defense for reliable multi-class handwritten digit classification.
