<template>
  <div class="page-container">
    <h2>Movies</h2>
    <div class="movie-grid">
        <div class="movie-card" v-for="movie in movies" :key="movie.id">
            <img :src="movie.poster" alt="movie poster"/>
            <h3>{{ movie.title }}</h3>
            <p>{{ movie.genre }}</p>
        </div>
  </div>
  <router-link to="/home" class="back-btn"> <- Back to Home</router-link>
</div>
</template>

<script>
export default {
    data(){
        return{
            movies: [
                {id:1, title: "Inception", genre: "Sci-Fi", poster:"https://via.placeholder.com/150"},
                {id:2, title: "The Dark Knight", genre: "Action", poster:"https://via.placeholder.com/150"},
                {id:3, title: "Interstellar", genre: "Adventure", poster:"https://via.placeholder.com/150"}
            ],
        }
    }
  //name: "Page1",
}
</script>

<style scoped>
.page-container {
  padding: 30px;
  background: #1c1c1c;
  color: #fff;
  min-height: 100vh;
  text-align: center;
}
.movie-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
}
.movie-card {
  background: #272727;
  padding: 15px;
  border-radius: 10px;
  width: 180px;
  transition: 0.3s;
}
.movie-card:hover {
  transform: scale(1.05);
  box-shadow: 0 0 10px #ff3c38;
}
.movie-card img {
  width: 100%;
  border-radius: 5px;
}
.back-btn {
  display: inline-block;
  margin-top: 30px;
  color: #ff3c38;
  text-decoration: none;
  font-weight: bold;
}
.back-btn:hover {
  text-decoration: underline;
}
</style>