from flask import Flask, jsonify
import random 

app = Flask(__name__)

Kiss = [
    "https://i.postimg.cc/7PtSXZrV/anime-kiss.gif",  "https://i.postimg.cc/W1kmdLK7/anime-kiss-1.gif",  "https://i.postimg.cc/GtfYpqxN/anime-kiss-anime.gif",  "https://i.postimg.cc/rpGS9Gq0/engage-kiss-anime-kiss.gif",   "https://i.postimg.cc/3RnmsK43/hyakkano-100-girlfriends.gif", "https://i.postimg.cc/5NZLdK0Q/kiss.gif",   "https://i.postimg.cc/WzzgjQgg/kiss-kisses.gif",    "https://i.postimg.cc/HsJXN1pC/love-cheek.gif",   "https://i.postimg.cc/QMZQ5YZZ/romance.gif", "https://i.postimg.cc/YSWNZKkP/64dbd9804a16727969c009911f04f611.gif", "https://i.postimg.cc/bwd90S5p/a58515204a44d696ad8f080bce1656d9.gif", "https://i.postimg.cc/RZ8QgVrf/debe0021256cde2eaa0a252506011799.gif"
]

@app.route('/')
def index():
    return "♦️ API funcionando, Existem 4 rotas /beez/kiss , /beez/hug, /team, /beez/job, todas sendo **GET!** "

@app.route('/beez/kiss', methods=['GET'])
def exemplo():
    dados = random.choice(Kiss)
    return (dados)



Hug = [  "https://i.postimg.cc/NG8jfNpr/aharen-san-anime-hug.gif",   "https://i.postimg.cc/7YxYCgWt/engage-kiss-anime-hug.gif", "https://i.postimg.cc/MHY6PTvY/excited-hug.gif",   "https://i.postimg.cc/BQMZ2jWS/max-and-kaylee-profile-picture.gif",   "https://i.postimg.cc/1zgzmsj9/oshi-no-ko-aqua.gif",   "https://i.postimg.cc/hjTPmMn6/syno-i-love-you-syno.gif", "https://i.postimg.cc/0yLDpWm0/027e0ab608f8b84a25b2d2b1d223edec.gif", "https://i.postimg.cc/KYBLQPDS/bfb5bed89f8c09bf53eab687eb3f9404.gif", "https://i.postimg.cc/TY3VGWfg/d895581d84d5c54ea9dba84afb88b678.gif"
]



@app.route('/beez/hug', methods=['GET'])
def hug():
    dds = random.choice(Hug)
    return (dds)


@app.route('/team', methods=['GET'])
def team():
    team = "Essa api foi desenvolvida por parguin da beeZ Team! e feita para ajudar bots de entretenimento!, se quiser entrar na beeZ team entrar em contato! @parguin."
    return team


@app.route('/beez/job', methods=['GET'])
def job():
    job = [
    "Engenheiro de Software",
    "Médico Clínico Geral",
    "Professor de Matemática",
    "Advogado",
    "Designer Gráfico",
    "Psicólogo",
    "Arquiteto",
    "Analista de Dados",
    "Farmacêutico",
    "Enfermeiro",
    "Veterinário",
    "Desenvolvedor Web",
    "Técnico em Informática",
    "Eletricista",
    "Motorista",
    "Cozinheiro",
    "Garçom",
    "Pedreiro",
    "Mecânico",
    "Atendente de Loja",
    "Auxiliar Administrativo",
    "Engenheiro Civil",
    "Contador",
    "Dentista",
    "Nutricionista",
    "Fisioterapeuta",
    "Programador Backend",
    "Programador Frontend",
    "Cientista de Dados",
    "Redator",
    "Editor de Vídeo",
    "Fotógrafo",
    "Jornalista",
    "Publicitário",
    "Social Media",
    "Instrutor de Academia",
    "Esteticista",
    "Barbeiro",
    "Cabelereiro",
    "Tatuador",
    "Soldador",
    "Zelador",
    "Segurança",
    "Porteiro",
    "Empregada Doméstica",
    "Babá",
    "Jardineiro",
    "Marceneiro",
    "Carpinteiro",
    "Pintor",
    "Lavador de Carros",
    "Padeiro",
    "Confeiteiro",
    "Balconista",
    "Recepcionista",
    "Caixa de Supermercado",
    "Bombeiro",
    "Policial Militar",
    "Policial Civil",
    "Delegado",
    "Juiz",
    "Promotor de Justiça",
    "Militar do Exército",
    "Aeromoça",
    "Piloto de Avião",
    "Marinheiro",
    "Engenheiro Mecânico",
    "Engenheiro Elétrico",
    "Engenheiro Ambiental",
    "Geólogo",
    "Biólogo",
    "Químico",
    "Físico",
    "Matemático",
    "Astrônomo",
    "Historiador",
    "Geógrafo",
    "Filósofo",
    "Sociólogo",
    "Antropólogo",
    "Psicanalista",
    "Coach",
    "Consultor Empresarial",
    "Corretor de Imóveis",
    "Corretor de Seguros",
    "Trader",
    "Youtuber",
    "Streamer",
    "Influencer Digital",
    "Game Designer",
    "Tester de Jogos",
    "Animador 2D",
    "Animador 3D",
    "Modelador 3D",
    "Produtor Musical",
    "Cantor", 
    "Músico",
    "DJ",
    "Ator",
    "Atriz",
    "Dublador",
    "Roteirista",
    "Diretor de Cinema"
    ]
    Work = random.choice(job)
    return Work


if __name__ == '__main__':
    app.run(debug=True)
    
