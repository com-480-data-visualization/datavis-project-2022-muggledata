<template>
    <div class="topnavbar">
        <a class="title" v-on:click="changeComponent('HomePage')"> Muggle Data Project </a>
        <a class ="navbutton">Genealogy</a>
        <a class ="navbutton">Spells</a>
        <a class ="navbutton">Potions</a>
    </div>
</template>

<script>
export default {
	name: "NavigationBar",
	props: {
		msg: String,
	},
	select_component() {
		return {
			selected_component: "HomePage"
		}
	},
	methods: {
		changeComponent : function (component){
			// this.selected_component = component
			this.$emit("nextComponent", component)
		},
	}
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