from bs4 import BeautifulSoup
import requests


# 得到子域名
def get_subdomain(page):
    global url
    global headers
    global domain
    url2 = url + "domain=" + domain + "&page=" + str(page)
    # print(url2)
    response = requests.get(url2, headers=headers)
    html = response.text
    bs = BeautifulSoup(html, "html.parser")
    # 子域名列表
    subdomains = bs.select('.subdomain')
    for i in subdomains:
        subdomain = i.a.text
        print(subdomain)
        with open('./subdomain.txt', 'a+') as f:
            f.write(subdomain + '\n')


# 得到页面数据
def get_pages_nums(domain):
    global url
    global headers
    url1 = url + "domain=" + str(domain)
    response = requests.get(url1, headers=headers)
    html = response.text
    try:
        bs = BeautifulSoup(html, "html.parser")
        nums = int(bs.select('.col-gray02')[0].text[1])
    except:
        nums = None
        print("查询失败！")

    # print(bs.select('.col-gray02')[0].text[1])
    return nums


if __name__ == '__main__':
    url = "https://tool.chinaz.com/subdomain?"

    headers = {
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://tool.chinaz.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    domain = input("请输入域名，如（bilibili.com）: ")
    pages_nums = get_pages_nums(domain)
    print("总的页面数据: " + str(pages_nums))
    if pages_nums:
        for i in range(0, pages_nums):
            # print(i+1)
            get_subdomain(i + 1)

    input("任意键关闭...")
