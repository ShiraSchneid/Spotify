import mysql.connector
from mysql.connector import FieldType

# delete a song
def delete_song(cursor, song_ID,p_ID):
    return delete_entity(cursor,"song_ID", song_ID,p_ID)
#took out table parameter     
def delete_entity(cursor, key_col, key_val,p_ID):
    #Creating a SQL query to delete the specified row from the table, which requires the name of the table, the name of the key column (typically - but not necessarily - the primary key), and the value(s) of that column (typically some kind of id) for which we wish to delete the record  
    query = "delete from " + 'playlist_song' +" where " + key_col + " = '" + key_val + "'"+ "and playlist_ID = " + p_ID
    #query = "delete from student where ID = 2468"
    print("Query:", query)
    #Executing the query 
    #Checking for errors (perhaps due to foreign key / referential integrity constraints)
    #Reporting that error back to the user    
    try:
        cursor.execute(query)
    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')    
        return -1
    #Determining the success or failure of the operation 
    #Closing or disconnecting the connection
    #return key_val
    
def insert_song(cursor,playlist_ID,song_ID):
    return insert_entity(cursor,playlist_ID,song_ID)

def insert_entity(cursor,key_col,key_val):
    query = "insert into " + 'playlist_song' +" values (" + key_col + "," + key_val+ ")"
    print("Query:", query)
    try:
        cursor.execute(query)
    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')    
        return -1   
 
def create_playlist(cursor,playListID,playlist_name,user_ID):
    return create_entity(cursor,playListID,playlist_name,user_ID)

def create_entity(cursor,key_playListID,key_name,key_ID):
    query = "insert into " + 'Playlist' +" values (" + key_playListID +",'"+ key_name + "'," + key_ID+")"
    print("Query:", query)
    try:
        cursor.execute(query)
    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')    
        return -1   
 
# delete playlist
def remove_playlist(cursor, playlist_ID):
    return remove_entity(cursor,"playlist_ID", playlist_ID)
#took out table parameter     
def remove_entity(cursor, key_col, key_val):
    #Creating a SQL query to delete the specified row from the table, which requires the name of the table, the name of the key column (typically - but not necessarily - the primary key), and the value(s) of that column (typically some kind of id) for which we wish to delete the record  
    query = "delete from " + 'Playlist' +" where " + key_col + " = '" + key_val + "'"
    #query = "delete from student where ID = 2468"
    print("Query:", query)
    #Executing the query 
    #Checking for errors (perhaps due to foreign key / referential integrity constraints)
    #Reporting that error back to the user    
    try:
        cursor.execute(query)
    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')    
        return -1
    #Determining the success or failure of the operation 
    #Closing or disconnecting the connection
    #return key_val 
    
#search for song in a playlist? 
def search_song(cursor,search_name,vari,pi_ID):
    return search_entity(cursor,search_name,vari,pi_ID)

def search_entity(cursor,key_col,key_val,p_ID):
    query = "select name from " + 'song natural join playlist_song ' +"where " + key_col + "=" + key_val+" and playlist_ID = "+p_ID
    #query = "select playlist_ID from playlist_song"
    print("Query:", query)
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
       
    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')    
        return -1   

    

#retrieve
def count_entity(cursor, table,user_ID):
    query = "select playlist_name, song.name from " + table + " natural join song " + " where user_ID = "+ user_ID
    print("Query:", query)
    x=""
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
       
        return rows 

    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')    
        
def adder(cursor, table,play):
    query= "select song.name from playlist_song natural join song where playlist_ID =" + play
    print("Query:", query)
    x=""
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
       
        return rows 

    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')
        
def deleter(cursor,play):
    query= 'select song_ID, song.name from playlist natural join playlist_song natural join song where playlist_ID = '+ play
    print("Query:", query)
    x=""
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
       
        return rows 

    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')    
    
def count_genre(cursor, table):
    query = "select * from " + table
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
       
        return rows 

    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')   
        
def counts(cursor, table):
    query = "select * from " + table
    try:
        cursor.execute(query)
        rows = cursor.fetchall()

        return cursor.rowcount   #Executing the query 
    except mysql.connector.Error as e:
        print("Error interacting with mySQL", e, '\n')   

    
 
def main():
    # create connection in main:
    conn = mysql.connector.connect(host="localhost", user="root",passwd="obsidiandagger", database="spotify") 
    cursor = conn.cursor()   
    
    # good test code:    
    #count_entity(cursor, "playlist_song")
    
    #insert_song(cursor,"1","6")
    #count_entity(cursor,'song')
    #delete_song(cursor, "1")
    #count_entity(cursor,"User")
    #update_user(cursor,'super')
    #count_entity(cursor,"User")
    #create_playlist(cursor,"3","party","1")
    #count_entity(cursor,'Playlist',"1")
    print(counts(cursor, 'Playlist'))
    #remove_playlist(cursor,"new")
    #search_song(cursor,"genre_ID","1","1")
    #count_entity(cursor,'Playlist')
    #retrieve_playlist(cursor,"playlist")
    conn.commit()    
    #count_entity(cursor, "playlist_song")
    #count_entity(cursor,'Playlist')
    conn.close()
    
    
#main()
