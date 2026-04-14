# Document AI and OCR — 2026-04-13

- Papers: 3
- Skipped as duplicates: 0

## 1. EXAONE 4.5 Technical Report

- arXiv: `2604.08644`
- Link: https://arxiv.org/abs/2604.08644
- Announcement date: 2026-04-13
- Categories: cs.CL
- Tags: vision-language model, document understanding
- Reason: Technical report for EXAONE 4.5 VLM with explicit focus on document understanding as a core capability, trained on document-centric corpora. Central to document AI.

### Abstract

This technical report introduces EXAONE 4.5, the first open-weight vision language model released by LG AI Research. EXAONE 4.5 is architected by integrating a dedicated visual encoder into the existing EXAONE 4.0 framework, enabling native multimodal pretraining over both visual and textual modalities. The model is trained on large-scale data with careful curation, particularly emphasizing document-centric corpora that align with LG's strategic application domains. This targeted data design enables substantial performance gains in document understanding and related tasks, while also delivering broad improvements across general language capabilities. EXAONE 4.5 extends context length up to 256K tokens, facilitating long-context reasoning and enterprise-scale use cases. Comparative evaluations demonstrate that EXAONE 4.5 achieves competitive performance in general benchmarks while outperforming state-of-the-art models of similar scale in document understanding and Korean contextual reasoning. As part of LG's ongoing effort toward practical industrial deployment, EXAONE 4.5 is designed to be continuously extended with additional domains and application scenarios to advance AI for a better life.

## 2. MAB-DQA: Addressing Query Aspect Importance in Document Question Answering with Multi-Armed Bandits

- arXiv: `2604.08952`
- Link: https://arxiv.org/abs/2604.08952
- Announcement date: 2026-04-13
- Categories: cs.CL, cs.IR
- Tags: document question answering, multimodal RAG, layout understanding
- Reason: Paper directly addresses Document Question Answering (DQA) with multimodal RAG that processes page images and interprets visual layouts. Core contribution is to document understanding and DQA.

### Abstract

Document Question Answering (DQA) involves generating answers from a document based on a user's query, representing a key task in document understanding. This task requires interpreting visual layouts, which has prompted recent studies to adopt multimodal Retrieval-Augmented Generation (RAG) that processes page images for answer generation. However, in multimodal RAG, visual DQA struggles to utilize a large number of images effectively, as the retrieval stage often retains only a few candidate pages (e.g., Top-4), causing informative but less visually salient content to be overlooked in favor of common yet low-information pages. To address this issue, we propose a Multi-Armed Bandit-based DQA framework (MAB-DQA) to explicitly model the varying importance of multiple implicit aspects in a query. Specifically, MAB-DQA decomposes a query into aspect-aware subqueries and retrieves an aspect-specific candidate set for each. It treats each subquery as an arm and uses preliminary reasoning results from a small number of representative pages as reward signals to estimate aspect utility. Guided by an exploration-exploitation policy, MAB-DQA dynamically reallocates retrieval budgets toward high-value aspects. With the most informative pages and their correlations, MAB-DQA generates the expected results. On four benchmarks, MAB-DQA shows an average improvement of 5%-18% over the state-of-the-art method, consistently enhancing document understanding. Code at https://github.com/ElephantOH/MAB-DQA.

## 3. UIPress: Bringing Optical Token Compression to UI-to-Code Generation

- arXiv: `2604.09442`
- Link: https://arxiv.org/abs/2604.09442
- Announcement date: 2026-04-13
- Categories: cs.CL
- Tags: UI-to-code, optical compression, OCR
- Reason: Paper adapts optical token compression from document OCR to UI-to-code generation. Explicitly builds on OCR techniques and addresses visual token efficiency for structured output from screenshots, relevant to document AI.

### Abstract

UI-to-Code generation requires vision-language models (VLMs) to produce thousands of tokens of structured HTML/CSS from a single screenshot, making visual token efficiency critical. Existing compression methods either select tokens at inference time using task-agnostic heuristics, or zero out low-attention features without actually shortening the sequence -- neither truly reduces prefill latency or adapts to the non-uniform information density of UI screenshots. Meanwhile, optical (encoder-side learned) compression has shown strong results for document OCR, yet no prior work has adapted this paradigm to UI-to-Code generation. We propose UIPress, a lightweight learned compression module inserted between the frozen ViT encoder and the LLM decoder of Qwen3-VL-8B. UIPress combines depthwise-separable convolutions, element-guided spatial reweighting, and Transformer refinement to compress ${\sim}$6{,}700 visual tokens to a fixed budget of 256. Together with Low-Rank Adaptation (LoRA) on the decoder to bridge the representation gap, the entire system adds only ${\sim}$21.7M trainable parameters (0.26\% of the 8B base model). Under a fair comparison on the same base model against four baselines on Design2Code, UIPress at 256 tokens achieves a CLIP score of 0.8127, outperforming the uncompressed baseline by +7.5\% and the strongest inference-time method by +4.6\%, while delivering 9.1$\times$ time-to-first-token speedup. To the best of our knowledge, UIPress is the first encoder-side learned compression method for the UI-to-Code task.
