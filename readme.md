## ArgParser - 命令行参数解析器

- 使用方法
```
    # 第二个参数为getopt风格的模式串
    parser = ArgParser(sys.argv[1:], 'p:t:')
    result = parser.parse()
    # result是一个元组列表, 每个元组的第一个元素为参数名，第二个元素为参数值

    # 对于 script.py -p 8080 -t 10
    # result为 [('-p', '8080'), ('-t', '10')]
    # 如果缺少参数值，扔ArgParserException
```
