# python_crawler

**All codes are for leaning use only**

this warehouse mainly provides some simple crawler scripts.

# List

## 一、 [liepin_crawler](https://github.com/jingluoguo/python_crawler/liepin_crawler)

> Get job information from www.liepin.com.

### 1 How to use

```bash
# enter the direction
cd liepin_crawler

# install packages
pip install requirements.txt

# python liepin_crawler [position] [page]
# eg.
python liepin_crawler python 1
```

### 2 How to achieve

1. Get job title and page count based on command line arguments. Eg.  `python liepn_crawler java 1`
2. Obtian the required class tags through www.liepin.com.
3. Parse class tags with BeautifulSoup4.
4. Get the required data