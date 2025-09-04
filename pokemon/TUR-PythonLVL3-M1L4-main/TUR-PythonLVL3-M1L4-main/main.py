import discord
from discord.ext import commands
from config import token
from logic import Pokemon

# Bot için yetkileri/intents ayarlama
intents = discord.Intents.default()  # Varsayılan ayarların alınması
intents.messages = True              # Botun mesajları işlemesine izin verme
intents.message_content = True       # Botun mesaj içeriğini okumasına izin verme
intents.guilds = True                # Botun sunucularla çalışmasına izin verme

# Tanımlanmış bir komut önekine ve etkinleştirilmiş amaçlara sahip bir bot oluşturma
bot = commands.Bot(command_prefix='!', intents=intents)


class Pokemon:
    # Sınıf değişkeni - tüm pokemonları saklar
    pokemons = {}
    
    def __init__(self, owner):
        self.owner = owner
        self.name = "Pikachu"  # Varsayılan
        self.level = 5
        self.pokemon_id = 25  # Pikachu ID
        self.image_url = ""
        self.types = []
        pokemon = Pokemon.pokemons[owner] = self

    async def info(self):
        return f"İsim: {self.name}, Level: {self.level}, ID: {self.pokemon_id}, img: {await self.show_img()}"

    async def show_img(self):
        return "https://img.pokemondb.net/sprites/home/normal/pikachu.png"

# Bot çalışmaya hazır olduğunda tetiklenen bir olay
@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  # Botun adını konsola çıktı olarak verir

@bot.command()
async def pokemon_stats(ctx):
    pokemon_id = int(input("Pokemon ID girin:(1-1302)"))
    if pokemon_id in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[pokemon_id]
        await ctx.send(await pokemon.info())
    else:
        await ctx.send("Bu Pokemon listede yok!")

# '!go' komutu
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Mesaj yazarının adını alma
    # Kullanıcının zaten bir Pokémon'u olup olmadığını kontrol edin. Eğer yoksa, o zaman...
    if author not in Pokemon.pokemons.keys():
        pokemon = Pokemon(author)  # Yeni bir Pokémon oluşturma
        await ctx.send(await pokemon.info())  # Pokémon hakkında bilgi gönderilmesi
        image_url = await pokemon.show_img()  # Pokémon resminin URL'sini alma
        if image_url:
            embed = discord.Embed()  # Gömülü mesajı oluşturma
            embed.set_image(url=image_url)  # Pokémon'un görüntüsünün ayarlanması
            await ctx.send(embed=embed)  # Görüntü içeren gömülü bir mesaj gönderme
        else:
            await ctx.send("Pokémonun görüntüsü yüklenemedi!")
    else:
        await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")  # Bir Pokémon'un daha önce oluşturulup oluşturulmadığını gösteren bir mesaj
# Botun çalıştırılması
bot.run(token)
