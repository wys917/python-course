import { nextTick, onMounted, onUnmounted, watch } from 'vue'
import type { ComputedRef } from 'vue'

/** Progressive enhancement: content stays visible without JS or motion support. */
export function useHomeMotion(isHome: ComputedRef<boolean>) {
  let observer: IntersectionObserver | undefined
  let preference: MediaQueryList | undefined
  let generation = 0

  function reset() {
    observer?.disconnect()
    observer = undefined
    document.querySelectorAll('[data-reveal]').forEach(el => {
      el.removeAttribute('data-reveal')
      ;(el as HTMLElement).style.removeProperty('--reveal-delay')
    })
  }

  async function setup() {
    const current = ++generation
    await nextTick()
    if (current !== generation) return
    reset()
    if (!isHome.value || preference?.matches || !('IntersectionObserver' in window)) return

    observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue
        entry.target.setAttribute('data-reveal', 'visible')
        observer?.unobserve(entry.target)
      }
    }, { threshold: 0.08 })

    const elements = document.querySelectorAll<HTMLElement>(
      '.course-overview .section-heading, .grading-panel, .exam-scope, ' +
      '.explore-section .section-heading, .module-card, .updates-section .section-heading, .update-row'
    )
    elements.forEach(el => {
      // Already-visible content is never briefly hidden during hydration.
      if (el.getBoundingClientRect().top < window.innerHeight) return
      const siblings = [...el.parentElement!.children]
      const delay = el.classList.contains('module-card') ? siblings.indexOf(el) * 65 : 0
      el.style.setProperty('--reveal-delay', `${delay}ms`)
      el.setAttribute('data-reveal', 'pending')
      observer?.observe(el)
    })
  }

  function moveCodeWindow(event: PointerEvent) {
    if (preference?.matches || event.pointerType !== 'mouse' ||
      !window.matchMedia('(hover: hover) and (pointer: fine)').matches) return
    const art = event.currentTarget as HTMLElement
    const bounds = art.getBoundingClientRect()
    const x = ((event.clientX - bounds.left) / bounds.width - 0.5) * 10
    const y = ((event.clientY - bounds.top) / bounds.height - 0.5) * 8
    art.style.setProperty('--pointer-x', `${x}px`)
    art.style.setProperty('--pointer-y', `${y}px`)
  }

  function resetCodeWindow(event: PointerEvent) {
    const art = event.currentTarget as HTMLElement
    art.style.removeProperty('--pointer-x')
    art.style.removeProperty('--pointer-y')
  }

  onMounted(() => {
    preference = window.matchMedia('(prefers-reduced-motion: reduce)')
    preference.addEventListener('change', setup)
    setup()
  })
  watch(isHome, setup)
  onUnmounted(() => {
    generation++
    preference?.removeEventListener('change', setup)
    reset()
  })

  return { moveCodeWindow, resetCodeWindow }
}
