# import (אִימְפּוֹרְט - ייבוא): מביאים את הפונקציה login מהקובץ auth.py
from auth import login

# קוראים לפונקציה עם חייל מורשה. התוצאה: True (נכון) או False (לא נכון)
ok = login("soldier1", "pass123")

# if (איף - אם): אם התוצאה נכונה, מציגים Access granted, אחרת Access denied
if ok:
    message = "Access granted"
else:
    message = "Access denied"

# open (אוֹפֶּן - פתח) עם "w" (כתיבה): יוצר את הקובץ index.html עם ההודעה
with open("index.html", "w", encoding="utf-8") as f:
    f.write("<h1>" + message + "</h1>")