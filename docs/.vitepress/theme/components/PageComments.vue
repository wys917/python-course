<script setup lang="ts">
import { defineAsyncComponent, onMounted, ref } from 'vue'
import { useData } from 'vitepress'

defineProps<{ thread: string }>()
const { isDark } = useData()
const Giscus = defineAsyncComponent(() => import('@giscus/vue'))
const opened = ref(false)
onMounted(() => {
  if (new URLSearchParams(window.location.search).has('giscus')) opened.value = true
})
</script>

<template>
  <section id="comments" class="page-comments" aria-labelledby="comments-title">
    <h2 id="comments-title">本页讨论</h2>
    <p>对哪道题有疑问？留言时可以带上题号。评论公开可见，请勿填写姓名、学号等个人信息。</p>
    <button v-if="!opened" type="button" class="button-primary" @click="opened = true">加载评论</button>
    <span v-if="!opened" class="comments-hint">阅读无需登录，发言需登录 GitHub。</span>
    <Giscus v-if="opened" repo="wys917/python-course" repo-id="R_kgDOVxsR-g"
      category="General" category-id="DIC_kwDOVxsR-s4DLZlk" mapping="specific" :term="thread"
      strict="1" reactions-enabled="1" input-position="top" lang="zh-CN" :theme="isDark ? 'dark' : 'light'" />
    <p class="comments-hint comments-link"><a href="https://github.com/wys917/python-course/discussions/categories/general">直接前往 GitHub 讨论区</a></p>
  </section>
</template>

<style scoped>
.page-comments { margin: 36px 0; padding-top: 24px; border-top: 1px solid var(--line); }
.page-comments h2 { margin: 0; color: var(--ink); font-size: 20px; }
.page-comments p { line-height: 1.7; }
.page-comments button { border: 0; }
.comments-hint { display: inline-block; margin: 8px 0; font-size: 13px; }
button + .comments-hint { margin-inline-start: 10px; }
.comments-hint a { text-decoration: underline; }
.comments-link { display: block; }
</style>
