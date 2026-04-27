# RU On Time

A Discord bot that helps Rutgers students catch their bus on time by combining live bus tracking, dorm location, and class schedules into a single `/busreport` command.

[Invite the Bot](https://discord.com/api/oauth2/authorize?client_id=1160223557536710738&permissions=277025868800&scope=bot)

---

## What it does

Tracks upcoming buses based on your dorm location, class location, class schedule, and live bus capacity — so you know exactly which bus to catch and whether you'll make it on time.

## Tech Stack

- **Python** — discord.py (slash commands, Cogs)
- **MySQL** — stores user housing and class schedules
- **Rutgers Passio Go API** — live bus locations, ETAs, and capacity
- **Coordinate math** — finds the nearest bus stop to any building using lat/lon distance

---

## Setup

### Prerequisites
- Python 3.10+
- MySQL database with the schema below
- A Discord bot token

### Installation

```bash
git clone https://github.com/dhawal-arora/RUOnTime.git
cd RUOnTime
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

```
DISCORD_TOKEN=your_discord_bot_token
DB_HOST=localhost
DB_USER=your_db_username
DB_PASS=your_db_password
DB_NAME=your_db_name
```

### Database Schema

```sql
CREATE TABLE housing (
    id      NUMERIC(23) NOT NULL PRIMARY KEY,
    dorm    VARCHAR(200) NOT NULL,
    scheduleopen INTEGER NOT NULL
);

CREATE TABLE classes (
    id        NUMERIC(23) NOT NULL,
    location  VARCHAR(200) NOT NULL,
    classname VARCHAR(200) NOT NULL,
    starttime TIME NOT NULL,
    endtime   TIME NOT NULL,
    day       VARCHAR(200) NOT NULL
);
```

### Run

```bash
python main.py
```

---

## Usage

| Step | Command | Description |
|------|---------|-------------|
| 1 | `/buschhousing` `/livihousing` `/collegeavehousing` `/cookdoughousing` | Set your dorm |
| 2 | `/openschedule` | Enable class entry mode |
| 3 | `/buschclass` `/liviclass` `/collegeaveclass` `/cookdougclass` | Add each class |
| 4 | `/closeschedule` | Submit your schedule |
| 5 | `/busreport` | Get today's live bus report |

**Other commands:** `/deletehousing` `/deleteschedule` `/help`

---

## Project Structure

```
RUOnTime/
├── main.py          # Entry point — bot setup and startup
├── config.py        # Loads credentials from .env
├── database.py      # Singleton MySQL connection
├── data.py          # Rutgers Passio Go API calls
├── locations.py     # Coordinates for all Rutgers dorms and buildings
├── report.py        # Bus timing logic — powers /busreport
└── cogs/
    ├── housing.py   # /buschhousing, /livihousing, /collegeavehousing, /cookdoughousing
    ├── schedule.py  # /openschedule, /closeschedule, /deleteschedule, /deletehousing, /busreport, /help
    └── classes.py   # /buschclass, /liviclass, /collegeaveclass, /cookdougclass
```

---

## Inspiration

Rutgers recently downgraded from Transloc to Passio Go, making it inconvenient for students to manage their daily schedules. RU On Time was built to solve this — and to go beyond what the Passio app offers.

## Challenges

- Getting accurate latitude/longitude for every Rutgers on-campus housing and academic building
- Testing live bus location data on weekends
- Finding the nearest bus stop to any building using coordinate mathematics

## What's next

- OpenAI integration for schedule feedback and lifestyle tips
- Circle (blockchain) integration for tipping bus drivers
- Estimated lateness calculation
