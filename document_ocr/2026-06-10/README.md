# Document AI and OCR — 2026-06-10

- Papers: 3
- Skipped as duplicates: 0

## 1. KCSAT-ML: Probing Reasoning Models with Nationwide-Cohort Human Difficulty

- arXiv: `2606.10403`
- Link: https://arxiv.org/abs/2606.10403
- Announcement date: 2026-06-10
- Categories: cs.CL
- Tags: OCR, math reasoning, benchmark, VLM
- Reason: Uses OCR to process math problems from exam images; OCR is a core component for evaluating VLMs on this benchmark. Central to document image understanding.

### Abstract

Math reasoning benchmarks have proliferated, yet most lack a per-item difficulty signal grounded in actual human performance. We introduce KCSAT-ML, a decade (2014-2025) of Korean College Scholastic Ability Test (KCSAT; Suneung) mathematics: 664 problems with a 339-item core set carrying official per-item error rates from nationwide cohorts of hundreds of thousands of examinees. We pair the benchmark with Difficulty-aligned Reasoning Gain (DRG): a score-orthogonal metric that asks whether a model's mistakes concentrate on the items humans found hard, or on items humans found easy. Together they expose, across a wide range of VLMs (and LLMs via OCR), three patterns: (i) low-budget accuracy collapses on the high-human-error tail at every model size; (ii) test-time scaling (TTS) raises token use roughly linearly with cohort error rate, while accuracy gains follow a non-monotonic curve; (iii) within a single family, TTS flips between anti-scaling on the hardest items and overthinking on easier ones -- two faces of the same alignment failure. On DRG, models with near-identical accuracy can sit at near-opposite values: one model gets wrong what humans also find hard, while another solves the hardest items yet fails on items humans find easy -- a contrast that aggregate accuracy hides. Our code and dataset builder will be open-sourced at https://github.com/naver-ai/KCSAT-ML.

## 2. ChartLens: A Dual-Branch Framework for Chart Data Correction and Factual Summary Refinement

- arXiv: `2606.10640`
- Link: https://arxiv.org/abs/2606.10640
- Announcement date: 2026-06-10
- Categories: cs.CV
- Tags: chart understanding, OCR, data extraction, summary generation
- Reason: Central task is chart understanding from images, involving OCR for data extraction and structured output. Directly targets document AI.

### Abstract

In this report, we present our champion solution for the DataMFM Challenge Track 2: Chart Understanding. This track requires models to recover structured chart data and generate faithful natural-language summaries from chart images. To address the complementary requirements of accurate data extraction and factual narration, we propose ChartLens, a dual-branch framework for chart data correction and summary refinement. ChartLens consists of two key modules: Structure-Aware CSV Verification and Correction (SAVC) and Text-Retention-Guided Summary Refinement (TRSR). SAVC improves the reliability of structured data extraction through verification and correction, while TRSR enhances summary generation by preserving critical textual and numerical evidence from charts. By combining model adaptation, correction-based generation, and OCR-assisted evidence grounding, ChartLens improves both structured data recovery and summary factuality. On the test set, our final system achieves an overall score of 69.10 and ranks first in Track 2, demonstrating its effectiveness for accurate chart understanding. Our code will be released at: https://github.com/iLearn-Lab/CVPRW26-ChartLens.

## 3. Mind the Gap: Can Frontier LLMs Pass a Standardized Office Proficiency Exam?

- arXiv: `2606.10956`
- Link: https://arxiv.org/abs/2606.10956
- Announcement date: 2026-06-10
- Categories: cs.AI, cs.CL
- Tags: document automation, office proficiency, document understanding
- Reason: Paper evaluates LLMs on office automation tasks involving Word, Excel, PowerPoint documents, which requires document understanding and manipulation.

### Abstract

The deployment of Large Language Model (LLM) agents for computer automation is accelerating, yet their ability to navigate complex, professional-grade productivity software is largely untested. We argue that Office automation is an ideal environment for benchmarking document-automation capability, as it requires long-horizon planning and reasoning, precise parameter configuration, and multi-application integration. To quantify this capability, we introduce an evaluation based on China's National Computer Rank Examination (NCRE), featuring 200 comprehensive practical-operation tasks across Word, Excel, and PowerPoint. Each task is scored on a 100-point rubric scale using 7,118 machine-gradable criteria, and Score Rate (SR) denotes the mean percentage of rubric points earned across these tasks. We benchmark 7 frontier LLMs and observe stark limitations: single-turn models score a maximum of 36.6%. A stronger agentic system with execution feedback, iterative repair, and broader Office automation access reaches 68.8%, but remains below the 95.5% community-reference score used as a scoring sanity check. Ultimately, our experiments demonstrate that despite recent advancements in code generation, achieving reliable fine-grained Office document automation remains a significant challenge for current code-generating LLM and agent systems.
