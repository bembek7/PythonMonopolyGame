Dokumentacja projektu Monopoly
Struktura projekt:
Stworzyłem 14 klas:

Plik Player:
Player - klasa gracza zawierająca metody potrzebne do zarządzania graczem jego gotówką i otrzymywania jego własności.

Plik Property:
Property - klasa posiadłości zawierająca metody potrzebne do zarządzania posiadłością i jego własnościami.
TypicalProperty - klasa dziedzicząca po klasie Property przedstawiająca typową posiadłość w Monopoly taką, która ma kolor i, na której można stawiać domki, czy hotele.
SpecialProperty - abstrakcyjna klasa dziedzicząca po klasie Property dodająca atrybut type, potrzebny w opisanych niżej klasach AirportProperty i DiceChargeProperty.
AirportProperty - klasa dziedzicząca po klasie SpecialProperty, która zmienia sposób płatności podczas wejścia na pole i opłata jest teraz zależna od ilości posiadanych przez gracza pól tego typu.
DiceChargeProperty - klasa dziedzicząca po klasie SpecialProperty, która zmienia sposób płatności podczas wejścia na pole i opłata jest teraz mnożona przez wynik na kostce danego gracza i dzielona przez 2 zależnie od ilości posiadanych przez gracza pól tego typu.

Plik Field:
Field - klasa reprezentująca pole na planszy, zawierająca nazwę i pozycję oraz metodę action, która wywoływana jest gdy gracz stanie na danym polu.
PropertyField - klasa dziedzicząca po klasie Field, reprezentująca pole na planszy, na którym znajduje się posiadłość. Przez nią gracz kupuje posiadłości i jej akcja ściąga opłatę za pole z gracza, który na nim stanął.
DiceChargePropertyField - klasa z dziedzicząca po klasie PropertyField, robiąca to samo tylko zamiast TypicalProperty lub AirportProperty trzyma DiceChargeProperty.
ChanceField - klasa dziedzicząca po klasie Field jej metoda akcji przyjmuje kwotę i zabiera lub daję ją graczowi (jeśli dostanie ujemną zabiera).
PayField - klasa dziedzicząca po klasie Field, gdy gracz stanie na te pole płaci określoną w konstruktorze kwotę.
GoToJailField - klasa dziedzicząca po klasie Field, gdy gracz stanie na te pole idzie do więzienia.

Plik Game:
Game - klasa reprzentująca grę zawiera metody takie jak sprzedawanie posiadłości innym graczom, oraz trzyma informacje generalne na temat gry takie jak tablica z graczami, cena wykupu z więzienia, plansza.

Plik GUI:
MainWindow - klasa głownego okna, zawiera metody i atrybuty potrzebne do obsługi GUI i logiki gry ściśle z nim związanym.

Atrybuty oraz metody klas są dokładniej opisane w kodzie w docstringach.

Plik Dice - znajduję tam się metoda losująca wynik rzutu kostką.

Plik Main - tworzy się tam obiekt klasy Game i przez niego uruchamia się program.

Program uruchamiamy uruchamiając plik Main, wtedy wyświetli nam się okno dodawania graczy i wyboru liczby rund, gdy dodamy przynajmniej dwóch graczy dostępny stanie się przycisk gry, który zmienia planszę już na naszą główną grę z planszą i innymi informacjami. Przy użyciu interfejsu możemy sprzedawać i kupować domki, zastawiać i wykupować posiadłości, jak i handlować między graczami. Gdy wszyscy gracze się poddadzą ,są do tego zmuszeni jeśli nie mają gotówki (nie mogą skończyć tury mając długi) lub mogą to zrobić dobrowolnie, lub skończy się określona wcześniej liczba rund, plansza zmieni się i ogłosi zwycięzce.



