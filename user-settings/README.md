# User Settings

A case-insensitive settings to store four functions to add, update, delete and
view key-value settings held in a dictionary.
## Run it

```bash
python settings.py
```

## Sample output

```
Current User Settings:
Brightness: high
Zoom: out
Contrast: small

Setting 'volume' added with value 'loud' successfully!
Setting 'brightness' already exists! Cannot add a new setting with this name.
Setting 'brightness' updated to 'low' successfully!
Setting 'contrast' deleted successfully!

Current User Settings:
Brightness: low
Zoom: out
Volume: loud
```

## Tests

```bash
pytest test_settings.py
```
