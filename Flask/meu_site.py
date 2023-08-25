from flask import Flask, render_template

app = Flask(__name__)

#Criar 1º pagina do site
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

#app é o nome do site que foi definido lá em cima.
#Rota padrão
#o simbolo @ significa decoreto -> linha d codigo que atribui uma nova funcionalidade para a funcao que vem abaixo
#criar arquivos na pasta templates
@app.route("/")
def homepage():
    #return "Alguma frase simples"
    return render_template("homepage.html")





@app.route("/contatos")
def contatos():
    #return "Contatos"
    return render_template("contatos.html")

    

#rotas dinamicas
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    #return nome_usuario
    return render_template("usuarios.html", nome_usuario=nome_usuario)





# colocar o site no ar
#o comando do if abaixo só roda se executar diretamente este codigo. Caso ele estiver sendo importado por outro arquivo ele nao vai entrar no if
#ao colocar o site no sr e nao tiver este codigo dessa maneira abaixo da erro
if __name__ == "__main__":
    #debug=true faz com que a cada mudaanca do codigo ele recompila automaticamente/
    app.run(debug=True)
    # servidor do heroku