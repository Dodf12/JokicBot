
<template>
  <div id="app-container">
    <!-- <div class="top-banner">
      <p>JokicBot is now live! Add it to your server today.</p>
      <a href="#">Add to Discord &rarr;</a>
    </div> -->
    <header class="main-header">
      <div class="logo">JokicBot</div>
      <nav class="main-nav">
        <a href="#">Features</a>
        <a href="#">Commands</a>
        <a href="#">Support</a>
      </nav>
      <nav class="user-nav">
        <a href="#" class="button-primary" onclick="window.location.href='https://discord.com/oauth2/authorize?client_id=1297777471944392714'">Add to Discord</a>
      </nav>
    </header>
    <main class="hero-section">
      <div class="hero-text">
        <h1>The ultimate fantasy basketball companion for Discord</h1>
        <p>Get real-time player stats, fantasy projections, and league-winning insights directly in your Discord server. Powered by the MVP.</p>
        <a href="#" class="button-secondary" onclick="window.location.href='https://discord.com/oauth2/authorize?client_id=1297777471944392714'">Add to Your Server</a>
      </div>
      <div class="hero-logo-container">
        <img src="@/assets/jokicBotLogo.png" alt="JokicBot Logo" class="bouncing-logo" />
      </div>
    </main>
  </div>
</template>

<script>
function redirectToDiscord() {
  window.location.href = "https://discord.com/oauth2/authorize?client_id=1297777471944392714";
}
</script>

<style scoped>
#app-container {
  background-color: #1b1b1b;
  color: #fff;
  min-height: 100vh;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: flex;
  flex-direction: column;
}

.top-banner {
  background-color: #0062ff;
  color: white;
  text-align: center;
  padding: 0.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  font-size: 0.9rem;
}

.top-banner a {
  color: white;
  font-weight: bold;
  text-decoration: none;
}

.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  border-bottom: none;
  position: relative;
}

.main-header::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 100px;
  background: linear-gradient(to bottom, rgba(0, 98, 255, 0.15), transparent);
  pointer-events: none;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.main-nav, .user-nav {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.main-header a {
  color: #ccc;
  text-decoration: none;
  transition: color 0.3s;
}

.main-header a:hover {
  color: #fff;
}

.button-primary {
  background-color: #3b82f6;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  font-weight: bold;
}

.button-primary:hover {
    background-color: #2563eb;
    color: white;
}

.hero-section {
  display: flex;
  align-items: center;
  justify-content: space-around;
  flex-grow: 1;
  padding: 2rem 4rem;
}

.hero-text {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  max-width: 50%;
}

.hero-section h1 {
  font-size: 5rem;
  font-weight: 800;
  max-width: 900px;
  line-height: 1.2;
  margin-bottom: 1.5rem;
}

.hero-section p {
  font-size: 1.5rem;
  color: #aaa;
  max-width: 700px;
  margin-bottom: 2.5rem;
}

.button-secondary {
  background-color: #3b82f6;
  color: white;
  padding: 1.25rem 2.5rem;
  border-radius: 5px;
  font-size: 1.25rem;
  font-weight: bold;
  text-decoration: none;
  transition: background-color 0.3s;
}

.button-secondary:hover {
  background-color: #2563eb;
}

.hero-logo-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.bouncing-logo {
  width: 800px;
  height: auto;
  border-radius: 50%;
  box-shadow: 0 0 35px rgba(0, 98, 255, 0.5), 0 0 60px rgba(0, 98, 255, 0.3);
  animation: bounce 1s infinite alternate ease-in-out;
}

@keyframes bounce {
  from {
    transform: translateY(0);
  }
  to {
    transform: translateY(-20px);
  }
}
</style>

