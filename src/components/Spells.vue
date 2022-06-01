<template>
  <SpellsCircleChart/>
  <SpellsGraph/>
</template>


<script>
import SpellsCircleChart from './SpellsCircleChart.vue'
import SpellsGraph from './SpellsGraph.vue'


export default {
  name: 'SpellsView',
  components: {
    SpellsCircleChart,
    SpellsGraph,
  },
  props: {},
}
</script>


<style scoped>

</style>
