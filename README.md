# Travel Destinations

Congratulations on finishing your `TravelPackage` class in the lesson.  As often happens, you just got new requirements: the app needs to read source data from three different file formats — **CSV**, **JSON**, and **pickle** — and the choice of format should be swappable without rewriting the rest of the app.

To handle that, there's a new `Source` class.  Your job is to subclass it for each file type and let `TravelApp` use the right `Source` via composition.

## Requirements

1. **Pseudocode first.**  Open `pseudocode.txt` and sketch out, in plain English:
   - What classes you'll need
   - What each `Source` subclass needs to do differently
   - How `TravelApp` will use a `Source` (composition!)
   Don't write Python until this is done.

2. **Implement `Source`** in `Source.py` as a base class with a `read_file(path)` method.  All three file types live in `data/`.

3. **Implement three subclasses** of `Source`:
   - `CsvSource` — uses the built-in `csv` module
   - `JsonSource` — uses the built-in `json` module
   - `PickleSource` — uses the built-in `pickle` module

   Each should return the data as a list of dicts (or a list of `DestinationInfo` objects, your call).

4. **Wire `TravelApp` to use a `Source`.**  `TravelApp` should take any `Source` subclass instance in its constructor and call `read_file(...)` on it — no hard-coded format checks inside `TravelApp`.

5. **Run `runner.py`** with each of the three formats and confirm the same end behavior.

6. **Run `tests.py`** and add at least one test for each subclass.

## Things to think about
- Why is this a good fit for **composition** rather than inheritance from `TravelApp`?
- Where should error handling live — on `Source` (file open fails) or on `TravelApp` (data unusable)?
- If a fourth format showed up next week (e.g. XML), how much code would you change?  Ideally: only the new subclass.

## Stretch
- Add an `XmlSource` subclass using the built-in `xml.etree.ElementTree`.
- Add a factory method on `Source` (e.g. `Source.from_path(path)`) that picks the right subclass based on the file extension.
- Add a `cache` flag to `Source` so repeated `read_file()` calls don't re-read the same file.

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!
