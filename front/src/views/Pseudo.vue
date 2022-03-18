<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-50 md-small-size-70 md-xsmall-size-100"
          >
            <h1 class="title">Rechercher par pseudo</h1>
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
              <h2 class="title text-center">Recherche par pseudo</h2>
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
            <p v-if="erreur === true" class="text-danger">Le format du pseudo n'est pas bon , caractère speciaux interdit</p>

            <br>
            <a href="javascript:window.print()">
              <md-button v-if="dataPseudo !== null" class="md-raised md-success mt-3"
              >Imprimer</md-button
            >
            </a>
           
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
    TableVuePseudo,
  },
  data() {
    return {
      name: null,
      pseudo: null,
      message: null,
      inputPseudo: null,
      dataPseudo: null,
      erreur: false,
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
          this.dataPseudo = this.dataPseudo.replace('[', '')
          this.erreur = false

        })
        .catch((e) => {
          console.log(e);;
          this.erreur = true

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
