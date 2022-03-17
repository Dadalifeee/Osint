<template lang="">
  <div>
    <div v-if="dataEmail.length > 0">
      <div v-for="(item, index) in dataEmail" :key="index">
        {{Object.keys(item)[0]}} : {{Object.values(item)[0]}}
      </div>
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