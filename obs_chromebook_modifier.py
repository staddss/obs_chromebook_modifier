#!/usr/bin/python3

# 置換対象のバイナリファイルのパス
file_path = "/usr/bin/obs"

# 置換するバイト列
search_bytes  = b'/opt/google/cros-containers'
replace_bytes = b'/00000000000000000000000000'

# バイナリファイルを読み込む
with open(file_path, 'rb') as file:
    binary_data = file.read()

# バイナリデータ内の特定の文字列を置換する
mod_data = binary_data.replace(search_bytes, replace_bytes)

# 変更されたバイナリデータをファイルに書き戻す
with open(file_path, 'wb') as file:
    file.write(mod_data)
