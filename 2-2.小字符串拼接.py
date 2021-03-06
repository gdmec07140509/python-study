'''
    问题：如何将多个小字符串拼接成一个大的字符串？

    案例：在设计某网络程序时，我们自定义了一个基于UDP的网络协议，
        按照固定次序向服务器传递一系列参数:
        hwDetect:           "<0112>"
        gxDepthBits:        "<32>"
        gxResolution:       "<1024x768>"
        gxRefresh:          "<60>"
        fullAlpha:          "<1>"
        lodDist:            "<100.0>"
        DistCull:           "<500.0>"
        在程序中我们将各个参数按次序收集到列表中:
        ["<0112>", "<32>", "<1024x768>", "<60>", "<1>", "<100.0>", "<500.0>"]
        最终我们要把各个参数拼接成-个数据报进行发送.
        "<0112><32><1024x768><60><1><100.0><500.0>"

    解决：方法一:迭代列表，连续使用'+'操怍依次拼接每一个字符串.
        方法二:使用str.join()方法，更加快速的拼接列表中所有字符串，

'''

# 浪费性能
# s = ''
pl = ["<0112>", "<32>", "<1024x768>", "<60>", "<1>", "<100.0>", "<500.0>"]
# for p in pl:
#     s += p
#     print(s)

# []  列表的方式，也存在性能的开销，所以 换成生成器的
# 生成器 的方式  ()
s = ''.join(str(p) for p in pl)
print(s)