<script setup>
    import { useRecommendationStore } from '../stores/recommendationStore';
    import { computed } from 'vue';

    const store = useRecommendationStore();

    const temperature = computed(() => store.temperature);
    const recommendation = computed(() => store.recommendation);
    const location = computed(() => store.location);
</script>

<template>
    <div>
      <h2>Recommendation</h2>
      <p>The temperature in {{ location }} is {{ temperature }} degrees Fahrenheit.</p>
      <p>I recommend wearing {{ recommendation }}!</p>
    </div>
  </template>