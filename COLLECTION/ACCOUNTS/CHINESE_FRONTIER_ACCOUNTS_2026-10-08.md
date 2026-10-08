# Chinese GitHub Frontier Accounts — Collection Capture — 2026-10-08

Purpose: preserve the discovered Chinese technical frontier accounts for later account-wide enumeration, extraction and dedupe. This record is preservation/triage only.

## Accounts captured

| Account | GitHub owner | Public repos observed | Scope status |
|---|---|---:|---|
| Huawei | Huawei | 100 | BOUNDED first page |
| Alibaba | alibaba | 100 | BOUNDED first page |
| Ant Group | antgroup | 73 | returned inventory |
| ByteDance | bytedance | 100 | BOUNDED first page |
| Baidu | baidu | 100 | BOUNDED first page |
| Tencent | Tencent | 100 | BOUNDED first page |
| PingCAP | pingcap | 100 | BOUNDED first page |
| StarRocks | StarRocks | 53 | returned inventory |
| Fit2Cloud | Fit2Cloud | 12 | returned inventory |
| Milvus | milvus-io | 68 | returned inventory |
| Zilliz | zilliztech | 75 | returned inventory |
| ESPRESSIF | ESPRESSIFSystems | 4 | returned inventory |
| DaoCloud | DaoCloud | 100 | BOUNDED first page |
| SelectDB | SelectDB | 7 | returned inventory |

## High-value triage

- Huawei: Huawei_LiteOS_Kernel, gophercloud, cloud-sdk-python, cloud-sdk-go, cloud-sdk-java, containerops, fpga-accel, DMM.
- Alibaba: arthas, nacos, canal, page-agent, spring-ai-alibaba, GraphScope, ROLL, MNN, zvec, lowcode-engine, SREWorks, EasyCV, xquic, havenask.
- Ant Group: vsag, MCPScan, agent-aegis, sofa, DeepXTrace, Finova, OmniKV, sglang, ANT-Fin-RAG, ant-kuberay, adversarial-ai-coding-plugin.
- ByteDance: deer-flow, UI-TARS-desktop, trae-agent, UI-TARS, sonic, LatentSync, MegaTTS3, Elkeid, terarkdb, appshark, SandboxFusion, vArmor, byteir, agentkit-samples, Lance.
- Baidu: Unlimited-OCR, braft, BaikalDB, EasyFaaS, Curve, QCompute, paddle-on-k8s-operator, dperf, openrasp, DuReader.
- Tencent: WeKnora, ncnn, MMKV, tinker, mars, BrowserSkill, AI-Infra-Guard, matrix, libco, TNN, Tendis, phxpaxos, tquic, TencentOS-kernel, flare.
- PingCAP: tidb, autoflow, ossinsight, tidb-operator, tiflash, tiflow, chaos, tidb-dashboard, tidb-lightning, tidb-vector-python, full-stack-app-builder-ai-agent, agent-rules, tidb-cloud-backup.
- StarRocks: starrocks, mcp-server-starrocks, starrocks-debug-skills, starrocks-kubernetes-operator, dbt-starrocks, starcache, airbyte-starrocks, helm-charts.
- Fit2Cloud: riskscanner, rackshift, LLM-CodeReview-Action, aliyun-oss-plugin, jenkins-s3-plugin.
- Milvus: milvus, pymilvus, milvus-lite, knowhere, milvus-operator, milvus-model, milvus-storage, milvus-insight, milvus-sdk-rust, towhee.
- Zilliz: deep-searcher, GPTCache, claude-context, memsearch, VectorDBBench, mcp-server-milvus, zilliz-mcp-server, milvus-skill, zilliz-skill, vector-graph-rag.
- ESPRESSIF: esp-open-sdk, Arduino.
- DaoCloud: dao, karmada-operator, ContextStore, HAMi, daocloud-skills, charts-syncer, dao-runtime, DeepGEMM, public-image-mirror, crproxy.
- SelectDB: dbt-doris, doris-new-mcp, selectdb-cloud-skills, datax-selectdb.

## Collection boundary

Discovery/preservation is not installation, integration, execution or production readiness. Large accounts with 100 results are explicitly bounded, not claimed exhaustive. Before extraction: enumerate the owner, inspect all relevant repositories, preserve provenance/revision/license/dependencies, and semantic-dedupe against COLLECTION and canonical Skills. Red line: do not reimplement an existing capability; extract only a proven-gap improvement.