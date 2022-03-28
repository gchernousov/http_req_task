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
        most_intelligence_heroes = []
        intelligence_values = []
        for hero_int_value in superheroes_list:
            intelligence_values.append(int(hero_int_value.stats['intelligence']))
        max_intelligence_value = max(intelligence_values)
        for hero in superheroes_list:
            if hero.stats['intelligence'] == str(max_intelligence_value):
                most_intelligence_heroes.append(hero.hero_name)
        if len(most_intelligence_heroes) > 1:
            print(f'Самые умные супергерои: {", ".join(most_intelligence_heroes)}')
            print(f'Их уровень интеллекта равен {max_intelligence_value}')
        else:
            print(f'Самый умный супергерой: {"".join(most_intelligence_heroes)}')
            print(f'Его уровень интеллекта равен {max_intelligence_value}')

    def show_all_heroes(superheroes_list):
        for hero in superheroes_list:
            print(hero)


    superhero_01 = SuperHeroes('Hulk')
    superhero_02 = SuperHeroes('Captain America')
    superhero_03 = SuperHeroes('Thanos')
    superhero_04 = SuperHeroes('Professor X')
    superhero_05 = SuperHeroes('Iron Man')

    show_all_heroes(SuperHeroes.superheroes_list)

    show_most_intelligence_hero(SuperHeroes.superheroes_list)