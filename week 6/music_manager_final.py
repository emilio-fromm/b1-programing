# Copyright by Emilio

import random

songs = []
genre_count = {}

print("=== Emilio's Music Manager ===")
print("Loading music collection...")

for i in range(1, 6):
    print(f"Enter song {i}:")
    song_name = input("  Song name: ")
    genre = input("  Genre: ")
    print()

    songs.append((song_name, genre))
    genre_count[genre] = genre_count.get(genre, 0) + 1

play_counts = {}
for name, genre in songs:
    play_counts[name] = random.randint(1, 200)

print("=== YOUR MUSIC LIBRARY ===")
for index, (name, genre) in enumerate(songs, 1):
    print(f"{index}. {name} ({genre}) - played {play_counts[name]} times")

print("\n=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} song(s)")

most_popular = max(genre_count, key=genre_count.get)
print(f"\nMost popular genre: {most_popular}")

most_played = max(play_counts, key=play_counts.get)
print(f"Most played song: {most_played} ({play_counts[most_played]} plays)")

print("\n=== SHUFFLE MODE ===")
shuffle = list(songs)
random.shuffle(shuffle)
print("Shuffle order:")
for i, (name, genre) in enumerate(shuffle, 1):
    print(f"  {i}. {name}")
