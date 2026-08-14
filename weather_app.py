import tkinter as tk
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta


# ==========================================
# LOAD API KEY FROM .ENV
# ==========================================

load_dotenv()

API_KEY = os.getenv("API_KEY")


# ==========================================
# GET WEATHER FUNCTION
# ==========================================

def get_weather():

    city = city_entry.get().strip()

    # Check empty input
    if city == "":
        show_error("Please enter a city")
        return

    # OpenWeather API URL
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:

        # Send request to API
        response = requests.get(url, timeout=10)

        # Convert response to JSON
        data = response.json()

        # ==========================================
        # SUCCESSFUL RESPONSE
        # ==========================================

        if response.status_code == 200:

            # --------------------------------------
            # BASIC WEATHER DATA
            # --------------------------------------

            city_name = data["name"]

            country = data["sys"]["country"]

            temperature_value = data["main"]["temp"]

            feels_like_value = data["main"]["feels_like"]

            humidity_value = data["main"]["humidity"]

            weather_description = data["weather"][0]["description"]

            wind_speed = data["wind"]["speed"]

            # --------------------------------------
            # SUNRISE / SUNSET DATA
            # --------------------------------------

            sunrise_timestamp = data["sys"]["sunrise"]

            sunset_timestamp = data["sys"]["sunset"]

            # Timezone offset of the city
            timezone_offset = data["timezone"]

            # Convert UTC timestamp to city's local time
            city_timezone = timezone(timedelta(seconds=timezone_offset))

            sunrise_time = datetime.fromtimestamp(
                sunrise_timestamp,
                timezone.utc
            ).astimezone(city_timezone)

            sunset_time = datetime.fromtimestamp(
                sunset_timestamp,
                timezone.utc
            ).astimezone(city_timezone)

            # Format time
            sunrise = sunrise_time.strftime("%I:%M %p")

            sunset = sunset_time.strftime("%I:%M %p")

            # ==========================================
            # UPDATE WEATHER CARD
            # ==========================================

            result_city.config(
                text=city_name
            )

            country_label.config(
                text=f"📍 {country}"
            )

            temperature.config(
                text=f"{temperature_value:.1f}°C"
            )

            feels_like.config(
                text=f"Feels like {feels_like_value:.1f}°C"
            )

            condition.config(
                text=f"☁️ {weather_description.title()}"
            )

            humidity.config(
                text=f"💧 Humidity\n{humidity_value}%"
            )

            wind.config(
                text=f"💨 Wind\n{wind_speed} m/s"
            )

            sunrise_label.config(
                text=f"🌅 Sunrise\n{sunrise}"
            )

            sunset_label.config(
                text=f"🌇 Sunset\n{sunset}"
            )


        # ==========================================
        # CITY NOT FOUND
        # ==========================================

        elif response.status_code == 404:

            show_error("City not found")

        # ==========================================
        # INVALID API KEY
        # ==========================================

        elif response.status_code == 401:

            show_error("Invalid API key")

        # ==========================================
        # OTHER API ERROR
        # ==========================================

        else:

            show_error("Unable to get weather")


    # ==========================================
    # INTERNET / REQUEST ERROR
    # ==========================================

    except requests.exceptions.RequestException:

        show_error("Connection Error")


# ==========================================
# ERROR DISPLAY FUNCTION
# ==========================================

def show_error(message):

    result_city.config(
        text=message
    )

    country_label.config(
        text="📍 --"
    )

    temperature.config(
        text="--°C"
    )

    feels_like.config(
        text="Feels like --°C"
    )

    condition.config(
        text="⚠️ Please try again"
    )

    humidity.config(
        text="💧 Humidity\n--"
    )

    wind.config(
        text="💨 Wind\n--"
    )

    sunrise_label.config(
        text="🌅 Sunrise\n--"
    )

    sunset_label.config(
        text="🌇 Sunset\n--"
    )


# ==========================================
# CLEAR FUNCTION
# ==========================================

def clear_weather():

    # Clear city input
    city_entry.delete(
        0,
        tk.END
    )

    # Reset weather information
    result_city.config(
        text="Enter a city"
    )

    country_label.config(
        text="📍 --"
    )

    temperature.config(
        text="--°C"
    )

    feels_like.config(
        text="Feels like --°C"
    )

    condition.config(
        text="🌤️ Weather"
    )

    humidity.config(
        text="💧 Humidity\n--"
    )

    wind.config(
        text="💨 Wind\n--"
    )

    sunrise_label.config(
        text="🌅 Sunrise\n--"
    )

    sunset_label.config(
        text="🌇 Sunset\n--"
    )

    # Put cursor back into input box
    city_entry.focus()


# ==========================================
# CREATE MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title("Weather App")

window.geometry("500x850")

window.resizable(False, False)

window.configure(
    bg="#E3F2FD"
)


# ==========================================
# HEADER
# ==========================================

header = tk.Frame(
    window,
    bg="#1976D2",
    height=200
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


# ==========================================
# WEATHER ICON
# ==========================================

icon = tk.Label(
    header,
    text="🌤️",
    font=("Arial", 45),
    bg="#1976D2",
    fg="white"
)

icon.pack(
    pady=(20, 0)
)


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    header,
    text="Weather App",
    font=("Arial", 28, "bold"),
    bg="#1976D2",
    fg="white"
)

title.pack()


# ==========================================
# SUBTITLE
# ==========================================

subtitle = tk.Label(
    header,
    text="Check the weather of any city",
    font=("Arial", 12),
    bg="#1976D2",
    fg="#E3F2FD"
)

subtitle.pack(
    pady=(5, 15)
)


# ==========================================
# SEARCH SECTION
# ==========================================

search_frame = tk.Frame(
    window,
    bg="#E3F2FD"
)

search_frame.pack(
    pady=25
)


# ==========================================
# ENTER CITY LABEL
# ==========================================

city_label = tk.Label(
    search_frame,
    text="Enter City",
    font=("Arial", 13, "bold"),
    bg="#E3F2FD",
    fg="#1565C0"
)

city_label.pack(
    anchor="w"
)


# ==========================================
# CITY INPUT
# ==========================================

city_entry = tk.Entry(
    search_frame,
    font=("Arial", 16),
    width=27,
    bd=2,
    relief="solid"
)

city_entry.pack(
    pady=8
)


# ==========================================
# BUTTON FRAME
# ==========================================

button_frame = tk.Frame(
    search_frame,
    bg="#E3F2FD"
)

button_frame.pack(
    pady=8
)


# ==========================================
# SEARCH BUTTON
# ==========================================

search_button = tk.Button(
    button_frame,
    text="🔍  Search",
    font=("Arial", 12, "bold"),
    bg="#1565C0",
    fg="white",
    activebackground="#0D47A1",
    activeforeground="white",
    width=13,
    height=2,
    bd=0,
    cursor="hand2",
    command=get_weather
)

search_button.grid(
    row=0,
    column=0,
    padx=5
)


# ==========================================
# CLEAR BUTTON
# ==========================================

clear_button = tk.Button(
    button_frame,
    text="🧹  Clear",
    font=("Arial", 12, "bold"),
    bg="#757575",
    fg="white",
    activebackground="#555555",
    activeforeground="white",
    width=13,
    height=2,
    bd=0,
    cursor="hand2",
    command=clear_weather
)

clear_button.grid(
    row=0,
    column=1,
    padx=5
)


# ==========================================
# WEATHER RESULT CARD
# ==========================================

weather_card = tk.Frame(
    window,
    bg="white",
    width=420,
    height=400
)

weather_card.pack(
    pady=5
)

weather_card.pack_propagate(False)


# ==========================================
# CITY NAME
# ==========================================

result_city = tk.Label(
    weather_card,
    text="Enter a city",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="#1565C0"
)

result_city.pack(
    pady=(15, 2)
)


# ==========================================
# COUNTRY
# ==========================================

country_label = tk.Label(
    weather_card,
    text="📍 --",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#666666"
)

country_label.pack(
    pady=(0, 8)
)


# ==========================================
# TEMPERATURE
# ==========================================

temperature = tk.Label(
    weather_card,
    text="--°C",
    font=("Arial", 40, "bold"),
    bg="white",
    fg="#FF9800"
)

temperature.pack()


# ==========================================
# FEELS LIKE
# ==========================================

feels_like = tk.Label(
    weather_card,
    text="Feels like --°C",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#555555"
)

feels_like.pack(
    pady=(0, 5)
)


# ==========================================
# WEATHER CONDITION
# ==========================================

condition = tk.Label(
    weather_card,
    text="🌤️ Weather",
    font=("Arial", 15),
    bg="white",
    fg="#555555"
)

condition.pack(
    pady=5
)


# ==========================================
# WEATHER DETAILS FRAME
# ==========================================

details_frame = tk.Frame(
    weather_card,
    bg="white"
)

details_frame.pack(
    pady=8
)


# ==========================================
# HUMIDITY
# ==========================================

humidity = tk.Label(
    details_frame,
    text="💧 Humidity\n--",
    font=("Arial", 11, "bold"),
    bg="#E3F2FD",
    fg="#1565C0",
    width=14,
    height=3
)

humidity.grid(
    row=0,
    column=0,
    padx=5
)


# ==========================================
# WIND
# ==========================================

wind = tk.Label(
    details_frame,
    text="💨 Wind\n--",
    font=("Arial", 11, "bold"),
    bg="#FFF3E0",
    fg="#EF6C00",
    width=14,
    height=3
)

wind.grid(
    row=0,
    column=1,
    padx=5
)


# ==========================================
# SUN INFORMATION FRAME
# ==========================================

sun_frame = tk.Frame(
    weather_card,
    bg="white"
)

sun_frame.pack(
    pady=5
)


# ==========================================
# SUNRISE
# ==========================================

sunrise_label = tk.Label(
    sun_frame,
    text="🌅 Sunrise\n--",
    font=("Arial", 11, "bold"),
    bg="#FFF8E1",
    fg="#F57C00",
    width=14,
    height=3
)

sunrise_label.grid(
    row=0,
    column=0,
    padx=5
)


# ==========================================
# SUNSET
# ==========================================

sunset_label = tk.Label(
    sun_frame,
    text="🌇 Sunset\n--",
    font=("Arial", 11, "bold"),
    bg="#FCE4EC",
    fg="#C2185B",
    width=14,
    height=3
)

sunset_label.grid(
    row=0,
    column=1,
    padx=5
)


# ==========================================
# PRESS ENTER TO SEARCH
# ==========================================

city_entry.bind(
    "<Return>",
    lambda event: get_weather()
)


# ==========================================
# START WITH CURSOR IN INPUT
# ==========================================

city_entry.focus()


# ==========================================
# RUN APPLICATION
# ==========================================

window.mainloop()