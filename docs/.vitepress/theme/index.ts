import DefaultTheme from 'vitepress/theme-without-fonts'
import Layout from './Layout.vue'
import Question from './components/Question.vue'
import Answer from './components/Answer.vue'
import ResourceCard from './components/ResourceCard.vue'
import './style.css'
import './code-window.css'
import './home-motion.css'

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    app.component('Question', Question)
    app.component('Answer', Answer)
    app.component('ResourceCard', ResourceCard)
  }
}
