import { defineStore } from 'pinia';

export const useRecommendationStore = defineStore('recommendationStore', {
  state: () => ({
    location: "",
    temperature: null,
    recommendation: null,
  }),
  actions: {
    setLocation(location) {
      this.location = location;
    },
    setRecommendationData(data) {
      this.temperature = data.temperature;
      this.recommendation = data.recommendation;
    },
  },
});