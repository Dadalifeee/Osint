<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-50 md-small-size-70 md-xsmall-size-100"
          >
            <h1 class="title">Rechercher par email</h1>
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
              <h2 class="title text-center">Email Search</h2>
              <h5 class="description">
                Chercher email
              </h5>
            </div>
          </div>
          <div id="domain">
            <div class="md-layout">
              <div class="md-layout-item md-size-66 mx-auto">
                <div class="form-group text-center">
                  <md-field>
                    <md-input v-model="inputEmail" placeholder="Email"></md-input>
                  </md-field>
                  <md-button class="md-raised md-success mt-3" v-on:click="sendEmail()"
                    >Search</md-button
                  >
                  <br>
                  <input type="radio" id="one" value="1" v-model="picked">
                  <label for="one">Chercher adresse google(gmail)</label>
                  <br>
                  <input type="radio" id="two" value="2" v-model="picked">
                  <label for="two">Autre</label>
                </div>
                
              </div>
            </div>
          </div>
          <TableVueEmail
            v-if="picked == 1"
            :dataEmail="dataEmailPreview"
          />
           <TableVueEmailHolehe
            v-if="picked == 2"
            :dataEmail="dataEmailHolehe"
          />
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import TableVueEmail from "./components/TableVueEmail";
import TableVueEmailHolehe from "./components/TableVueEmailHolehe";
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
    TableVueEmail,
    TableVueEmailHolehe
  },
  data() {
    return {
      name: null,
      email: null,
      message: null,
      inputEmail: null,
      dataEmail: null,
      dataEmailPreview: [],
      dataEmailHolehe: [],
      picked: 1
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
    sendEmail() {
      if(this.picked == 1) {
        axios
        .get(`http://127.0.0.1:5000/api/email/${this.inputEmail}`)
        .then((response) => {
          console.log(response.data);
          this.dataEmail = response.data
          const tests = this.dataEmail.split(',')
          for(let i in tests) {
            if(tests[i].length > 0) {
              console.log(tests[i]);
              this.dataEmailPreview.push(JSON.parse(tests[i]))
            }
          }
        })
        .catch((e) => {
          console.log(e);;
        });
      }else if(this.picked == 2) {
        axios
        .get(`http://127.0.0.1:5000/api/mail/${this.inputEmail}`)
        .then((response) => {
          console.log(response.data);
          this.dataEmailHolehe = response.data
        })
        .catch((e) => {
          console.log(e);;
        });
      }
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
