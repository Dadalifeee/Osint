<template lang="">
  <div>
    <table class="table table-striped table-bordered table-dark">
      <thead>
        <tr>
          <th>asns</th>
          <th>emails</th>
          <th>hosts</th>
          <th>interesting_urls</th>
          <th>ips</th>
          <th>linkedin_people</th>
          <th>shodan</th>
          <th>trello_urls</th>
          <th>twitter_people</th>
        </tr>
      </thead>
      <tbody>
          <tr v-for="(harvest, index) in dataTheHarvester.asns" :key="index">
              <td>{{dataTheHarvester.asns[index]}}</td>
              <td>{{dataTheHarvester.emails[index]}}</td>
              <td>{{dataTheHarvester.hosts[index]}}</td>
              <td>{{dataTheHarvester.interesting_urls[index]}}</td>
              <td>{{dataTheHarvester.ips[index]}}</td>
              <td>{{dataTheHarvester.linkedin_people[index]}}</td>
              <td>{{dataTheHarvester.shodan[index]}}</td>
              <td>{{dataTheHarvester.trello_urls[index]}}</td>
              <td>{{dataTheHarvester.twitter_people[index]}}</td>
          </tr>
      </tbody>
  </table>
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
      
      <md-table-row>
        <md-table-cell md-numeric>3</md-table-cell>
        <md-table-cell>Vera Taleworth</md-table-cell>
        <md-table-cell>vtaleworth2@google.ca</md-table-cell>
        <md-table-cell>Male</md-table-cell>
        <md-table-cell>Community Outreach Specialist</md-table-cell>
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