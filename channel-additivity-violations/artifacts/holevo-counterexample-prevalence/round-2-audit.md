# 第 2 轮审计摘要：加性反例是否“很多”

## 最可靠的结论

“很多”必须按不同量词分别回答：

| 口径 | 审计后的答案 |
|---|---|
| 存在性 | 是；\(p=1\) minimum-output entropy（MOE）的普遍加性已被 Hastings 否定，Holevo 普遍加性经 Shor 的全称等价定理随之被否定。 |
| 随机模型 | 对 MOE 是：Hastings 原始结论是正概率；后续特定高维 Haar 模型给出概率趋于 1 或 almost-sure eventual violation。必须说明模型和 witness。 |
| 开集/正测度 | 是：固定维数中的严格 gap 由连续性保持，因此反例集合相对开，并有正的内禀 Lebesgue 测度。 |
| 稠密/generic/全测度 | 否（在完整 CPTP 空间的自然口径下）：entanglement-breaking channels 有非空内部且强加性，构成 additive open region。 |
| 显式 deterministic matrix witness | 仍缺少公认、低维、可打印 Kraus/Stinespring 矩阵并严格认证的 \(p=1\) 例子。随机构造公式不等于显式实例。 |
| 低维/少参数/自然族 | 强版本仍开放；Werner–Holevo qutrit 是漂亮的显式 \(p>1\) 反例，但不是 \(p=1\) 答案。 |

## 本轮最有价值的自主推导：stability lemma

设输出维数为 \(d_B,d_D\)，并令
\[
\varepsilon_N=\tfrac12\|\mathcal N-\mathcal N'\|_\diamond,
\qquad
\varepsilon_M=\tfrac12\|\mathcal M-\mathcal M'\|_\diamond.
\]
对足够小的 \(\varepsilon\)，取 Audenaert–Fannes 函数
\[
f_d(\varepsilon)=\varepsilon\log_2(d-1)+h_2(\varepsilon).
\]
则可得
\[
|S_{\min}(\mathcal N)-S_{\min}(\mathcal N')|
\le f_{d_B}(\varepsilon_N)
\]
以及
\[
|\chi(\mathcal N)-\chi(\mathcal N')|
\le 2f_{d_B}(\varepsilon_N).
\]
再用
\[
\tfrac12\|\mathcal N\otimes\mathcal M-
\mathcal N'\otimes\mathcal M'\|_\diamond
\le \varepsilon_N+\varepsilon_M
\]
控制联合信道，就得到 \(\Delta S\) 和 \(\delta_\chi\) 的连续性。因此任意严格 gap \(g>0\) 都有一个仍保持正 gap 的 diamond-norm 邻域。

这严格支持：反例不是孤立点；在已有严格反例的固定维数组合中，它们构成非空相对开集并具有正内禀测度。它并不支持稠密或 generic。

## arXiv:2607.15210 的定位

- 作者：Debbie Leung、Benjamin Lovitz、Peixue Wu；v1 日期 2026-07-16。
- 题目：*Counterexamples to additivity of minimum output p-Rényi entropy of quantum channels for p>3/4 and 0≤p<1/4*。
- 报告称 Theorem 1.1 覆盖 \(p\in[0,1/4)\cup(3/4,\infty]\)，所以明确包含 \(p=1\)。
- 构造是 Haar-random projection 加 local Choi normalization；它是明确的随机 ensemble，但不是一份具体 deterministic Kraus witness。
- 论文直接证明的是 minimum-output \(p\)-Rényi entropy 反例。Shor 只能把“普遍 MOE 加性为假”转成“存在某些 Holevo 反例”，不能保留同一随机信道、同一维数或同一 witness。
- 报告所述 \(k_{\mathrm{high}}(1)=182\) 来自特定 ensemble/Bell witness 下的高精度数值优化，不是所有量子信道的严格全局最小维数。
- 该论文回答了 \(p\)-参数覆盖和随机反例问题，没有关闭低维显式 \(p=1\) witness 的缺口。

## 需要回原论文复核的技术点

1. 原始导出多次把 \(\overline{\mathcal E}\) 的 overline 丢失，出现 \(\mathcal E\otimes\mathcal E\) 的表面记号。Hastings/ASW witness 的准确 conjugate/self-channel 口径必须按原文重写。
2. Hastings random-unitary 公式中 \(U_i\rho U_i^\dagger\) 的次序与权重记号在 DOM 导出里可能损坏。
3. ASW 所列 \(m=ck^2,d=Ck^2\)、异常概率 \(e^{-c'm}\) 的准确常数依赖和 theorem 量词需要逐字核对。
4. BCN 的 \(k\ge183\) 与 LLW 的 \(182\) 都依赖特定 random ensemble、conjugate/Bell witness 和数值优化；不能提升为解析、全局或最小维数定理。
5. LLW 构造参数在 DOM 文本中显示为 \((k-2,1)\)，很可能原式是 \((k^{-2},1)\)；必须从 PDF/TeX 核实。
6. Audenaert–Fannes 界应在其标准有效范围内使用，较大扰动时需采用截断/分段版本；stability lemma 只需足够小扰动，因此不影响开集结论。
7. “EB channels 有非空内部”以及其与任意辅助信道的强加性足以排除稠密、residual 和全测度；正式证明中应明确采用 CPTP Choi affine hull 上的相对拓扑与内禀 Lebesgue 测度。
8. “没有满意的显式例子”是截至日期的文献状态陈述，不是不存在这种例子的定理。

## 主要来源

- [Hastings 2009](https://arxiv.org/abs/0809.3972)
- [Aubrun–Szarek–Werner 2011](https://arxiv.org/abs/1003.4925)
- [Belinschi–Collins–Nechita 2016](https://arxiv.org/abs/1305.1567)
- [Leung–Lovitz–Wu 2026](https://arxiv.org/abs/2607.15210)
- [Shor 2004](https://arxiv.org/abs/quant-ph/0305035)
- [Shor 2002, entanglement-breaking](https://arxiv.org/abs/quant-ph/0201149)
- [Audenaert 2007](https://arxiv.org/abs/quant-ph/0610146)
- [Werner–Holevo 2002](https://arxiv.org/abs/quant-ph/0203003)
- [Cubitt–Harrow–Leung–Montanaro–Winter 2008](https://arxiv.org/abs/0712.3628)
- [Leditzky et al. 2023，量子容量，仅作排除混淆](https://arxiv.org/abs/2202.08377)

## 给导师的一句话

反例在随机、高维、局部开集和正测度意义下确实“很多”；但在低维、显式、少参数、可严格认证的 \(p=1\) 意义下仍然稀缺，而 \(182/183\) 只是特定随机模型与 Bell witness 的阈值，不是全局最小反例维数。


