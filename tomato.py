import requests
import json
import unicodedata
import operator

API_URI    = "http://api.rottentomatoes.com/api/public/v1.0/"
BOX_OFFICE = "lists/movies/box_office.json"
THEATERS   = "lists/dvds/top_rentals.json"
API_KEY    = "GetYourOwn"
MOVIES     = "movies.json"

num_movies = '50'

def compare_ratings(response, q):
  total = 0
  ratings = 0
  all_ratings = 0
  for m in response['movies']:
    all_ratings += m['ratings']['audience_score']
    m_str = str(m)
    if q in m_str:
      ratings += m['ratings']['audience_score']
      total+=1

  if total:
    print '\taverage rating of movies with', q, ': ', ratings / float(total)

  return sum([m['ratings']['audience_score'] 
              for m in response['movies']]) / float(num_movies)

def makequery(q, searchterms):
  parameters = { 'apikey' : API_KEY, 'q':q}
  r = requests.get( API_URI + MOVIES, params=parameters )
  response = json.loads( r.text )
  for term in searchterms:
    total_avg = compare_ratings(response, term)
  print "\ttotal avg: ", total_avg
  return response

queries = ['cat', 'dog']
print 'movies about cats:'
makequery('cat', queries)

print 'movies about dogs:'
makequery('dog', queries)

print 'movies about chickens:'
queries.append('chicken')
resp = makequery('chicken', queries)
#compare_ratings(resp, 'chicken')
