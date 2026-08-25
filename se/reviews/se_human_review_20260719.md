# Human cross-stack review of se_explicit_witness (paper v3-final, 27pp)

- **Provenance:** received verbatim from the lead (李佶) on 2026-07-19, transcribed to disk by the coordinating agent the same day. This is the FIRST completed cross-stack review of the SE campaign — the standing obligation recorded on `SE.goal` and in the paper's honesty section.
- **Verdict:** **Major revision / proof incomplete.** The main theorem is NOT established as written; no simple counterexample found in the first half; one definite type/dimension inconsistency and several unproved key operator identities in the canonical Gram–sandwich chain.
- **DAG processing:** entry (33); rule-3 demotions executed the same day.

---

## 审核结论(原文)

目前不能认定主定理的证明正确。
更准确地说:我没有发现前半部分存在简单反例,但支撑 Ω(n^{1/3}) 主结果的 canonical Gram—sandwich 核心链条中,存在一处明确的类型/维数不一致,以及多处尚未证明的关键算子恒等式。因此主定理按当前版本并未被证明。
建议评级:**Major revision / proof incomplete**,不宜按"已证明的新结果"公开宣称优先权。这篇稿件自己也明确承认尚未完成人类或跨模型审核。

## 一、最严重的问题:physical transport 恒等式在 c>1 时维数不匹配

稿件先定义 strict sector:P S^λ ≅ V_κ⊗V_ν⊗ℂ^c, c=c_{αβ}^θ。
然后对每个 j-元集合 D 定义 Π_D^λ = (1/(q−j)!)Σ_{s:s|D=id} ρ_λ(s),令 E_D 是 Ran Π_D^λ 的 "orthonormal synthesis",随后声称:

    ρ_λ(τ_p)Π_D^λ = E_K [ρ_θ(σ_p)⊗L_p] E_D*,

其中 L_p 作用在 c 维 LR multiplicity space 上。
但稿件稍后自己计算出 rank Π_D^λ = f^{λ/(q−j)} = f^θ。因此:
- E_D 的自然定义域维数是 f^θ;
- ρ_θ(σ_p) 作用在 f^θ 维空间;
- ρ_θ(σ_p)⊗L_p 却作用在 f^θ·c 维空间。

只要 c>1,这个乘积就不能与 E_D* 复合。稿件自己的数值例子中明确出现了 c_{αβ}^θ = 2。所以这不是只在理论上可能发生的边缘情形,而是稿件声称要覆盖的实际 sector。

**第二层问题:** 稿件说 L_p 是同一个 permutation action 在固定 H-multiplicity space 上的限制,并因此是酉的。但一般的 τ_p 并不显然正规化 H = S_{n−1}×S_n。通常 ρ_λ(τ_p) 会把一个 H-isotypic component 送到一个 τ_p H τ_p^{−1}-isotypic component,而不自动给出固定 multiplicity space 上的酉自同构。因此当前的 L_p 不仅维数没有对齐,作为一个固定 multiplicity-space endomorphism 也尚未被定义。

**影响:** 这个恒等式是后面"所有 LR copies 一次性处理、不损失 multiplicity factor"的基础。它出错后,以下结论都没有建立:output frame construction;multiplicity-safe trace;Direct canonical Gram bound;omega-decaying lower block;最终 Ω(n^{1/3}) 下界。这是一处实质性的证明断点,不是纯粹的表述不够详细。

## 二、output-frame Gram 恒等式基本上是直接宣称的

核心证明声称 E_{out,0}*E_{out,0} = B_θ(q)Π_0 以及 E_{out,z}*E_{out,z} = B_θ(q)/(δ_z+1)·Π_z。
但当前文本中:(1) E_{out,0} 和 E_{out,z} 没有被正式定义;(2) 没有给出它们的定义域、值域及与前面 E_D 的关系;(3) "horizontal-strip paths" 的求和没有写出来;(4) "all other strip hooks cancel" 只是一句话,没有 hook-product 计算;(5) 没有逐 sector 证明在 LR multiplicity space 上仍为这个标量。
而这两个 Gram 恒等式正是 weighted Bessel inequality 和最终 15/4 常数的来源。因此它们不能作为未展开的"标准事实"直接使用。

**可能的 off-by-one:** 稿件定义 δ_z = q−j−t(z)+θ'_{t(z)},随后称相关两个盒子的 axial distance 是 δ_z+1。按标准 content 差:第一行右端盒子的 content 是 q−j−1;尾部 corner 的 content 是 t(z)−θ'_{t(z)}−1;二者差为 q−j−t(z)+θ'_{t(z)} = δ_z,而不是 δ_z+1。δ_z+1 确实像是对应 hook length,但稿件这里明确称它为 axial distance,并据此写出 δ_z/(2(δ_z+1)) 与 (δ_z+2)/(2(δ_z+1)) 两个系数。必须明确究竟交换的是哪两个盒子,并从 Young orthogonal form 重新推导。若这里确实差了 1,后面的 exact frame Gram 也会改变。

## 三、matching average 并没有自动等于完整 H-twirl

稿件正确写出了标准 Schur twirl 公式,但实际构造首先只对 bipartite matchings 做平均,这直接提供的是第二半 S_n^B 的平均。随后文本只用一句 "Canonical-matching diagonal covariance supplies the S_{n−1}^A twirl as well." 就得出完整 H-twirl。
这里需要正式证明:B_h 如何在左右两侧变换,以及 (1/n!)Σ_h B_h*B_h 为什么同时与 S_{n−1}^A 和 S_n^B 对易。仅仅"matching 集合在群作用下不变"并不足以自动给出所声称的输入端共轭 twirl,尤其还涉及:query position 1 被固定;completion projector;strict sector projector;multiplicity copies。
这个步骤决定了是否能用一个 c×c 的 normalized multiplicity trace 代替完整算子,所以也是 load-bearing 的。

## 四、coset identity 与 strict-purge 的结合没有完整推导

稿件声称 b̂_j(λ)P = q^j(q−j)!·RP。证明只说明了:某个 partial injection 的扩展数是 (q−j)!;query-pinned 扩展数是 (q−j−1)!;lower-degree terms 被 strict-purge 杀掉;"no binomial or power of two remains"。
但要得到精确等式和精确常数,仍然需要逐项展示:(1) e_j(qx_i−2) 展开后每个 monomial 的系数;(2) 一个选中的位置是否来自 i 还是 ī;(3) 不相交性如何去掉所有重复项;(4) matching-stack 的 1/√(n!) 是否已计入;(5) Fourier transform 的归一化;(6) P 应该置于左侧、右侧还是双侧;(7) multiplicity copies 上是否完全相同。
当前几句话不足以证明精确的 coefficient q^j(q−j)!。而后面的 canonical Gram 及 exact sandwich 都依赖这个精确系数。

## 五、Full-multiplicity NO scalar 证明依赖了未证明的"彩色轨道等于完整中心和"

稿件考虑的实际和是 Σ_{I⊂A∖{1},|I|=a} Σ_{J⊂B,|J|=b} Π_{I∪J}^λ。这并不是 S_q-central,也不是完整的 S_{q−1}-central sum,因为它只包含固定颜色分配 (a,b) 的子集。
证明先计算完整中心和 Σ_{|D|=j}Π_D^λ = B_θ(q)I,然后声称 strict-purge 会杀掉其他所有颜色轨道,因此压缩后的彩色和就是同一个 scalar。
但 strict-purge lemma 原本是针对"一个函数在右 H-平移下依赖多少个 named coordinates"。它并没有正式证明以下算子恒等式:

    P(Σ_{all D} Π_D^λ)P = P(Σ_{|I|=a,|J|=b} Π_{I∪J}^λ)P。

对于 pinned sum 也有同样问题。证明直接称其为 S_{q−1}-central trace,但实际求和仍只覆盖一个彩色 orbit。
这个桥梁可能能够补出来,但当前文本没有证明它;而它是 C_{N,prob} = r_top·ω·I 在全部 LR multiplicities 上成立的唯一依据。

## 六、Exact sandwich 的 "raw backbone" 没有真正从 legal kernel 推出来

Exact sandwich 的关键等式是 C*C = (1/(q!)²)A_raw。在这个等式之后,counting gauge 与 probability gauge 之间的换算是代数上一致的;两个 d_N^{−1/2} whitening factors 也确实产生 d_N^{−1}。
但最关键的第一步只是说:strict purge 提取了 degree j;cancellation lemma 把 C 变成 Z;因而 "extract exactly C_{λ,ξ}";所以得到 raw backbone。
这不足以建立实际 legal matrix block 与 b̂_h(λ) 之间的逐项相等关系。尤其需要明确:legal YES restriction;legal NO restriction;matching-row normalization;completion;central alphabet projection;strict H-sector projection——这些操作的顺序以及每一步的 coefficient。
目前多个关键细节被指向未随论文提供的私人文件(se_strict_level_partial_injection_symbol.md、se_cancel_identity_review_20260718.md 及其他 review artifacts)。因此这个 LaTeX 文件本身并没有给出一个可独立复核的 sandwich 证明。

## 七、定理量词不完整:"admissible" 从未定义

文中多次说 "Only admissible partitions are retained"、"every admissible strict sector",但全文没有给出 "admissible" 的正式定义。
特别是 Exact sandwich 声称对每个 j≥1 的 admissible sector 成立,并强调没有 n≥3j 和 taper 假设。然而它在证明中反复使用:"stable LR removal of the two long first rows";unique-long-child;κ=(n−1−a,α)、ν=(n−b,β) 是合法 partition;第一行足够长。这些都需要明确的稳定区间假设。
对主定理而言,直接把 sandwich 和相关 sector lemmas 限制到实际所需的 n≥3j、j+1<K 可能就够了,因此这未必破坏最终渐近结论;但当前定理的原始量词没有被证明。

## 八、前半部分哪些看起来是正确的

以下部分未发现明确矛盾:
1. **Legal normalization**:从 raw coefficient q^{−3n/2}/√(n!) 和两侧概率 L² restriction factors 出发,在 q=2n 时得到 ℛ(W̄_{se,k}) = (1/q!)W_k^leg Π̄_{se,k},因子计算自洽。
2. **Numerator**:k=0 atom 把常数向量映到常数向量,k>0 position-defect sectors 与 trivial representation 正交,‖Γ_n‖ ≥ K 合理。
3. **Matched-degree restriction scalar**:r_d(λ) 公式在 d=j、λ=(q−j,θ) 时只有 t=j 项存活,得 r_top = q^j f^θ/(j! f^λ),内部一致。
4. **Defect pinning**:LR first-row inequality 加 Peter–Weyl 相同 shape 配对,legal X/Y block 只留 alphabet defect k,合理。
5. **最后的 taper 算术**:在 omega-decaying lower-block lemma 成立的前提下,cross-defect regrouping、f(x)=(1−x)√x 的最大化、M=(4√6+3√10)/18、最终 1/(2(1+M)) = 9/(18+4√6+3√10) 都正确。
问题不在最终算术,而在给第四个 lower-defect term 提供正确算子界的中间桥梁。

## 九、n^{1/6} 旧界与 n^{1/3} 主界应分开评价

**Ω(n^{1/3}) 主定理:当前没有被证明。** 链条 physical transport → output frames → canonical Gram → sandwich → ω-decay 在第一步就存在维数问题,后面还有若干未证明恒等式。
**Ω(n^{1/6}) corollary:** 不使用新的 canonical Gram,而用较粗的 ‖C_{k→k−1}‖ ≤ (k−1)ρ_{k−1}‖T_k‖;最终最大化和常数计算正确,比主结果可信得多。但仍不能完全认证:BR completion constants 以 "local explicit reading" 形式给出、special-path correction 依赖作者声称的原文勘误、ambient X/Y/Φ Schur reductions 被压缩、corollary 引用未提供的私人 proof record。
(Belovs–Rosmanis 已发表工作给出大字母表 explicit adversary 且原始分析要求 q=Ω(n²);Zhandry 已从其他方法得到 SE 的最优 Ω(n^{1/3})。这只能确认研究背景,不能验证本文新增的 minimal-alphabet operator analysis。)

## 十、数值证据目前无法独立审核

稿件列出 SHA-256、exact rational gates、independent scripts、pressure tests,但实际脚本和日志没有随论文提供。稿件自己也说数值只是 corroboration。所以能确认的只是"论文写了这些数值",不能确认:hash 对应的代码内容;代码是否实现同一个算子;是否存在共同实现错误;c>1 sector 是否真的处理了完整 multiplicity space。数值测试通过不能修复 physical-transport 公式的维数不一致。

## 十一、较小的源码问题

LaTeX 可正常编译 27 页;交叉引用正常。但源码有五处把 `\qquad` 写成裸文本 `qquad`,会在公式中打印斜体 qquad。

## 最终判定

**可以接受:** 研究方向有意义;legal normalization、numerator、matched restriction、defect pinning、最终 taper arithmetic 大体可信;无证据表明最终定理为假;n^{1/6} 较弱结果可能经较少修改成为可审核结果。
**不能接受:** 当前不能声称 Adv±(SE(n,2n)) ≥ (0.241385…−o(1))n^{1/3} 已被严格证明。

**最优先需要重建的九项:**
1. 用维数正确的 sector-specific frames 替换 physical-transport 公式;
2. 证明 τ_p 如何在不同 H-multiplicity spaces 之间运输,而不是声称它限制为固定空间上的酉算子;
3. 完整定义 E_{out,0}、E_{out,z},逐步推导 frame Grams;
4. 澄清 axial-distance 的 δ_z / δ_z+1 问题;
5. 正式证明 matching average 等于完整 H-twirl;
6. 将 strict-purge 从函数支持 lemma 提升为实际 projector/orbit-sum 恒等式;
7. 从 legal kernels 逐项推导 raw sandwich backbone;
8. 定义 "admissible sector",加入准确稳定区间;
9. 把所有被引用的 artifacts、脚本和原文勘误 diff 一并提供。

**结论标签:主定理 proof incomplete;需要 major revision,而不是小修。**
