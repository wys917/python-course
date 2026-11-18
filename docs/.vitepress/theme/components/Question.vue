<script setup lang="ts">
defineProps<{ questionId: string; title: string }>()
</script>
<template><article class="question-card" :aria-labelledby="questionId"><h3 :id="questionId" tabindex="-1"><a class="question-anchor" :href="`#${questionId}`" aria-label="链接到本题">{{ title }}</a></h3><div class="question-body"><slot /></div></article></template>

<style>
.question-body:has(> .question-tags) > p:first-child {
  margin-top: 0;
  color: var(--ink);
  font-size: clamp(16px, 1.5vw, 18px);
  font-weight: 600;
  line-height: 1.7;
}

.question-body > .question-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 8px;
  margin: 18px 0 0;
}

.question-tags + .answer {
  margin-top: 12px;
}

.question-tags > .question-tag {
  max-width: 100%;
  padding: 2px 9px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--soft);
  color: var(--text);
  font-size: 12px;
  font-weight: 400;
  line-height: 1.5;
  overflow-wrap: anywhere;
}
</style>
