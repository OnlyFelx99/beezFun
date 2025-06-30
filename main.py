from flask import Flask, jsonify
import random 

app = Flask(__name__)

Kiss = [
    "https://i.postimg.cc/7PtSXZrV/anime-kiss.gif",  "https://i.postimg.cc/W1kmdLK7/anime-kiss-1.gif",  "https://i.postimg.cc/GtfYpqxN/anime-kiss-anime.gif",  "https://i.postimg.cc/rpGS9Gq0/engage-kiss-anime-kiss.gif",   "https://i.postimg.cc/3RnmsK43/hyakkano-100-girlfriends.gif", "https://i.postimg.cc/5NZLdK0Q/kiss.gif",   "https://i.postimg.cc/WzzgjQgg/kiss-kisses.gif",    "https://i.postimg.cc/HsJXN1pC/love-cheek.gif",   "https://i.postimg.cc/QMZQ5YZZ/romance.gif", "https://i.postimg.cc/YSWNZKkP/64dbd9804a16727969c009911f04f611.gif", "https://i.postimg.cc/bwd90S5p/a58515204a44d696ad8f080bce1656d9.gif", "https://i.postimg.cc/RZ8QgVrf/debe0021256cde2eaa0a252506011799.gif"
]

@app.route('/')
def index():
    return "♦️ API funcionando, Existem 3 rotas /beez/kiss , /beez/hug, /team, todas sendo **GET!** "

@app.route('/beez/kiss', methods=['GET'])
def exemplo():
    dados = random.choice(Kiss)
    return (dados)



Hug = [  "https://i.postimg.cc/NG8jfNpr/aharen-san-anime-hug.gif",   "https://i.postimg.cc/7YxYCgWt/engage-kiss-anime-hug.gif", "https://i.postimg.cc/MHY6PTvY/excited-hug.gif",   "https://i.postimg.cc/BQMZ2jWS/max-and-kaylee-profile-picture.gif",   "https://i.postimg.cc/1zgzmsj9/oshi-no-ko-aqua.gif",   "https://i.postimg.cc/hjTPmMn6/syno-i-love-you-syno.gif"
]



@app.route('/beez/hug', methods=['GET'])
def hug():
    dds = random.choice(Hug)
    return (dds)


@app.route('/team', methods=['GET'])
def team():
    team = "Essa api foi desenvolvida por parguin da beeZ Team! e feita para ajudar bots de entretenimento!, se quiser entrar na beeZ team entrar em contato! @parguin."
    return team




if __name__ == '__main__':
    app.run(debug=True)
    
