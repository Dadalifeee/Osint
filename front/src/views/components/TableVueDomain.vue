<template lang="">
  <div>
    <div v-if="dataTheHarvester !== false">
      <div @click="isOpenAsns = !isOpenAsns">
      <b>Donnée Asns</b>
      <collapse-transition>
        <div v-show="isOpenAsns">
          <md-table>
            <md-table-row>
              <md-table-head>asns</md-table-head>
            </md-table-row>
            
            <md-table-row v-for="(harvest, index) in dataTheHarvester.asns" :key="index">
              <md-table-cell>{{dataTheHarvester.asns[index]}}</md-table-cell>
            </md-table-row>
          </md-table>
        </div>
      </collapse-transition>
    </div>
    <hr>
    <div @click="isOpenUrl = !isOpenUrl">
      <b>Urls intéressantes</b>
      <collapse-transition>
        <div v-show="isOpenUrl">
          <md-table>
            <md-table-row>
              <md-table-head>Url</md-table-head>
            </md-table-row>
            
            <md-table-row v-for="(harvest, index) in dataTheHarvester.interesting_urls" :key="index">
              <md-table-cell>{{dataTheHarvester.interesting_urls[index]}}</md-table-cell>
            </md-table-row>
          </md-table>
        </div>
      </collapse-transition>
    </div>
    <hr>

    <div @click="isOpenIp = !isOpenIp">
      <b>Adresse Ip</b>
      <collapse-transition>
        <div v-show="isOpenIp">
          <md-table>
            <md-table-row>
              <md-table-head>IP</md-table-head>
            </md-table-row>
            
            <md-table-row v-for="(harvest, index) in dataTheHarvester.ips" :key="index">
              <md-table-cell>{{dataTheHarvester.ips[index]}}</md-table-cell>
            </md-table-row>
          </md-table>
        </div>
      </collapse-transition>
    </div>
    <hr>

    <div @click="isOpenLinkedin = !isOpenLinkedin">
      <b>Linkedin</b>
      <collapse-transition>
        <div v-show="isOpenLinkedin">
          <md-table>
            <md-table-row>
              <md-table-head>IP</md-table-head>
            </md-table-row>
            
            <md-table-row v-for="(harvest, index) in dataTheHarvester.linkedin_people" :key="index">
              <md-table-cell>{{dataTheHarvester.linkedin_people[index]}}</md-table-cell>
            </md-table-row>
          </md-table>
        </div>
      </collapse-transition>
    </div>
    <hr>

    <div @click="isOpenShodan = !isOpenShodan">
      <b>Shodan</b>
      <collapse-transition>
        <div v-show="isOpenShodan">
          <md-table>
            <md-table-row>
              <md-table-head>Shodan</md-table-head>
            </md-table-row>
            
            <md-table-row v-for="(harvest, index) in dataTheHarvester.shodan" :key="index">
              <md-table-cell>{{dataTheHarvester.shodan[index]}}</md-table-cell>
            </md-table-row>
          </md-table>
        </div>
      </collapse-transition>
    </div>
    <hr>

    <div @click="isOpenHost = !isOpenHost">
      <b>Hosts trouvés</b>
      <collapse-transition>
        <div v-show="isOpenHost">
          <md-table>
            <md-table-row>
              <md-table-head>Hosts</md-table-head>
            </md-table-row>
            
            <md-table-row v-for="(harvest, index) in dataTheHarvester.hosts" :key="index">
              <md-table-cell>{{dataTheHarvester.hosts[index]}}</md-table-cell>
            </md-table-row>
          </md-table>
        </div>
      </collapse-transition>
    </div>
  </div>
  <div v-else-if="dataTheHarvester === false">
    <p>Erreur veuillez réessayer</p>
  </div>
</div>
  
</template>
<script>
import { CollapseTransition } from "@ivanv/vue-collapse-transition";

export default {
  components: {
    CollapseTransition,
  },
  props: {
    dataTheHarvester: {
      type: Object,
    },
  },
  data() {
    return {
      previewData: null,
      isOpenAsns: false,
      isOpenUrl: false,
      isOpenHost: false,
      isOpenIp: false,
      isOpenLinkedin: false,
      isOpenShodan: false,
    };
  },
};
</script>
<style lang="">
</style>