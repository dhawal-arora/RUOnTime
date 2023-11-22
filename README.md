## RUOnTime

[Invite the Bot 😃](https://discord.com/api/oauth2/authorize?client_id=1160223557536710738&permissions=277025868800&scope=bot)

### Description
A bot made to make your lives easier by tracking upcoming buses based on dorm location, class location, class schedule and bus capacity to tell you if you will make it to your class on time.

### Unique Functions/Future Ideas
* Class ETA.
* Bus Schedule based on Class Schedule and Dorm Location.
* Thank the Bus Driver using Circle, Payment options.
* OpenAI gives feedback on the schedule and organizes your time to eat, rest and study. Even fun jokes!
* Chances of Catching Bus based on Capacity and distance from current location.

### Executing program
* Invite the bot and give it permissions.
* Use `/` and view all available commands.
* Use `/help` for detailed information on commands,
* Add your dorm location and schedule using the commands.
* Execute `/busreport` to get schedule information. 

## Inspiration
Rutgers recently downgraded from Transloc to Passio Go, making it inconvenient for students to manage their daily schedules. RUOnTime was an attempt to solve this issue and incorporate features beyond the scope of the Passio App.

## What it does
A bot made to make your lives easier by tracking upcoming buses based on dorm location, class location, class schedule and bus capacity to tell you if you will make it to your class on time with goals to incorporate OPEN-AI to critique student lifestyle and to provide incentive in terms of tipping the bus drivers on the blockchain using CIRCLE.

## How we built it
Stack Used: Bus Tracking API | Python | mySQL | Discord API | Web Scraping | phpMyAdmin | JSON
Bus data was cleaned using python, which later was used to compute distances between classrooms, dorms and live bus locations. This was then combined with user inputted class schedules on Discord to create a unique dataset, which in-turn helped us to display computed information.

## Challenges we ran into
Issues with getting latitude and longitude for every Rutgers on-campus housing and academic buildings.
Testing live bus location on the weekend
Finding nearest bus stop to a building using coordinate mathematics.
and most importantly sleep.....

## Accomplishments that we're proud of
Calculations of distance using geolocations.
Computation of bus timings
Unique and easy bot data entry interface

## What we learned
Cleaning big JSON files and databases.
Combating SQL issues.

## What's next for RUOnTime
Circle + OpenAI integration and large scale deployment.




