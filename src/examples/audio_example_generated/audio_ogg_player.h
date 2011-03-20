/* This file has been generated automatically by GObjectCreator
* (see http://www.bollmeier.de/GObjectCreator for details).
* Please modify user sections only!
*/

#ifndef AUDIOOGGPLAYER_H
#define AUDIOOGGPLAYER_H

#include "glib-object.h"

G_BEGIN_DECLS

#include "audio_iplayer.h"

/* UserCode header_top { */

    /* add includes here... */

/* } UserCode */

typedef struct _AudioOggPlayerPriv AudioOggPlayerPriv;

typedef struct _AudioOggPlayer {
    
    GObject super;
    
    /* UserCode public_members { */
    
        /* add further public members...*/
    
    /* } UserCode */
    
    AudioOggPlayerPriv* priv;
    
} AudioOggPlayer;

/* ===== Class ===== */

typedef struct _AudioOggPlayerClass {

    GObjectClass super_class;

} AudioOggPlayerClass;

GType audio_oggplay_get_type();

/* ===== instance creation ===== */

AudioOggPlayer*
audio_oggplay_new();

/* ===== Properties ======
* status <-- player's status (read)
*/

/* ===== macros ===== */

#define AUDIO_TYPE_OGG_PLAYER \
    (audio_oggplay_get_type())
#define AUDIO_OGG_PLAYER(obj) \
    (G_TYPE_CHECK_INSTANCE_CAST((obj), AUDIO_TYPE_OGG_PLAYER, AudioOggPlayer))
#define AUDIO_OGG_PLAYER_CLASS(cls) \
    (G_TYPE_CHECK_CLASS_CAST((cls), AUDIO_TYPE_OGG_PLAYER, AudioOggPlayerClass))
#define AUDIO_IS_OGG_PLAYER(obj) \
    (G_TYPE_CHECK_INSTANCE_TYPE((obj), AUDIO_TYPE_OGG_PLAYER))
#define AUDIO_IS_OGG_PLAYER_CLASS(cls) \
    (G_TYPE_CHECK_CLASS_TYPE((cls), AUDIO_TYPE_OGG_PLAYER))
#define AUDIO_OGG_PLAYER_GET_CLASS(obj) \
    (G_TYPE_INSTANCE_GET_CLASS((obj), AUDIO_TYPE_OGG_PLAYER, AudioOggPlayerClass))

/* UserCode header_bottom { */

/* } UserCode */

G_END_DECLS

#endif

