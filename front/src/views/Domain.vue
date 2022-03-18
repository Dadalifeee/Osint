<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-50 md-small-size-70 md-xsmall-size-100"
          >
            <h1 class="title">Rechercher par nom de domaine</h1>
            
          </div>
        </div>
      </div>
    </parallax>
    <div class="main main-raised">
      <div class="section">
        <div class="container">
          <div class="md-layout">
            <div
              class="md-layout-item md-size-66 md-xsmall-size-100 mx-auto text-center"
            >
              <h2 class="title text-center">Domain Search</h2>
              <h5 class="description">
                Chercher des informations depuis une nom de domaine
              </h5>
            </div>
          </div>
          <div id="domain">
            <div class="md-layout">
              <div class="md-layout-item md-size-66 mx-auto">
                <div class="form-group text-center">
                  <md-field>
                    <md-input v-model="inputDomaine" placeholder="Domaine"></md-input>
                  </md-field>
                  <md-button :disabled="!validateInput()" class="md-raised md-success mt-3" v-on:click="sendDomain()"
                    >Search</md-button
                  >
                </div>
              </div>
            </div>
          </div>
          <TableVueDomain
            v-if="dataTheHarvester !== null"
            :dataTheHarvester="dataTheHarvester"
          />
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import TableVueDomain from "./components/TableVueDomain";
import axios from "axios";

export default {
  bodyClass: "landing-page",
  props: {
    header: {
      type: String,
      default: require("@/assets/img/fond.jpg")
    },
    teamImg1: {
      type: String,
      default: require("@/assets/img/faces/avatar.jpg")
    },
    teamImg2: {
      type: String,
      default: require("@/assets/img/faces/christian.jpg")
    },
    teamImg3: {
      type: String,
      default: require("@/assets/img/faces/kendall.jpg")
    }
  },
   components: {
    TableVueDomain,
  },
  
  data() {
    return {
      name: null,
      email: null,
      message: null,
      inputDomaine: null,
      dataTheHarvester: null,
    };
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
    }
  },
  created() {
  axios.interceptors.request.use((config) => {
      // trigger 'loading=true' event here
      return config;
    }, (error) => {
      // trigger 'loading=false' event here
      return Promise.reject(error);
    });

    axios.interceptors.response.use((response) => {
      // trigger 'loading=false' event here
      return response;
    }, (error) => {
      // trigger 'loading=false' event here
      return Promise.reject(error);
    })
  },
  watch:{
    inputDomaine() {
      this.validateInput(this.inputDomaine);
    }
  },
  methods: {
    sendDomain() {
      axios
        .get(`http://127.0.0.1:5000/api/domain/${this.inputDomaine}`)
        .then((response) => {
          // JSON responses are automatically parsed.
          console.log(response.data);
          this.dataTheHarvester = response.data

        })
        .catch((e) => {
          console.log(e);;
        });
    },
    validateInput(input){
      var regex = new RegExp('^(http(s)?://)?[a-zA-Z0-9]+.((fr)|(com))$') ;
      var test = regex.test(input);
      console.log("test : " + test)
      return test;
    }
  }
};
</script>

<style lang="scss" scoped>
.md-card-actions.text-center {
  display: flex;
  justify-content: center !important;
}
.contact-form {
  margin-top: 30px;
}

.md-has-textarea + .md-layout {
  margin-top: 15px;
}
</style>
