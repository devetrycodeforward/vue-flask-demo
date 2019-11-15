<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <ul>
      <TodoItem v-for="todo in todos" :key="todo.id" :todo="todo" :getAllTodos="getAllTodos" />
    </ul>
    <input v-model="inputValue"/>
    <button @click="handleAddTodoClick">Add New Todo</button>
  </div>
</template>

<script>
import axios from 'axios';
import TodoItem from './TodoItem.vue';

export default {
  name: 'TodoList',
  props: ['title'],
  components: {
    TodoItem
  },
  data() {
    return {
      todos: ['apple'],
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
