import requests

class SuperHeroes:

    superheroes_list = []

    def __init__(self, hero_name):
        self.hero_name = hero_name
        self.id_ = self.get_superhero_id()
        self.stats = self.get_superhero_stats()
        SuperHeroes.superheroes_list.append(self)

    def get_superhero_id(self):
        url = 'https://superheroapi.com/api/2619421814940190/search/'
        url_for_search = url + self.hero_name
        response = requests.get(url_for_search)
        response.raise_for_status()
        for id_ in response.json()['results']:
            return id_['id']
            break

    def get_superhero_stats(self):
        url = 'https://superheroapi.com/api/2619421814940190/'
        url_for_search = url + self.id_
        response = requests.get(url_for_search)
        response.raise_for_status()
        return response.json()['powerstats']

    def __str__(self):
        superhero_info = f'Имя: {self.hero_name}\n' \
                         f'id: {self.id_}\n' \
                         f'ХАРАКТЕРИСТИКИ:\n' \
                         f'\tИнтеллект: {self.stats["intelligence"]}\n' \
                         f'\tСила: {self.stats["strength"]}\n' \
                         f'\tСкорость: {self.stats["speed"]}\n' \
                         f'\tВыносливость: {self.stats["durability"]}\n' \
                         f'\tМощь: {self.stats["power"]}\n' \
                         f'\tБоевые навыки: {self.stats["combat"]}\n'
        return superhero_info


if __name__ == '__main__':

    def show_most_intelligence_hero(superheroes_list):
        max_intelligence = 0
        most_intelligence_hero = ''
        for hero in superheroes_list:
            if max_intelligence < int(hero.stats['intelligence']):
                max_intelligence = int(hero.stats['intelligence'])
                most_intelligence_hero = hero.hero_name
        print(f'\nСамый умный супергерой -- {most_intelligence_hero}, его интеллект равен {max_intelligence}\n')


    superhero_01 = SuperHeroes('Hulk')
    superhero_02 = SuperHeroes('Captain America')
    superhero_03 = SuperHeroes('Thanos')

    # Общая информация об имеющихся супергероях:
    print(superhero_01)
    print(superhero_02)
    print(superhero_03)

    show_most_intelligence_hero(SuperHeroes.superheroes_list)