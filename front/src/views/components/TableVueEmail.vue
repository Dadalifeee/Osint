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
};
</script>
<style lang="">
</style>