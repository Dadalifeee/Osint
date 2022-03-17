<template lang="">
  <div>
    <div v-if="dataEmail.length > 0">
      <p>Mail : {{dataEmail[0].Mail}}</p>
      <p>Account matches : {{dataEmail[1].Account_matches}}</p>
      <p>Accounts Name : {{dataEmail[2].Accounts_Name}}</p>
      <p>Last profile edit : {{dataEmail[3].Last_profile_edit}}</p>
      <p>Email : {{dataEmail[4].Email}}</p>
      <p>Gaia ID : {{dataEmail[5].Gaia_ID}}</p>
      <p>Hangouts Bot : {{dataEmail[6].Hangouts_Bot}}</p>
      <p>YouTube channel : {{dataEmail[7].YouTube_channel}}</p>
      <p>Google Calendar : {{dataEmail[8].Google_Calendar}}</p>

      <!-- <img :src="'../../../../backend/email/profile_pics/' + dataEmail[0].Mail"/> -->
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
  data() {
    return {
      previewData: [],
      tests: "{\"Mail\" :\"bouxoudeboux@gmail.com\"},{\"Account_matches\" : \"1\"},{\"Accounts_Name\" : \"Dada Lunardon\"},{\"Last_profile_edit\" : \"2022/03/05 18:11:55 (UTC)\"},{\"Email\" : \"bouxoudeboux@gmail.com\"}, {\"Gaia_ID\" : \"101314718496270372823\"},{\"Hangouts_Bot\" : \"No \"},{\"YouTube_channel\" : \"Not found\"},{\"Google Calendar\" : \"No public calendar\"}"
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