import os
from bs4 import BeautifulSoup

"""
讀檔案-> 找出 <li><a href="https://tw.pycon.org/2016/zh-hant/dashboard/" target="_blank"><span class="em">控制面板</span></a></li>
移除-> 寫入 -> happy
"""
data = '<span class="em">控制面板</span></a>'
en_data = '<span class="em">Dashboard</span></a>'


def rm_content(page='index.html', status=None):
    htmldoc = open(page, 'r+')
    soup = BeautifulSoup(htmldoc, "html.parser")
    try:
        for i in range(0, len(soup.ul.find_all('li'))):
            if str(data) in str(soup.ul.find_all('li')[i]):
                status = str(soup.ul.find_all('li')[i])
                soup.ul.find_all('li')[i].replaceWith('')
            elif str(en_data) in str(soup.ul.find_all('li')[i]):
                status = str(soup.ul.find_all('li')[i])
                soup.ul.find_all('li')[i].replaceWith('')
        htmldoc.close()
    except Exception as e:
        pass

    if status != None:
        html = soup.prettify("utf-8")
        with open(page, "wb") as fp:
            fp.write(html)
    return status


def main():
    with open('log.txt', 'a') as fp:
        for root, dirs, files in os.walk(os.getcwd()):
            for f in files:
                if os.path.splitext(f)[-1] == '.html':
                    print(os.path.join(root, f))
                    r = rm_content(page=os.path.join(root, f))
                    if r != None: 
                        fp.writelines(os.path.join(root, f)+"\n")
    fp.close()


if __name__ == '__main__':
    main()