<template>
  <div class="home-container">
    <h2>Welcome Home!</h2>
    <p>Choose a page:</p>
    <div class="nav-cards">
    <ul>
      <li><router-link to="/page1" class="card">Page 1</router-link></li>
      <li><router-link to="/page2" class="card">Page 2</router-link></li>
    </ul>
    </div>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/");
    },
  },
};
</script>


<style scoped>
.home-container{
  text-align: center;
  padding: 50px;
  background: linear-gradient(to right, #655555, #fdf7f7);
  color: #fff;
  min-height: 100vh;
}
.nav-cards{
  display: flex;
  justify-content: center;
  gap: 30px;
  margin: 30px 0;
}
.card{
  display: block;
  padding: 20px 40px;
  background-color: #eed3d3;
  color: #3e3c3c;
  font-size: 20px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: bold;
  transition: 0.5s;
}
.card:hover{
  background-color: #e5d0cf;
  transform: scale(1.05);
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin: 10px;
}
button{
  padding: 10px 20px;
  background-color: #ef0c0c;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover{
  background-color: #d85959;
}
</style>