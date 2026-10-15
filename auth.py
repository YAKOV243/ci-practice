# USERS (יוּזֶרְס - משתמשים): רשימה של שם משתמש וסיסמה.
# הסוגריים { } יוצרים מילון: זוגות של "שם: ערך".
USERS = {"soldier1": "pass123", "soldier2": "abc456"}

# def (דֶף - הגדרה): מגדירים פונקציה, פעולה עם שם.
# login (לוֹגִין - כניסה): השם שבחרנו.
# user (יוּזֶר - משתמש), password (פַּסְוֶורְד - סיסמה): הנתונים שנכנסים.
def login(user, password):
    # return (רִיטֶרְן - החזר): מחזיר תשובה.
    # user in USERS: האם השם נמצא ברשימה?
    # and (אֵנְד - וגם): שני התנאים חייבים להתקיים.
    # USERS[user] == password: האם הסיסמה תואמת?
    return user in USERS and USERS[user] == password