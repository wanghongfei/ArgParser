## ArgParser - 命令行参数解析器
编写ArgParser的原因是python自带的getopt模块中，当指定`p:`模式串时如果`-p`参数不存在则会报异常,
这样就无法指定可选参数。ArgParser指定的所有参数都是可选的, 即当参数项不存在时不会报错

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
