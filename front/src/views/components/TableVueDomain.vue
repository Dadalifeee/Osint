<template lang="">
  <div>
    <h4>Donnée Asns</h4>
    <md-table>
      <md-table-row>
        <md-table-head>asns</md-table-head>
      </md-table-row>
      
      <md-table-row v-for="(harvest, index) in dataTheHarvester.asns" :key="index">
        <md-table-cell>{{dataTheHarvester.asns[index]}}</md-table-cell>
      </md-table-row>
    </md-table>
    <h4>Urls intéressantes</h4>
    <md-table>
      <md-table-row>
        <md-table-head>interesting_urls</md-table-head>
      </md-table-row>
      <md-table-row v-for="(harvest, index) in dataTheHarvester.interesting_urls" :key="index">
        <md-table-cell>{{dataTheHarvester.interesting_urls[index]}}</md-table-cell>
      </md-table-row>
    </md-table>

    <h4>ip</h4>
    <md-table>
      <md-table-row>
        <md-table-head>ip</md-table-head>
      </md-table-row>
      <md-table-row v-for="(harvest, index) in dataTheHarvester.ips" :key="index">
        <md-table-cell>{{dataTheHarvester.ips[index]}}</md-table-cell>
      </md-table-row>
    </md-table>
    <h4>linkedin_people</h4>
    <md-table>
      <md-table-row>
        <md-table-head>linkedin_people</md-table-head>
      </md-table-row>
      
      <md-table-row v-for="(harvest, index) in dataTheHarvester.linkedin_people" :key="index">
        <md-table-cell>{{dataTheHarvester.linkedin_people[index]}}</md-table-cell>
      </md-table-row>
    </md-table>
    <h4>shodan</h4>
    <md-table>
      <md-table-row>
        <md-table-head>shodan</md-table-head>
      </md-table-row>
      
      <md-table-row v-for="(harvest, index) in dataTheHarvester.shodan" :key="index">
        <md-table-cell>{{dataTheHarvester.shodan[index]}}</md-table-cell>
      </md-table-row>
      <md-table-row v-for="(harvest, index) in dataTheHarvester.asns" :key="index">
        <md-table-cell>{{dataTheHarvester.asns[index]}}</md-table-cell>
      </md-table-row>
    </md-table>
    <h4>Donnée hosts</h4>
    <md-table>
      <md-table-row v-for="(harvest, index) in dataTheHarvester.hosts" :key="index">
        <md-table-cell>{{dataTheHarvester.hosts[index]}}</md-table-cell>
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
      previewData: null,
    };
  },
};
</script>
<style lang="">
</style>