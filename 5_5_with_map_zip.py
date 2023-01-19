# name1='poly.txt'
# name2='poly1.txt'

# with open(name1, 'r', encoding='utf-8') as m_file1, \
#             open(name2, 'r', encoding='utf-8') as m_file2:
      
            # str1 = m_file1.readlines()
            # str2 = m_file2.readlines()
            
str1='9*x^5+4*x^4+3*x^2+7*x+5=0'            
str2='4*x^5+7*x^4+9*x^2+2*x+6=0'  

print(str1)
print(str2)

def str_to_list(strA):
    strA = ''.join(strA)
    str10=strA.replace('*x', '').replace('^', '').replace('+', '').replace('=', '')
    m_list = list(map(int, str10))
    x=len(m_list)-2
    m_list.insert(x, 1)
    return m_list

print(str_to_list(str1))
print(str_to_list(str2))


def list_of_key(m_list):
    new_list = []
    for i in range(1, len(m_list)+1,2):
        new_list.append(m_list[i])
        
    return new_list


def list_of_means(m_list):
    new_list = []
    for i in range(0, len(m_list), 2):
      
            new_list.append(m_list[i])
           
                
    return new_list

def dict_poly(list1, list2):
    dict_poly=dict(zip(list1, list2))
    return dict_poly
    
def sum_poly(dict1, dict2):
    sum=0
    alist=[]
    for k, v in dict1.items():
        if dict1.keys()==dict2.keys():
            sum=dict1.get(k)+dict2.get(k)
            alist.append(sum)
            sum=0
    return(alist)        
            
def polinomial(alist, alist1):
    poly_list=''
    # with open('sum_poly1.txt', 'a', encoding='utf-8') as m_file3:
    #     poly_list=''
    for i in range(0, len(alist)):
        value = alist1[i]
        s=alist[i]
        if alist[i]>1:
            poly_list+=f"{value} *x^{s} + "
        elif alist[i]==1:
            poly_list+=f"{value} *x + "
        elif alist[i]==0:
            poly_list+=f"{value} = 0"
    
    return poly_list        


# m_list1 = str_to_list(str1)
# m_list2 = str_to_list(str2)
# l_o_k = list_of_key(str_to_list(str1))
# print(l_o_k)
# l_o_k1 = list_of_key(str_to_list(str2))
# print(l_o_k1)
# l_o_m = list_of_means(str_to_list(str1))
# print(l_o_m)
# l_o_m1 = list_of_means(str_to_list(str2))
# print(l_o_m1)
m_d = dict_poly(list_of_key(str_to_list(str1)), list_of_means(str_to_list(str1)))
# print(m_d)
m_d1 = dict_poly(list_of_key(str_to_list(str2)), list_of_means(str_to_list(str2)))
# print(m_d1)

s_p =sum_poly(m_d, m_d1)
print(s_p)

# s_p =sum_poly(l_o_k, l_o_k1, l_o_m, l_o_m1)
# # print(s_p)

poly_list3 = polinomial(list_of_key(str_to_list(str1)), s_p)
print(poly_list3)

# with open('sum_poly1.txt', 'a', encoding='utf-8') as m_file3:
#     m_file3.write(poly_list3)
