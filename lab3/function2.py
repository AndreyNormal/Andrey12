<<<<<<< HEAD



movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1)Write a function that takes a single movie and returns True if its IMDB score is above 5.5

def CheckIMDB(movies): 
        if(movies['imdb']>5.5):
         return True
        else:
             return False
        
print('Checking if Dark Knight is greater than 5.5')
print("is_greater=check_score_greater(movies[2])")
  

#2)Write a function that returns a sublist of movies with an IMDB score above 5.5.

def sublistreturnmovie(movies):
     outList = []
     for i in range(0,len(movies)):
          correctmovie=movies[i]
          if correctmovie["imdb"]>5.5:
               outList.append(correctmovie)
               return outList
          
print("List of movies with an IMDB score > 5.5:")

#3)Write a function that takes a category name and returns just those movies under that category.

def myfunc(movies,categoryname):
     ourList =[]
     for i in movies:
          categorynames = i["category"]
          if categoryname.lower() ==categorynames():
               ourList.append(i)
               return ourList
          
          print("Movies category  are: ")
          print("Movies Triller are ")


#4)Write a function that takes a list of movies and computes the average IMDB score.
          
def avg_imdb_score(movies):
     avrscore = 0
     thatmovie = len(movies)
     for i in movies:
          avrscore = avrscore + i["imbg"]
          return avrscore
     
print("This is average score")


#5)Write a function that takes a category and computes the average IMDB score.
def myfunc(movies,categorymovie):
     ourList =[]
     for i in movies:
          categorymovie = i["category"]
          if categoryname.lower() ==categorymovie():
               ourList.append(i)
               return ourList
          
          print("Movies category  are: ")
          print("Movies Triller are ")
=======



movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1)Write a function that takes a single movie and returns True if its IMDB score is above 5.5

def CheckIMDB(movies): 
        if(movies['imdb']>5.5):
         return True
        else:
             return False
        
print('Checking if Dark Knight is greater than 5.5')
print("is_greater=check_score_greater(movies[2])")
  

#2)Write a function that returns a sublist of movies with an IMDB score above 5.5.

def sublistreturnmovie(movies):
     outList = []
     for i in range(0,len(movies)):
          correctmovie=movies[i]
          if correctmovie["imdb"]>5.5:
               outList.append(correctmovie)
               return outList
          
print("List of movies with an IMDB score > 5.5:")

#3)Write a function that takes a category name and returns just those movies under that category.

def myfunc(movies,categoryname):
     ourList =[]
     for i in movies:
          categorynames = i["category"]
          if categoryname.lower() ==categorynames():
               ourList.append(i)
               return ourList
          
          print("Movies category  are: ")
          print("Movies Triller are ")


#4)Write a function that takes a list of movies and computes the average IMDB score.
          
def avg_imdb_score(movies):
     avrscore = 0
     thatmovie = len(movies)
     for i in movies:
          avrscore = avrscore + i["imbg"]
          return avrscore
     
print("This is average score")


#5)Write a function that takes a category and computes the average IMDB score.
def myfunc(movies,categorymovie):
     ourList =[]
     for i in movies:
          categorymovie = i["category"]
          if categoryname.lower() ==categorymovie():
               ourList.append(i)
               return ourList
          
          print("Movies category  are: ")
          print("Movies Triller are ")
>>>>>>> dd8f882a758c64afd814387123f34671af6bcf0f
