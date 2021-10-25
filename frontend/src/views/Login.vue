<template>
  <section>
    <h1>Login</h1>
    <form method="post" @submit.prevent="onSubmit">
      <p><input type="text" name="username" v-model="username" /></p>
      <p><input type="password" name="password" v-model="password" /></p>
      <p><button type="submit">Login</button></p>
    </form>
    <pre v-if="error">{{ error }}</pre>
  </section>
</template>
<script>
import Axios from 'axios'
export default {
  name: "Login",
  data() {
    return {
      username: null,
      password: null,
      error: null,
      tokens: null,
    }
  },
  methods: {
    onSubmit() {
      Axios.post(`/token/`, { 
        username: this.username, 
        password: this.password
      }).then(response => {
        this.tokens = response.data
        Axios.get(`/users/current/`, {
          headers: { Authorization: `Bearer ${this.tokens.access}` }
        }).then(response => {
          this.$store.commit('login', {
            access: this.tokens.access,
            refresh: this.tokens.refresh,
            user: response.data,
          })
          this.$router.push('/')
        })
      }).catch(error => this.error = error.response.data )
    }
  }
}
</script>