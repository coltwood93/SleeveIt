<script setup>
    defineProps(['location', 'temperature', 'recommendation']);
</script>

<template>
    <div>
      <h2>Recommendation</h2>
      <p>The temperature in {{ location }} is {{ temperature }} degrees Fahrenheit.</p>
      <p>I recommend wearing {{ recommendation }}!</p>
    </div>
  </template>