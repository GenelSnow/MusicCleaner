from services.scanner import MusicScanner

scanner = MusicScanner()

songs = scanner.scan(r"C:\Users\LENOVO\AA2\musia\parchar")

print(len(songs))

for song in songs[:10]:
    print(song.name, "-", song.size_mb, "MB")