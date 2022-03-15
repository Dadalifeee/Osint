function sendDomain() {
  let message = $('#inputDomaine').val();
  console.log('%cindex.html line:132 message', 'color: #007acc;', message);
  if (message != "") {
      const encoreString = encodeURIComponent(message)
      console.log(`http://127.0.0.1:5000/api/domain/${encoreString}`)
      fetch(`http://127.0.0.1:5000/api/domain/${encoreString}`, {
          mode: 'cors',
          headers: {
              'Access-Control-Allow-Origin': '*',
              "content-type": "application/json"
          }
      }).then(function (response) {
        return response.text();
      }).then(function (text) {
          console.log(text); 
      });
  }
};

function sendPseudo() {
  let message = $('#inputPseudo').val();
  console.log('%cindex.html line:132 message', 'color: #007acc;', message);
  if (message != "") {
      const encoreString = encodeURIComponent(message)
      console.log(`http://127.0.0.1:5000/api/Pseudo/${encoreString}`)
      fetch(`http://127.0.0.1:5000/api/Pseudo/${encoreString}`, {
          mode: 'cors',
          headers: {
              'Access-Control-Allow-Origin': '*',
              "content-type": "application/json"
          }
      }).then(function (response) {
        return response.text();
      }).then(function (text) {
          console.log(text); 
      });
  }
};