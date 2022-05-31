import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import SpellsChart from '../components/SpellsChart.vue'
import WordsCloud from '../components/WordsCloud.vue'
import NotFound from '../components/NotFound.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/spells',
    name: 'spells',
    component: SpellsChart
  },
  {
    path: '/words',
    name: 'words',
    component: WordsCloud
  },
  {
    path: "/:catchAll(.*)",
    component: NotFound,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


export default router
