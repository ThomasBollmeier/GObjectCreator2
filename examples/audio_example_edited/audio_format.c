/* This file has been generated automatically by GObjectCreator
* (see http://www.bollmeier.de/GObjectCreator for details).
* Please modify user sections only!
*/

#include "audio_format.h"

GType
audio_format_get_type() {
    
    static GType type_id = 0;
    GEnumValue* values;
    guint idx;
    
    if (type_id == 0) {
        
        values = g_new(GEnumValue, 3);
        idx = 0;
        
        values[idx].value = AUDIO_FORMAT_MP3;
        values[idx].value_name = "MP3";
        values[idx].value_nick = "MP3";
        idx++;
        
        values[idx].value = AUDIO_FORMAT_OGG_VORBIS;
        values[idx].value_name = "OGG_VORBIS";
        values[idx].value_nick = "OGG_VORBIS";
        idx++;
        
        values[idx].value = 0;
        values[idx].value_name = NULL;
        values[idx].value_nick = NULL;
        
        type_id = g_enum_register_static("AudioFormat", values);
        
    }
    
    return type_id;
    
}

