<template>
  <div class="page-container">
    <h2>📺 Series</h2>
    <div class="series-grid">
      <div class="series-card" v-for="series in seriesList" :key="series.id">
        <img :src="series.poster" alt="series poster"/>
        <h3>{{ series.title }}</h3>
        <p>{{ series.genre }}</p>
      </div>
    </div>
    <router-link to="/home" class="back-btn">⬅ Back to Home</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
      seriesList: [
        { id: 1, title: "Stranger Things", genre: "Sci-Fi", poster: "https://via.placeholder.com/150" },
        { id: 2, title: "Breaking Bad", genre: "Drama", poster: "https://via.placeholder.com/150" },
        { id: 3, title: "The Witcher", genre: "Fantasy", poster: "https://via.placeholder.com/150" }
      ],
    };
  },
};
</script>

<style scoped>
.page-container {
  padding: 30px;
  background: #1c1c1c;
  color: #fff;
  min-height: 100vh;
  text-align: center;
}
.series-grid {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
}
.series-card {
  background: #272727;
  padding: 15px;
  border-radius: 10px;
  width: 180px;
  transition: 0.3s;
}
.series-card:hover {
  transform: scale(1.05);
  box-shadow: 0 0 10px #ff3c38;
}
.series-card img {
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

