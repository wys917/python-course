<script setup lang="ts">
import { withBase } from 'vitepress'
import Icon from './Icon.vue'
defineProps<{ href?: string; title: string; subtitle?: string; icon?: string; status?: string }>()
</script>
<template><component :is="href ? 'a' : 'div'" :href="href ? withBase(href) : undefined" class="resource-card" :class="{ 'is-placeholder': !href }"><span class="resource-icon"><Icon :name="icon || 'file'" :size="23" /></span><div class="resource-info"><span v-if="subtitle" class="eyebrow">{{ subtitle }}</span><h3>{{ title }}</h3><div class="resource-description"><slot /></div></div><span class="resource-status">{{ status || (href ? '查看内容' : '待更新') }}<Icon v-if="href" name="arrow" :size="18" /></span></component></template>
