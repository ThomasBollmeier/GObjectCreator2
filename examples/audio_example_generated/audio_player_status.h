/* This file has been generated automatically by GObjectCreator
* (see http://www.bollmeier.de/GObjectCreator for details).
* Please modify user sections only!
*/

#ifndef AUDIO_PLAYER_STATUS_H
#define AUDIO_PLAYER_STATUS_H

#include "glib-object.h"

G_BEGIN_DECLS

typedef enum _AudioPlayerStatus {
    
    AUDIO_PLAYER_STATUS_READY,
    AUDIO_PLAYER_STATUS_PLAYING,
    AUDIO_PLAYER_STATUS_PAUSED
    
} AudioPlayerStatus;

GType
audio_player_status_get_type();

#define AUDIO_TYPE_PLAYER_STATUS audio_player_status_get_type()

G_END_DECLS

#endif

