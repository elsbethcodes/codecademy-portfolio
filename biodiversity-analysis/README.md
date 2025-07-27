---

## 🦅 Project Description

Data analysis of species recorded across four U.S. national parks, exploring biodiversity, conservation status, and observation trends. Developed as part of Codecademy’s Data Scientist: Machine Learning career path to apply data wrangling, aggregation, and visualisation techniques.

## 🏔️ Data Source

The dataset comes from Codecademy’s “Biodiversity in National Parks” project and is based on data from the U.S. National Parks Service. It includes two CSV files:

* `species_info.csv` – species names, categories, and conservation status
* `observations.csv` – species sightings by park

Original source: U.S. National Park Service – [https://www.nps.gov/](https://www.nps.gov/)

## 🧾 Data Description

**species\_info.csv** contains:

| Variable              | Description                                                     |
| --------------------- | --------------------------------------------------------------- |
| `category`            | Type of organism (e.g. Mammal, Bird, Plant)                     |
| `scientific_name`     | Species’ scientific name                                        |
| `common_names`        | Common name(s)                                                  |
| `conservation_status` | Current protection status (e.g. Species of Concern, Endangered) |

**observations.csv** contains:

| Variable          | Description                                     |
| ----------------- | ----------------------------------------------- |
| `scientific_name` | Species’ scientific name                        |
| `park_name`       | Name of the national park                       |
| `observations`    | Number of sightings recorded over the past week |

---
