def read_data(path):
    f_lines = []
    f_names = ['ID','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','class']
    with open(path) as f_stream:
        for line in f_stream:
            f_lines.append(line)
    res_data = []
    for line in f_lines:
        col_vals = line.strip().split(',')
        line_dict = {}
        for key,value in zip(f_names,col_vals):
            line_dict[key] = float(value)
        res_data.append(line_dict)
    return res_data
