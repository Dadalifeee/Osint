<template lang="">
  <div>
    <md-button class="md-raised md-success mt-3" v-on:click="test()"
      >test</md-button
    >
    <h4>Donnée Email</h4>
    
    {{tests}}
    {{previewData}}
  </div>
  
</template>
<script>
export default {
  props: {
    dataEmail: {
      type: String,
    },
  },
  data() {
    return {
      previewData: [],
      tests: "{\"Mail\" :\"serialzdada26@gmail.com\"},{\"Account matches\" : \"1\"},{\"Accounts Name\" : \"Mathias DaDa\"},{\"Last profile edit\" : \"2022/03/05 18:11:55 (UTC)\"},{\"Email\" : \"serialzdada26@gmail.com\"}, {\"Gaia ID\" : \"101769243515293799329\"},{\"Hangouts Bot\" : \"No \"},{\"Youtube channel\" : \"Not found\"},{\"Google Calendar\" : \"No public calendar\"}"
    };
  },
  methods: {
    test() {
      this.tests = this.tests.split(',')
      console.log(this.tests);
      for(let i in this.tests) {
       this.previewData.push(JSON.parse(this.tests[i]))
      }
      console.log(this.previewData);
    }
  }
};
</script>
<style lang="">
</style>