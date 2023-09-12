"""Constant values for the AEMET OpenData component."""
from __future__ import annotations

from aemet_opendata.const import (
    AOD_COND_CLEAR_NIGHT,
    AOD_COND_CLOUDY,
    AOD_COND_FOG,
    AOD_COND_LIGHTNING,
    AOD_COND_LIGHTNING_RAINY,
    AOD_COND_PARTLY_CLODUY,
    AOD_COND_POURING,
    AOD_COND_RAINY,
    AOD_COND_SNOWY,
    AOD_COND_SUNNY,
)

from homeassistant.components.weather import (
    ATTR_CONDITION_CLEAR_NIGHT,
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_LIGHTNING,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SUNNY,
)
from homeassistant.const import Platform

ATTRIBUTION = "Powered by AEMET OpenData"
CONF_STATION_UPDATES = "station_updates"
PLATFORMS = [Platform.SENSOR, Platform.WEATHER]
DEFAULT_NAME = "AEMET"
DOMAIN = "aemet"
ENTRY_NAME = "name"
ENTRY_WEATHER_COORDINATOR = "weather_coordinator"

ATTR_API_CONDITION = "condition"
ATTR_API_FORECAST_CONDITION = "condition"
ATTR_API_FORECAST_DAILY = "forecast-daily"
ATTR_API_FORECAST_HOURLY = "forecast-hourly"
ATTR_API_FORECAST_PRECIPITATION = "precipitation"
ATTR_API_FORECAST_PRECIPITATION_PROBABILITY = "precipitation_probability"
ATTR_API_FORECAST_TEMP = "temperature"
ATTR_API_FORECAST_TEMP_LOW = "templow"
ATTR_API_FORECAST_TIME = "datetime"
ATTR_API_FORECAST_WIND_BEARING = "wind_bearing"
ATTR_API_FORECAST_WIND_MAX_SPEED = "wind_max_speed"
ATTR_API_FORECAST_WIND_SPEED = "wind_speed"
ATTR_API_HUMIDITY = "humidity"
ATTR_API_PRESSURE = "pressure"
ATTR_API_RAIN = "rain"
ATTR_API_RAIN_PROB = "rain-probability"
ATTR_API_SNOW = "snow"
ATTR_API_SNOW_PROB = "snow-probability"
ATTR_API_STATION_ID = "station-id"
ATTR_API_STATION_NAME = "station-name"
ATTR_API_STATION_TIMESTAMP = "station-timestamp"
ATTR_API_STORM_PROB = "storm-probability"
ATTR_API_TEMPERATURE = "temperature"
ATTR_API_TEMPERATURE_FEELING = "temperature-feeling"
ATTR_API_TOWN_ID = "town-id"
ATTR_API_TOWN_NAME = "town-name"
ATTR_API_TOWN_TIMESTAMP = "town-timestamp"
ATTR_API_WIND_BEARING = "wind-bearing"
ATTR_API_WIND_MAX_SPEED = "wind-max-speed"
ATTR_API_WIND_SPEED = "wind-speed"

CONDITIONS_MAP = {
    AOD_COND_CLEAR_NIGHT: ATTR_CONDITION_CLEAR_NIGHT,
    AOD_COND_CLOUDY: ATTR_CONDITION_CLOUDY,
    AOD_COND_FOG: ATTR_CONDITION_FOG,
    AOD_COND_LIGHTNING: ATTR_CONDITION_LIGHTNING,
    AOD_COND_LIGHTNING_RAINY: ATTR_CONDITION_LIGHTNING_RAINY,
    AOD_COND_PARTLY_CLODUY: ATTR_CONDITION_PARTLYCLOUDY,
    AOD_COND_POURING: ATTR_CONDITION_POURING,
    AOD_COND_RAINY: ATTR_CONDITION_RAINY,
    AOD_COND_SNOWY: ATTR_CONDITION_SNOWY,
    AOD_COND_SUNNY: ATTR_CONDITION_SUNNY,
}

FORECAST_MONITORED_CONDITIONS = [
    ATTR_API_FORECAST_CONDITION,
    ATTR_API_FORECAST_PRECIPITATION,
    ATTR_API_FORECAST_PRECIPITATION_PROBABILITY,
    ATTR_API_FORECAST_TEMP,
    ATTR_API_FORECAST_TEMP_LOW,
    ATTR_API_FORECAST_TIME,
    ATTR_API_FORECAST_WIND_BEARING,
    ATTR_API_FORECAST_WIND_SPEED,
]
MONITORED_CONDITIONS = [
    ATTR_API_CONDITION,
    ATTR_API_HUMIDITY,
    ATTR_API_PRESSURE,
    ATTR_API_RAIN,
    ATTR_API_RAIN_PROB,
    ATTR_API_SNOW,
    ATTR_API_SNOW_PROB,
    ATTR_API_STATION_ID,
    ATTR_API_STATION_NAME,
    ATTR_API_STATION_TIMESTAMP,
    ATTR_API_STORM_PROB,
    ATTR_API_TEMPERATURE,
    ATTR_API_TEMPERATURE_FEELING,
    ATTR_API_TOWN_ID,
    ATTR_API_TOWN_NAME,
    ATTR_API_TOWN_TIMESTAMP,
    ATTR_API_WIND_BEARING,
    ATTR_API_WIND_MAX_SPEED,
    ATTR_API_WIND_SPEED,
]

FORECAST_MODE_DAILY = "daily"
FORECAST_MODE_HOURLY = "hourly"
FORECAST_MODES = [
    FORECAST_MODE_DAILY,
    FORECAST_MODE_HOURLY,
]
FORECAST_MODE_ATTR_API = {
    FORECAST_MODE_DAILY: ATTR_API_FORECAST_DAILY,
    FORECAST_MODE_HOURLY: ATTR_API_FORECAST_HOURLY,
}
