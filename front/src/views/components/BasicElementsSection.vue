<template>
  <div class="wrapper">
    <div id="domain">
      <div class="title">
        <h4>Domain Search</h4>
			  <p>Chercher des adresses ip des mails des noms de personnes de l'entreprise depuis un nom de domaine</p>
      </div>
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
    <div id="email">
      <div class="title">
        <h4>Email Search</h4>
			  <p>Chercher des informations depuis un mail sur l'organisation photo de profil etc...</p>
      </div>
      <div class="md-layout">
        <div class="md-layout-item md-size-66 mx-auto">
          <div class="form-group text-center">
            <md-field>
              <md-input v-model="inputEmail" placeholder="Email"></md-input>
            </md-field>
            <md-button class="md-raised md-success mt-3" v-on:click="sendEmail()"
              >Search</md-button
            >
          </div>
        </div>
      </div>
      
    </div>
    <div id="Pseudo">
      <div class="title">
        <h4>Pseudo Search</h4>
			  <p>Chercher des informations depuis un pseudo savoir sur quel site le pseudo est renseigné</p>
      </div>
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
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      inputDomaine: null,
      inputPseudo:null,
      inputEmail:null
    };
  },
  methods: {
    sendDomain() {
      axios
        .get(`http://127.0.0.1:5000/api/domain/${this.inputDomaine}`)
        .then((response) => {
          // JSON responses are automatically parsed.
          console.log(response.data);;
        })
        .catch((e) => {
          console.log(e);;
        });
    },
    sendEmail() {
      axios
        .get(`http://127.0.0.1:5000/api/domain/${this.inputEmail}`)
        .then((response) => {
          // JSON responses are automatically parsed.
          console.log(response.data);;
        })
        .catch((e) => {
          console.log(e);;
        });
    },
    sendPseudo() {
      axios
        .get(`http://127.0.0.1:5000/api/domain/${this.inputPseudo}`)
        .then((response) => {
          // JSON responses are automatically parsed.
          console.log(response.data);;
        })
        .catch((e) => {
          console.log(e);;
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.vertical-center {
  display: flex;
  align-items: center;
}
.flex-column {
  display: flex;
  flex-direction: column;
}
.md-checkbox,
.md-radio {
  display: flex;
  margin: 0;
  margin-bottom: 0.5rem;
}
</style>
