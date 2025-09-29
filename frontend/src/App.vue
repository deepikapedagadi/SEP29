//Root component i.e. wraps router-view
<template>
  <div id = "app">
    <router-view></router-view>
  </div>
</template>

<style>
body{
  font-family: Arial, sans-serif;
}
#app {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px; 
}
</style>

<script>
export default{
  name: "App",
};
</script>

