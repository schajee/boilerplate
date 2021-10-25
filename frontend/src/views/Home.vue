<template>
  <section>
    <h1>Tasks</h1>
    <ul v-if="tasks && tasks.count">
      <li v-for="(task, index) in tasks.results" :key="index">
        <span>{{ task.done ? '&check;' : '&cross;'}}</span>
        <a href="#" @click="onSelect(task)">{{ task.title }}</a>
      </li>
    </ul>
    <p v-else>No tasks</p>
    <form method="post" @submit.prevent="onSubmit">
      <p>
        <template v-if="selected">
          <input v-if="selected" type="text" name="title" v-model="selected.title" />
          <input type="checkbox" v-model="selected.done" />
        </template>
        <input v-else type="text" name="title" v-model="title" />
      </p>
      <p>
        <template v-if="selected">
          <button type="submit">Update</button>
          <button type="button" :disabled="selected.done" @click="onExecute">Execute</button>
          <button type="button" @click="onDelete">Delete</button>
        </template>
        <button v-else type="submit">Create</button>
      </p>
    </form>
    <pre v-if="error">{{ error }}</pre>
    <pre v-if="message">{{ message }}</pre>
  </section>
</template>

<script>
import Axios from 'axios'
export default {
  name: 'Home',
  data() {
    return {
      tasks: null,
      title: null,
      selected: null,
      error: null,
      message: null
    }
  },
  mounted() {
    if (!this.$store.state.user) {
      this.$router.push('/login')
    } else {
      this.getTasks()
    }
  },
  methods: {
    getTasks() {
      Axios.get(`/tasks/`).then(response => this.tasks = response.data )
    },
    onSubmit() {
      this.message = null
      if (this.selected) {
        Axios.patch(this.selected.url, { title: this.selected.title, done: false })
        .then(response => {
          this.selected = null
          this.message = response.data
          this.getTasks()
        })
        .catch(error => this.error = error.response.data)
      } else {
        Axios.post(`/tasks/`, { title: this.title, user: this.$store.state.user.url })
        .then(response => {
          this.title = null
          this.message = response.data
          this.getTasks()
        })
        .catch(error => this.error = error.response.data)
      }
    },
    onSelect(task) {
      this.message = null
      if (this.selected === task) {
        this.selected = null
      } else {
        this.selected = task
      }
    },
    onDelete() {
      Axios.delete(this.selected.url)
      .then(response => {
        this.selected = null
        this.message = response.data
        this.getTasks()
      })
      .catch(error => this.error = error.response.data)
    },
    onExecute() {
      Axios.post(`${this.selected.url}execute/`).then(response => {
        this.message = response.data
        this.selected = null
      })
      .catch(error => this.error = error.response.data)
    }
  }
}
</script>
