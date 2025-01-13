import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    # Get address from clipboard.
    address = pyperclip.paste()

# Open the address in the browser using Google Maps.
webbrowser.open(f'https://www.google.com/maps?q={address}')
