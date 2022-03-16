<template lang="">
  <div>
    <span v-html="dataPseudo"></span>
  </div>
  
</template>
<script>
export default {
  props: {
    dataPseudo: {
      type: String,
    },
  },
};
</script>
<style lang="">
</style>