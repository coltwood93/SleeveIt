// Rounds the temperature to two decimal places
export const roundTemperature = (temp) => {
  return parseFloat(temp).toFixed(2);
}

// Determine CSS class based on value of temperature
export const getTemperatureClass = (temp) => {
  const COLD_THRESHOLD = 60;
  const HOT_THRESHOLD = 80;  
  
  if (temp < COLD_THRESHOLD) {
    return 'cold-temperature';
  } else if (temp > HOT_THRESHOLD) {
    return 'hot-temperature';
  } else {
    return 'normal-temperature';
  }
};
