# Set Equality 成果外部审查报告

**审查日期：**2026-07-29  
**审查范围：**审查包 `se_review_package_20260729.zip` 中的定理 A、猜想 H（H1/H2/H3）、条件定理 B 规约链及证据边界。  
**完整性检查：**`MANIFEST.sha256` 所列 67 个载荷文件全部逐字节通过 SHA-256；清单首行含 UTF-8 BOM，标准 `sha256sum -c` 会对首行给出格式警告，但去除 BOM 后该项哈希也匹配。这是打包卫生问题，不影响数学内容。

## 结论摘要

| 任务 | 判词 | 核心结论 |
|---|---|---|
| T1 定理 A 正确性 | **CONFIRM-WITH-ISSUES** | 主体证明链和常数成立；但认证报告及论文使用了一个错误的“精确权重投影与合法限制相互 intertwine”恒等式。该错误有一个三行的、保持同一 witness 与全部常数不变的乘积级修复。 |
| T2 H1/H2/H3 陈述一致性 | **GAP** | H1 基本一致；论文 H2 与冻结 GRAM 节点的 Claim 不是同一命题，且把全载体算子与 `c×c` multiplicity block 直接相等，类型不合；H3 也不是 OMEGA 节点 Claim 的逐字冻结版。 |
| T3 规约完备性 | **GAP** | H1/H2/H3 经类型修正后确实推出论文中的逐 sector bound 和最终常数；但从逐 sector compression 到实际全局 lower block 的正交、穷尽分解及 multiplicity lift 没有被 H1/H2/H3 或包内无 caveat 的认证完整覆盖。需要一条明确的第四义务 H4，或将其证明作为前置引理收入论文。 |
| T4 证据边界诚实性 | **CONFIRM-WITH-ISSUES** | 论文主体对“有限证据不是证明”和“充分条件反例不是 H1 反例”的表述总体诚实；但若干 DAG/旧审计文字仍把条件装配称为 certified、把 CONJECTURED 节点写成无开放义务，并错误宣称 H2/H3 与节点完全一致。 |

---

# T1 — 定理 A 正确性

## 判词：**CONFIRM-WITH-ISSUES**

### T1.1 已独立核验并确认的主链

1. **归一化与分子。**在 `q=2n` 时，NO/YES 两个合法集合大小均为 `q!`，matching stack、两个 probability-
   `L^2` restriction 与 raw kernel 的公共系数合成恰为 `1/q!`；见
   `03_theoremA_certification/se_cor16_certification_20260723.md:129-161`。对 `k=0`，
   `W_0^{leg}` 是全一矩阵；对 `k>0`，合法位置 defect projector 湮灭常向量，所以
   `Γ_n 1=K1`、`||Γ_n||≥K` 精确成立；见同文件 `:182-194`。这里没有额外的 `n!` 或 `q!` 因子。

2. **菱形代表与 mask 因子 2。**X/Y/Z/C 分解及 `Z_k` 与 `-X_{k-1}` 的 masked equality 给出合法代表；
   equal-symbol 部分是行列同时按查询字母分块的压缩，故其范数不超过原矩阵范数，从而
   `||Γ∘Δ_i||≤2||D||`；见认证报告 `:196-265`。

3. **defect 支撑和 LR 重数。**X/Y 被钉在 defect `k`，C 仅落在 `k-1,k`；LR sector 的实际维数写为
   `f^σ f^{σ'} c`，证明只使用 `c>0` 和 first-row inequality，不使用 occurrence-space transport；见
   `03_theoremA_certification/se_cor16_certification_20260723.md:267-330,613-629,644-657`。
   completion/forgetting 证明是整个 isotypic component 上的向量不等式，而不是选定 copy 的标量式；
   其完整推导见 `03_theoremA_certification/se_one_defect_forgetting_bound.md:100-158,160-273`。

4. **hook 包络。**精确乘积和对数界给出 `ρ_d=1+O(n^{-1/3})`，对 `q=2n`、`d≤K` 及所有
   `θ⊢d` 一致；见认证报告 `:394-418`。

5. **BR:1307 修复和环境常数。**BR 原文先说明特殊路径含
   `2^{(|P|-2)/2}` 个等模正交项且最多两个存活，却在下一行误印成增长因子；见
   `03_theoremA_certification/references/BR_1310.5185v4_collision.tex:1292-1308`。
   正确投影因子为 `2^{-(|P|-4)/4}`；与 row-count/cycle 因子组合后的平方为
   `((|P|+2)/2)2^{-max(0,|P|-4)/2}`，在偶数 `|P|` 上于 `|P|=4` 取最大值 3；见认证报告
   `:422-470` 和 blind line-read `se_phi_blind_lineread_codex_20260717.md:79-93`。
   精确值依次为 `|P|=2:2`、`4:3`、`6:2`，此后递减。因此 `√3` 和
   `||T_k||≤√6/√(n-2k+1)` 正确。

6. **装配与常数。**不同 alphabet defect 的 domain/range 正交；固定 defect 内只用三角不等式。
   主要增长项的整数最大值精确为 `floor((K-1)^2/4)`，所以
   `||D||≤(√6/4+o(1))n^{1/6}+O(1)`，mask 后为 `(√6/2+o(1))n^{1/6}`；见认证报告
   `:476-568`。除以 `K=floor(n^{1/3})` 给出 `2/√6`。

7. **量词。**`q=2n` 是严格等式；分析证明从 `n≥8` 起适用，因为此时 `K≤n/3` 且所有 BR 分母为正；
   `o(1)` 对查询位置、taper、shape 和所有 `c≥1` 一致。ε–N 表述完整且没有声称有效的 `N(ε)`；见
   `03_theoremA_certification/se_cor16_certification_20260723.md:473-474,838-886`。未发现量词缺口。

### T1-G1：认证报告的 projector intertwining 恒等式为假

- **位置：**
  - `03_theoremA_certification/se_cor16_certification_20260723.md:115-127`（A.2）；
  - 同文件 `:157-162`（由 A.2 得 A.5）；
  - 同文件 `:617-620,668-670,700-711`（类型表和“仅记号修复”的判断）；
  - `01_paper/se_explicit_witness.tex:229-248,294-304`（论文同一论证）。
- **类别：****类型 / 投影 intertwining**。
- **问题：**`P_k^{amb}` 不只是 position-group central projector；它还包含 exact tensor-weight projector。
  合法输入集在 `S_n×S_n` 下不变，只能直接推出 coordinate restriction 与 position group algebra
  中的 projector 相互 intertwine，不能推出它与 exact-weight projector intertwine。exact-weight projector
  会把非法列的 delta 函数投影成在合法列上非零的函数。
- **最小反例：**取 `n=1,q=2,k=0`，令 `f=δ_(1,1)`，其中 `(1,1)` 是非法 NO word。
  合法 restriction 满足 `J_N f=0`；但 exact-weight-0 projector 将 `f` 投到非零常向量，随后 restriction 非零。
  因此不存在认证报告所写的 `J_NP_0^{amb}=P_0^{leg}J_N`。
- **影响：**A.2、论文 `eq:level-normalization` 的 operator-level 证明及“零 caveat”字样不能原样保留。
  但这不推翻定理 A，因为所需的是 **`W_{se,k}P_k^{amb}` 的乘积级 restriction identity**，而不是
  `P_k^{amb}` 单独 intertwine。
- **完整的局部修复：**令 `Q_k^{pos}` 是两半 position defects 总和为 `k` 的纯 position central projector，
  `P_{wt,k}` 是 exact total weight projector。由 Schur–Weyl 支撑，半边 position defect 不超过该半边 weight，
  因而在 exact-total-weight-`k` 子空间上，BR 的 `\bar\Pi_{se,k}` 与 `Q_k^{pos}` 相同。另一方面，
  `Ψ_0` 只接受 pair-weight 0，`Ψ_1` 只接受 pair-weight 1，所以从定义直接有
  
  ```text
  W_{se,k}=W_{se,k}P_{wt,k},
  W_{se,k}\bar\Pi_{se,k}=W_{se,k}Q_k^{pos}.
  ```
  
  `Q_k^{pos}` 属于 position group algebra，故合法 restriction 真正满足
  `J_NQ_k^{pos}=Q_k^{leg}J_N`。于是
  
  ```text
  R(W_{se,k}\bar\Pi_{se,k})
    =R(W_{se,k}Q_k^{pos})
    =(1/q!) W_k^{leg}Q_k^{leg}.
  ```
  
  这正是后续证明和 VERDICT 中实际使用的合法 witness，其中
  `P_k^{leg}` 本来就被定义成纯 position central projector
  (`se_cor16_certification_20260723.md:838-850`)。修复不改变 Γ、分子、任何通道或常数。
- **最小文本修复：**删除 A.2；将 A.5 前的论证替换为上述乘积级 lemma；论文
  `se_explicit_witness.tex:296-303` 同步替换；类型表注明“单独的 ambient projector 不 intertwine，
  但左乘 `W_{se,k}` 后可消去 weight projector”。

### T1 最终判断

定理 A 的数学陈述和 `2/√6` 常数可确认；认证报告不是“逐字零缺陷”，而是含一个明确的错误恒等式。
由于上面的局部修复从冻结的 `Ψ_0,Ψ_1,\bar\Pi_{se,k}` 定义直接推出、且不新增估计或假设，判为
**CONFIRM-WITH-ISSUES**，而不是 GAP。

---

# T2 — H1/H2/H3 冻结陈述一致性

## 判词：**GAP**

### T2.1 H1：主体一致

- 论文 `01_paper/se_explicit_witness.tex:1047-1065` 与 T6 Claim
  `02_dag/nodes/SE.denom.Phi.legal.trace.t6.yaml:24-44` 在对象、方向和常数上相同：
  `J=ω²rawT_a+rawT_b=d Tr(M_ξ)`，`M_ξ⪯(15/4)B_θ(q)²ωI_c`。
- 物理 `ω=(1-p_0)/p_0`、`p_0=f^{(q-j-1,θ)}/f^{(q-j,θ)}` 写对，未偷换成 taper proxy；
  见论文 `:1048-1054`，以及 T6 对错误 proxy 的撤回说明 `:104-120`。
- **小缺口（定义/自包含性）：**论文在 `:1057-1064` 首次正式使用 `rawT_a,rawT_b`，但在猜想陈述前
  没有给出它们作为哪两个 physical branch trace 的公式。最小修复是在 H1 中加入二者的冻结定义或
  精确引用定义式。另应将“every LR multiplicity copy”改成“every sector, uniformly for every `c≥1`”，
  因为 `M_ξ` 是同时作用于全部 copies 的 `c×c` block，而不是逐 copy 的标量。

### T2-G1：论文 H2 与冻结 GRAM 节点不是同一个命题

- **位置：**
  - 论文 H2：`01_paper/se_explicit_witness.tex:1067-1075`；
  - 冻结 GRAM Claim：`02_dag/nodes/SE.denom.Phi.legal.gram.yaml:24-30`；
  - T6 明确把 coefficient/interface 单列为开放义务：
    `02_dag/nodes/SE.denom.Phi.legal.trace.t6.yaml:60,81-83,128-133`。
- **类别：****陈述不一致 / 规约对象错置**。
- **问题：**论文 H2 是恒等式
  `G_can=[r_top/(B²ω)]M_ξ`；GRAM 节点的冻结 Claim 却是范数上界
  `||G_can||<(15/4)r_top`，并明确写着“NOT yet identified with the actual legal lower block”。
  节点状态段又说明 transport、frame Gram、twirl、coset coefficient 均未证。两者不是变量重命名，
  而是“接口恒等式”与“其下游范数结论”两个不同命题。
- **影响：**不满足任务要求的逐字一致性；当前 DAG 不能把论文 H2 的真实性归因于 GRAM Claim。
- **最小修复：**新建冻结节点（例如 `SE.denom.Phi.legal.gram.interface`）专门陈述 H2，令原 GRAM 节点
  作为 `H1∧H2` 的 consequence；或把 GRAM 节点 Claim 改写为接口恒等式并把 norm bound 移到子节点。

### T2-G2：H2 的全载体等式类型不合

- **位置：**
  - 严格载体 `\mathcal H_ξ≅V_κ⊗V_ν⊗C^c`：论文 `:815-838`；
  - multiplicity trace `\mathfrak m_ξ` 输出 `c×c`：论文 `:966-974`；
  - `G_can` 的原始定义作用于完整 `P`-carrier：论文 `:986-1000`；
  - `M_ξ=\mathfrak m_ξ(...)` 为 `c×c`：论文 `:1015-1024,1051-1054`；
  - H2 却称二者“as an operator on the whole carrier”直接相等：论文 `:1067-1075`。
- **类别：****类型 / 维数**。
- **问题：**完整 `G_can` 是 `dc×dc` 算子，`M_ξ` 是 `c×c` 算子。H2 缺少 Schur identity lift。
  后面的证明又与 `I_c` 比较（论文 `:1112-1116`），确认文本实际上把 `G_can` 当成 multiplicity block；
  而 H3 的 `C_N=r_topω I_{\mathcal H_ξ}` 又回到完整载体。
- **最小修复（二选一）：**
  
  ```text
  G_can^full|_{H_ξ}
    = I_{V_κ⊗V_ν} ⊗ \widehat G_ξ,
  \widehat G_ξ = [r_top/(B_θ(q)^2ω)] M_ξ,
  ```
  
  并在 H3 中使用 `I_d⊗\widehat G_ξ`；或者从一开始把 `G_can^{λ,ξ}` 定义为 multiplicity block，
  并在所有 full-carrier 式中显式写 `I_d⊗G_can^{λ,ξ}`。

### T2-G3：由 H1+H2 只能得到非严格上界

- **位置：**论文 `01_paper/se_explicit_witness.tex:1102-1123`；GRAM Claim
  `02_dag/nodes/SE.denom.Phi.legal.gram.yaml:24-26`。
- **类别：****不等式方向/严格性**。
- **问题：**H1 是 `M_ξ⪯(15/4)B²ωI_c`，H2 是等式，因此只能推出
  `G_can⪯(15/4)r_top I` 和 `||G_can||≤(15/4)r_top`，不能推出论文和节点写的严格 `<`。
- **影响：**不影响任何后续渐近常数；但正式陈述不成立。
- **最小修复：**将第一条改成 `≤`。绝对 `9/2` 可写 `≤9/2`；若需要严格 `<9/2`，对 `j≥2`
  可继续使用 `r_top<3/2`，而 `j=1` 单独给出非严格界即可。

### T2-G4：论文 H3 不是冻结 OMEGA Claim 的逐字版本

- **位置：**论文 H3 `01_paper/se_explicit_witness.tex:1077-1087`；OMEGA Claim
  `02_dag/nodes/SE.denom.Phi.legal.omega.yaml:24-30`。
- **类别：****陈述范围不一致**。
- **问题：**论文 H3 只假设 sandwich 与 NO polar；OMEGA 节点 Claim 则直接包括最终
  `||C_{j+1→j}||` 界、`ω`-range、GRAM bound 和定理 B 常数。论文的拆分在数学上更合理，
  但不满足“与节点冻结版逐字一致”。
- **最小修复：**将 OMEGA 节点拆成 `OMEGA.interface`（论文 H3）与 `OMEGA.consequence`
  （lower-block bound 和定理 B），然后让后者依赖 H1/H2/H3。

---

# T3 — H1∧H2∧H3 ⇒ 定理 B 的规约完备性

## 判词：**GAP**

### T3.1 条件算术本身正确

在将 H2 按 T2-G2 修成 full-carrier identity lift、并把严格 `<` 改成 `≤` 后，逐 sector 的推导成立：

1. H1+H2 给出 `||G_can||≤(15/4)r_top`。
2. H3 给出 `C^*C=C_N^{1/2}G_can C_N^{1/2}` 和 `||C_N||=r_topω`。
3. `ω≤j/[q-2j]=j/[2(n-j)]` 后，
   
   ```text
   ||C_{λ,ξ}||² ≤ (15/8) r_top² j/(n-j),
   ```
   
   即论文 `√(15/8)` bound；见 `01_paper/se_explicit_witness.tex:1494-1521`。
4. defect regrouping、固定 defect 内三角不等式和 taper 算术见论文 `:1590-1695`。
   精确符号重算给出
   
   ```text
   M = (2/(3√3))(√2+√(15/8))
     = (4√6+3√10)/18,
   1/[2(1+M)] = 9/(18+4√6+3√10)
              = 0.2413852814754581733126245049897… .
   ```

因此问题不在装配数值，而在逐 sector 假设如何覆盖实际全局算子。

### T3-G1：存在隐藏的第四条义务 H4（sectorization / identity lift / exhaustiveness）

- **位置：**
  - 全载体结构：`01_paper/se_explicit_witness.tex:815-838`；
  - H2/H3 的局部 compression：`:1067-1087,1284-1294,1400-1410`；
  - Proposition 的证明只控制 `C_{λ,ξ}`，但陈述和装配使用全局 `C_{j+1→j}`：
    `:1494-1517,1627-1641`；
  - FOUND 对 `c≥2` 仍带 caveat，且明确说逐 sector `⊗I_c` lift 曾“REFUTED AS TYPED”：
    `02_dag/nodes/SE.denom.Phi.legal.found.yaml:23-30,43-51`。
- **类别：****规约缺环 / 类型 / 穷尽性**。
- **问题：**H1/H2/H3 如今只对每个写出的 `C_{λ,ξ}` compression 作断言。要把这些局部界代入
  `final-envelope`，还必须证明 actual legal lower block 在 alphabet Fourier block 和 H-isotypic sectors
  上正交、无遗漏地分解，并且 full-carrier operator 是 irrep identity 与 multiplicity block 的张量积。
  论文没有给出一个可引用的全局 norm=max-sector-norm 命题；包内 FOUND 又没有无 caveat 地覆盖 `c≥2`
  compressed identity regime。
- **应补的最小义务 H4：**可冻结为：
  
  > **H4（实际 lower block 的穷尽 Schur 分解）。**对每个 active `j`，
  > `C_{j+1→j}` 是 `S_q` 及固定查询位置子群
  > `H=S_{n-1}×S_n` 的 intertwiner，并在实际 legal NO/YES spaces 上有正交、穷尽分解
  > 
  > ```text
  > C_{j+1→j} ≅ ⊕_{λ=(q-j,θ)} I_{S^λ} ⊗
  >               ⊕_{ξ=(κ,ν), admissible}
  >               ( I_{V_κ⊗V_ν} ⊗ \widetilde C_{λ,ξ} ),
  > ```
  > 
  > 不存在 residual sectors；H2/H3 中的 `c×c` blocks 正是这些
  > `\widetilde C_{λ,ξ}` 的 Gram/NO-polar blocks。因此
  > `||C_{j+1→j}||=max_{λ,ξ}||\widetilde C_{λ,ξ}||`，且该式对全部 `c≥1` 成立。

  若 FOUND 的底层证明事实上已经给出此定理，可不把它命名为 H4，但必须把相应 artifact 和无 caveat
  的跨栈审查放入包内，并在论文 Proposition 之前明确引用。当前包只给出 `CERTIFIED*` 摘要，不能完成外审确认。

### T3-G2：T6 只关闭 TRACE 的 PSD 目标，不能单独传递 `C_Y=15/4`

- **位置：**TRACE Claim
  `02_dag/nodes/SE.denom.Phi.legal.trace.yaml:24-36`；T6
  `02_dag/nodes/SE.denom.Phi.legal.trace.t6.yaml:24-44,128-133`。
- **类别：****规约依赖**。
- **问题：**T6/H1 与 TRACE 的现行 PSD target 相同，所以 `T6⇒TRACE` 这一 OR 分支关系成立；
  但 TRACE 和 T6 均明确说 canonical coefficient/GRAM connection 仍是独立义务。故
  “T6 的 15/4 直接变成 canonical `C_Y=15/4`”不成立；必须显式经过 H2。
- **最小修复：**在规约图上写成
  `H1(T6) ∧ H2(interface) ⇒ canonical Gram bound C_Y=15/4`，而不是 `T6⇒C_Y`。

### T3-G3：DAG 的状态/依赖闭包不能支持“只有三条义务”这一元结论

- **位置：**
  - TAME 是 `GRAM∧OMEGA∧TRACE∧FOUND`：
    `02_dag/nodes/SE.denom.Phi.legal.tame.yaml:29-48`；
  - FOUND 为 `CERTIFIED*`，开放 `c≥2` identity gate：
    `SE.denom.Phi.legal.found.yaml:27-30,49-51`；
  - assembly 是 `kind: AND` 但 `children: []`，并自认 dependency-modeling debt：
    `02_dag/nodes/SE.denom.assembly.yaml:1-12,29-41`；
  - closeout capability audit 也明确说即使 T6 成功，GRAM、OMEGA、FOUND caveat 和 assembly input 仍需关闭：
    `05_closeout_context/se_capability_audit_20260723.md:143-150`。
- **类别：****规约缺环 / 依赖闭包**。
- **问题：**论文把 H1/H2/H3 直接作为数学假设后，确实可以吸收 TRACE/GRAM/OMEGA 的大部分开放内容；
  但它没有吸收或证明 T3-G1 的 FOUND/sectorization 内容。DAG frontmatter 又没有表示 assembly 的真实孩子，
  因而不能用当前节点状态机械地证明规约闭合。
- **最小修复：**补 H4 或无 caveat foundation lemma；随后重接
  `assembly <- {OMEGA.consequence, sectorization}`，并把旧 adjudicated 状态与 frontmatter 同步。

### T3 最终判断

**经类型修复并补 H4 后，H1∧H2∧H3∧H4 ⇒ 定理 B 的数学链可确认；当前写成
H1∧H2∧H3⇒定理 B 尚未被包内材料完整证明。**因此 T3 判 **GAP**。

---

# T4 — 证据边界诚实性

## 判词：**CONFIRM-WITH-ISSUES**

### T4.1 主论文的边界表述总体合格

- 论文明确写出所有 finite “all pass” 只是证据、不是证明：
  `01_paper/se_explicit_witness.tex:1719-1727`。
- 六个 `c=2` 门和 107-gate ledger 被明确限定为有限证书，未声称关闭 H1：`:1729-1749`。
- raw T-a、(G)、(SC)、same-index/common-Q 的失败被准确限定为“充分 shortcut 被驳”，不是 H1/T6/SE 反例：
  `:1751-1774`。
- j=24 relative-9j reduction 被标为 proposer-level、pending review；`Q∈[0,10]` 内含阈值不能作方向性证据；
  `:2087-2112`。这一段诚实。

### T4.2 精确有理数抽查

所有下列比较均从所打印整数直接构造 `Fraction`，未从浮点反推：

| 项目 | 精确值 | 结论 | 包内位置 |
|---|---:|---|---|
| 旧 raw T-a，`n=18,c=2` | `36224413/28242984 > 1` | 旧分离式被驳 | `04_conjectureH_provenance/logs_se_trace_t5_uniform_ta_two_frame_20260722_REPORT.md:107-113` |
| 旧 raw T-a，`n=19,c=2` | `10611004/8023575 > 1` | 同上 | 同文件 `:107-113` |
| 粗 gate (G)，`j=8,n=24` | `457025824/439285275 > 1` | 只驳 (G) | `04_conjectureH_provenance/logs_se_trace_t6_joint_countersearch_20260722_SCALAR_GATE_REPORT.md:72-83` |
| 粗 gate (G)，`n=25` | `22018369536/21678509125 > 1` | strict range 仍失败 | 同文件 `:82-83` |
| T6 联合 JT，`n=18,c=2` | `2556731948080/3452466241653 < 1` | 有限门通过 | `04_conjectureH_provenance/se_t6_highc_hunt_20260723.md:26-32` |
| j=24 决策阈值 | `423059181968170/69760278879123` | 严格位于 `(0,10)` | `04_conjectureH_provenance/se_j24_decision_20260723.md:87-90,146-149` |
| c=2 gateway `Q(18)` | `7280/4437` | erratum 后精确值 | `04_conjectureH_provenance/se_red_implementation_20260723.md:25-45,101-110` |

这些复算支持论文对证据边界的叙述；没有发现把 finite pass 升格为 theorem 或把 shortcut failure 升格为 H1 failure 的情况。

### T4-I1：assembly 节点仍含越界的“Certified content”

- **位置：**`02_dag/nodes/SE.denom.assembly.yaml:29-41`，尤其 `:33`。
- **类别：****表述越界 / 状态矛盾**。
- **问题：**同一节点先写 `CONJECTURED`、operator input 缺失，下一段却称 uniform O(1) assembly 为
  “Certified content”，并引用“certified tame”；而 TAME 现为 OPEN，FOUND 有 star，GRAM/OMEGA 为 CONJECTURED。
- **最小修复：**改成“conditional assembly arithmetic, reviewed under the stated operator inputs”；只将
  已确认的 envelope calculus、endpoint 和常数标为 confirmed，不把实际 operator bound 标为 certified。

### T4-I2：GRAM/OMEGA 的 “Open obligations: None” 与状态段冲突

- **位置：**
  - `02_dag/nodes/SE.denom.Phi.legal.gram.yaml:28-30,50-52`；
  - `02_dag/nodes/SE.denom.Phi.legal.omega.yaml:32-39,61-63`。
- **类别：****表述越界 / DAG 状态卫生**。
- **问题：**两节点均为 CONJECTURED，状态段列出 load-bearing 未证步骤，却在 Open obligations 写 None。
- **最小修复：**把状态段中的 transport/frame/twirl/coset、colored-orbit bridge、backbone 等逐项移入
  Open obligations；或将 Claim 拆成已证 consequence 与未证 interface。

### T4-I3：closeout paper audit 的 H2/H3 fidelity 结论错误

- **位置：**`05_closeout_context/se_paperaudit3_20260723.md:32-43,103-109`。
- **类别：****审计越界 / 陈述一致性误判**。
- **问题：**该审计称 H2/H3 与冻结节点完全匹配并给出 zero blocking findings；但 T2-G1/T2-G4 表明
  H2 是接口恒等式而 GRAM Claim 是范数上界，H3 只是 OMEGA chain 的子假设。它也未发现 H2 的
  `dc×dc` 对 `c×c` 类型问题。
- **最小修复：**将该审计标为 superseded，并在新的审计中记录 T2/T3 的阻断项。

### T4-I4：论文先以 boxed identity 展示未证 H2，后置免责声明

- **位置：**`01_paper/se_explicit_witness.tex:1006-1024,1026-1040`。
- **类别：****表述越界风险**。
- **问题：**`eq:gcan2` 先被 boxed 并写成“therefore give”，直到后段才说明不把它当 theorem。
  严格阅读全文不会误判，但局部引用容易把开放接口误当已证明恒等式。
- **最小修复：**在 boxed 式上直接标注 `\stackrel{\mathrm{(H2)}}{=}` 或标题写
  “candidate canonical interface”；把免责声明移到式前。

### T4-I5：打包清单首行 BOM

- **位置：**`MANIFEST.sha256:1`。
- **类别：****复现卫生（非数学）**。
- **问题：**UTF-8 BOM 使标准 `sha256sum -c` 忽略/警告首项；人工去 BOM 后 67/67 全部匹配。
- **最小修复：**以无 BOM 的 ASCII/UTF-8 重写 manifest。

---

# 最终总判词

**GAP——定理 A 在替换错误的单独 projector-intertwining 式为上述乘积级 lemma 后可确认且常数不变；但论文 H2/H3 与冻结节点不一致、H2 全载体类型不合，并且 H1/H2/H3 到全局 lower block/assembly 之间尚缺一个明确且无 caveat 的 sectorization–multiplicity-lift 义务 H4，因此当前“三义务即完备规约”的结论不能确认。**
