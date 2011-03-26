/* This file has been generated automatically by GObjectCreator
* (see http://www.bollmeier.de/GObjectCreator for details).
* Please modify user sections only!
*/

#ifndef AUDIO_FORMAT_H
#define AUDIO_FORMAT_H

#include "glib-object.h"

G_BEGIN_DECLS

typedef enum _AudioFormat {
    
    AUDIO_FORMAT_MP3,
    AUDIO_FORMAT_OGG_VORBIS
    
} AudioFormat;

GType
audio_format_get_type();

#define AUDIO_TYPE_FORMAT audio_format_get_type()

G_END_DECLS

#endif

