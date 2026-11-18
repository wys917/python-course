<script setup lang="ts">
import { ref } from 'vue'
import Icon from './Icon.vue'
const open = ref(false)
</script>
<template>
  <div class="answer" :class="{ 'is-open': open }">
    <button class="answer-toggle" :aria-expanded="open" @click="open = !open"><span class="answer-toggle-label"><Icon name="code" :size="17" />{{ open ? '收起答案与解析' : '查看答案与解析' }}</span><span class="answer-toggle-right">ANSWER <Icon name="chevron" :size="15" /></span></button>
    <div class="answer-grid" :aria-hidden="!open" :inert="!open"><div class="answer-overflow"><div class="answer-content"><slot /></div></div></div>
  </div>
</template>
