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

  // send request to backend when user searches location
  const requestRandomLocation = async () => {

    // request recommendation from backend
    const response = await fetch(`${import.meta.env.VITE_MICROSERVICE_URL}/cities`, {
      method: 'GET'
    });

    const data = await response.json();

    // set search location
    location.value = `${data.city}, ${data.state}`;

    // initiate search
    getRecommendation()
  };
</script>

<template>
  <div>
    <input type="text" placeholder="Enter city name" v-model="location" @keyup.enter="getRecommendation">
    <button @click="getRecommendation">Search</button>
    <br>
    <button @click="requestRandomLocation">Random City</button>
    <button @click="clearSearch">Clear</button>
  </div>
</template>
