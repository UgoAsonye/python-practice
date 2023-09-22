playlist = {
    "title": "Deutsche Musik (Kurz)", 
    "author": "Ugo Asonye", 
    "songs": [
        {"title": "Hoodnights", "artist": ["BHZ"], "duration": 3.5},
        {"title": "Roller", "artist": ["Apache 207"], "duration": 2.5},
        {"title": "Bounce", "artist": ["Dennis Dies Das"], "duration": 3.0}

    ]
}
total_length = 0
for song in playlist["songs"]:
    total_length += song["duration"]
print(total_length)