var fireBase = fireBase || firebase;
var hasInit = false;
var config = {
    apiKey: "AIzaSyD0vNHSNUWOTYYEa8utKyDaDSOn0OHbIH0",
    authDomain: "ecommerce-a9c9b.firebaseapp.com", // URL of auth server. TO talk to this server securely, use API key, for project indentification, use projectID
    projectId: "ecommerce-a9c9b",
    storageBucket: "ecommerce-a9c9b.appspot.com",
    messagingSenderId: "735053096772"
  };
if(!hasInit){
    firebase.initializeApp(config);
    hasInit = true;
}