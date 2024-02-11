<script setup>
  defineProps(['recommendationData']);
  import RecommendationComponent from '../components/RecommendationComponent.vue'
</script>

<template>
  <div class="center">
    <RecommendationComponent />
  </div>
</template>

<style>

.center {
  display: flex;
  justify-content: center;
}

@media (min-width: 1024px) {
  .center {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
