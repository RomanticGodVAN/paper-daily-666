# Document AI and OCR — 2026-06-08

- Papers: 4
- Skipped as duplicates: 0

## 1. TraRA: Trajectory-level Recognition Aggregation for Video Text Spotting in Urban Surveillance

- arXiv: `2606.07161`
- Link: https://arxiv.org/abs/2606.07161
- Announcement date: 2026-06-08
- Categories: cs.CV
- Tags: video text spotting, scene text, text recognition
- Reason: Central task is video text spotting in surveillance, directly OCR-related.

### Abstract

Video Text Spotting (VTS) is essential for urban surveillance and intelligent transportation systems, enabling automated reading of street signs, vehicle markings, and scene text in video streams. However, reliable recognition remains challenging due to dynamic video factors common in surveillance scenarios, including motion blur, occlusion, and scale variation, which degrade frame-level recognition. Existing VTS methods typically perform recognition independently on each frame, leading to inconsistent and inaccurate results across sequences. To address these limitations, we propose TraRA (Trajectory-level Recognition Aggregation for VTS), a plug-and-play method that performs trajectory-level text recognition by leveraging temporal and multimodal consistency. TraRA integrates two key modules: (1) the Temporal Clustering and (2) the Vision-Language Aggregation. The former refines noisy trajectories by grouping temporally and visually coherent text instances, while the latter employs a Low-Rank Adaptation-enhanced Vision-Language model to fuse visual cues with linguistic context across frames. By aggregating information over entire text trajectories, TraRA achieves robust text recognition even under challenging surveillance conditions. Extensive experiments on four public benchmarks, including road and urban scene datasets (RoadText, BOVText, ArTVideo, and ICDAR15), demonstrate that TraRA consistently improves tracking and recognition performance over state-of-the-art VTS methods. The source code is available at https://github.com/trid2912/TraRA.

## 2. FLOWREADER: Min-Cost Flow Optimization for Multi-Modal Long Document Q&A

- arXiv: `2606.07235`
- Link: https://arxiv.org/abs/2606.07235
- Announcement date: 2026-06-08
- Categories: cs.IR, cs.LG
- Tags: document QA, multimodal, evidence assembly
- Reason: Focuses on long multimodal document Q&A with tables, slides, figures; core document AI.

### Abstract

Long, multimodal documents force retrieval-augmented systems to assemble answers from evidence fragmented across text, tables, and slides broken across cells in a long table, spread over multiple slides, or split between a figure and its discussion. Top-$k$ chunk retrieval treats each fragment independently and cannot represent how evidence connects. We introduce FLOWREADER, which reframes evidence assembly as a min-cost flow problem on a multimodal node graph: a single scoring vector $h$ controls source selection (via MMR), sink selection (via a length-aware answerability proxy), and the costs and capacities of every edge. The optimal flow is decomposed into candidate evidence paths, a compact non-redundant subset is selected by entropy-regularized replicator dynamics, and parallel VLM workers under a dual-process gate produce the answer with a single System-2 refinement pass triggered when answer consistency is low or the routed flow is strained. On VisDoMBench, FLOWREADER is best on the two subsets dominated by fragmented evidence PaperTab ($58.40$, $+1.30$ over G^{2}-Reader) and SlideVQA ($72.93$, $+0.62$) and competitive on SPIQA, FetaTab, and SciGraphQA. Macro-averaged across all five subsets, FLOWREADER ($65.47$) is within $0.74$ of the strongest baseline (G^{2}-Reader, $66.21$). Overall, these results show that min-cost flow performs well on fragmented multimodal evidence, where top-$k$ retrieval fails. It also provides a unified way to control scoring, routing, selection, and adaptive compute together.

## 3. Closed-Form Spectral Regularization for Multi-Task Model Merging

- arXiv: `2606.07289`
- Link: https://arxiv.org/abs/2606.07289
- Announcement date: 2026-06-08
- Categories: cs.CV, cs.LG
- Tags: OCR, model merging, multi-task
- Reason: Paper explicitly evaluates on OCR benchmark and includes OCR as a task in multi-task merging.

### Abstract

Model merging combines several independently fine-tuned experts into a single multi-task model without any training data, reducing the storage, serving, and decentralized-development costs of large foundation models. State-of-the-art merging methods formulate merging as a layer-wise quadratic interference minimization problem. Although this problem admits an exact closed-form pseudoinverse solution, that solution underperforms hundreds of iterations of gradient descent in practice. The iterative loop dominates the cost of the pipeline, yet its effectiveness has remained unexplained. We revisit this regime and show that the iterative solver does not primarily act as an optimizer; rather, it serves as an implicit spectral regularizer for an ill-posed normal equation, where small-eigenvalue directions of the per-layer interference operator amplify proxy noise. Building on this finding, we formalize multi-task model merging as a noisy linear inverse problem and propose a spectral filtering estimator parameterized by a per-direction filter. We instantiate this estimator with SWUDI, a closed-form method that combines a soft exponential filter, which matches the gradient-flow trajectory of iterative descent, with a hard top-K truncation that suppresses noise-amplifying small-eigenvalue directions. Furthermore, we propose SWUDI-A, an adaptive variant that replaces the global rank hyperparameter with per-layer rank rules, further improving robustness across architectures. Both variants share a single symmetric eigendecomposition per linear layer and require no training data or optimizer state. Across four general benchmarks and a multimodal merging benchmark spanning VQA, Geometry, Chart, OCR, Grounding, and modality merging, our proposed spectral solvers match or outperform state-of-the-art merging methods. Crucially, they reduce wall-clock time by 28-72x and peak GPU memory by up to 50%.

## 4. RealDocBench: A Benchmark for Field-Level QA and Layout Understanding on Real-World Regulated Documents

- arXiv: `2606.07401`
- Link: https://arxiv.org/abs/2606.07401
- Announcement date: 2026-06-08
- Categories: cs.CV
- Tags: document parsing, layout understanding, benchmark, OCR
- Reason: Central task is document parsing and layout understanding on real-world documents.

### Abstract

Document parsing systems are increasingly deployed in high-stakes, regulated workflows such as mortgage underwriting, financial reporting, supply-chain logistics, and clinical records. Yet most public benchmarks evaluate parsers on clean academic layouts or synthetic prose, and report a single OCR or markdown-level similarity score. Such documents and metrics correlate poorly with what downstream agents actually need: the correct value for a specific field on a messy real-world page. We introduce RealDocBench, a two-track benchmark built from real regulated documents. The QA track contains 1,356 field-level questions over 581 documents spanning four domains, where each question is paired with a typed gold_dict of key-to-value answers and parsers are scored on both per-field and strict per-question accuracy. The layout track contains 1,500 human-verified page images annotated with COCO-style bounding boxes under a nine-class public taxonomy, scored with a Hungarian matcher that includes adjacency-aware split/merge recovery. We evaluate eighteen systems, spanning commercial parsing APIs, general-purpose VLMs, and open-source OCR models, under a uniform extraction-and-scoring protocol, and report accuracy alongside per-page cost and cache-busted latency. RealDocBench exposes a wide performance spread that single-number benchmarks hide, a persistently hard medical sub-domain, and sharp cost/latency trade-offs across operating points. We release the datasets, parser adapters, and evaluation harness to support reproducible, field-level comparison of document parsing systems.
