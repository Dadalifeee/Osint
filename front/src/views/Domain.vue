<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-50 md-small-size-70 md-xsmall-size-100"
          >
            <h1 class="title">Rechercher par nom de domaine.</h1>
            <h4>
              Every landing page needs a small description after the big bold
              title, that's why we added this text here. Add here all the
              information that can make you or your product create the first
              impression.
            </h4>
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
                Chercher des adresses ip des mails des noms de personnes de l'entreprise depuis un nom de domaine
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
                  <md-button class="md-raised md-success mt-3" v-on:click="sendDomain()"
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
      default: require("@/assets/img/bg7.jpg")
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
