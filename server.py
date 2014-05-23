import web, webbrowser
render = web.template.render('templates/')
urls = ('/', 'index')

class index:
	def GET(self):
		return render.home(None)

if __name__ == '__main__':
	webbrowser.open("http://localhost:8080")
	app = web.application(urls, globals())
	app.run()