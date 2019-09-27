<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="todo in todos"> {{ todo.item }}</li>
    </ul>
    <input v-model="inputValue"/>
    <button @click="handleAddTodoClick">Add New Todo</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TodoList',
  props: ['title'],
  data() {
    return {
      todos: ['a', 'b', 'c'],
      inputValue: ''
    }
  },
  methods: {
    handleAddTodoClick() {
      axios.post('/todo', { item: this.inputValue } )
        .then(() => {
          axios.get('/todos').then( res => this.todos = res.data.items);
        })
      this.inputValue = '';
    }
  },
  mounted() {
    axios.get('/todos').then( res => this.todos = res.data.items);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
