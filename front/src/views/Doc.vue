<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-50 md-small-size-70 md-xsmall-size-100"
          >
            <h1 class="title">Documentation</h1>
          </div>
        </div>
      </div>
    </parallax>
    <div class="main main-raised">
      <div class="section">
        <div class="container">
          <div class="md-layout">
            <h2 class="title text-center">Domaine</h2>
              <h5 class="description">
                La recherche par nom de domaine permet d’obtenir des informations à partir d’un nom de domaine. Il suffit de le taper dans la barre de recherche et les résultats s’afficheront directement au dessous.
              </h5>
          </div>
           <div class="md-layout">
            <h2 class="title text-center">Email</h2>
              <h5 class="description">
                La recherche par adresse mail permet d’obtenir des informations à partir d’un email. Il suffit de le taper dans la barre de recherche et les résultats s’afficheront directement au dessous. Deux options sont disponibles : la recherche d’adresse mail Google et la recherche pour tous les autres types d’adresse.
              </h5>
          </div>
           <div class="md-layout">
            <h2 class="title text-center">Pseudo</h2>
              <h5 class="description">
                La recherche par pseudo permet d’obtenir des informations à partir d’un pseudo. Il suffit de le taper dans la barre de recherche et les résultats s’afficheront directement au dessous. Ils seront composés d’une liste de sites sur lesquels il y a un utilisateur qui se sert du pseudo en question.
              </h5>
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
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
