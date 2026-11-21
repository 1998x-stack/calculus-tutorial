# 微积分 · 从入门到精通

一套从函数、极限、连续性到导数、积分、多元微积分与数学建模的中文课程。项目以纯静态 HTML 为主体，数学公式使用原生 MathML，交互图形使用本地 SVG 与 JavaScript；无需 CDN、账号或后端服务。

**课程入口：** https://1998x-stack.github.io/calculus-tutorial/

## 学习路径

| 阶段 | 章节 | 主题 |
|---|---:|---|
| 函数与极限 | 01–07 | 函数、数列极限、函数极限、无穷小、连续性、闭区间定理、极限计算 |
| 导数与应用 | 08–14 | 导数定义、求导法则、中值定理、泰勒公式与导数应用 |
| 积分与累积 | 15–18 | 不定积分、积分技巧、定积分与微积分基本定理 |
| 多元与空间 | 19–25 | 向量、偏导、多元极值、重积分、曲线/曲面积分与积分定理 |
| 级数与建模 | 26–28 | 无穷级数、常微分方程、微积分与机器学习 |

## 首批精细化章节

01–08 章已按统一教学结构重新编排：函数映射；ε–N 数列极限；ε–δ 函数极限；无穷小阶与两个重要极限；连续与间断；闭区间定理和二分法；七种未定式的策略选择；导数定义与切线几何。

第 09–28 章保留原有内容与入口，后续可沿同一规范逐批精修。

## 仓库结构

```text
.
├── index.html                  # 静态首页：路径、搜索、28 章目录
├── 01.html ... 28.html         # 章节正文
├── courses.json                # 结构化课程元数据
├── theme.css                   # 兼容入口
├── assets/
│   ├── css/calculus.css        # 首页、章节和旧章节统一设计系统
│   └── js/calculus.js          # 交互实验与目录筛选
├── scripts/validate_site.py    # 数学标记、链接、结构静态校验
├── tests/browser.spec.js       # Playwright 桌面/移动端浏览器验收
├── playwright.config.js
├── package.json
├── docs/first-eight-audit.md   # 首批八章数学审计记录
├── AGENTS.md                   # 后续内容维护和验证规范
└── .github/workflows/validate.yml
```

## 本地预览

```bash
python3 -m http.server 4173
# 浏览器访问 http://127.0.0.1:4173/
```

## 验证

```bash
python scripts/validate_site.py
npm install
npx playwright install chromium
npm test
```

静态校验检查 28 章入口、站内链接、MathML 结构、SVG 可访问标签与本地依赖。浏览器验收覆盖首页搜索、首批 8 章、MathML 呈现、交互状态和窄屏横向溢出。

## 数学与交互约定

- 数学表达使用语义化 MathML；复杂公式不以普通文本、Unicode 拼凑或 `<code>` 代替。
- 长公式放入可键盘聚焦、可横向滚动的区域；页面本身不允许横向溢出。
- 每张 SVG 图必须有 `title`、`desc` 和说明文字；默认静态图本身就要能讲清核心概念。
- 交互必须改变有意义的数学输出，不能只做装饰；所有滑块提供标签、数值和 live status。
- 证明、例题与数值实验分开标注；数值实验用于直观检验，不替代证明。
- 双侧极限必须检查左右两侧；等价无穷小替换必须检查乘除结构与抵消风险。

## 参考资料

- [OpenStax Calculus Volume 1](https://openstax.org/details/books/calculus-volume-1)
- [MIT OpenCourseWare 18.01SC — Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)
- [3Blue1Brown — Calculus lessons](https://www.3blue1brown.com/topics/calculus)
- [Calculo — Interactive Calculus Simulations](https://calculo.knovay.com/)
- [NIST DLMF — About MathML](https://dlmf.nist.gov/help/mathml)

本项目借鉴渐进式图解和交互式数学实验的教学方法，所有课程文字、示意图与交互均独立编写，不复制第三方教材的图文素材。
