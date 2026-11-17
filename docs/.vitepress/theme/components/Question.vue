<script setup lang="ts">
defineProps<{ questionId: string; title: string }>()
</script>
<template><article class="question-card" :aria-labelledby="questionId"><h3 :id="questionId" tabindex="-1"><a class="question-anchor" :href="`#${questionId}`" aria-label="链接到本题">{{ title }}</a></h3><div class="question-body"><slot /></div></article></template>
