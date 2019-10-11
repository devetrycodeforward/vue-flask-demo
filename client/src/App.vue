<template>
  <div id="app">
    <div>
      <button @click="handleNavClick">{{buttonText}}</button>
    </div>
    <NewComponent v-if="!showTodoList" />
    <img v-if="showTodoList" alt="Vue logo" src="./assets/logo.png">
    <TodoList v-if="showTodoList" title="Todo List:"/>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue';
import NewComponent from './components/NewComponent.vue';

export default {
  name: 'app',
  components: {
    TodoList,
    NewComponent
  },
  data() {
    return {
      showTodoList: false,
      buttonText: 'Show Todo List'
    }
  },
  methods: {
    handleNavClick() {
      this.showTodoList = !this.showTodoList;
      if (this.buttonText ===  'Show Todo List') {
        this.buttonText = 'Show Welcome Screen'
      } else {
        this.buttonText =  'Show Todo List'
      }
    }
  }
}
</script>

<style>
</style>
