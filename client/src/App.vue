<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <TodoList title="Todo List:"/>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'

export default {
  name: 'app',
  components: {
    TodoList
  }
}
</script>

<style>
</style>
