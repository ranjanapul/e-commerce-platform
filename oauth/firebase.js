import firebase from 'firebase/app'
import 'firebase/auth'

const app = firebase.initializeApp({
    apiKey: "AIzaSyD0vNHSNUWOTYYEa8utKyDaDSOn0OHbIH0",
    authDomain: "ecommerce-a9c9b.firebaseapp.com",
    projectId: "ecommerce-a9c9b",
    storageBucket: "ecommerce-a9c9b.appspot.com",
    messagingSenderId: "735053096772",
    appId: "1:735053096772:web:882bd1df2aed35fad0d911",
    measurementId: "G-KMB8DP5R7S"
})

export const auth = app.auth()
export default app