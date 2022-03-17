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
                </div>
              </div>
            </div>
          </div>
          <TableVueEmail
            :dataEmail="dataEmailPreview"
          />
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import TableVueEmail from "./components/TableVueEmail";
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
  },
  data() {
    return {
      name: null,
      email: null,
      message: null,
      inputEmail: null,
      dataEmail: null,
      dataEmailPreview: [],
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
