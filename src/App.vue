<template>
  <NavigationBar/>
  <HomePage/>
  <SpellsChart/>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue'
import HomePage from './components/HomePage.vue'
import SpellsChart from './components/SpellsChart.vue'

export default {
  name: 'App',
  components: {
    NavigationBar,
    HomePage,
    SpellsChart,
  },
  methods: {
    changeComponent(component){
      this.component = component
    },
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
