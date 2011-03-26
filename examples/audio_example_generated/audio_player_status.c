/* This file has been generated automatically by GObjectCreator
* (see http://www.bollmeier.de/GObjectCreator for details).
* Please modify user sections only!
*/

#include "audio_player_status.h"

GType
audio_player_status_get_type() {
    
    static GType type_id = 0;
    GEnumValue* values;
    guint idx;
    
    if (type_id == 0) {
        
        values = g_new(GEnumValue, 4);
        idx = 0;
        
        values[idx].value = AUDIO_PLAYER_STATUS_READY;
        values[idx].value_name = "READY";
        values[idx].value_nick = "READY";
        idx++;
        
        values[idx].value = AUDIO_PLAYER_STATUS_PLAYING;
        values[idx].value_name = "PLAYING";
        values[idx].value_nick = "PLAYING";
        idx++;
        
        values[idx].value = AUDIO_PLAYER_STATUS_PAUSED;
        values[idx].value_name = "PAUSED";
        values[idx].value_nick = "PAUSED";
        idx++;
        
        values[idx].value = 0;
        values[idx].value_name = NULL;
        values[idx].value_nick = NULL;
        
        type_id = g_enum_register_static("AudioPlayerStatus", values);
        
    }
    
    return type_id;
    
}

