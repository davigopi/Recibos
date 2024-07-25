import os
from pathlib import Path


class Path_file:
    def __init__(self, *args, **kwargs) -> None:

        self.path_source = Path(__file__).parent

        if 'components' in self.path_source.parts or 'tables' in self.path_source.parts:  # noqa
            self.path_source = Path(__file__).parent.parent
        self.path_components = self.path_source / 'components'
        self.path_tables = self.path_source / 'tables'
        self.path_documentos = "~/Documents"
        self.path_home = "~"
        self.path_desktop = "~/Desktop"
        self.path_downloads = "~/Downloads"
        # self.path_home = "~/Music"
        # self.path_home = "~/Pictures"
        # self.path_home = "~/Videos"
        self.path_appdata = "APPDATA"
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
        new_folder = path_destination / file_origin
        return (new_folder)

    def path_file_create_user(self, path_user, path_origin, name_file):
        if path_user == 'Documentos':
            user_path = os.path.expanduser(self.path_documentos)
        elif path_user == 'Downloads':
            user_path = os.path.expanduser(self.path_downloads)
        elif path_user == 'Desktop':
            user_path = os.path.expanduser(self.path_desktop)
        elif path_user == 'Appdata':
            user_path = os.getenv(self.path_appdata)
        else:
            user_path = os.path.expanduser(self.path_home)
        if not user_path:
            raise ValueError(f"O diretório '{path_user}' não é válido.")
        new_folder = os.path.join(user_path, path_origin)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        path_file = os.path.join(new_folder, name_file)
        if not os.path.exists(path_file):
            open(path_file, 'w').close()
        return path_file
