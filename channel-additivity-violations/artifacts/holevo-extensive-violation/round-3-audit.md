# 第 3 轮审计摘要：定量 gap 与 extensive violation

## 结论盘点

| 问题 | 审计后的结论 |
|---|---|
| \(p=1\) 的 MOE 加性违反能否达到固定常数量级？ | 能。Belinschi–Collins–Nechita（BCN）的随机共轭信道构造给出趋近 **1 bit** 的严格下界。 |
| “1 bit” 是否是普遍上界？ | 不是。它是 BCN 特定构造和 Bell-state witness 的渐近标尺，不能当作任意信道的上界。 |
| Holevo 加性 gap 能否同样趋近 1 bit？ | 能，但一般要换成 Fukuda 的 Weyl-flag 扩张信道。该构造把原 MOE gap **精确转移**成扩张信道的 Holevo gap；Shor 的抽象等价定理本身不保留原 witness、维数或 gap。 |
| 已知有限维 \(p=1\) gap 是否超过 1 bit？ | 本轮没有找到经过验证的结果。 |
| 已知 gap 是否随维数无界，或达到 \(\Omega(\log d)\)？ | 本轮没有找到；截至 2026-08-29 应标为开放/未检得，而不是“不可能”的定理。 |
| 把一个反例做 \(r\) 份张量能否自动线性放大？ | 不能自动成立。线性主项会被两个单信道自身的正则化缺陷（self-defect）抵消。 |
| 什么条件足以得到 extensive gap？ | 若两边 self-defect 合计为 \(o(r)\)，一份严格正 gap 就可放大为 \(r\delta-o(r)\)。但已知 Hastings/ASW/BCN/LLW 随机信道对尚未证明满足这一条件。 |

## 四类随机构造的定量定位

1. **Hastings（2009）**：原始 \(p=1\) MOE gap 的尺度约为
   \[
   \frac{\ln D}{D}-2\delta,
   \]
   在其参数极限中趋于零。这里的精确常数、共轭记号与参数顺序仍须按原论文核对。

2. **Aubrun–Szarek–Werner（ASW）**：报告给出的量级是
   \[
   \Omega\!\left(\frac{\log k}{k}\right),
   \]
   仍随输出维数参数 \(k\) 增大而趋零。它改善了几何与概率论表达，并未给出 extensive gap。

3. **Belinschi–Collins–Nechita（BCN）**：在 \(t=1/2\)，先取 \(n\to\infty\)，再取 \(k\to\infty\) 的口径下，Bell witness 给出
   \[
   \Delta S\ge 1-o(1)\quad\text{bit}.
   \]
   这是目前本轮找到的最强固定常数量级结论。它证明“任意接近 1 bit 的下界”，不证明 1 bit 是全局极限。

4. **Leung–Lovitz–Wu（LLW，arXiv:2607.15210）**：其 \(p=1\)、固定 \(t\)、大 \(k\) 的 gap 在报告中为
   \[
   \Theta(k^{-2}).
   \]
   这篇工作的主要贡献是 Rényi 参数范围与特定随机模型阈值（报告称 \(k=182\)），不是更大的 \(p=1\) gap。系数及展开式须从 PDF/TeX 再核。

## MOE 到 Holevo：哪种“等价”足够定量

只引用 Shor 的四猜想等价性，只能推出：

> 若普遍 MOE 加性为假，则普遍 Holevo 加性也为假。

它不能保证同一对信道、同一维数、同一 witness，也不能保证数值 gap 不变。

本轮更关键的是 Fukuda（2014，arXiv:1307.0707）Lemma 6.2 所用的 Weyl-flag 扩张。按报告中的归一化，它为给定 \(\mathcal N,\mathcal M\) 构造 \(\widetilde{\mathcal N},\widetilde{\mathcal M}\)，并满足
\[
\delta_\chi(\widetilde{\mathcal N},\widetilde{\mathcal M})
=
\Delta S(\mathcal N,\mathcal M),
\]
其中
\[
\delta_\chi(\mathcal N,\mathcal M)
=\chi(\mathcal N\otimes\mathcal M)-\chi(\mathcal N)-\chi(\mathcal M),
\]
\[
\Delta S(\mathcal N,\mathcal M)
=S_{\min}(\mathcal N)+S_{\min}(\mathcal M)
-S_{\min}(\mathcal N\otimes\mathcal M).
\]
因此 BCN 的近 1-bit MOE 下界可转移为另一对有限维扩张信道的近 1-bit Holevo 下界。正式写作仍应逐项核对扩张的输入/输出维数、对数底以及 Lemma 6.2 的准确记号。

## 为什么复制反例不自动得到线性 gap

### Holevo 情形

定义单信道 self-defect
\[
a_r=\chi(\mathcal N^{\otimes r})-r\chi(\mathcal N),\qquad
b_r=\chi(\mathcal M^{\otimes r})-r\chi(\mathcal M).
\]
由在 \((\mathcal N\otimes\mathcal M)^{\otimes r}\) 上使用每份最优的乘积 ensemble，
\[
\boxed{
\delta_\chi(\mathcal N^{\otimes r},\mathcal M^{\otimes r})
\ge r\,\delta_\chi(\mathcal N,\mathcal M)-a_r-b_r .
}
\]

### Minimum-output entropy 情形

定义
\[
\alpha_r=rS_{\min}(\mathcal N)-S_{\min}(\mathcal N^{\otimes r}),\qquad
\beta_r=rS_{\min}(\mathcal M)-S_{\min}(\mathcal M^{\otimes r}).
\]
由
\(S_{\min}((\mathcal N\otimes\mathcal M)^{\otimes r})
\le rS_{\min}(\mathcal N\otimes\mathcal M)\)，
\[
\boxed{
\Delta S(\mathcal N^{\otimes r},\mathcal M^{\otimes r})
\ge r\,\Delta S(\mathcal N,\mathcal M)-\alpha_r-\beta_r .
}
\]

这两式精确暴露了障碍：跨信道的线性增益可能被 \(\mathcal N\) 和 \(\mathcal M\) 各自多份使用时的 regularization gain 吃掉。

## 条件性 amplification lemma

若一份 Holevo gap 为 \(\delta>0\)，且
\[
a_r+b_r=o(r),
\]
则
\[
\delta_\chi(\mathcal N^{\otimes r},\mathcal M^{\otimes r})
\ge r\delta-o(r).
\]
MOE 情形同理：若 \(\alpha_r+\beta_r=o(r)\)，则
\[
\Delta S(\mathcal N^{\otimes r},\mathcal M^{\otimes r})
\ge r\Delta S-o(r).
\]

这确实是 extensive：若原信道维数固定，块信道维数为 \(d^r\)，于是
\[
r=\Theta(\log d^r).
\]
因此线性于 \(r\) 同时就是 \(\Omega(\log d_{\mathrm{block}})\)。

特殊充分条件是每个单信道都 tensor-stably additive（所有 self-defect 为零）。但常见的 entanglement-breaking 信道虽然具有这种稳定性，却与任意辅助信道强加性，因而跨信道 gap 也为零。已知随机反例目前缺的是“严格跨 gap + 次线性 self-defect”的同时认证。

## 正则化后的真正核心

由次/超加性和 Fekete 型极限，
\[
\lim_{r\to\infty}\frac1r
\delta_\chi(\mathcal N^{\otimes r},\mathcal M^{\otimes r})
=C(\mathcal N\otimes\mathcal M)-C(\mathcal N)-C(\mathcal M).
\]
MOE 也对应 regularized minimum-output entropy 的同类差值。因此“复制后是否 extensive”本质上不是单次加性问题，而是**正则化容量/熵是否仍非加性**的问题。

Collins–Youn 的相关结果位于无限维 commuting-operator 模型，不能当作有限维 tensor-product 信道的解决方案。

## direct-sum/flagging 为什么会稀释

网页 DOM 丢失了指数；正确的直和公式应写成
\[
\chi(\mathcal N\oplus\mathcal M)
=\log_2\!\left(2^{\chi(\mathcal N)}+2^{\chi(\mathcal M)}\right),
\]
而不是原始提取文本表面显示的 \(\log_2(2\chi(\mathcal N)+2\chi(\mathcal M))\)。

若 \(\chi(\mathcal N)=\chi(\mathcal M)\)，且交叉 gap 为 \(\delta\)，对 \(\mathcal T=\mathcal N\oplus\mathcal M\) 可得的两份 self-gap 下界为
\[
\chi(\mathcal T^{\otimes2})-2\chi(\mathcal T)
\ge \log_2\frac{1+2^\delta}{2}.
\]
即使 \(\delta\to1\)，右侧也只趋于
\[
\log_2(3/2)\approx0.585,
\]
说明这种 flagging 不是线性放大器。

## 维数允许什么

一般只有粗上界
\[
\Delta S\le\log_2(d_Bd_D),
\]
以及
\[
\delta_\chi\le
\min\{\log_2(d_Ad_C),\log_2(d_Bd_D)\}.
\]
所以信息论维数界并未排除 \(\Omega(\log d)\)；问题是目前没有有限维构造达到并严格证明这种增长。

## 最需要回原论文复核的点

1. Hastings 与 ASW 的 gap 公式、共轭信道 overline、常数和极限次序在 DOM 导出中可能受损。
2. BCN 的“近 1 bit”是 Bell witness 下的渐近**下界**；必须保留 \(n\to\infty\) 后 \(k\to\infty\) 的量词顺序。
3. Fukuda Lemma 6.2 的扩张维数及恒等式需按原文逐项核对；原始网页的上标在若干处已经丢失。
4. LLW 的 \(\Theta(k^{-2})\) 系数和 \(k=182\) 的严格/数值口径需查 PDF；不能把 182 说成全局最小信道维数。
5. “未找到 >1 bit、无界或 extensive 的有限维 \(p=1\) 结果”是截至日期的文献审计结论，不是不存在性定理。
6. 条件性 amplification lemma 是正确的初等推导；它还不是无条件构造，因为已知反例对的 self-defect 假设尚未证明。
7. Collins–Youn 的无限维结果必须与这里的有限维张量积模型严格分开。
8. direct-sum 公式须保留 \(2^{\chi}\)；原始网页文本在此处发生了明确的指数丢失。

## 主要来源

- [Hastings 2009](https://arxiv.org/abs/0809.3972)
- [Aubrun–Szarek–Werner](https://arxiv.org/abs/1003.4925)
- [Belinschi–Collins–Nechita](https://arxiv.org/abs/1305.1567)
- [Fukuda 2014](https://arxiv.org/abs/1307.0707)
- [Leung–Lovitz–Wu 2026](https://arxiv.org/abs/2607.15210)
- [Shor：四个加性猜想的等价性](https://arxiv.org/abs/quant-ph/0305035)
- [Fukuda–Wolf：direct-sum 与 additivity](https://arxiv.org/abs/0704.1092)
- [Collins–Youn](https://arxiv.org/abs/1907.07856)
- [Shor：entanglement-breaking channels](https://arxiv.org/abs/quant-ph/0201149)

## 给导师的一句话

目前有限维 \(p=1\) 已严格做到“任意接近 1 bit”的 MOE gap，并可通过 Fukuda 扩张精确转成同量级 Holevo gap；但没有找到 >1 bit、无界或 \(\Omega(\log d)\) 的严格结果。张量复制只有在单信道 self-defect 为次线性时才会真正 extensive，而这正是现有随机反例尚未解决的关键障碍。


