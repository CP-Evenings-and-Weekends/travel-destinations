import csv


class DestinationInfo:
    def __init__(self, country, cost):
        self.country: str = country
        self.cost: int = cost

    def __str__(self):
        return f"{self.country}"


class TravelApp:

    def __init__(self):
        self.user_budget: int
        self.country_cost_data: list[DestinationInfo]
        self.user_destination: str

    def get_user_budget(self, input_func=input) -> None:
        budget: str = input_func("Enter your budget: ")
        self.user_budget = int(budget)

    def get_possible_destinations_based_on_budget(self) -> list[DestinationInfo]:
        return list(
            filter(
                lambda dest_info: self.user_budget >= dest_info.cost,
                self.country_cost_data,
            )
        )

    def display_confirmation_msg(self):
        print(f"You have chosen {self.user_destination}")

    def get_user_destination(self):
        self.user_destination = input(
            f"Choose one of {[str(dest) for dest in self.get_possible_destinations_based_on_budget()]}: "
        )

    def read_source_data(self):
        with open("data/destinations.csv", "r") as f:
            reader = csv.DictReader(f)
            self.country_cost_data = [
                DestinationInfo(
                    country=country_data["Country"], cost=int(country_data["Cost"])
                )
                for country_data in reader
            ]


if __name__ == "__main__":
    travel_app1 = TravelApp()
    travel_app1.user_budget = 1200
    travel_app1.read_source_data()
    # list_dest = travel_app1.get_possible_destinations_based_on_budget()
    travel_app1.get_user_destination()
    travel_app1.display_confirmation_msg()
