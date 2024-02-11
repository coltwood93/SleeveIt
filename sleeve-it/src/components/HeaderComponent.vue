<script setup>
import SearchBar from './SearchBar.vue';
import router from '../router'
import { useRecommendationStore } from '../stores/recommendationStore';

// pinia store for state management
const store = useRecommendationStore();

// send request to backend when user searches location
const handleRecommendation = async (location) => {
  // update state store
  store.setLocation(location);

  // request recommendation from backend
  const response = await fetch(`http://127.0.0.1:5000/get_recommendation?location=${location}`, {
    method: 'GET',
  });
  const data = await response.json();

  // update state store
  store.setRecommendationData(data);

  // display recommendation to user
  router.push({ path: '/recommendation'});
};
</script>

<template>
  <div class="greetings">
    <h1 class="purple">Sleeve It or Leave It?</h1>
    <SearchBar @get-recommendation="handleRecommendation" />
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
