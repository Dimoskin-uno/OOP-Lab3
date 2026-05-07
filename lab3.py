class SeaBoat:
    def __init__(self, name: str, length: float, speed: float, capacity: int, year: int):
        self.__name = name
        self.__length = float(length)
        self.__speed = self.__validate_speed(speed)
        self.__capacity = int(capacity)
        self.__year = self.__validate_year(year)

    @staticmethod
    def __validate_speed(value: float) -> float:
        if value <= 0:
            raise ValueError(f"Швидкість має бути додатньою, отримано: {value}")
        return float(value)

    @staticmethod
    def __validate_year(value: int) -> int:
        if not (1800 <= value <= 2100):
            raise ValueError(f"Рік поза допустимим діапазоном: {value}")
        return int(value)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Назва не може бути порожньою")
        self.__name = value.strip()

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, value: float):
        self.__length = float(value)

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, value: float):
        self.__speed = self.__validate_speed(value)

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        self.__capacity = int(value)

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, value: int):
        self.__year = self.__validate_year(value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SeaBoat):
            return NotImplemented
        return (
            self.__name == other.__name
            and self.__length == other.__length
            and self.__speed == other.__speed
            and self.__capacity == other.__capacity
            and self.__year == other.__year
        )

    def __repr__(self) -> str:
        return (
            f"SeaBoat(name='{self.__name}', length={self.__length}, "
            f"speed={self.__speed}, capacity={self.__capacity}, year={self.__year})"
        )

class SeaFleet:
    """Клас-контейнер, що інкапсулює колекцію SeaBoat та всю логіку роботи з нею."""

    def __init__(self):
        self.__boats: list[SeaBoat] = []

    @property
    def boats(self) -> tuple[SeaBoat, ...]:
        """Повертає незмінну копію — зовні змінити список не можна."""
        return tuple(self.__boats)

    def add(self, boat: SeaBoat) -> None:
        if not isinstance(boat, SeaBoat):
            raise TypeError("Можна додавати лише об'єкти SeaBoat")
        self.__boats.append(boat)

    def remove(self, boat: SeaBoat) -> bool:
        try:
            self.__boats.remove(boat)
            return True
        except ValueError:
            return False

    def sort_by_length(self, descending: bool = False) -> None:
        """Сортування за довжиною (за зростанням), при рівності — за швидкістю (за спаданням)."""
        self.__boats.sort(key=lambda b: (b.length, -b.speed), reverse=descending)

    def sort_by_speed(self, descending: bool = True) -> None:
        """Сортування за швидкістю (за спаданням), при рівності — за довжиною."""
        self.__boats.sort(key=lambda b: (-b.speed, b.length) if descending else (b.speed, b.length))

    def find(self, target: SeaBoat) -> SeaBoat | None:
        """Повертає перший ідентичний об'єкт або None."""
        for boat in self.__boats:
            if boat == target:
                return boat
        return None

    def display(self, title: str = "Флот") -> None:
        print(f"\n{title}:")
        for boat in self.__boats:
            print(f"  {boat}")

    def __len__(self) -> int:
        return len(self.__boats)

    def __iter__(self):
        return iter(self.__boats)

    def __repr__(self) -> str:
        return f"SeaFleet({len(self.__boats)} boats)"

def main():
    fleet = SeaFleet()
    for data in [
        ("Odessa",   30.5, 45, 120, 2010),
        ("Neptune",  25.0, 60,  80, 2015),
        ("BlackSea", 40.2, 50, 200, 2008),
        ("Poseidon", 35.0, 55, 150, 2012),
        ("Atlantis", 28.7, 48, 100, 2018),
    ]:
        fleet.add(SeaBoat(*data))

    fleet.display("Початковий список")

    fleet.sort_by_length()
    fleet.display("Після сортування за довжиною ↑")

    fleet.sort_by_speed()
    fleet.display("Після сортування за швидкістю ↓")

    target = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
    result = fleet.find(target)
    print("\nПошук:")
    print(f"  {'Знайдено: ' + repr(result) if result else 'Не знайдено'}")

if __name__ == "__main__":
    main()
