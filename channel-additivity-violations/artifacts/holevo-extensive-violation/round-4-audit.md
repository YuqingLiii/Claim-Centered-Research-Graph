# 第 4 轮审计摘要：老板三问、Hayden–Penington 与 WHGAP

## 最终结论

老板表面上问了三件事：

1. \(\chi(\mathcal N^{\otimes n})\ge n\chi(\mathcal N)\) 能否总取等号？
2. 非加性反例是否“很多”？
3. 违反能否随信道规模增长，即达到 extensive？

| 问题 | 截至 2026-08-29 的结论 |
|---|---|
| 普遍等号 | **已否定**。Hastings 否定 \(p=1\) minimum-output entropy（MOE）普遍加性；经 Shor 的全称等价和标准构造，存在有限维信道满足 \(C(\mathcal N)>\chi(\mathcal N)\)。特殊信道类仍可加性。 |
| 反例是否很多 | **随机高维、开集、正测度意义下很多；稠密/generic 意义下不是；低维显式 \(p=1\) witness 仍稀缺。** |
| 已知 gap 大小 | 有限维 \(p=1\) MOE gap 可严格趋近 \(1\) bit；Fukuda 扩张把它精确转为另一对信道的近 \(1\)-bit Holevo pair gap。 |
| HP 意义的 extensive gap | **仍开放**：未核实到有限维 \(p=1\) 的 \(>1\)-bit、无界或 \(\Omega(\log d)\) lower-bound theorem。 |
| Hayden–Penington 做了什么 | 给出依赖 holographic/semiclassical 输入的 **A 或 B**：要么 extensive 加性违反存在，要么存在几乎计满黑洞熵的低纠缠微观态；不是 extensive 反例构造。 |
| WHGAP 是否是其子问题 | **不是**。WHGAP 研究 \(Q,P\)；老板的问题研究 \(\chi,C,S_{\min}\)。二者只是同属量子信道正则化与张量非加性的大类。 |

## 先纠正两个材料识别问题

- 附图 1 和附图 3 不是两篇不同材料：它们分别是 Hayden–Penington 论文的正文页和首页。
- 附图 2 才是 Hastings 2009。因此老板实际展示的是 **两篇论文**，不是三篇：
  1. Hastings 2009；
  2. Hayden–Penington 2020。
- Hayden–Penington 正文 Eq. (1) 排版漏掉了 \(1/n\)。无辅助经典容量的正确公式是
  \[
  C(\mathcal N)=\lim_{n\to\infty}\frac1n\chi(\mathcal N^{\otimes n}),
  \]
  不是论文该行表面印出的 \(\lim_n\chi(\mathcal N^{\otimes n})\)。其 Eq. (3)
  \[
  \chi(\mathcal N^{\otimes n})\ge n\chi(\mathcal N)
  \]
  与“猜想是否总为等号”的讨论是正确的。

## “三个问题”严格展开为何至少有十个命题

1. 一对给定信道的 pair additivity；
2. 一个给定信道的二重 self-additivity；
3. 一个给定信道的全部 \(n\)-copy additivity；
4. 固定信道的单字母化 \(C=\chi\)；
5. 对所有信道的 universal additivity；
6. MOE 的 universal additivity；
7. 反例存在性；
8. 随机概率、开集与测度意义的丰度；
9. 稠密/generic 与低维显式性；
10. 固定信道累计 \(n\)-copy defect 与 primitive-channel-size extensive gap 的区别。

Shor 的结论是若干**全称猜想**等价，不是“同一个 MOE witness 自动就是同一 pair 的 Holevo witness”。数值精确保留需要 Fukuda 的显式扩张信道。

## 最重要的新口径：两种“线性增长”不能混为一谈

若对固定有限维信道 \(\mathcal N\) 有
\[
C(\mathcal N)>\chi(\mathcal N),
\]
定义累计 defect
\[
\delta_n=\chi(\mathcal N^{\otimes n})-n\chi(\mathcal N).
\]
由 \(n^{-1}\chi(\mathcal N^{\otimes n})\to C(\mathcal N)\)，
\[
\frac{\delta_n}{n}\to C(\mathcal N)-\chi(\mathcal N)>0.
\]
所以固定信道的累计 defect 确实是 \(\Theta(n)\)。

但把 \(\mathcal N^{\otimes n}\) 看成新的 block channel 时，
\[
C(\mathcal N^{\otimes n})-\chi(\mathcal N^{\otimes n})
=nC(\mathcal N)-\chi(\mathcal N^{\otimes n})=o(n).
\]
因此简单 blocking 并没有产生 Hayden–Penington 所问的 primitive-size capacity advantage。

HP 的 extensive 问题是：是否存在一列本身规模增长的 primitive channels，使一次 pair gap 或相应 capacity advantage满足
\[
\Omega(m)=\Omega(\log d),
\]
其中 \(m\) 是描述输入/输出 Hilbert space 所需的 qubit 数。这在有限维 \(p=1\) 情形仍开放。

## Hayden–Penington 的数学命题

论文 Section 2, Eq. (11) 把 Possibility 1 写为：存在两列信道
\[
\mathcal N_j^{(n)}:\mathcal S(A_j^{(n)})\to\mathcal S(B_j^{(n)}),\qquad j=1,2,
\]
其输入、输出 Hilbert space 的 qubit size 随 \(n\) 线性增长，且
\[
\Delta^{(n)}
=S_{\min}(\mathcal N_1^{(n)})
+S_{\min}(\mathcal N_2^{(n)})
-S_{\min}(\mathcal N_1^{(n)}\otimes\mathcal N_2^{(n)})
\ge Cn
\]
对某个常数 \(C>0\)。

论文主结论是
\[
\boxed{\text{A: extensive additivity violations}\quad\lor\quad
\text{B: disentangled black-hole almost-basis}.}
\]

这不是 exclusive XOR；论文明确允许 A、B 同时成立，也没有决定哪一支成立。

### 黑洞一侧的量词

在没有 extensive violation 的分支下，HP 的剔除论证得到一组正交低纠缠微观态，其数目满足
\[
\operatorname{rank}P_{\rm disent}
\ge p_{\rm disent}(\beta)e^{S_{\rm BH}}.
\]
若 thermal weight 是 nonvanishing order-one，即
\[
-\log p_{\rm disent}(\beta)=O(1),
\]
则
\[
\log\operatorname{rank}P_{\rm disent}\ge S_{\rm BH}-O(1),
\qquad
\operatorname{rank}P_{\rm disent}\ge e^{S_{\rm BH}-O(1)}.
\]

这里不能把物理文献中的“\(O(1)\) probability”机械理解成只有一个 Big-O 上界；需要的是非消失常数量级，或等价地 \(-\log p=O(1)\)。

### “disentangled” 不等于 product state

令 \(B\) 略小于半个 boundary。HP 的低纠缠条件为
\[
S(\rho_{\rm disent}^{B})
\lesssim \frac12 S(\rho_{\rm TFD}^{B_LB_R})
\]
（按 \(1/G_N\) 的 leading order 理解）。它表示相对 typical microstate 存在 \(\Theta(1/G_N)\) 的 entanglement deficit，不表示完全无纠缠。

“almost-basis”只表示有 \(e^{S_{\rm BH}-O(1)}\) 个正交低纠缠态；典型光滑视界态仍可能是这些基态的高度纠缠叠加。

### “视界处或外部有结构”是条件性物理推论

该结论额外假设：

1. 低纠缠态具有 semiclassical geometric bulk description；
2. 其边界熵服从 RT/QES prescription。

在这些假设下，若几何在视界外完全像普通 AdS-Schwarzschild，QES 面积过大，无法产生所需 leading-order entropy deficit；所以必须在视界处或外部出现非平凡结构。Fuzzball、firewall、end-of-the-world brane 是候选机制，不是论文构造出的解。

## 2020 年后的状态

### Wei–Yoneta 2024

Wei–Yoneta 给出大量低纠缠微观态的强条件性结果，量级为
\[
\exp[S_{\rm micro}-f(S_{\rm micro})],
\qquad f\in\omega(1)
\]
的正交态，并在额外热力学条件下与 canonical \(S_{\rm BH}-O(1)\) 口径建立更紧联系。

但其黑洞应用明确依赖 Conjecture 0：
\[
E_P\le E_W,
\]
即 entanglement of purification 被 entanglement-wedge cross section 上界。因此它不是无条件有限维 channel theorem。

更重要的是：
\[
B\not\Rightarrow \neg A.
\]
即使低纠缠微观态确实很多，也不能排除 extensive additivity violation 同时存在。

### Collins–Youn 与后续 commuting-operator 工作

这些结果涉及无限维 commuting-operator setting；作者明确说明有限维适用性不清楚。它们不能宣布 HP 的有限维 tensor-product 分支已解决。

### Leung–Lovitz–Wu 2026

LLW 覆盖 \(p=1\) 并扩大 Rényi 参数范围、改善特定随机模型的阈值；报告中的 \(182\) 是 ensemble/Bell-criterion-specific 数值阈值，不是全局最小维数，更不是 \(>1\)-bit 或 extensive theorem。

## 近 1-bit MOE 如何转成 Holevo

Fukuda Lemma 6.2, Eq. (6.9) 对给定
\[
\Phi:L(\mathbb C^l)\to L(\mathbb C^k),\qquad
\Omega:L(\mathbb C^{l'})\to L(\mathbb C^{k'})
\]
构造 Weyl-flag extensions \(\widetilde\Phi,\widetilde\Omega\)，满足
\[
\chi(\widetilde\Phi^{\otimes m}\otimes\widetilde\Omega^{\otimes n})
=\log\!\bigl(k^m(k')^n\bigr)
-S_{\min}(\Phi^{\otimes m}\otimes\Omega^{\otimes n}).
\]
取 \((m,n)=(1,1),(1,0),(0,1)\)，得到精确恒等式
\[
\delta_\chi(\widetilde\Phi,\widetilde\Omega)
=\Delta S(\Phi,\Omega).
\]

因此 BCN 的 \(1-\varepsilon\) bit MOE gap 可以精确转成另一对扩张信道的 \(1-\varepsilon\) bit Holevo pair gap。它不是 Shor 抽象等价本身的 pointwise 结论。

若未来 HP 给出 \(\Omega(m)\) MOE pair gap，Fukuda 扩张只增加线性 qubit overhead，所以 extensive 量级也能保留。

## 对网页报告中 direct-sum 推导的更正

第 4 轮原始网页报告给出了一个把 Holevo pair gap 转成 same-channel gap 的 balancing + direct-sum 推导；思路成立，但原始文本的一处符号被写反。

设平衡后
\[
x=\chi(\mathcal N),\quad y=\chi(\mathcal M),\quad |x-y|<1,\quad
g=\delta_\chi(\mathcal N,\mathcal M),
\]
并令 \(a=2^x,b=2^y\)、\(\mathcal T=\mathcal N\oplus\mathcal M\)。则
\[
\chi(\mathcal T^{\otimes2})-2\chi(\mathcal T)
\ge \log_2\!\left[1+w(2^g-1)\right],
\qquad
w=\frac{2ab}{(a+b)^2}\ge\frac49.
\]
所以
\[
\chi(\mathcal T^{\otimes2})-2\chi(\mathcal T)
\ge g+\log_2(4/9)
=g-\log_2(9/4).
\]
正确的是“至多损失 \(\log_2(9/4)\approx1.17\) bits”，不是原始提取文本表面的 \(g-\log_2(4/9)\)。

在正式论文中，这个 balancing lemma 仍应独立写出并审稿式检查；它不是 HP、Fukuda 或 Fukuda–Wolf 原文直接陈述的 theorem。

## WHGAP 为什么不是子问题

| 老板的 additivity 问题 | WHGAP |
|---|---|
| \(\chi(\mathcal N)=\max I(X:B)\) | \(Q^{(1)}(\mathcal N)=\max I_c\) |
| \(C=\lim_n n^{-1}\chi(\mathcal N^{\otimes n})\) | \(Q=\lim_n n^{-1}Q^{(1)}(\mathcal N^{\otimes n})\) |
| 不要求 secrecy | \(P^{(1)}=\max[I(X:B)-I(X:E)]\)，要求 secrecy |
| 通过 Shor 联系 \(S_{\min}\) 加性 | 通过 coherent/private information、degradability/antidegradability 分析 |
| 问纠缠编码是否提高经典通信率 | 问能否传 qubit 或私密 classical bits |

antidegradability/no-cloning 可以给 \(Q=P=0\)，却不推出 \(\chi=0\) 或 Holevo additivity。例如 \(d\)-维 erasure channel 在 \(p\ge1/2\) 时 antidegradable、\(Q=P=0\)，但只要 \(p<1\)，其 classical capacity 仍为
\[
(1-p)\log_2 d>0.
\]

因此最终判决是：

> WHGAP 与老板问题是平行项目，不是 special case，也不存在当前已知的直接归约。共同点只是都研究量子信道在 tensor powers 下的 regularization/nonadditivity。

## 给老板的 60 秒口头版

您当时给的是两篇论文、三个问题。第一，Holevo 加性等号并不普遍成立：Hastings 已否定普遍猜想，所以纠缠码字有时确实能提高经典通信率。第二，反例在高维随机模型、开集和正测度意义下很多，但不是全空间 generic，漂亮的低维显式 \(p=1\) 例子仍缺。第三，目前严格认证的 \(p=1\) gap 可趋近 1 bit；但随 primitive channel 的 qubit 数线性增长、也就是 Hayden–Penington 意义的 extensive gap，有限维里仍没有解决。Hayden–Penington 给出的是条件性二择一：要么这种 extensive violation 存在，要么黑洞有 \(e^{S_{\rm BH}-O(1)}\) 个低纠缠微观态；他们没有构造 extensive counterexample。我的 WHGAP 项目研究 \(Q/P\) 边界，是同一大类中的平行容量问题，不是这个 Holevo 问题的子问题。

## 可落地的四个研究子题

| 难度 | 子题 | 最小里程碑 | 失败判据 | 回答哪一问 |
|---|---|---|---|---|
| ★★ | 认证一个具体有限维 \(p=1\) Kraus witness | 给出具体矩阵并对 single-channel \(S_{\min}\) 下界及 joint witness 上界做严格证书 | 所有可认证下界都盖不过 joint gap | 显式 |
| ★★★ | 在 BCN/LLW 附近搜索 \(>1\)-bit witness | 先数值获得稳定 \(1+\eta\)，再做 interval/SOS/谱界认证 | 扩展搜索中 margin 始终回落到 \(1\) 以下 | 大 |
| ★★★★ | 控制随机反例的 self-regularization defect | 先完成 \(r=2,3\) 的统一 concentration/lower bound，再争取 \(o(r)\) | self-defect 被证明本身为 \(cr\) | extensive |
| ★★★★★ | 有限维 holographic/tensor-network toy family | 同时证明 single-channel uniform MOE 下界与 TFD-like joint 上界 | 指数多个低纠缠态持续压低单信道 MOE | HP extensive |

## 主要原始来源

- [Hayden–Penington 2020](https://arxiv.org/abs/2012.07861)
- [Hastings 2009](https://arxiv.org/abs/0809.3972)
- [Shor 2004](https://arxiv.org/abs/quant-ph/0305035)
- [Belinschi–Collins–Nechita 2016](https://arxiv.org/abs/1305.1567)
- [Fukuda 2014](https://arxiv.org/abs/1307.0707)
- [Fukuda–Wolf 2007](https://arxiv.org/abs/0704.1092)
- [Collins–Youn 2022](https://arxiv.org/abs/1907.07856)
- [Wei–Yoneta 2024](https://arxiv.org/abs/2211.11787)
- [Leung–Lovitz–Wu 2026](https://arxiv.org/abs/2607.15210)
- [Devetak 2005](https://arxiv.org/abs/quant-ph/0304127)

## 仍需保持审慎的内容

1. “没有 \(>1\)-bit、无界或 finite-dimensional HP-extensive theorem”是截至日期的文献审计状态，不是不存在性定理。
2. HP 的 CFT lattice regularization、对 atypical states 的 QES 适用性和 semiclassical scaling 不是普通有限维 QIT 定理。
3. Wei–Yoneta 的黑洞结论依赖 \(E_P\le E_W\) 等 holographic assumptions。
4. Fukuda 定量转移会换信道；不能说 BCN 原始 random pair 自己就是 Holevo witness。
5. 网页 DOM 会丢上标、分母与共轭线；正式写作应以 PDF/TeX 为准。
6. 第 4 轮网页报告中的 direct-sum balancing 是公开推导而非原论文定理，且已在本摘要修正符号。


