<script setup>
  defineProps(['recommendationData']);
  import Recommendation from '../components/Recommendation.vue'
</script>

<template>
  <Recommendation :location="recommendationData.location" :temperature="recommendationData.temperature" :recommendation="recommendationData.recommendation" />
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
