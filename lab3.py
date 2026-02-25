class SeaBoat:
    def __init__(self, name, length, speed, capacity, year):
        self.name = name
        self.length = length
        self.speed = speed
        self.capacity = capacity
        self.year = year
    def __eq__(self, other):
        return (
            self.name == other.name and
            self.length == other.length and
            self.speed == other.speed and
            self.capacity == other.capacity and
            self.year == other.year
        )
    def __repr__(self):
        return (f"SeaBoat(name='{self.name}', length={self.length}, "
                f"speed={self.speed}, capacity={self.capacity}, year={self.year})")

def main():
    boats = [
        SeaBoat("Odessa", 30.5, 45, 120, 2010),
        SeaBoat("Neptune", 25.0, 60, 80, 2015),
        SeaBoat("BlackSea", 40.2, 50, 200, 2008),
        SeaBoat("Poseidon", 35.0, 55, 150, 2012),
        SeaBoat("Atlantis", 28.7, 48, 100, 2018)
    ]
    print("Початковий масив човнів:")
    for boat in boats:
        print(boat)

    boats.sort(key=lambda boat: (boat.length, -boat.speed))
    print("\nМасив після сортування (довжина за зростанням):")
    for boat in boats:
        print(boat)

    boats.sort(key=lambda boat: (-boat.speed, boat.length))
    print("\nМасив після сортування (швидкість за спаданням):")
    for boat in boats:
        print(boat)
    target_boat = SeaBoat("Poseidon", 35.0, 55, 150, 2012)
    print("\nПошук заданого об'єкта:")
    found = False

    for boat in boats:
        if boat == target_boat:
            print("Знайдено ідентичний об'єкт:")
            print(boat)
            found = True
            break
    if not found:
        print("Ідентичний об'єкт не знайдено.")
if __name__ == "__main__":
    main()
