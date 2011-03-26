/* This file has been generated automatically by GObjectCreator
* (see http://www.bollmeier.de/GObjectCreator for details).
* Please modify user sections only!
*/

#ifndef AUDIO_ERROR_H
#define AUDIO_ERROR_H

#include "glib-object.h"

G_BEGIN_DECLS

#define AUDIO_ERROR g_quark_from_static_string("audio_error_quark")

enum AudioError {
    
    AUDIO_ERROR_INVALID_STATUS = 1,
    AUDIO_ERROR_URI_NOT_FOUND,
    AUDIO_ERROR_UNKNOWN_FORMAT
    
};

G_END_DECLS

#endif

