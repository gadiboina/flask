from flask import Flask,render_templates,request,url_from
import sqilite3
app = 
def index();
    conn = get_db()
    cursor = conn.cursor()
    cursor.excute("SELECT * FROM entries")
    entries = cursor.fetchall()
    conn.close()
    return render_template('index.html',entries=entries)
@app.route('/add',methods=['POST'])
def add_entry();
    title = request.from['title']
    content = request.from['content']
    conn = get_db()
    cursor.execute("INSERT INTO entries (title,content)VALUES(?,?)",(title,content))
    conn.commit()
    conn.close


 @app.route('/delete/<int:id'):
conn = get_db()
cursor = conn.cursor()
cursor.excute("DELETE FROM entries WHERE id=? ")
conn.commit()
conn.close()
return redirect(url_for('index'))

def init_db();
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXIST entries(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,content  TEXT NOT NULL)''')
    conn.commit()
    conn.close()
if __name__=='__main__':
    init_()
    app.run(debug==True)
