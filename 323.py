class Pokupateli():
    def __init__(self, koli4estvopokupatelei, familiya, imya, ot4estvo, pasportniedannie, adres, gorod, vozrast, pol):
        self.koli4estvopokupatelei = koli4estvopokupatelei
        self.familiya = familiya
        self.imya = imya
        self.ot4estvo = ot4estvo
        self.pasportniedannie = pasportniedannie
        self.adres = adres
        self.gorod = gorod
        self.vozrast = vozrast
        self.pol = pol
          
    def izmenitkoli4estvopokupatelei(self, value):
        if isinstance(value, int):
            answer = self.koli4estvopokupatelei + value
        elif isinstance(value, str):
            answer = "nujno vvesti 4islo"
        else:
            answer = "error"
        print(answer)

s1 = Pokupateli(132, "Yands", "Alex", "Tenid", "-----", "dom12", "Omsk", 32, "mujskoy")
s2 = Pokupateli("200", "Melix", "Nekit", "Major", "-----", "dom13", "Moskva", "18", "mujskoy")
s3 = Pokupateli("56", "Otel", "Masha", "Rasha", "-----", "dom35", "Novosibirsk", "44", "jenskiy")
s4 = Pokupateli("51", "Ytea", "Pasha", "Dots", "-----", "dom41", "Novosibirsk", "67", "mujskoy")

s1.izmenitkoli4estvopokupatelei(100)
s2.izmenitkoli4estvopokupatelei("iphone")



