<template>
  <NavigationBar/>
  <HomePage/>
  <GenealogyGraph/>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue'
import HomePage from './components/HomePage.vue'
import GenealogyGraph from './components/GenealogyGraph.vue'

export default {
  name: 'App',
  components: {
    NavigationBar,
    HomePage,
    GenealogyGraph
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
