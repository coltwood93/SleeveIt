<script setup>
  import { ref } from 'vue';

  const location = ref('');

  const emit = defineEmits(['get-recommendation']);

  // tells HeaderComponent to communicate with backend
  const getRecommendation = async () => {
    emit('get-recommendation', location.value);
  };

  const clearSearch = () => {
    const confirmClear = window.confirm('Are you sure you want to clear the search?');
    if (confirmClear) {
      location.value = ''; // Clear the search bar
    }
  };

</script>

<template>
  <div>
    <input type="text" placeholder="Enter city name" v-model="location" @keyup.enter="getRecommendation">
    <button @click="getRecommendation">Get Recommendation</button>
    <br>
    <button @click="clearSearch">Clear</button>
  </div>
</template>
