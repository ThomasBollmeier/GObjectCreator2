/* This file has been generated automatically by GObjectCreator
* (see http://www.bollmeier.de/GObjectCreator for details).
* Please modify user sections only!
*/

#ifndef AUDIOIPLAYER_H
#define AUDIOIPLAYER_H

#include "glib-object.h"

G_BEGIN_DECLS

/* UserCode header_top { */

    /* add further includes.../

/* } UserCode */

typedef struct _AudioIPlayer AudioIPlayer;

typedef struct _AudioIPlayerIface {
    
    GTypeInterface base_interface;
    
    /* == methods == */
    
    void
    (*start)(AudioIPlayer* self, const gchar* track_uri, AudioFormat format, 
        GError** error);
    gboolean
    (*pause)(AudioIPlayer* self);
    gboolean
    (*stop)(AudioIPlayer* self);
    
    /* == signals == */
    
    void /* started */
    (*started)(AudioIPlayer* sender, const gchar* track_uri, gboolean resumed);
    void /* paused */
    (*paused)(AudioIPlayer* sender, const gchar* track_uri);
    void /* stopped */
    (*stopped)(AudioIPlayer* sender, const gchar* track_uri);
    
} AudioIPlayerIface;

GType
audio_iplayer_get_type();

/* ===== methods ===== */

void
audio_iplayer_start(AudioIPlayer* self, const gchar* track_uri, AudioFormat format, 
    GError** error);

gboolean
audio_iplayer_pause(AudioIPlayer* self);

gboolean
audio_iplayer_stop(AudioIPlayer* self);

/* ===== macros ===== */

#define AUDIO_TYPE_IPLAYER \
    (audio_iplayer_get_type())
#define AUDIO_IPLAYER(obj) \
    (G_TYPE_CHECK_INSTANCE_CAST((obj), AUDIO_TYPE_IPLAYER, AudioIPlayer))
#define AUDIO_IPLAYER_CLASS(cls) \
    (G_TYPE_CHECK_CLASS_CAST((cls), AUDIO_TYPE_IPLAYER, AudioIPlayerIface))
#define AUDIO_IS_IPLAYER(obj) \
    (G_TYPE_CHECK_INSTANCE_TYPE((obj), AUDIO_TYPE_IPLAYER))
#define AUDIO_IPLAYER_GET_CLASS(obj) \
    (G_TYPE_INSTANCE_GET_INTERFACE((obj), AUDIO_TYPE_IPLAYER, AudioIPlayerIface))
#define AUDIO_IPLAYER_GET_INTERFACE(obj) \
    (G_TYPE_INSTANCE_GET_INTERFACE((obj), AUDIO_TYPE_IPLAYER, AudioIPlayerIface))

/* UserCode header_bottom { */

/* } UserCode */

G_END_DECLS

#endif

