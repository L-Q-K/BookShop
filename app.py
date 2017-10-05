from flask import *
import mlab
from mongoengine import *

mlab.connect()

class Book(Document):
    name = StringField()
    image = StringField()
    description = StringField()

book = Book(    name= "Mị Châu - Trọng Thủy",
    image= "https://i.ytimg.com/vi/JaQSmAU0UoY/maxresdefault.jpg",
    description= "Một cậu thanh niên với lòng yêu nước nồng nàn đã ra đi tìm đường cứu nước, nhưng cuối cùng lại lỡ sa vào đôi mắt em."
)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', books=Book.objects())

if __name__ == '__main__':
  app.run(debug=True)
