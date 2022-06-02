<template>
  <div style="position:absolute">
    <div id="introduction">
      <h1 style="text-align: left"> Introduction</h1>
      <h2>The world of Harry Potter was created by J.K. Rowling in the 
      beggining of the 21's century.It is a series of seven novels that 
      chronicle the life a Harry Potter, a young wizard and his friends
      Hermione Granger and Ron Weasly that learn magic in the famous 
      <p>School of Witchcraft and Wizardy Hogwarts</p>. In this website, 
      you will explore one fantasy part of this universe : the spells.
      What are the most common spell and their evolution during the 
      history. Also, you will found some visualisation that intend to 
      resume books.
      </h2>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  props: {},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#introduction {
  width: 70%;
  padding-left: 15%;
  color: var(--light_silver);
  text-align: justify;
  font-family: 'Harry Potter', sans-serif;
}
p {
  font-family: 'Harry Potter', sans-serif;
  font-size: small;
  display: inline-block;
}

h1 {
  font-size: xx-large;
  font-family: 'Harry Potter', sans-serif;
}

h2 {
  font-size: large;
  font-family:fantasy;
}
</style>
