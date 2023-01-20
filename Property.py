class Property:
    """
    A base class to represent a property.

    ...

    Attributes
    ----------
    name : str
        name of the property
    basic_charge : int
        charge of the property
    owner : Player
        owner of the property, none if there is no owner
    price : int
        price of the property
    active : bool
        if property is active

    Methods
    -------
    free():
        sets owner to None and activate property
    charge():
        returns basic charge or 0 depending if property is active
    other are obvious
    """

    def __init__(self, name, basic_charge, price) -> None:
        self._name = name
        self._basic_charge = basic_charge
        self._owner = None
        self._price = price
        self._active = True

    def free(self):
        self._owner = None
        self._active = True

    def is_active(self):
        return self._active

    def deactivate(self):
        self._active = False

    def activate(self):
        self._active = True

    def __str__(self) -> str:
        return self._name

    def get_owner(self):
        return self._owner

    def set_owner(self, player):
        self._owner = player

    def get_name(self):
        return self._name

    def charge(self):
        if self._active:
            return self._basic_charge
        else:
            return 0

    def get_price(self):
        return self._price


class TypicalProperty(Property):
    """
    A class to represent a typical monopoly property.
    Inherits from Property class.

    ...

    Attributes
    ----------
    name : str
        name of the property
    basic_charge : int
        charge of the property
    owner : Player
        owner of the property, none if there is no owner
    price : int
        price of the property
    active : bool
        if property is active
    color : string
        color of the property
    apartment_price : int
        price of apartments that can be build on this property

    Methods
    -------
    free():
        sets owner to None and activate property, and sets nr of aparts to 0
    charge():
        returns basic charge multiplied accordingly to apartments number
    other are obvious
    """
    def __init__(self, name, basic_charge, price, color, apart_price) -> None:
        super().__init__(name, basic_charge, price)
        self._color = color
        self._aparts = 1  # 6 = hotel
        self._apart_price = apart_price

    def free(self):
        super().free()
        self._aparts = 1

    def get_color(self):
        return self._color

    def get_apartment(self):
        if self._aparts < 6:
            self._aparts += 1

    def lose_apartment(self):
        if self._aparts > 1:
            self._aparts -= 1

    def get_apartments_nr(self):
        return self._aparts - 1

    def get_apartment_price(self):
        return self._apart_price

    def charge(self):
        if self._active:
            return self._basic_charge * self._aparts * self._apart_price / 50
        else:
            return 0


class SpecialProperty(Property):
    """
    A class to represent a special property inheriting from Property class.

    ...

    Attributes
    ----------
    name : str
        name of the property
    basic_charge : int
        charge of the property
    owner : Player
        owner of the property, none if there is no owner
    price : int
        price of the property
    active : bool
        if property is active
    type : string
        type of the property

    Methods
    -------
    free():
        sets owner to None and activate property
    charge():
        returns basic charge or 0 depending if property is active
    get_type():
        returns type of the property
    other are obvious
    """
    def __init__(self, name, basic_charge, price, type) -> None:
        super().__init__(name, basic_charge, price)
        self._type = type

    def get_type(self):
        return self._type


class AirportProperty(SpecialProperty):
    """
    A class to represent an airport type of property.
    Inherits from SpecialProperty class.

    ...

    Attributes
    ----------
    name : str
        name of the property
    basic_charge : int
        charge of the property
    owner : Player
        owner of the property, none if there is no owner
    price : int
        price of the property
    active : bool
        if property is active
    type : string
        type of the property

    Methods
    -------
    free():
        sets owner to None and activate property
    charge():
        returns charge multiplied accordingly to number of airports of owner
    get_type():
        returns type of the property
    other are obvious
    """
    def charge(self):
        if self._active:
            owning_other = self._owner.get_amount_of_type(self._type)
            if owning_other == 3:
                owning_other = 4
            elif owning_other == 4:
                owning_other = 8
            return self._basic_charge * owning_other
        else:
            return 0


class DiceChargeProperty(SpecialProperty):
    """
    A class to represent a dice charge type of property.
    Inherits from SpecialProperty class.

    ...

    Attributes
    ----------
    name : str
        name of the property
    basic_charge : int
        charge of the property
    owner : Player
        owner of the property, none if there is no owner
    price : int
        price of the property
    active : bool
        if property is active
    type : string
        type of the property

    Methods
    -------
    free():
        sets owner to None and activate property
    charge():
        returns charge multiplied by dice result of currently moving player
        divided by two or not if owner has two of them or not.
    get_type():
        returns type of the property
    other are obvious
    """
    def charge(self, dice_result):
        if self._active:
            owning_other = self._owner.get_amount_of_type(self._type)
            if owning_other == 2:
                charge = self._basic_charge * dice_result
            else:
                charge = round(self._basic_charge * dice_result / 2)
            return charge
        else:
            return 0
