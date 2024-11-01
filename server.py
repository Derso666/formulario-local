from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class ServidorContato(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/submit':
            # Determinar o tamanho dos dados recebidos
            content_length = int(self.headers['Content-Length'])
            # Ler os dados recebidos
            post_data = self.rfile.read(content_length)
            # Decodificar os dados
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            
            # Extrair as informações
            nome = data.get('nome', [''])[0]
            email = data.get('email', [''])[0]
            mensagem = data.get('mensagem', [''])[0]

            # Salvar as informações em um arquivo de texto
            with open("dados_contato.txt", "a", encoding="utf-8") as file:
                file.write(f"Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}\n\n")
            
            # Responder ao navegador com uma mensagem de sucesso
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<html><body><h2>Mensagem recebida com sucesso!</h2></body></html>")
        else:
            self.send_response(404)
            self.end_headers()

# Configurar e iniciar o servidor
def run():
    endereco_servidor = ('', 8000)  # Porta 8000
    httpd = HTTPServer(endereco_servidor, ServidorContato)
    print("Servidor rodando na porta 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
