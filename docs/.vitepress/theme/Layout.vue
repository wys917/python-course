<script setup lang="ts">
import { computed, ref, watch, onMounted, onUnmounted, nextTick } from 'vue'
import { useData, withBase, useRoute } from 'vitepress'
import VPNavBarSearch from 'vitepress/dist/client/theme-default/components/VPNavBarSearch.vue'
import Icon from './components/Icon.vue'
import { useHomeMotion } from './useHomeMotion'
const { frontmatter, page, isDark } = useData()
const route = useRoute()
const menuOpen = ref(false)
const tocOpen = ref(false)
const currentAnchor = ref('')
const isHome = computed(() => frontmatter.value.layout === 'home')
const { moveCodeWindow, resetCodeWindow } = useHomeMotion(isHome)
const nav = [ ['Home', '/'], ['Topics', '/topics/'], ['Assignments', '/assignments/'], ['Quizzes', '/quizzes/'], ['Final Review', '/final-review/'] ]
const section = computed(() => nav.slice(1).find(n => route.path.includes(n[1])) || [])
const tocTitle = computed(() => section.value[0] === 'Assignments' ? '本次作业目录' : '本次小测目录')
const groups = computed(() => frontmatter.value.questionGroups || [])
const questionCount = computed(() => groups.value.reduce((sum: number, g: any[]) => sum + Number(g[2]), 0))
const topic = computed(() => frontmatter.value.chapter === true)
const headings = ref<{ id: string; text: string }[]>([])
async function refreshHeadings() {
  await nextTick()
  headings.value = [...document.querySelectorAll('.vp-doc h2[id]')].map(h => ({ id: h.id, text: h.textContent?.replace('#', '').trim() || '' }))
}
watch(() => route.path, refreshHeadings)
const quiz = computed(() => groups.value.length > 0)
function active(href: string) { return href === '/' ? isHome.value : route.path.includes(href) }
watch(() => route.path, () => { menuOpen.value = false; tocOpen.value = false })
watch(menuOpen, value => { if (typeof document !== 'undefined') document.body.style.overflow = value ? 'hidden' : '' })
function trackAnchor() {
  const headings = [...document.querySelectorAll('.question-card h3, .quiz-group')]
  let id = ''
  for (const h of headings) { if (h.getBoundingClientRect().top < 160) id = h.id }
  currentAnchor.value = id
}
onMounted(() => { window.addEventListener('scroll', trackAnchor, { passive: true }); refreshHeadings() })
onUnmounted(() => { window.removeEventListener('scroll', trackAnchor); document.body.style.overflow = '' })
</script>
<template>
  <a class="skip-link" href="#main-content">跳转到正文</a>
  <header class="site-header"><div class="header-inner">
    <a :href="withBase('/')" class="brand"><span class="brand-mark"><Icon name="code" :size="23" /></span><span class="brand-course"><strong>浙江大学</strong><span>Python 程序设计<span class="brand-detail"> · 2026 秋冬 · 孟炳泉老师班</span></span></span></a>
    <nav class="desktop-nav" aria-label="主导航"><a v-for="[label, href] in nav" :key="href" :href="withBase(href)" :class="{ active: active(href) }" :aria-current="active(href) ? 'page' : undefined">{{ label }}</a></nav>
    <div class="header-tools"><VPNavBarSearch /><span class="tool-divider"></span><button class="icon-button theme-toggle" :aria-label="isDark ? '切换浅色模式' : '切换深色模式'" @click="isDark = !isDark"><Icon :name="isDark ? 'sun' : 'moon'" /></button><button class="icon-button mobile-menu-button" :aria-expanded="menuOpen" aria-controls="mobile-nav" aria-label="切换导航菜单" @click="menuOpen = !menuOpen"><Icon :name="menuOpen ? 'close' : 'menu'" /></button></div>
  </div></header>
  <nav v-if="menuOpen" id="mobile-nav" class="mobile-nav" aria-label="移动导航"><a v-for="[label, href] in nav" :key="href" :href="withBase(href)" :class="{ active: active(href) }">{{ label }}<Icon name="arrow" /></a></nav>
  <main v-if="page.isNotFound" id="main-content" class="not-found"><span class="eyebrow">PAGE NOT FOUND</span><div class="error-number">404<span>_</span></div><h1>页面不存在</h1><p>请检查链接或返回首页。</p><a class="button-primary" :href="withBase('/')">回到课程首页 <Icon name="arrow" /></a></main>
  <main v-else-if="isHome" id="main-content" class="home-main">
    <section class="hero page-width"><div class="hero-copy"><div class="hero-kicker"><span></span> 浙江大学 · 课程学习资源</div><h1>Python<br /><span>Programming</span><i>.</i></h1><div class="hero-description"><p class="hero-course-title">Python 程序设计</p><p class="hero-course-meta"><span>2026 年秋冬学期</span><span>教师：孟炳泉</span><span class="hero-ta">助教：苏易文</span></p></div><div class="hero-actions"><a class="button-primary" :href="withBase('/quizzes/')">上机小测答案 <Icon name="arrow" :size="18" /></a><a class="button-text" :href="withBase('/topics/')">课程知识点 <Icon name="arrow" :size="17" /></a></div></div>
    <div class="hero-art" aria-hidden="true" @pointermove="moveCodeWindow" @pointerleave="resetCodeWindow"><div class="art-orbit orbit-one"></div><div class="art-orbit orbit-two"></div><span class="art-plus plus-one">+</span><span class="art-plus plus-two">+</span><div class="code-window"><div class="code-window-top"><span class="window-dots"><i></i><i></i><i></i></span><span>learning.py</span><Icon name="code" :size="15" /></div><div class="code-window-body"><div><span class="code-purple">def</span> <span class="code-yellow">learn_python</span>():</div><div class="indent">curiosity = <span class="code-green">True</span></div><br /><div class="indent"><span class="code-purple">while</span> curiosity:</div><div class="indent2">explore()</div><div class="indent2">practice()</div><div class="indent2"><span class="code-purple">yield</span> <span class="code-green">"a little better"</span><span class="terminal-caret"></span></div></div><div class="code-window-bottom"><span>learning.py</span><span>Python 3</span></div></div></div></section>
    <section class="course-overview page-width" aria-labelledby="course-overview-title">
      <div class="section-heading"><h2 id="course-overview-title">课程安排</h2></div>
      <div class="course-overview-grid">
        <div class="grading-panel"><h3>成绩构成</h3>
          <div class="grading-bar" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
          <dl class="grading-list">
            <div><dt>平时作业 <span>PTA 上完成</span></dt><dd>25<span>%</span></dd></div>
            <div><dt>课堂表现 <span>点名、随堂小测</span></dt><dd>5<span>%</span></dd></div>
            <div><dt>上机小测 <span>4 次</span></dt><dd>20<span>%</span></dd></div>
            <div><dt>期末考试 <span>理论 70 分 · 编程 30 分</span></dt><dd>50<span>%</span></dd></div>
          </dl>
        </div>
        <div class="exam-scope"><h3>考试范围</h3>
          <div class="scope-block"><div class="scope-heading"><h4>实验编程题</h4><span class="scope-chapters">第 <strong>1–6</strong> 章</span></div><p class="scope-exclusions"><span>不含</span><span class="scope-sections"><span>2.7</span></span></p></div>
          <div class="scope-block"><div class="scope-heading"><h4>理论题 <span>选择 / 填空 / 判断</span></h4><span class="scope-chapters">第 <strong>1–8</strong> 章</span></div><p class="scope-exclusions"><span>不含</span><span class="scope-sections"><span v-for="section in ['2.7','7.3','7.4','8.3','8.4','8.5']" :key="section">{{ section }}</span></span></p></div>
        </div>
      </div>
    </section>
    <section class="explore-section page-width"><div class="section-heading"><div><h2>课程资源</h2></div></div><div class="module-grid"><a v-for="(item, i) in [{en:'Topics',cn:'课程知识点',desc:'Python 知识体系。',href:'/topics/',icon:'book'},{en:'Assignments',cn:'课后作业',desc:'课后作业与参考解答。',href:'/assignments/',icon:'file'},{en:'Quizzes',cn:'课堂小测',desc:'课堂小测与详细解析。',href:'/quizzes/',icon:'quiz'},{en:'Final Review',cn:'期末复习',desc:'重点知识与复习资料。',href:'/final-review/',icon:'review'}]" :key="item.en" :href="withBase(item.href)" class="module-card"><div class="module-card-top"><span class="module-icon"><Icon :name="item.icon" :size="25" /></span><span class="module-index">0{{ i + 1 }}</span></div><span class="module-en">{{ item.en }}</span><h3>{{ item.cn }}</h3><p>{{ item.desc }}</p><span class="module-link">进入模块 <Icon name="arrow" :size="17" /></span></a></div></section>
    <section class="updates-section page-width"><div class="section-heading"><div><h2>最近更新</h2></div><a class="button-text" :href="withBase('/quizzes/')">全部小测 <Icon name="arrow" :size="17" /></a></div><a class="update-row" :href="withBase('/quizzes/quiz-02.html')"><span class="update-symbol"><Icon name="quiz" :size="23" /></span><div class="update-title"><span class="eyebrow">QUIZ 02 <span class="new-pill">已收录</span></span><h3>第二次上机小测 · 题目与解析</h3><p>判断、单选、填空、编程。</p></div><span class="update-meta">41 道题 · Python 3</span><Icon name="arrow" /></a><a v-for="update in [{title:'第一次上机小测',code:'QUIZ 01',description:'判断、单选、填空、编程。',count:'42 道题',href:'/quizzes/quiz-01.html'},{title:'第1–3章课后作业',code:'ASSIGNMENTS',description:'157 道题目及参考解析。',count:'3 次作业',href:'/assignments/'},{title:'第1–8章课程知识点',code:'TOPICS',description:'按教材章节整理。',count:'8 章',href:'/topics/'}]" :key="update.code" class="update-row" :href="withBase(update.href)"><span class="update-symbol"><Icon name="book" :size="23" /></span><div class="update-title"><span class="eyebrow">{{ update.code }}</span><h3>{{ update.title }}</h3><p>{{ update.description }}</p></div><span class="update-meta">{{ update.count }}</span><Icon name="arrow" /></a></section>
  </main>
  <main v-else id="main-content" class="document-main page-width" :class="{ 'quiz-layout': quiz || topic }"><div class="document-column"><nav class="breadcrumbs" aria-label="面包屑"><a :href="withBase('/')">Home</a><Icon name="chevron" :size="12" /><a v-if="quiz || topic" :href="withBase(section[1] || '/quizzes/')">{{ section[0] }}</a><template v-if="quiz || topic"><Icon name="chevron" :size="12" /><span>{{ frontmatter.code }}</span></template><span v-else>{{ section[0] || page.title }}</span></nav><header class="page-heading"><span class="eyebrow">{{ frontmatter.eyebrow || 'COURSE RESOURCES' }}</span><h1>{{ frontmatter.title }}</h1><p v-if="frontmatter.description">{{ frontmatter.description }}</p><div v-if="quiz" class="quiz-meta"><span><Icon name="quiz" :size="16" />{{ questionCount }} 道题</span><span>Python 3</span><span>参考答案默认收起</span></div></header><button v-if="quiz" class="toc-mobile-toggle" :aria-expanded="tocOpen" @click="tocOpen = !tocOpen">{{ tocTitle }} <Icon name="menu" :size="17" /></button><nav v-if="quiz && tocOpen" class="mobile-toc" :aria-label="tocTitle"><a v-for="[name, id, count] in groups" :key="id" :href="`#${id}`" @click="tocOpen = false">{{ name }} <span>{{ count }} 题</span></a></nav><details v-if="topic" class="topic-mobile-nav"><summary>本章目录</summary><a v-for="h in headings" :key="h.id" class="topic-anchor" :href="`#${h.id}`">{{ h.text }}</a></details><div class="vp-doc"><Content /></div></div>
    <aside v-if="quiz" class="quiz-sidebar"><div class="sidebar-inner"><a class="sidebar-back" :href="withBase(section[1] || '/quizzes/')">← 返回{{ section[0] }}</a><div class="sidebar-title">{{ tocTitle }}<span>{{ questionCount }} QUESTIONS</span></div><div v-for="[name,id,count] in groups" :key="id" class="sidebar-group"><a class="sidebar-group-title" :href="`#${id}`">{{ name }}<span>{{ count }}</span></a><div class="question-nav-grid"><a v-for="n in Number(count)" :key="n" :href="`#${id}-${n}`" :class="{ current: currentAnchor === `${id}-${n}` }" :aria-label="`${name}第 ${n} 题`">{{ String(n).padStart(2, '0') }}</a></div></div></div></aside>
    <aside v-if="topic" class="quiz-sidebar topic-sidebar"><div class="sidebar-inner"><a class="sidebar-back" :href="withBase('/topics/')">← 全部章节</a><div class="sidebar-title">本章目录</div><nav aria-label="本章目录"><a v-for="h in headings" :key="h.id" class="topic-anchor" :href="`#${h.id}`">{{ h.text }}</a></nav></div></aside>
  </main>
  <footer class="site-footer page-width"><div><a :href="withBase('/')" class="footer-brand"><span class="footer-course">浙江大学 · Python 程序设计</span><span class="footer-course-meta">2026 秋冬学期<span>孟炳泉老师班</span></span></a></div><span class="footer-ta">课程助教<span>苏易文</span></span></footer>
</template>
