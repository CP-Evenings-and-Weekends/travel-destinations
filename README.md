# Travel Package Source Data

## Description
Congratulations on finishing your TravelPackage class.  Unfortunately, as often happens, you just got new requirements.  You now need to be able to read three different file formats: csv, json and pkl.  

To handle this additional complexity, there is a new `Source` class that will handle all of that.

Take a look at the code to understand how everything is connected, then create appropriate subclasses of `Source` so that it is able to read those three file types (feel free to add more).  You should use composition to give TravelPackage access to the appropriate file-reading ability.

We will talk more about virtual environments later, but for now you can just run:
```bash
python -m venv venv
source venv/bin/activate
pip install pandas
```
to get access to the pandas library (already imported for you in `Source.py`.
