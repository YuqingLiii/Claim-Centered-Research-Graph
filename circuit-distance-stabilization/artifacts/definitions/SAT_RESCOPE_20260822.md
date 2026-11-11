# CIRCDIST 第四题重定向：稳定值与稳定轮数（2026-08-22）

## 0. 调度决定

Lead 选择保守改题：保留原有的理想初始化、理想最终数据读出、固定单轮
single-ancilla CSS syndrome-extraction schedule 与单位故障权重模型；不改成 lattice surgery
或 timelike-logical 任务。

`research/circdist/notes/CIRCDIST_PROBLEMS.md` 中 2026-08-20 的第四题是冻结的历史题面，
不回写。自本说明起，canonical 根节点 `CIRCDIST.sat` 按下述新版问题解释；旧定义
`R_sat = min{R_0 : d_R=d for all R>=R_0}` 只作为“为何改题”的历史记录保留。

## 1. 为什么必须改题

在当前边界约定下，可以在一个 undetectable logical witness 后添加无故障轮，所以

\[
d_{R+1}(M)\le d_R(M).
\]

另一方面总有空间逻辑算符给出 `d_R(M) <= d`。因此旧题期待的“轮数增加使距离上升，
最后达到空间码距 `d`”在这个模型中方向相反。旧 `R_sat` 只能取两类值：如果从第一轮
起就有 `d_R=d`，则 `R_sat=1`；否则永远不能回升到 `d`，即 `R_sat=infinity`。

这不表示重复轮数没有问题可研究。真正随模型变化、并且能被有限窗口决定的量是最终
稳定值和达到该值所需的轮数。

## 2. 新版第四题（正式题面）

固定一个合法的单轮 schedule `M`，令 `d_R(M)` 为重复 `R` 轮所得电路的 circuit
distance。定义

\[
d_\infty(M)=\lim_{R\to\infty} d_R(M),
\qquad
R_{\mathrm{stab}}(M)
=\min\{R_0:\forall R\ge R_0,\ d_R(M)=d_\infty(M)\}.
\]

新版第四题要求：

1. 给出 `d_R(M)` 的有限状态 / min-plus transfer 表示；
2. 证明 `d_\infty(M)` 与 `R_stab(M)` 可由有限窗口决定，并给出显式窗口或算法；
3. 对标准 surface-code schedule、故意 hook-misaligned 的 surface-code schedule，以及至少
   一个 qLDPC schedule，计算或严格界定 `(d_infty,R_stab)`；
4. 解释最终距离由哪种机制限制：单轮 hook/bulk、边界、测量故障，还是跨轮混合机制。

这里不再要求 `d_R` 上升到空间码距，也不再把 timelike logical 当作当前模型里的候选
机制。若以后研究连接两个时间边界的 logical transmission distance，那是单独的新题。

## 3. 已有进展按新题重排

| 新任务 | 当前结论 | 证据等级 | 还缺什么 |
|---|---|---|---|
| 单调性与极限 | `d_{R+1}<=d_R`，故整数序列必有 `d_infty` | 有证明草图；7,610 个合法 schedules 零反例 | 对新版精确命题做独立 claim-level 评审 |
| 有限窗口 | 最小见证可压到连续至多其权重的轮；由 `d_R<=d` 得 `R_stab<=d_infty<=d`，且 `R>=d` 后恒定，所以 `d_infty=d_d` | contiguity 论证及后续修正评审支持；旧评审绑定的是 lift 命题，不是这个新节点 | 汇编成独立定理并做 hash-bound 评审；核对模型边界与合法 schedule 的全称量词 |
| transfer 表示 | 候选状态空间 `Sigma=F_2^n/rowspace(H_X)`，候选式 `d_R=u^T (min-plus) A^R v`；`d=3` surface 实现与 Stim 一致 | 一般论证为 CONJECTURED，有限实例为 numerical corroboration | 补齐一般证明，明确两 CSS sectors、边界向量、不可达态和故障字典 |
| 标准 surface 实例 | rotated surface `d=3,5,7` 在 Stim 的 `R=1..12` 均恒定；`d=3` 四种 schedule 的 transfer 计算在 `R=1..10` 均恒定 | NUMERICAL（作为实例子任务的部分证据） | 完成 `d=5,7` 第二种独立方法并形成可审计表格 |
| hook-misaligned surface 实例 | 决定性 gate 尚未完成 | OPEN / 部分计划 | 构造合法 misaligned schedules，完成 `R=1..d+2` 的双方法交叉检查 |
| qLDPC 实例 | 尚无满足题面的完整实例 | OPEN | 选定一个明确 code/schedule，计算或证明 `(d_infty,R_stab)` |
| 机制归因 | 在理想时间边界下，纯 timelike-logical 类为空；其余机制已有分类蓝图 | CONJECTURED | 给每个已算实例提供最小见证与排他性归因 |
| `R_stab>1` 是否存在 | 7,610 个已枚举 schedules 全部 `R_stab=1`，但这不是不存在性证明 | NUMERICAL absence evidence，按证据不对称规则只能低置信使用 | 构造一个合法反例，或证明某个清楚限定的 schedule 类具有 single-round dominance |

## 4. 新 canonical DAG

新版根节点仍为 `CIRCDIST.sat`，但它通过一条 AND-route 依赖三个可独立评审的子节点：

```text
CIRCDIST.sat
└── asymptotic-stability-assembly (AND)
    ├── CIRCDIST.sat.transfer   有限状态 / min-plus 表示
    ├── CIRCDIST.sat.window     单调性、d_infty、R_stab 与 B=d 窗口
    └── CIRCDIST.sat.instances  surface、misaligned、qLDPC 与机制归因
```

这样拆分的原因是：`window` 已有接近定理级的材料，`transfer` 的一般证明仍需补齐，
而 `instances` 明显没有完成。三者若混在根节点里，会把“结构定理已经很近”和“题面实例
尚缺两臂”错误地压成一个模糊状态。

## 5. 当前最短完成路线

1. 先把 `CIRCDIST.sat.window` 汇编为一个精确、独立的定理稿并做新命题级评审；这是最便宜、
   最可能关闭的节点。
2. 补 `CIRCDIST.sat.transfer` 的一般证明；数值程序只能作旁证，不能替代全称证明。
3. 对 surface `d=5,7` 补独立 transfer 计算，并完成 hook-misaligned arm。
4. 选一个规模可控且 schedule 定义明确的 qLDPC 实例。
5. 对每个实例输出最小见证、`d_infty`、`R_stab` 与机制标签；只有在搜索范围被明确记录后，
   才能使用“没有发现跨轮机制”这类缺席结论。

## 6. 目前可以对外说到什么程度

可以说：在当前理想边界模型下，`d_R` 不会上升；已有论证强烈支持它在至多 `d` 轮内
稳定，因此 `d_infty` 可由前 `d` 项决定。大量 surface/Steane/Shor 数值样本都在第一轮
就稳定。

还不能说：所有合法 schedule 都有 `R_stab=1`；一般 transfer 公式已经完成证明；
hook-misaligned 和 qLDPC 两类题面实例已经交付；新版第四题已经整体解决。

