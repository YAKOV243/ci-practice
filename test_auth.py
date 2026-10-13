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