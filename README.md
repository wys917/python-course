# Python 程序设计课程学习资源

在线网站：https://wys917.github.io/python-course/

课程教师：孟炳泉 · 课程助教：苏易文

原始 PTA 网页、课件及文案编辑稿仅保留在本地，不上传公开仓库。公开仓库包含整理后的题目、知识点、参考解答、测试和部署配置。

# Python Course

浙江大学 Python 程序设计课程的辅助学习网站，由课程助教维护，非学校官方网站。使用 VitePress + Vue + 自定义 CSS，构建后为纯静态文件，无后端、数据库、外部字体、图片 CDN 或付费 API。

已收录第 1–8 章知识点、第 1–3 章作业 157 题，以及两次小测 83 题，共 240 题。期末复习暂未整理。原始 HTML、PPTX、图片和 `2026下-PTA测试2_题目与答案解析.md` 均保留原样。资料问题和验证记录见 `materials/README.md`。

## 修改网站文案

根目录的 [网站文案编辑稿.md](./网站文案编辑稿.md) 汇总了全站界面文字以及 Quiz 02 全部题目、答案和解析。可直接修改并保存，再让 Codex「按照网站文案编辑稿更新网站」。这份文件作为修改需求稿，不会自动同步网页；更新网站时需同时维护对应页面与组件。

## 本地运行

安装 Node.js 22 或更新的受支持 LTS 版本（推荐 22），然后在项目根目录运行：

```sh
npm ci
npm run dev
```

打开终端显示的本地地址，通常是 `http://localhost:5173/`。停止服务按 Ctrl+C。

```sh
npm test         # 资料完整性与编程题所有原始样例；需要 Python 3
npm run build   # 构建到 docs/.vitepress/dist
npm run preview # 预览生产构建
```

浏览器回归测试（首次需要下载 Chromium，仅开发时使用）：

```sh
npx playwright install chromium
npm run test:e2e
```

测试覆盖：首页、四个栏目、8 章知识点、240 题数量与折叠、页面刷新、404、主题保存、代码复制、本地搜索、公式与图片、手机导航和页面宽度。

## 项目结构

```text
.github/workflows/deploy.yml   GitHub Pages 自动部署
 docs/.vitepress/config.ts    站点、Markdown、搜索与 base 配置
 docs/.vitepress/theme/       定制布局、组件和 CSS
 docs/public/                本地静态资源
 docs/index.md               首页入口
 docs/topics/index.md        知识体系
 docs/assignments/           作业目录和独立作业页面
 docs/quizzes/               小测目录和 quiz-02.md
 docs/final-review/          复习专区
 templates/                  未发布的作业、小测模板
 scripts/import-quiz.py      原始 Quiz 02 一次性导入脚本
 tests/                      资料核对与浏览器回归测试
```

首页排版位于 `docs/.vitepress/theme/Layout.vue`，题目正文与样式分离。正常添加课程内容只需编辑 Markdown。导入脚本会重新生成 Quiz 02，人工编辑页面后不要再次运行它，以免覆盖人工修订。

## 添加课后作业

1. 复制 `templates/assignment.md` 为 `docs/assignments/homework-01.md`。
2. 更新 frontmatter 的标题、英文编号与简介，替换所有占位内容。
3. 按下面的题目规范增加题目，使用唯一 ID，如 `hw01-q1`。
4. 在 `docs/assignments/index.md` 中删除初始空状态，添加入口：

```md
<ResourceCard href="/assignments/homework-01.html" title="第一次课后作业" subtitle="HOMEWORK 01" icon="file">填写本次作业的真实介绍。</ResourceCard>
```

继续添加 `homework-02.md`、`homework-03.md` 即可。

## 添加课堂小测

1. 复制 `templates/quiz.md` 为 `docs/quizzes/quiz-03.md`。
2. 更新标题和内容；普通模板无需配置侧边栏或修改组件。
3. 在 `docs/quizzes/index.md` 的 `resource-list` 内增加：

```md
<ResourceCard href="/quizzes/quiz-03.html" title="第三次课堂小测" subtitle="QUIZ 03" icon="quiz">填写本次小测的真实介绍。</ResourceCard>
```

4. 更新目录页已收录数量。首页“最近更新”位于 `Layout.vue`，发布新资料时相应更新入口与描述。

如需桌面题号侧栏和手机分组目录，在 frontmatter 添加（数量按实际填写）：

```yaml
code: Quiz 03
questionGroups:
  - [编程题, programming, 3]
```

对应分组标题使用 `<h2 id="programming" class="quiz-group">编程题</h2>`，三道题的 ID 分别使用 `programming-1`、`programming-2`、`programming-3`。侧栏按这些数据自动生成，作业页同样适用，无需修改组件。

## 题目、答案和解析规范

```md
:::: question hw01-q1 | Q01. 题目标题

<div class="section-label">题干 <span>QUESTION</span></div>

这里放完整题干。可以加入选项、表格、图片、代码和输入输出样例。

::: answer

这里放参考答案，可使用文字或 Python 代码块。

:::

::: explanation

这里放详细解析，可使用列表、公式、代码与样例。

:::

::::
```

外层使用 **四个冒号**，内层使用 **三个冒号**，每个容器与正文间保留空行。ID 不要含空格，页面内不可重复。答案默认收起，点击后动画展开；解析默认展示。代码块使用三个反引号并标记 `python`，自动高亮并提供复制按钮；输出样例标记 `text`，直接保留前导及末尾空格。不要用编辑器自动清除样例行尾空格。

公式：行内 `$x^2$`，独立公式用两行 `$$` 包围。公式在构建时用 MathJax 转换为内联 SVG，无需外部脚本和字体。原始资料目前没有独立公式，功能已配置可用于后续内容。

本地图片放在 `docs/public/images/`。Markdown 中可写 `![图片说明](/images/example.png)`，由 VitePress 处理 base；Vue 中使用 `withBase('/images/example.png')`。普通页面链接推荐明确的 `.html` URL 或目录 `/quizzes/`，便于 GitHub Pages 直接访问、刷新。

普通 Markdown 二级标题也可以直接链接 `#标题`；题目通过唯一 ID 定位。

## 搜索和主题

导航栏的放大镜打开 VitePress 本地搜索，可搜索中文、题目文字、解析、知识点与 Python 关键词。索引随构建更新，答案在折叠时仍被索引。快捷键 Ctrl+K / Command+K，Esc 关闭。数据保存在站点内，不调用第三方搜索服务。

深浅色切换会保存到本地浏览器，并默认尊重系统主题；答案展开状态不保存，刷新后重新收起。

## 创建 GitHub 仓库并上传

1. 在 GitHub 登录，点击 **New repository**。
2. 仓库名可设为 `python-course`，通常选择 Public 以便使用免费 GitHub Pages。不要勾选自动添加 README，以免首次推送冲突。
3. 在当前项目目录运行（替换 `YOUR_NAME` 和仓库名）：

```sh
git init
git add .
git commit -m "Build Python course website"
git branch -M main
git remote add origin https://github.com/YOUR_NAME/python-course.git
git push -u origin main
```

认证按 GitHub 提示完成，可使用 GitHub CLI 或个人访问令牌。`node_modules`、构建缓存与测试截图已被忽略。原始资料会随源码提交；如需限制源资料访问，请先选择适合的仓库可见性。

## 启用 GitHub Pages

1. 打开仓库 **Settings → Pages**。
2. 在 **Build and deployment → Source** 选择 **GitHub Actions**。
3. 向 `main`（亦支持 `master`）推送后，工作流自动安装锁定依赖、核对内容、构建并部署。
4. 也可以打开 **Actions → Deploy course to GitHub Pages → Run workflow** 手动部署。
5. 等待工作流 build 和 deploy 全部成功。最终链接显示在部署任务的 environment 链接和 Settings → Pages 顶部。

普通项目仓库的网站地址：

```text
https://YOUR_NAME.github.io/python-course/
```

如果仓库名就是 `YOUR_NAME.github.io`，则地址为：

```text
https://YOUR_NAME.github.io/
```

配置从 Actions 的 `GITHUB_REPOSITORY` 自动读取仓库名，普通仓库使用 `/仓库名/`，以 `.github.io` 结尾的仓库使用 `/`。不要在 Actions 中硬编码仓库名。没有 GitHub 环境变量的本地开发默认使用 `/`。

如使用自定义域名，在 GitHub Pages 配置域名，并在仓库 **Settings → Secrets and variables → Actions → Variables** 增加 `SITE_BASE=/`，同时将工作流构建步骤设置为：

```yaml
- run: npm run build
  env:
    SITE_BASE: ${{ vars.SITE_BASE }}
```

本地测试项目子路径：

```sh
SITE_BASE=/python-course/ npm run build
SITE_BASE=/python-course/ npm run preview
```

按预览服务器提示访问 `/python-course/`，不要访问根路径。发布前恢复普通 `npm run build`。构建生成每个页面的 HTML 与 `404.html`，因此直接访问或刷新 `.html` 路径均可使用。GitHub Pages 对不存在的 URL 使用同风格 404 页面。

该目录当前没有关联远程仓库，因此尚无线上网址；创建仓库、推送并启用 Pages 后即可完成首次发布。
