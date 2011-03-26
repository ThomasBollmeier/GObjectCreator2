/* This file has been generated automatically by GObjectCreator
* (see http://www.bollmeier.de/GObjectCreator for details).
* Please modify user sections only!
*/

#include "audio_ogg_player_prot.h"

/* UserCode source_top { */

#include "audio_error.h"

/* } UserCode */

struct _AudioOggPlayerPriv {
    AudioPlayerStatus status;
    gchar* current;
};

/* ===== interface methods (definition) ===== */

/* IPlayer->start */
static void
audio_oggplay_start_im(AudioIPlayer* obj, const gchar* track_uri, AudioFormat format, 
    GError** error);

/* IPlayer->pause */
static gboolean
audio_oggplay_pause_im(AudioIPlayer* obj);

/* IPlayer->stop */
static gboolean
audio_oggplay_stop_im(AudioIPlayer* obj);

/* UserCode private_methods { */

    /* define further methods...*/

/* } UserCode */

/* ===== properties ===== */

enum {
    PROP_STATUS = 1
};

static void
audio_oggplay_set_property(
    GObject* object,
    guint property_id,
    const GValue* value,
    GParamSpec* param_spec
    );

static void
audio_oggplay_get_property(
    GObject* object,
    guint property_id,
    GValue* value,
    GParamSpec* param_spec
    );

/* ===== class initialization ===== */

static void
audio_oggplay_class_init(AudioOggPlayerClass* cls) {
    
    GObjectClass* gobj_class = G_OBJECT_CLASS(cls);
    GParamSpec* pspec_status;
    
    /* Register structure holding private attributes: */
    g_type_class_add_private (cls, sizeof(AudioOggPlayerPriv));
    
    /* UserCode class_init { */
    
        /* init class members ... */
    
    /* } UserCode */
    
    gobj_class->dispose = audio_oggplay_dispose;
    gobj_class->finalize = audio_oggplay_finalize;
    gobj_class->set_property = audio_oggplay_set_property;
    gobj_class->get_property = audio_oggplay_get_property;
    
    /* install properties */
    
    /* UserCode property_reg_status { */
    
    pspec_status = g_param_spec_enum(
        "status",
        "player's status",
        "player's status",
        AUDIO_TYPE_PLAYER_STATUS,
        AUDIO_PLAYER_STATUS_READY,
        G_PARAM_READABLE|G_PARAM_STATIC_STRINGS
        );
    g_object_class_install_property(
        gobj_class,
        PROP_STATUS,
        pspec_status
        );
    
    /* } UserCode */
    
    
}

/* ===== interfaces ===== */

static void
audio_oggplay_audio_iplayer_init(AudioIPlayerIface* iface) {
    
    iface->start = audio_oggplay_start_im;
    iface->pause = audio_oggplay_pause_im;
    iface->stop = audio_oggplay_stop_im;
    
}

/* UserCode external_interfaces_init { */

    /* Initialize implementation of unmodeled interfaces... */

/* } UserCode */

/* ===== type initialization ==== */

static void
audio_oggplay_instance_init(
    GTypeInstance* obj,
    gpointer cls
    ) {
    
    AudioOggPlayer* self = AUDIO_OGG_PLAYER(obj);
    
    self->priv = G_TYPE_INSTANCE_GET_PRIVATE(
        self,
        AUDIO_TYPE_OGG_PLAYER,
        AudioOggPlayerPriv
        );
    
    /* UserCode instance_init { */
    
    /* init members, allocate memory, etc ... */
    self->priv->current = NULL;
    self->priv->status = AUDIO_PLAYER_STATUS_READY;

    /* } UserCode */
    
}

GType audio_oggplay_get_type() {

    static type_id = 0;
    
    if (type_id == 0) {
        
        const GTypeInfo class_info = {
            sizeof(AudioOggPlayerClass),
            NULL, /* base initializer */
            NULL, /* base finalizer */
            (GClassInitFunc) audio_oggplay_class_init,
            NULL, /* class finalizer */
            NULL, /* class data */
            sizeof(AudioOggPlayer),
            0,
            audio_oggplay_instance_init
            };
        
        const GInterfaceInfo audio_iplayer_info = {
            (GInterfaceInitFunc) audio_oggplay_audio_iplayer_init,
            NULL,
            NULL
            };
        
        type_id = g_type_register_static(
            G_TYPE_OBJECT,
            "AudioOggPlayer",
            &class_info,
            0
            );
        
        g_type_add_interface_static(
            type_id,
            AUDIO_TYPE_IPLAYER,
            &audio_iplayer_info
            );
        
    /* UserCode external_interfaces_register { */
    
        /* Register implementation of unmodeled interfaces... */
    
    /* } UserCode */
    
    }
    
    return type_id;

}

/* ===== implementation ===== */

AudioOggPlayer*
audio_oggplay_new() {

    AudioOggPlayer* obj = g_object_new(AUDIO_TYPE_OGG_PLAYER, NULL);
    
    audio_oggplay_init(obj);
    
    return obj;

}

void
audio_oggplay_init(AudioOggPlayer* self) {
/* UserCode constructor { */

    /* == init your members == */

/* } UserCode */
}

void
audio_oggplay_dispose(GObject* obj) {
/* UserCode dispose { */

    /* unref ...*/

/* } UserCode */
}

void
audio_oggplay_finalize(GObject* obj){
    
    /* UserCode finalize { */
    
    AudioOggPlayer* self = AUDIO_OGG_PLAYER(obj);

    if (self->priv->current)
    	g_free(self->priv->current);
    
    /* } UserCode */
    
}

void
audio_oggplay_set_property(
    GObject* obj,
    guint property_id,
    const GValue* value,
    GParamSpec* param_spec
    ) {
    
    G_OBJECT_WARN_INVALID_PROPERTY_ID(
        obj,
        property_id,
        param_spec
        );

}

void
audio_oggplay_get_property(
    GObject* obj,
    guint property_id,
    GValue* value,
    GParamSpec* param_spec
    ) {
    
    AudioOggPlayer* self = AUDIO_OGG_PLAYER(obj);
    
    /* UserCode property_get_data_decls { */
    
        /* data declarations...*/
    
    /* } UserCode */
    
    switch (property_id) {
        
        case PROP_STATUS:
            /* UserCode property_get_status { */
            g_value_set_enum(value, self->priv->status);
            /* } UserCode */
            break;
        
        default:
            G_OBJECT_WARN_INVALID_PROPERTY_ID(
                obj,
                property_id,
                param_spec
                );
        
    }

}

/* ===== interface methods (implementation) ===== */

static void
audio_oggplay_start_im(AudioIPlayer* obj, const gchar* track_uri, AudioFormat format, 
    GError** error) {
/* UserCode IPlayer_start { */

	AudioOggPlayer* self = AUDIO_OGG_PLAYER(obj);
	gboolean resumed = FALSE;

	if (format != AUDIO_FORMAT_OGG_VORBIS) {

		if (error) {
			*error = g_error_new(
					AUDIO_ERROR,
					AUDIO_ERROR_UNKNOWN_FORMAT,
					"audio format of file \"%s\" unknown",
					track_uri
					);
		}

		return;

	}

	switch (self->priv->status) {
	case AUDIO_PLAYER_STATUS_READY:
		if (self->priv->current)
			g_free(self->priv->current);
		self->priv->current = g_strdup(track_uri);
		self->priv->status = AUDIO_PLAYER_STATUS_PLAYING;
		break;
	default:
		if (error) {
			*error = g_error_new(
					AUDIO_ERROR,
					AUDIO_ERROR_INVALID_STATUS,
					"player is not ready"
					);
		}
		return;
	}

	g_signal_emit_by_name(self, "started", self->priv->current, resumed);

/* } UserCode */
}

static gboolean
audio_oggplay_pause_im(AudioIPlayer* obj) {
/* UserCode IPlayer_pause { */

	AudioOggPlayer* self = AUDIO_OGG_PLAYER(obj);
	gboolean resumed;

	switch (self->priv->status) {
	case AUDIO_PLAYER_STATUS_READY:
		/* nothing to do */
		break;
	case AUDIO_PLAYER_STATUS_PLAYING:
		self->priv->status = AUDIO_PLAYER_STATUS_PAUSED;
		g_signal_emit_by_name(self, "paused", self->priv->current);
		break;
	case AUDIO_PLAYER_STATUS_PAUSED:
		self->priv->status = AUDIO_PLAYER_STATUS_PLAYING;
		resumed = TRUE;
		g_signal_emit_by_name(self, "started", self->priv->current, resumed);
		break;
	}

/* } UserCode */
}

static gboolean
audio_oggplay_stop_im(AudioIPlayer* obj) {
/* UserCode IPlayer_stop { */

	AudioOggPlayer* self = AUDIO_OGG_PLAYER(obj);
	gchar* tmp = NULL;

	if (self->priv->current) {
		tmp = self->priv->current;
		self->priv->current = NULL;
	}

	self->priv->status = AUDIO_PLAYER_STATUS_READY;

	g_signal_emit_by_name(self, "stopped", tmp);

	if (tmp)
		g_free(tmp);

/* } UserCode */
}

/* UserCode source_bottom { */

/* } UserCode */

