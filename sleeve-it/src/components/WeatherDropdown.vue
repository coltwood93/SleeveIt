<script setup>
  import { ref } from 'vue';
  import { useRecommendationStore } from '../stores/recommendationStore';
  import { computed } from 'vue';

  const store = useRecommendationStore();
  const showDropdown = ref(false);

  const toggleDropdown = () => {
    showDropdown.value = !showDropdown.value;
  };

  const feelslike = computed(() => store.feelslike);
  const windspeed = computed(() => store.windspeed);
  const humidity = computed(() => store.humidity);

  // Rounds the temperature to two decimal places
  const roundTemperature = (temp) => {
    return parseFloat(temp).toFixed(2);
  }

  // Determine CSS class based on value of temperature
  const getTemperatureClass = (temp) => {
    if (temp < 60) {
      return 'cold-temperature';
    } else if (temp > 80) {
      return 'hot-temperature';
    } else {
      return 'normal-temperature';
    }
  };

</script>

<template>
  <div class="weather-dropdown">
    <button @click="toggleDropdown">More Weather Info</button>
    <div v-if="showDropdown" class="dropdown-content">
      
      <p>Feels Like: <span :class="getTemperatureClass(feelslike)">{{ roundTemperature(feelslike) }}</span> degrees Fahrenheit</p>
      <p>Wind speed: <span style="font-weight: bold; color: rgb(175, 134, 248)">{{ windspeed }}</span> meters/second</p>
      <p>Humidity: <span style="font-weight: bold; color: rgb(175, 134, 248)">{{ humidity }}%</span></p>

    </div>
  </div>
</template>

<style scoped>
  .weather-dropdown {
    position: relative;
  }

  .dropdown-content {
    position: absolute;
    top: 100%;
    left: 0;
  }

  .cold-temperature {
  color: rgb(85, 85, 255);
  font-weight: bold;
}

.hot-temperature {
  color: rgb(247, 89, 89);
  font-weight: bold;
}

.normal-temperature {
  font-weight: bold;
}
</style>