<script setup>
import SearchBar from './SearchBar.vue';
import router from '../router'
import { useRecommendationStore } from '../stores/recommendationStore';

const store = useRecommendationStore();

const handleRecommendation = async (location) => {
  store.setLocation(location);

  const response = await fetch(`http://127.0.0.1:5000/get_recommendation?location=${location}`, { // Use GET and query parameters
    method: 'GET',
  });
  const data = await response.json();
  store.setRecommendationData(data);
  router.push({ path: '/recommendation'});
};
</script>

<template>
  <div class="greetings">
    <h1 class="green">Sleeve It or Leave It?</h1>
    <SearchBar @get-recommendation="handleRecommendation" />
    <!-- <h3>
      You’ve successfully created a project with
      <a href="https://vitejs.dev/" target="_blank" rel="noopener">Vite</a> +
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a>.
    </h3> -->
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.2rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
