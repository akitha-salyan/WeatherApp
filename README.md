# 🌤️ Weather App

A simple and colorful desktop Weather Application built using **Python and Tkinter**.  
The application uses the **OpenWeatherMap API** to fetch real-time weather information for any city.

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Current temperature
- 🤗 Feels-like temperature
- ☁️ Weather condition
- 💧 Humidity
- 💨 Wind speed
- 📍 Country information
- 🌅 Sunrise time
- 🌇 Sunset time
- 🧹 Clear button
- ⌨️ Press Enter to search
- ⚠️ Error handling for invalid cities
- 🌐 Internet connection error handling
- 🔐 API key protected using `.env`

## 🛠️ Technologies Used

- **Python**
- **Tkinter** – GUI development
- **Requests** – API requests
- **python-dotenv** – Environment variable management
- **OpenWeatherMap API** – Real-time weather data

## 📂 Project Structure

```text
WeatherApp/
│
├── weather_app.py
├── .env
├── .gitignore
├── README.md

.env contains the API key and is excluded from GitHub using .gitignore.

⚙️ Installation
1. Clone the repository
    git clone https://github.com/akitha-salyan/WeatherApp.git
2. Open the project folder
    cd WeatherApp
3. Install required packages
    pip install requests python-dotenv

🔑 API Key Setup
This project uses the OpenWeatherMap API.
Create a file named:
    .env
Inside the .env file, add:
API_KEY=YOUR_API_KEY
Replace YOUR_API_KEY with your own OpenWeatherMap API key.
⚠️ Never upload your .env file to GitHub.

▶️ Run the Application
Run:
python weather_app.py
The Weather App window will open.

Enter a city name, for example:
EX:Mangalore
Then click 🔍 Search.
You can also press Enter to search.

🌦️ Weather Information
The application displays:
Information	Description
🌡️ Temperature	Current temperature
🤗 Feels Like	Perceived temperature
☁️ Weather Condition	Current weather condition
💧 Humidity	Humidity percentage
💨 Wind	Wind speed
📍 Country	Country code
🌅 Sunrise	Sunrise time
🌇 Sunset	Sunset time
🔐 Security

The API key is stored in a .env file instead of being written directly in the Python code.

The .env file is added to .gitignore, so the API key is not uploaded to GitHub.

🚀 Future Improvements
🧭 Wind direction
🌤️ Weather-specific icons
🌙 Dark and light themes
📅 5-day weather forecast
🌡️ Celsius / Fahrenheit selection
📍 Automatic location detection
📊 Weather history
👩‍💻 Author


```text
Akitha Salyan
MCA Student | Python | Web Development | IoT
