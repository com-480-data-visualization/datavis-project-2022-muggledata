<template>
    <div class="topnavbar">
		<router-link :to="{name: 'home'}"><a class="title"> Muggle Data Project </a></router-link>
		<router-link :to="{name: 'spells'}"><a class ="navbutton">Spells</a></router-link> 
		<router-link :to="{name: 'words'}"><a class ="navbutton">Words</a></router-link> 
    </div>
</template>

<script>
export default {
	name: "NavigationBar",
	props: {
		msg: String,
	},
};
</script>

<style scoped>
h1 {
    cursor: pointer;
}
/*
	TOP Navigation Bar
*/
.topnavbar {
	top: 0;
	overflow: hidden;
	background-color: var(--navbar_background);
	padding: 0px 10px;
	position: fixed;
	width: 100%;
	z-index: 500;
}

/* Style of the title inside the box */
.topnavbar .title{
	float: left;
	color: var(--title);
	font-family: 'Harry Potter', sans-serif;
	font-size: large;
	padding-top: 9px;
	padding-left: 10px;
	padding-right: 10px;
}

.topnavbar .navbutton {
	top: 0;
	float: left;
	color: var(--light_silver);
	background-color: var(--navbar_background);
	text-align: center;
	padding: 10px 10px;
	text-decoration: none;
	font-size: 17px;
}

.topnavbar .navbutton:hover {
	color: var(--navbar_background);
	background-color: var(--light_silver);
}
</style>