import os
import tarfile

current_path = os.getcwd()
cur_dir_file_names = os.listdir(current_path)
print(current_path)
for cur_dir_file_name in cur_dir_file_names:
    if os.path.isdir(cur_dir_file_name):
        print(cur_dir_file_name + "  DIR is skipped!!!")
    else:
        print(cur_dir_file_name)
        (fname, fextension) = os.path.splitext(cur_dir_file_name)
        if fextension != ".tar":
            print(cur_dir_file_name + "  FILE is skipped!!!")
        else:
            path = current_path + "/" + fname
            if os.path.exists(path):
                pass
            else:
                tar = tarfile.open(cur_dir_file_name)
                names = tar.getnames()
                for name in names:
                    tar.extract(name, path)
                tar.close()
        print(cur_dir_file_name + "  unzip is done!!!")