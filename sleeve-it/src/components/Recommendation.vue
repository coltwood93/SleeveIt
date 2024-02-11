<script setup>
    import { useRecommendationStore } from '../stores/recommendationStore';
    import { computed } from 'vue';

    const store = useRecommendationStore();

    const temperature = computed(() => store.temperature);
    const recommendation = computed(() => store.recommendation);
    const location = computed(() => store.location);

    // Rounds the temperature to two decimal places
    const roundTemperature = (temp) => {
      return parseFloat(temp).toFixed(2);
    }

    // Determine CSS class based on value of temperature
    const getTemperatureClass = (temp) => {
      if (temp < 55) {
        return 'cold-temperature';
      } else if (temp > 75) {
        return 'hot-temperature';
      } else {
        return 'normal-temperature';
      }
    };
</script>

<template>
  <div>
    <h2>Recommendation</h2>
    <p>
      The current temperature in <span style="font-weight: bold;">{{ location }}</span>
        is <span :class="getTemperatureClass(temperature)">{{ roundTemperature(temperature) }}</span>
        degrees Fahrenheit.
    </p>
    <p>I recommend wearing <span style="font-weight: bold;">{{ recommendation }}</span>!</p>
  </div>
</template>

<style>
.cold-temperature {
  color: blue;
  font-weight: bold;
}

.hot-temperature {
  color: red;
  font-weight: bold;
}

.normal-temperature {
  font-weight: bold;
}
</style>