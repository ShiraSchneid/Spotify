import Draw

from spotify_db1 import *

conn = mysql.connector.connect(host="localhost", user="root",passwd="obsidiandagger", database="spotify") 
cursor = conn.cursor() 
Draw.setCanvasSize(500,500)
Draw.setBackground(Draw.BLACK)
user_ID=1
num = 0

#create a new playlist
def make_playlist():
    Draw.clear()
    conn = mysql.connector.connect(host="localhost", user="root",passwd="obsidiandagger", database="spotify") 
    cursor = conn.cursor()     
    Draw.setColor(Draw.GREEN)
    Draw.string("create a new playlist:",25,100)  #get the name of the new playlist
    playlist_name=""
    while True:
        if Draw.hasNextKeyTyped():                  #take in new playlist name and remove return 
            playlist_name+=Draw.nextKeyTyped()
            if "Return" in playlist_name:
                playlist_name=playlist_name[:-6]        
                global num
                num +=1 
                break
            Draw.setColor(Draw.WHITE)
            Draw.string(playlist_name,135,100)
            
            Draw.show()
    create_playlist(cursor,str(num),playlist_name,"1")

    conn.commit() 
    conn.close()
    back()


#delete a playlist
def delete_playlist():
    Draw.clear()
    conn = mysql.connector.connect(host="localhost", user="root",passwd="obsidiandagger", database="spotify") 
    cursor = conn.cursor()     
    Draw.setColor(Draw.GREEN)
    if counts(cursor, 'Playlist') ==0:
        Draw.string("You currently have no playlists", 25, 100)  #you have no playlists
        back()
    else: 
        Draw.string("Pick which playlist you want to delete from: ", 25, 100)       #choose a playlist
        full_set = ""
        full_set = count_genre(cursor,"playlist")       
        x=250
        y=100
        for each in full_set:                   
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            Draw.setColor(Draw.WHITE)
            Draw.string(each[1],x+20,y)                
            y+=50  
        s_playlist=""
        while True:                             #choose a playlist to delete
            if Draw.hasNextKeyTyped():
                s_playlist+=Draw.nextKeyTyped()
                if "Return" in s_playlist:
                    s_playlist = s_playlist[:-6]
                    break
                Draw.setColor(Draw.WHITE)
                Draw.string(s_playlist,430,400)   
                Draw.show()
        
        Draw.clear()
        Draw.setColor(Draw.GREEN)
        result = deleter(cursor,s_playlist)
        for each in result:
            delete_song(cursor, str(each[0]), s_playlist)       #delete all the songs
        remove_playlist(cursor,s_playlist)                      #delete the whole playlist 
     
    conn.commit() 
    conn.close()    
    back()
    
def display_playlist():
    Draw.clear()
    conn = mysql.connector.connect(host="localhost", user="root",passwd="obsidiandagger", database="spotify") 
    cursor = conn.cursor()       
    Draw.setColor(Draw.GREEN)
    if counts(cursor, 'Playlist') ==0:
        Draw.string("You currently have no playlists", 25, 100)
        back()
    else: 
        Draw.string("Pick which # playlist you want to view: ", 25, 100)
        full_set = ""
        full_set = count_genre(cursor,"playlist")
        x=250
        y=100
        for each in full_set:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            Draw.setColor(Draw.WHITE)
            Draw.string(each[1],x+20,y)                
            y+=50  
        s_playlist=""
        while True:
            if Draw.hasNextKeyTyped():                  #pick a playlist to view 
                s_playlist+=Draw.nextKeyTyped()
                if "Return" in s_playlist:
                    s_playlist = s_playlist[:-6]
                    break
                Draw.setColor(Draw.WHITE)
                Draw.string(s_playlist,430,400)   
                Draw.show()
           
        Draw.clear()
        Draw.setColor(Draw.GREEN)
        Draw.string("Here is your playlist",25,100)     #show playlist 
        display=''
        display=adder(cursor,"playlist",s_playlist)
        x=200
        y=100
        for each in display:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            y+=50
    back()

    
def search_playlist():
    Draw.clear()
    conn = mysql.connector.connect(host="localhost", user="root",passwd="obsidiandagger", database="spotify") 
    cursor = conn.cursor()     
    Draw.setColor(Draw.GREEN)
    if counts(cursor, 'Playlist') ==0:
        Draw.string("You currently have no playlists", 25, 100)
        back()   
    else: 
        Draw.string("Pick which # playlist you want to search: ", 25, 100)
        full_set = ""
        full_set = count_genre(cursor,"playlist")
        x=250
        y=100
        for each in full_set:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            Draw.setColor(Draw.WHITE)
            Draw.string(each[1],x+20,y)                
            y+=50  
        s_playlist=""
        while True:
            if Draw.hasNextKeyTyped():                  #type in playlist to view 
                s_playlist+=Draw.nextKeyTyped()
                if "Return" in s_playlist:
                    s_playlist = s_playlist[:-6]
                    break
                Draw.setColor(Draw.WHITE)
                Draw.string(s_playlist,430,400)   
                Draw.show()    
        Draw.clear()
        Draw.setColor(Draw.GREEN)
        Draw.string("Search your playlist based on genre: ", 25,100)        #choose genre 
        display = count_genre(cursor, "genre")
        x=250
        y=100
        for each in display:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            Draw.setColor(Draw.WHITE)
            Draw.string(each[1],x+20,y)
            y+=50    
        Draw.string("Type the number of the genre you are looking for and click enter:", 100,400)    
        genre_lookup=""
        while True:
            if Draw.hasNextKeyTyped():
                genre_lookup+=Draw.nextKeyTyped()
                if "Return" in genre_lookup:
                    genre_lookup = genre_lookup[:-6]
                    break
                Draw.setColor(Draw.WHITE)
                Draw.string(genre_lookup,430,400)
                
        Draw.show()    
        Draw.clear()
        result = ""
        result=search_song(cursor,"genre_ID",genre_lookup, s_playlist)
        
        Draw.string("These are the songs you have in this genre:", 25, 100)     #display songs in genre 
        x=250
        y=100
        for each in result:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            y+=50                
    Draw.show()
    back()    
            
def add_song():
    Draw.clear()
    conn = mysql.connector.connect(host="localhost", user="root",passwd="obsidiandagger", database="spotify") 
    cursor = conn.cursor()      
    Draw.setColor(Draw.GREEN)
    if counts(cursor, 'Playlist') ==0:
        Draw.string("You currently have no playlists", 25, 100)
        back()
    else: 
        Draw.string("Pick which playlist you want to add to: ", 25, 100)
        full_set = ""
        full_set = count_genre(cursor,"playlist")
        x=250
        y=100
        for each in full_set:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            Draw.setColor(Draw.WHITE)
            Draw.string(each[1],x+20,y)                
            y+=50  
        s_playlist=""
        while True:
            if Draw.hasNextKeyTyped():
                s_playlist+=Draw.nextKeyTyped()
                if "Return" in s_playlist:
                    s_playlist = s_playlist[:-6]
                    break
                Draw.setColor(Draw.WHITE)
                Draw.string(s_playlist,430,400)   
                Draw.show()
        
        Draw.clear()
        Draw.string("Add a song to your playlist from this list of songs: ", 25,100)
        display = count_genre(cursor, "song")
        x=265
        y=115
        for each in display:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            Draw.setColor(Draw.WHITE)
            Draw.string(each[1],x+20,y)
            y+=15 
        Draw.string("Type the number of the song you want to add and click enter:", 100,400)    
        song_insert=""
        while True:
            if Draw.hasNextKeyTyped():
                song_insert+=Draw.nextKeyTyped()
                if "Return" in song_insert:
                    song_insert = song_insert[:-6]
                    break
                Draw.setColor(Draw.WHITE)
                Draw.string(song_insert,430,400)   
                Draw.show()
        
        result = ""
        insert_song(cursor,s_playlist,song_insert)
        conn.commit()
        result=adder(cursor,"playlist",s_playlist)
        Draw.clear()
        Draw.string("These are the songs in this playlist:", 25, 100)
        x=250
        y=100
        for each in result:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)              
            y+=50               
    Draw.show()
    conn.close() 
    back()
    


def remove_song():
    Draw.clear()
    conn = mysql.connector.connect(host="localhost", user="root",passwd="obsidiandagger", database="spotify") 
    cursor = conn.cursor()     
    Draw.setColor(Draw.GREEN)
    if counts(cursor, 'Playlist') ==0:
        Draw.string("You currently have no playlists", 25, 100)
        back()
    else:
        Draw.string("Pick which playlist you want to delete from: ", 25, 100)
        full_set = ""
        full_set = count_genre(cursor,"playlist")
        x=250
        y=100
        for each in full_set:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            Draw.setColor(Draw.WHITE)
            Draw.string(each[1],x+20,y)                
            y+=50  
        s_playlist=""
        while True:
            if Draw.hasNextKeyTyped():
                s_playlist+=Draw.nextKeyTyped()
                if "Return" in s_playlist:
                    s_playlist = s_playlist[:-6]
                    break
                Draw.setColor(Draw.WHITE)
                Draw.string(s_playlist,430,400)   
                Draw.show()
        
        Draw.clear()
        Draw.setColor(Draw.GREEN)
        Draw.string("Delete a song from your playlist: ", 25,100)
        display=deleter(cursor,s_playlist)
        x=265
        y=115
        for each in display:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)
            Draw.string(each[1],x+10,y)
            
            y+=15 
        Draw.string("Type the number of the song you want to remove and click enter:", 100,400)    
        song_delete=""
        while True:
            if Draw.hasNextKeyTyped():
                song_delete+=Draw.nextKeyTyped()
                if "Return" in song_delete:
                    song_delete = song_delete[:-6]
                    break
                Draw.setColor(Draw.WHITE)
                Draw.string(song_delete,430,400)   
                Draw.show()
        
        result = ""
        delete_song(cursor,song_delete,s_playlist)
        result=adder(cursor,"playlist",s_playlist)
        Draw.clear()
        Draw.string("These are now the songs in your playlist:", 25, 100)
        x=250
        y=100
        for each in result:
            Draw.setColor(Draw.GREEN)
            Draw.string(each[0],x, y)             
            y+=50               
        
    Draw.show() 
    
    conn.commit()
    conn.close()
    back()

#button that brings the user back to the home page 
def back():
    Draw.setColor(Draw.RED)
    Draw.filledRect(50,450,50,25)
    Draw.setColor(Draw.WHITE)
    Draw.string("BACK",60,457)
    while True:
        if Draw.mousePressed():
            x=Draw.mouseX()
            y=Draw.mouseY()
            if x >= 50 and x<=100 and y>=450 and y<=475:
                print("back")
                Draw.clear()
                main_display()   
           


#create button page with create playlist, delete playlist, see playlist and its songs ,search playlist, delete song, add song
#create a back button to bring you back to the button page 

def main_display():
    conn = mysql.connector.connect(host="localhost", user="root",passwd="obsidiandagger", database="spotify") 
    cursor = conn.cursor()     
    Draw.clear()
    Draw.setColor(Draw.GREEN)
    Draw.setFontFamily('Arial')
    Draw.setFontSize(50)
    Draw.string("Spotify", 100, 100)
    Draw.setFontSize(12)
    Draw.string("welcome to spotify user #1!",100,200)
    Draw.string("Click a button to choose the action you want to complete",100,250)
    Draw.filledRect(100,300,75,50)
    Draw.filledRect(212,300,75,50)
    Draw.filledRect(324,300,75,50)
    Draw.filledRect(100,400,75,50)
    Draw.filledRect(212,400,75,50)
    Draw.filledRect(324,400,75,50)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(10)
    Draw.string("Create Playlist",103,320)   
    Draw.string("Delete Playlist",215,320)
    Draw.string("See Playlist",335,320)
    Draw.string("Search Playlist",103,420)
    Draw.string("Delete Song",220,420)
    Draw.string("Add Song",340,420)
    while True:        
        if Draw.mousePressed():
            x=Draw.mouseX()
            y=Draw.mouseY()
            if x >100 and x <175 and y>300 and y< 350:
                make_playlist()
            if x > 212 and x < 287 and y > 300 and y <350:
                delete_playlist()
            if x > 324 and x < 400 and y >300 and y < 350:
                display_playlist()
            if x > 100 and x <175 and y >400 and y < 450:
                search_playlist()
            if x >212 and x <287 and y > 400 and y < 450:
                remove_song()
            if x > 324 and x < 400 and y > 400 and y < 450:
                add_song()
            
    
main_display()