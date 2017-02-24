from firebase import firebase
firebase = firebase.FirebaseApplication('https://coffeecu-6f84a.firebaseio.com/', authentication='AIzaSyB07PemCqeZDjBjgJu7dAOp6gUJI7KkirE')
#authentication = firebase.FirebaseAuthentication( 'AIzaSyB07PemCqeZDjBjgJu7dAOp6gUJI7KkirE')
#firebase.authentication = authentication
#print authentication.extra
result = firebase.get('/users', None)
print result
