# CIRCDIST — four open problems on circuit distance of syndrome-extraction schedules

Lead commission, 2026-08-20. This file is the frozen problem statement set for the `circdist`
project (four independent problems, shared common definitions). It is also the live test of the
valuation/scheduling layer (`research/VALUATION_PROTOCOL.md`): Fable 5 dispatches and supervises;
Opus 5 sessions execute proofs and reasoning.

Ground rules for every worker session: no Lean; numerical simulation never substitutes for
mathematical proof; computational search may generate conjectures and evidence, but final results
need checkable proofs or proof certificates.

---

## 公共定义

研究对象固定为 CSS 稳定子码

Q = [[n, k, d]]

以及单辅助比特、CNOT-based syndrome extraction circuit。每个稳定子生成元使用一个辅助比特,辅助比特
准备一次、测量一次,并与该生成元支撑上的每个数据比特作用一次 CNOT。

统一使用:

d_eff(M) := d_ext(E(M)),

即由调度 M 所产生的全部 terminal residual/hook errors 构造 extended code 后得到的距离。

完整电路距离定义为

d_circ(C) = min{ |F| : F 不触发任何 detector,但翻转非平凡逻辑量 }.

在标准 memory experiment、相同 elementary-fault 权重和理想最终读出边界下:

d_eff(M) <= d_circ(C(M)) <= d.

非交错电路已知满足 d_circ = d_eff。

四个课题都不讨论 Lean,也不以数值模拟代替数学证明。计算搜索可以用于发现猜想和证据,但最终结果需要
可核查的证明或证明证书。

---

## 课题一:Gross code 的最优 circuit distance(node `CIRCDIST.gross`)

### 核心问题

考虑 Gross code Q_Gross = [[144,12,12]] 的所有合法单辅助比特 CNOT syndrome-extraction schedules,
包括 X/Z CNOT 相互交错的调度。

令 S_Gross 表示所有满足以下条件的调度:

- 每个 weight-6 stabilizer 使用一个辅助比特;
- 每条需要的 CNOT 恰好执行一次;
- 同一时刻一个物理比特最多参与一个二比特门;
- 允许 X-check 与 Z-check 的 CNOT 交错;
- 不允许额外 flag ancilla、cat state 或改变 stabilizer generating set;
- 无意义的空闲层应当压缩掉。

定义 D*_Gross = max_{M in S_Gross} d_circ(C(M))。要求严格确定 D*_Gross。

### 已知结果

现有工作证明:d_circ(C(M)) <= 11 对所有非交错调度成立。论文还给出了一个 conjectured distance-11
电路,但尚未完全证明其距离确实为 11;并明确留下:是否存在 d_circ = 12 的交错调度?

因此完整任务分成两部分:

1. 严格证明现有候选电路的 d_circ = 11;
2. 证明以下二者之一:存在 M 使 d_circ(C(M)) = 12,或对所有 M 有 d_circ(C(M)) <= 11。

### 建议证明路线

- 利用 Gross code 的平移、交换 X/Z、辅助比特和逻辑对称性压缩调度空间;
- 为 weight-6 check 的 90 种 inequivalent residual sets 增加时间 detector signature;
- 将调度问题表示为局部顺序变量及全局冲突约束;
- 若构造 distance-12 调度,必须证明所有 weight-<=11 故障均不可能成为 undetectable logical;
- 若证明 no-go,需要从任意合法调度中构造一个 weight-<=11 logical fault witness。

### 最低验收结果

至少完成下列之一:

- 严格证明候选电路 d_circ = 11;
- 对一个有意义的大子类(例如 translation-invariant 或三色周期交错调度)确定最优距离;
- 完整证明 D*_Gross = 11 或 12。

---

## 课题二:d_circ = d_eff 的 closed-lift 判据(node `CIRCDIST.lift`)

### 核心问题

研究 graph-like detector error model 中,effective logical 为什么有时能成为完整 circuit logical,
有时却被中间时间 detector 阻止。

设 G_circ 是完整时空 detector graph;G_eff 是忽略中间时间 detector、只保留 terminal residual
effects 后得到的 effective graph;pi: G_circ -> G_eff 是压缩时间方向的投影。

目标是建立一个严格的 graph-covering、voltage-graph 或 chain-complex 框架,并证明类似下面的必要
充分条件:

d_circ = d_eff  当且仅当  存在 gamma in L_eff, |gamma| = d_eff, volt(gamma) = 0,

其中 L_eff 是 G_eff 中的非平凡逻辑环集合;volt(gamma) 表示该环在时间 detector 方向上的总
syndrome/monodromy;voltage 为零表示 gamma 能够无额外故障地提升为 G_circ 中的闭合逻辑环。

更完整的目标公式是

d_circ = min_{gamma in L_eff} { gamma 的最短闭合时空 lift 的长度 }。

### 必须解决的技术问题

1. 严格定义从 full detector model 到 effective model 的投影;
2. 说明何时该投影是 graph covering,何时只能看成 branched covering 或 chain map;
3. 证明完整时空 logical 投影后一定是 effective logical;
4. 刻画一个 effective logical 能否同权重闭合提升;
5. 处理 detector boundary 和 logical boundary;
6. 从一般定理推出:non-interleaved ==> d_circ = d_eff。

### 希望得到的进一步结果

- 给出一个 d_circ > d_eff 的显式交错例子;
- 定义 completion gap g(C) = d_circ(C) − d_eff(M);
- 用 voltage、monodromy 或同调 obstruction 解释 g(C) > 0;
- 给出不需要构造完整多轮电路的等号判定算法。

### 最低验收结果

在 graph-like、固定边界的模型下,给出一个非平凡的必要充分条件,并严格证明其同时覆盖:非交错等号;
至少一个交错严格不等号例子。

---

## 课题三:保距调度存在性的计算复杂度(node `CIRCDIST.cplx`)

### 核心问题

研究的不是"给定调度后计算距离有多难",而是:是否存在一个调度,使 effective distance 达到理论码距?

定义 promise decision problem: Eff-Preserve。

输入:CSS check matrices H_X, H_Z;已知且经过 promise 保证的静态距离 d;允许的 CNOT
interaction/conflict graph;可选深度上限 T。

问题:是否存在 M 使 d_eff(M) = d?

使用 promise"静态距离已知为 d"是为了避免把一般 quantum-code distance 本身的困难混入本问题。

### 目标复杂度结果

第一部分:固定常数 d。由于可以多项式枚举所有少于 d 个故障,问题属于 NP。目标是证明在尽量严格的
限制下仍然 NP-complete,例如:stabilizer weight 至多 4 或 6;Tanner degree 有界;每个 check 只
允许两个或少数几个局部 CNOT order;CSS code;固定 d = 3、4 或其他小常数。

第二部分:d 是输入的一部分。问题具有量词结构

存在 M,使得对所有 F, |F| < d: F 不是 undetectable logical。

因此自然的上界候选是 Sigma_2^P。目标是确定其准确复杂度,优先尝试证明 Eff-Preserve 是
Sigma_2^P-complete。

### 建议归约路线

可以尝试从以下问题归约:QSAT_2;Betweenness;ordering CSP;Not-All-Equal SAT。

基本编码思想:每个 check 的 CNOT 相对顺序编码存在变量;低权 fault configuration 编码全称变量;
某个 fault configuration 成为逻辑错误,当且仅当对应布尔赋值违反原公式。

### 可选扩展

定义完整电路版本 Circ-Preserve: 存在 M 使 d_circ(C(M)) = d,并比较 Eff-Preserve 与
Circ-Preserve 的复杂度是否相同。

还可以寻找 tractable islands,例如:Tanner graph 为树或有界 treewidth;HGP 及高维 HGP;固定
check weight 和固定逻辑维数。

### 最低验收结果

至少得到以下之一:固定 d 情况下的 NP-hardness/completeness;一般情况下严格的
polynomial-hierarchy 分类;一个非平凡受限码类的多项式算法,并证明正确性。

---

## 课题四:重复 syndrome rounds 的精确 saturation 定理(node `CIRCDIST.sat`)

### 核心问题

固定一个单轮 syndrome-extraction schedule M。令 C_R(M) 表示将同一轮 M 重复 R 次,并添加标准
初始化和最终理想数据读出所得到的 memory circuit。定义 d_R(M) := d_circ(C_R(M))。

进一步定义 saturation index:

R_sat(M) = min{ R_0 : d_R(M) = d 对所有 R >= R_0 }。

如果不存在这样的 R_0,定义 R_sat(M) = 无穷。

研究目标:1. 判断 R_sat(M) 是否有限;2. 若有限,确定或界定其大小;3. 区分限制距离的机制究竟来自:
单轮 hook/bulk mechanism;timelike measurement mechanism;初末边界;跨多轮的混合 spacetime
mechanism。

### 目标定理

将每轮边界 syndrome 看成有限状态,构造带权状态转移系统或 min-plus transfer matrix A,使得
d_R(M) 可以由 A^R 的某个矩阵元素表示。

证明一个 pumping/finite-window theorem:若某个任意长的 C_R(M) 中存在 weight-<d 的 undetectable
logical,那么存在一个长度至多 B(r,d) 的电路也包含这种 logical。这里 r 是跨轮 syndrome-state
space 的维数,B(r,d) 是明确可计算的函数。

由此得到:R_sat(M) < 无穷 可以通过有限多个 R 的检查决定,而不是检查无限多轮。

### 建议证明路线

- 状态记录一轮结束时的 syndrome/boundary charge 和 logical parity;
- elementary faults 对应带非负权重的状态转移;
- weight-<d 的 logical mechanism 只访问有限多个状态;
- 若一个过长的无故障区间出现重复状态,则删除或 pumping 该区间;
- 对 graph-like model,将问题化为周期图条带中的最短非平凡路径;
- 对一般 detector hypergraph,再尝试用 binary matroid 或 trellis 推广。

### 与已有 composition theorem 的区别

已有 stabilizer-channel 工作给出了保证任意组合保持距离的充分局部条件,并提出检查长度约 d+1 的
局部组合。本课题要求的是:固定周期 extractor M;必要且充分,而不只是充分;精确描述
R -> d_R(M);求出最小的 R_sat;明确拆分 hook、measurement 和 boundary 的贡献。

### 最低验收结果

至少在 graph-like periodic extractor 上完成:有限状态或 min-plus 表述;finite-window/pumping
theorem;一个明确的 B(r,d);在 surface-code schedule 和至少一个 qLDPC schedule 上算出或严格
界定 R_sat。

---

## 四个课题的核心输出

| 课题 | 最终要回答的问题 |
|---|---|
| 1 (gross) | Gross code 的最优值究竟是 11 还是 12? |
| 2 (lift) | 什么结构条件精确保证 d_circ = d_eff? |
| 3 (cplx) | 决定"是否存在达到 d_eff = d 的调度"有多难? |
| 4 (sat) | 固定调度后,需要重复多少轮才能稳定达到 d_circ = d? |
