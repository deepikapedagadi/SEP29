<template>
  <div class="register-container">
    <div class="register-box">
      <h1>Register</h1>
      <form @submit.prevent="register">
        <input v-model="name" type="name" placeholder="full name" required/>
        <input v-model="email" type="email" placeholder="Email" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <button type="submit">Register</button>
      </form>
      <p class="success" v-if="success">{{ success }}</p>
      <p class="error" v-if="error">{{ error }}</p>
      <router-link to="/">Already have an account? Login</router-link>
    </div>
  </div>
</template>

<script>
import API from "../services/api";

export default {
  data() {
    return {
      email: "",
      name: "",
      password: "",
      success: "",
      error: "",
    };
  },
  methods: {
    async register() {
      try {
        const res = await API.post("/register", {
          email: this.email,
          password: this.password,
          name: this.name,
        });
        this.success = res.data.message;
        this.error = "";
        this.email = "";
        this.password = "";
      } catch (err) {
        this.error = err.response?.data?.message || "Registration failed";
        this.success = "";
      }
    },
  },
};
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to right, #1c1c1c, #2c2c2c);
  color: #fff;
}
.register-box {
  background: #272727;
  padding: 30px;
  border-radius: 10px;
  width: 350px;
  text-align: center;
  box-shadow: 0 0 15px rgba(0,0,0,0.5);
}
input {
  width: 90%;
  padding: 10px;
  margin: 10px 0;
  border-radius: 5px;
  border: none;
}
button {
  width: 95%;
  padding: 10px;
  background-color: #ff3c38;
  border: none;
  border-radius: 5px;
  color: white;
  font-weight: bold;
  cursor: pointer;
}
button:hover {
  background-color: #ff1c0f;
}
.success {
  color: #4caf50;
  margin-top: 10px;
}
.error {
  color: #ff4d4d;
  margin-top: 10px;
}
</style>
