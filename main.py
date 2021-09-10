# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import sys
    from pathlib import Path, PureWindowsPath
    from utils.utils import Utils
    from utils import get_file_class

    obj = Utils(4)
    for arg in sys.argv[1:]:
        if "=" in arg:
            key, value = arg.split("=")
            if key == "string":
                string = value.strip()
                # print(obj.reverse_string(obj, string))
                # print(obj.reverse_string(string))
                obj.str_rev_using_queue(string)
            elif key == "file":
                path = Path(__file__).parent.absolute().joinpath('Logs')
                file_ = path.joinpath(value)
                cls = get_file_class(file_.suffix)
                if cls is not None:
                    # cls.write(file_)
                    cls.read(file_)
                else:
                    raise NotImplementedError('csv and json only supports')
            else:
                pass
        elif arg.isdigit():
            print(obj.catch_signal(int(arg)))
        elif arg.__contains__("/"):
            path_ = PureWindowsPath(arg)
            print(obj.is_directory_exist(path_))
        else:
            print(f"no operations defined!...{sys.argv}")
            print("I'm done")
            exit(1)
