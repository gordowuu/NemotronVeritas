int addSong(char* title, char* artist) {
    assert(count < MAX_SONGS);
    int insertidx = -1;
    for (int i = 0; i < MAX_SONGS; i++) {
        index = (hash(title) + i) % MAX_SONGS;
        if (flags[index] == 'F') {
            if (strcmp(songs[index], title) == 0 && strcmp(artists[index], artist) == 0) {
                return 0;
            }
        }
        else {
            if (insertidx == -1) {
                insertidx = index;
            }

            if (flag[index] == 'E') {
                break;
            }
         }
    }
    if (insertidx != -1) {
        songs[insertidx] = title;
        artists[insertidx] = artist;
        flags[insertidx] = 'F';
        count++;
        return 1;
    }
    return 0;
}

char* findArtist(char *title) {
    assert(count < MAX_SONGS);
    for (int i = 0; i < MAX_SONGS; i++) {
        index = (hash(title) + i) % MAX_SONGS;
        else if (flags[index] == 'E') {
            return NULL;
        }
        else if (flags[index] == 'F') {
           if (strcmp(songs[index], title) == 0){
                return artists[index];
           }
        }
    }
    return NULL;
}