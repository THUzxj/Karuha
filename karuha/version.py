from importlib.metadata import distribution

APP_VERSION = __version__ = "0.2.0b3"
LIB_VERSION = distribution("tinode_grpc").version
