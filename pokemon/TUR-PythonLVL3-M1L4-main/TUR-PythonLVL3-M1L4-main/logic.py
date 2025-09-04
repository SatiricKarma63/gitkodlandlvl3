import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random

class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.hp = random.randint(200, 400)
        self.starter = self.hp
        self.power = random.randint(30, 60)
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
                    return data['forms'][0]['name']  #  Pokémon adını döndürme
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür

    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()  # Henüz yüklenmemişse bir adın geri alınması
        return f"""Pokémonunuzun ismi: {self.name}
                Pokémonunuzun HP'si: {self.hp}
                Pokémonunuzun saldırı gücü: {self.power}
        """  # Pokémon adını içeren dizeyi döndürür

    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    img_url= data["sprites"]["front_default"]
                    return img_url
                else:
                    return None


    async def attack(self, enemy):
        if isinstance(enemy, Wizard):  # Düşmanın Wizard veri tipi olup olmadığının kontrol edilmesi (Sihirbaz sınıfının bir örneği midir?)
            chance = random.randint(1, 10)
            if chance == 1:
                return "Wizard Pokémon, savaşta bir kalkan kullanıldı!"
            else:
                return f"Wizard Pokémon,{self.hp} kadar canı kaldı!"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ne saldırdı\n@{enemy.pokemon_trainer}'nin sağlık durumu {enemy.hp}"
        else:
            enemy.hp = 0
            return f"""Pokémon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ni yendi!
            Pokémonlarınızın canları yeniden doldurmak için lütfen Pokémon merkezine gidiniz. {self.hp: }/{self.starter}"""
        


class Fighter(Pokemon):
    async def attack(self, enemy):
        super_attack = random.randint(5, 10)
        self.power += super_attack
        result = await super().attack(enemy)
        return result


class Wizard(Pokemon):
    #burayı biz dolduracağız ek görev
    None

if __name__ == '__main__':
    import asyncio
    wizard = Wizard("username1")
    fighter = Fighter("username2")
    print(asyncio.run(fighter.info()))
    print(asyncio.run(wizard.info()))
    print(asyncio.run(fighter.attack(wizard)))
    print(asyncio.run(wizard.info()))