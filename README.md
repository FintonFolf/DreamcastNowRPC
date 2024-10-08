# DreamcastNowRPC

A simple Discord Rich Presence appication for Dreamcast Now!

## Prerequisites
- Python 3.8 or later
- `requests` library for making HTTP requests
- `pypresence` library for Discord Rich Presence integration

## Installation
1. Clone the GitHub repository and navigate to the project directory
2. Install the required python packages  
```pip install requests pypresence```
3. Open the script and locate the `primaryUsername` variable  
```primaryUsername = "Your-Dreacast-Now!-username"```  
Replace `Your-Dreacast-Now!-username` with your Dreamcast Now! username.
- If you have a secondary Dreamcast Now! username you may wish to enter a value for the  `secondaryUsername` variable.
## Usage
1. Run the script  
```python DreamcastNowRPC.py```
2. Your Discord status should now display your current Dreamcast game from the Dreamcast Now! website.

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

# Credits
- [Dreamcast Now!](https://dreamcast.online/now/) for the Dreamcast Now! API
