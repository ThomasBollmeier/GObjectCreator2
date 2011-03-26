CFLAGS=`pkg-config gobject-2.0 --cflags`
LIBS=`pkg-config gobject-2.0 --libs`

OBJ_FILES=\
audio_format.o \
audio_iplayer.o \
audio_iplayer_marshaller.o \
audio_ogg_player.o \
audio_player_status.o \
demo.o

audio_format.o: audio_format.c
	gcc -c $(CFLAGS) audio_format.c	

audio_iplayer.o: audio_iplayer.c
	gcc -c $(CFLAGS) audio_iplayer.c

audio_iplayer_marshaller.o: audio_iplayer_marshaller.c
	gcc -c $(CFLAGS) audio_iplayer_marshaller.c	
	
audio_ogg_player.o: audio_ogg_player.c
	gcc -c $(CFLAGS) audio_ogg_player.c	

audio_player_status.o: audio_player_status.c
	gcc -c $(CFLAGS) audio_player_status.c	

demo.o: demo.c
	gcc -c $(CFLAGS) demo.c	

demo: $(OBJ_FILES)
	gcc -o demo $(LIBS) $(OBJ_FILES) 

clean:
	rm -f *.o
	rm -f demo
