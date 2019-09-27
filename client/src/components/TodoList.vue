<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <ul>
      <li v-bind:class="{ 'done-todo': todo.done }" v-for="todo in todos" v-bind:key="todo.id" @click="toggleTodo(todo.id)"> {{ todo.item }}</li>
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
      todos: [],
      inputValue: ''
    }
  },
  methods: {
    getAllTodos() {
      axios.get('/todos').then( res => this.todos = res.data.items);
    },
    handleAddTodoClick() {
      axios.post('/todo', { item: this.inputValue } )
        .then(() => this.getAllTodos());
      this.inputValue = '';
    },
    toggleTodo(id) {
      axios.patch('/todo', {id: id})
      .then(() => this.getAllTodos())
    }
  },
  mounted() {
    this.getAllTodos();
  }
}
</script>
<style >

.done-todo {
  text-decoration: line-through;
}
</style>
