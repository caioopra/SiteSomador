import cherrypy


class Calculator:
    @cherrypy.expose
    def index(self):
        return "Hello World!"
    @cherrypy.expose
    def add(self, value1: str = "0", value2: str = "0") -> str:
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
        cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        cherrypy.response.headers["Access-Control-Allow-Headers"] = "Content-Type"

        if value1 == "" or value2 == "":
            return "Insira valores para o cálculo."

        try:
            value1 = float(value1)
            value2 = float(value2)
            
            return str(value1 + value2)

        except ValueError:
            return "Valores inválidos."


cherrypy.quickstart(Calculator(), '/', {'global': {'server.socket_host':'0.0.0.0','server.socket_port': 8080}})
