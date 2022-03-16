<template lang="">
  <div>
  <md-table>
      <md-table-row>
        <md-table-head>asns</md-table-head>
        <md-table-head>emails</md-table-head>
        <md-table-head>hosts</md-table-head>
        <md-table-head>interesting_urls</md-table-head>
        <md-table-head>ips</md-table-head>
        <md-table-head>linkedin_people</md-table-head>
        <md-table-head>shodan</md-table-head>
        <md-table-head>trello_urls</md-table-head>
        <md-table-head>twitter_people</md-table-head>
      </md-table-row>
      
      <md-table-row v-for="(harvest, index) in dataTheHarvester.asns" :key="index">
        <md-table-cell>{{dataTheHarvester.asns[index]}}</md-table-cell>
        <md-table-cell>{{dataTheHarvester.emails[index]}}</md-table-cell>
        <md-table-cell>{{dataTheHarvester.hosts[index]}}</md-table-cell>
        <md-table-cell>{{dataTheHarvester.interesting_urls[index]}}</md-table-cell>
        <md-table-cell>{{dataTheHarvester.ips[index]}}</md-table-cell>
        <md-table-cell>{{dataTheHarvester.linkedin_people[index]}}</md-table-cell>
        <md-table-cell>{{dataTheHarvester.shodan[index]}}</md-table-cell>
        <md-table-cell>{{dataTheHarvester.trello_urls[index]}}</md-table-cell>
        <md-table-cell>{{dataTheHarvester.twitter_people[index]}}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>
<script>
export default {
  props: {
    dataTheHarvester: {
      type: Object,
    },
  },
  data() {
    return {
      previewData: null
    }
  }
};
</script>
<style lang="">
</style>