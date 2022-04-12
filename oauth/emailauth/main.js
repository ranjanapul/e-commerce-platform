var mainApp = {};
(function(){
var mainContainer = document.getElementById("main_container");

    var logtout =  function(){
        firebase.auth().signOut().then(function(){
            console.log('success');
            window.location.replace("login.html");
        },function(){})
    }

var init = function(){
  console.log(firebase.auth().currentUser)
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
          // User is signed in.
          console.log({user: user.getIdToken()})
          console.log("stay");
          if (firebase.auth().currentUser !== null){ 
            console.log(firebase.auth().currentUser.uid);
            //console.log(firebase.auth().currentUser)
            var token = firebase.auth().currentUser.getIdToken();
            console.log(token)
          }
          mainContainer.style.display = "";
        } else {
          // No user is signed in.
          mainContainer.style.display = "none";
          console.log("redirect");
          window.location.replace("login.html");
        }
      });
}
    
init();

mainApp.logout = logtout;
})();