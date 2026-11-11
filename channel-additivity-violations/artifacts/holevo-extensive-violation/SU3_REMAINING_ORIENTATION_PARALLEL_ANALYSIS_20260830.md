# 剩余 SU(3) 三面方向的降维证书路线

日期：2026-08-30

状态：旁路解析与数值路线选择；**不是证书，不支持任何节点升级**。本文没有修改现有
proof-DAG 节点，也没有终止、重启或改写正在运行的 input-centered triangle、weakest
bent 或其他六维输入脚本。

## 1. 范围与现状

本文核对了 `DAG_PROTOCOL.md`、`FILE_PROTOCOL.md`、三面分类与 cover-complexity
artifacts，以及以下实现：

- `certify_su3_input_centered_triangle_sixdim.py`；
- `certify_su3_weakest_bent_three_face_cluster.py`；
- `certify_su3_chain_three_face_sixdim_covers.py`；
- 公共后端 `certify_su3_triangular_three_face_clusters.py`、
  `certify_su3_highest_edge_adjacent_faces.py`、
  `certify_su3_all_elementary_cycles.py` 与 `su3_common_den_controls.py`。

两个重点方向的当前精确问题为：

| 方向 | 当前保留块 | 连续维数 | Gram 端点 |
|---|---|---:|---:|
| input-centered triangle `((-2,1),(-1,-1),(0,0))` | 四个 binary 块 | 6 | 12 |
| weakest bent `((-3,0),(-2,1),(0,0))` | 三个 binary 块 | 5 | 36 |

下文给出两个更短的候选路线。所有抽样都直接最大化**端点化后的 Gram 表达式**，而不是
只计算原通道的 Gram 值，因此它们检验的是正确的 fixed-side 充分条件；但浮点抽样仍然
不能取代全参数证书。

用于复现路线选择的非证书脚本为

`holevo-extensive-violation/tools/analyze_su3_remaining_orientation_shortcuts.py`。

它只使用浮点抽样，文件头与输出语义均明确标为 non-certificate。

## 2. 新引理 A：标签扇区 cover 拼接

设 `R_1,R_2` 是两个 fixed-original-side cover，`D_1,D_2` 是标签域的 cover。若在
每个 `D_i` 上，用同一个端点 pattern 保留全部 Gram 相关性的精确计算证明

\[
 B\!\left(\max_e t_{i,e}\right)
 >2\min_{r\in R_i}H(q_r),
\]

且 `D_1 union D_2` 包含所有允许的 Dynkin 标签，则 fixed-original-side endpoint
lemma 分别作用在两个扇区，并立即给出整个标签域的 Bell no-gap 结论。不同扇区允许使用
不同的原始 side cover；这里没有把 endpoint-channel side output 当作原通道输出，也没有
交换任何不合法的量词。

证明只是现有 endpoint lemma 在标签域上的有限分片应用。这个引理的意义是：**没有必要
寻找一个全局成立的三块 cover**。

## 3. Input-centered triangle：一个六维问题降为两个五维问题

### 3.1 两个互补三块 cover

令 `P,Q>=0` 是当前脚本中的 residual Dynkin labels，并令

\[
 a={P\over P+1},\qquad b={Q\over Q+1}.
\]

数值路线选择发现以下两个三块 cover 互补：

1. 低 `P` cover

   ```text
   R_low = ((-1,1),(1,0),(2,-2))
   ```

   分支型为 `h/m, h/m, h/c`，连续变量为 `(a,b,x,y,z)`，其余四块给出
   `2*3*2*2=24` 个相关 Gram 端点。

2. 高 `P` cover

   ```text
   R_high = ((-2,0),(1,-3),(1,0))
   ```

   分支型为 `c/m, h/c, h/m`，同样是五维、24 个相关 Gram 端点。

选择阈值

\[
 a_*=63/64\quad\Longleftrightarrow\quad P=63.
\]

候选精确分片为

\[
 D_{\rm low}=\{0\le a\le63/64,\ 0\le b\le1\},\qquad
 D_{\rm high}=\{63/64\le a\le1,\ 0\le b\le1\}.
\]

这两个闭盒甚至覆盖整个连续 compactified 标签域，而不只覆盖整数标签。阈值是 dyadic，
所以无需新的非二分 de Casteljau 算法：沿 `a` 轴连续取右半区六次即可得到
`[63/64,1]`；低区是其余六个 dyadic slabs 的并。

### 3.2 数值压力

用 30,000 个普通与 corner-biased 三维权重点、标签集
`0,1,4,16,48,64,128,1024,10^6` 检验**端点化后的**不等式，得到：

| 扇区/cover | 最小抽样自然对数裕量 | 位置 |
|---|---:|---|
| `R_low`, `P<=63` | `0.008756953452` | `P=63,Q=48` |
| `R_high`, `P>=63` | `0.006972278794` | `P=64,Q=0` |

额外 100,000--250,000 点与更密标签压力（含 `Q=0.1,8,32,96,256,10^12`）仍保持
正值；所有压力运行中看到的最小值约 `0.00515` nat。这个裕量比当前四块 cover 的抽样
裕量小，但从六维降到五维通常比端点数从 12 增到 24 更重要。

30,000 点复现命令：

```text
PYTHONPATH=holevo-extensive-violation/tools \
<home>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
holevo-extensive-violation/tools/analyze_su3_remaining_orientation_shortcuts.py \
triangle --samples 30000
```

### 3.3 为什么必须分扇区

`R_low` 正是已知 fixed-three 失败路线。现有 artifact 已给出
`P=10^6,Q=64` 的精确负 witness；本次端点化探针也在该点得到约
`-0.00379305` nat。因此不能把 `R_low` 全局化。

`R_high` 也不能全局化。取

```text
P=0, Q=4, weights=(1,0,3/8), endpoint pattern=(1,0,2,0)
```

精确计算给出

\[
 t={66713\over94325},
\]

三个保留 side distributions 为

\[
 (1/10,1/10,4/5),\quad(1/10,3/20,3/4),\quad(1/2,1/2,0).
\]

公共 24-term rational logarithm区间给出 gap upper bound
`-0.1637059899629` nat，严格为负。因此高 `P` cover 必须排除小标签区。

此外，六个 binary input offsets 的全部 `C(6,3)=20` 个三块 cover 在测试标签集上都各有
负的端点化 witness。最好的全局单 cover 仍是 `R_low`，但其抽样最小值为负。故目前最强
的降维结论是**两个扇区 cover**，不是某个遗漏的全局三块 cover。

### 3.4 精确实现蓝图

公共五维后端已经支持三个 binary retained coordinates；不需要沿用六维脚本。两个配置
的精确次数与端点数为：

| 配置 | cleared Gram degrees | side degrees | endpoints |
|---|---|---|---:|
| `R_low` | `(12,12,2,2,2)` | `(5,5,1,1,1)` | 24 |
| `R_high` | `(12,12,2,2,2)` | `(4,4,1,1,1)` | 24 |

建议新建独立 exact checker（不要改当前输入脚本）：

1. 分别重构两个 `Configuration` 的 24 个 Gram numerators；
2. compactify 后，先沿 `a` 轴得到上述 low/high 初始 slabs；
3. 在各自扇区使用原来的 correlated side entropy upper bounds；
4. 加入下文的 active-pattern pruning 与 axis scoring；
5. 两个扇区都完成后再组装 sector-cover lemma。

## 4. Weakest bent：整数角切除把五维降为四维/三维

### 4.1 两块 cover 及其唯一坏角

只保留两个 `h/m` 原始块

```text
R_2 = ((-1,1),(1,0)).
```

则变量为 `(a,b,x,y)`，其余五块产生 72 个相关 Gram 端点。这个四维 cover 不能直接在
整个连续域使用，因为原点有如下精确反例：

```text
P=Q=0, (x,y)=(0,7/10), endpoint pattern=(0,0,0,1,0).
```

精确值为

\[
 t={793\over1120},\qquad q_x=q_y=(1/4,3/4,0).
\]

现有 rational-log bounds 给出

\[
 B(793/1120)-2H(1/4,3/4)< -0.0124474513116<0.
\]

所以“全局四维 fixed-two cover”被严格排除。这不是原通道 Bell witness，只是又一个
selected-side/endpoint 充分条件的失败 witness。

### 4.2 新引理 B：整数角切除

`P,Q` 是非负整数，故

\[
 \mathbb Z_{\ge0}^2=
 \{P\ge1,Q\ge0\}\ \dot\cup\
 \{P=0,Q\ge1\}\ \dot\cup\ \{(0,0)\}.
\]

因此只需三个较低维证书：

| 标签片 | cover | 精确维数 | endpoints |
|---|---|---:|---:|
| `P>=1,Q>=0` | `R_2` | 4 | 72 |
| `P=0,Q>=1` | `R_2` | 3 | 72 |
| `P=Q=0` | 当前 `((-1,-2),(-1,1),(1,0))` | 3 | 36 |

在 compact variables 中，第一片就是 `a>=1/2`，第二片是面 `a=0,b>=1/2`，原点是
`a=b=0`。全部都是一次 specialization 或 dyadic half split；没有开放边界或极限量词。

### 4.3 数值压力

30,000 点端点化压力给出：

| 标签 | fixed-two 最小抽样 gap (nat) |
|---|---:|
| `(0,0)` | `-0.012447451312`（上述严格失败） |
| `(0,1)` | `0.040795571947` |
| `(1,0)` | `0.044089935816` |
| `(1,1)` | `0.121686370024` |
| `(10^6,0)` | `0.036742910353` |
| `(0,10^6)` | `0.008973971556` |
| `(10^6,10^6)` | `0.004226933106` |

原点使用当前 fixed-three cover 的 300,000 点端点化压力仍为正，最小约
`0.01771197` nat。复现 fixed-two 表的命令为：

```text
PYTHONPATH=holevo-extensive-violation/tools \
<home>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
holevo-extensive-violation/tools/analyze_su3_remaining_orientation_shortcuts.py \
bent --samples 30000
```

### 4.4 精确实现蓝图

fixed-two cleared degrees 为

```text
Gram: (14,12,2,2)
side: (4,4,1,1)
```

公共五维函数目前把三个 retained coordinates 写死为 `x,y,z`，所以不要用一个无效的
dummy `z` 保留第五维。应从同一后端抽出按 `retained_coordinate_count` 参数化的四维
版本，然后：

1. 在完整 compact controls 上沿 `a` 取右半区，处理 `P>=1`；
2. 在 `a=0` 面 specialization，再沿 `b` 取右半区，处理 `P=0,Q>=1`；
3. 在 `a=b=0` specialization 上跑当前三块 cover 的纯三维权重证书。

这比继续一个 5D/36-branch 均匀 subdivision 更短；72 branches 的代价可由第 6 节的精确
pruning 明显减小。

## 5. Exact reconstruction 与 compactification 边界审计

### 5.1 次数是否足够

Gram denominator 是

\[
 8\,D_I(P,Q)\prod_E (r_E+1)(s_E+1)(r_E+s_E+2),
\]

其中 `D_I` 是全部 input dimensions 之和。每个 local `chi^2` 项与 cross term 的唯一
有理分母都整除某个 environment dimension 的三个线性因子；乘清分母后，标签次数不超过
上述 denominator 的标签次数。每个 binary block 的次数至多 2；ternary stick-breaking

\[
 (u,(1-u)v,(1-u)(1-v))
\]

在每个 stick coordinate 中次数也至多 2。side distribution 对每个 stick coordinate
分别至多一次。故现有 interpolation degree tuples 足够，没有发现 higher-degree aliasing。

不过，脚本目前只有两个额外有理点的 reconstruction equality tests；这些点本身不能逻辑上
证明次数上界。正式 theorem artifact 应把上一段的 degree/divisibility lemma 写成显式证明，
或者在构造器中直接符号生成 cleared polynomial，而不应只把 spot checks 称为次数证明。

### 5.2 compactification 恒等式

对标签次数 `(d_P,d_Q)` 的 polynomial `f`，代码 `compactify` 精确构造

\[
 \widetilde f(a,b,\xi)=
 (1-a)^{d_P}(1-b)^{d_Q}
 f\!\left({a\over1-a},{b\over1-b},\xi\right).
\]

binomial loop 正是两个因子 `(1-a)^(d_P-i)`、`(1-b)^(d_Q-j)` 的展开。因此在
`a,b<1` 上 numerator/denominator ratio 与原有理函数完全相同。所有有限整数标签都映入
这个开方形，故 `a=1` 或 `b=1` 上的极限点不可能遗漏一个真实标签。

### 5.3 matched projective zeros

设同一 Bernstein grid 上

\[
 N=\sum_i n_i B_i,\qquad D=\sum_i d_iB_i,
\]

且 `d_i>=0`。若 `d_i=0` 时也有 `n_i=0`，则在 `D>0` 的所有点

\[
 {N\over D}=\sum_{d_i>0}{n_i\over d_i}
 {d_iB_i\over D}.
\]

右端是 control ratios 的凸组合。因此 `rational_range_common` 跳过 matched zeros 是严格
安全的；若 denominator control 为零而 numerator 不为零，代码会立即报
`unmatched projective zero`。双无穷角 `(a,b)=(1,1)` 可能代表不同比例的趋近路径，但每个
有限 interior 点仍受上述凸组合控制；没有因把多条射线压到一个角而漏掉有限标签。

若某方向的 gap infimum 在无穷角恰为零，闭盒算法可能永远得不到严格正裕量，但这只会导致
不终止/未证，而不会产生假阳性。当前探针的两块 bent cover 在大标签平衡方向仍见约
`0.004` nat 裕量，没有观察到零极限，但正式 checker 仍应保留这个失败模式。

### 5.4 simplex 与有限标签边界

stick-breaking map 覆盖闭 simplex 的全部边界；在 `u=1` 时 `v` 不唯一只造成重复参数，
不造成遗漏。`P=0`、`Q=0` 由 `minimum_base` 后的实际 representation labels 直接计算，
本次精确 rational witnesses 也实际经过这些代码路径，没有发现非法 branch 或被漏掉的
barycenter component。

**审计结论：**没有发现现有 reconstruction/compactification 会漏掉真实边界。需要补强的
是对 degree bound 与 matched-zero convex-ratio argument 的书面证明，而不是修改数学域。

## 6. 可直接降低长跑成本的精确后端改进

以下改进都不改变证书逻辑。

### 6.1 Active-pattern pruning lemma

对当前 box `C`，设 exact Bernstein ratios 给出每个 endpoint branch 的区间
`[L_e(C),U_e(C)]`。若

\[
 U_e(C)<\max_f L_f(C),
\]

则 branch `e` 在 `C` 的任何点都不可能实现 Gram maximum，可从该 box 的所有后代永久
删除。证明是逐点的：某个 `f` 在整个 box 上都至少为右端 lower bound，而 `e` 在整个 box
上都不超过其 upper bound。

这只需现有 `rational_range_common` 已经返回的 lower endpoint，不引入浮点数。当前循环却
丢弃了 lower endpoints，并在每个后代继续 split 所有 12/36 branches。

抽样 winner 数虽然不是 pruning 证明，但说明收益可能很大：

| 候选路线 | 总 patterns | 压力样本中实际成为 winner 的 patterns |
|---|---:|---:|
| bent fixed-two | 72 | 10 |
| triangle low sector | 24 | 10 |
| triangle high sector | 24 | 12 |

### 6.2 共同分母上的整型比较

所有 endpoint numerators 共用同一个**多项式** Gram denominator。现有 common-den backend
只对每个 tensor 单独取一个整数 scalar denominator。可在初始化时再取一次所有 Gram
numerator controls 与 Gram denominator controls 的全局 LCM，使 branch lower/upper、
dominance 与 pruning 全部变为整数 cross multiplication。无需把 controls 转回逐项
`Fraction`。

不要只保存 controlwise maximum tensor 后再 subdivision：父盒上逐 control 取 `max_e`
会混合不同 endpoint patterns，split 后无法恢复 branch correlation，通常显著变松。安全
做法是保留 active branches，或保留下述 block potentials，并在每个子盒重新取 envelope。

### 6.3 分块 Bernstein / max-plus 消元

endpoint Gram numerator 是 retained-only base、每个 eliminated block 的 unary potential，
以及共享 environment 产生的 pair potentials 之和。对每个 Bernstein control index，这仍是
一个有限离散能量最大化问题。

- 当前 weakest-bent 三块 cover 的 eliminated interaction graph 是一条短链；
- triangle 的两个新 cover 分别是小 triangle-with-tail 与小 star。

可保存这些 unary/pair potential control tensors，de Casteljau 后在每个 child control 上用
max-plus dynamic programming/直接小图 variable elimination 求 endpoint envelope。这样避免
为 36 或 72 个完整 numerator tensors 全部复制和 split，同时仍在每个子盒重新最大化，
不会犯“父盒 controlwise max tensor”失去相关性的错误。

### 6.4 选择 split axis，而不是 round-robin

当前 axis 规则是最小 `(depth,axis)`，因此一个困难路径会近似轮流切所有坐标。建议对每个
允许 axis 做一次 exact trial split，计算两个 child 的

```text
t_upper, side_upper, certified/uncertified, margin deficit
```

优先选择能立即证掉最多 child、其次使最大 deficit 最小的 axis。trial split 仍是 exact
de Casteljau；它只改变搜索顺序。若全 trial 太贵，可用 numerator/denominator control spread
作第一阶段 cheap score，再对前两个 axis 真 split。

### 6.5 specialization 必须真正降维

在 bent 的 `P=0` 或 `P=Q=0` slices，应先对 Bernstein controls 取边界 control face并删除
对应 axis；不要保留 dummy coordinate。否则形式上虽分片，盒数仍按原维数增长。

## 7. 额外解析观察与未采用路线

Bell isotropic entropy 满足

\[
 B'(t)=-{8\over9}\log{1+8t\over1-t}<0,
 \qquad
 B''(t)=-{8\over(1+8t)(1-t)}<0.
\]

对一个 binary retained weight `w`，固定其他参数后 `t(w)` 是凸二次式，因此

`B(t(w))` 是凹函数。若所用 side upper bound 与 `w` 无关，区间最小值在 endpoints；这
正是 endpoint lemma 的 entropy-level 解释。若把该块自己的 side entropy 也放入右端，
则 `B(t(w))-2H(q_w)` 是两个凹函数之差，不能据此断言端点最小。故没有采用“把第四个
triangle weight 直接解析消掉”的不充分路线。

可行但尚未实现的加强是：在 `w` 的小区间上用 entropy tangent 作 affine upper bound；
`B(t(w))` 减 affine 仍为凹，因而只需区间 endpoints。若再与其他 side upper bound 的常数
最小值分片，需要显式处理 affine/constant crossover。这个方法可能把当前四块路线变成
有效五维 branch-and-bound，但实现复杂度高于第 3 节已经找到的两个固定五维 cover。

没有使用 Weyl、共轭或图反射把两个方向等同。分类 artifact 明确禁止导入未证明的
channel-level symmetry；实际 labelled incidence 与最小标签边界也不支持一个可立即使用的
全局交换对称性。

## 8. 最强可用结论与执行优先级

1. **优先新跑 input-centered triangle 的 sectorized 5D exact checker。** 两个 24-branch
   cover 在 dyadic 阈值 `a=63/64` 处重叠；已有明确的 sector-cover lemma 与正压力裕量。
2. **并行实现 weakest-bent integer-corner excision。** 主体是 `a>=1/2` 上的 4D/72-branch
   checker，另加一个 3D face 与一个 3D origin checker；原点失败已被严格定位。
3. 在两条新 checker 中先加入 active-pattern pruning 和 axis scoring；它们比重写 entropy
   bound 风险更低，也更容易独立审计。
4. 当前长跑仍可自然完成并保留为独立证书或交叉审计；本分析不授权停止它们。

这些结论目前仍是路线选择。只有新 exact runs 完成、terminal certificates 落盘、节点按
DAG protocol 链接并经过独立审查后，才能改变任何 orientation node 的 assessment。
