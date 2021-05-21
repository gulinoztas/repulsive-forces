
def excel(table,function,num_var,set_size): #exports excel file
    table.to_excel(r'C:\Users\Pau\Google Drive\ref\{}{}{}set.xlsx'.format(function,num_var,set_size), index=None, header=True)
    return "tablo"