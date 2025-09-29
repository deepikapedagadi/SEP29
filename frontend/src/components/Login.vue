<template>
  <div class= "login-container">
  <div class= "login-box">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <input v-model="email" placeholder="Email" required /><br></br>
      <input v-model="password" type="password" placeholder="Password" required /><br></br><br></br>
      <button type="submit">Login</button>
    </form>
    <br></br>
    <br></br>
    <router-link to="/register">Don't have an account?<br>Register</router-link>
    <p style="color:red">{{ error }}</p>
  </div>
</div>
</template>

<script>
import API from "../services/api";

export default {
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async login() {
      try {
        const res = await API.post("/login", { 
          email: this.email, 
          password: this.password 
        });
        localStorage.setItem("token", res.data.token); // store token
        this.$router.push("/home"); // redirect to home
      } catch (err) {
        this.error = err.response?.data?.message || "Login failed";
      }
    },
  },
};
</script>


<style scoped>
.login-container{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #1c1c1c, #2c2c2c);
  color: #fff;
}
.login-box{
  background: #272727;
  padding: 30px;
  border-radius: 10px;
  width: 350px;
  text-align: center;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
}
input{
  width: 90%;
  padding: 30px;
  margin: 10px 0;
  border-radius: 5px;
  border: none;
}
button{
  width: 95%;
  padding: 10px;
  border-radius: 5px;
  background-color: #ff3c38;
  border: none;
  color: white;
  font-weight: bold;
  cursor: pointer;
}
button:hover{
  background-color: #ff4d4d;
}
</style>
