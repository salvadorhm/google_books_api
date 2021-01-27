import web
import requests
import json

render = web.template.render("mvc/")

class Index():

    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        book_name = form.book_name

        result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name)

        book = result.json()

        items = book["items"]

        encoded = json.dumps(items)
        decoded = json.loads(encoded)

        url = decoded[0]["volumeInfo"]["infoLink"]

        link ="<a target='blank' href='"+url+"'>"+book_name+"</a>"

        return link
