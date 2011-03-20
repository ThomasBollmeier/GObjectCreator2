/* This file has been generated automatically by GObjectCreator
* (see http://www.bollmeier.de/GObjectCreator for details).
* Please modify user sections only!
*/

#include "audio_iplayer.h"

/* UserCode source_top { */

#include "audio_iplayer_marshaller.h"
/* add further includes... */

/* } UserCode */

/* ===== signals ===== */

enum {
    STARTED,
    PAUSED,
    STOPPED,
    LAST_SIGNAL
};

static guint audio_iplayer_signals[LAST_SIGNAL] = {0};

/* ===== initialization & finalization ===== */

static void
audio_iplayer_base_init(AudioIPlayerIface* iface) {
    
    static gboolean initialized = FALSE;
    
    if (initialized)
        return;
    
    /* add signals */
    
    /* UserCode signal_started { */
    
    audio_iplayer_signals[STARTED] = g_signal_new("started",
        AUDIO_TYPE_IPLAYER,
        G_SIGNAL_RUN_LAST|G_SIGNAL_DETAILED,
        G_STRUCT_OFFSET(AudioIPlayerIface, started),
        NULL, /* accumulator */
        NULL,
        audio_iplayer_VOID__STRING_BOOLEAN,
        G_TYPE_NONE,
        2,
        G_TYPE_STRING,
        G_TYPE_BOOLEAN
        );
    
    /* } UserCode */
    
    /* UserCode signal_paused { */
    
    audio_iplayer_signals[PAUSED] = g_signal_new("paused",
        AUDIO_TYPE_IPLAYER,
        G_SIGNAL_RUN_LAST|G_SIGNAL_DETAILED,
        G_STRUCT_OFFSET(AudioIPlayerIface, paused),
        NULL, /* accumulator */
        NULL,
        audio_iplayer_VOID__STRING,
        G_TYPE_NONE,
        1,
        G_TYPE_STRING
        );
    
    /* } UserCode */
    
    /* UserCode signal_stopped { */
    
    audio_iplayer_signals[STOPPED] = g_signal_new("stopped",
        AUDIO_TYPE_IPLAYER,
        G_SIGNAL_RUN_LAST|G_SIGNAL_DETAILED,
        G_STRUCT_OFFSET(AudioIPlayerIface, stopped),
        NULL, /* accumulator */
        NULL,
        audio_iplayer_VOID__STRING,
        G_TYPE_NONE,
        1,
        G_TYPE_STRING
        );
    
    /* } UserCode */
    
    /* UserCode interface_init { */
    
        /* further initializations... */
    
    /* } UserCode */
    
    initialized = TRUE;
    
}

static void
audio_iplayer_base_finalize(AudioIPlayerIface* iface) {
    
    static gboolean finalized = FALSE;
    
    if (finalized)
        return;
    
    /* UserCode interface_finalize { */
    
        /* do some final stuff... */
    
    /* } UserCode */
    
    finalized = TRUE;
    
}

GType
audio_iplayer_get_type() {
    
    static GType type_id = 0;
    
    if (type_id == 0) {
        
        const GTypeInfo audio_iplayer_info = {
            sizeof(AudioIPlayerIface),
            (GBaseInitFunc) audio_iplayer_base_init,
            (GBaseFinalizeFunc) audio_iplayer_base_finalize
            };
        
        type_id = g_type_register_static(
            G_TYPE_INTERFACE,
            "AudioIPlayer",
            &audio_iplayer_info,
            0
            );
            
        /* all classes are allowed to implement this interface: */
        g_type_interface_add_prerequisite(type_id, G_TYPE_OBJECT);
        
    }
    
    return type_id;
    
}

/* ===== methods ===== */

void
audio_iplayer_start(AudioIPlayer* self, const gchar* track_uri, AudioFormat format, 
    GError** error) {
    
    AudioIPlayerIface* iface = AUDIO_IPLAYER_GET_INTERFACE(self);
    
    iface->start(self, track_uri, format, error);
    
}

gboolean
audio_iplayer_pause(AudioIPlayer* self) {
    
    AudioIPlayerIface* iface = AUDIO_IPLAYER_GET_INTERFACE(self);
    
    return iface->pause(self);
    
}

gboolean
audio_iplayer_stop(AudioIPlayer* self) {
    
    AudioIPlayerIface* iface = AUDIO_IPLAYER_GET_INTERFACE(self);
    
    return iface->stop(self);
    
}

/* UserCode source_bottom { */

/* } UserCode */

