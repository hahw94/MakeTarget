def save_data(data, filename ,save_path = None):
    save_data = data
    np.save(save_path + filename, save_data)