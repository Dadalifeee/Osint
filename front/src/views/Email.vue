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
              <h2 class="title text-center">Recherche par mail</h2>
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
                  <p v-if="erreur === true" class="text-danger">Le format du mail n'est pas bon essayez sous la forme(exemple@gmail.com)</p>
                  <input type="radio" id="one" value="1" v-model="picked">
                  <label for="one">Chercher adresse google(gmail)</label>
                  <br>
                  <input type="radio" id="two" value="2" v-model="picked">
                  <label for="two">Autre</label>
                  <br>
                  <a href="javascript:window.print()">
                    <md-button v-if="dataEmailPreview.length > 0 " class="md-raised md-success mt-3"
                    >Imprimer</md-button
                  >
                  </a>
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
      picked: 1,
      erreur: false,
      testmail:"Twitter : @palenath\nGithub : https://github.com/megadose/holehe\nFor BTC Donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ\n\u001b[H\u001b[J\n*************************\n   mathias@lunardon.fr\n*************************\n\u001b[31m[x] about.me\u001b[0m\n\u001b[35m[-] adobe.com\u001b[0m\n\u001b[35m[-] amazon.com\u001b[0m\n\u001b[35m[-] amocrm.com\u001b[0m\n\u001b[35m[-] any.do\u001b[0m\n\u001b[35m[-] archive.org\u001b[0m\n\u001b[35m[-] armurerie-auxerre.com\u001b[0m\n\u001b[31m[x] atlassian.com\u001b[0m\n\u001b[31m[x] axonaut.com\u001b[0m\n\u001b[31m[x] babeshows.co.uk\u001b[0m\n\u001b[31m[x] badeggsonline.com\u001b[0m\n\u001b[31m[x] bios-mods.com\u001b[0m\n\u001b[31m[x] biotechnologyforums.com\u001b[0m\n\u001b[31m[x] bitmoji.com\u001b[0m\n\u001b[31m[x] blablacar.com\u001b[0m\n\u001b[31m[x] blackworldforum.com\u001b[0m\n\u001b[31m[x] blip.fm\u001b[0m\n\u001b[31m[x] forum.blitzortung.org\u001b[0m\n\u001b[31m[x] bluegrassrivals.com\u001b[0m\n\u001b[35m[-] bodybuilding.com\u001b[0m\n\u001b[31m[x] buymeacoffee.com\u001b[0m\n\u001b[31m[x] discussion.cambridge-mt.com\u001b[0m\n\u001b[35m[-] caringbridge.org\u001b[0m\n\u001b[31m[x] chinaphonearena.com\u001b[0m\n\u001b[31m[x] clashfarmer.com\u001b[0m\n\u001b[31m[x] codecademy.com\u001b[0m\n\u001b[31m[x] forum.codeigniter.com\u001b[0m\n\u001b[31m[x] codepen.io\u001b[0m\n\u001b[35m[-] coroflot.com\u001b[0m\n\u001b[31m[x] cpaelites.com\u001b[0m\n\u001b[31m[x] cpahero.com\u001b[0m\n\u001b[31m[x] cracked.to\u001b[0m\n\u001b[31m[x] crevado.com\u001b[0m\n\u001b[35m[-] deliveroo.com\u001b[0m\n\u001b[31m[x] demonforums.net\u001b[0m\n\u001b[35m[-] devrant.com\u001b[0m\n\u001b[35m[-] diigo.com\u001b[0m\n\u001b[35m[-] discord.com\u001b[0m\n\u001b[35m[-] docker.com\u001b[0m\n\u001b[31m[x] dominos.fr\u001b[0m\n\u001b[31m[x] ebay.com\u001b[0m\n\u001b[35m[-] ello.co\u001b[0m\n\u001b[35m[-] envato.com\u001b[0m\n\u001b[35m[-] eventbrite.com\u001b[0m\n\u001b[35m[-] evernote.com\u001b[0m\n\u001b[35m[-] fanpop.com\u001b[0m\n\u001b[35m[-] firefox.com\u001b[0m\n\u001b[35m[-] flickr.com\u001b[0m\n\u001b[35m[-] freelancer.com\u001b[0m\n\u001b[31m[x] drachenhort.user.stunet.tu-freiberg.de\u001b[0m\n\u001b[35m[-] garmin.com\u001b[0m\n\u001b[32m[+] github.com\u001b[0m\n\u001b[31m[x] google.com\u001b[0m\n\u001b[35m[-] en.gravatar.com\u001b[0m\n\u001b[35m[-] hubspot.com\u001b[0m\n\u001b[35m[-] imgur.com\u001b[0m\n\u001b[35m[-] insightly.com\u001b[0m\n\u001b[35m[-] instagram.com\u001b[0m\n\u001b[35m[-] issuu.com\u001b[0m\n\u001b[31m[x] forum.kodi.tv\u001b[0m\n\u001b[35m[-] komoot.com\u001b[0m\n\u001b[35m[-] laposte.fr\u001b[0m\n\u001b[35m[-] last.fm\u001b[0m\n\u001b[35m[-] lastpass.com\u001b[0m\n\u001b[35m[-] mail.ru\u001b[0m\n\u001b[31m[x] community.mybb.com\u001b[0m\n\u001b[31m[x] myspace.com\u001b[0m\n\u001b[31m[x] nattyornotforum.nattyornot.com\u001b[0m\n\u001b[35m[-] naturabuy.fr\u001b[0m\n\u001b[31m[x] forum.ndemiccreations.com\u001b[0m\n\u001b[31m[x] forums.nextpvr.com\u001b[0m\n\u001b[35m[-] nike.com\u001b[0m\n\u001b[35m[-] nimble.com\u001b[0m\n\u001b[35m[-] nocrm.io\u001b[0m\n\u001b[31m[x] nutshell.com\u001b[0m\n\u001b[31m[x] forum.odampublishing.com\u001b[0m\n\u001b[31m[x] office365.com\u001b[0m\n\u001b[31m[x] onlinesequencer.net\u001b[0m\n\u001b[31m[x] parler.com\u001b[0m\n\u001b[31m[x] patreon.com\u001b[0m\n\u001b[35m[-] pinterest.com\u001b[0m\n\u001b[35m[-] pipedrive.com\u001b[0m\n\u001b[35m[-] plurk.com\u001b[0m\n\u001b[31m[x] pornhub.com\u001b[0m\n\u001b[35m[-] protonmail.ch\u001b[0m\n\u001b[35m[-] quora.com\u001b[0m\n\u001b[31m[x] raidforums.com\u001b[0m\n\u001b[35m[-] rambler.ru\u001b[0m\n\u001b[31m[x] redtube.com\u001b[0m\n\u001b[35m[-] replit.com\u001b[0m\n\u001b[35m[-] rocketreach.co\u001b[0m\n\u001b[35m[-] samsung.com\u001b[0m\n\u001b[35m[-] seoclerks.com\u001b[0m\n\u001b[35m[-] 7cups.com\u001b[0m\n\u001b[31m[x] smule.com\u001b[0m\n\u001b[31m[x] snapchat.com\u001b[0m\n\u001b[31m[x] soundcloud.com\u001b[0m\n\u001b[35m[-] sporcle.com\u001b[0m\n\u001b[35m[-] spotify.com\u001b[0m\n\u001b[35m[-] strava.com\u001b[0m\n\u001b[35m[-] taringa.net\u001b[0m\n\u001b[35m[-] teamleader.eu\u001b[0m\n\u001b[35m[-] teamtreehouse.com\u001b[0m\n\u001b[35m[-] tellonym.me\u001b[0m\n\u001b[31m[x] thecardboard.org\u001b[0m\n\u001b[31m[x] forums.therian-guide.com\u001b[0m\n\u001b[31m[x] thevapingforum.com\u001b[0m\n\u001b[31m[x] forum.treasureclassifieds.com\u001b[0m\n\u001b[35m[-] tumblr.com\u001b[0m\n\u001b[35m[-] tunefind.com\u001b[0m\n\u001b[35m[-] twitter.com\u001b[0m\n\u001b[31m[x] venmo.com\u001b[0m\n\u001b[35m[-] vivino.com\u001b[0m\n\u001b[35m[-] voxmedia.com\u001b[0m\n\u001b[35m[-] vrbo.com\u001b[0m\n\u001b[35m[-] vsco.co\u001b[0m\n\u001b[35m[-] wattpad.com\u001b[0m\n\u001b[35m[-] wordpress.com\u001b[0m\n\u001b[35m[-] xing.com\u001b[0m\n\u001b[31m[x] xnxx.com\u001b[0m\n\u001b[31m[x] xvideos.com\u001b[0m\n\u001b[31m[x] yahoo.com\u001b[0m\n\u001b[35m[-] zoho.com\u001b[0m\n\n\u001b[32m[+] Email used\u001b[0m,\u001b[35m [-] Email not used\u001b[0m,\u001b[31m [x] Rate limit\u001b[0m\n124 websites checked in 10.07 seconds\nTwitter : @palenath\nGithub : https://github.com/megadose/holehe\nFor BTC Donations : 1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ\n"
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
          this.erreur = false
        })
        .catch((e) => {
          console.log(e);;
          this.erreur = true

        });
      }else if(this.picked == 2) {
        axios
        .get(`http://127.0.0.1:5000/api/mail/${this.inputEmail}`)
        .then((response) => {
          console.log(response.data);
          this.dataEmailHolehe = response.data.split('[0m\n\u001b')
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
