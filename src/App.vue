<template>
  <NavigationBar/>
  <HomePage/>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue'
import HomePage from './components/HomePage.vue'

export default {
  name: 'App',
  components: {
    NavigationBar,
    HomePage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
