# import (אִימְפּוֹרְט - ייבוא): מביאים את הפונקציה login מהקובץ auth.py
from auth import login

# בדיקה 1: משתמש נכון וסיסמה נכונה, אמור להיכנס (True)
def test_valid_user():
    assert login("soldier1", "pass123") == True

# בדיקה 2: משתמש נכון וסיסמה שגויה, אמור להיחסם (False)
def test_wrong_password():
    assert login("soldier1", "wrong") == False

# בדיקה 3: משתמש שלא קיים ברשימה, אמור להיחסם (False)
def test_unknown_user():
    assert login("hacker", "pass123") == False

# בדיקה 4: סיסמה ריקה, אמור להיחסם (False)
def test_empty_password():
    assert login("soldier1", "") == False

# בדיקה 5: אותיות גדולות בשם משתמש צריכות להיחסם, כי הסיסמאות רגישות לאותיות
def test_uppercase_user():
    assert login("SOLDIER1", "pass123") == False

# בדיקה 6: סיסמה של משתמש אחר צריכה להיחסם
def test_other_users_password():
    assert login("soldier1", "abc456") == False

# בדיקה 7: משתמש שני עם סיסמה נכונה צריך להיכנס
def test_second_user():
    assert login("soldier2", "abc456") == True