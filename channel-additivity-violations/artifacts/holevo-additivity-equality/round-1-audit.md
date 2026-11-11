# 第 1 轮审计摘要：Holevo 加性等号与逻辑关系

## 结论

第 1 轮已经完整回答“等号是不是成立”。核心结论是：

1. 对固定信道 \(\mathcal N\)，
   \[
   C(\mathcal N)=\chi(\mathcal N)
   \quad\Longleftrightarrow\quad
   \chi(\mathcal N^{\otimes n})=n\chi(\mathcal N)\ \text{for all }n.
   \]
   这只用到 \(a_n=\chi(\mathcal N^{\otimes n})\) 的超加性和 Fekete 引理。

2. 对固定的一对 \((\mathcal N,\mathcal M)\)，等式
   \[
   \chi(\mathcal N\otimes\mathcal M)=\chi(\mathcal N)+\chi(\mathcal M)
   \]
   只说明这一对信道加性，不能推出 \(\mathcal N\) 的全部张量幂加性。

3. 把量词改为“对所有有限维信道”后，强两信道加性、所有信道的二重自身加性、所有张量幂加性以及所有信道的单字母化彼此等价。异信道到同信道的关键是 Fukuda–Wolf direct-sum/classical-flag reduction。

4. Shor 的加性等价定理是四个**全称命题**之间的等价：Holevo quantity 加性、最小输出 von Neumann 熵加性、entanglement of formation 加性、以及 entanglement of formation 的 strong superadditivity。它不是保持同一个反例 witness 的逐点等价。

5. Hastings 直接否定了 \(p=1\) minimum-output entropy 的普遍加性；经 Shor 的存在性 reduction，普遍 Holevo 加性也被否定。再经 direct-sum reduction，可得到某个单一信道 \(\mathcal T\) 满足 \(\chi(\mathcal T^{\otimes2})>2\chi(\mathcal T)\)，因而 \(C(\mathcal T)>\chi(\mathcal T)\)。

6. 这只是否定“所有信道都加性”，不等于“每个信道都不加性”。entanglement-breaking、unital qubit 和 depolarizing channels 是报告列出的代表性强加性类。

## 关键 reduction

对 block-direct-sum channel \(\mathcal T=\mathcal N\oplus\mathcal M\)，正交 classical flag 使
\[
\chi\!\left(\bigoplus_i\mathcal N_i\right)
=\log_2\!\left(\sum_i 2^{\chi(\mathcal N_i)}\right).
\]
而 \(\mathcal T^{\otimes2}\) 分成 \(NN,NM,MN,MM\) 四个正交 block。这个 log-sum-exp 恒等式让 cross term \(\chi(\mathcal N\otimes\mathcal M)\) 可以被代数地隔离，因此全称的“自身二重加性”足以推出全称的“两信道加性”；反向使用则把 pair counterexample 嵌入单信道 counterexample。

Shor reduction 的概念桥梁是 constrained Holevo quantity：若 \(V:A\to B\otimes E\) 是 Stinespring isometry，且 \(\sigma_{BE}=V\rho V^\dagger\)，则
\[
\chi_{\mathcal N}(\rho)=S(\mathcal N(\rho))-E_F(\sigma_{BE}).
\]
真正困难的是把指定平均态的 constrained optimization 嵌入 unconstrained channel optimization；因此等价定理需要辅助 classical registers、modified channels 和凸分析，而不是一个逐点恒等式。

## 需要正式核对的疑点

- 网页原文在 Hastings 段落写成了 \(S_{\min}(\mathcal E\otimes\mathcal E)\)；标准 Hastings 构造通常涉及随机信道与其复共轭信道 \(\mathcal E\otimes\overline{\mathcal E}\)。这可能是 DOM 文本提取丢失了 overline，也可能是回答书写疏漏，引用时必须回到原论文确认。
- 原始网页回答的数学上下标在文本导出中有损坏；原始文件仅作为记录，不能直接复制进论文。
- “unital qubit/depolarizing 与任意辅助信道的 Holevo 强加性”的准确假设、参数范围及从最小输出熵到 Holevo quantity 的 passage，正式写作前仍应逐一定理核查。
- 回答给 Holevo 1998 使用了 ResearchGate 链接；应改用 arXiv 或期刊原始页面。
- 第 1 轮没有回答反例的概率、测度、显式性、最小维数或 gap 大小；这是有意留给后续轮次，不是遗漏。

## 原始来源

- [Schumacher–Westmoreland 1997](https://doi.org/10.1103/PhysRevA.56.131)
- [Holevo 1998 / arXiv:quant-ph/9611023](https://arxiv.org/abs/quant-ph/9611023)
- [Shor 2004, Additivity Equivalence](https://arxiv.org/abs/quant-ph/0305035)
- [Hastings 2009](https://arxiv.org/abs/0809.3972)
- [Fukuda–Wolf 2007](https://arxiv.org/abs/0704.1092)
- [Shor 2002, Entanglement-Breaking Channels](https://arxiv.org/abs/quant-ph/0201149)
- [King 2002, Unital Qubit Channels](https://arxiv.org/abs/quant-ph/0103156)
- [King 2003, Depolarizing Channel](https://arxiv.org/abs/quant-ph/0204172)

## 置信度

- 固定信道的 \(C=\chi\) 与所有张量幂加性的等价：高。
- Fukuda–Wolf 的全称 weak-to-strong reduction：高。
- Shor 四个全称命题的等价以及 Hastings 对整个全称等价类的否定：高。
- 网页回答对 Hastings witness 的具体记号以及特殊信道定理的最强口径：中等，需原论文逐条复核。


