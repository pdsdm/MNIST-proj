def csv_convert_list(train_csv, test_csv):
    train_file = open(train_csv, 'r')  
    train_list = train_file.readlines()
    train_file.close()

    test_file = open(test_csv, 'r')
    test_list = test_file.readlines()
    test_file.close()

    return train_list, test_list