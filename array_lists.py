from operator import attrgetter


class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
    
    def __str__(self):
        return str([self.album_name, self.album_artist, self.number_of_songs])
# Create a list and add five album


albums1 = []
albums1.append(Album("Album1", 10, "Artist1"))
albums1.append(Album("Album2", 12, "Artist2"))
albums1.append(Album("Album3", 8, "Artist3"))
albums1.append(Album("Album4", 15, "Artist4"))
albums1.append(Album("Album5", 11, "Artist5"))
# Print the list out
for a in albums1:
    print(a)
print()
# # sorting the list accordingly to the number of songs
albums1_sorted = sorted(albums1, key=attrgetter('number_of_songs'))
for s in albums1_sorted:
    print(s)
print()
# # swap element at position 1 with element at position 2
albums1[1], albums1[2] = albums1[2], albums1[1]
for j in albums1:
    print(j)
print()

# # Create a new list and add five albums
albums2 = []
albums2.append(Album("Album6", 11, "Artist6"))
albums2.append(Album("Album7", 13, "Artist7"))
albums2.append(Album("Album8", 9, "Artist8"))
albums2.append(Album("Album9", 16, "Artist9"))
albums2.append(Album("Album10", 12, "Artist10"))

# # Print the new list out
for i in albums2:
    print(i)
print()
# Copy the albums 1 into albums2
albums2.extend(albums1)
print()
# # Add two new elements to album2
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!...I Did It Again", "Britney Spears", 16))
# # Sort the albums2 alphabetcaly according to the name
sorted_album = sorted(albums2, key=attrgetter('album_name'))


# Print the sorted list
for a in sorted_album:
    print(a)

# Searching for the album "Dark side of the moon" in albums2
search_album = "Dark Side of the Moon"
index = next((i for i, album in enumerate(albums2) if album.album_name == search_album), None)
if index is not None:
    print(f"\nIndex of '{search_album}' in Albums 2: {index}")
else:
    print(f"\n'{search_album}' not found in Albums 2.")
