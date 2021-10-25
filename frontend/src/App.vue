<template>
  <div id="app" :key="$store.state.key">
    <div id="nav">
      <a href="#" v-if="$store.state.user" @click="logout">Logout</a>
    </div>
    <router-view/>
    <pre>{{ $store.state.socket.isConnected ? 'Online' : 'Offline' }}</pre>
  </div>
</template>
<script>
export default {
  name: "Page",
  methods: {
    logout() {
      this.$store.commit('logout')
      this.$router.push('/login')
    }
  }
}
</script>