<script setup>
  defineProps(['recommendationData']);
  import Recommendation from '../components/Recommendation.vue'
</script>

<template>
  <div class="center">
    <Recommendation />
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
