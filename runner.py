from travel_app import TravelApp

if __name__ == "__main__":
    # Wire your own Source subclass in here once you've built it,
    # e.g.  app = TravelApp(CsvSource("data/destinations.csv"))
    app = TravelApp()
    app.read_source_data()
    app.get_user_budget()
    app.get_user_destination()
    app.display_confirmation_msg()