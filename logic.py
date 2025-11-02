from datetime import datetime, timedelta
from random import randint
import requests

class Pokemon:
    pokemons = {}  # { username : pokemon }

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = randint(30, 60)
        self.hp = randint(200, 400)
        self.last_feed_time = datetime.now() - timedelta(seconds=9999)
        Pokemon.pokemons[pokemon_trainer] = self

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']["other"]['official-artwork']["front_default"]
        return "https://static.wikia.nocookie.net/anime-characters-fight/images/7/77/Pikachu.png"

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        return "Pikachu"

    def info(self):
        return f"""Имя покемона: {self.name}
Сила: {self.power}
Здоровье: {self.hp}"""

    def show_img(self):
        return self.img

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            if randint(1, 5) == 1:
                return "Покемон-волшебник применил щит"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\nЗдоровье @{enemy.pokemon_trainer} теперь {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_train_
