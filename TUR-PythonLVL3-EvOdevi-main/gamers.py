# "Gamer" sınıfının tanımı
# Görev 2. nickname alanını ekleyin
# Görev 3. email alanını ekleyin
class Gamer:
    def __init__(self, name, age, nickname, email):
        self.name = name
        self.age = age
        self.nickname = nickname
        self.email = email

        self.games = []

    def add_game(self, game):
        self.games.append(game)

    # Görev 4: Mesajı değiştirin
    def introduce(self):
        print(f"Merhaba, bana {self.name}, ve ben {self.age} yaşındayım. Bana {self.nickname} diye hitap edebilirsin ve eğer bana ulaşmak istersen, e-posta adresim: {self.email}.")


# Oyuncu sınıfının bir örneğini oluşturma
gamer1 = Gamer("Asil", 16, "SatiricKarma63", "asilturkekole@gmail.com")

# Oyunları ekleme
gamer1.add_game("Minecraft")
gamer1.add_game("League of Legends")

# Bir oyuncunun mini sunumu
gamer1.introduce()

# Favori oyunların çıktısının alınması
print(f"{gamer1.nickname} şu oyunları seviyor: {', '.join(gamer1.games)}")
