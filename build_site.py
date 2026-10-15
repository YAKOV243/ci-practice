from auth import login

# בודקים שלושה מקרים אמיתיים ומציגים כל אחד בדף
cases = [
    ("soldier1", "pass123", "חייל מורשה עם סיסמה נכונה"),
    ("soldier1", "wrong", "חייל מורשה עם סיסמה שגויה"),
    ("hacker", "pass123", "משתמש שלא קיים ברשימה"),
]

rows = ""
for user, password, description in cases:
    ok = login(user, password)
    result = "אושר ✔" if ok else "נדחה ✘"
    rows += "<tr><td>" + description + "</td><td>" + result + "</td></tr>"

html = """<!DOCTYPE html>
<html lang="he" dir="rtl">
<head><meta charset="utf-8"><title>מערכת כניסה</title></head>
<body style="font-family:Arial;max-width:600px;margin:40px auto">
<h1>מערכת בקרת כניסה</h1>
<p>הדף הזה נבנה אוטומטית מתוצאות הפונקציה login.
הוא עלה לאוויר רק כי כל הבדיקות עברו.</p>
<table border="1" cellpadding="8">
<tr><th>מקרה</th><th>תוצאה</th></tr>""" + rows + """</table>
<h2>איך זה עבד?</h2>
<ol>
<li>כתבנו קוד ובדיקות בענף נפרד</li>
<li>דחפנו ל-GitHub, וה-CI הריץ את כל הבדיקות</li>
<li>פתחנו Pull Request וצירפנו ל-main</li>
<li>ה-CD פרסם את הדף הזה אוטומטית</li>
</ol>
</body></html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)