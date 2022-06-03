<template>
  <WordsCloud/>
  <SentimentAnalysisGraph/>
</template>


<script>
import WordsCloud from './WordsCloud.vue'
import SentimentAnalysisGraph from './SentimentAnalysisGraph.vue'


export default {
  name: 'WordsView',
  components: {
    WordsCloud,
    SentimentAnalysisGraph,
  },
}
</script>


<style scoped>

</style>
