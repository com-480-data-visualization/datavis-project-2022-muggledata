<template>
  <NavigationBar/>
  <WordsCloud/>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue'
import WordsCloud from './components/WordsCloud.vue'

export default {
  name: 'App',
  components: {
    NavigationBar,
    WordsCloud,
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
