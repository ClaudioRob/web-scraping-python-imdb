import scrapy
import json

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    alloewd_domais = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):

        raw_data = response.css("script[id='__NEXT_DATA__']::text").get()
        json_data = json.loads(raw_data)
        need_data = json_data['props']['pageProps']['pageData']['chartTitles']['edges']

        for movie in need_data:
            yield{
                'title': movie['node']['titleText']['text'],
                'movie_rank': movie['currentRank'],
                'release_yaer': movie['node']['releaseYear']['year'],
                'movie_length': movie['node']['runtime']['seconds'],
                'rating': movie['node']['ratingSumary']['aggregateRating'],
                'vout_count': movie['node']['RatingsSumary']['voteCount'],
                'description': movie['node']['plot']['plotText']['plainText']
            }
                                                    
        pass
