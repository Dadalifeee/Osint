<template lang="">
  <div>
    <h4>Donnée Email</h4>
    <p>{{test}}</p>
    
  </div>
  
</template>
<script>
export default {
  props: {
    dataEmail: {
      type: Object,
    },
  },
  data() {
    return {
      previewData: null,
      test: JSON.parse("{\"Mail\" :\"bouxoudeboux@gmail.com\"},{\"Account matches\" : \"1\"},{\"Accounts Name\" : \"Dada Lunardon\"},{\"Last profile edit\" : \"2022/03/05 18:11:55 (UTC)\"},{\"Email\" : \"bouxoudeboux@gmail.com\", \"Gaia ID\" : \"101314718496270372823\"},{{\"Hangouts Bot\" : \"No \"}},{\"YouTube channel\" : \"Not found\"},{\"Google Calendar\" : \"No public calendar\"}")
    };
  },
};
</script>
<style lang="">
</style>