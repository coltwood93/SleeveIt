import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RecommendationView from '../views/RecommendationView.vue'

// Instructs which view to show based on URL address
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/recommendation',
      name: 'recommendation',
      component: RecommendationView
    }
  ]
})

export default router
