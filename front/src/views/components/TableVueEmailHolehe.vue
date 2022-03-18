<template lang="">
  <div>
    <div v-if="dataEmail.length > 0">
      {{dataEmail}}
    </div>
    
  </div>
  
</template>
<script>
export default {
  props: {
    dataEmail: {
      type: Array,
    },
  },
};
</script>
<style lang="">
</style>