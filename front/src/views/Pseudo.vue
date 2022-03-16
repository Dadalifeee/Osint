<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-50 md-small-size-70 md-xsmall-size-100"
          >
            <h1 class="title">Rechercher par pseudo.</h1>
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
              <h2 class="title text-center">Pseudo Search</h2>
              <h5 class="description">
                Chercher pseudo
              </h5>
            </div>
          </div>
          <div id="domain">
            <div class="md-layout">
              <div class="md-layout-item md-size-66 mx-auto">
                <div class="form-group text-center">
                  <md-field>
              <md-input v-model="inputPseudo" placeholder="Pseudo"></md-input>
            </md-field>
            <md-button class="md-raised md-success mt-3" v-on:click="sendPseudo()"
              >Search</md-button
            >
                </div>
              </div>
            </div>
          </div>
          <TableVuePseudo
            :dataPseudo="dataPseudo"
          />
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import TableVuePseudo from "./components/TableVuePseudo";
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
    TableVuePseudo,
  },
  data() {
    return {
      name: null,
      pseudo: null,
      message: null,
      inputPseudo: null,
      dataPseudo: null,
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
    sendPseudo() {
      axios
        .get(`http://127.0.0.1:5000/api/pseudo/${this.inputPseudo}`)
        .then((response) => {
          console.log(response.data);
          this.dataPseudo = response.data.replace(/[[+]]/g, "<br>")
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
