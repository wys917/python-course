<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import { withBase } from 'vitepress'
import Icon from './Icon.vue'

// 每次发布新通知时修改版本号，访客会再看到一次
const VERSION = '2026-11-26-homework04-past-exams'
const STORAGE_KEY = 'update-notice-seen'
const open = ref(false)

function seen() {
  try { return localStorage.getItem(STORAGE_KEY) === VERSION } catch { return false }
}
function close() {
  open.value = false
  try { localStorage.setItem(STORAGE_KEY, VERSION) } catch {}
}
function onKey(e: KeyboardEvent) { if (e.key === 'Escape' && open.value) close() }

function reopen() { open.value = true }

onMounted(() => {
  if (!seen()) open.value = true
  window.addEventListener('keydown', onKey)
  window.addEventListener('open-update-notice', reopen)
})
onUnmounted(() => {
  window.removeEventListener('keydown', onKey)
  window.removeEventListener('open-update-notice', reopen)
})
</script>

<template>
  <Teleport to="body">
    <div v-if="open" class="notice-overlay" @click.self="close">
      <section class="notice-dialog" role="dialog" aria-modal="true" aria-labelledby="notice-title">
        <button class="notice-close" aria-label="关闭通知" @click="close"><Icon name="close" :size="18" /></button>
        <span class="notice-eyebrow">UPDATE NOTICE</span>
        <h2 id="notice-title">网站更新通知</h2>
        <ul class="notice-list">
          <li>
            <strong>第4章作业</strong>已更新：48 道题，附详细解析。
            <a :href="withBase('/assignments/homework-04.html')" @click="close">去看看</a>
          </li>
          <li>
            <strong>期末上机真题</strong>已收录：往届期末编程题 16 题，附参考代码与解析。
            <a :href="withBase('/final-review/past-exams.html')" @click="close">去看看</a>
          </li>
        </ul>
        <p class="notice-warning">
          <strong>请重点关注期末编程题。</strong>考试可能会考到原题或变式，建议每一题都认真做一遍、弄懂思路，确保每题都会。
        </p>
        <button class="notice-ok" @click="close">知道了</button>
      </section>
    </div>
  </Teleport>
</template>

<style>
.notice-overlay {
  position: fixed;
  inset: 0;
  z-index: 200;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  background: rgba(20, 30, 26, 0.5);
}
.notice-dialog {
  position: relative;
  width: min(460px, 100%);
  max-height: calc(100vh - 32px);
  overflow-y: auto;
  padding: 28px 26px 22px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  color: var(--text);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.25);
}
.notice-close {
  position: absolute;
  top: 12px;
  right: 12px;
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  border: 0;
  border-radius: 8px;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
}
.notice-close:hover { background: var(--soft); color: var(--ink); }
.notice-eyebrow {
  display: block;
  font-size: 11px;
  letter-spacing: 0.12em;
  color: var(--muted);
}
.notice-dialog h2 {
  margin: 6px 0 14px;
  padding: 0;
  border: 0;
  font-size: 22px;
  color: var(--ink);
}
.notice-list {
  margin: 0 0 16px;
  padding-left: 20px;
  line-height: 1.8;
}
.notice-list a {
  margin-left: 6px;
  color: var(--vp-c-brand-1);
  font-weight: 600;
  white-space: nowrap;
}
.notice-warning {
  margin: 0 0 18px;
  padding: 12px 14px;
  border-left: 3px solid var(--green);
  border-radius: 6px;
  background: var(--accent);
  color: var(--ink);
  line-height: 1.7;
}
.notice-ok {
  display: block;
  width: 100%;
  padding: 10px 0;
  border: 0;
  border-radius: 8px;
  background: var(--green);
  color: var(--surface);
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}
.notice-ok:hover { opacity: 0.9; }
</style>
