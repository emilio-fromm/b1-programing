


songs = []
genres = []
genreCount = []

music_library = []




def add_song():

    print("To add a song, 1. please enter the name: ")
    songName = input()
    
    print("To add a song, 2. please enter the genre: ")
    genreName = input()
    
    songs.append([songName, genreName])
    
    
def display_genres():
    
    for genre in songs:
        genres.append(genre[1])
    
    for genre in genres:
        
        counter = genres.count(genre)
        counterTupel = [genre, counter]
        
        if counterTupel not in genreCount:
            genreCount.append(counterTupel)
    
    print(genreCount)
    

def display_songs():
    for song in songs:
        print(song[0])

def display_most_popular():
    mostPopGenre = ""
    biggestNumber = 0
    
    for genreTupel in genreCount:
        if genreTupel[1] > biggestNumber:
            mostPopGenre = genreTupel[0]
            biggestNumber = genreTupel[1]
            
    print("Beliebtestes Genre: ", mostPopGenre, " mit: ", biggestNumber, " Einträgen")

def main(userInput):

    i = 0
    while i < userInput:
        add_song()
        i = i+1
    
    display_songs()
    display_genres()
    display_most_popular()

    
    
main(5)




# def display_library(library, filter_artist=None, filter_genre=None):



