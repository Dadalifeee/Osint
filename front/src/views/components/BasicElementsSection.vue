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
    <TableVueDomain
      :dataTheHarvester="test"
    />
  </div>
</template>

<script>
import axios from "axios";
import TableVueDomain from "./TableVueDomain";

export default {
  components: {
    TableVueDomain
  },
  data() {
    return {
      inputDomaine: null,
      inputPseudo:null,
      inputEmail:null,
      selected: {},
      dataTheHarvester: null,
      dataSherlock: null,
      test:{
    "asns": [
        "AS15133",
        "AS15169"
    ],
    "emails": [
        "edeltraud.fleck@jeu.fr",
        "grace.heidenreich@jeu.fr",
        "mihaela.gebert@jeu.fr",
        "rumold.stork@jeu.fr",
        "swidger.zimmermann@jeu.fr"
    ],
    "hosts": [
        "cdn.jeu.fr:35.186.238.173",
        "cdn.prod.jeu.fr",
        "cdn.prod.jeu.fr:35.186.238.173",
        "cdn.test.jeu.fr:205.185.216.10, 205.185.216.42",
        "cdn.test.jeu.fr:cds.y8i3s4x8.hwcdn.net",
        "cdn.test.jeu.fr:di-9eduq5yy.vo.lswcdn.net.",
        "cdn.test.jeu.fr:di-9eduq5yy.vo.lswcdn.net",
        "clubmarian.jeu.fr:35.186.238.173",
        "clubpenguin.jeu.fr:35.186.238.173",
        "damoria.jeu.fr:35.186.238.173",
        "darkorbit.jeu.fr:35.186.238.173",
        "deepolis.jeu.fr:35.186.238.173",
        "dev.jeu.fr:35.186.238.173",
        "divein.jeu.fr:35.186.238.173",
        "drakensang-online.jeu.fr:35.186.238.173",
        "dyn.jeu.fr:35.186.238.173",
        "email.jeu.fr",
        "fantasyrama.jeu.fr:35.186.238.173",
        "farmerama.jeu.fr:35.186.238.173",
        "fdj.jeu.fr:35.186.238.173",
        "flylikeabird2.jeu.fr:35.186.238.173",
        "hockeymanager.jeu.fr:35.186.238.173",
        "imap.jeu.fr:35.186.238.173",
        "king.jeu.fr:35.186.238.173",
        "lavachequirit.jeu.fr:35.186.238.173",
        "lb.jeu.fr.",
        "letrangepouvoirdenorman.jeu.fr:35.186.238.173",
        "login.jeu.fr:35.186.238.173",
        "losetheheat.jeu.fr:35.186.238.173",
        "m.jeu.fr:www.lb.jeu.fr",
        "m.jeu.fr:34.95.108.35",
        "m.jeu.fr:o.www.jeu.fr",
        "m.jeu.fr:o.www.jeu.fr.",
        "mafia1930.jeu.fr:35.186.238.173",
        "mail2.amazon.jeu.fr:35.186.238.173",
        "managerzone.jeu.fr:91.123.205.100",
        "moonbase.jeu.fr:35.186.238.173",
        "multijoueur.jeu.fr:35.186.238.173",
        "mylittlefarmies.jeu.fr:35.186.238.173",
        "o.jeu.fr.:35.186.238.173",
        "o.www.jeu.fr:www.lb.jeu.fr.",
        "o.www.jeu.fr:34.95.108.35",
        "o.www.jeu.fr:www.lb.jeu.fr",
        "panfu.jeu.fr:35.186.238.173",
        "piratestorm.jeu.fr:35.186.238.173",
        "powersoccer.jeu.fr:35.186.238.173",
        "prv.jeu.fr:35.186.238.173",
        "risingcities.jeu.fr:35.186.238.173",
        "seafight.jeu.fr:35.186.238.173",
        "service.jeu.fr",
        "skyrama.jeu.fr:35.186.238.173",
        "soccermanager.jeu.fr:35.186.238.173",
        "static.jeu.fr:di-7i6hmqsq.vo.lswcdn.net.",
        "static.jeu.fr:cl-2d703670.gcdn.co",
        "static.jeu.fr:35.186.238.173",
        "static.jeu.fr:cds.m7t7c4m6.hwcdn.net",
        "static.jeu.fr:di-7i6hmqsq.vo.lswcdn.net",
        "static.stg.jeu.fr:35.186.238.173",
        "static.stg.jeu.fr:34.107.209.94",
        "stg.jeu.fr:35.186.238.173",
        "stg.jeu.fr:stg.lb.jeu.fr",
        "stg.lb.jeu.fr:34.95.79.96",
        "stg.lb.jeu.fr",
        "stg.lb.jeu.fr.",
        "switchin.jeu.fr:35.186.238.173",
        "t.jeu.fr:35.186.238.173",
        "tankball2.jeu.fr:35.186.238.173",
        "teamtanks.jeu.fr:35.186.238.173",
        "test.jeu.fr:52.200.92.237, 34.196.27.148",
        "test.jeu.fr:34.196.27.148, 52.200.92.237",
        "w.jeu.fr:35.186.238.173",
        "waroftitans.jeu.fr:35.186.238.173",
        "woozworld.jeu.fr:www-vpc-330095793.us-east-1.elb.amazonaws.com",
        "woozworld.jeu.fr:www.woozworld.com",
        "woozworld.jeu.fr:www.woozworld.com.",
        "woozworld.jeu.fr:18.208.14.206, 3.211.134.76",
        "worldofsoccer.jeu.fr:35.186.238.173",
        "ww.jeu.fr:35.186.238.173",
        "www.jeu.fr:34.231.157.198, 35.174.39.12, 18.235.254.189",
        "www.jeu.fr:34.231.157.198, 18.235.254.189, 35.174.39.12",
        "www.jeu.fr:34.95.108.35",
        "www.jeu.fr:yepi-application-loadbalancer-1784543555.us-east-1.elb.amazonaws.com.",
        "www.jeu.fr:35.174.39.12, 34.231.157.198, 18.235.254.189",
        "www.jeu.fr:18.235.254.189, 34.231.157.198, 35.174.39.12",
        "www.jeu.fr:18.235.254.189, 35.174.39.12, 34.231.157.198",
        "www.jeu.fr:35.174.39.12, 18.235.254.189, 34.231.157.198",
        "www.lb.jeu.fr:34.95.108.35",
        "www.login.jeu.fr:35.186.238.173",
        "xblaster.jeu.fr:35.186.238.173"
    ],
    "interesting_urls": [
        "http://www.jeu.fr/",
        "https://mail2.amazon.jeu.fr/signin.php",
        "https://www.jeu.fr/?utm_source=spildomains&utm_medium=redirect&utm_campaign=mail2.amazon.jeu.fr"
    ],
    "ips": [
        "3.64.163.50",
        "3.93.83.85",
        "3.228.245.203",
        "5.22.145.16",
        "5.22.145.121",
        "5.35.232.119",
        "5.39.76.234",
        "5.104.105.135",
        "5.135.252.9",
        "5.187.126.145",
        "13.37.6.18",
        "13.248.150.189",
        "23.227.38.32",
        "23.227.38.36",
        "23.227.38.65",
        "23.235.37.119",
        "23.236.62.147",
        "31.207.35.105",
        "34.77.251.68",
        "34.95.79.96",
        "34.95.108.35",
        "34.107.209.94",
        "34.213.106.51",
        "35.186.238.173",
        "35.201.104.236",
        "35.214.45.95",
        "35.214.145.246",
        "35.214.218.97",
        "35.214.237.214",
        "37.97.135.129",
        "37.187.17.29",
        "37.187.248.56",
        "46.17.70.43",
        "46.17.70.44",
        "46.51.206.141",
        "46.101.121.244",
        "46.105.56.89",
        "46.105.57.169",
        "46.105.78.122",
        "46.105.121.45",
        "46.166.189.98",
        "46.182.4.120",
        "46.183.50.44",
        "46.247.135.9",
        "46.255.160.251",
        "51.15.15.93",
        "51.15.185.165",
        "51.38.48.83",
        "51.68.117.202",
        "51.68.123.12",
        "51.68.190.249",
        "51.75.97.37",
        "51.79.164.104",
        "51.89.191.60",
        "51.91.18.148",
        "51.91.36.239",
        "51.91.60.233",
        "51.91.236.193",
        "51.91.236.255",
        "51.158.70.155",
        "51.178.81.9",
        "51.178.82.155",
        "51.178.112.113",
        "51.178.219.207",
        "51.254.16.36",
        "52.2.56.64",
        "52.6.168.161",
        "52.21.33.16",
        "52.30.116.180",
        "52.31.163.216",
        "52.36.172.71",
        "52.45.20.64",
        "52.49.93.188",
        "52.50.200.106",
        "52.54.163.93",
        "52.202.150.81",
        "52.213.220.98",
        "54.36.91.62",
        "54.36.136.152",
        "54.36.190.113",
        "54.37.100.196",
        "54.37.162.121",
        "54.37.169.108",
        "54.38.7.236",
        "54.68.182.72",
        "54.75.61.127",
        "54.76.77.34",
        "54.88.27.200",
        "54.161.77.142",
        "54.213.236.111",
        "62.210.105.203",
        "62.210.201.13",
        "63.34.192.120",
        "63.249.197.23",
        "64.190.62.111",
        "66.114.52.10",
        "66.114.52.11",
        "66.114.52.12",
        "66.114.52.14",
        "72.21.81.131",
        "72.21.91.19",
        "72.21.91.39",
        "72.21.92.20",
        "72.52.10.14",
        "74.208.29.71",
        "76.223.18.1",
        "77.158.35.202",
        "78.40.8.125",
        "79.99.38.16",
        "79.137.5.137",
        "80.80.233.53",
        "80.92.70.141",
        "80.237.138.5",
        "80.245.16.174",
        "81.92.80.55",
        "81.92.80.56",
        "81.169.145.152",
        "82.64.47.238",
        "82.65.234.120",
        "82.165.68.80",
        "83.166.130.52",
        "83.166.138.187",
        "83.167.59.11",
        "84.16.66.164",
        "84.16.76.220",
        "84.16.76.235",
        "84.246.225.176",
        "85.14.138.113",
        "85.236.157.21",
        "87.98.150.35",
        "87.98.188.232",
        "87.98.242.236",
        "87.98.247.4",
        "87.106.15.162",
        "89.238.140.16",
        "91.121.31.214",
        "91.121.34.147",
        "91.121.37.205",
        "91.121.41.228",
        "91.121.58.113",
        "91.121.233.68",
        "91.121.243.183",
        "91.132.253.21",
        "91.134.167.163",
        "91.216.107.46",
        "91.216.107.47",
        "91.216.107.146",
        "91.224.162.23",
        "92.222.80.210",
        "92.222.94.73",
        "92.222.139.190",
        "92.222.150.170",
        "92.222.255.101",
        "93.88.246.189",
        "93.184.220.39",
        "94.23.16.94",
        "94.23.58.143",
        "94.23.109.84",
        "94.23.114.138",
        "94.23.114.155",
        "94.23.114.158",
        "94.23.115.104",
        "94.23.218.41",
        "104.18.12.156",
        "104.18.13.156",
        "104.18.30.183",
        "104.18.31.183",
        "104.21.12.205",
        "104.21.18.180",
        "104.21.23.201",
        "104.21.26.144",
        "104.21.33.121",
        "104.21.33.198",
        "104.21.34.237",
        "104.21.45.65",
        "104.21.48.24",
        "104.21.65.134",
        "104.21.68.20",
        "104.21.68.93",
        "104.21.71.17",
        "104.21.76.12",
        "104.21.77.236",
        "104.21.81.76",
        "104.21.87.81",
        "104.21.89.35",
        "104.21.89.160",
        "104.247.81.51",
        "104.247.81.53",
        "104.247.81.54",
        "107.21.178.125",
        "107.178.250.147",
        "109.69.187.130",
        "109.234.160.22",
        "109.234.161.33",
        "109.234.161.51",
        "109.234.161.158",
        "109.234.161.178",
        "109.234.161.200",
        "109.234.162.14",
        "109.234.162.39",
        "109.234.164.49",
        "109.234.164.84",
        "109.234.164.101",
        "109.234.164.134",
        "109.234.165.33",
        "109.234.165.83",
        "127.0.0.1",
        "127.0.0.2",
        "127.0.0.4",
        "128.65.195.127",
        "128.65.195.207",
        "128.204.216.222",
        "129.151.254.61",
        "135.125.160.59",
        "141.95.139.97",
        "142.93.107.115",
        "145.239.37.162",
        "145.239.120.63",
        "145.239.140.148",
        "146.59.209.152",
        "146.88.234.242",
        "146.88.237.34",
        "146.88.237.40",
        "149.202.23.67",
        "151.80.25.48",
        "151.80.59.28",
        "151.249.89.21",
        "152.199.20.177",
        "154.41.67.224",
        "154.49.211.95",
        "155.133.132.8",
        "158.190.101.146",
        "163.172.75.142",
        "163.172.75.186",
        "163.172.196.236",
        "164.132.95.103",
        "164.132.152.69",
        "164.132.152.71",
        "164.132.235.17",
        "165.160.13.20",
        "165.160.15.20",
        "167.99.242.112",
        "167.114.98.180",
        "172.67.136.129",
        "172.67.136.249",
        "172.67.142.130",
        "172.67.144.142",
        "172.67.149.27",
        "172.67.153.66",
        "172.67.158.64",
        "172.67.163.161",
        "172.67.166.84",
        "172.67.169.1",
        "172.67.176.32",
        "172.67.183.25",
        "172.67.185.11",
        "172.67.185.28",
        "172.67.189.154",
        "172.67.192.189",
        "172.67.210.189",
        "172.67.212.150",
        "172.67.213.59",
        "174.35.10.195",
        "174.35.22.29",
        "174.35.24.74",
        "174.35.30.74",
        "174.35.30.76",
        "174.35.30.82",
        "174.35.30.83",
        "174.35.30.132",
        "174.35.30.141",
        "174.35.30.144",
        "174.35.30.145",
        "174.35.30.151",
        "174.35.30.153",
        "174.35.30.155",
        "174.35.30.195",
        "174.35.30.199",
        "174.35.30.202",
        "174.35.30.203",
        "174.35.30.213",
        "174.35.30.217",
        "174.35.32.96",
        "174.35.35.16",
        "174.35.35.17",
        "174.35.35.36",
        "174.35.35.37",
        "174.35.37.141",
        "174.35.37.144",
        "174.35.50.73",
        "174.35.50.75",
        "178.20.66.231",
        "178.32.4.52",
        "178.32.175.231",
        "185.2.4.98",
        "185.2.4.106",
        "185.31.40.12",
        "185.31.40.16",
        "185.47.61.20",
        "185.63.173.6",
        "185.65.56.159",
        "185.65.56.190",
        "185.65.56.191",
        "185.65.56.196",
        "185.75.71.133",
        "185.93.1.241",
        "185.93.1.243",
        "185.98.131.28",
        "185.98.131.40",
        "185.98.131.44",
        "185.98.131.45",
        "185.98.131.213",
        "185.98.136.51",
        "185.100.4.82",
        "185.136.96.96",
        "185.136.97.96",
        "185.136.98.96",
        "185.136.99.96",
        "185.181.104.74",
        "185.181.163.123",
        "185.230.63.107",
        "185.230.63.171",
        "185.230.63.186",
        "188.130.25.102",
        "188.130.25.202",
        "188.165.4.35",
        "188.165.26.121",
        "188.165.33.133",
        "188.165.53.185",
        "188.165.61.82",
        "188.165.220.133",
        "192.0.78.24",
        "192.0.78.25",
        "192.0.78.180",
        "192.0.78.231",
        "193.34.136.223",
        "193.70.45.215",
        "193.169.64.193",
        "193.203.239.24",
        "193.203.239.25",
        "193.203.239.34",
        "193.238.228.174",
        "193.238.231.57",
        "194.5.30.10",
        "194.145.209.43",
        "194.146.224.78",
        "194.150.236.81",
        "194.169.225.100",
        "195.15.224.118",
        "195.66.82.43",
        "195.72.134.91",
        "195.72.135.91",
        "195.154.55.84",
        "195.154.154.51",
        "199.34.228.59",
        "205.185.216.10",
        "205.185.216.42",
        "212.72.60.152",
        "212.72.60.153",
        "212.72.60.162",
        "212.72.60.163",
        "212.72.60.164",
        "212.72.60.165",
        "212.72.60.166",
        "212.72.60.167",
        "212.72.60.177",
        "212.72.60.178",
        "212.72.60.181",
        "212.72.60.182",
        "212.72.60.197",
        "212.72.60.198",
        "212.72.60.214",
        "212.72.60.215",
        "212.72.60.218",
        "212.72.60.219",
        "212.72.60.220",
        "212.72.60.221",
        "212.72.60.223",
        "212.72.60.224",
        "212.72.60.226",
        "212.72.60.227",
        "212.129.27.193",
        "212.227.247.121",
        "213.36.252.182",
        "213.36.252.183",
        "213.171.208.172",
        "213.186.33.2",
        "213.186.33.3",
        "213.186.33.4",
        "213.186.33.5",
        "213.186.33.17",
        "213.186.33.18",
        "213.186.33.19",
        "213.186.33.24",
        "213.186.33.40",
        "213.186.33.50",
        "213.186.33.82",
        "213.186.33.87",
        "213.186.33.176",
        "213.186.33.177",
        "213.251.188.141",
        "216.58.204.147",
        "217.19.248.132",
        "217.70.184.38",
        "217.70.184.55",
        "217.160.0.28",
        "217.160.0.32",
        "217.160.0.40",
        "217.160.0.57",
        "217.160.0.64",
        "217.160.0.69",
        "217.160.0.74",
        "217.160.0.77",
        "217.160.0.91",
        "217.160.0.92",
        "217.160.0.97",
        "217.160.0.105",
        "217.160.0.134",
        "217.160.0.135",
        "217.160.0.138",
        "217.160.0.151",
        "217.160.0.169",
        "217.160.0.199",
        "217.160.0.203",
        "217.160.0.207",
        "217.160.0.215",
        "217.160.231.208",
        "217.160.233.140",
        "217.160.233.217",
        "217.182.222.221"
    ],
    "linkedin_people": [
        "Alain Moreno ",
        "Alan Sanz - Creajeux ",
        "Alexandra Manet - Graphiste ",
        "Alexandre Lancelin ",
        "Arthur Six - Remontada le Jeu ",
        "Ber WAJCHENDLER ",
        "Briac du Jeu ",
        "Charles COLLIER ",
        "Charlotte Gervreau - Auberge du Jeu de Paume ",
        "Christian du Jeu ",
        "Christophe Gonthier ",
        "Christophe Jeu ",
        "DIDIER JEU - Commercial ",
        "Damien LUREL ",
        "David Broc ",
        "Dylan V. ",
        "Evingel Vanessa ",
        "Franck Da Silva ",
        "Francois Montmirel - Owner ",
        "Gaspard DU JEU - Product Marketing Manager ",
        "Genet Alain ",
        "Ghislain du Jeu ",
        "Henri Morawski - Chef de projet culturel ",
        "Hubert Jeu - Ordre de Malte France ",
        "Hugues du Jeu - Consultant ",
        "Isabeau du Jeu - Head Of English ",
        "Islem Sharouda ",
        "Jeux DePiste - Detective ",
        "Jeux pour Deux - Blogueur ",
        "Juliette Rosard ",
        "Justine Magniez - Commercial ",
        "Kalliance Le Jeu - co fondatrice ",
        "Karl CCCP ",
        "Kikos Jeux ",
        "Laurent Demichel - Formateur consultant ",
        "Le Temple du Jeu Multilud - magasin de jeux ",
        "Lionel PICHON - Directeur Commercial ",
        "Lisa BENHATRI ",
        "Luc Becker ",
        "Luc Janes ",
        "Marie Edery ",
        "Marie GUIBERT ",
        "Mathieu LAURENCE ",
        "Mathilde Morel ",
        "Maud VAMBERT - Animation par le Jeu ",
        "Maxime Bienvenu ",
        "Michael Merletti - Croupier de jeu ",
        "Michel CGT ",
        "Michel LE ROY ",
        "Minh Duc Nguyen - Fondateur ",
        "Mylene Migazzi - Administratrice des ventes ",
        "Nicolas Fort ",
        "Paul Jeu - Equipier polyvalent ",
        "Pierre-Yves Franck ",
        "Renaud Mearini ",
        "Ricardo Eliassaint - Technicien polyvalent ",
        "Ronan Marec - Au Coin Du Jeu Lorient ",
        "Sandrine JEU - VRP ",
        "Sandrine Saltao - Auberge du Jeu de Paume ",
        "Stephanie Thibaux ",
        "Studio Jeu de Pistes ",
        "Sylvie Guilleminot - Slapstick Prod et Jeux de mains ",
        "Thierry DETHOOR - Entrepreneur ",
        "Thomas Hossepied ",
        "Thomas Larcher ",
        "Thomas Mader ",
        "Thomas Planques ",
        "Tony Wart ",
        "Valentin Daubresse ",
        "Vanessa Kaplan ",
        "Victor Jeu ",
        "Virginie Chapron-du Jeu ",
        "Wilfried Fort ",
        "balade toi ",
        "jean jeu - ddd ",
        "sarah perin "
    ],
    "shodan": [],
    "trello_urls": [
        "https://trello.com/b/0ihafwx0/bac-pro-animation-1aepa-2023",
        "https://trello.com/b/0ybrbkdy/repartition-des-roles",
        "https://trello.com/b/2op7lfpq/lespawn-fr-suggestions",
        "https://trello.com/b/3d7n7ecn/tcel1-cours-de-mme-devaux-fr-et-hg",
        "https://trello.com/b/5gcoqmwx/to-do",
        "https://trello.com/b/5muwqpuu/no",
        "https://trello.com/b/7jsrvw6u/devmemories",
        "https://trello.com/b/8rvkunjd/senewebfr",
        "https://trello.com/b/agyorknb/digital-learning",
        "https://trello.com/b/avg8vvcn/fuzeau",
        "https://trello.com/b/b1jraj6t/graphiste",
        "https://trello.com/b/b9tvdr7d/switch-veille-sur-lorientation-scolaire",
        "https://trello.com/b/bbrqondf/danganronpa-bloodmoon-serie",
        "https://trello.com/b/bncwfbhb/ets-2019",
        "https://trello.com/b/bny6w0ui/restream-ootr-fr",
        "https://trello.com/b/bo2khwcx/justin-favier-conception-et-realisation-d-un-jeu-d-escape-game-futuriste-",
        "https://trello.com/b/bwev1eks/regles-elementaires",
        "https://trello.com/b/bxxfo2uy/cubexlandfr",
        "https://trello.com/b/c2p7zwgs/calendrier-editorial-instagram-blune",
        "https://trello.com/b/c5shjwav/defre",
        "https://trello.com/b/cto9is2i/funwise-minecraft",
        "https://trello.com/b/cve4ah1h/contributions-elrond-france",
        "https://trello.com/b/dpwwadgx/slash-fr-suggestions",
        "https://trello.com/b/dy5barkd/nassim",
        "https://trello.com/b/e4zyynrk/vn-travail-d",
        "https://trello.com/b/fgzsbbvt/vio-campagne-omt-covid-19",
        "https://trello.com/b/fiqpobvm/draftbot-bot-discord",
        "https://trello.com/b/ftww4pnh/veille-informatique",
        "https://trello.com/b/gmoncewb/veille-informationnelle",
        "https://trello.com/b/hunk7dhs/cars-byama",
        "https://trello.com/b/hvfgdr4v/groupe-classe-tapr-lp-jacquard-oullins",
        "https://trello.com/b/ignbcg8y/board",
        "https://trello.com/b/imgbzjet/des-id",
        "https://trello.com/b/iqlnpqye/to-do",
        "https://trello.com/b/iyplu6dt/groupe-classe-tspvl-jacquard",
        "https://trello.com/b/j8utdhw1/restons-group",
        "https://trello.com/b/klhzmfz6/onset-rp-fr-v2",
        "https://trello.com/b/lqichpk6/cec-semaine-des-langues",
        "https://trello.com/b/lwgk4tvh/sciences-inverses",
        "https://trello.com/b/mr9gkwfk/boite-a-outils-marketing-digital-design",
        "https://trello.com/b/msoudnno/omega-roleplay-fr",
        "https://trello.com/b/muuzqwes/formations-noemi-parcours-test-f",
        "https://trello.com/b/myqgzmvi/planif-sec-4-5-2021-2022",
        "https://trello.com/b/noudovtf/ayoub",
        "https://trello.com/b/okrfodid/id",
        "https://trello.com/b/ouz8fvru/orbital-views-press-review",
        "https://trello.com/b/pcpalzo8/chemin",
        "https://trello.com/b/pe8mtexn/poc-capeline-sprint-02-d",
        "https://trello.com/b/ptolehyz/roguelikefr",
        "https://trello.com/b/qhqoifm8/lrp-changelog",
        "https://trello.com/b/s9ipmfuc/projets-medias-1-2-3-cycles",
        "https://trello.com/b/tyx925nj/nouvelle-revue",
        "https://trello.com/b/ujpacgyu/calendrier-editorial-facebook-blune",
        "https://trello.com/b/wnqci0yk/r",
        "https://trello.com/b/xicdvcvz/glossarissimo",
        "https://trello.com/b/xnpkpkgb/les-bibliotheques-de-saint-brieuc",
        "https://trello.com/b/y839rx6i/hyldaria-fr",
        "https://trello.com/b/yqksllgz/boite-a-outils",
        "https://trello.com/b/yxfjrrvo/bibliotheque",
        "https://trello.com/b/zhhbelri/guide-dragon-raja-fr",
        "https://trello.com/b/zou6vta7/yellow-agile",
        "https://trello.com/c/06ek3sxs/33-site-vitrine-rc-prise-de-contact-avec-informaticien-pour-modif",
        "https://trello.com/c/0yiqdvyy/24-fran",
        "https://trello.com/c/1otvlbe5/104-marshmallow-challenge-entre-10-et-30pers-30-min",
        "https://trello.com/c/1qzjqmrx/149-free-lego-seigneur-des-anneaux-pc-crack-fr",
        "https://trello.com/c/2k200jae/6-multi-alexandra-ledermann-8-les-secrets-du-haras-fr",
        "https://trello.com/c/3gkbdpru/1539-faire-plus-de-petite-animation-comme-par-exemple-le-loup-garou-plato-plusieurs-sorte-de-mini-jeux-gartic-phone-et-autre",
        "https://trello.com/c/3kzosujm/56-jeu-darme-nuketown",
        "https://trello.com/c/4cmymnfu/3-vtech-storio-2-jeux-crack",
        "https://trello.com/c/6tg8lgq1/116-les-cinq-legende-french-dvdrip-wedleksi",
        "https://trello.com/c/70hk0tw9/78-scicog-knowledge-graph",
        "https://trello.com/c/7mrgtkfx/94-new-la-nouvelle-maison-du-style-roms-3dsl",
        "https://trello.com/c/847ncnkl/69-empereur-l-empire-du-milieu",
        "https://trello.com/c/9abn4rzt/42-jeux-auditifs-et-visuels",
        "https://trello.com/c/9kbxlnho/21-lego-seigneur-des-anneaux-pc-crack-fr-best",
        "https://trello.com/c/9rmczjgl/316-cestes-aeth",
        "https://trello.com/c/9tomeuxv/9-conjugo",
        "https://trello.com/c/9zfsecvq/22-fifa-12-pc-commentary-language-packs",
        "https://trello.com/c/a58vq9bp/10-titre-professionnel-d",
        "https://trello.com/c/adxqdydl/95-ademe-base-carbone",
        "https://trello.com/c/asu9334p/12-club-des-trouvetout-la-cit-perdue",
        "https://trello.com/c/b1mhmuqk/8-top-crack-covadis-11rar",
        "https://trello.com/c/baezncho/4-bright-memory-infinite-pr",
        "https://trello.com/c/bgqafvie/246-sans-pr",
        "https://trello.com/c/buutky6j/104-outils-2e",
        "https://trello.com/c/bypcio0m/27-jeu-qui-veut-gagner-des-millions-gratuit-en-francais-crack",
        "https://trello.com/c/c4yvys38/48-test-de-niveau-fran",
        "https://trello.com/c/cdxadnpk/54-across-the-grooves",
        "https://trello.com/c/ckrrjli6/3-le-ch",
        "https://trello.com/c/ckwyx4q4/87-vtech-storio-2-jeux-crack-yamiretta",
        "https://trello.com/c/d2ags0ez/45-ravensburger-jeu-interactif-tiptoi-a-la-d",
        "https://trello.com/c/dab3pn2l/44-l",
        "https://trello.com/c/dgdaehgf/29-x32-fr-police-simula-registration-final-keygen-full",
        "https://trello.com/c/dlq8zyyr/43-jeux-solf",
        "https://trello.com/c/dmptswqd/180-candy-love-5-",
        "https://trello.com/c/dpv778os/48-jeux-de-rythme",
        "https://trello.com/c/ekcvrdbz/26-fable-2-for-pc-microsoft-windows-macos-download-complet-version",
        "https://trello.com/c/ekgu5s2u/72-exposition-chefs-d",
        "https://trello.com/c/emejbitb/82-licence-https-datagrandlyoncom",
        "https://trello.com/c/exjacl67/4-suggestion-de-titilh76-ajouter-des-v",
        "https://trello.com/c/f02atobj/130-jeux-sur-leurope-f",
        "https://trello.com/c/fer7yclq/1183-faire-des-salons-de-discussion-",
        "https://trello.com/c/fngpdgeg/1-juliette-digital-wording-nl-soi-paris",
        "https://trello.com/c/gmh6zgmr/127-10",
        "https://trello.com/c/gumvmdhy/451-",
        "https://trello.com/c/gybzn2e2/161-fix-spectromancer-activation-code-keygen-music",
        "https://trello.com/c/h5qg05bl/49-club-des-trouvetout-la-cit-perdue",
        "https://trello.com/c/hgzphror/63-proc",
        "https://trello.com/c/hqu4ghtc/969-jeu-wordle",
        "https://trello.com/c/hyvbatyn/14-retropardy",
        "https://trello.com/c/ia31uryh/11-sims-4-crack-patch-fr",
        "https://trello.com/c/idrsjbj1/1363-telecharger-gta-4-pc-sur-utorrent",
        "https://trello.com/c/ivzzsr46/81-harmoniser-les-traductions-de-review",
        "https://trello.com/c/iwrt9psw/2429-moussa-wagu",
        "https://trello.com/c/j39w0zfm/148-rank-citoyen-doreo",
        "https://trello.com/c/jfm47l0y/64-exercices-compl",
        "https://trello.com/c/jgj19pnp/239-sutom-motus-1-mot-par-jour",
        "https://trello.com/c/jimfpqnu/42-yams",
        "https://trello.com/c/jvsnoidn/25-unit-5-relationships-in-triangles-gina-wilson-answer-key",
        "https://trello.com/c/jzdtfovl/119-patch-fr-city-car-driving-karlefri",
        "https://trello.com/c/k3dtm8jv/19-empereur-l-empire-du-milieu-latest-activator-64-keygen-windows-full-version-utorrent",
        "https://trello.com/c/khj0bs6a/75-fwd-relance-litige-r",
        "https://trello.com/c/kjldkpol/244-escape-game-outils-de-cr",
        "https://trello.com/c/kyiaarce/1-l-osti-d-jeupdf",
        "https://trello.com/c/l5ypjs3m/28-monopoly-tricheurs-jeu-de-societe-jeu-de-plateau-pour-la-famille-version-francaise-a-partir-de-8-ans-amazonfr-jeux-et-jouets",
        "https://trello.com/c/lfrg8n7h/54-d",
        "https://trello.com/c/lli9lwjx/12-alexandra-ledermann-7-pc-crack-z-patched",
        "https://trello.com/c/lnz75z/62-out-there-oceans-of-time",
        "https://trello.com/c/loawtj3p/586-225-le-code-source-de-chaque-page-contient-une-m",
        "https://trello.com/c/mf9xbu7t/32-suggestion-15-889850080188850196",
        "https://trello.com/c/mjlffuag/111-le-monde-de-nemo-pc-fr-link-crack-torrent",
        "https://trello.com/c/mk0xhgk4/4-telecharger-jeux-psp-gratuit-resident-evil-4-psp-iso",
        "https://trello.com/c/mqyzvl7z/67-fifa-12-commentary-pack-all-languages-uleechri",
        "https://trello.com/c/muivpdhl/44-patch-fr-police-simulator-2",
        "https://trello.com/c/mur4xclp/5-liste-des-activit",
        "https://trello.com/c/mvcrjfeh/57-suggestion-40-923157990754881597",
        "https://trello.com/c/nbaxuupw/20-1c-concurrents-to-do",
        "https://trello.com/c/nnfyxasc/50-solsuite-2012-francais-patch-fr-best",
        "https://trello.com/c/o4ht4bid/28-serie-les-revenants-saison-1-complet-dvdrip-fr-torrent-tullidarw",
        "https://trello.com/c/olktteod/159-excuse-moi-c",
        "https://trello.com/c/pgwtewln/28-docteur-maboul",
        "https://trello.com/c/q66tmfti/84-orchestra-lab",
        "https://trello.com/c/qe9juedt/4908-le-reve-de-souleymane-seneplus",
        "https://trello.com/c/qiwoxadh/89-harmoniser-les-traductions-de-reset",
        "https://trello.com/c/qltoe5vp/206-divinity-original-sin-german-language-pack-download-free",
        "https://trello.com/c/qmufztqu/53-telecharger-jeux-psp-gratuit-resident-evil-4-psp-iso-exclusive",
        "https://trello.com/c/qnwo8gki/15-commandos-le-sens-du-devoir-crack",
        "https://trello.com/c/r06oxddo/57-programmation",
        "https://trello.com/c/rakllnlt/75-lespion-qui-maimait-dvdrip",
        "https://trello.com/c/rgddu0dc/2-tof-turf-365",
        "https://trello.com/c/rjkfnraz/50-red-dead-redemption-games-pc-iso-fr-torrent",
        "https://trello.com/c/sbbekazk/50-lego-seigneur-des-anneaux-pc-crack-fr",
        "https://trello.com/c/sjahld0s/1445-top-scan-wakfu-tome-1-fr",
        "https://trello.com/c/stptla1c/221-au-c",
        "https://trello.com/c/sv7tqwhg/12-fishdom-triche-astuce-fishdom-diamants-et-pieces-illimite",
        "https://trello.com/c/sxeefacw/53-spellcaster-university",
        "https://trello.com/c/t7p5q5k1/560-5-pratiques-p",
        "https://trello.com/c/tc2w4fnv/41-repack-iden-lab-rss-29-patch",
        "https://trello.com/c/thpeec3v/86-re-fin-de-contrat-mood-media",
        "https://trello.com/c/tonafyvd/39-crash-time-5-patch-fr-expsubje",
        "https://trello.com/c/tz3qvhh3/22-jeux-de-confiance-et-esprit-d",
        "https://trello.com/c/u8dls6ot/38-sites-musique-coll",
        "https://trello.com/c/ueh3fmik/39-telecharger-jeux-gratuit-storio-3epub",
        "https://trello.com/c/ujvivftw/121-le-projet-dont-vous-",
        "https://trello.com/c/umsq9fti/371-patch-fr-red-faction-armageddon-pc-maricgarr",
        "https://trello.com/c/uz5ydqe1/304-secret-files-3-patch-fr-deaanni",
        "https://trello.com/c/uzrexbmq/18-windows-7-titan-fr-64-bits-iso-trisvanil",
        "https://trello.com/c/v6x7u1lj/42-mes-amis-sont-3-11-j-30-min-16",
        "https://trello.com/c/vl7edrsx/25-apprendre-",
        "https://trello.com/c/vwyrkskp/20-lula-3d-patch-fr",
        "https://trello.com/c/wcaekanj/8-super-ordre-pmu",
        "https://trello.com/c/we1ckcry/123-telecharger-petanque-le-jeu-du-centenaire-gratuit",
        "https://trello.com/c/wiwsmsxg/44-terrorist-takedown-3-english-language-pack-top",
        "https://trello.com/c/wlo6sifw/103-outils-1",
        "https://trello.com/c/wpcjuyfg/14-top-fifa-12-pc-commentary-language-packs",
        "https://trello.com/c/ws0kravr/1756-m-archambaudpsi1psiet1groupe6-supercondensateurs",
        "https://trello.com/c/wvjcuv6a/42-la-course-",
        "https://trello.com/c/x3lpz3ad/11-google-apps-script-url-parameters",
        "https://trello.com/c/xlhuovad/5-telecharger-c-pas-bien-jeux-pc-gratuit-verified",
        "https://trello.com/c/xrswvmkk/9-patch-francais-cabelas-big-game-hunter-pro-hunts",
        "https://trello.com/c/y4n5e3a3/913-fr-lexique-des-termes-utilis",
        "https://trello.com/c/yjnml3qh/105-outils-2ec",
        "https://trello.com/c/ytiqllkl/14-mettre-les-modes-de-jeux-comme-ballpings-amogse3",
        "https://trello.com/c/yvk8wqoz/4-telecharger-dexter-saison-6-french-torrent-bereacaci",
        "https://trello.com/c/zdfcakqw/4772-patch-fr-police-simulator-2-top",
        "https://trello.com/c/zeuqavkj/10-telechargement-12-dictionnaires-indispensables-gratuit",
        "https://trello.com/c/zhj1rcxq/39-kaeloo-saison-2-torrentfr-mega-best",
        "https://trello.com/c/zmeesm5f/60-solasta-crown-of-the-magister",
        "https://trello.com/c/zylegwm4/20-https-wwwfrancebleufr-emissions-l-invite-de-7h50-france-bleu-herault-herault-l-invite-de-7h50-france-bleu-herault-888fbclidiwar0",
        "https://trello.com/fr/government",
        "https://trello.com/fr/guide/enterprise/admins-dashboard",
        "https://trello.com/fr/guide/enterprise/creating-projects-inviting-members",
        "https://trello.com/fr/guide/remote-work/communication-collaboration",
        "https://trello.com/fr/guide/remote-work/digital-tools",
        "https://trello.com/fr/teams/home",
        "https://trello.com/fr/teams/support",
        "https://trello.com/fr/use-cases/meetings"
    ],
    "twitter_people": [
        "@932Ak1m",
        "@AffordStudio",
        "@Aiirmes",
        "@Akihide_Tsugane",
        "@AlphaCastFR",
        "@At0mium_",
        "@CHOWh1z1",
        "@CJackmiel",
        "@Cardosotaku37",
        "@Clionautes1",
        "@Doc_Noki",
        "@Intovinceres",
        "@JVCom",
        "@Jeel_TV",
        "@Jeux_jeu",
        "@LaPvlga",
        "@LeVeritableVun",
        "@Makiudbzublgh",
        "@MarionDeborde",
        "@MillVictories",
        "@NeeoxxYTL",
        "@Nos_Trotro",
        "@Noxymillien",
        "@OrangePaix",
        "@Pandrezz",
        "@Rams_Meb",
        "@RaphI_I",
        "@RaveaudGilles",
        "@ScienceXGames",
        "@Sow_Aida",
        "@Stritllors1",
        "@Supergame1232",
        "@TheArcadeCrew",
        "@VoiceOfOBrien",
        "@YouTube",
        "@Ypsem",
        "@_Lyslero_",
        "@akaAgar",
        "@alexinthesauuce",
        "@atlantide_io",
        "@badgonesdu69",
        "@dowinordine",
        "@dredshin",
        "@font",
        "@fuckyoubIoody",
        "@gautoz",
        "@getcrackin",
        "@gh0stwaltz",
        "@hamsterjoueur",
        "@keyframes",
        "@larouchealexe",
        "@media",
        "@morin61400",
        "@nintendalerts",
        "@seb666astien",
        "@theomcx",
        "@titi_juju",
        "@toomsoo_",
        "@tralalere",
        "@vanitus111",
        "@woetices",
        "@xim8__"
    ]
}
    };
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
    sendEmail() {
      axios
        .get(`http://127.0.0.1:5000/api/email/${this.inputEmail}`)
        .then((response) => {
          console.log(response.data);
        })
        .catch((e) => {
          console.log(e);;
        });
    },
    sendPseudo() {
      axios
        .get(`http://127.0.0.1:5000/api/pseudo/${this.inputPseudo}`)
        .then((response) => {
          // JSON responses are automatically parsed.
          this.dataSherlock = response.data;
          console.log(response.data);
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
