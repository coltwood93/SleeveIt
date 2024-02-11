<script setup>
  import { ref } from 'vue';

  const location = ref('');

  const emit = defineEmits(['get-recommendation']);

  // tells HeaderComponent to communicate with backend
  const getRecommendation = async () => {
    emit('get-recommendation', location.value);
  };
</script>

<template>
  <div>
    <input type="text" placeholder="Enter city name" v-model="location" @keyup.enter="getRecommendation">
    <button @click="getRecommendation">Get Recommendation</button>
  </div>
</template>
