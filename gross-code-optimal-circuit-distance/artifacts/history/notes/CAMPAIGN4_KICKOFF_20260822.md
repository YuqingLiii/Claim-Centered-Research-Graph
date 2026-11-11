# CIRCDIST 战役-4 续跑指令(2026-08-22,Lead/调度 = Fable 5,执行 = Opus 5)

你是 circdist 项目的 ProofPilot 调度/督导 session。上一战役(战役-3)已在 SCHEDULER.yaml 记为
spent 25/25、cap closed、zero reserve。本指令**开启战役-4,目标:把四个 open question 尽力跑完**。
先重载状态,再排序派单。DISK 永远优先于本指令;若冲突,报告冲突,不要静默解决。

## 第 0 步 — 重载(任何数学/派单之前,完整按序读盘)
1. `research/DAG_PROTOCOL.md`(全文;特别是 §3 六级证据表与谁能写、§5 更新协议、§6 节点审计、rule 6
   完成级必须独立评审、rule 8e 子节点须带组合蓝图)。
2. `research/FILE_PROTOCOL.md`(§4 放置、§5 命名、§6 原子更新、§9 收尾)。
3. `research/VALUATION_PROTOCOL.md`(§1–§9;拍卖排序只推荐"下一步在哪做",绝不改数学状态)。
4. `research/circdist/notes/CIRCDIST_PROBLEMS.md`(冻结题面;注意 circdist 无 README.md,题面在此)。
5. `research/circdist/notes/SAT_RESCOPE_20260822.md`(**今天 15:06–15:08 第四题重构说明,最新**)。
6. `research/circdist/proof-dag/NODE_INDEX.md`,然后四个 outcome 节点及其全部子节点:
   `CIRCDIST.gross` / `CIRCDIST.cplx` / `CIRCDIST.lift` / `CIRCDIST.sat`。
7. `research/circdist/notes/SCHEDULER.yaml`(战役-3 账本;本战役在其后追加,不改历史)。

## 第 1 步 — 项目状态报告(动手前先输出)
逐一给出四个 outcome 节点:当前 level(照盘读)、最强 live 子节点、卡点一句话、引用盘上文件。
再跑 `python3 tools/proofpilot_rank.py`(circdist)得到排序表;若 SCHEDULER.yaml 缺本战役 work_items,
先按下方"四题攻坚清单"补齐 work_items 的 {P, D_sessions, s_sessions} 再排序。报告与盘一致后方可派单。

## 第 2 步 — 战役-4 预算(授权)
- 用户已授权新一轮。建议上限 **~40 worker sessions**(4 题 × 侦察/攻坚/独立评审;实际拆分你按排序定,
  写进 SCHEDULER.yaml budget,total_sessions 追加、ledger 逐条记 tokens 便于校准)。
- **每题设 stop-loss**:花超其预算盒且无 level 提升,就把当前最小残差写成精确子节点、降级记录,转下一题。
- 纪律(战役-3 教训,必须继承):委托 prompt **禁止 worker 侧再生子代理(FIX-1)**、单 session、
  停损、结算条件、标签纪律——用 `proofpilot_rank.py --commission <node>` 机械生成,不要凭记忆写。

## 第 3 步 — 四题攻坚清单(每条独立 Opus 5 session,完成级必须另派独立评审)
**① CIRCDIST.gross(D*_Gross)** — dext-cap 已 CERTIFIED*(每调度 d_ext≤11),mc-equiv 已 REFUTED。
   D*∈{11,12} 未定。DEM 级直接认证被墙(数周集群 CPU),SBB Thm-1 归约是唯一可行认证路。优先跑
   **gap-forcing no-go**(证每个调度都有权重-11 witness 且交错单值相消 ⇒ D*=11)与**对称子类穷举**
   (25920 个平移不变最小深度调度,witness 认证界);若能定 D*=11,gross 根可升。BB 自同构对称(~70×)
   用来压 360 列 extended-code 最小距离认证规模。争取:D*=11 闭合;若 12 真不可达,给出 no-go 证明。
**② CIRCDIST.cplx(Eff-Preserve 复杂度)** — 固定 d∈NP、d 为输入∈Σ₂ᴾ(upper 已 CONJ)。缺口是
   **sigma2(Σ₂ᴾ-hard)仍 OPEN**;补上即得 Σ₂ᴾ-complete。若硬,则坐实 **islands(P/FPT 子类,现实头条)**
   + fixed-d NP-complete(用已修复的 coupling gadget,注意 padding 在 weight-4 作为定理失败,已记录)。
**③ CIRCDIST.lift(d_circ=d_eff 充要刻画)** — iff/nonint/gap-example 三子节点已 CERTIFIED*,但根仍 CONJ。
   任务:按 rule 8e 把组合蓝图**写成可评审的散文组合证明**,独立评审后把根升到完成级。这是四题里最接近
   闭合的一个,优先做。
**④ CIRCDIST.sat(d_∞, R_stab)** — 今天刚重构(旧 R_sat 退化,已冻结)。三子任务(AND-route):
   `transfer`(min-plus 有限状态表示的通用证明,现仅 d=3 surface 复现 Stim)、`window`(有限窗口定理,
   最强:d_R 单调 + min witness 占 ≤weight 连续轮 ⇒ R_stab≤d_∞≤d,有草图 + 7610 调度零反例)、
   `instances`(surface d=5,7 独立 transfer 校验 + hook-misaligned 臂 + 至少一个 qLDPC 实例 + witness 级
   机制归因)。三条齐 + 约定对齐审计,才能装配根。**诚实纪律:"从未观测 R_stab>1" 只是数值缺席,不是定理。**

## 第 4 步 — 诚实与收尾(每个 session 强制)
- 无独立评审不得写完成级(CERTIFIED*/PROVED/REFUTED);自作工作永不自带完成级(rule 6)。
- 证不出就把残差缩到最小精确子节点,如实标 CONJECTURED/NUMERICAL/OPEN,**不 overclaim**(KSUM/SE 教训:
  空心内审放行 + 话术夸大都要避免;数值≠证明)。
- 收尾必过:`python3 tools/proof_dag_check.py --problem circdist`、`tools/literature_check.py`、
  `tools/check_event_append_only.py --base-ref HEAD` 全 exit 0;`--write-generated` 重生 NODE_INDEX/GRAPH;
  节点文件/索引/图/大纲/"Most recent change" 头四处同步后再停。留下不同步或未记录结果的 session 记 INCOMPLETE。

目标复述:**尽力闭合四个 open question;闭不了的,给出精确的最小残差 + 诚实标签。质量优先于数量。**
