# Weather Icons

A set of 32 flat weather icons mapped to the WMO weather interpretation codes (the full WMO code table 4677, codes 0-99, which includes the subset used by Open-Meteo's `weather_code`). The icons are drawn from scratch by the script in `scripts/`, so they carry no third-party artwork.

![Icon preview](docs/preview_sheet.png)

## What's in the repo

| Path | Contents |
|---|---|
| `wmo_weather_icons.csv` | Lookup dataset: `wmo_code`, `weather_description`, `weather_icon_url` (100 rows) |
| `png/` | 256×256 PNGs with transparent backgrounds |
| `svg/` | The same icons as scalable SVGs |
| `scripts/make_icons.py` | Generator script: palette, shapes and code-to-icon composition |
| `scripts/make_preview_sheet.py` | Builds `docs/preview_sheet.png` from the PNGs |
| `scripts/requirements.txt` | Python packages for both scripts |
| `docs/preview_sheet.png` | Contact sheet of every icon |

## Code mapping

| WMO code | Description | Icon |
|---|---|---|
| 0 | Clear | `sunny` |
| 1 | Mainly Clear | `sunny_s_cloudy` |
| 2 | Partly Cloudy | `partly_cloudy` |
| 3 | Cloudy | `cloudy` |
| 4 | Smoke | `haze` |
| 5 | Haze | `haze` |
| 6 | Dust | `dust` |
| 7 | Blowing Dust or Sand | `dust` |
| 8 | Dust Whirls | `dust` |
| 9 | Duststorm or Sandstorm Nearby | `dust` |
| 10 | Mist | `fog` |
| 11 | Patchy Shallow Fog | `fog` |
| 12 | Shallow Fog | `fog` |
| 13 | Lightning Without Thunder | `lightning` |
| 14 | Precipitation Not Reaching Ground | `cloudy` |
| 15 | Distant Precipitation | `cloudy` |
| 16 | Precipitation Nearby | `cloudy` |
| 17 | Dry Thunderstorm | `lightning` |
| 18 | Squalls | `wind` |
| 19 | Funnel Cloud or Tornado | `tornado` |
| 20 | Recent Drizzle | `cloudy` |
| 21 | Recent Rain | `cloudy` |
| 22 | Recent Snow | `cloudy` |
| 23 | Recent Rain and Snow | `cloudy` |
| 24 | Recent Freezing Rain | `cloudy` |
| 25 | Recent Rain Showers | `cloudy` |
| 26 | Recent Snow Showers | `cloudy` |
| 27 | Recent Hail Showers | `cloudy` |
| 28 | Recent Fog | `cloudy` |
| 29 | Recent Thunderstorm | `cloudy` |
| 30 | Duststorm Easing | `dust` |
| 31 | Duststorm | `dust` |
| 32 | Duststorm Worsening | `dust` |
| 33 | Severe Duststorm Easing | `dust` |
| 34 | Severe Duststorm | `dust` |
| 35 | Severe Duststorm Worsening | `dust` |
| 36 | Drifting Snow | `blowing_snow` |
| 37 | Heavy Drifting Snow | `blowing_snow` |
| 38 | Blowing Snow | `blowing_snow` |
| 39 | Heavy Blowing Snow | `blowing_snow` |
| 40 | Fog in the Distance | `fog` |
| 41 | Fog Patches | `fog` |
| 42 | Fog Thinning | `fog` |
| 43 | Thick Fog Thinning | `fog` |
| 44 | Fog | `fog` |
| 45 | Fog | `fog` |
| 46 | Fog Thickening | `fog` |
| 47 | Thick Fog Thickening | `fog` |
| 48 | Freezing Fog | `fog_s_snow` |
| 49 | Thick Freezing Fog | `fog_s_snow` |
| 50 | Light Intermittent Drizzle | `rain_light` |
| 51 | Light Drizzle | `rain_light` |
| 52 | Intermittent Drizzle | `rain_light` |
| 53 | Drizzle | `rain_light` |
| 54 | Heavy Intermittent Drizzle | `rain` |
| 55 | Heavy Drizzle | `rain` |
| 56 | Light Freezing Drizzle | `freezing_rain_light` |
| 57 | Freezing Drizzle | `freezing_rain` |
| 58 | Light Drizzle and Rain | `rain_light` |
| 59 | Drizzle and Rain | `rain` |
| 60 | Light Intermittent Rain | `rain_light` |
| 61 | Light Rain | `rain_light` |
| 62 | Intermittent Rain | `rain` |
| 63 | Rain | `rain` |
| 64 | Heavy Intermittent Rain | `rain_heavy` |
| 65 | Heavy Rain | `rain_heavy` |
| 66 | Light Freezing Rain | `freezing_rain_light` |
| 67 | Freezing Rain | `freezing_rain` |
| 68 | Light Rain and Snow | `rain_s_snow` |
| 69 | Rain and Snow | `snow_s_rain` |
| 70 | Light Intermittent Snow | `snow_light` |
| 71 | Light Snow | `snow_light` |
| 72 | Intermittent Snow | `snow` |
| 73 | Snow | `snow` |
| 74 | Heavy Intermittent Snow | `snow_heavy` |
| 75 | Heavy Snow | `snow_heavy` |
| 76 | Diamond Dust | `snow_light` |
| 77 | Snow Grains | `snow_light` |
| 78 | Scattered Snow Crystals | `snow_light` |
| 79 | Ice Pellets | `hail_light` |
| 80 | Light Showers | `sunny_s_rain` |
| 81 | Showers | `rain_s_sunny` |
| 82 | Heavy Showers | `rain_heavy` |
| 83 | Light Rain and Snow Showers | `rain_s_snow` |
| 84 | Rain and Snow Showers | `snow_s_rain` |
| 85 | Light Snow Showers | `cloudy_s_snow` |
| 86 | Snow Showers | `snow_s_cloudy` |
| 87 | Light Snow Pellet Showers | `hail_light` |
| 88 | Snow Pellet Showers | `hail` |
| 89 | Light Hail Showers | `hail_light` |
| 90 | Hail Showers | `hail` |
| 91 | Light Rain After Thunderstorm | `rain_light` |
| 92 | Rain After Thunderstorm | `rain` |
| 93 | Light Snow or Hail After Thunderstorm | `snow_light` |
| 94 | Snow or Hail After Thunderstorm | `snow` |
| 95 | Thunderstorm | `thunderstorms` |
| 96 | Thunderstorm With Hail | `thunderstorms_light_s_hail` |
| 97 | Heavy Thunderstorm | `thunderstorms` |
| 98 | Thunderstorm With Duststorm | `thunderstorms_s_dust` |
| 99 | Heavy Thunderstorm With Hail | `thunderstorms_s_hail` |

The icons show daytime conditions only; there are no night variants.

Codes 0-3 follow Open-Meteo's use of them as cloud cover. In the original WMO table they describe how the sky changed over the past hour (01 clouds dissolving, 02 unchanged, 03 clouds forming).

Freezing drizzle and freezing rain (56, 57, 66, 67) use the `freezing_rain` icons, with an ice line under the drops. Mixed rain and snow (68, 69, 83, 84) uses `rain_s_snow` for the lighter codes, with rain in front, and `snow_s_rain` for the heavier ones, with snow in front.

## Using the dataset

### dbt seed (Snowflake)

Copy `wmo_weather_icons.csv` into your project's `seeds/` folder and pin the column types:

```yaml
# seeds/_seeds.yml
seeds:
  - name: wmo_weather_icons
    config:
      column_types:
        wmo_code: number(3,0)
        weather_description: varchar
        weather_icon_url: varchar
```

Then join it to your weather data:

```sql
select
    w.*,
    i.weather_description,
    i.weather_icon_url
from {{ ref('stg_open_meteo__daily') }} as w
left join {{ ref('wmo_weather_icons') }} as i
    on w.weather_code = i.wmo_code
```

(`stg_open_meteo__daily` is illustrative; substitute your own model.)

### Qlik Sense

```
WeatherIcons:
LOAD
    wmo_code             AS [Weather Code],
    weather_description  AS [Weather Description],
    weather_icon_url     AS [Weather Icon URL]
FROM [lib://<your-connection>/wmo_weather_icons.csv]
(txt, utf8, embedded labels, delimiter is ',', msq);
```

In a table object, set the `Weather Icon URL` column's representation to **Image** to show the icon.

### Where the URLs point

`weather_icon_url` points at the PNGs in this repo via `raw.githubusercontent.com`, which serves the image file itself. The repo has been set to public to allow the images to be retrieved directly.

## Regenerating or restyling the icons

```bash
pip install -r scripts/requirements.txt
python scripts/make_icons.py
python scripts/make_preview_sheet.py
```

The requirements are `resvg_py` (renders the SVGs to PNG, with no system libraries to install) and `Pillow` (builds the preview sheet).

`make_icons.py` writes every icon to `svg/` and `png/`, and `make_preview_sheet.py` rebuilds `docs/preview_sheet.png` from whatever is in `png/`. Colours are defined as constants at the top of the file (`SUN`, `CLOUD_LIGHT`, `CLOUD_MID`, `CLOUD_DARK`, `RAIN`, `SNOW`, `BOLT`, `FOG`, `DUST`, `ICE`). Each icon is a short composition in the `icons` dictionary if you want to add or adjust one.

## Sources

- WMO codes and descriptions: stellasphere, *WMO weather interpretation code descriptions* gist — https://gist.github.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c. Descriptions for the 28 Open-Meteo codes are taken from the gist's wording, with a few simplified; descriptions for the remaining codes are simplified from the WMO table below. The icons are original to this repo.
- WMO code table 4677 reference: https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM

## Licence

Released under the [MIT License](LICENSE). Copyright (c) 2026 Tahola LTD.

You can use, copy, modify, merge, publish, distribute, sublicense and sell the icons, dataset and script, including in commercial work, as long as the copyright notice and licence text are kept with all copies or substantial portions. The software is provided "as is", without warranty of any kind.
