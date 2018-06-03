
base62table = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def to_base62(urlint):
    result=''
    if urlint >62:
        while (urlint > 62):
            m = urlint / 62
            n = urlint % 62
            urlint = int(m)
            n = int(n)
            result = result + base62table[n]

        if urlint > 0:
            result = result + base62table[urlint]
    else :
        result=base62table[urlint]
    return result


def to_prime_num(org_url):
    hash_num = 65521
    hash_str = b'apeach_is_most_cute_peach_in_the_world'
    key = org_url.encode()+hash_str
    for c in key:
        hash_num = ((hash_num<<5)+hash_num)+c
    return hash_num

def make_short(org_url):
    source = org_url
    m = to_prime_num(source)
    return to_base62(m)




if __name__ == '__main__':
    print(make_short("www.naver.com"))

