<script setup>
import { RouterView } from 'vue-router'
import HeaderComponent from './components/HeaderComponent.vue'
</script>

<template>
  <header>
    <RouterLink to="/">
      <img alt="Vue logo" class="logo" src="./assets/Sleeve-It Logo.png" width="125" height="125" />
    </RouterLink>
    
    <div class="wrapper">
      <HeaderComponent />
    </div>
  </header>

  <div class="center">
    <RouterView />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

header .wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
    margin-right: 1rem;
  }
}

@media (max-width: 1024px) {
  header {
    margin-top: 2rem;
    margin-bottom: 2rem;
  }
}

.center {
  display: flex;
  justify-content: center;
}

@media (min-width: 1024px) {
  .center {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
