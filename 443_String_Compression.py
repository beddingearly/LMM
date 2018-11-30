#coding=utf-8
'''
@Time    : 2018/11/28 15:33
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : 443_String_Compression.py
@Software: PyCharm

给定一组字符，使用原地算法将其压缩。压缩后的长度必须始终小于或等于原数组长度。

数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。在完成原地修改输入数组后，返回数组的新长度。

进阶：
你能否仅使用O(1) 空间解决问题？



示例 1：

输入：
["a","a","b","b","c","c","c"]

输出：
返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]

说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。

示例 2：

输入：
["a"]

输出：
返回1，输入数组的前1个字符应该是：["a"]

说明：
没有任何字符串被替代。

示例 3：

输入：
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

输出：
返回4，输入数组的前4个字符应该是：["a","b","1","2"]。

说明：
由于字符"a"不重复，所以不会被压缩。"bbbbbbbbbbbb"被“b12”替代。
注意每个数字在数组中都有它自己的位置。

注意：

    所有字符都有一个ASCII值在[35, 126]区间内。
    1 <= len(chars) <= 1000。
'''


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        base = chars[0]
        count = 1
        pos = 0
        for i in range(1, len(chars), 1):
            if chars[i] != base:
                base = chars[i]
                pos += 1
                if count == 1 and i != len(chars)-1:
                    chars[pos] = base
                    continue
                elif count != 1:
                    for j in str(count):
                        chars[pos] = j
                        pos += 1
                    count = 1

                chars[pos] = base
            elif chars[i] == base:
                count += 1
                if i == len(chars)-1:  # 最后一个
                    chars[pos] = chars[i]
                    pos += 1
                    if count == 1:
                        continue
                    for i in str(count):
                        chars[pos] = i
                        pos += 1
        if pos == 0:
            return chars[:1]
        return chars[:pos]

if __name__ == '__main__':
    a = Solution()
    print a.compress(["a","b","c","d","e","f","g","g","g","g","g","g","g","g","g","g","g","g","a","b","c"])