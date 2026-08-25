# Set Equality 修复包 v2 外部复审报告

**复审日期：**2026-07-30  
**复审对象：**`se_review_package_v2_20260729.zip`  
**对照对象：**上一轮外审报告 `SE_external_review_20260729.md`  
**审查方式：**以 TeX、Markdown 节点、认证原文和精确复现脚本为主；数值判断均以整数或有理数复算，不由浮点数反推分数。

## 总结判词

| 任务 | 判词 | 结论 |
|---|---|---|
| T1′ 逐项修复复核 | **CONFIRM-WITH-ISSUES** | A.2 的乘积级修复、Schur–Weyl 支撑、Schur lift、非严格上界和新增 H4 均在数学上成立；但“等价”措辞、部分 DAG 当前状态及修复脚本存档仍未完全同步。 |
| T2′ 四义务规约完备性 | **CONFIRM-WITH-ISSUES** | **H1∧H2∧H3∧H4 足以推出定理 B；未发现隐藏的 H5。** 四节点与四假设在数学核心上对应，但并非严格逐字一致，且 DAG 的传播拓扑仍有元数据债务。 |
| T3′ 自由全面重审 | **CONFIRM-WITH-ISSUES** | 定理 A 的完整数学证明已闭合；论文的证据边界总体诚实。新发现主要是一个全局范数/逐 sector 量词错位、见后才定义的 witness 简写、以及复现记录不自洽。 |

> **定理 A 的证明（含 2026-07-29 修正案）我确认无保留。**

这里的“无保留”指数学陈述、证明链、量词和常数；下文列出的认证节点措辞、DAG 元数据和复现存档问题不构成定理 A 的数学缺口。

---

# 0. 包完整性与 append-only 核查

## 判词：PASS

1. `MANIFEST.sha256` 共列出 65 个文件，逐项执行 SHA-256 校验为 **65/65 PASS**；该文件不含 UTF-8 BOM。与上一包的 BOM 卫生问题相比，此项已修复。
2. v1 与 v2 的认证文件逐字节比较结果：
   - 旧文件 SHA-256：`a045781c3e8280ec1a8ac879ea12089b47cf9e8134cc70b3698ad0ffffb76293`；
   - 新文件 SHA-256：`4911ad56e1cd38398526af652e5cd9098b0eb2ea060d55ce6655263fc216fb81`；
   - 新文件以前一文件的全部字节为严格前缀；
   - `git diff --no-index --numstat` 为 **333 insertions, 0 deletions**。
3. 修正案自行记录旧哈希、触发原因和 append-only 纪律，见
   `03_theoremA_certification/se_cor16_certification_20260723.md:890-915`；其“被取代内容”与“不受影响内容”分别列于 `:1143-1167`、`:1169-1187`。

未发现旧认证正文被静默改写。

---

# T1′ — 逐项修复复核

## 总判词：**CONFIRM-WITH-ISSUES**

## T1′-1：A.2 的 append-only 乘积级修复

### 判词：PASS

### 1. 原错误识别正确

修正案明确撤销

\[
J_NP_k^{\rm amb}=P_k^{\rm leg}J_N,
\]

并正确指出 `P_k^{amb}` 含 exact-weight 因子，不属于纯位置群代数；合法集合的位置不变性不足以使它单独 intertwine。见
`03_theoremA_certification/se_cor16_certification_20260723.md:917-961`。其 `n=1,q=2,k=0` 反例以精确值 `1/4` 复现，见 `:931-953`。这一判断与上一轮外审一致。

### 2. Lemma A.2′ 的证明成立

#### (a) 权重吸收

修正案从

\[
\Psi_0=\Psi_0(\Pi_0\otimes\Pi_0),\qquad
\Psi_1=\Psi_1(\Pi_1\otimes\Pi_0+\Pi_0\otimes\Pi_1)
\]

推出每个 `|c|=k` 张量只接受总权重 `k`，所以

\[
W_{{\rm se},k}=W_{{\rm se},k}P_{{\rm wt},k}.
\]

见认证文件 `:1010-1025`，论文同步证明见
`01_paper/se_explicit_witness.tex:338-370`。matching 只重排输入槽，不改变总权重，论证对所有 matching 成立。

#### (b) Schur–Weyl 支撑

exact-weight-`w` 半空间作为位置群模写成

\[
\operatorname{Ind}_{S_w\times S_{m-w}}^{S_m}
(H_1^{\otimes w}\boxtimes\mathbf 1).
\]

对 `H_1^{⊗w}` 的每个不可约分量应用 Pieri：增加大小 `m-w` 的 horizontal strip；这些新增盒子占据 `m-w` 个不同列，因此最终分拆第一行长度至少 `m-w`，即 position defect 不超过 `w`。于是

\[
P_{m,w}D_u^{(m)}=0\quad(u>w).
\]

在两半展开 `P_{wt,k}` 与 `Q_k^{pos}` 后，存活项同时满足
`u≤w_A`、`v≤w_B` 及 `u+v=w_A+w_B=k`，强制 `u=w_A,v=w_B`，故

\[
P_{{\rm wt},k}Q_k^{\rm pos}
=Q_k^{\rm pos}P_{{\rm wt},k}=P_k^{\rm amb}.
\]

见认证文件 `:1027-1063`，论文 `:372-391`。该论证没有调用 LR occurrence-space transport，也没有遗漏 `k>n` 的形式范围：在空层上等式退化为零等式。

#### (c) 纯位置 projector 的合法 intertwining

`Q_k^{pos}` 属于 `Z(C[S_n×S_n])`，而合法 NO 集合对两半内部的位置置换不变，因此

\[
J_NQ_k^{\rm pos}=Q_k^{\rm leg}J_N.
\]

见认证文件 `:1065-1075`。结合权重吸收得到真正需要的乘积级恒等式

\[
\mathcal R(W_{{\rm se},k}P_k^{\rm amb})
=\frac1{q!}W_k^{\rm leg}Q_k^{\rm leg},
\]

见 `:1077-1091`；论文对应 `01_paper/se_explicit_witness.tex:393-407`。

### 3. 类型、重数与分子均闭合

修正案逐一写出 ambient/legal map 尺寸，并明确此引理不进入任何 multiplicity space，见
`03_theoremA_certification/se_cor16_certification_20260723.md:1093-1100`。纯位置 defect projector 对常向量的作用给出

\[
Q_k^{\rm leg}\mathbf1=0\ (k>0),\qquad
Q_0^{\rm leg}\mathbf1=\mathbf1,
\]

所以 `Γ_n 1=K1` 和 `||Γ_n||≥K` 仍精确成立，见 `:1102-1108`。

### 结论

上一轮 T1-G1 已被正确、局部、无新增分析假设地修复；witness、归一化、分子、通道估计和常数均未改变。

---

## T1′-2：H2/H3 的 Schur lift 与类型修复

### 判词：PASS，附一项逐字对齐问题

论文现在明确区分：

- 完整 sector carrier
  `H_ξ≅V_κ⊗V_ν⊗C^c` 上的 `dc×dc` 算子；
- multiplicity trace 输出的 `c×c` block；
- 两者之间必须有 `I_{V_κ⊗V_ν}⊗(·)` lift。

关键位置为：

- H-twirl 本身带 lift：`01_paper/se_explicit_witness.tex:1095-1104`；
- `G_can` 的 full-carrier 类型及 lift 必要性：`:1136-1154`；
- 候选 H2 恒等式：`:1156-1182`；
- 猜想 H2 的正式陈述：`:1250-1263`；
- H3 全载体 sandwich：`:1265-1281` 和 `:1689-1706`。

冻结 H2 节点也使用同一类型：
`02_dag/nodes/SE.denom.Phi.legal.gram.interface.yaml:21-29`；H3 节点只冻结 sandwich 与 full-multiplicity NO polar，见
`02_dag/nodes/SE.denom.Phi.legal.omega.interface.yaml:21-26`。

**未再发现任何承重的 `dc×dc = c×c` 直接等式。**

但“逐字一致”仍不是严格成立：论文 H3 的显示式把由 H2 立即推出的第二个等号也写在 H3 内
(`01_paper/se_explicit_witness.tex:1270-1279`)，而 H3 节点只冻结 sandwich 与 NO polar
(`omega.interface.md:21-26`)。这不增加数学假设，因为论文明确说第二等号来自 H2；最小编辑是把第二等号移至 H3 陈述之后，写成 “H2+H3 consequently imply …”。

---

## T1′-3：`≤`、`r_top<6/5` 与 taper 范围

### 判词：数学修复 PASS；三处“等价”措辞 FAIL

### 1. 非严格上界修复正确

由 H1 的 PSD 非严格界与 H2 恒等式只能推出

\[
\|G_{\rm can}^{\lambda,\xi}\|
\le \frac{15}{4}r_{\rm top},
\]

论文现已明确写成 `≤`，并解释此步不能产生严格性，见
`01_paper/se_explicit_witness.tex:1326-1354`。

### 2. 严格 `9/2` 的正确判据与证明成立

因为

\[
\frac92=\frac{15}{4}\frac65,
\]

需要的是 `r_top<6/5`，而不是上一轮报告误写的 `r_top<3/2`。论文正确利用 active taper 条件

\[
k=j+1<K\quad\Longrightarrow\quad K\ge j+2
\quad\Longleftrightarrow\quad n\ge(j+2)^3,
\]

再分 `j=1` 与 `j≥2` 证明 `r_top<6/5`；见
`01_paper/se_explicit_witness.tex:1356-1397`。其中 `j≥2` 的精确包络
`E≤7/48` 和 `e^E≤48/41<6/5` 正确。

独立精确 hook 扫描确认：

- `(j,n)=(1,3)` 时 `(15/4)r_top=9/2`；
- `(2,6)` 时为 `5`，`(2,8)` 时为 `60/13`，说明宽窗口 `n≥3j` 内严格界确会失败；
- 在 `n=(j+2)^3` 的边界，`j=1,…,6` 的最大值均严格小于 `9/2`。

### 3. 新发现：`r_top<6/5` 与 `n≥(j+2)^3` 并不等价

以下三处把二者写成“等价”或 `⟺`：

- `00_REVIEW_PROMPT_V2.md:21-23`；
- `05_repair_record/se_paperrev5_changelog_20260729.md:614-620`，尤其 `:617`；
- `02_dag/SE_PROOF_DAG.md:1641-1644`。

这是逻辑错误。反例：`j=1,n=4` 时

\[
r_{\rm top}=\frac87<\frac65,
\]

但 `n=4<27=(j+2)^3`。正确关系是：

> `k=j+1<K` 与 `n≥(j+2)^3` 等价；这一 taper 条件是论文用来证明 `r_top<6/5` 的充分条件，而非后者的必要条件。

**类别：**量词/逻辑等价。  
**影响：**不影响论文证明，因为论文正文 `:1360-1363` 只使用正确的蕴含。  
**最小修复：**将三处 “equivalently/⟺” 改为上述两句。

---

## T1′-4：H4 的注册与论文接入

### 判词：PASS

H4 节点明确要求实际 legal lower block 有正交、穷尽、无 residual sector 的 Schur 分解，并把 H2/H3 的 multiplicity blocks 指认为这些实际 sector blocks，进而给出全局范数等于最大 sector 范数：

`02_dag/nodes/SE.denom.Phi.legal.sect.yaml:21-31`。

论文正式陈述与之对应，见
`01_paper/se_explicit_witness.tex:1283-1299`。在 omega-decay 证明中，论文也明确指出 H4 是从逐 sector bound 到全局 `||C_{j+1→j}||` 的唯一桥梁，见 `:1814-1825`。

这正好填补上一轮发现的缺环；没有把 FOUND 的 caveated `⊗I_c` 结论悄悄升级为已证事实。H4 仍标 OPEN，见 `SE.denom.Phi.legal.sect.yaml:40-50,73-76`，状态诚实。

---

## T1′-5：上一轮 T4 卫生项是否全部落实

### 判词：PARTIAL

已经落实的项目包括：

- assembly 标题从 “Certified content” 改成 “Conditional content”：
  `02_dag/nodes/SE.denom.assembly.yaml:29-33`；
- GRAM/OMEGA 的 open obligations 不再写 None：
  `SE.denom.Phi.legal.gram.yaml:50-56`、
  `SE.denom.Phi.legal.omega.yaml:61-67`；
- 论文 H2 disclaimer 前置并带 `(H2)` tag：
  `01_paper/se_explicit_witness.tex:1156-1178`；
- `rawT_a/rawT_b` 在 H1 前定义：`:1214-1233`；
- 论文明确记载旧 paperaudit3 的相关结论被 supersede：`:2478-2508`；
- manifest 无 BOM。

但仍有下列未同步问题：

### T1′-I1：assembly 仍称 OPEN 输入为 “certified tame bound”

- **位置：**`02_dag/nodes/SE.denom.assembly.yaml:33`。
- **类别：**状态/表述越界。
- **问题：**同一段已经标为 conditional，却仍写 `C_Y=15/4 from the certified tame bound`；`tame` 当前为 OPEN。
- **最小修复：**改成 “from the assumed H1–H4/tame operator inputs” 或 “conditional tame bound”。

### T1′-I2：TAME 的当前状态公式遗漏新增 SECT 子节点

- **位置：**`02_dag/nodes/SE.denom.Phi.legal.tame.yaml:29-35`；对照 frontmatter `:5-12` 与 Dependencies `:44-48`。
- **类别：**DAG 状态公式/依赖闭包。
- **问题：**当前状态仍写成 `min(gram,omega,trace,found)`，没有 SECT；但 children 已包括 SECT。
- **最小修复：**更新为 `min(gram,omega,trace,found,sect)`，并注明 entry (90)/(91)。

### T1′-I3：GRAM/OMEGA 父节点的 kind、children 与 Dependencies 冲突

- **位置：**
  - `SE.denom.Phi.legal.gram.yaml:1-12,32-36`；
  - `SE.denom.Phi.legal.omega.yaml:1-12,43-47`。
- **类别：**DAG 拓扑/元数据。
- **问题：**frontmatter 标 `kind: LEAF` 却列出 interface child；Dependencies 又写 `Children: none`。此外 GRAM Claim 仍保留旧严格 `<`（`:24-26`），OMEGA Claim 仍把带 `θ` 的逐-sector 右端写成全局 norm（`:24-30`）。
- **最小修复：**要么将父节点改为 AND/consequence 节点并同步 children，要么取消传播 child、以 related 表示；同时把父 Claim 同步为 rev5 的 consequence 形式。

### T1′-I4：COR 当前状态仍反复写 “CERTIFY, no caveats”

- **位置：**`02_dag/nodes/SE.br.cor16.yaml:29-45,53-57,67-72,74-77`。
- **类别：**认证状态/历史与当前状态混淆。
- **问题：**该节点已记录外审发现 A.2 为假及修正义务，但 Current status、旧 work record、Evidence/Status history 仍把 “no caveats” 当作当前描述；Open obligations 仍写没有新义务。
- **最小修复：**Current status 应写为“原认证 verdict 经 2026-07-29 append-only amendment 修复，现由本次独立复审确认”；历史条目可以保留，但加 `SUPERSEDED AS CURRENT DESCRIPTION`。

### T1′-I5：assembly 的 AND 拓扑仍没有 children

- **位置：**`02_dag/nodes/SE.denom.assembly.yaml:1-12,35-41`。
- **类别：**DAG 规约传播。
- **问题：**文件诚实披露该债务，但自动图上不能由 H1–H4 状态传播到 assembly。
- **最小修复：**建立一个明确的 conditional consequence AND 节点，children 至少指向 T6、GRAMI、OMI、SECT（或经同步后的 TAME），再供 assembly 使用。

这些是包结构与状态标注问题，不是定理 A 或条件定理 B 的新增数学义务。

---

# T2′ — H1∧H2∧H3∧H4 ⇒ 定理 B

## 判词：**CONFIRM-WITH-ISSUES**

## T2′.1 条件规约的数学链完整

固定 active defect `j`、shape `θ` 和 admissible sector `ξ`。

### 第一步：H1+H2 给出 canonical Gram bound

H2 写成 full-carrier Schur lift：

\[
G_{\rm can}^{\lambda,\xi}
=I_{V_\kappa\otimes V_\nu}\otimes
\frac{r_{\rm top}}{B_\theta(q)^2\omega}M_\xi.
\]

H1 给出

\[
M_\xi\preceq\frac{15}{4}B_\theta(q)^2\omega I_c.
\]

因标量为正且 identity lift 保范数，得到

\[
\|G_{\rm can}^{\lambda,\xi}\|
\le\frac{15}{4}r_{\rm top}.
\]

论文逐步推导见
`01_paper/se_explicit_witness.tex:1326-1354`。

### 第二步：H3 给出 sector lower-block bound

H3 提供

\[
C_{\lambda,\xi}^*C_{\lambda,\xi}
=C_{N,\rm prob}^{1/2}G_{\rm can}^{\lambda,\xi}C_{N,\rm prob}^{1/2},
\quad
C_{N,\rm prob}=r_{\rm top}\omega I.
\]

结合已证的

\[
\omega\le\frac{j}{q-2j}=\frac{j}{2(n-j)}
\]

（论文 `:1521-1524`），得到

\[
\|C_{\lambda,\xi}\|^2
\le \frac{15}{8}r_{\rm top}^2\frac{j}{n-j}.
\]

见论文 `:1799-1816`。

### 第三步：H4 把 sector 界提升到实际全局 block

H4 明确无 residual sectors，且

\[
\|C_{j+1\to j}\|
=\max_{\lambda,\xi}\|\widetilde C_{\lambda,\xi}\|.
\]

因此上一步不是对任意 compression 的孤立估计，而确实控制 assembly 所用的实际 legal lower block。见论文 `:1814-1825` 和 H4 节点 `:21-31`。

### 第四步：已证的 defect assembly 给出常数

论文的正交 regrouping 与固定 defect 内三角不等式见
`01_paper/se_explicit_witness.tex:1898-1951`。令 `ρ_d=max_θ r_top` 后，新增第四项为

\[
\sqrt{\frac{15}{8}}\,\alpha_{d+1}\sqrt{\frac d{n-d}}.
\]

在线性 taper 下，两个非消失的极限项都含

\[
f(x)=(1-x)\sqrt x,
\qquad \max_{0\le x\le1}f(x)=\frac{2}{3\sqrt3}.
\]

精确符号化简为

\[
M=\frac{2}{3\sqrt3}
\left(\sqrt2+\sqrt{\frac{15}{8}}\right)
=\frac{4\sqrt6+3\sqrt{10}}{18},
\]

以及

\[
\frac1{2(1+M)}
=\frac9{18+4\sqrt6+3\sqrt{10}}
=0.2413852814754581733126245049897285\ldots .
\]

见论文 `:1954-2004`。精确符号复算无误。

## T2′.2 是否存在第五义务 H5？

**未发现。**

上一轮缺失的所有内容均集中在“实际全局 lower block 是否由写出的 sectors 穷尽、以及 multiplicity lift 是否正是实际块”这一环；H4 已把下列事项一次性冻结：

1. `S_q` 与固定查询位置子群 `H` 的 intertwining；
2. orthogonal decomposition；
3. exhaustiveness；
4. no residual sectors；
5. H2/H3 blocks 与实际 `\widetilde C_{λ,ξ}` 的一致性；
6. 全局 norm=max-sector-norm，含所有 `c≥1`。

余下进入定理 B 的输入——`ω` 范围、X/Y/diagonal-Φ 界、hook envelope、cross-defect orthogonality、mask 因子 2、分子 `K` 和 taper 算术——均在条件假设之外已有独立证明。没有再出现需要另立命题的 operator substitution。

DAG 尚不能机械传播四个节点的状态，是元数据问题，不是数学上的 H5。

## T2′.3 四假设与四冻结节点是否“逐字一致”

### 数学核心对应关系

| 论文假设 | 冻结节点 | 评价 |
|---|---|---|
| H1 | `SE.denom.Phi.legal.trace.t6` | 主体 PSD 式、`J`、常数与方向一致；T6 Claim 另列 CT/JT 充分目标，不属于 H1 本体。 |
| H2 | `SE.denom.Phi.legal.gram.interface` | 类型、lift、标量及 `c` 说明一致；仅名称 `G_can^full|Hξ` 与 `G_can^{λξ}` 不同，论文 `:1151-1153` 已说明二者相同。 |
| H3 | `SE.denom.Phi.legal.omega.interface` | 核心 sandwich+NO polar 一致；论文把 H2 推出的第二等号写进同一 display，故非严格逐字。 |
| H4 | `SE.denom.Phi.legal.sect` | 基本逐字采用，包含 exhaustiveness、no residual sector 和 norm equality。 |

因此应表述为“**四假设与四节点在冻结的数学义务上逐项对应**”，不宜声称完全逐字相同。

---

# T3′ — 自由全面重审与新发现

## 判词：**CONFIRM-WITH-ISSUES**

## T3′.1 定理 A 完整证明链

在用 Lemma A.2′ 替换旧 A.2 后，我重新核查了以下承重环节：

1. 合法 YES/NO 空间与 `1/q!` 归一化：
   `03_theoremA_certification/se_cor16_certification_20260723.md:49-87,129-161`，修正后由 `:1077-1091` 提供 projector 级结论；
2. exact numerator：`:180-194` 与修正案 `:1102-1108`；
3. mask 代表和因子 2：`:196-265`；
4. X/Y defect pinning、C 的 `k-1/k` 支撑及全部 LR multiplicity：`:267-330`；
5. whole-isotypic completion scalar及 hook envelope：`:332-420`；
6. BR:1307 倒数修复与 `√3`：`:422-470`；
7. defect assembly、整数最大值、half-swap 及 `2/√6`：`:476-568`；
8. 完整量词、严格 `q=2n`、`n≥8` 与 uniform `o(1)`：`:832-886`。

修正案只替换合法 level atom 的进入方式，不触碰第 3–8 项。未发现新的类型、重数、归一化或量词缺口。

**结论：定理 A 的证明（含修正案）确认无保留。**

## T3′-N1：omega-decay proposition 的全局范数/逐 sector 量词错位

- **位置：**`01_paper/se_explicit_witness.tex:1790-1798`；正确的两阶段推导见 `:1814-1823`。
- **类别：**量词/类型。
- **问题：**命题先说“on every admissible strict sector”，但显示式左边写全局
  `||C_{j+1→j}||`，右边却保留单个 sector 的 `θ` 依赖。全局 norm 不能同时对每个不同 `θ` 被各自右端控制；它应取 `max_θ`，即 `ρ_j`。
- **正确版本二选一：**
  1. sector 版本：
     \[
     \|\widetilde C_{\lambda,\xi}\|
     \le\sqrt{15/8}\,r_{\rm top}(2n,j,\theta)\sqrt{j/(n-j)};
     \]
  2. 全局版本：
     \[
     \|C_{j+1\to j}\|
     \le\sqrt{15/8}\,\rho_j\sqrt{j/(n-j)},
     \quad \rho_j=\max_{\theta\vdash j}r_{\rm top}(2n,j,\theta).
     \]
- **影响：**非阻断。证明正文 `:1814-1823` 已按“先 sector、后 H4、再外层 θ 最大值”正确操作，assembly `:1942-1951` 也使用 `ρ_d`。
- **最小修复：**把命题陈述拆成上述两行。

## T3′-N2：witness 简写在定义之前出现，形式上先天 ill-typed

- **位置：**摘要 `01_paper/se_explicit_witness.tex:52-58`、定理 A `:122-127`；简写约定直到 `:427-431` 才给出。
- **类别：**类型/记号作用域。
- **问题：**按首次出现的字面定义，`W_k^{leg}` 是 legal map，而 `\bar\Pi_{se,k}` 是 ambient projector，二者不能相乘。后文才说明该符号实际代表 `W_k^{leg}Q_k^{leg}`。
- **影响：**读完整文后无歧义，不影响数学；但摘要或定理被单独引用时会复现上一轮的类型误读。
- **最小修复：**摘要和定理直接写 `W_k^{leg}Q_k^{leg}`，或在定理前先定义该 shorthand。

## T3′-N3：修复记录中的脚本 SHA-256 错误

- **位置：**`05_repair_record/se_paperrev5_changelog_20260729.md:251-257`。
- **类别：**复现/完整性。
- **问题：**正文称脚本 SHA 为
  `89958a55b448f4f7bed5206c1a6400df698b4a65d4f56f0beb4bc32e2792d23f`；包内实际脚本、`SHA256SUMS.txt:1` 和 MANIFEST 一致为
  `0c0497b230fdd8685cd3efa046741b31d4ccb092945540c5322671b6a5c6fa8e`。
- **最小修复：**更正正文哈希，说明它对应最终存档脚本。

## T3′-N4：归档脚本/日志不能复现表中 C8

- **位置：**
  - C8 被列为已执行检查：`se_paperrev5_changelog_20260729.md:259-270`；
  - C8 代码只附在 changelog：`:551-596`；
  - 实际归档脚本止于 `05_repair_record/logs_se_paperrev5_20260729/verify_repair.py:220`，仍运行旧的 `r_top<3/2` C7 spot checks：`:205-220`；
  - 归档日志止于 `verify_repair.log:38`，无 C8 输出；
  - DAG 却称脚本已存档并 re-run exit 0：`02_dag/SE_PROOF_DAG.md:1649-1651`。
- **类别：**复现覆盖范围。
- **问题：**C8 数学结果本身经我独立精确复算为正确，但当前“归档脚本+日志”并不能重跑它。
- **最小修复：**把 C8 代码并入最终脚本、重新生成日志和 SHA；或者把表述改成“C8 代码仅在 changelog 附录中，未包含于归档 re-run”。

### 附带小项：C5 对 `k=0` 的脚本断言不足

Changelog `:267` 称脚本精确检查了 `Q_0^{leg}1=1`；实际脚本
`verify_repair.py:160-167` 对 `k=0` 只打印 `killsconst=False`，并没有断言归一化后的 `Q_0^{leg}1=1`。该数学事实由纯位置 trivial projector 立即成立，也已在证明中使用；这里仅是脚本覆盖说明过度。

## T3′-N5：DAG 仍有当前态与历史态混杂

除 T1′-I1 至 I5 外，父 GRAM/OMEGA 节点仍保留旧 Claim：

- GRAM `SE.denom.Phi.legal.gram.yaml:24-26` 写严格 `<` 与宽范围 `n≥3j`；
- OMEGA `SE.denom.Phi.legal.omega.yaml:24-30` 把带 `θ` 的 sector 右端直接赋给全局 norm。

这些节点可作为历史 consequence 记录保留，但应在 Claim 顶部加 `SUPERSEDED FOR CURRENT CONDITIONAL REDUCTION`，并把当前正式 consequence 指向 rev5 proposition；否则后续自动审计可能再次把旧陈述当成冻结目标。

## T3′.2 证据边界

### 判词：PASS

论文对有限证据的定位仍然明确：

- “finite all-pass never a proof”：`01_paper/se_explicit_witness.tex:2027-2035`；
- 人审拆除的 c>1 transport、frame Gram、twirl、colored-orbit 和 sandwich 问题没有被重新包装成已证：`:2460-2476,2510-2520`；
- 外审修复、H4 注册和内部/无优先权声明均明确：`:2478-2508,2522-2527`。

未发现把有限 gate 当成证明、把 `(G)/(SC)` 等充分路线反例说成 H1 原命题反例、或把条件定理 B说成无条件定理的越界。

---

# 最小修复清单

按优先级建议：

1. **论文正式陈述：**修正 omega-decay proposition 的 sector/global 量词
   (`se_explicit_witness.tex:1790-1798`)。
2. **冻结语义：**将论文 H3 的 H2-consequence 第二等号移出 H3 本体，以实现与 OMI 节点真正逐字一致
   (`:1265-1281`)。
3. **逻辑措辞：**把 prompt、changelog、DAG 中
   `r_top<6/5 ⟺ n≥(j+2)^3` 改成正确的“taper 等价 + 充分蕴含”。
4. **记号：**在摘要和定理 A 中直接使用 `W_k^{leg}Q_k^{leg}`，或提前定义 shorthand。
5. **DAG 同步：**更新 TAME 状态公式、GRAM/OMEGA kind/children、assembly conditional wording 与 children、COR 当前状态。
6. **复现存档：**更正 verifier SHA；把 C8 纳入实际脚本与日志；把 C5 的 `k=0` 断言写实。

上述各项都不是新的 H5，也不改变定理 A、条件定理 B 或其常数。

---

# 最终总判词

**CONFIRM-WITH-ISSUES：上一轮的两个阻断性数学 GAP 均已闭合；定理 A（含修正案）无保留确认，H1∧H2∧H3∧H4 对定理 B 的规约完整且不存在隐藏 H5，但论文局部量词、冻结文本逐字对齐、DAG 当前态和复现存档仍需上述非阻断修订。**
