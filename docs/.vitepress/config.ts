import { defineConfig } from 'vitepress'
import container from 'markdown-it-container'
import mathjax3 from 'markdown-it-mathjax3'

const repository = process.env.GITHUB_REPOSITORY?.split('/')[1] || ''
const base = process.env.SITE_BASE || (repository && !repository.endsWith('.github.io') ? `/${repository}/` : '/')

export default defineConfig({
  title: '浙江大学 2026秋冬学期Python程序设计 孟炳泉老师班',
  description: '浙江大学Python 程序设计课程 孟炳泉老师班学习资源：知识点、课后作业、课堂小测与参考解析。',
  lang: 'zh-CN',
  base,
  cleanUrls: false,
  lastUpdated: false,
  head: [['link', { rel: 'icon', type: 'image/svg+xml', href: `${base}favicon.svg` }], ['meta', { name: 'theme-color', content: '#183e35' }]],
  themeConfig: {
    search: {
      provider: 'local',
      options: {
        miniSearch: {
          options: {
            tokenize(text) {
              const terms = text.match(/[a-zA-Z0-9_]+|[\p{Script=Han}]+/gu) || []
              return terms.flatMap(term => {
                if (!/\p{Script=Han}/u.test(term)) return [term]
                const chars = Array.from(term)
                return [...chars, ...chars.slice(0, -1).map((c, i) => c + chars[i + 1])]
              })
            }
          },
          _splitIntoSections(file, html) {
            const clean = (s: string) => s.replace(/<[^>]*>/g, ' ').replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')
            const questions = [...html.matchAll(/<Question question-id="([^"]+)" title="([^"]+)">([\s\S]*?)<\/Question>/g)]
            if (questions.length) return questions.map(m => ({ anchor: m[1], titles: [file.split('/').pop()?.replace('.md', '').toUpperCase() || '课程练习', clean(m[2])], text: clean(m[3]) }))
            const markdownTitle = html.match(/<h[12][^>]*>([\s\S]*?)<\/h[12]>/)?.[1]
            const chapter = file.match(/chapter-(\d+)/)?.[1]
            const title = chapter ? `第${Number(chapter)}章 ${clean(markdownTitle || '')}` : file.includes('/topics/') ? '课程知识点' : file.includes('/assignments/') ? '课后作业' : file.includes('/quizzes/') ? '课堂小测' : file.includes('/final-review/') ? '期末复习' : 'Python Programming'
            if (chapter) {
              const sections = [...html.matchAll(/<h2[^>]*id="([^"]+)"[^>]*>([\s\S]*?)<\/h2>([\s\S]*?)(?=<h2|$)/g)]
              return sections.map(m => ({ anchor: m[1], titles: [title, clean(m[2]).replace(/#$/, '').trim()], text: clean(m[3]) }))
            }
            return [{ anchor: '', titles: [title], text: clean(html) }]
          }
        },
        locales: { root: { translations: {
          button: { buttonText: '搜索课程内容', buttonAriaLabel: '搜索课程内容' },
          modal: { displayDetails: '显示详细内容', resetButtonTitle: '清除搜索', backButtonTitle: '返回', noResultsText: '未找到相关内容', footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' } }
        } } }
      }
    }
  },
  markdown: {
    theme: { light: 'github-light', dark: 'github-dark' },
    config(md) {
      md.use(mathjax3)
      md.use(container, 'question', {
        render(tokens, idx) {
          if (tokens[idx].nesting === -1) return '</Question>\n'
          const info = tokens[idx].info.trim().slice('question'.length).trim()
          const [id, ...title] = info.split(' | ')
          return `<Question question-id="${md.utils.escapeHtml(id)}" title="${md.utils.escapeHtml(title.join(' | '))}">\n`
        }
      })
      md.use(container, 'answer', { render: (tokens, idx) => tokens[idx].nesting === 1 ? '<Answer>\n' : '</Answer>\n' })
      md.use(container, 'explanation', { render: (tokens, idx) => tokens[idx].nesting === 1 ? '<div class="explanation"><div class="section-label">解析 <span>EXPLANATION</span></div>\n' : '</div>\n' })
    }
  }
})
