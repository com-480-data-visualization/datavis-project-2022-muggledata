import { createRouter, createWebHashHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import Spells from '../components/Spells.vue'
import Words from '../components/Words.vue'
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
    component: Spells
  },
  {
    path: '/words',
    name: 'words',
    component: Words
  },
  {
    path: "/:catchAll(.*)",
    component: NotFound,
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})


export default router
