liked_songs = {
  'Me Jalo': 'Grupo Frontera',
  'Moscow Mule' : 'Bad Bunny',
  'Calma' : 'Pedro Capo'
}
file_name = 'liked_playlist.txt'
def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked Songs: \n')
        for k,v in liked_songs.items():

            file.writelines(f'{k} by {v}')


write_liked_songs_to_file(liked_songs, file_name)
