// Rounds the temperature to two decimal places
export const roundTemperature = (temp) => {
  return parseFloat(temp).toFixed(2);
}

// Determine CSS class based on value of temperature
export const getTemperatureClass = (temp) => {
  if (temp < 60) {
    return 'cold-temperature';
  } else if (temp > 80) {
    return 'hot-temperature';
  } else {
    return 'normal-temperature';
  }
};
