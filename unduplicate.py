array = [{'title': 'name'}, {'title': 'agg'}]

def add_unique_dict(array, new_dict):
    for item in array:
        if item == new_dict:
            return array  # Jika dictionary sudah ada, langsung kembalikan array tanpa menambahkan
    array.append(new_dict)  # Jika tidak ada, tambahkan dictionary ke dalam array
    return array

# Menambahkan dictionary baru
new_dict = {'title': 'ass'}
add_unique_dict(array, new_dict)

print(array)
