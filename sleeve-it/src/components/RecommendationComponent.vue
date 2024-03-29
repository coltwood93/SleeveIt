<script setup>
  import WeatherDropdown from './WeatherDropdown.vue'
  import { useRecommendationStore } from '../stores/recommendationStore';
  import { computed } from 'vue';

  // pinia store for state management
  const store = useRecommendationStore();

  // get values from state store
  const temperature = computed(() => store.temperature);
  const recommendation = computed(() => store.recommendation);
  const location = computed(() => store.location);

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

  // Capitalize the first letter of each word in location
  const formattedLocation = computed(() => {
    return location.value
      .split(' ')
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
    }
  );
</script>

<template>
  <div>
    <h2><span style="font-weight: bold;">Recommendation</span> for
     <span style="font-weight: bold;">{{ formattedLocation }}</span></h2>
    <p>
      The current temperature is
       <span :class="getTemperatureClass(temperature)">{{ roundTemperature(temperature) }}</span>
       degrees Fahrenheit.
    </p>
    <p>I recommend wearing <span style="font-weight: bold; color: rgb(175, 134, 248)">{{ recommendation }}</span>!</p>
    <br>
    <WeatherDropdown />
  </div>
</template>

<style>
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
