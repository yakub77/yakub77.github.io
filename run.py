from livereload import Server

server = Server()

server.watch('*.html')

server.watch('*.css')

server.watch('*.js')

server.serve(port=8000, liveport=35729, host='192.168.1.156')