# coding=UTF-8
import sys

class ArgParserException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


# 解析命令行参数
class ArgParser:
    def __init__(self, args, mod):
        self.args = args
        self.mod = mod
        self.tokens = []

        self.__parse_mode__()

    # 解析mod参数
    # mod: q:t:
    def __parse_mode__(self):
        LEN = len(self.mod)
        for ix in range(0, LEN):
            ch = self.mod[ix]
            if ch != ":":
                if ix != LEN - 1 and self.mod[ix + 1] == ":":
                    self.tokens.append(self.Token("-%s" % ch, True))
                else:
                    self.tokens.append(self.Token("-%s" % ch, False))

    # return: 元组list, 元组第一个元素为参数名, 第二个元素为参数值
    def parse(self):
        result = []

        LEN = len(self.args)

        for ix in range(0, LEN):
            arg = self.args[ix]

            if arg.startswith("-"):
                example = self.Token(arg)
                pos = self.tokens.index(example)
                # 判断参数是否是必须的
                if self.tokens[pos].required:
                    # 读取下一个参数
                    if ix == LEN - 1:
                        # 已经是最后一个参数了
                        raise ArgParserException('argument %s lacks of value' % arg)
                    next_arg = self.args[ix + 1]
                    # 如果下一个参数也是以-开头
                    # 说明这也不是参数值
                    if next_arg.startswith('-'):
                        raise ArgParserException('argument %s lacks of value' % arg)
                    result.append( (arg, next_arg) )

        return result



    class Token:
        # name: 参数名(-p)
        # requried: 是否是必须的
        def __init__(self, name, required=False):
            self.name = name
            self.required = required

        def __eq__(self, other):
            return self.name == other.name

if __name__ == '__main__':
    parser = ArgParser(sys.argv[1:], "p:t:")
    print parser.parse()
