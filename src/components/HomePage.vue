<template>
    <div id="introduction">
      <h1 style="text-align: left"> Introduction</h1>
      The world of Harry Potter was created by J.K. Rowling in the 
      beggining of the 21's century.It is a series of seven novels that 
      chronicle the life a Harry Potter, a young wizard and his friends
      Hermione Granger and Ron Weasly that learn magic in the famous 
      School of Witchcraft and Wizardy <p>Hogwarts</p>. In this website, 
      you will explore one fantasy part of this universe : the spells.
      What are the most common spell and their evolution during the 
      history. Also, you will found some visualisation that intend to 
      resume books.
    </div>
</template>

<script>
export default {
  name: 'HomePage',
}

</script>

<style scoped>
#introduction {
  width: 60%;
  margin-left: 20%;
  padding: 50px;
  color: var(--light_silver);
  text-align: justify;
  font-family: 'Fantasy';
  font-size: 22px;
  background-color: rgb(0, 0, 0, 0.7);
  border-radius: 10px;
}

p {
  font-family: 'Harry Potter', sans-serif;
  font-size: smaller;
  display: inline-block;
}

h1 {
  font-size: xx-large;
  font-family: 'Harry Potter', sans-serif;
}

h2 {
  font-size: large;
  font-family:fantasy;
  background-color: rgb(0, 0, 0, 0.8);

}
</style>
