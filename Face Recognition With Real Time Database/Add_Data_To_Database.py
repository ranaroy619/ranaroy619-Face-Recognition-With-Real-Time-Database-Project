import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-project-28832-default-rtdb.firebaseio.com/"})

ref = db.reference('Students')
data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "totoal_attendance": 6,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economices",
            "starting_year": 2018,
            "totoal_attendance": 12,
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2018,
            "totoal_attendance": 7,
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)
