<template>
    <div class="todo-item-container">
      <li @click="toggleTodo" v-bind:class="{ 'done-todo': todo.done }">{{todo.item}}</li>
      <button @click="deleteTodo">X</button>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'TodoItem',
  props: ['todo', 'getAllTodos'],

  methods: {
    toggleTodo() {
      axios.patch('/todo', {id: this.todo.id})
        .then(() => this.getAllTodos())
    },
    deleteTodo() {
      axios.delete('/todo/' + this.todo.id)
        .then(() => this.getAllTodos())
    }
  }
}
</script>

<style>
.done-todo {
  text-decoration: line-through;
}

.todo-item-container {
  display: flex;
}
</style>