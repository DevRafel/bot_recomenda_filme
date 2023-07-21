import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = '586988b442944988a3b2e3830a19e754'
analyzer = SentimentIntensityAnalyzer()


def suggest_movies(i):
    phrase = i
    emotion = analyzer.polarity_scores(phrase)['compound']

    if emotion <= -0.5:
        genre = "18"  # Drama
    elif emotion < 0:
        genre = "35"  # Comedia
    elif emotion < 0.5:
        genre = "10749"  # romance
    else:
        genre = "27"  # horror

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genre}&vote_count.gte=4"
    response = requests.get(url).json()


    if response['results']:
        # pegando os titulos dos filmes
        titles = [result['title'] for result in response['results'][:3]]

        # pegando as datas dos filmes
        release_date = [result['release_date'] for result in response['results'][:3]]

        # pegando os votos dos filmes
        vote_average = [result['vote_average'] for result in response['results'][:3]]

        # pegando os posters dos filmesl
        # definindo a string do prefix
        prefix = "https://www.themoviedb.org/t/p/w220_and_h330_face/xxPXsL8V95dTwL5vHWIIQALkJQS.jpg"

        # concatenar o prefix com o caminho da imagem do link
        poster_path = [prefix + result['poster_path'].lstrip('/') for result in response['results'][:3]]

        # retornando os resultados como uma lista
        return [titles, poster_path, release_date, vote_average]



