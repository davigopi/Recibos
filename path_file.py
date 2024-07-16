import os
from pathlib import Path


class Path_file:
    def __init__(self, *args, **kwargs) -> None:
        self.path_source = Path(__file__).parent
        if 'components' in self.path_source.parts or 'tables' in self.path_source.parts:  # noqa
            self.path_source = Path(__file__).parent.parent
        self.path_components = self.path_source / 'components'
        self.path_tables = self.path_source / 'tables'
        if not os.path.exists(self.path_components):
            os.makedirs(self.path_tables)
        if not os.path.exists(self.path_tables):
            os.makedirs(self.path_tables)

    def path_file_create(self, path_origin, file_origin):
        if path_origin == 'components':
            path_destination = self.path_components
        elif path_origin == 'tables':
            path_destination = self.path_tables
        else:
            path_destination = self.path_source
        path_file_ = path_destination / file_origin
        return (path_file_)
