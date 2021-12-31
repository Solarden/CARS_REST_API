# CARS_REST_API

Django REST API which saves user input of make and model into database. It connects with external API for confirmation
if user input really exist. If true it is added to database.

# /cars/

- GET: shows information about all cars already existing in database with average rating calculated from objects passed
  by user at `/rate/`
  `{
  "id": 1,
  "make": "Honda",
  "model": "Civic",
  "avg_rating": 5.0 }`
- POST: receives user input and searches for confirmation in external API. If car does not exist returns an error.

# /cars/<int:id>/

- GET: shows information about car with pointed ID in URL `{
  "id": 1,
  "make": "Honda",
  "model": "Civic",
  "avg_rating": 5.0 }`
- POST: enables possibility of updating object with passed ID in URL
- DELETE: removes from database object with passed ID in URL. If object with passed ID does not exist returns an error.

# /rate/

- POST: receives user voting information which then is saved in database `{
  "id": 1,
  "rating": 3 }`
  Rating is available in scale of 1 to 5

# /popular/

- GET: shows information about all cars already existing in database in order by all rates passed by users at `/rate/`

# Deployment

- Docker if you don't have it follow these instructions: https://docs.docker.com/get-docker/
- Docker-compose: https://docs.docker.com/compose/install/

Then use in root folder of project:
- `docker-compose up`

After building up please consider doing migrations!
- `docker ps` - prints all active containers
- Look for container ID for cars_rest_api_web
- Then enter the container by `docker exec -it {four first characters of containder ID} bash`
- After entering container `python manage.py migrate`
- To leave container `exit`

To close active containers use in terminal `^C`

# Check me out at heroku!
https://cars-checker-rest-api.herokuapp.com/cars/
