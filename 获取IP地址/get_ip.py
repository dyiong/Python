from bs4 import BeautifulSoup
import requests


# 得到ip地址
def get_ip(subdomain):
    global url
    url1 = url + subdomain
    print(url1)
    response = requests.get(url1, headers=headers)
    print(response)
    html = response.text
    try:
        bs = BeautifulSoup(html, "html.parser")
        results = bs.select('.Whwtdhalf')[4:]
        # print(results)
        ip_file = open('url_ip.txt', 'a+', encoding='utf-8')
        # url+ip+地址
        for result in results:
            # print(result.text)
            ip_file.write(result.text + ' ')
        ip_file.write('\n')
        ip_file.close()
        # ip
        # print(results[1].text)
        with open('ip.txt', 'a+') as f:
            # print(results[1].text)
            f.write(results[1].text + '\n')
    except:
        print("解析失败！")


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Origin": "http://ip.tool.chinaz.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://ip.tool.chinaz.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    url = "http://ip.tool.chinaz.com/"

    # get_ip("www.xq110.hpu.edu.cn")
    subdomain_file = open('./subdomain.txt', 'r')
    subdomains = subdomain_file.readlines()
    # print(subdomains)
    for subdomain in subdomains:
        subdomain = subdomain.strip()
        # print(subdomain)
        get_ip(subdomain)
    subdomain_file.close()
