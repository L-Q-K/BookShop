from flask import *
import mlab
from mongoengine import *

mlab.connect()

class Book(Document):
    name = StringField()
    image = StringField()
    description = StringField()

book = Book(name= "Mị Châu - Trọng Thủy",
    image= "https://i.ytimg.com/vi/JaQSmAU0UoY/maxresdefault.jpg",
    description= "Một cậu thanh niên với lòng yêu nước nồng nàn đã ra đi tìm đường cứu nước, nhưng cuối cùng lại lỡ sa vào đôi mắt em."
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', books=Book.objects())

@app.route('/admin')
def adminn():
    return render_template('admin.html',books=Book.objects())

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    #1. Delete book from database:
    book = Book.objects().with_id(book_id)
    if book is not None:
        #Found it:
        Book.delete()
    #2. Come back to admin:
    return redirect('/admin')

@app.route ('/read/<book_id>')
def book_content(book_id):
    return render_template(str(book_id) + '.html')

if __name__ == '__main__':
  app.run(debug=True)
