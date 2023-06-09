ENG, scroll down for PL version
The final version is the last commit of the Monopoly Project Documentation. Project structure: I created 14 classes:

File Player: Player - a player class containing methods necessary for managing the player, their cash, and receiving their properties.

File Property: Property - a property class containing methods necessary for managing the property and its ownership. TypicalProperty - a class inheriting from the Property class, representing a typical property in Monopoly, which has a color and can have houses or hotels built on it. SpecialProperty - an abstract class inheriting from the Property class, adding the attribute "type" needed in the classes described below: AirportProperty and DiceChargeProperty. AirportProperty - a class inheriting from the SpecialProperty class, which changes the payment method when entering the field, and the fee now depends on the number of properties of this type owned by the player. DiceChargeProperty - a class inheriting from the SpecialProperty class, which changes the payment method when entering the field, and the fee is now multiplied by the player's dice roll result and divided by 2, depending on the number of properties of this type owned by the player.

File Field: Field - a class representing a square on the board, containing its name and position, and the action method, which is called when a player lands on that square. PropertyField - a class inheriting from the Field class, representing a square on the board where a property is located. The player buys properties through this class, and its action deducts the rent from the player who landed on it. DiceChargeField - a class inheriting from the PropertyField class, doing the same as before, but instead of TypicalProperty or AirportProperty, it holds a DiceChargeProperty. ChanceField - a class inheriting from the Field class, its action method takes an amount and deducts or adds it to the player (if it receives a negative amount, it deducts). PayField - a class inheriting from the Field class, when a player lands on this square, they pay a specified amount defined in the constructor. GoToJailField - a class inheriting from the Field class, when a player lands on this square, they go to jail.

File Game: Game - a class representing the game, contains methods such as selling properties to other players and holds general information about the game, such as an array of players, jail bailout price, and the board.

File GUI: MainWindow - a class representing the main window, contains methods and attributes necessary for handling the GUI and the closely related game logic.

The attributes and methods of the classes are described in more detail in the code's docstrings.

File Dice - it contains a method for generating a random dice roll result.

File Main - an instance of the Game class is created there, and the program is executed through it.

To run the program, execute the Main file, which will display a window for adding players and selecting the number of rounds. Once you add at least two players, the game button becomes available, which switches the board to the main game view with the board and other information. Using the interface, you can buy and sell houses, mortgage and redeem properties, and trade between players. When all players surrender, either forcibly (if they have no cash and cannot finish their turn with debts) or voluntarily, or when a predetermined number of rounds is completed, the board changes, and the winner is announced. The last commit is the final version that should be run.

PL
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
DiceChargeField - klasa dziedzicząca po klasie PropertyField, robiąca to samo tylko zamiast TypicalProperty lub AirportProperty trzyma DiceChargeProperty.
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
Ostatni commit jest wersją ostateczną, którą powinno się uruchamiać



