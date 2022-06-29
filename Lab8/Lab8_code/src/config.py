GL_VERSION = (3, 3)
WINDOW_TITLE = 'WMM Lab8'

FRAGMENT_SHADER_EXTENSION = ['.frag']
VERTEX_SHADER_EXTENSION = ['.vert']
GEOMETRY_SHADER_EXTENSION = ['.geom']


def get_supported_extensions():
    return [
        *GEOMETRY_SHADER_EXTENSION,
        *VERTEX_SHADER_EXTENSION,
        *FRAGMENT_SHADER_EXTENSION
    ]
