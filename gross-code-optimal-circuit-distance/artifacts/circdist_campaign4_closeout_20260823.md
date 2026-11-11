# CIRCDIST 战役 4 闭卷报告(2026-08-23)

调度:Fable 5(监督/决策/状态写入)。执行:Opus 5 工人会话(证明/计算/评审)。
预算:**64.75 / 65 box**;战役 4 共 32 波(waves 1–32),全部串行(round-12 模式切换后无一例外)。
验证终态:`proof_dag_check.py --problem all` 绿(se 85 + ksum 144 + circdist 16 = 245 节点),append-only 绿。
canonical 家:`Claim-Centered-Research-Graph`(2026-08-23 自 discovery-new-algorithms 迁入,旧家冻结)。

---

## 1. 终局棋盘

| 节点 | 等级 | hash 绑定 |
|---|---|---|
| CIRCDIST.lift(课题二根) | **PROVED** | 6e463ba0 |
| CIRCDIST.lift.iff | **PROVED** | 0c4c466b |
| CIRCDIST.lift.nonint | **PROVED** | e2d1b292 |
| CIRCDIST.lift.gap-example | **PROVED** | e080155d |
| CIRCDIST.gross.dext-cap | **PROVED** | 4bc0b5eb |
| CIRCDIST.cplx.islands | **PROVED** | 2e786e96 |
| CIRCDIST.sat(课题四根) | CERTIFIED\* | c6205671 |
| CIRCDIST.sat.window | CERTIFIED\* | 8698b051 |
| CIRCDIST.sat.transfer | CERTIFIED\* | eb50730d |
| CIRCDIST.sat.instances | CERTIFIED\* | c71ac7cd |
| CIRCDIST.gross(课题一根) | CONJECTURED(candidate 路线 NUMERICAL 已审) | — |
| CIRCDIST.gross.mc-equiv | REFUTED·DEAD | — |
| CIRCDIST.cplx.sigma2 | OPEN(止损,结构化残差) | — |

**PROVED ×6,CERTIFIED\* ×4。** 每个完成级节点都有 hash 绑定的独立对抗评审;每次 claim 修订都走"评审先祝福确切字节、调度后安装"的原子流程。

## 2. 四题逐题终局

**课题二(closed-lift 判据)— 整根 PROVED,完全闭合。**
判据(iff:d_circ = min ℓ(γ),零电压/monodromy 刻画,单轮可计算性)、非交错推论、严格不等式实例、根组装全部 PROVED。题面把全部假设写进正文:逐 sector graph-like、合法 + (MC)、R ≥ d_sec(交叉配对)、最小重量、修复代价措辞。战役内新数学:**正确窗口常数 d_sec**(交叉配对:d_X 界 Z-memory、d_Z 界 X-memory),紧性由链族 Q_m 实证为**无界**——旧常数 d 的错误在 d_X = d_Z 实例上原理性不可见。

**课题四(重复轮稳定性)— 按改定题面闭合于 CERTIFIED\*。**
三前提与根全部 CERTIFIED\*。**战役最大发现:R_stab > 1 存在**——构造的 hook 错位调度族给出 R_stab = 2/3/4(d = 5/7/9),d = 5/7 过敌意评审(三独立方法);单轮支配被见证型证据推翻;拟合律 R_stab = (d−1)/2 留为 CONJECTURED。停在 CERTIFIED\* 的诚实理由:三步桥引理在前提 claim 文本之外(R-C4)、共享冻结模型单点(R-C1)、路线非平坦合取(R-C12)。

**课题三(Eff-Preserve 复杂度)— 可解侧 PROVED,难度侧止损。**
四个可解岛(因子化/自证;HGP;有界树宽 Courcelle;d=3 双序 2-SAT)加承重桥 **Theorem B(d_ext = min(d_eff^X, d_eff^Z),全 CSS 通用、无 promise)** 整卷 PROVED。第五岛子句被 Steane 见证驳倒后诚实删除(重加需先定义 "choice-free")。Σ₂ᴾ-难度侧:sigma2 止损持有,残差结构化(DEEP-FLAG 子命题 + Seed Barrier 定理封死 R4 padding 路)。

**课题一(Gross 码 D\*)— 主体已证,头名 11-vs-12 未判。**
PROVED:每个合法调度 d_ext ≤ 11。已审 NUMERICAL:候选族 990/990 UNSAT ⇒ d_ext = 11 双 sector,SBB 距离-11 猜想在正确 φ=a+b 族确认,Figure-12 像素核验(唯一具名风险解除)。**精确残差**:D\* ∈ {11,12};12 的唯一机制 = completion gap ≥ 1,判定工具即课题二判据(已 PROVED,d_sec 在手);冲 12 = 见证型搜索(侦察价 P≈0.2),证 11 = 全称 no-go(缺席型,P≈0.12)。gap-via-lift 路线登记在案,随时续跑。SBB Thm 1 以正式外部假设登记(定理照发表引用,证明未独立验证)。

## 3. 评审架构战绩(本战役核心论据)

- **约 15 处数学/文本缺陷,100% 由下一层独立评审抓获,自审 0 次。** 样本:错误窗口常数 d(五层评审放过、第六层用 d_X≠d_Z 见证击破);islands V 子句(自家 Amendment §6.2 早算过反例、六层没连线、端到端一击);CE12 Prop 5.13 反极性错引(页码自洽、唯读陈述可破);R_stab 差一(前提口径 2、根口径 1);(MC) 双载体丢失。
- **三个系统性缺陷模式**(供协议改进):① 全电路事实错移植为逐 sector(d vs d_sec 类);② **针对 implication 字段的已接受修理从不被执行**(R2、R6 两半、C-M6——三连发现;建议 se/ksum 也做同类清扫);③ 页码自洽型错误引文(Prop 5.13、draft-页码挂印刷版名——只有真读陈述才能抓)。
- 证据不对称公理再验:见证型零翻车;缺席型两次死于"仓库里已有的对象"。
- 共同局限(如实入册):全战役共享同一冻结公共定义模型,**无任何 stim 交叉验证**——模型与真实编译器的系统性错配可穿透所有独立实现。

## 4. 战役内产生的新定理(评审驱动)

1. **d_sec 交叉配对窗口常数** + Lemma A(极小假设)+ 无界紧性族 Q_m(wave 22,wave 23 独立确认)。
2. **Theorem B**:d_ext(E(M)) = min(d_eff^X, d_eff^Z),全 CSS 码全调度、无 promise;附结构事实"无单一位置双 sector 贡献 hook"(wave 20,三套独立实现确认)。
3. **R_stab > 1 调度族** + 拟合律(wave 24,wave 25 敌意确认)。
4. 全电路读法下 5.10 的补证(L2 二分法首次获得真证明)。
5. Seed Barrier(sigma2,R4 路封死)。

## 5. 站立事项(战役外)

- 课题一 gap-via-lift 狩猎(D\* = 11 或 12)。
- sigma2 DEEP-FLAG(Σ₂ᴾ-难度)。
- islands V 子句重加(先定义 choice-free);Island V 一般情形(task-004)。
- iff 子节点 (MC) 卫生折入(task-008,非阻断);iff/islands 整卷合并稿(非阻断)。
- sat:W-G4 紧性、R_stab 拟合律证明、d_X≠d_Z 实例臂。
- 仓库级"已接受未执行修理"清扫(se/ksum)。
- 独立性升级:任一关键结果的 stim 交叉验证。

## 6. 预算决算

25(战役 1–3)+ 39.75(战役 4 waves 1–32,含被 lead 指令中断的 wave 10)= **64.75 / 65**。
逐波账目在 `research/circdist/notes/SCHEDULER.yaml` round_log(rounds 1–36-final)。


---

# 战役 5 附录(2026-08-23,+8 box,64.75 → 73.0 满额收官)

## A1. 战役 5 终局增量

| 项 | 战役 4 终态 | 战役 5 终态 |
|---|---|---|
| 课题四 transfer | CERTIFIED\*(桥在文档内) | CERTIFIED\*,**三条桥折入认证题面**(hash 8fb50ff0;BB 最小重量结论双 sector 验证,第 27 单"不可行"被关) |
| 全战役共享模型 caveat | "无任何 stim 验证" | **stim 1.16.0 交叉验证 5/5 MATCH**(含 R_stab>1 发现格点从 stim DEM 复现;两个具名风险面被扰动实验证明惰性;四节点 caveat 按授权降格) |
| 课题四根 | CERTIFIED\*(R-C4 桥 + R-C1) | CERTIFIED\*,阻断收敛到**一个新发现**:根题面未钉检测器划分而值随划分而动(V3 折入 = 最后一道 PROVED 门,**待 lead 批准**);R-C4 (a)(b)(c) 注销;R-C1 先例张力正式解决(随 PROVED 的范围注记);A1 机器可见登记 |
| 课题一 candidate 路线 | NUMERICAL | **CERTIFIED\***:链 3 唯一性在更大空间穷举池上重推(72 读法一对象)、链 4 编码保真双向往返、**SBB Thm 1 证明验证通过**(顺带修好论文两处缺陷,一处由评审员自证闭合) |
| 课题一 D\* | 未启动 | **狩猎两段打完**:见证候选生一次死一次(死因精确:第 4 个增益形状被漏检——第 16 处缺陷,仍是下层评审抓获);D\* 仍 OPEN ∈ {11,12},P(12)=0.10 / P(11)=0.15,证据向 11 倾斜 |

## A2. 狩猎净产出(全部提案级,机器与日志在档)

- **三面 no-go 墙**:check-serial(全局势)类 repair-0 整类证明;完全 TI 调度保不住双 sector d_eff = 11;M_cand 的 297/297 交错重定时全部死于水平 hook。
- **Lemma D**:d_eff 只依赖检查内顺序 ⇒ M_cand 的 160 CPU 时认证免费迁移到其全部交错重定时(至 504/648 交错)。
- 结构事实:gross 逻辑算符重量全偶(重量-13 空);增益形状恰四种(2-前缀是此前全战役误读为后缀的那种)。
- 判定器 + 穷举层机器在档,含地面真值校准记录——任何未来战役可直接续跑。
- 二手来源相互印证:第 38 单的独立穷举代码对 M_cand 给 0 构型,与 990 全 UNSAT 相符——候选认证又多一层。

## A3. 决算与纪律

73.0/73(战役 5 实耗 8.25:含 33a plan 模式截断 0.5、33b/38 两次网络损耗 0.75,均无过失入账)。缺陷台账累计 **16 处,100% 由下一层独立评审抓获,自审 0**。战役 5 新墨:blessed-then-installed 流程零事故运行 6 次;两次基础设施中断(plan 模式传导、API/网络)均按盘面抢救 + resumeFromRunId 恢复。

## A4. 站立事项(更新)

1. **sat V3 折入(待 lead 一句话)**:钉 Definition 3.5 进课题四根题面 → 课题四整根 PROVED,~0.5 box。
2. D\* 决战(如再拨预算):修复后的 d_eff 过滤器 + 四形状全查重扫非 TI 空间;或攻 D\* = 11 的第四面墙(水平 hook 论证一般化)。
3. islands V 子句(choice-free 定义)、iff/islands 合并稿、se/ksum 决议单清扫、LRAT 抽查——皆非阻断。
